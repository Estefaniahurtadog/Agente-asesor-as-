@echo off
cd /d "%~dp0"
set PYTHON_EXE=C:\WPy64-31241\python-3.12.4.amd64\python.exe
echo Iniciando Agente IA Asesorias en http://localhost:8501 ...
"%PYTHON_EXE%" -m streamlit run app.py
pause
