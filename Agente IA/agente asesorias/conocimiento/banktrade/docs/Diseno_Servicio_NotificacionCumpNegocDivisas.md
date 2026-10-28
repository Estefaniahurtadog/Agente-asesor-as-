> Convertido automaticamente. Revisar tablas y diagramas antes de usar.
> Origen: documento1 (1).docx
> Fecha del original: 2026-10-25
> Fecha de conversion: 2026-10-25

1. **Introducción**

Este documento provee una representación de diseño detallado del Componente de integración WMB (Flujo) que implementa la operación “**notificarCumpNegocDivisas**” del servicio **“NotificacionCumpNegocDivisas”** la cual le permite al sistema BANKTRADE solicitar la notificación del cumplimiento de negociación de divisas.

1. **Documentos Relacionados**

A continuación se detalla la lista de documentos complementarios a este documento.

| **Descripción** | **Nombre Archivo** | **SVN** | **Repositorio** |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

**Tabla 1.**

1. **Contexto General de la Solución**

Este es uno de los servicios que maneja Banco de Occidente para que BANKTRADE pueda solicitar la notificación de cumplimiento de negociación de divisas. Esta operación será implementada por un flujo WMB.

A continuación se presenta de forma gráfica como será cubierta la funcionalidad de negocio de NotificacionCumpNegocDivisas - notificarCumpNegocDivisas.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 1. Diagrama de Contexto**

1. **Componentes de la Solución**

A continuación se detalla la información relacionada con los diferentes sistemas o componentes de software que participan en la solución de alto nivel.

1. **Componentes de la Solución General**

| **Nombre** | **Descripción** | **Protocolo Transporte** | **Formato Mensaje** |
| --- | --- | --- | --- |
| Consumidor | BANKTRADE. | SOAP | XML |
| SERIVA | Aplicación de Comercio Exterior | SOAP | XML |
| Websphere Message Broker | Solución middleware de IBM utilizada por Banco de Occidente para realizar la implementación de su ESB corporativo. | Multi | XML |

**Tabla 2.**

1. **Componentes de la Solución Específica de Integración**

A continuación se detalla deferentes flujos o componentes WMB que participan en la solución detallada.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 2. Diagrama de Componentes de Integración**

| **Nombre** | **Descripción** | **Tipo** | **Mensaje Entrada** | **Mensaje Salida** |
| --- | --- | --- | --- | --- |
| NotificacionCumpNegocDivisas\_WS | Componente de integración que expone el ESB para la comunicación con el Consumidor. | Interface | XML/  SOAP | SOAP/XML |
| NotificacionCumpNegocDivisas\_notificarCumpNegocDivisas\_FMG | Componentes Message flow responsable de realizar las transformaciones y enriquecimientos requeridos con el objetivo de cubrir el requerimiento de solicitar la notificación de cumplimiento negociación de divisas. | Subflujo | XML/  Canónico | XML/  Canónico |
| OperacionWS | Componente Message Flow responsable de implementar las necesidades de integración con la aplicación Multipropósito. | Subflujo | XML/  Canónico | XML/  Canónico |
| ManejoMonitoreo | Componente MessageFlow genérico responsable realizar el registro en BD de los mensajes de error que se produzcan en los flujos. | Flujo | XML/  Especifico/  MQ | No Genera Respuesta |
| Auditoría | Componente MessageFlow genérico responsable realizar el registro en BD de los mensajes de auditoría por cada transacción. | Flujo | XML/  Especifico/  MQ | No Genera Respuesta |

**Tabla 3.**

1. **Descripción del Servicio**

| **Nombre del Servicio** | NotificacionCumpNegocDivisas |
| --- | --- |
| **Identificador** | Pendiente |
| **Taxonomía del Servicio** | Servicio de Negocio – Evaluación Pendiente |
| **Responsable de Negocio** | Pendiente |
| **Responsable en TI** | Integración ESB |
| **Versión No.** | 1.0 |

**Tabla 4.**

1. **Descripción del Servicio**

El servicio de NotificacionCumpNegocDivisas tiene por objetivo implementar y exponer una operación al consumidor BANKTRADE/Módulo de Pagos, que permita solicitar la notificación de cumplimiento de una negociación de divisas. Para esto el ESB debe exponer un Web Service al consumidor, una vez reciba el mensaje de petición, debe enrutarlo hacia SERIVA, consumiendo también un Web Service, recibir la respuesta y enviarla al consumidor.

1. **Operación e Interfaz del Servicio**
2. **Operaciones del Servicio**

Este servicio de consulta expone la siguiente operación:

* notificarCumpNegocDivisas

1. **Interfaz del Servicio**

A continuación se muestra una representación de los mensajes de entrada y salida que serán utilizados por la operación de notificarCumpNegocDivisas.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 3. Mensajes notificarCumpNegocDivisas**

1. **Diseño Detallado de Flujos**

A continuación se presenta la información detallada asociada a la operación a implementar notificarCumpNegocDivisas, y al flujo que realizará su implementación: NotificacionCumpNegocDivisas\_notificarCumpNegocDivisas\_FMG.

1. **notificarCumpNegocDivisas**
2. **Descripción de la Operación**

Esta operación tiene por objetivo permitirle al sistema BANKTRADE solicitar la notificación de cumplimiento de negociación de divisas. Esta operación se implementara con el flujo NotificacionCumpNegocDivisas\_notificarCumpNegocDivisas\_FMG el cual se presenta a continuación:

1. **NotificacionCumpNegociacionDivisas\_notificarCumpNegocDivisas\_FMG**
2. **Diagrama Flujo NotificacionCumpNegociacionDivisas\_WS**

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 4. NotificacionCumpNegociacionDivisas\_notificarCumpNegocDivisas\_TRANS**

1. **Diagrama Subflujo NotificacionCumpNegociacionDivisas\_ notificarCumpNegocDivisas\_FMG**

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 5. NotificacionCumpNegociacionDivisas\_notificarCumpNegocDivisas\_TRANS**

1. **Mensaje de Entrada (Request) – notificarCumpNegocDivisas**

A continuación se brinda los detalles técnicos asociados con el mensaje de entrada al Flujo NotificacionCumpNegociacionDivisas\_notificarCumpNegocDivisas\_FMG.

| **Dominio mensaje** | XMLNSC |
| --- | --- |
| **Tipo Mensajería** | Canónico |
| **Mensaje de Entrada** | notificarCumpNegocDivisas |
| **Elementos del Mensaje** | El detalle del mensaje de entrada se encuentra en el documento adjunto:  [<u>http://190.66.22.185:82/svn/BOCC/Static Versions/Analisis y Diseño/COMEX/Analisis/Especificaciones/</u><u>Notificación Cumplimiento Negociación Divisas/</u><u>Mapeo NotificacionCumpNegocDivisas.xls</u>](http://190.66.22.185:82/svn/BOCC/Static%20Versions/Analisis%20y%20Dise%C3%B1o/COMEX/Analisis/Especificaciones/%20Notificaci%C3%B3n%20Cumplimiento%20Negociaci%C3%B3n%20Divisas/%20Mapeo%20NotificacionCumpNegocDivisas.xls) |

**Tabla 5.**

1. **Mensaje de Salida (Response) – notificarNegociacionDivisas**

A continuación se brinda los detalles técnicos asociados con el mensaje de salida del Flujo NotificacionCumpNegociacionDivisas\_notificarCumpNegocDivisas\_FMG.

| **Dominio mensaje** | XMLNSC |
| --- | --- |
| **Tipo Mensajería** | Canónico |
| **Mensaje de Entrada** | notificarCumpNegocDivisasRta |
| **Elementos del Mensaje** | El detalle del mensaje de entrada se encuentra en el documento adjunto:  [<u>http://190.66.22.185:82/svn/BOCC/Static Versions/Analisis y Diseño/COMEX/Analisis/Especificaciones/ Notificación Cumplimiento Negociación Divisas/ Mapeo NotificacionCumpNegocDivisas.xls</u>](http://190.66.22.185:82/svn/BOCC/Static%20Versions/Analisis%20y%20Dise%C3%B1o/COMEX/Analisis/Especificaciones/%20Notificaci%C3%B3n%20Cumplimiento%20Negociaci%C3%B3n%20Divisas/%20Mapeo%20NotificacionCumpNegocDivisas.xls) |

**Tabla 6.**

1. **Mensaje de Error (Fault) - notificarCumpNegocDivisas**

En el caso de presentarse Error se generará el mensaje respectivo manejando los campos RtaCod con el valor “9999”, y el campo RtaMnsje con el valor “No existe comunicación con SERIVA”.

1. **Diagrama de Secuencia**

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 6. Diagrama de Secuencia**

A continuación se detallan las actividades y secuencias relacionadas con el flujo objeto del diseño para el servicio NotificacionCumpNegocDivisas.

1. Se recibe el mensaje del consumidor.
2. En el flujo NotificacionNegociacionDivisas\_WS se almacena la petición y se transforma el mensaje a formato canónico.
3. Se envía el mensaje transformado al flujo NotificacionCumpNegocDivisas\_notificarCumpNegocDivisas\_FMG.
4. Se almacenan las variables requeridas para el mensaje de auditoría y se genera el mensaje de petición para SERIVA en formato XML.
5. Se envía la petición al flujo OperacionWS.
6. El flujo OperacionWS, transforma el mensaje para SERIVA y lo envía al subflujo de comunicación.
7. OperacionWS recibe y transforma el mensaje, en caso de que se genere un error de comunicación con SERIVA, genera mensaje y envía a la cola de monitoreo.
8. OperacionWS envía mensaje de respuesta al flujo FMG.
9. Se valida la respuesta recibida, si se recibe por la terminal de SalidaError pasa al numeral 1.2.2.3.3.; si se genera por la salida se genera el mensaje de respuesta (se realiza la respectiva homologación del campo RtaCod y del campo RtaMnsje con la función HomologacionError).
10. Se envía el mensaje de respuesta al flujo TRANS.
11. El flujo TRANS transforma el mensaje de respuesta a formato específico.
12. Se envía mensaje a la cola de Auditoría y se responde al consumidor y finaliza el flujo.
13. Si la respuesta del subflujo OperacionWS se recibe por la terminal SalidaError, se debe generar mensaje de respuesta de Error.
14. Se envía el mensaje de respuesta al flujo TRANS.
15. El flujo TRANS transforma el mensaje de respuesta a formato específico.
16. Se envía mensaje a la cola de Auditoría y se responde al consumidor y finaliza el flujo.
17. **Dependencias del Servicio**

| **Componente** | **Tipo** | **Protocolo** |
| --- | --- | --- |
| OperacionWS | Flujo | SOAP/XML |
| ManejoMonitoreo | Flujo | MQ |
| Auditoría | Flujo | MQ |

**Tabla 5**

1. **Premisas Generales**

| **Tipo** | **Descripción del Requerimiento** |
| --- | --- |
| Auditoria | La auditoría no es responsabilidad del flujo NotificacionCumpNegocDivisas\_notificarCumpNegocDivisas\_FMG esto será responsabilidad del flujo de entrada NotificacionCumpNegocDivisas\_WS que entregará la respuesta al sistema consumidor. |
| Errores entre Aplicativos | Si los sistemas que participan en la integración responden con algún error, deberá homologarse el código del error utilizando las funciones establecidas para dicho fin (Util). Con el objetivo que la aplicación consumidora pueda entender el error. |
| Homologación | Las homologaciones de códigos y tipos deberán realizarse utilizando las funciones comunes especificadas para dicho fin. |
| Constantes | Las constantes deberán trabajarse utilizando el archivo de constantes .ESQL |
| Manejo de Excepciones | Toda excepción que se produzca al interior del flujo deberá ser responsabilidad del flujo de integración y deberá reportarla a la cola de ManejoMonitoreo\_IN con base en el mensaje de entrada especificado para el flujo ManejoMonitoreo. |

**Tabla 6**

1. **Requerimientos No Funcionales**

| **ID** | **Tipo** | **Descripción del Requerimiento** |
| --- | --- | --- |
| RNF-3 | Desempeño | El tiempo óptimo para que el ESB retorne la respuesta a los aplicativos impactados en 5 segundos. |
| RNF-4 | Disponibilidad | El servicio expuesto en el ESB debe estar disponible el 99.5% del mes. |

**Tabla 7**

1. **Políticas**

Para este servicio no se han establecido políticas (WS-Policys), que controlen, restrinjan o informen sobre los detalles de su operación. Los requerimientos no funcionales deberán ser controlados con mecanismos alternos.

1. **Decisiones de Realización**

| **Tema** | **Estrategia utilizada para la comunicación con los sistemas legados** |
| --- | --- |
| **Contexto** | La integración con sistemas legados puede generar particularidades técnicas las cuales se pueden ver como tareas repetitivas, ya que una gran cantidad de flujos podrían requerir integrarse con el mismo sistema. |
| **Problema** | ¿Qué estrategia será utilizado para comunicarse con los sistemas externos? |
| **Alternativas** | 1. Desde cada flujo establecer la comunicación acorde al protocolo y mensaje de cada sistema externo    2. Delegar la responsabilidad de integración a un único componente MessageFlow (Flujo) con interfaz MQ.    3. Delegar la responsabilidad de integración a un único componente MessageFlow (Subflujo) con interfaz interna (Solo WMB). |
| **Decisión** | Se opta por la alternativa número 3. |
| **Justificación** | Se opta por esta alternativa, para mantener la arquitectura implementada, y lograr mayor independencia en caso de que se realice algún cambio en cuanto a formatos de mensajes, protocolos de comunicación, etc. Además se desea que las unidades de despliegue incluyan las responsabilidades de integración, y que estas no estén delegadas en otro flujo. |
| **Implicaciones** | Al momento de desarrollar los Flujos NotificacionCumpNegocDivisas\_notificarCumpNegocDivisas\_FMG se tiene una dependencia con el componente responsable de realizar la integración con el sistema externo. |
