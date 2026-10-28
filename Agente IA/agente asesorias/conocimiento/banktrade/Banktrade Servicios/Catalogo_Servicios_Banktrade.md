> Catálogo generado a partir de los archivos WSDL/XSD originales. Este documento es un **resumen de consulta rápida**;
> los archivos `.wsdl`/`.xsd` de cada carpeta siguen siendo la fuente de verdad técnica (tipos de datos exactos,
> restricciones, imports, etc.).
> Fecha de generación: 2026-10-27

# Catálogo de Servicios Web Banktrade

Todos los servicios son **Web Services SOAP** (`document/literal`, transporte `http://schemas.xmlsoap.org/soap/http`).
Todos comparten el mismo patrón de mensaje: un **Encabezado de Entrada/Salida común** (`EncabezadosSOA.xsd`) más un
bloque de datos propio de la operación (`*Entrada` / `*Salida`).

## Encabezados comunes (EncabezadosSOA.xsd)

Presentes en el mensaje de entrada y salida de **todos** los servicios:

**EncabezadoEntrada**
| Campo | Tipo |
| --- | --- |
| AplCod | integer |
| TrmnalId | string |
| SesionId | string |
| PtcionId | string |
| Usrio | string |
| PtcionFecha | dateTime |

**EncabezadoSalida**
| Campo | Tipo |
| --- | --- |
| PtcionId | string |
| RtaCod | string |
| RtaMnsje | string |
| SistMnsje | string |
| MasMnsjes | boolean |

---

## 1. NotificacionCumpNegocDivisas

- **Carpeta:** `Banktrade Servicios/NotificacionCumpNegocDivisas/`
- **Documento de diseño relacionado:** [Diseno_Servicio_NotificacionCumpNegocDivisas.md](../docs/Diseno_Servicio_NotificacionCumpNegocDivisas.md)
- **Namespace WSDL:** `http://bancodeoccidente.com.co/Servicios/Negocio/Administracion/wsdl/NotificacionCumpNegocDivisas`
- **Endpoint (WSDL):** `http://localhost:80/NotificacionCumpNegocDivisasService/NotificacionCumpNegocDivisasPort` *(placeholder, no es la URL real de ambiente)*
- **PortType:** `NotificacionCumpNegocDivisasPortType`

### Operación: `notificarCumpNegocDivisas`
- **SOAPAction:** `http://bancodeoccidente.com.co/Servicios/Negocio/Administracion/wsdl/NotificacionCumpNegocDivisas/NewOperation`
- **Mensaje de entrada** (`NotificarCumpNegocDivisas`): Encabezado + `NotificarCumpNegocDivisasEntrada`
  | Campo | Tipo |
  | --- | --- |
  | OperacionCodigo | dic:OperacionCodigo_type |
- **Mensaje de salida** (`NotificarCumpNegocDivisasRta`): solo Encabezado de Salida (no agrega campos propios de negocio).

---

## 2. ReversoTransaccion

- **Carpeta:** `Banktrade Servicios/ReversoTransaccion/`
- **Namespace WSDL:** `http://bancodeoccidente.com.co/Servicio/Negocio/Administracion/wsdl/ReversoTransaccion`
- **Endpoint (WSDL):** `http://10.120.22.130:4800/ReversoTransaccionService/ReversoTransaccionPort`
- **PortType:** `ReversoTransaccionPortType`

Expone **dos operaciones**:

### Operación: `ReversarTransaccion`
- **SOAPAction:** `http://bancodeoccidente.com.co/Servicio/Negocio/Administracion/wsdl/ReversoTransaccion/ReversarTransaccion`
- **Mensaje de entrada** (`ReversarTransaccion`): Encabezado + `ReversarTransaccionEntrada`
  | Campo | Tipo | Obligatorio |
  | --- | --- | --- |
  | CompensacionFecha | dic:CompensacionFecha_type | No |
  | ReversoMotivoCodigo | dic:ReversoMotivoCodigo_type | No |
  | OrigenPtcionId | dic:OrigenPtcionId_type | No |
- **Mensaje de salida** (`ReversarTransaccionRta`): Encabezado + `ReversarTransaccionSalida`
  | Campo | Tipo | Obligatorio |
  | --- | --- | --- |
  | RespuestaAdvertenciaCodigo | dic:RespuestaAdvertenciaCodigo_type | No |
  | RespuestaAdvertenciaCodigoDesc | dic:RespuestaAdvertenciaCodigoDesc_type | No |

### Operación: `AnularTransaccion`
- **SOAPAction:** `http://bancodeoccidente.com.co/Servicio/Negocio/Administracion/wsdl/ReversoTransaccion/AnularTransaccion`
- **Mensaje de entrada** (`AnularTransaccion`): Encabezado + `AnularTransaccionEntrada`
  | Campo | Tipo | Obligatorio |
  | --- | --- | --- |
  | CompensacionFecha | dic:CompensacionFecha_type | No |
  | ReversoMotivoCodigo | dic:ReversoMotivoCodigo_type | No |
  | OrigenPtcionId | dic:OrigenPtcionId_type | No |
  | TrxNumAsoc | dic:TrxNumAsoc_type | No |
  | UsrioAsoc | dic:UsrioAsoc_type | No |
- **Mensaje de salida** (`AnularTransaccionRta`): Encabezado + `AnularTransaccionSalida`
  | Campo | Tipo | Obligatorio |
  | --- | --- | --- |
  | RespuestaAdvertenciaCodigo | dic:RespuestaAdvertenciaCodigo_type | No |
  | RespuestaAdvertenciaCodigoDesc | dic:RespuestaAdvertenciaCodigoDesc_type | No |

> Nota: el WSDL también declara un tipo `AnularTransaccion`/`AnularTransaccionResponse` simplificado (`in`/`out` string)
> dentro de `wsdl:types`, que parece residual de una plantilla auto-generada y no se usa en el binding real (el binding
> usa los mensajes basados en `AnularTransaccion.xsd`).

---

## 3. DebitoCreditoCuentaPorComex

- **Carpeta:** `Banktrade Servicios/DebitoCreditoCuentaPorComex/`
- **Namespace WSDL:** `http://bancodeoccidente.com.co/Servicios/Negocio/Administracion/wsdl/DebitoCreditoCuentaPorComex`
- **Endpoint (WSDL):** `http://10.120.22.195:20004/DebitoCreditoCuentaPorComexService/DebitoCreditoCuentaPorComexPort`
- **PortType:** `DebitoCreditoCuentaPorComexPortType`

### Operación: `debitarAcreditarCuenta`
- **SOAPAction:** `http://www.example.org/DebitoCreditoCuentaPorComex/NewOperation` *(placeholder genérico, no personalizado)*
- **Mensaje de entrada** (`DebitarAcreditarCuenta`): Encabezado + `DebitarAcreditarCuentaEntrada`
  | Campo | Tipo |
  | --- | --- |
  | ProductoTipo | dic:ProductoTipo_type |
  | EsExtemporaneo | dic:EsExtemporaneo_type |
  | OperacionCodigo | dic:OperacionCodigo_type |
  | Producto | dic:Producto_type |
  | TrxNum | dic:TrxNum_type |
  | TrxTipo | dic:TrxTipo_type |
  | NotaDesc | dic:NotaDesc_type |
  | TransaccionValor | dic:TransaccionValor_type |
- **Mensaje de salida** (`DebitarAcreditarCuentaRta`): Encabezado + `DebitarAcreditarCuentaSalida`
  | Campo | Tipo |
  | --- | --- |
  | Autorizacion | dic:Autorizacion_type |

---

## 4. ConsultaTitularidad

- **Carpeta:** `Banktrade Servicios/ConsultaTitularidad/`
- **Namespace WSDL:** `http://bancodeoccidente.com.co/Servicios/Negocio/Consulta/wsdl/ConsultaTitularidad`
- **Endpoint (WSDL):** `http://10.120.16.205:4800/ConsultaTitularidadService/ConsultaTitularidadPort`
- **PortType:** `ConsultaTitularidadPortType`

### Operación: `consultarTitularidadDetallada`
- **SOAPAction:** `http://bancodeoccidente.com.co/Servicios/Negocio/Consulta/wsdl/ConsultaTitularidad/consultarTitularidadDetallada`
- **Mensaje de entrada** (`consultarTitularidadDetallada`): Encabezado + `consultarTitularidadDetalladaEntrada`
  | Campo | Tipo | Obligatorio |
  | --- | --- | --- |
  | OperacionCodigo | dic:OperacionCodigo_type | No |
  | OficinaCodigo | dic:OficinaCodigo_type | **Sí** |
  | OfcnaNom | dic:OfcnaNom_type | **Sí** |
  | CiudadCodigo | dic:CiudadCodigo_type | No |
  | JornadaCodigo | dic:JornadaCodigo_type | No |
  | CompensacionFecha | dic:CompensacionFecha_type | **Sí** |
  | ProductoTipo | dic:ProductoTipo_type | **Sí** |
  | Producto | dic:Producto_type | **Sí** |
  | PrdctoInfo | dic:PrdctoInfo_type | No |
  | ModoEntrada | dic:ModoEntrada_type | No |
- **Mensaje de salida** (`consultarTitularidadDetalladaRta`): Encabezado + `consultarTitularidadDetalladaSalida`
  | Campo | Tipo | Obligatorio |
  | --- | --- | --- |
  | IdentificacionTipo | dic:IdentificacionTipo_type | **Sí** |
  | Identificacion | dic:Identificacion_type | **Sí** |
  | ClienteNombre | dic:ClienteNombre_type | **Sí** |
  | Autorizacion | dic:Autorizacion_type | **Sí** |

---

## 5. ConsultaClienteYContactos

- **Carpeta:** `Banktrade Servicios/ConsultaClienteYContactos 1/`
- **Namespace WSDL:** `http://bancodeoccidente.com.co/Servicios/Negocio/Consulta/wsdl/ConsultarDatosClienteYContactos`
- **Endpoint (WSDL):** `http://DPBOCC:7800/ConsultaClienteYContactosService/ConsultaClienteYContactosPort`
- **PortType:** `ConsultaClienteYContactosPortType`

### Operación: `consultarDatosClienteYContactos`
- **SOAPAction:** `http://www.example.org/ConsultaClienteYContactos/NewOperation` *(placeholder genérico)*
- **Mensaje de entrada** (`ConsultarDatosClienteYContactos`): Encabezado + `ConsultarDatosClienteYContactosEntrada`
  | Campo | Tipo |
  | --- | --- |
  | IdentificacionTipo | dic:IdentificacionTipo_type |
  | Identificacion | dic:Identificacion_type |
  | CntactoTipo | dic:CntactoTipo_type |
- **Mensaje de salida** (`ConsultarDatosClienteYContactosRta`): Encabezado + `ConsultarDatosClienteYContactosSalida`.
  Es el servicio con el **mayor número de campos de respuesta** del catálogo (información demográfica, direcciones,
  teléfonos, representante legal, contactos, sedes, etc.). Entre los principales:
  | Campo | Tipo |
  | --- | --- |
  | EstCod | dic:EstCod_type |
  | PrdctoDesc | dic:PrdctoDesc_type |
  | PersonaTipo | dic:PersonaTipo_type |
  | IdentificacionTipo | dic:IdentificacionTipo_type |
  | Identificacion | dic:Identificacion_type |
  | CliNomPrmro / CliNomSgndo | dic:CliNomPrmro_type / CliNomSgndo_type |
  | CliApellPrmro / CliApellSgndo | dic:CliApellPrmro_type / CliApellSgndo_type |
  | RazonSocial / NombreComercial | dic:RazonSocial_type / NombreComercial_type |
  | ClienteEst / ClienteNivel | dic:ClienteEst_type / ClienteNivel_type |
  | Sexo / CivilEst / Profesion / Ocupacion | — |
  | NactoFecha / NactoPais / NactoDepto / NactoCiudad / Nacionalidad | — |
  | EsClinton / EsVIP / EsListaSeg / EsSIPLA / EsSegBca | indicadores booleanos/código de riesgo y cumplimiento |
  | InfoDir (bloque repetible) | Dirección: DirTipo, Dir, Ciudad, Depto, Pais, CrmPerfilNum |
  | InfoTelefono (bloque repetible) | Teléfono: TelTipo, Tel, Ciudad, Depto, Pais, TelCrmPerfilNum |
  | RepresentanteLegal (bloque) | IdentificacionTipo, Identificacion, Nombre |
  | InfoCntactoDatos (bloque) | CliApellPrmro, CliApellSgndo, ClienteNombre, Tel |
  | InfoCorreoElectronico (bloque) | TipoCorreoElectronico, CorreoElectronico, CorreoCrmPerfilNum |
  | InfoSedes / InfoSede (bloque repetible, `maxOccurs="unbounded"`) | Información de sedes asociadas al cliente |

  > El detalle completo de este mensaje de salida (más de 30 campos y sub-bloques) está en
  > `xsd/ConsultarDatosClienteYContactos.xsd`; consulta ese archivo si necesitas el listado exhaustivo o los tipos
  > exactos de cada campo.

---

## Resumen comparativo

| Servicio | Operación(es) | Tipo | Endpoint |
| --- | --- | --- | --- |
| NotificacionCumpNegocDivisas | notificarCumpNegocDivisas | Notificación | localhost (placeholder) |
| ReversoTransaccion | ReversarTransaccion, AnularTransaccion | Transaccional | 10.120.22.130:4800 |
| DebitoCreditoCuentaPorComex | debitarAcreditarCuenta | Transaccional | 10.120.22.195:20004 |
| ConsultaTitularidad | consultarTitularidadDetallada | Consulta | 10.120.16.205:4800 |
| ConsultaClienteYContactos | consultarDatosClienteYContactos | Consulta | DPBOCC:7800 |

## Diccionario de tipos (`Diccionario.xsd`)

Todos los servicios importan `base/Diccionario.xsd` (uno por carpeta de servicio, con el mismo contenido) para los
tipos de datos de negocio (`dic:*_type`). Revisa ese archivo dentro de la carpeta `xsd/base/` de cada servicio si
necesitas restricciones exactas (longitudes, patrones, enumeraciones) de un campo puntual.
