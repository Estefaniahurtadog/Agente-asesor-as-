"""
Front web local del Agente IA Asesorías.
Ejecutar con: streamlit run app.py  (o doble clic en iniciar.bat)
"""
import os
import streamlit as st

from config import CONOCIMIENTO_DIR, CHROMA_DIR, CHAT_MODEL, EMBED_MODEL
from indexer import build_index
from rag import ask

st.set_page_config(page_title="Agente IA Asesorías", page_icon="🤖", layout="wide")
st.title("🤖 Agente IA Asesorías")
st.caption(
    f"100% local · Modelo de chat: `{CHAT_MODEL}` · Embeddings: `{EMBED_MODEL}` · "
    "Ningún dato sale de este equipo."
)

index_exists = os.path.isdir(CHROMA_DIR) and len(os.listdir(CHROMA_DIR)) > 0

with st.sidebar:
    st.header("⚙️ Administración")
    st.write("Carpeta de conocimiento conectada:")
    st.code(CONOCIMIENTO_DIR, language=None)

    if st.button("🔄 Reconstruir índice", help="Ejecuta esto después de agregar o actualizar documentos en 'conocimiento/'"):
        progress_bar = st.progress(0)
        status = st.empty()

        def cb(i, total, name):
            progress_bar.progress(i / total if total else 1.0)
            status.write(f"Indexando ({i}/{total}): `{name}`")

        with st.spinner("Construyendo índice... esto puede tardar varios minutos la primera vez."):
            total_chunks = build_index(progress_callback=cb)
        st.success(f"✅ Índice construido: {total_chunks} fragmentos indexados.")
        st.rerun()

    if not index_exists:
        st.warning("⚠️ Aún no hay índice construido. Haz clic en 'Reconstruir índice' antes de preguntar.")
    else:
        st.success("✅ Índice listo.")

    st.divider()
    if st.button("🧹 Limpiar conversación"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Pregunta algo sobre el conocimiento indexado (ej. BankTrade, servicios, tablas...)")

if prompt:
    if not index_exists:
        st.error("Primero construye el índice desde la barra lateral (⚙️ Administración).")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""
            try:
                stream, contexts = ask(prompt, k=6)
                for part in stream:
                    token = part.get("message", {}).get("content", "")
                    full_response += token
                    placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)

                sources = sorted({m["source"] for _, m in contexts})
                with st.expander("📎 Fuentes consultadas"):
                    for s in sources:
                        st.write(f"- `{s}`")
            except Exception as e:
                full_response = (
                    f"⚠️ Error al generar la respuesta: {e}\n\n"
                    "Verifica que Ollama esté corriendo (`ollama serve`) y que los modelos "
                    f"estén descargados (`ollama pull {EMBED_MODEL}` y `ollama pull {CHAT_MODEL}`)."
                )
                placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
