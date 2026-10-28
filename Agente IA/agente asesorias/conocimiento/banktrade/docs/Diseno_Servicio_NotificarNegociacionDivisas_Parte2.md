> Convertido automaticamente. Revisar tablas y diagramas antes de usar.
> Origen: Documento sin título (8).docx
> Fecha del original: 2026-10-25
> Fecha de conversion: 2026-10-25

1. **Introducción**

Este documento provee una representación de diseño detallado del Componente de integración WMB (Flujo) que implementa las operaciones “**notificarNegociacionDivisas**” la cual le permite al sistema SERIVA solicitar la notificación de negociación de divisas.

1. **Documentos Relacionados**

A continuación se detalla la lista de documentos complementarios a este documento.

| **Descripción** | **Nombre Archivo** | **SVN** | **Repositorio** |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

**Tabla 1.**

1. **Contexto General de la Solución**

Este es uno de los servicios que maneja Banco de Occidente para que SERIVA pueda solicitar la notificación de negociación de divisas. Esta operación será implementada por un flujo WMB.

A continuación se presenta de forma gráfica como será cubierta la funcionalidad de negocio de notificarNegociacionDivisas.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 1. Diagrama de Contexto**

1. **Componentes de la Solución**

A continuación se detalla la información relacionada con los diferentes sistemas o componentes de software que participan en la solución de alto nivel.

1. **Componentes de la Solución General**

| **Nombre** | **Descripción** | **Protocolo Transporte** | **Formato Mensaje** |
| --- | --- | --- | --- |
| Consumidor | CORE Pasivas, ICBS, COMEX, etc. | HTTP | SOAP/XML |
| CRM | Es el acrónimo de Customer Relationship Management – Occicliente. Aplicación que reúne la información del cliente tanto de productos, servicios e información del cliente. Actualmente se tienen reunidos el 80% de productos que tiene el cliente en el mismo lugar. | HTTP | HTTP/XML |
| Websphere Message Broker | Solución middleware de IBM utilizada por Banco de Occidente para realizar la implementación de su ESB corporativo. | Multi | XML |

**Tabla 2.**

1. **Componentes de la Solución Específica de Integración**

A continuación se detalla deferentes flujos o componentes WMB que participan en la solución detallada.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 2. Diagrama de Componentes de Integración**

| **Nombre** | **Descripción** | **Tipo** | **Mensaje Entrada** | **Mensaje Salida** |
| --- | --- | --- | --- | --- |
| NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_TRANS | Componente de integración que expone el ESB para la comunicación con el Consumidor. | Interface | XML/  SOAP | SOAP/XML |
| NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG | Componentes Message flow responsable de realizar las transformaciones y enriquecimientos requeridos con el objetivo de cubrir el requerimiento de solicitar la notificación de negociación de divisas. | Subflujo | XML/  Canónico | XML/  Canónico |
| BankTrade | Sistema de COMEX. | MQ | Trama Plana / MQ | MQ/Trama Plana |
| ManejoMonitoreo | Componente MessageFlow genérico responsable realizar el registro en BD de los mensajes de error que se produzcan en los flujos. | Flujo | XML/  Especifico/  MQ | No Genera Respuesta |
| Auditoría | Componente MessageFlow genérico responsable realizar el registro en BD de los mensajes de auditoría por cada transacción. | Flujo | XML/  Especifico/  MQ | No Genera Respuesta |

**Tabla 3.**

1. **Descripción del Servicio**

| **Nombre del Servicio** | notificarNegociacionDivisas |
| --- | --- |
| **Identificador** | Pendiente |
| **Taxonomía del Servicio** | Servicio de Negocio – Evaluación Pendiente |
| **Responsable de Negocio** | Pendiente |
| **Responsable en TI** | Integración ESB |
| **Versión No.** | 1.0 |

**Tabla 4.**

1. **Descripción del Servicio**

El servicio de notificarNegociacionDivisas tiene por objetivo implementar y exponer una operación al consumidor SERIVA, que permita solicitar la notificación de negociación de divisas.

1. **Operación e Interfaz del Servicio**
2. **Operaciones del Servicio**

Este servicio de consulta expone la siguiente operación:

* notificarNegociacionDivisas

1. **Interfaz del Servicio**

A continuación se muestra una representación de los mensajes de entrada y salida que serán utilizados por la operación de notificarNegociacionDivisas.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 3. Mensajes notificarNegociacionDivisas**

1. **Diseño Detallado de Flujos**

A continuación se presenta la información detallada asociada a la operación a implementar notificarNegociacionDivisas, y al flujo que realizará su implementación: NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG.

1. **notificarNegociacionDivisas**
2. **Descripción de la Operación**

Esta operación tiene por objetivo permitirle al sistema SERIVA solicitar la notificación de negociación de divisas. Esta operación se implementara con el flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG el cual se presenta a continuación:

1. **NotificacionNegociacionDivisas\_notificarNegociacionDivisas**
2. **Diagrama Flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas \_TRANS**

**[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]**

**Grafico 4. NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_TRANS**

1. **Diagrama Subflujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas \_FMG**

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**Grafico 5. NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG**

1. **Mensaje de Entrada (Request) – notificarNegociacionDivisas**

A continuación se brinda los detalles técnicos asociados con el mensaje de entrada al Flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG.

| **Dominio mensaje** | XMLNSC |
| --- | --- |
| **Tipo Mensajería** | Canónico |
| **Mensaje de Entrada** | notificarNegociacionDivisas |
| **Elementos del Mensaje** | El detalle del mensaje de entrada se encuentra en el documento adjunto:  http://190.66.22.185:82/svn/BOCC/Service Specification and Design/COMEX\Release 1\Especificaciones\Paquete 4\Notificacion Negociacion Divisas \Mapeo Notificacion Negociacion Divisas.xls |

**Tabla 5.**

1. **Mensaje de Salida (Response) – notificarNegociacionDivisas**

A continuación se brinda los detalles técnicos asociados con el mensaje de salida del Flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG.

| **Dominio mensaje** | XMLNSC |
| --- | --- |
| **Tipo Mensajería** | Canónico |
| **Mensaje de Entrada** | notificarNegociacionDivisas |
| **Elementos del Mensaje** | El detalle del mensaje de entrada se encuentra en el documento adjunto:  http://190.66.22.185:82/svn/BOCC/Service Specification and Design/COMEX\Release 1\Especificaciones\Paquete 4\Notificacion Negociacion Divisas \Mapeo Notificacion Negociacion Divisas.xls |

**Tabla 6.**

1. **Mensaje de Error (Fault) - notificarNegociacionDivisas**

En el caso de presentarse Error se generará el mensaje respectivo manejando los campos RtaCod con el valor “9999”, y el campo RtaMnsje con el valor “No existe comunicación con BankTrade”.

1. **Diagrama de Secuencia**

**Grafico 6. Diagrama de Secuencia**

A continuación se detallan las actividades y secuencias relacionadas con el flujo objeto del diseño NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG.

1. El consumidor envía la petición de notificarNegociacionDivisas al ESB.
2. En el flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_TRANS se transforma el mensaje de petición a formato canónico.
3. Se envía el mensaje transformado al flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG.
4. Se genera el mensaje de petición para BankTrade en formato XML, con las transformaciones indicadas en el archivo de mapeo.
5. Se envía la petición al flujo de IntegracionBankTrade, que se encargara de transformar el mensaje a formato MRM para realizar la comunicación con el legado.
6. El flujo de Integración responde la petición de notificarNegociacionDivisas.
7. Se valida la respuesta recibida, si se recibe por la terminal de SalidaError pasa al numeral 3; si se genera por la salida se valida si fue exitosa (el campo RtaCod debe venir con 0) o no. Se genera el mensaje de respuesta exitoso o no exitoso (se realiza la respectiva homologación del campo RtaCod).
8. Se envía el mensaje de respuesta al flujo TRANS.
9. El flujo TRANS responde al consumidor la petición de notificarNegociacionDivisas y finaliza la transacción.

**Flujo Alternativo**

1. Se genera error en la comunicación con BankTrade (no se recibe el mensaje dentro del tiempo estimado).
2. Se genera el mensaje para enviar a la cola de monitoreo.
3. El flujo de integración responde con error (por la terminal SalidaError).
4. Se genera el mensaje de error (el campo RtaCod se setea con el valor “9999” y el campo RtaMnsje con el valor “No existe comunicación con BankTrade”.
5. Se envía el mensaje de respuesta de error al flujo TRANS.
6. Se responde con error al consumidor y finaliza el flujo.

1. **Dependencias del Servicio**

| **Componente** | **Tipo** | **Protocolo** |
| --- | --- | --- |
| ManejoMonitoreo | Flujo | MQ |
| Auditoría | Flujo | MQ |

**Tabla 5**

1. **Premisas Generales**

| **Tipo** | **Descripción del Requerimiento** |
| --- | --- |
| Auditoria | La auditoría no es responsabilidad del flujo NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG esto será responsabilidad del flujo de entrada NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_TRANS que entregará la respuesta al sistema consumidor. |
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
| **Implicaciones** | Al momento de desarrollar los Flujos NotificacionNegociacionDivisas\_notificarNegociacionDivisas\_FMG se tiene una dependencia con el componente responsable de realizar la integración con el sistema externo. |
