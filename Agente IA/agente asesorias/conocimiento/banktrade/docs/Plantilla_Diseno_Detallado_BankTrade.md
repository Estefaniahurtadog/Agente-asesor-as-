> Convertido automaticamente. Revisar tablas y diagramas antes de usar.
> Origen: diseñoydesarrollobanktrade.docx
> Fecha del original: 2026-10-25
> Fecha de conversion: 2026-10-25

**CONTROL DE VERSIONES**

| **VERSION** | **FECHA** | **MODIFICACIÓN** | **RESPONSABLE** | **DIVULGACIÓN/ REGLAMENTACIÓN** |
| --- | --- | --- | --- | --- |
| 1.0 | 24/04/2025 | Creación documento | Equipo técnico |  |
|  |  |  |  |  |
|  |  |  |  |  |

**APROBACIONES DEL COMITÉ DE DISEÑO DETALLADO**

A continuación, se deben listar las personas que aprueban el diseño detallado del requerimiento para poder dar paso al desarrollo del mismo.

Comités de diseño:

* Diseño detallado: Aprobaciones por COE (para el caso de servicios), director o coordinador, Infraestructura, Arquitectura, Seguridad de la Información en caso de que hayan participado en el requerimiento

| **SECCIÓN** | **NOMBRE Y APELLIDO** | **CARGO Y ÁREA** | **FECHA DE APROBACIÓN** |
| --- | --- | --- | --- |
| PO | Sandra Liliana Diaz | Product Owner Célula moneda extranjera |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

**TABLA DE CONTENIDO**

[INTRODUCCIÓN 3](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645428&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=9831f0fe-fbd9-4baf-8fc2-bca99b841644&McasHash=affb28f75e81ba5ef29009c0306306f1a456526ff134f3d1433d0bc178f88b27)

[1. DESCRIPCIÓN 4](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645429&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=aaad1492-4c7b-4972-aa1e-e6e600ef0c01&McasHash=357feddcf93c41411116d2929282554aa2aea6a8af26fb1824822910553f2255)

[2. DISEÑO DETALLADO 4](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645430&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=77bdf2a6-22c3-4be0-b48c-c7dd464c030b&McasHash=1eb0838aff5cf976c028b5c443f1de07dbcbe93fdffba717cb8d678ac7c0d060)

[2.1. PROCESOS DE DEPURACIÓN 7](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645431&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=6683c4a0-62f5-46de-8681-8d33a5ca66d9&McasHash=e3101d05f5c8295e9802f013f22326408de6db31b8cfe2e2178be815871d79fe)

[2.2. COPIAS DE SEGURIDAD O BACKUP 7](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645432&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=7713a49b-f928-4308-9023-122b1ba53394&McasHash=61b1bb93f3c5e882dc86bb1658658765ff9f3a182c3bcef5d9f6ac6dc703982c)

[3. DESARROLLO DEL REQUERIMIENTO (Si aplica) 8](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645433&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=6b52f409-903d-44bb-aa27-fb31bdc1364a&McasHash=9378307dadabea9805e4458dc2ff7d00b5a305472dce4682b98c81473c32228e)

[3.1. DETALLAR COMPONENTES ADICIONALES 8](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645434&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=3927dc63-2ef6-4236-8dc8-b2d26261afdd&McasHash=963d4c1bfc7e6b17237ec29148d989b7cd89cdedc3e2d064a94b86ed8fc168da)

[3.2. DETALLAR FUNCIONALIDADES 9](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645435&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=4f17674f-e20a-4842-ae27-b22743487567&McasHash=fd7d3a15c6b3f4e1d0cc431baff08a5eda75656f7dc4ec9f46f84e7b297c88d0)

[4. ANEXOS 11](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645437&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=e68e2269-f2d8-4c94-abe3-0935f5e39bae&McasHash=404e72f861c6a83e783905abb1b805da62b9f0a5498ebe6aabca58364beea181)

[5. VERIFICACIONES ADICIONALES 12](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645438&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=62932b79-79b4-4325-97f4-1d58a1ce6b82&McasHash=6bab2f7d4d165cc488d46722320eaf05e3be17db6cb469250bd9014d35b7d84e)

[6. CASOS DE PRUEBAS UNITARIAS 12](https://word-edit.officeapps.live.com.mcas.ms/mcasapi/McasPoliciesEndPoint/v2?policy=NativeApps&redir=0&McasSrc=bookmark%3A%2F%2F_Toc490645439&McasUserAuth=casBF3NoYXJlZC1uaXB0dWNrLTIwMjAwODA5c79Rd2_Ze6vglHw1CUNKKLC1vVq5pH_Amo1YVueM_gKv4iIavTl7JqGCqXwDefn1i1X1M3INoXrq4SrVq_lIlbqTN3jvOqZYJVaBZ8eFPOdyJQFQKyItnJXOsS-WwAEyq8eRX3CP325j-YwW9bKCm4-TWIdsq4JAQnY3TGNtEo5EekAdViOCl17dbqjMOVTPtR5C1CciC_jDRlf8tALUx0Se_PkJjv_gtf8pSunKU5HCI5Y9oLJWXJ_moZxLrV6kaNeHD6cpyIhNtWzFbhAhFjs78xL6jigk19O43nByEseWwVGBBn9sutnHwNtbOu5WoTV4qulqgdvxyQLYEIahmUKwbQ0qXlIaRbXkyd9AsNUFFNXBDiSRQTy80cDixCC4MPmyRDpldU5gz445Faw6ZdNqJatohdmmJm9aXS62TQrmkVHbBxvmVHGtk7kyqMeXtjwDyldJCJtB_3PpiqU87g&McasTsid=20892&McasId=d91fde7b-89ba-4382-b799-4ce19b384ab7&McasHash=72d7fb9098b9aecebced2772b93811adeec617f94deabd4f50361cfc598d1212)

**INTRODUCCIÓN**

Este documento provee una representación de diseño detallado del Componente de integración WMB (Flujo) que implementa “**IntegracionBankTrade**” el cual les permite a los flujos desplegados de Message Bróker realizar las transformaciones de mensajería y actividades de comunicación requeridas para el intercambio de mensajería con la solución BankTrade del Banco de Occidente.

1. **DESCRIPCIÓN**

**Descripción del requerimiento:**

Banco de Occidente trabaja las implementaciones de flujos bajo un esquema de capas, cada capa es la responsable de realizar actividades específicas y bien definidas. Bajo este esquema se ha identificado que para poder intercambiar cualquier tipo de información o realizar cualquier transacción con el sistema de comercio exterior BankTrade se requiere realizar actividades como son, “Transformar al formato propietario BankTrade” y “Comunicarse”, para poder ejecutar estas actividades en Message Bróker se han establecido dos flujos que tendrán dicha responsabilidad : “IntegracionBankTrade y ComunicacionBankTrade”

1. **DISEÑO DETALLADO**

**[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]**

Gráfico 1. Diagrama de Contexto

| <BANKTRADE > | |
| --- | --- |
| **Componente 1. n:** | INTEGRACIONBANKTRADE |
| **Tipo:** | XML |
| **Tipo de Cambio:** | Transformación |
| **Descripción:** | Flujo FMG que se encarga de transformar el mensaje de XML a trama plana para enviar al flujo de comunicación hacia BankTrade. |

| < BANKTRADE> | |
| --- | --- |
| **Componente 2. n:** | BANKTRADE |
| **Tipo:** | MR – FORMATO MENSAJE |
| **Tipo de Cambio:** | MQ – PROTOCOLO DE TRANSPORTE |
| **Descripción:** | Core Moneda Extranjera. |

| < BANKTRADE> | |
| --- | --- |
| **Componente 3. n:** | Websphere Message Bróker |
| **Tipo:** | XML |
| **Tipo de Cambio:** | IMPLEMENTACIÓN |
| **Descripción:** | Solución middleware de IBM utilizada por Banco de Occidente para realizar la implementación de su ESB corporativo |

1. **DETALLAR COMPONENTES ADICIONALES**

A continuación, se detalla deferentes flujos o componentes WMB que participan en la solución detallada.

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

Gráfico 2. Diagrama de Componentes de Integración

| Nombre | Descripción | Tipo | Mensaje Entrada | Mensaje Salida |
| --- | --- | --- | --- | --- |
| IntegracionBankTrade | Componente Framework responsable de la transformación del mensaje de formato canónico a formato BankTrade y de realizar la comunicación con dicho sistema. | Subflujo | XML/Canónico | XML/Canónico |
| ComunicacionBankTrade | Componente Framework responsable de la comunicación con BankTrade. | Subflujo | MRM | MRM |
| ManejoMonitoreo | Componente MessageFlow genérico responsable realizar el registro en BD de los mensajes de error que se produzcan en los flujos. | Flujo | XML/  Especifico/  MQ | No Genera Respuesta |
| Auditoría | Componente MessageFlow genérico responsable de registrar en BD a manera de auditoría toda la información de transacciones procesadas. | Flujo | XML/  Especifico/  MQ | No Genera Respuesta |

1. **DETALLAR FUNCIONALIDADES**

El servicio técnico de Integración BankTrade es el responsable de garantizar un intercambio de mensajería de forma exitosa entre BankTrade y WMB, para esto deberá realizar actividades específicas como son: transformar el mensaje al formato especifico BankTrade y realizar la comunicación con BankTrade, al igual tiene la responsabilidad enviar la auditoria de todas las transacciones procesadas.

* **IntegracionBankTrade**

**Descripción de la Operación**

Este flujo tiene por objetivo permitirles a flujos WMB realizar las transformaciones de mensaje a formato trama plana para intercambiar mensajería con el sistema BankTrade. Esta operación se implementará con el flujo IntegracionBankTrade el cual se presenta a continuación:

**Diagrama Subflujo IntegracionBankTrade**

Gráfico 4. IntegracionBankTrade

**Diagrama Subflujo ComunicaciónBankTrade**

Gráfico 5. ComunicacionBankTrade

**Mensaje de Entrada (Request)**

A continuación, se brinda los detalles técnicos asociados con el mensaje de entrada al Flujo IntegracionBankTrade.

| Dominio mensaje: | XMLNSC |
| --- | --- |
| Tipo Mensajería : | Canónico |
| Mensaje de Entrada: | PeticionEspecifica |
| Elementos del Mensaje: | El detalle del mensaje de entrada es dinámico acorde al servicio a consumir en BankTrade. |

Tabla 5.

**Mensaje de Salida (Response)**

A continuación, se brinda los detalles técnicos asociados con el mensaje de salida del Flujo IntegracionBankTrade.

| Dominio mensaje: | XMLNSC |
| --- | --- |
| Tipo Mensajería : | Canónico |
| Mensaje de Entrada: | RespuestaEspecífica |
| Elementos del Mensaje: | El detalle del mensaje de respuesta es dinámico acorde al servicio a consumir en BankTrade. |

Tabla 6.

**Diagrama de Secuencia**

**Gráfico 6. Diagrama de Secuencia**

A continuación, se detallan las actividades y secuencias relacionadas con el flujo objeto del diseño Integración y ComunicacionBankTrade.

1. Llega un mensaje al nodo de entrada de IntegracionBankTrade.
2. Se transforma el mensaje canónico recibido a formato trama plana:

* En la tabla TBL\_CACHE\_COLAS, se debe insertar el registro del nombre del servicio y asignar un nombre para el message set del mismo.
* Para realizar el parseo con el message set respectivo, se debe realizar la consulta a la base de datos (utilizando el mismo proceso que se maneja para obtener el nombre de las colas en el Listener Flow, con la tabla TBL\_CACHE\_COLAS).

1. Se envía el mensaje transformado al flujo de ComunicacionBankTrade.
2. Se almacena en variables de ambiente el MsgId para correlacionar el mensaje de respuesta.
3. Se envía el mensaje a la cola MQ respectiva de BankTrade.
4. BankTrade toma el mensaje, lo procesa y genera la respuesta.
5. BankTrade envia el mensaje a la cola MQ de respuesta respectiva.
6. El flujo de comunicación procesa el mensaje de respuesta
7. Al ser la operación exitosa se genera el mensaje para auditoría y se envía a la cola respectiva.
8. El flujo de comunicación envía el mensaje de respuesta al flujo de integración.
9. El flujo de integración transforma el mensaje de respuesta a formato canónico XML y envía el mensaje al flujo que lo invoco.

**Flujo Alternativo Error en Comunicación**

1. Si el mensaje de respuesta no se recibe en el tiempo esperado (10 segundos).
2. Se genera el mensaje de monitoreo y se envía a la cola respectiva.
3. Se responde al flujo de integración por la terminal de error.
4. Se respondo al flujo que invoco el servicio por la terminal de error.
5. **VERIFICACIONES ADICIONALES**

**Dependencias del Servicio**

| **Componente** | **Tipo** | **Protocolo** |
| --- | --- | --- |
| QManager BankTrade | QManager | MQ |
| ManejoMonitoreo | Flujo | MQ |
| Auditoría | Flujo | MQ |

**Tabla 5**

**Premisas Generales**

| **Tipo** | **Descripción del Requerimiento** |
| --- | --- |
| **Auditoria** | **Se debe enviar un mensaje al flujo de auditoría en el flujo de comunicación de todas las transacciones procesadas.** |
| **Constantes** | **Las constantes deberán trabajarse utilizando el archivo de constantes .ESQL** |
| **Manejo de Excepciones** | **Toda excepción que se produzca al interior del flujo deberá ser responsabilidad de este y deberá reportarla a la cola de ManejoMonitoreo\_IN con base en el mensaje de entrada especificado para el flujo ManejoMonitoreo.** |

**Tabla 6**

**Requerimientos No Funcionales**

| **ID** | **Tipo** | **Descripción del Requerimiento** |
| --- | --- | --- |
| **RNF-3** | **Desempeño** | **El tiempo óptimo para que el ESB retorne la respuesta a los aplicativos impactados en 10 segundos.** |
| **RNF-4** | **Disponibilidad** | **El servicio expuesto en el ESB debe estar disponible el 99.5% del mes.** |

**Tabla 7**

**Políticas**

Para este servicio no se han establecido políticas (WS-Policys), que controlen, restrinjan o informen sobre los detalles de su operación. Los requerimientos no funcionales deberán ser controlados con mecanismos alternos.

**Decisiones de Realización**

| **Tema** | **Estrategia utilizada para la comunicación con los sistemas legados** |
| --- | --- |
| **Contexto** | **La integración con sistemas legados puede generar particularidades técnicas las cuales se pueden ver como tareas repetitivas, ya que una gran cantidad de flujos podrían requerir integrarse con el mismo sistema.** |
| **Problema** | **¿Qué estrategia será utilizado para comunicarse con los sistemas externos?** |
| **Alternativas** | **1. Desde cada flujo establecer la comunicación acorde al protocolo y mensaje de cada sistema externo**    **2. Delegar la responsabilidad de integración a un único componente MessageFlow (Flujo) con interfaz MQ.**    **3. Delegar la responsabilidad de integración a un único componente MessageFlow (Subflujo) con interfaz interna (Solo WMB).** |
| **Decisión** | **Se opta por la alternativa número 3.** |
| **Justificación** | **Se desea que las unidades de despliegue incluyan las responsabilidades de integración, y que estas no estén delegadas en otro flujo.** |
