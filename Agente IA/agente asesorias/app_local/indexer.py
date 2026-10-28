"""
Construye el índice vectorial a partir de todos los .md y .csv dentro de conocimiento/.
Se puede volver a ejecutar cada vez que se agreguen o actualicen documentos
(reconstruye el índice desde cero).
"""
import os
import re
import glob
import csv as csv_module

import pandas as pd
import chromadb
import ollama

from config import (
    CONOCIMIENTO_DIR,
    CHROMA_DIR,
    EMBED_MODEL,
    COLLECTION_NAME,
    MAX_CHARS_MD,
    ROWS_PER_CHUNK_CSV,
)


def _split_oversized_block(block: str, max_chars: int):
    """Último recurso: si un bloque (p. ej. una tabla markdown de una sola 'línea lógica'
    sin saltos dobles) sigue siendo más grande que max_chars, lo parte por líneas,
    acumulando hasta el límite en vez de cortar a la mitad de una palabra/fila.
    Si detecta que es una tabla markdown (encabezado + fila separadora '|---|'),
    repite esas 2 líneas de encabezado en cada sub-fragmento para que no se pierda
    el significado de las columnas."""
    if len(block) <= max_chars:
        return [block]

    lines = block.split("\n")
    header_lines = []
    if len(lines) >= 2 and "|" in lines[0] and re.match(r"^\s*\|?[\s:-]+\|", lines[1]):
        header_lines = lines[:2]
        lines = lines[2:]

    out = []
    header_prefix = ("\n".join(header_lines) + "\n") if header_lines else ""
    current = header_prefix
    base_len = len(header_prefix)
    for line in lines:
        if len(current) > base_len and len(current) + len(line) + 1 > max_chars:
            out.append(current.strip())
            current = header_prefix + line
        else:
            current = f"{current}\n{line}" if current.strip() else header_prefix + line
    if current.strip():
        out.append(current.strip())
    return out


def chunk_markdown(text: str, max_chars: int = MAX_CHARS_MD):
    """Parte un .md por encabezados (#, ##, ###) y luego por tamaño si una sección es muy larga."""
    sections = re.split(r"(?=^#{1,3} )", text, flags=re.MULTILINE)
    chunks = []
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        if len(sec) <= max_chars:
            chunks.append(sec)
            continue
        # Sección larga: partir por párrafos, acumulando hasta el límite
        paras = sec.split("\n\n")
        current = ""
        for p in paras:
            if current and len(current) + len(p) > max_chars:
                chunks.append(current.strip())
                current = p
            else:
                current = f"{current}\n\n{p}" if current else p
        if current.strip():
            chunks.append(current.strip())

    # Último recurso: si tras lo anterior algún fragmento sigue siendo enorme
    # (ej. una tabla markdown sin saltos de párrafo), partirlo por líneas.
    final_chunks = []
    for c in chunks:
        final_chunks.extend(_split_oversized_block(c, max_chars))
    return final_chunks


def _detect_separator(path: str) -> str:
    with open(path, encoding="utf-8-sig") as f:
        sample = f.readline()
    # Nuestros diccionarios de datos usan ';' como separador
    return ";" if sample.count(";") >= sample.count(",") else ","


def chunk_csv(path: str, rows_per_chunk: int = ROWS_PER_CHUNK_CSV):
    """Agrupa filas de CSV por 'Table Name'/'Tabla' si existe esa columna, para mantener
    juntos los campos de una misma tabla; si no, parte en bloques simples de N filas."""
    sep = _detect_separator(path)
    df = pd.read_csv(path, sep=sep, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    df.columns = [c.strip() for c in df.columns]

    group_col = None
    for c in df.columns:
        lc = c.lower()
        if "table" in lc or "tabla" in lc:
            group_col = c
            break

    chunks = []
    if group_col:
        for table_name, group in df.groupby(group_col):
            if not str(table_name).strip():
                continue
            records = group.to_dict(orient="records")
            for i in range(0, len(records), rows_per_chunk):
                sub = records[i : i + rows_per_chunk]
                header = f"Tabla: {table_name} (filas {i+1}-{i+len(sub)} de {len(records)})\n"
                body = "\n".join(
                    "; ".join(f"{k}={v}" for k, v in row.items() if str(v).strip())
                    for row in sub
                )
                chunks.append(header + body)
    else:
        for i in range(0, len(df), rows_per_chunk):
            sub = df.iloc[i : i + rows_per_chunk]
            chunks.append(sub.to_csv(index=False, sep=sep))
    return chunks


def build_index(progress_callback=None):
    """Reconstruye el índice completo. Devuelve el número total de fragmentos indexados."""
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = client.create_collection(COLLECTION_NAME)

    files = []
    for ext in ("*.md", "*.csv"):
        files.extend(glob.glob(os.path.join(CONOCIMIENTO_DIR, "**", ext), recursive=True))
    files.sort()

    total = len(files)
    doc_id = 0

    for i, path in enumerate(files):
        rel = os.path.relpath(path, CONOCIMIENTO_DIR)
        app_name = rel.split(os.sep)[0]

        try:
            if path.lower().endswith(".md"):
                with open(path, encoding="utf-8-sig") as f:
                    text = f.read()
                chunks = chunk_markdown(text)
            else:
                chunks = chunk_csv(path)
        except Exception as e:
            chunks = []
            print(f"[WARN] No se pudo procesar {rel}: {e}")

        for chunk in chunks:
            chunk = chunk.strip()
            if not chunk:
                continue
            emb = ollama.embeddings(model=EMBED_MODEL, prompt=chunk)["embedding"]
            collection.add(
                ids=[f"doc_{doc_id}"],
                embeddings=[emb],
                documents=[chunk],
                metadatas=[{"source": rel, "app": app_name}],
            )
            doc_id += 1

        if progress_callback:
            progress_callback(i + 1, total, rel)

    return doc_id


if __name__ == "__main__":
    print(f"Indexando documentos desde: {CONOCIMIENTO_DIR}")

    def cb(i, total, name):
        print(f"  [{i}/{total}] {name}")

    n = build_index(progress_callback=cb)
    print(f"Listo. {n} fragmentos indexados en {CHROMA_DIR}")
