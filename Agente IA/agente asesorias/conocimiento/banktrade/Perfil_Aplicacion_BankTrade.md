> Ficha técnica de arquitectura. Complementa (no reemplaza) los documentos funcionales en
> `docs/` y el catálogo de servicios en `Banktrade Servicios/Catalogo_Servicios_Banktrade.md`.
> Última actualización: 2026-10-28 (revisada tras incorporar el diagrama oficial de
> infraestructura — ver `Infraestructura_Banktrade.md`). Partes marcadas como
> "⚠️ Por confirmar" siguen pendientes de validar con el equipo/proveedor antes de usarse para
> decisiones críticas.

# Perfil de Aplicación — BankTrade

## 1. Resumen del perfil

| Campo | Valor |
|---|---|
| Nombre | BankTrade |
| Dominio funcional | COMEX (Comercio Exterior) — cartas de crédito, cobranzas, préstamos, giros, remesas, FX, etc. |
| Infraestructura | On-premise |
| Modelo de soporte | Tercerizado (proveedor externo) |
| Tecnología del núcleo | COBOL legacy (ambiente tipo AIX) |
| Tecnología de capas adicionales | Java (front), WebLogic, IIS, Windows Services |
| Tipos de integración | Webservices SOAP (vía ESB), colas MQ, interfaces batch, Recon |

## 2. Arquitectura por capas (confirmada con el diagrama oficial de infraestructura)

```
┌─────────────────────────────────────────────────────────────┐
│  Usuarios Banktrade/Clientrade → https → Firewall interno     │
└───────────────┬─────────────────────────────────────────────┘
                │
     ┌──────────┴───────────┐
     │                       │
┌────┴─────────────────┐ ┌───┴───────────────────────────────┐
│ Servidor Windows A     │ │ Servidor Windows B (otro servidor) │
│ Oracle WebLogic 14     │ │ IIS 10 + .NET 4.8                  │
│ IIS 10 + Java 11       │ │ "CT Absorber/Collector", TS Online │
│ Webprinting, AlertU,   │ │ /BIP .NET, Central Collector,      │
│ BT Imaging, UC HTML    │ │ RECON, BTS.W/S, IPSATP             │
└────────────┬───────────┘ └───┬─────────────────────────────┘
             │                  │
             └─────────┬────────┘
                        │ (MQ / webservices SOAP vía ESB)
┌───────────────────────┴───────────────────────────────────────┐
│  NÚCLEO "Banktrade v17" — AIX 7.2 (PowerVM)                     │
│  BIS ClientTrade, BIS OPAS, BIS RECON, BIS Ventanilla            │
│  MQ Client 9.1, Oracle Client 19, Java 11                       │
│  (Producción: clúster de 2 nodos con filesystem GPFS compartido) │
│  Contiene la base de datos y ~300+ tablas documentadas en        │
│  Banktrade_Database_Diccionario_Tablas.md / Banktrade_DataDictionary.csv │
└───────────────────────┬───────────────────────────────────────┘
                        │
┌───────────────────────┴───────────────────────────────────────┐
│  BASE DE DATOS                                                  │
│  SQL Server (Windows, instancia SDCOMEX) — Tradestats/AlertU/    │
│  Imaging/RECON   +   Oracle Database (AIX, instancia QDCOMEX;    │
│  RAC de 2 nodos en Producción) — core Banktrade                  │
└─────────────────────────────────────────────────────────────────┘
```

> Detalle completo por ambiente (servidores, IPs, versiones de SO) en
> [`Infraestructura_Banktrade.md`](./Infraestructura_Banktrade.md).

## 3. Detalle por componente

| Componente | Tecnología | Función (según lo informado) | Estado |
|---|---|---|---|
| Front de usuario | Java sobre WebLogic 14 + IIS 10 + Java 11, en servidores Windows Server 2019 (VMware) | Webprinting, AlertU, BT Imaging, UC HTML. Interfaz para usuarios de la Gerencia de Operaciones; control de acceso por segmento de usuario | Confirmado (servidor y stack verificados en el diagrama oficial) |
| Servicios en IIS | IIS 10 + .NET 4.8, en **otro** servidor Windows Server 2019 distinto del front Java | Rotulado literalmente **"CT Absorber/Collector"**, junto con "TS Online/BIP .NET", "Central Collector", "RECON", "BTS.W/S" e "IPSATP" | Confirmado que así se llama y dónde corre; ⚠️ sigue sin confirmarse qué significa la sigla "CT" (el diagrama no lo define) |
| Windows Services | Servidores Windows Server 2019 (VMware) | Alojan el front Java/WebLogic y el servicio .NET/IIS "collector" (son 2 servidores Windows distintos, no uno solo) | Confirmado (ver `Infraestructura_Banktrade.md`) |
| Núcleo / backend | AIX 7.2 (PowerVM) — en Producción, clúster de 2 nodos con filesystem compartido GPFS | "Banktrade v17": BIS ClientTrade, BIS OPAS, BIS RECON, BIS Ventanilla. Stack: MQ Client 9.1, Oracle Client 19, Java 11 | Confirmado que corre en AIX; ⚠️ sigue sin confirmarse si este AIX ejecuta directamente el COBOL documentado en `Banktrade_Database_Diccionario_Tablas.md` o es una capa Java/MQ intermedia sobre ese COBOL |
| Recon | No es un servidor separado: aparece como función del servicio .NET/IIS "collector" **y** del servidor SQL Server (Tradestats Management) | Conciliación | Corrige lo informado antes ("procesos batch propios" ⚠️ no confirmado por el diagrama) |
| Integración | Webservices SOAP (vía ESB), colas MQ (MQ Client 9.1 en el núcleo AIX) | Ver `Catalogo_Servicios_Banktrade.md` y los diseños de servicio en `docs/` | Confirmado |
| Base de datos | SQL Server (Windows, instancia SDCOMEX) + Oracle Database (AIX, instancia QDCOMEX; RAC de 2 nodos en Producción) | SQL Server soporta Tradestats/AlertU/Imaging/RECON; Oracle soporta el core Banktrade | Confirmado (ver `Infraestructura_Banktrade.md`) |

## 4. Relación entre el núcleo COBOL y las capas Java/WebLogic/IIS

El diagrama oficial de infraestructura (`Infraestructura_Banktrade.md`) **confirma que son
capas separadas y paralelas**, no que una reemplace a la otra:

1. Front Java/WebLogic (Windows) — Webprinting, AlertU, BT Imaging, UC HTML.
2. Servicio .NET/IIS "CT Absorber/Collector" (Windows, otro servidor) — Central Collector,
   RECON, BTS.W/S, IPSATP.
3. Núcleo "Banktrade v17" (AIX 7.2, PowerVM) — BIS ClientTrade, BIS OPAS, BIS RECON, BIS
   Ventanilla, con MQ Client + Oracle Client + Java 11.

⚠️ **Sigue pendiente de confirmar** si el AIX del punto 3 ejecuta directamente los programas
COBOL documentados en `Banktrade_Database_Diccionario_Tablas.md` (escenario más probable, ya
que la base de datos del core — tablas `L*` — vive en Oracle sobre ese mismo AIX), o si hay una
capa Java adicional entre ese AIX y el COBOL. El diagrama de infraestructura no distingue entre
"proceso COBOL" y "proceso Java" dentro del servidor AIX — solo muestra el servidor y su stack
instalado.

## 5. Relación con el conocimiento ya documentado

- El **diagrama de infraestructura** (`Infraestructura_Banktrade.md`) describe los servidores,
  IPs, SO y stack técnico por ambiente (Desarrollo/Pruebas/Producción) — es la fuente de
  verdad para esta ficha a partir de ahora.
- El **diccionario de tablas** (`Banktrade_Database_Diccionario_Tablas.md`) y el
  **diccionario de datos** (`Banktrade_DataDictionary.csv`) describen el **núcleo** (tablas
  `L*`), que corre sobre el servidor AIX documentado en `Infraestructura_Banktrade.md`.
- El **catálogo de servicios** (`Catalogo_Servicios_Banktrade.md`) describe los **webservices
  SOAP** expuestos vía ESB, consumidos/producidos por BankTrade — estos probablemente se
  comunican con el núcleo a través de alguna de las capas Java/WebLogic/IIS descritas
  arriba, pero el mapeo exacto capa-por-capa aún no está documentado.
- Los **diseños de servicio** (`Diseno_Servicio_*.md`) describen la lógica de negocio de
  integraciones puntuales (notificación de cumplimiento/negociación de divisas), que se
  apoyan en MQ — consistente con el MQ Client 9.1 instalado en el servidor AIX del núcleo.

## 6. Preguntas abiertas para seguir completando esta ficha

1. ¿Qué significa exactamente la sigla "CT" en "CT Absorber/Collector"? (el diagrama oficial
   no lo define, solo confirma el nombre y dónde corre)
2. ¿El servidor AIX del núcleo ejecuta directamente los programas COBOL documentados, o hay
   una capa Java/MQ intermedia entre ese AIX y el COBOL?
3. ¿Qué es exactamente el nodo "LTBOG109V" (Oracle Linux, Oracle DB 12c) visto solo en el
   ambiente de Pruebas? ¿Y la caja "SAP BD"/integración con correo mostrada ahí?
4. Confirmar el nombre exacto de la instancia Oracle RAC de Producción (VLAN 329).
