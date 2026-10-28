# Agente IA Asesorías — versión local (sin licencia de Copilot)

Esta carpeta contiene una aplicación web **100% local**: corre en tu propio equipo, usa un
modelo de IA que se ejecuta localmente (no envía nada a internet) y responde preguntas
basándose en todo el contenido de la carpeta [`conocimiento/`](../conocimiento/) (hoy
BankTrade; cualquier otra aplicación que agregues ahí después también quedará disponible
automáticamente, sin importar su tecnología).

> ⚠️ **Antes de instalar nada**: confirma con el área de TI/Seguridad de tu organización que
> está permitido instalar Python y Ollama en este equipo. Ambas son herramientas de código
> abierto ampliamente usadas, y Ollama en particular corre modelos **100% locales** (no
> requiere conexión a internet para funcionar ni envía datos a servidores externos), lo cual
> suele facilitar la aprobación frente a herramientas de IA en la nube.

## ¿Qué es cada cosa?

| Herramienta | Para qué sirve |
|---|---|
| **Python** | Lenguaje en el que está escrita la aplicación |
| **Ollama** | Motor que ejecuta modelos de IA localmente en tu PC (como un "mini servidor de IA" sin internet) |
| **Streamlit** | Librería que genera la interfaz web (el "front") donde escribes tus preguntas |
| **ChromaDB** | Base de datos vectorial local donde se guarda el índice de tus documentos para poder buscarlos rápido |

## Instalación (una sola vez)

### 1. Instalar Python
Descarga e instala Python 3.11 o superior desde https://www.python.org/downloads/
(marca la casilla "Add python.exe to PATH" durante la instalación), o si tienes `winget`
disponible:

```powershell
winget install -e --id Python.Python.3.12
```

### 2. Instalar Ollama
Descarga el instalador desde https://ollama.com/download (Windows), o con `winget`:

```powershell
winget install -e --id Ollama.Ollama
```

Después de instalarlo, Ollama queda corriendo en segundo plano automáticamente
(`http://localhost:11434`).

### 3. Instalar las dependencias de la app y descargar los modelos

Dentro de esta carpeta (`app_local/`), haz doble clic en **`instalar_dependencias.bat`**
(o ejecútalo desde PowerShell). Esto instala las librerías de Python necesarias y descarga
dos modelos de IA:

- `nomic-embed-text` (~274 MB) — para "entender" e indexar tus documentos.
- `llama3.1` (~4.7 GB) — para generar las respuestas de chat.

> Tu equipo tiene suficiente RAM (15.5 GB) para correr estos modelos sin problema. La
> descarga puede tardar varios minutos según tu conexión.

## Uso diario

1. Doble clic en **`iniciar.bat`**. Se abrirá tu navegador en `http://localhost:8501`.
2. La **primera vez** (o cada vez que agregues/actualices documentos en `conocimiento/`),
   haz clic en **"🔄 Reconstruir índice"** en la barra lateral. Esto lee todos los `.md` y
   `.csv` de la carpeta `conocimiento/` y los indexa (puede tardar varios minutos la primera
   vez, dependiendo de cuántos documentos haya).
3. Escribe tu pregunta en el cuadro de chat, igual que lo haces en esta conversación. La
   respuesta aparecerá con un listado de **"📎 Fuentes consultadas"** debajo, indicando de
   qué archivo(s) salió la información.

## Cómo agregar una nueva aplicación/tecnología al agente

1. Crea una carpeta nueva dentro de `conocimiento/` (ej. `conocimiento/otra_app/`).
2. Coloca ahí sus documentos ya convertidos a `.md`/`.csv` (sigue las mismas convenciones
   descritas en [`MANUAL_DE_USO.md`](../MANUAL_DE_USO.md)).
3. Abre la app y haz clic en **"🔄 Reconstruir índice"**. Ya puedes preguntar sobre esa nueva
   aplicación en el mismo chat — no hace falta crear un agente aparte.

## Solución de problemas

| Problema | Posible causa / solución |
|---|---|
| "Error al generar la respuesta" | Ollama no está corriendo. Abre una terminal y ejecuta `ollama serve`, o reinicia el equipo (Ollama suele iniciar solo). |
| Respuestas muy lentas | Normal en equipos sin tarjeta gráfica dedicada; el modelo corre por CPU. Puedes probar un modelo más liviano cambiando `CHAT_MODEL` en `config.py` (ej. `llama3.2:3b`). |
| "No encontré esta información" en todas las preguntas | El índice no se construyó correctamente. Revisa la consola/terminal por errores y vuelve a hacer clic en "Reconstruir índice". |
| Quiero usar otro modelo | Edita `CHAT_MODEL` o `EMBED_MODEL` en [`config.py`](./config.py), descarga el modelo con `ollama pull <nombre>`, y reconstruye el índice si cambiaste el modelo de embeddings. |

## Nota de confidencialidad

Esta app no envía ningún dato a servicios externos: todo el procesamiento (embeddings +
generación de respuestas) ocurre dentro de tu equipo vía Ollama. Aun así, el contenido de
`conocimiento/` puede incluir información interna/confidencial del banco — ten el mismo
cuidado que ya se indica en `MANUAL_DE_USO.md` respecto a mantener este repositorio privado.
