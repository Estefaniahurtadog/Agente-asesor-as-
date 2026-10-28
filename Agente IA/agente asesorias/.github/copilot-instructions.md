# Instrucciones para Copilot — Agente IA Asesorías

Este repositorio es una **base de conocimiento documental multi-aplicación** consultable por
IA. Antes de responder, lee `MANUAL_DE_USO.md` en la raíz si necesitas más contexto.

## Contexto del repositorio

- `originales/<aplicacion>/` contiene los documentos **fuente** sin modificar (Word, Excel,
  PDF, WSDL/XSD, etc.). No los edites ni los borres.
- `conocimiento/<aplicacion>/docs/` (y subcarpetas propias de cada app) contiene la versión
  convertida y organizada en Markdown/CSV, pensada para consulta rápida. **Usa siempre esta
  carpeta como fuente principal para responder preguntas**, no los binarios en `originales/`.
- Cada aplicación (ej. `banktrade`) puede tener: documentos de diseño, un catálogo resumen de
  servicios/WSDL, un diccionario de tablas y un diccionario de datos a nivel de campo (CSV).
  Cruza esta información entre sí para responder preguntas de negocio, de servicios expuestos
  o de estructura de datos.

## Cómo responder

- Responde solo con base en lo que está documentado en `conocimiento/`. Si algo no está
  documentado (p. ej. valores reales de tablas paramétricas, datos de producción,
  homologaciones no documentadas), dilo explícitamente en vez de inventar.
- Si la pregunta requiere cruzar varias fuentes (diseño + WSDL + diccionario de datos),
  hazlo y explica de dónde sale cada parte de la respuesta, enlazando los archivos relevantes.
- Este agente es **agnóstico de tecnología**: no asumas que todas las aplicaciones son
  legacy/COBOL solo porque BankTrade lo es.

## Cómo agregar/convertir conocimiento nuevo

- Si el usuario trae documentos nuevos en formatos binarios (`.docx`, `.doc` legacy, `.xlsx`,
  PDF escaneado), conviértelos a Markdown/CSV dentro de `conocimiento/<aplicacion>/docs/`
  antes de intentar responder preguntas sobre ellos (no leas binarios directamente con
  herramientas de texto).
  - `.docx`/`.pdf` con texto: usar `convertidorMD.py` (requiere Python + `markitdown`), o
    convertir manualmente si Python no está disponible.
  - `.doc` legacy / `.xlsx`: si no hay Python disponible, usar automatización COM de
    Word/Excel vía PowerShell (requiere Office instalado).
  - `.wsdl`/`.xsd`: ya son texto plano, no requieren conversión; para catálogos con muchos
    servicios, genera un Markdown resumen (namespaces, operaciones, campos de
    entrada/salida) para evitar reexplorar el XML completo en cada pregunta.
- Usa nombres de archivo descriptivos del contenido real (nunca "Documento 1", "sin
  título", etc.).
- Si una hoja/tabla es muy grande (miles de filas, ej. diccionarios de datos), exporta a CSV
  en vez de una tabla Markdown gigante.
- Borra archivos temporales/scratch usados solo para análisis intermedio antes de terminar.

## Confidencialidad

Esta información puede ser interna/confidencial del banco. No repliques datos de clientes
reales, credenciales ni cadenas de conexión en los documentos convertidos. Verifica que el
repositorio de destino permanezca privado.
