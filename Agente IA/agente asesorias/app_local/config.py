"""
Configuración central de la app. Ajusta aquí los modelos o rutas si lo necesitas.
"""
import os

# Carpeta raíz del proyecto (un nivel arriba de app_local/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta donde viven todos los documentos ya convertidos (uno o más subfolders por app)
CONOCIMIENTO_DIR = os.path.join(BASE_DIR, "conocimiento")

# Carpeta donde se guarda el índice vectorial (se crea sola al construir el índice)
CHROMA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chroma_db")

# Modelos de Ollama (deben descargarse una vez con 'ollama pull <modelo>')
EMBED_MODEL = "nomic-embed-text"   # modelo de embeddings (liviano, ~274MB)
CHAT_MODEL = "llama3.1"            # modelo de chat (~4.7GB). Alternativa en español: "qwen2.5:7b"

COLLECTION_NAME = "conocimiento_apps"

# Tamaño de fragmentos de texto (en caracteres) y filas por bloque para CSVs
MAX_CHARS_MD = 1500
ROWS_PER_CHUNK_CSV = 40
