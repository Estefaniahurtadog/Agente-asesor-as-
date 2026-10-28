@echo off
cd /d "%~dp0"

REM Ruta a WinPython instalado en este equipo. Ajusta esta linea si tu ruta es distinta.
set PYTHON_EXE=C:\WPy64-31241\python-3.12.4.amd64\python.exe

echo ===========================================================
echo Instalando dependencias del Agente IA Asesorias (local)
echo ===========================================================
echo.
if not exist "%PYTHON_EXE%" (
    echo [ERROR] No se encontro Python en: %PYTHON_EXE%
    echo Edita la variable PYTHON_EXE en este archivo con la ruta correcta de tu WinPython.
    pause
    exit /b 1
)
echo Usando Python: %PYTHON_EXE%
echo.
echo 1) Instalando librerias de Python...
"%PYTHON_EXE%" -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Fallo la instalacion de dependencias de Python.
    pause
    exit /b 1
)

echo.
echo 2) Descargando modelos de Ollama (puede tardar varios minutos)...
echo    - Embeddings: nomic-embed-text
ollama pull nomic-embed-text
echo    - Chat: llama3.1
ollama pull llama3.1

echo.
echo ===========================================================
echo Listo. Ejecuta iniciar.bat para abrir la aplicacion.
echo ===========================================================
pause
