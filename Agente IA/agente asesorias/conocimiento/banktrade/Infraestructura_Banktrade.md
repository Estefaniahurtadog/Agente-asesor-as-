> Transcripción del diagrama de infraestructura **"Infraestructura Banktrade V17.pdf"**
> (`originales/banktrade/Infraestructura Banktrade V17.pdf`).
> Proyecto: CQ209750 — Upgrade BankTrade V17. División de Tecnología — Subgerencia de
> Infraestructura. Elaboró/Diagramó: David Cañón.
> El PDF contiene 3 esquemas (uno por ambiente): Desarrollo (Esquema N°1, v1,
> 05/noviembre/2021), Pruebas (Esquema N°2, v1.2, 21/noviembre/2022) y Producción
> (Esquema N°3, v1.1, 21/noviembre/2022).
> Las IPs y nombres de servidor de Desarrollo y Producción fueron leídos con zoom alto sobre
> el diagrama y tienen **alta confianza**. Los de Pruebas se leyeron a menor zoom y algunos
> dígitos pueden tener error de transcripción (marcados igualmente, pero conviene confirmar
> contra el PDF si se requiere precisión exacta, p. ej. para firewall/redes).

# Infraestructura de BankTrade v17 (Desarrollo / Pruebas / Producción)

## 0. Patrón general (los 3 ambientes comparten esta forma)

```
Usuarios Banktrade/Clientrade → https → Firewall interno → Red LAN – CPD Bogotá
        → (Pruebas y Producción: Balanceador de carga) →
   VLAN "app" (servidores Windows + servidor(es) AIX "core")
        → VLAN "bd" (servidor(es) de base de datos)
        → SAN
```

Cada ambiente tiene **3 roles de servidor de aplicaciones** que se repiten:

1. **Webprinting / AlertU / BT Imaging / UC HTML** → Windows Server + **Oracle WebLogic 14 +
   IIS 10 + Java 11** (este es el front Java/WebLogic mencionado en `Perfil_Aplicacion_BankTrade.md`).
2. **"CT Absorber/Collector" / TS Online /BIP .NET / Central Collector / RECON / BTS.W/S /
   IPSATP** → Windows Server + **IIS 10 + .NET 4.8** (este es el servicio "collector" en IIS;
   la etiqueta literal del diagrama es **"CT Absorber/Collector"** — "CT" no se define en el
   PDF, pero queda documentado tal como aparece; es un servicio .NET independiente del front
   Java, corre en **otro** servidor Windows).
3. **Banktrade v17 / BIS ClientTrade / BIS OPAS / BIS RECON / BIS Ventanilla** → servidor
   **AIX 7.2 (PowerVM)** con **MQ Client 9.1 + Oracle Client 19 + Java 11** — este es el
   **núcleo** (core) de BankTrade.

Y **2 roles de base de datos**:

- **SQL Server** (Windows) — instancia para *Tradestats Management / AlertU / Imaging / RECON*.
- **Oracle Database** (AIX) — instancia para el **core Banktrade** (tablas `L*` documentadas en
  `Banktrade_Database_Diccionario_Tablas.md` / `Banktrade_DataDictionary.csv`).

---

## 1. Ambiente de Desarrollo (Esquema N°1, v1 — 05/nov/2021)

Red LAN – CPD Bogotá → Firewall interno → https → Usuarios Banktrade/Clientrade.
**Sin balanceador de carga** (acceso directo). VLAN 1127 (app) → VLAN 68 (BD) → SAN.

### Servidores de aplicaciones (VLAN 1127)

| Servidor | IP | SO / Plataforma | Rol funcional | Stack técnico |
|---|---|---|---|---|
| VWDSTABOG15-09 | 10.121.117.70 | Windows Server 2019 (VMware) | Webprinting, AlertU, BT Imaging, UC HTML | Oracle WebLogic 14, IIS 10, Java 11 |
| VWDSTABOG15-10 | 10.121.117.69 | Windows Server 2019 (VMware) | CT Absorber/Collector, TS Online/BIP .NET, Central Collector, RECON, BTS.W/S, IPSATP | IIS 10, .NET 4.8 |
| ADBOG03E | 10.121.117.75 | AIX 7.2 (PowerVM) | **Banktrade v17 (core)**, BIS ClientTrade, BIS OPAS, BIS RECON, BIS Ventanilla | MQ Client 9.1, Oracle Client 19, Java 11 |

### Servidores de base de datos (VLAN 68)

| Servidor | IP | SO / Plataforma | Motor / Instancia | Soporta |
|---|---|---|---|---|
| VWDSTABOG15-11 | 10.120.31.44 | Windows Server 2019 (VMware) | SQL Server, collation `Latin1_General_CP1_CI_AS`, instancia **SDCOMEX** | Tradestats Management, AlertU, Imaging, RECON |
| ADBOG06D | 10.120.31.45 | AIX 7.2 (PowerVM) | Oracle Database, encoding `AL32UTF8`, instancia **QDCOMEX** | Banktrade (core) |

Cierra con **SAN** compartido entre ambos servidores de BD.

---

## 2. Ambiente de Pruebas (Esquema N°2, v1.2 — 21/nov/2022)

Mismo patrón, pero **con balanceador de carga** (VLAN "xx" en el diagrama, nombre de entrada
tipo `boc##.tes.app.bancodeoccidente.net`) y **5 servidores de aplicaciones** en vez de 3
(más redundancia que Desarrollo). ⚠️ *IPs leídas a menor zoom, confirmar contra el PDF si se
requiere exactitud total.*

### Servidores de aplicaciones (VLAN 63)

| Servidor (aprox.) | Rol funcional | Stack técnico |
|---|---|---|
| VWTSTABOG15-443 | Webprinting, AlertU, BT Imaging, UC HTML | Oracle WebLogic 14, IIS 10, Java 11 |
| VWTSTABOG15-444/445 | CT Absorber/Collector, TS Online/BIP .NET, Central Collector, RECON, BTS.W/S, IPSATP | IIS 10, .NET 4.8 |
| ATBOG030D | Banktrade v17 (core), BIS ClientTrade, BIS OPAS, BIS RECON, BIS Ventanilla | MQ Client 9.1, Oracle Client 19, Java 11 (AIX 7.2) |
| ATBOG031E | Banktrade v17 (core) — nodo adicional | MQ Client 9.1, Oracle Client 19, Java 11 (AIX 7.2) |

### Servidores de base de datos (VLAN 66)

| Servidor (aprox.) | Motor / Instancia | Soporta |
|---|---|---|
| VWTSTABOG15-442 | SQL Server 2019, instancia SDCOMEX | Tradestats Management, AlertU, Imaging, RECON |
| ATBOG032D / ATBOG033E | Oracle RAC 19c | Banktrade (core) |
| LTBOG109V (≈10.120.87.154) | Oracle Database 12c (Oracle Linux) | Componente adicional (no identificado con certeza en el diagrama) |
| "SAP BD" (caja aparte, rotulada "CORREO"/integración) | — | Integración con SAP — ⚠️ por confirmar el detalle exacto |

---

## 3. Ambiente de Producción (Esquema N°3, v1.1 — 21/nov/2022)

Mismo patrón que Pruebas, con **balanceador de carga** confirmado con alto zoom:
`bocxx.prd.app.bancodeoccidente.net` → `[10.120.16.xxx]` (el diagrama enmascara el último
octeto/el nombre de VLAN con "xx", es así literalmente en el PDF, no es un error de lectura).

### Servidores de aplicaciones (VLAN 79)

| Servidor | IP | SO / Plataforma | Rol funcional | Stack técnico |
|---|---|---|---|---|
| VWPSTABOG15-187 | 10.121.83.39 | Windows Server 2019 (VMware) | Webprinting, AlertU, BT Imaging, UC HTML | Oracle WebLogic 14 |
| VWPSTABOG15-188 | 10.121.83.44 | Windows Server 2019 (VMware) | Webprinting, AlertU, BT Imaging, UC HTML (par balanceado del anterior) | Oracle WebLogic 14 |
| VWPSTABOG15-189 | 10.121.83.37 | Windows Server 2019 (VMware) | CT Absorber/Collector, TS Online/BIP .NET, Central Collector, RECON, BTS.W/S, IPSATP | IIS 10 |
| VWPSTABOG15-190 | 10.121.83.38 | Windows Server 2019 (VMware) | Mismo rol (par balanceado del anterior) | IIS 10, .NET 4.8 |

### Servidores "core" (VLAN 51) — clúster activo de 2 nodos

| Servidor | IP | SO / Plataforma | Rol funcional | Stack técnico | Filesystem compartido |
|---|---|---|---|---|---|
| APBOG141A | 10.120.21.226 | AIX 7.2 (PowerVM) | Banktrade v17 (core), BIS ClientTrade, BIS OPAS, BIS RECON, BIS Ventanilla | MQ Client 9.1, Oracle Client 19, Java 11 | GPFS 5.5.5.199 (VLAN 13) |
| APBOG142B | 10.120.21.227 | AIX 7.2 (PowerVM) | Mismo rol — nodo par del clúster | MQ Client 9.1, Oracle Client 19, Java 11 | GPFS 5.5.5.200 (VLAN 51) |

Ambos nodos comparten un **FileSystem** vía GPFS — es decir, en Producción el núcleo de
BankTrade corre en un **clúster de 2 nodos AIX con filesystem compartido (GPFS)**, no en un
único servidor como en Desarrollo. También se etiquetan agentes `BK_TSM` (backup, Tivoli
Storage Manager) en cada nodo.

### Servidores de base de datos (VLAN 329 — "BD Banktrade")

| Servidor (VIP) | IP | Filesystem compartido |
|---|---|---|
| APBOG143A_vip | 10.121.107.135 | GPFS 5.5.5.201 (VLAN 53) |
| ATBOG33E_vip | 10.121.107.138 | GPFS 5.5.5.20x (VLAN 53) |

Esto confirma que la base de datos de Producción es un **clúster Oracle RAC de 2 nodos**
(nombres `_vip` = IP virtual típica de Oracle RAC/Grid Infrastructure), consistente con la
instancia `QDCOMEX` usada en los demás ambientes — no se alcanzó a leer el nombre exacto de
instancia en Producción con certeza total.

---

## 4. Conclusiones para `Perfil_Aplicacion_BankTrade.md`

Esta información permite **resolver** varias de las preguntas abiertas del perfil de
arquitectura:

1. **"CT" en los servicios de IIS**: la etiqueta literal y completa en el diagrama oficial es
   **"CT Absorber/Collector"**, agrupada junto a "TS Online/BIP .NET", "Central Collector",
   "RECON", "BTS.W/S" e "IPSATP", corriendo en IIS 10 + .NET 4.8 en un servidor Windows
   **distinto** del que aloja el front Java/WebLogic. El PDF no define qué significa "CT" como
   sigla — solo confirma el nombre del componente y dónde corre.
2. **Relación Java/WebLogic ↔ núcleo COBOL/AIX**: el diagrama confirma que son capas
   **separadas y paralelas**, no una reemplaza a la otra: (a) Front Java/WebLogic (Webprinting,
   AlertU, BT Imaging, UC HTML), (b) servicio .NET/IIS "collector" (CT Absorber/Collector,
   TS Online/BIP, Central Collector, RECON, BTS.W/S, IPSATP), y (c) el **núcleo real** del
   "Banktrade v17" (BIS ClientTrade/OPAS/RECON/Ventanilla) corre en **AIX** — el diagrama no
   detalla si ese núcleo AIX ejecuta COBOL directamente o es otra capa; solo se confirma que
   es la capa que trae MQ Client + Oracle Client + Java 11. **Sigue sin confirmarse en el PDF**
   si ese AIX es el mismo backend COBOL documentado en `Banktrade_Database_Diccionario_Tablas.md`
   o una capa Java adicional sobre AIX — ambas lecturas son compatibles con el diagrama.
3. **Diagrama oficial**: ya se incorporó (`Infraestructura Banktrade V17.pdf`), por lo que la
   pregunta 4 del perfil queda resuelta — este documento es la transcripción de esa fuente.
4. **Recon**: el diagrama no indica una tecnología distinta para Recon; aparece como parte de
   las funciones del servicio .NET/IIS "collector" (ver rol 2 arriba) en los 3 ambientes, y
   también como una de las funciones del servidor SQL Server (ítem "RECON" en
   Tradestats Management). Es decir, "Recon" **no es un servidor separado**, sino una
   funcionalidad presente en dos de los servidores — esto contradice ligeramente lo que se
   había documentado antes ("Recon corre procesos batch propios"); se recomienda tratar esa
   afirmación anterior como ⚠️ por confirmar/corregir.

## 5. Preguntas que siguen abiertas

- ¿Qué significa la sigla "CT"? (el PDF no lo define)
- ¿El servidor AIX del núcleo ("Banktrade v17 / BIS ClientTrade...") ejecuta directamente los
  programas COBOL documentados en `Banktrade_Database_Diccionario_Tablas.md`, o es una capa
  Java/MQ que a su vez llama al COBOL en otro sistema?
- ¿Qué es exactamente el nodo "LTBOG109V" (Oracle Linux, Oracle DB 12c) visto solo en
  Pruebas? ¿Y la caja "SAP BD"/integración con correo?
- Confirmar nombre exacto de la instancia Oracle RAC de Producción (VLAN 329).
