# Manual de Uso — Agente IA Asesorías

## 1. ¿Qué es esto?

**Agente IA Asesorías** no es un chatbot entrenado ni un modelo propio: es una **base de
conocimiento documental organizada**, pensada para ser consultada con un asistente de IA
(GitHub Copilot / Copilot CLI u otro asistente equivalente) que lee los archivos de este
repositorio y responde preguntas de negocio, técnicas y funcionales sobre las aplicaciones
documentadas aquí.

El agente es **agnóstico de tecnología**: no importa si la aplicación que documentas está
hecha en COBOL, Java, .NET, es on-premise, en la nube, propia o tercerizada. Lo único que
necesita es **documentación legible** (Markdown, CSV, texto plano, XML/WSDL/XSD). Formatos
binarios (Word, Excel, PDF) se convierten antes de poder consultarse de forma eficiente.

## 2. Estructura del repositorio

```
agente asesorias/
├── MANUAL_DE_USO.md              <- este documento
├── convertidorMD.py              <- script de conversión masiva Word/PDF -> Markdown (requiere Python + markitdown)
├── originales/
│   └── <aplicacion>/             <- documentos FUENTE sin modificar (.docx, .doc, .xlsx, .pdf, .wsdl, .xsd...)
└── conocimiento/
    └── <aplicacion>/
        ├── docs/                 <- versión en Markdown/CSV lista para consulta rápida
        └── <subcarpetas propias de la app>   <- p.ej. catálogos de servicios, WSDL/XSD, etc.
```

Ejemplo real con BankTrade:

```
originales/banktrade/
  Banktrade Database.doc
  Diseno_Servicio_NotificacionCumpNegocDivisas.docx
  ...

conocimiento/banktrade/
  docs/
    Banktrade_Database_Diccionario_Tablas.md      <- diccionario de tablas (29 grupos funcionales)
    Banktrade_DataDictionary.csv                  <- diccionario de datos a nivel de CAMPO (13,000+ filas)
    Banktrade_TableFunction.md, Banktrade_Rules.md, Banktrade_TableReports.md, Banktrade_ProgramDescriptions.md
    Diseno_Servicio_*.md                          <- diseños de servicios de negocio
    Funcionalidad_Lista_OFAC_ALR.md
    _reporte_conversion.txt                       <- registro de qué se convirtió y cuándo
  Banktrade Servicios/
    Catalogo_Servicios_Banktrade.md                <- catálogo resumen de los 5 webservices SOAP (WSDL/XSD)
    <NombreServicio>/.../xsd, wsdl                 <- WSDL/XSD originales (ya son texto, no requieren conversión)
```

## 3. Regla de oro: todo pasa a texto/Markdown consultable

Para que el asistente de IA responda rápido y bien, **evita dejar como única fuente**
archivos binarios (.docx, .doc, .xlsx, .pdf escaneado). El flujo es siempre:

1. Coloca el/los archivo(s) originales en `originales/<aplicacion>/`.
2. Conviértelos a Markdown/CSV dentro de `conocimiento/<aplicacion>/docs/`.
3. Dale nombres **descriptivos** a los `.md` resultantes (el nombre debe reflejar el
   contenido real, no "Documento 1", "Documento sin título", etc.).
4. Si hay varios servicios/WSDL, considera crear un **catálogo resumen** en Markdown
   (como `Catalogo_Servicios_Banktrade.md`) para no tener que explorar todo el XML cada vez.

### Cómo convertir según el tipo de archivo

| Tipo de archivo | Cómo convertir |
|---|---|
| `.docx` / `.pdf` (texto, no escaneado) | Usar `convertidorMD.py` (ver sección 4) o pedirle al asistente que lo convierta |
| `.doc` legacy (Word 97-2003, binario) | El asistente usa automatización COM de Word vía PowerShell (Word debe estar instalado en el equipo) |
| `.xlsx` | El asistente usa automatización COM de Excel vía PowerShell; hojas pequeñas → Markdown, hojas muy grandes (miles de filas) → CSV |
| `.wsdl` / `.xsd` | **Ya son texto plano**, no necesitan conversión. Opcionalmente se arma un catálogo Markdown resumen para consulta rápida |
| `.pdf` escaneado (imagen) | Requiere OCR — avisa al asistente para abordarlo con otra estrategia |

## 4. Usar el script `convertidorMD.py` (opcional, requiere Python)

```
pip install "markitdown[docx,pdf]"
python convertidorMD.py <nombre_aplicacion>
python convertidorMD.py <nombre_aplicacion> --sobrescribir   # para reemplazar .md ya existentes
```

> ⚠️ El script tiene una ruta `BASE` hardcodeada en la cabecera del archivo. Si lo ejecutas
> en un equipo distinto al que lo creó, ajusta esa ruta a la ubicación real de la carpeta
> `agente asesorias` en tu máquina.

Si no tienes Python/markitdown disponibles, el asistente de IA puede convertir los archivos
igualmente usando automatización de Word/Excel (COM) vía PowerShell, siempre que Office esté
instalado en el equipo donde corre la sesión.

## 5. Cómo consultar el conocimiento (preguntas típicas)

Simplemente pídele al asistente, en lenguaje natural, lo que necesites saber. Ejemplos ya
probados con BankTrade:

- "¿Qué hace BankTrade?"
- "¿Cuáles son los servicios que utiliza BankTrade?"
- "¿Cuáles son los webservices que expone?"
- "¿Cuáles son las descripciones de todos los campos de la tabla LLNIS25?"
- "¿Dónde se almacena el catálogo de códigos de tipo de identificación?"

El asistente cruza información entre los documentos de diseño, el catálogo de servicios
(WSDL/XSD) y el diccionario de datos para dar respuestas completas y, cuando algo **no**
está documentado, debe decirlo explícitamente en vez de inventar la respuesta (así se hizo,
por ejemplo, al no tener los valores reales configurados en la tabla `LTABL` de BankTrade).

### 5.1 Opción sin licencia de Copilot: app web local (`app_local/`)

Si quieres que otras personas consulten este conocimiento **sin necesitar una licencia de
GitHub Copilot**, en la carpeta [`app_local/`](./app_local/) hay una aplicación web lista
para correr 100% en un PC (Python + Streamlit + Ollama, sin enviar datos a internet). Ver
[`app_local/README_INSTALACION.md`](./app_local/README_INSTALACION.md) para la guía paso a
paso de instalación y uso. Esta app lee automáticamente todo lo que haya en `conocimiento/`,
sin importar la aplicación o tecnología, por lo que no se necesita un agente distinto por
cada una.

## 6. Cómo agregar una aplicación nueva

1. Crea `originales/<nueva_aplicacion>/` y copia ahí toda la documentación fuente disponible
   (diseños, diccionarios de datos, WSDL/XSD, Swagger/OpenAPI, manuales, etc.).
2. Pídele al asistente que explore esos archivos y proponga una conversión a Markdown/CSV
   organizada en `conocimiento/<nueva_aplicacion>/docs/` (o subcarpetas propias, como se hizo
   con `Banktrade Servicios/` para los webservices).
3. Pide nombres de archivo descriptivos y, si hay muchos documentos técnicos (varios WSDL,
   muchas tablas), pide un **catálogo/índice resumen** en Markdown.
4. Prueba con preguntas de negocio reales para validar que el conocimiento quedó bien cargado.
5. (Opcional) Agrega a este repositorio una "ficha técnica" por aplicación indicando su
   tecnología, infraestructura (on-premise/cloud), modelo de soporte (interno/tercerizado) y
   tipos de integración — es solo para referencia humana, no afecta cómo responde el asistente.

## 7. Confidencialidad

Este repositorio puede contener información interna/confidencial del banco y de sus
aplicaciones (estructuras de base de datos, reglas de negocio, contratos de servicios). Antes
de compartirlo con más personas o subirlo a cualquier repositorio:

- Verifica que el repositorio de destino sea **privado** y que el acceso esté restringido a
  las personas autorizadas.
- No publiques credenciales, cadenas de conexión, IPs internas ni datos de clientes reales
  dentro de los documentos convertidos.
- Si una aplicación es tercerizada, valida con el proveedor/área de seguridad si existe alguna
  restricción adicional antes de documentar sus detalles internos.

## 8. Limitaciones a tener en cuenta

- El asistente solo sabe lo que está escrito en estos archivos; **no inventa datos de
  producción** (p. ej. valores reales de tablas paramétricas como `LTABL`, códigos ya
  asignados, etc.) si esa información no fue cargada.
- Los documentos convertidos automáticamente (Word/Excel/legacy `.doc`) deben revisarse una
  vez para validar que tablas, diagramas e imágenes no se hayan perdido en la conversión.
- Mantener los nombres de archivo descriptivos y el `_reporte_conversion.txt` actualizado
  facilita mucho el mantenimiento futuro de la base de conocimiento.
