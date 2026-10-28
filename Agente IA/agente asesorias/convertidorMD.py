"""Convierte los Word (.docx) y PDF de una aplicacion a Markdown (.md).

Las rutas ya estan configuradas. Estructura esperada:

    agente asesorias\\
      originales\\<aplicacion>\\      <- aqui van los Word y PDF de origen
      conocimiento\\<aplicacion>\\docs\\   <- aqui salen los .md convertidos
      herramientas\\convertidorMD.py

Uso (sin argumentos convierte Banktrade):
    python convertidorMD.py
    python convertidorMD.py banktrade
    python convertidorMD.py teyco
    python convertidorMD.py banktrade --sobrescribir

Requiere:
    pip install "markitdown[docx,pdf]"
"""
import argparse
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    sys.exit('Falta la libreria markitdown. Instalala con:  pip install "markitdown[docx,pdf]"')

# Carpeta raiz del proyecto
BASE = Path(r"C:\Users\Estef\Desktop\Agente IA\agente asesorias")

EXTENSIONES = {".docx", ".pdf"}
MIN_CARACTERES_PDF = 200
PATRON_IMAGEN = re.compile(r"!\[([^\]]*)\]\(data:image[^)]*\)")


def contar_imagenes_docx(ruta):
    # Un .docx es un zip; las imagenes y diagramas pegados viven en word/media/
    try:
        with zipfile.ZipFile(ruta) as z:
            return sum(1 for n in z.namelist() if n.startswith("word/media/"))
    except zipfile.BadZipFile:
        return 0


def limpiar(texto):
    # Las imagenes incrustadas salen como data URI gigante; se reemplazan por un marcador visible
    texto = PATRON_IMAGEN.sub(
        lambda m: "[IMAGEN: %s - DESCRIBIR EN TEXTO]" % (m.group(1) or "sin descripcion"),
        texto,
    )
    return re.sub(r"\n{3,}", "\n\n", texto).strip() + "\n"


def encabezado(origen, raiz):
    modificado = datetime.fromtimestamp(origen.stat().st_mtime).strftime("%Y-%m-%d")
    hoy = datetime.now().strftime("%Y-%m-%d")
    return (
        "> Convertido automaticamente. Revisar tablas y diagramas antes de usar.\n"
        "> Origen: %s\n"
        "> Fecha del original: %s\n"
        "> Fecha de conversion: %s\n\n"
        % (origen.relative_to(raiz).as_posix(), modificado, hoy)
    )


def main():
    ap = argparse.ArgumentParser(description="Convierte Word y PDF de una aplicacion a Markdown.")
    ap.add_argument(
        "aplicacion",
        nargs="?",
        default="banktrade",
        help="Nombre de la carpeta de la aplicacion (por defecto: banktrade)",
    )
    ap.add_argument(
        "--sobrescribir",
        action="store_true",
        help="Reemplaza los .md que ya existan (por defecto se respetan, por si ya los editaste)",
    )
    args = ap.parse_args()

    raiz = BASE / "originales" / args.aplicacion
    destino = BASE / "conocimiento" / args.aplicacion / "docs"

    if not raiz.is_dir():
        sys.exit(
            "No existe la carpeta de originales:\n  %s\n"
            "Crea la carpeta y copia ahi los Word y PDF de la aplicacion." % raiz
        )

    archivos = sorted(
        p
        for p in raiz.rglob("*")
        if p.is_file() and p.suffix.lower() in EXTENSIONES and not p.name.startswith("~$")
    )
    if not archivos:
        sys.exit("No se encontraron archivos .docx ni .pdf en:\n  %s" % raiz)

    print("Origen:  %s" % raiz)
    print("Destino: %s\n" % destino)

    conversor = MarkItDown()
    convertidos, omitidos, avisos, errores = [], [], [], []
    usados = set()

    for origen in archivos:
        rel = origen.relative_to(raiz)
        salida = (destino / rel).with_suffix(".md")
        if salida in usados:  # mismo nombre en .docx y .pdf
            salida = salida.with_name("%s_%s.md" % (origen.stem, origen.suffix[1:].lower()))
        usados.add(salida)

        if salida.exists() and not args.sobrescribir:
            omitidos.append(str(rel))
            continue

        try:
            texto = conversor.convert(str(origen)).text_content
        except Exception as e:  # un archivo danado no debe detener el resto
            errores.append("%s: %s" % (rel, e))
            continue

        if origen.suffix.lower() == ".pdf" and len(texto.strip()) < MIN_CARACTERES_PDF:
            avisos.append("%s: casi sin texto, probablemente PDF escaneado (requiere OCR)" % rel)
        if origen.suffix.lower() == ".docx":
            n = contar_imagenes_docx(origen)
            if n:
                avisos.append("%s: contiene %d imagen(es) o diagrama(s), describirlos en texto" % (rel, n))

        salida.parent.mkdir(parents=True, exist_ok=True)
        salida.write_text(encabezado(origen, raiz) + limpiar(texto), encoding="utf-8")
        convertidos.append(str(rel))

    lineas = [
        "Convertidos: %d" % len(convertidos),
        "Omitidos (ya existian): %d" % len(omitidos),
        "Con errores: %d" % len(errores),
        "Para revisar a mano: %d" % len(avisos),
    ]
    if avisos:
        lineas += ["", "REVISAR:"] + ["- " + a for a in avisos]
    if errores:
        lineas += ["", "ERRORES:"] + ["- " + e for e in errores]
    if omitidos:
        lineas += ["", "OMITIDOS (usa --sobrescribir para reemplazarlos):"] + ["- " + o for o in omitidos]

    reporte = "\n".join(lineas) + "\n"
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "_reporte_conversion.txt").write_text(reporte, encoding="utf-8")
    print(reporte)


if __name__ == "__main__":
    main()