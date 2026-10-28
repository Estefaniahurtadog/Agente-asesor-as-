> Convertido automaticamente. Revisar tablas y diagramas antes de usar.
> Origen: documento2 (2).docx
> Fecha del original: 2026-10-25
> Fecha de conversion: 2026-10-25

Funcionalidad de la Lista OFAC – SAM Administración Listas de Riesgo

**1. Resumen**

La "Lista OFAC" (Office of Foreign Assets Control – Departamento del Tesoro de EE. UU., también conocida como *SDN List*) es uno de los listados de riesgo que administra el aplicativo **ALR (Administración de Listas de Riesgo)**. El sistema tiene dos frentes relacionados con esta lista:

1. **Cargue (Batch)**: proceso que descarga/recibe el archivo XML oficial de la OFAC y lo persiste en la tabla ALR\_TBL\_LISTAS\_NEGRAS.
2. **Consulta (Servicio SOAP)**: servicio ConsultarPersonaNegativoEJB que permite a otros sistemas del banco verificar si una persona/identificación/razón social está reportada en la lista OFAC (y en otras listas: ONU, Seguridad, Fraude).

Este documento describe ambos frentes, con énfasis en el **servicio de consulta**, sus parámetros de entrada/salida, y un análisis crítico de la lógica implementada.

<< RTF: Rich object >>

**2. Cargue de la lista OFAC (proceso Batch)**

**Módulo:** ALR\_AdministracionListasRiesgoBatch

| **Elemento** | **Detalle** |
| --- | --- |
| Archivo de origen | A099.DAT (constante NOMBRE\_ARCHIVO\_ONU\_OFAC), formato XML tipo *SDN List* de OFAC |
| Handler SAX | OFacHandler.java |
| Selección de handler | UtilidadesXML.java – método leerArchivoXMLSAX, selecciona OFacHandler cuando strTipoListaNegra == "OFC" |
| Orquestación | ProcesamientoCargueEJBBean.java |
| Tabla destino | ALR\_TBL\_LISTAS\_NEGRAS (entidad VacTblListasNegras), con STR\_TIPO\_LISTADO = 'OFC' |

**Lógica de parseo (OFacHandler)**

* Recorre cada nodo sdnEntry del XML (una entrada = una persona/entidad sancionada).
* Concatena lastName + firstName en el campo Nombre (evitando los nodos aka – alias).
* Toma publishDate como fecha de publicación de la lista.
* Por cada idNumber (ID\_NUMBER) encontrado dentro de una misma entrada, **clona** el registro (ArchivoDTO.clone()) generando una fila adicional por cada identificación asociada a la misma persona (una persona puede tener varios documentos/IDs reportados).
* El resultado (List<ArchivoDTO>) se entrega a la capa de persistencia (FachadaVacTblListasNegrasEJBLocal) para insertarlo en ALR\_TBL\_LISTAS\_NEGRAS con tipo de listado OFC y estado activo.

Este flujo no es el foco principal de la pregunta, pero es la fuente de datos que consulta el servicio descrito en la sección 3.

**3. Servicio que se ejecuta: ConsultarPersonaNegativoEJB.consultarClienteNegativo**

**Módulo:** ALR\_AdministracionListasRiesgo (Model) **Clase:** ConsultarPersonaNegativoEJBBean.java **EJB:** @Stateless(name = "ConsultarPersonaNegativoEJB", mappedName = "ALR-ConsultarPersonaNegativoEJB") **Operación SOAP:** ConsultarClienteNegativo (WSDL ConsultaClientesReportadosService.wsdl, XSD ConsultarClienteNegativo.xsd) **Método Java:** consultarClienteNegativo(MnsjeEntradaType input) : MnsjeSalidaType

Este es el servicio que efectivamente **consulta la lista OFAC**, junto con las listas ONU, Seguridad (LSG) y Fraude (FRD), en una sola invocación.

**3.1 Parámetros de entrada**

El mensaje de entrada (MnsjeEntradaType) se compone de un encabezado técnico estándar SOA y el cuerpo propio del servicio:

**EncabezadoEntrada (EncabezadoEntradaType)**

| **Campo** | **Tipo** | **Obligatorio** | **Descripción** |
| --- | --- | --- | --- |
| AplCod | int | Sí | Código de aplicación/canal que invoca el servicio |
| TrmnalId | string | Sí | Identificador de la terminal/máquina origen |
| SesionId | string | Sí | Identificador de sesión |
| PtcionId | string | Sí | Identificador de la petición (se retorna igual en la salida, útil para trazabilidad) |
| Usrio | string | Sí | Usuario que realiza la consulta |
| PtcionFecha | dateTime | Sí | Fecha/hora de la petición |

**ConsultarClienteNegativoEntrada (ConsultarClienteNegativoEntradaType)**

| **Campo** | **Tipo** | **Descripción** |
| --- | --- | --- |
| IdentificacionTipo | string | Tipo de documento (CC, NIT, etc.) — se recibe pero **no se usa** en la lógica de búsqueda |
| Identificacion | string | Número de identificación/documento a buscar |
| RazonSocial | string | Nombre o razón social a buscar (se tokeniza por espacios para la búsqueda "LIKE") |

Nota: al menos uno de Identificacion o RazonSocial debe venir diligenciado; si ambos llegan vacíos el servicio responde error técnico (IDENTIFICACION\_RAZON\_SOCIAL).

**3.2 Parámetros de salida**

**EncabezadoSalida (EncabezadoSalidaType)**

| **Campo** | **Tipo** | **Descripción** |
| --- | --- | --- |
| PtcionId | string | Eco del PtcionId recibido |
| RtaCod | string | Código de respuesta (0000 exitoso, 0002 error técnico, 0020 sin registros) |
| RtaMnsje | string | Mensaje de respuesta asociado al código |
| SistMnsje | string | Mensaje adicional/detalle técnico (en algunos casos incluye e.getMessage() de la excepción) |
| MasMnsjes | boolean | Indicador de "hay más datos" (paginación) |

**ConsultarClienteNegativoSalida (ConsultarClienteNegativoSalidaType)**

* InfoClientes (0..1) → contiene de 1 a 200 elementos InfoCliente:

| **Campo** | **Tipo** | **Descripción** |
| --- | --- | --- |
| IdentificacionTipo | string | Siempre se retorna en blanco (" ") — no se resuelve el tipo real |
| Identificacion | string | Identificación del registro encontrado, rellenada con ceros a la izquierda hasta 14 posiciones |
| RazonSocial | string | Nombre almacenado en la lista negra (STR\_NOMBRE) |
| NvdadFecha | string | Fecha de reporte (DTM\_FECHA\_REPORTE) formateada yyyy-MM-dd. Para Seguridad/Fraude siempre viene en blanco (" ") |
| DescEst | string | Descripción textual del hallazgo, p. ej. *"El Cliente se encuentra en la lista OFAC"* |
| ListaSegNom | string | Nombre de la lista donde se encontró: Lista OFAC, Lista ONU, Lista de Seguridad o Lista de Fraude |

**3.3 Códigos de respuesta relevantes**

| **RtaCod** | **Significado** |
| --- | --- |
| 0000 | Transacción exitosa (se encontraron registros) |
| 0002 | Error técnico SAM (falla de validación, BD, o excepción no controlada) |
| 0020 | No se encontraron registros |

**4. Lógica de negocio (flujo interno del servicio)**

[IMAGEN: sin descripcion - DESCRIBIR EN TEXTO]

**4.1 Construcción de la búsqueda (consultarClientesNEgativosListS)**

Por cada tipo de lista se ejecuta una consulta JPA/JPQL contra la entidad VacTblListasNegras (tabla ALR\_TBL\_LISTAS\_NEGRAS):

* Si llegan **Identificación y Razón Social**: filtra por strNombre LIKE '%palabra%' (una condición AND por cada palabra de la razón social) **y** strIdentificacion = <valor exacto>.
* Si llega **solo Identificación**: filtra únicamente por strIdentificacion = <valor exacto>.
* Si llega **solo Razón Social**: filtra únicamente por strNombre LIKE.
* Siempre agrega: strTipoListado.strRangoValor IN (:tipo) y estado.strRangoValor = :strEstado (solo registros con estado lógico **ACTIVO**).

Para la lista OFAC específicamente, la búsqueda se ejecuta con tipo IN ('OFC', 'ONU') en una sola consulta combinada (listOnuOfac), y luego, al recorrer los resultados, se etiqueta cada fila como *"Lista OFAC"* o *"Lista ONU"* comparando strTipoListado.strRangoValor contra TipoListadoEnum.OFC ("OFC").

**4.2 Reglas de combinación de resultados**

El método evalúa combinaciones de las tres bolsas de resultados (listOnuOfac, seguridad, fraude) con bloques if/else if anidados que cubren: los tres con datos, solo OFAC/ONU, solo Seguridad, solo Fraude, o ninguno. **Todo este bloque de lógica está duplicado íntegramente dos veces** (ver sección 5), una vez para identificaciones con guion (NIT+DV) y otra para identificaciones simples (≤14 caracteres).

Ejemplo del servicio;

CONSULTA

<soapenv:Envelope xmlns:soapenv=[<u>http://schemas.xmlsoap.org/soap/envelope/</u>](https://mcas-proxyweb.mcas.ms/certificate-checker?login=false&originalUrl=http%3A%2F%2Fschemas.xmlsoap.org.mcas.ms%2Fsoap%2Fenvelope%2F%3FMcasTsid%3D20892&McasCSRF=7aa5c614f8d200e2369058e4a4d59abb64b9bc069fc39b1928bd9bb4408a55c1) xmlns:val=[<u>http://bancodeoccidente.com.co/Servicios/Negocio/Consulta/xsd/ValidarPersonaListasRestrictivas</u>](https://mcas-proxyweb.mcas.ms/certificate-checker?login=false&originalUrl=http%3A%2F%2Fbancodeoccidente.com.co.mcas.ms%2FServicios%2FNegocio%2FConsulta%2Fxsd%2FValidarPersonaListasRestrictivas%3FMcasTsid%3D20892&McasCSRF=7aa5c614f8d200e2369058e4a4d59abb64b9bc069fc39b1928bd9bb4408a55c1) xmlns:enc=[<u>http://bancodeoccidente.com.co/Servicios/Base/EncabezadosSOA</u>](https://mcas-proxyweb.mcas.ms/certificate-checker?login=false&originalUrl=http%3A%2F%2Fbancodeoccidente.com.co.mcas.ms%2FServicios%2FBase%2FEncabezadosSOA%3FMcasTsid%3D20892&McasCSRF=7aa5c614f8d200e2369058e4a4d59abb64b9bc069fc39b1928bd9bb4408a55c1)>

   <soapenv:Header/>

   <soapenv:Body>

      <val:ValidarPersonaListasRestrictivas>

         <enc:EncabezadoEntrada>

            <enc:AplCod>184</enc:AplCod>

            <enc:TrmnalId>19-268</enc:TrmnalId>

            <enc:SesionId>131</enc:SesionId>

            <enc:PtcionId>AMI270220171</enc:PtcionId>

            <enc:Usrio>77204</enc:Usrio>

            <enc:PtcionFecha>2014-09-03T10:02:23</enc:PtcionFecha>

         </enc:EncabezadoEntrada>

         <val:ValidarPersonaListasRestrictivasEntrada>

            <!--Optional:-->

            <val:NumeroIdentificacion>1015454</val:NumeroIdentificacion>

            <!--Optional:-->

            <val:NombreRazonSocial>Pepes</val:NombreRazonSocial>

         </val:ValidarPersonaListasRestrictivasEntrada>

      </val:ValidarPersonaListasRestrictivas>

   </soapenv:Body>

</soapenv:Envelope>

RESPUESTA

<S:Envelope xmlns:S=[<u>http://schemas.xmlsoap.org/soap/envelope/</u>](https://mcas-proxyweb.mcas.ms/certificate-checker?login=false&originalUrl=http%3A%2F%2Fschemas.xmlsoap.org.mcas.ms%2Fsoap%2Fenvelope%2F%3FMcasTsid%3D20892&McasCSRF=7aa5c614f8d200e2369058e4a4d59abb64b9bc069fc39b1928bd9bb4408a55c1)>

   <S:Body>

      <ValidarPersonaListasRestrictivasRta xmlns=[<u>http://bancodeoccidente.com.co/Servicios/Negocio/Consulta/xsd/ValidarPersonaListasRestrictivas</u>](https://mcas-proxyweb.mcas.ms/certificate-checker?login=false&originalUrl=http%3A%2F%2Fbancodeoccidente.com.co.mcas.ms%2FServicios%2FNegocio%2FConsulta%2Fxsd%2FValidarPersonaListasRestrictivas%3FMcasTsid%3D20892&McasCSRF=7aa5c614f8d200e2369058e4a4d59abb64b9bc069fc39b1928bd9bb4408a55c1) xmlns:ns0=[<u>http://bancodeoccidente.com.co/Servicios/Base/EncabezadosSOA</u>](https://mcas-proxyweb.mcas.ms/certificate-checker?login=false&originalUrl=http%3A%2F%2Fbancodeoccidente.com.co.mcas.ms%2FServicios%2FBase%2FEncabezadosSOA%3FMcasTsid%3D20892&McasCSRF=7aa5c614f8d200e2369058e4a4d59abb64b9bc069fc39b1928bd9bb4408a55c1)>

         <ns0:EncabezadoSalida>

            <ns0:PtcionId>AMI270220171</ns0:PtcionId>

            <ns0:RtaCod>0000</ns0:RtaCod>

            <ns0:RtaMnsje>Transacción exitosa</ns0:RtaMnsje>

            <ns0:SistMnsje/>

            <ns0:MasMnsjes>false</ns0:MasMnsjes>

         </ns0:EncabezadoSalida>

         <ValidarPersonaListasRestrictivasSalida>

            <Resultados>

               <Resultado>

                  <TipoLista>FTO</TipoLista>

                  <EnListasRestrictivas>N</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>LOT</TipoLista>

                  <EnListasRestrictivas>N</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>FRD</TipoLista>

                  <EnListasRestrictivas>N</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>CMP</TipoLista>

                  <EnListasRestrictivas>N</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>OFC</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>ONU</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>UEL</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>UKL</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>CSL</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>LSG</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

               <Resultado>

                  <TipoLista>LUC</TipoLista>

                  <EnListasRestrictivas>S</EnListasRestrictivas>

                  <IdentificadorBusqueda>20260929095340563375</IdentificadorBusqueda>

               </Resultado>

            </Resultados>

         </ValidarPersonaListasRestrictivasSalida>

      </ValidarPersonaListasRestrictivasRta>

   </S:Body>

</S:Envelope>
