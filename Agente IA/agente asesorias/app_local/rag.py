"""
Lógica de recuperación (retrieval) + generación de respuesta vía Ollama.
"""
import ollama
import chromadb

from config import CHROMA_DIR, EMBED_MODEL, CHAT_MODEL, COLLECTION_NAME

SYSTEM_PROMPT = """Eres el "Agente IA Asesorías", un asistente experto en documentación \
técnica y funcional de aplicaciones internas (por ejemplo BankTrade), pensado para dar \
soporte en consultas de ingeniería de datos, arquitectura e integraciones.

Reglas que debes seguir SIEMPRE:
1. Responde únicamente con base en el CONTEXTO que se te entrega en cada pregunta. No \
   inventes nombres de tablas, campos, servidores, IPs ni servicios que no aparezcan ahí.
2. Si la información solicitada no está en el contexto entregado, dilo explícitamente \
   (ej. "No encontré esta información en los documentos indexados") en vez de adivinar.
3. Cuando uses un dato del contexto, menciona el archivo fuente entre corchetes, por \
   ejemplo: [Fuente: Banktrade_DataDictionary.csv].
4. Responde en español, de forma clara, usando tablas o listas cuando ayude a la lectura.
5. Si la pregunta abarca varias aplicaciones/tecnologías, organiza la respuesta por \
   aplicación.
"""


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    return client.get_collection(COLLECTION_NAME)


def retrieve(query: str, k: int = 6):
    collection = get_collection()
    emb = ollama.embeddings(model=EMBED_MODEL, prompt=query)["embedding"]
    results = collection.query(query_embeddings=[emb], n_results=k)
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    return list(zip(docs, metas))


def build_user_prompt(query: str, contexts) -> str:
    context_text = "\n\n---\n\n".join(
        f"[Fuente: {m['source']}]\n{d}" for d, m in contexts
    )
    return (
        f"CONTEXTO RECUPERADO DE LA BASE DE CONOCIMIENTO:\n\n{context_text}\n\n"
        f"PREGUNTA DEL USUARIO:\n{query}"
    )


def ask(query: str, k: int = 6, history=None):
    """Devuelve (stream_de_respuesta, contexts_usados) para que la UI pueda
    mostrar la respuesta en streaming y las fuentes consultadas."""
    contexts = retrieve(query, k=k)
    user_prompt = build_user_prompt(query, contexts)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": user_prompt})

    stream = ollama.chat(model=CHAT_MODEL, messages=messages, stream=True)
    return stream, contexts
