> Convertido automaticamente desde 'Banktrade Database.doc' (formato legado Word 97-2003) usando Word COM automation.
> Origen: originales/banktrade/Banktrade Database.doc
> Fecha de conversion: 2026-10-27
> Nota: documento tecnico en ingles (fuente del fabricante de BankTrade). Se preserva el idioma original.

# Banktrade Database - Diccionario de Tablas

## Overview

Banktrade application system database is a set of more than 300 tables without built-in primary-foreign keys constraints, but with strong relationship based on key fields.
The Banktrade database can be implemented on most industry database types including DB2, Oracle, Sybase, MS SQL server.
For detail information about tables, fields, programs, etc. use Banktrade Navigator (BTNavigator) tool. To design SQL queries, views, stored procedures use Banktrade Database Query Designer (BTQD) tool.

There are two basic Banktrade system configurations: single country and multi-country.
- **Single country:** all tables are located in the same physical database (library, catalog, or schema).
- **Multi-country:** the "Central" database keeps Security, Workflow, and GPS tables. All other databases ("Country 1", "Country 2" ... "Country N") keep all tables except Security and GPS groups.

## Grupos de Tablas

Cada grupo corresponde a un subsistema funcional de BankTrade. El nombre de tabla en negrita (en el documento original) indica la(s) tabla(s) principal(es) del grupo.

### 1. Letter of Credit tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LOLOC00 | L/C Issue | Group, Number, Sequence | LOLOC40, LOLOC62 -additional records |
| LOLOC01 | L/C Amendment | Group, Number, Sequence | LOLOC41– additional record |
| LOLOC02 | L/C Payment | Group, Number, Sequence | LOLOC43 – additional record. LOLOC02, LOLOC05, LOLOC06, LOLOC07 are part of the same “LC Payment” process |
| LOLOC03 | L/C Participation | Group, Number, Sequence |  |
| LOLOC04 | L/C Government Guarantee | Group, Number, Sequence |  |
| LOLOC06 | L/C Payee | Group, Number, Sequence | LOLOC02, LOLOC05, LOLOC06, LOLOC07 are part of the same “LC Payment” process |
| LOLOC07 | L/C Drawings | Group, Number, Sequence |  |
| LOLOC15 | L/C Pre-Payment | Group, Number, Sequence |  |
| LOLOC40 | L/C Issue Additional Record | Group, Number, Sequence |  |
| LOLOC41 | L/C Amendment Additional Record | Group, Number, Sequence |  |
| LOLOC43 | L/C Payment Additional Record | Group, Number, Sequence |  |
| LOLOC45 | L/C Multiple Contracts | Group, Number, Sequence, Payee |  |
| LOLOC46 | L/C Amendment Additional Parties | Group, Number, Sequence |  |
| LOLOC48 | L/C Payment Additional Agents and Documents | Group, Number, Sequence |  |
| LOLOC50 | L/C Issue Additional Parties | Group, Number, Sequence |  |
| LOLOC51 | L/C Amendment Additional Parties | Group, Number, Sequence |  |
| LOLOC54 | L/C Amendment/Adjustment/ Payment Additional Parties | Group, Number, Sequence |  |
| LOLOC57 | Amendment/Adjustment/ Payment Additional Parties | Group, Number, Sequence |  |
| LOLOC55 | L/C Cash Collateral Advance Payment | Group, Number, Sequence |  |
| LOLOC70 | L/C Issue Agent Commission | Group, Number, Sequence |  |
| LOLOC71 | L/C Amendment/Adjustment Agent Commission | Group, Number, Sequence |  |
| LACCR | Accrual Record | Location, Date Accrued To, RRN Number |  |
| LCANL00 | Cancellation Header | Location, Key-fill |  |
| LCANL01 | Cancellation Detail | Group, Number, Sequence |  |
| LCSRSA | Commission Adjustment | Group, Number, Sequence |  |
| LDFNC | Recovery of Charges from Non Bank Customers - Additional Charges | Group, Number, Sequence |  |
| LGDAR00 | Goods Arrival 00 | Group, Number, Sequence |  |
| LGDAR01 | Goods Arrival 01 | Group, Number, Sequence |  |
| LGDARXX | Index for LGDAR00, LGDAR01 |  |  |
| LINTR | Tier Commission by Product - General Information | Account NO, Application Type, Product Code, Event |  |
| LMMDB | Multiple Debit Margin for LC ISS/AMD/ADJ/PAY, COLL ISS/AMD | Group, Number, Sequence, Record Type |  |
| LOLOC62 | Issuance L/C Additional Record | Group, Number, Sequence |  |
| LOLOC76 | Interest Calculation for LC Payment | Group, Number, Sequence |  |
| LPRTR | Tier Pricing by Product | Type, Group, Number, Sequence |  |
| LSBAM | Standby Commission Info for Charges by Product Code and Relation | Type, Group, Number, Sequence |  |

### 2. Banker's Acceptance, Direct Finance (D/F) tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LOLOC05 | L/C Acceptance | Group, Number, Sequence | LOLOC02, LOLOC05, LOLOC06, LOLOC07 are part of the same “LC Payment” process |
| LOLOC60 | L/C Draft Acceptance | Group, Number, Sequence Draft Number |  |
| LINVS | New Investor | Location, Account Number, Branch Code, SPAD Number, SPAD Filler |  |
| LSPAD | Sale, Purchase, Anticipation, Discount | SPAD Number, SPAD Filler1, SPAD Filler2 |  |
| LSPCR | SPAD Cross Reference | Account Number, City Code, SPAD Number |  |

### 3. Collection tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LOLOC30 | Collection Issue | Prefix, Number, Sequence | LOLOC35 – additional record C30_AMEND_CNT - muestra el número de modificación/aceptación |
| LOLOC31 | Collection Drawer/Drawee | Prefix, Number, Sequence | Realacion draft y main XC1_MAN_DRF_CL_NMB |
| LOLOC32 | Collection Payment |  | LOLOC37 – additional record |
| LOLOC33 | Collection Payment Payees | Prefix, Number, Sequence |  |
| LOLOC34 | Collection Issue, Amendment Additional Record | Prefix, Number, Sequence |  |
| LOLOC35 | Collection Issue Additional Record /Cash Collateral | Prefix, Number, Sequence |  |
| LOLOC36 | Collection Additional Agents and Documents | Prefix, Number, Sequence |  |
| LOLOC37 | Collection Payment Additional Record /Cash Collateral | Prefix, Number, Sequence |  |
| LOLOC73 | L/C and Collection Payment CIF and Agent Commission | Prefix, Number, Sequence |  |
| LOLOC74 | L/C and Collection Payment Additional Payees for 3rd Parties | Prefix, Number, Sequence |  |
| LCASH | Cash Collection | Collection Number, Sequence |  |

### 4. Loan tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LLNIS04 | Loan Advance Issue Additional Record /Cash Collateral | Prefix, Number, Sequence, Location |  |
| LLNIS05 | Loan Advance Issue | Prefix, Number, Sequence, Location, Original Record | LLNIS04,LLNAD – additional record |
| LLNIS25 | Loan Advance Amendment | Prefix, Number, Sequence, Location, Amendment Sequence |  |
| LLNISXX | Loan Advance Index | Prefix, Number, Sequence, Location |  |
| LLNAD | Loan Advance Issue Additional Record | Prefix, Number, Sequence, Location |  |
| LLNBL15 | Loan Advance Accrual Entries | Prefix, Number, Sequence, Location, Accrual Sequence |  |
| LLNBL16 | Loan Advance Accrual/Billing Control Record by Location | Location, Word Control | Tiene fecha de ultimo accrual y maturity |
| LLNBL17 | Loan Advance Billing History | Prefix, Number, Sequence, Location, Billing Sequence |  |
| LLNCL | Loan Advance Cancellation | Prefix, Number, Sequence, Location |  |
| LLNCR | Loan Advance Cross Reference | Prefix, Number, Sequence, Location, Loan Number, Payment Number, Payment Sequence |  |
| LLNFX | Accrual Details for Loan Linked to FX Contract Payment | Prefix, Number, Sequence, Location |  |
| LLNPY | Loan Payment | Prefix, Number, Sequence, Location, Loan Number, Payment Number, Payment Sequence |  |

### 5. Reimbursement tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LOLOC20 | Reimbursement Issue | Group, Number, Sequence |  |
| LOLOC21 | Reimbursement Amendment | Group, Number, Sequence |  |
| LOLOC22 | Reimbursement Payment | Group, Number, Sequence |  |

### 6. Purchase Order tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LPOFL01 | Purchase Order Header | Prefix, Number, Sequence, PO Number, PO Item Number |  |
| LPOFL02 | Purchase Order Detail | Prefix, Number, Sequence, PO Number, PO Item Number |  |

### 7. Fund Transfer tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LFTRS00 | Fund Transfer 00 | Group, Number, Sequence, Location, FT Group, FT Group Number |  |
| LFTRS01 | Fund Transfer 01 | Group, Number, Sequence, Location, FT Group, FT Group Number |  |
| LFTRS02 | Fund Transfer 02 | Group, Number, Sequence, Location, FT Group, FT Group Number |  |
| LFTRSXX | Fund Transfer Index | Group, Number, Sequence, Location, FT Group, FT Group Number |  |
| LFTUP | Special Funds Transfer | FT Number |  |

### 8. Money Transfer tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LMTDF01 | Money Transfer 01 |  |  |
| LMTDF02 | Money Transfer 02 |  |  |
| LMTDFXX | Money Transfer Index |  |  |
| LMPTH | Money Transfer Message Path |  |  |
| LMTCF | Money Transfer Message Control |  |  |
| LMTMF | Money Transfer Message |  |  |

### 9. Declaration tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LDCIA00 | Declaration central |  |  |
| LDCIA01 | Format 1 header |  |  |
| LDCIA02 | Format 2 header |  |  |
| LDCIA03 | Format 3 header |  |  |
| LDCIA3A | Format 3A header |  |  |
| LDCIA04 | Format 4 header |  |  |
| LDCIA05 | Format 5 header |  |  |
| LDCDT11 | Format 1 detail 1 |  |  |
| LDCDT12 | Format 1 detail 2 |  |  |
| LDCDT02 | Format 2 detail 1 |  |  |
| LDCDT31 | Format 3 detail 1 |  |  |
| LDCDT32 | Format 3 detail 2 |  |  |
| LDCDT3A | Format 3A detail 1 |  |  |
| LDCDT05 | Format 5 detail 1 |  |  |
| LDCFN | Cross-reference |  |  |

### 10. Remittance tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LRM00 | Main transactions |  |  |
| LRM01 | Collection transactions |  |  |
| LRM00XX | Cross-reference |  |  |
| LRMCR |  |  |  |
| LRMRP |  |  |  |

### 11. Security tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LUSER | Security (User Sign on) | User |  |
| LPSWD00 | Password, User ID Record 00 | Operator ID, Control Record |  |
| LPSWD01 | Password, User ID, Menu Record 01 | Operator ID, Menu Name |  |
| LPSWD05 | Password, User ID Record 05 |  |  |
| LPSWDXX | Password, User ID Index |  |  |
| LAUP | Authorization |  |  |
| LAUTH | Authorization - LC, Collection, Loan | Authorization Key |  |
| LAUT2 | Authorization - Fund Transfer | Authorization Key |  |
| LAUT3 | Authorization - Tiered Authorization | Authorization Key |  |
| LAUT4 | Authorization - Tiered Authorization Fund Transfer | Authorization Key |  |
| LVLTN | Violation | Terminal, Date, Time |  |
| LAUDT | Audit Trial |  |  |
| LAUD1 | Audit Trial 1 |  |  |
| LAUD2 | Audit Trial 2 |  |  |
| LAUD3 | Audit Trial 3 |  |  |
| LAUD4 | Audit Trial 4 |  |  |
| LXCIF | License and CIF Related Cross Reference |  |  |

### 12. Configuration, Text and Logs tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LTABL | Rules | Location, ID, Number |  |
| LTXTV | Text |  |  |
| LLOGA | Logs | Group, Number, Type, Sequence, GL Voucher Number, GL Voucher Sequence | Historico de la transaccion. LGA_REC_TYPE es la tabla |
| LTICK | Ticklers | Tickler Date, Worker Number, Sequence |  |
| LVERS | Transaction Version | Group, Number, Sequence, Sequence 2, Version |  |
| LLOCK | Transaction Lock |  |  |
| LEMAL | Standard Format for Email or Fax Messages |  |  |
| LTXHT | Send Fax/Email History | Location, Account, Group, Number, Sequence |  |
| XTXTV | Data Area for LCTXTV | Location, Account, Group, Number, Sequence |  |

### 13. Rebate tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LRBDT | Rebate by Mnemonic | ID, City Code, Mnemonic, Open Advising Bank |  |
| LRBFL01 | Rebate Control 01 | ID, City Code, Mnemonic, Open Advising Bank |  |
| LRBFL02 | Rebate Control 02 | ID, City Code, Mnemonic, Open Advising Bank, Sequence, Date |  |
| LRBFL03 | Rebate Control 03 | ID, City Code, Mnemonic, Open Advising Bank, Sequence, Date |  |
| LRBFLXX | Rebate Index |  |  |
| LRBST | Rebate static Info | ID, City Code |  |

### 14. Account Master tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LACTM00 | Account Master Primary | Account Number, City Code |  |
| LACTM01 | Account Master Commission | Account Number, City Code |  |
| LACTM02 | Account Master Sub Account | Account Number, City Code |  |
| LACTM03 | Account Master Saving Account | Account Number, City Code |  |
| LACTM99 | Account Master Purge Replace | RID Number, RID City Code, RID Sequence |  |
| LABBR | Abbreviation | Abbreviation, Account Number, City Code |  |
| LACRT | Account Lock for Creation | Account Number, City Code |  |
| LACXR | Account Master Cross Reference |  |  |
| LADVC | Bank Reference Number |  |  |
| LBRAL | Bank Reference Alternate Number |  |  |
| LBREF | Bank Cross Reference Number | Customer DDA, Bank Reference Number |  |
| LACMB | Customer Monthly Bill | Account Number, Group, Number, Sequence |  |
| LCSTC | Account Master Audit Trial Report |  |  |

### 15. Facility tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LFCFL00 | Facility Information | Location, Account Number, Facility ID |  |
| LFCFL01 | Facility Transaction | Location, Account Number, Facility ID |  |
| LFCFLXX | Facility Index |  |  |
| LFC01 | Facility Reconciliation Temporarily 01 | Location, Account Number, Facility ID, System Code |  |
| LFC02 | Facility Reconciliation Temporarily 02 |  |  |
| LFCHT | Facility History | Account Number, Facility ID |  |
| LFCRL | Facility Information Cross Reference | Account Number, Facility ID |  |
| LACDF01 | Account Product Defaults for Margins and Modifier | Account Number, Product Code, Facility ID |  |
| LACDF02 | Account Product Defaults for Special Rates by Currency | Account Number, Product Code, Currency Code |  |
| LACDFXX | Account Product Defaults Index |  |  |
| LFCDL00 | Facility Information Used in Batch Processes 00 | Location, Account, Facility ID |  |
| LFCDL01 | Facility Information Used in Batch Processes 01 | Location, Account, Facility ID |  |
| LFCDLXX | Index Facility Information Used in Batch Processes |  |  |
| LFCLC | Account - Facility Cross Reference for Facility Audit Trail Report | Account, Facility ID |  |

### 16. FX (Foreign Exchange) Contract tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LOLOC90 | FX Contract Issue | Prefix, Number, Sequence |  |
| LOLOC91 | FX Contract Beneficiary/Agent Information | Prefix, Number, Sequence |  |
| LOLOC92 | FX Contract Payment | Prefix, Number, Sequence |  |
| LOLOC93 | FX Contract Attachments | Prefix, Number, Sequence |  |

### 17. Accounting tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LACTG01 | Accounting Entries | Group, Number, Sequence |  |
| LACTG02 | Accounting Commission Entries | Group, Number, Sequence |  |
| LACTG03 | Accounting Cash Collateral Entries | Group, Number, Sequence |  |
| LACTG04 | Accounting General Ledger Entries | Group, Number, Sequence |  |
| LACKU | Offering Acknowledgment |  |  |
| LACRV | Account Receivable | Group, Number, Sequence |  |
| LACXR | Account Cross Reference | Group, Number, Account |  |
| LAG2E | Extended Accounting 02 | Group, Number, Sequence, Type |  |
| LAUTF | Account Trail | Group, Number, Sequence, Date, Time |  |
| LCCSC | Insurance for L/C Expired |  |  |
| LCROS | Commission / Amortization | LOC-Code, SYS-Code, Group, Number, Sequence |  |
| LDFPY00 | Deferred Payment Summary |  |  |
| LDFPY01 | Deferred Payment Accounting |  |  |
| LDFPY02 | Deferred Payment Multiple Contract |  |  |
| LDFPY03 | Deferred Payment Additional Charges | Tran. Number, Record Type, Appl. Type, Record Seq, Tran. Type, Tran. Seq. |  |
| LDFPY04 | Deferred Payment Commission |  | Ch52 cl52 cc52 |
| LEARN | Earnings | Account, Product Code, Income, Year |  |
| LEXGL | General Ledger Extract |  |  |
| LEXRN | External Reference Number |  |  |
| LGLFV | Cross Reference for Online Processing |  |  |
| LGLG2 | General Ledger Additional Record |  |  |
| LGLGA | General Ledger and LACTG04 Data Set Definitions |  |  |
| LGLGI | General Ledger for Internal Use |  |  |
| LGLGX | General Ledger | Voucher Number, Voucher Sequence |  |
| LGLXL | Transaction With General Ledger Information |  |  |
| LPROF | Profitability |  |  |
| LSUBL | Sub Ledger |  |  |
| LSUBR | Sub Ledger Deleted |  |  |
| LTRFL | Tier Price Commission |  |  |

### 18. SWIFT tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LBICF | SWIFT ID Validation |  |  |
| LEXSW | Extra Partition KSDS for SWIFT | Extra sequence |  |
| LINS3 | SWIFT Incoming |  |  |
| LISRT | Rerouting Incoming SWIFT |  |  |
| LISXR | SWIFT Letters Template Generator |  |  |
| LOLOC56 | Telex/SWIFT Claim | Group, Number, Sequence |  |
| LSWIF | SWIFT Outgoing |  |  |
| LSWIN | SWIFT Outgoing Released |  |  |
| LSWTE | Reconciliation SWIFT and Telex |  |  |
| LTLXC | Telex - SWIFT Claim Cross Reference |  |  |
| LTLXI | Telex - SWIFT Claim Interface |  |  |
| LWBIC | SWIFT Correspondent ID | Bank, Country, Location, Branch |  |
| L02D2 | Processed Country |  |  |

### 19. Fedwire tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LFDIN | Fedwire Incoming |  |  |
| LFDIN00 | Fedwire Incoming Control 01 |  |  |
| LFDIN01 | Fedwire Incoming Control 02 |  |  |
| LFDINXX | Fedwire Incoming Index |  |  |
| LFINT | Fedwire Outgoing Interface |  |  |
| LFOUT | Fedwire Outgoing |  |  |

### 20. Workflow tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LQEVT | Workflow Events History File |  |  |
| LQGRP | Workflow Queue Group assignment |  |  |
| LQHR2 | Workflow Queue History |  |  |
| LQHRL | Workflow Queue History after Release |  |  |
| LQHS2 | Workflow Queue History before Release |  |  |
| LQHST | Workflow Queue History pre Release |  |  |
| LQINQ | Workflow Queue Cross Reference |  |  |
| LQLRL | Workflow Queue List Deleted records |  |  |
| LQLST | Workflow Queue List |  |  |
| LQPTY | Workflow Queue Payment |  |  |
| LQTIM | Workflow Queue Time |  |  |
| LQXRA | Workflow Queue Cross Reference by Amount |  |  |
| LQXRF | Workflow Queue Cross Reference by Record Type |  |  |
| LQXRL | Workflow Queue Cross Reference |  |  |

### 21. GPS (Global Processing System) tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LFOTC | GPS Conditional PT | FOT Code, Next Condition Sequence |  |
| LFOTE | GPS PT Exists | FOT Code |  |
| LFOTH | GPS PT History | Country, Location, Number, Type, Sequence, Sequence 2, Version, Version 2 |  |
| LFOTU | GPS Current Processing Tasks (PT's) |  |  |
| LGPCP | GPS Prefer Customer Priority Assignment |  |  |
| LGTID | GPS Team Definition |  |  |
| LGTMS | GPS Team Setting |  |  |
| LGTMW | GPS Team - Worker Assignment |  |  |
| LGTPT | GPS Team Scope |  |  |
| LGTRT | GPS Transaction Type |  |  |
| LGTTP | GPS Transaction Type Priority |  |  |
| LWCRT | GPS Worker Profile - Criteria Assignment |  |  |
| LWFOT | GPS Worker Profile - PT Assignment |  |  |

### 22. Customer Bridge tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LBLPD | Customer Bridge Communication |  |  |
| LCBTA | Customer Bridge Communication |  |  |
| LOBRT | Customer Bridge Print Report |  |  |
| LPCDT | Customer Bridge Interface |  |  |
| LSMRT | Customer Bridge Report |  |  |
| LPCDL | Customer LBREC Data |  |  |

### 23. TradeStats tables (Banktrade Standard Report Populated)

| Name | Report Name | Comment |
| --- | --- | --- |
| L1462 | Department Worker Status |  |
| L1463 | Department Worker Summary |  |
| L1464 | Daily Log of New Transactions |  |
| L146A | Transaction Status |  |
| L146B | Transaction Status |  |
| L181A | Customer Statement L/C Report of Acceptance. |  |
| L181L | Customer Statement LC Report |  |
| L2331 | Direct Finance Activity Report with Date Selected |  |
| L2332 | Roll-over Activity |  |
| L2334 | Past-due Activity |  |
| L2335 | Deferred Activity |  |
| L2337 | Federal Reserve |  |
| L2338 | Specific Activity |  |
| L5481 | Outstanding Discounted and Held |  |
| L5482 | Outstanding Non-discounted Acceptances |  |
| L5483 | Outstanding Pending Acceptances |  |
| L5484 | Outstanding Acceptance Reconcilement |  |
| L5485 | Outstanding Sold Acceptances |  |
| L5631 | Monthly Banker’s Acceptance Survey Report by mm/yy (acceptance) |  |
| L5632 | Monthly Banker’s Acceptance Survey report by mm/yy (SPAD) |  |
| L5861 | Banker’s Acceptance Monthly Statistics for mm/yy (created) |  |
| L5862 | Banker’s Acceptance Monthly Statistics for mm/yy (in processing) |  |
| L881A | Flat File Data Elements for Acceptance |  |
| L881L | Flat File Data Elements for LC Number |  |
| LB542 | Maturing Acceptance Report |  |
| LB566 | Loan Officer Acceptance Report |  |
| LB589 | Banker’s Acceptance Monthly Commission Report for mm/yy |  |
| LD081 | Trace Report |  |
| LD086 | Customer Statements |  |
| LD146 | Items Pending/Hold, Department Worker Summary |  |
| LD172 | Turnaround Report |  |
| LD175 | Released Payment Report |  |
| LD178 | Paying Efficiency Report |  |
| LD181 | Reciprocity Report |  |
| LD184 | Held Payments Report |  |
| LD187 | Volume Statistics Report |  |
| LD189 | Profitability Report |  |
| LD194 | Monthly Collection Statistics Report |  |
| LD197 | Safekeeping Summary Report |  |
| LD521 | Collection Cancellation Report |  |
| LD888 | G/L Customer Accounting Report |  |
| LD889 | G/L Interface Summary Report |  |
| LD900 | Print Collection Due Report |  |
| LGREC | End Of Day Report: GL History |  |
| LL080 | Audit Trail for Account Master |  |
| LL081 | Audit Trail for Rules |  |
| LL082 | Audit Trail for Passwords |  |
| LL083 | Audit Trail for Authorization |  |
| LL132 | Liability Report by Customer |  |
| LL133 | Liability Report by Country |  |
| LL134 | Liability Report by Currencies |  |
| LL141 | Outstanding Security Funds and Cash Collateral Report |  |
| LL142 | Earnings Profitability Report |  |
| LL144 | Reciprocity Report |  |
| LL161 | Risk Report by Movement |  |
| LL232 | Matured Acceptance Report |  |
| LL233 | Acceptance Activity |  |
| LL339 | Account Transfer (extracting customers by cost center) |  |
| LL344 | Account Master Audit List for Location |  |
| LL352 | Full Report by Name and Address |  |
| LL352 | Customer Report for Selected Accounts |  |
| LL359 | Account Number Changed, Deleted or Rejected |  |
| LL382 | Unreleased GL Posting |  |
| LL385 | Released Automated |  |
| LL387 | Released Automated and Manual |  |
| LL388 | Customer Accounting Interface |  |
| LL389 | Daily General Ledger Interface |  |
| LL395 | Summary of Accounting Entries |  |
| LL512 | Account Transfer |  |
| LL909 | MIS Volume/Amount Statistics Report |  |
| LL911 | MIS Volume/Amount Statistics Follow up Report |  |
| LU09C | Reciprocity Outgoing Collections |  |
| LU09L | Reciprocity Export Letter of Credit |  |
| LU10C | Reciprocity Incoming Collections |  |
| LU10L | Reciprocity Import Letter of Credit |  |

### 24. Declarations (PLANILLA) tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LCFPX10 | Final PLANILLA Register 10 |  |  |
| LCFPX20 | Final PLANILLA Register 20 |  |  |
| LCFPX30 | Final PLANILLA Register 30 |  |  |
| LCFPX40 | Final PLANILLA Register 40 |  |  |
| LCFPX60 | Final PLANILLA Register 60 |  |  |
| LCFPX70 | Final PLANILLA Register 70 |  |  |
| LCFPX80 | Final PLANILLA Register 80 |  |  |
| LCFPXXX | Import/Export Index |  |  |
| LDCCR | Declaration Cross Reference |  |  |
| LDCLF | Import/Export Declaration |  |  |
| LDISC | Discrepancy |  |  |
| LEXFP | Final PLANILLA Extract |  |  |
| LFPLN | Final PLANILLA |  |  |
| LFPRF | Virtual PLANILLA Reference |  |  |
| LVPLN | Virtual PLANILLA |  |  |

### 25. Foreign Exchange tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LBCIN | LBTCIN-Record |  |  |
| LBTE4 | Transaction Extended |  |  |
| LBTE7 | Transaction Avalistas Information |  |  |
| LCKIN | Interface Check Print Data |  |  |
| LCMCS | CMCS Data |  |  |
| LCOMT00 | Internally Used for Commission Release 00 |  |  |
| LCOMT01 | Internally Used for Commission Release 01 |  |  |
| LCOMTXX | Commission/Text Index |  |  |
| LFX00 | Foreign Exchange Deals 00 |  |  |
| LFX01 | Foreign Exchange Deals 01 Cross Reference |  |  |
| LFX02 | Foreign Exchange Deals 02 Cross Reference |  |  |

### 26. Other tables

| Name | Description | Unique Key Fields | Comment |
| --- | --- | --- | --- |
| LBCAN | Book-off/Cancellation Report |  |  |
| LBLRF | Bill of Landing - SLG/Payment Reference |  |  |
| LFXDL | Multiple Debit Accounts in Payment Transactions and Loan Issue |  |  |
| LFXMD | Multiple Debit Accounts per Payee |  |  |
| LFXRF | FX out Dealing Reference Defined in Central Database Only |  |  |
| LTRCR | Cross Reference for Online Process Multiple Transaction |  |  |
| LDEC1 | Relationship Between Worker Number and Operating Group |  |  |
| LDEC2 | Inferior Groups and Related Workers |  |  |
| LFHST | Fax History |  |  |
| LMQA1 | MQ-Series Acknowledgement |  |  |
| LCURX | Reevaluation Currency |  |  |
| LRVFL | Revolving Credit |  |  |

### 27. Tables and Common Links

| Table Name | Description | Link Fields | Table and Linkage Comments |
| --- | --- | --- | --- |
| LLOGA | Transaction Log | LGA_PREFIX LGA_NUMB LGA_REC_TYPE LGA_SEQ | LLOGA table stores information about transaction changes history. Transaction is defined by PREFIX, NUMBER and SEQUENCE. Transaction RECORD TYPE defines table where the transaction is stored. For example, value 00 points on table LOLOC00. |
| LTABL | Rules | TBF_LOCATION TBF_NUM TBF_ID | To retrieve the description of Rules values, you can link the value to the appropriate LOCATION, NUMBER, and ID in LTABL. For example, to get the description of the current Obligation Code from a LC record, you should link to TBF_NUM with a value of “214” plus TBF_ID and TBF_LOC in LTABL with the values from the fields C00_OBLG_CLSS_CURR and C00_WRKR_LOCATION from LOLOC00. LOCATION is optional in the sharable location configuration. Once linked, you can then retrieve any value from that Rule (descriptions, counters, indicators). |
| LACTM00 | Account Master | AM0_ACCOUNT_NUM | To obtain party information such as name, address, officer code, cost center, etc, you must use the fields defined as “Account Number” for the appropriate party. For example, to get Customer information from a LC record, using C00_CUST_DDA_ACCT you should link to AM0_ACCOUNT_NUM in table LACTM00. In the case where a City Code is used, add the field C00_CUST_CITY_CODE to C00_CUST-DDA-ACCT and link to AM2_ACCOUNT_NUM plus AM2_CITY_CODE in LACTM02 to retrieve the unique information for that subsidiary/branch table. |
| LOLOC00 | LC Issue | C00_GROUP C00_NUMBER C00_TYPE_SEQ | C00_TYPE_SEQ is always “000” |
| LOLOC40 | LC Issue Additional Parties | C40_GROUP C40_NUMBER C40_TYPE_SEQ | C40_TYPE_SEQ is always “000” |
| LOLOC01 | LC Amendment | C01_GROUP C01_NUMBER C01_TYPE_SEQ | Amendment and Adjustment transaction sequence are separate and started from “001”. Indicator C01_AMEND_ADJ_IND values: ‘N’ – Amendment (XL1_RECORD_TYPE=’01’); ‘J’ - Adjustment (XL1_RECORD_TYPE=’11’). For Log mode only values (replaced by ‘N’ or ‘J’ on update): ’E’ – export LC Amendment; ’B’- Guarantee Amendment; ’S’-export LC Adjustment; ’T’ – Guarantee Adjustment |
| LOLOC41 | LC Amendment Additional Parties | C41_GROUP C41_NUMBER C41_TYPE_SEQ |  |
| LOLOC02 | LC Payment | C02_GROUP C02_NUMBER C02_TYPE_SEQ | Payment transaction sequence started from “001” |
| LOLOC05 | LC Acceptance | C05_GROUP C05_NUMBER C05_TYPE_SEQ | This table is mostly used for Acceptance and Discount information. Since this record is used for both Acceptances under LC and Direct Finance, release and Facility information is kept here. |
| LOLOC06 | LC Payee | C06_GROUP C06_NUMBER C06_TYPE_SEQ | C06_RECORD_SEQUNC is used to define up to the 10 payees allowed in Payment processing. Therefore payee 1 is defined as “000001”, payee 2 as “000002” and so on. Payee information such as name and address, disbursement, currency and amount and reference details are kept in this table. |
| LOLOC07 | LC Drawing | C07_GROUP C07_NUMBER C07_TYPE_SEQ | Drawing information such as draft amounts, negotiating bank charges and debit information is kept in this table. |
| LOLOC43 | LC Payment Additional Information | C43_GROUP C43_NUMBER C43_TYPE_SEQ | Additional information includes Exchange rates for each of the payees, account numbers and cash collateral info. |
| LOLOC30 | Collection Issue | C30_GROUP C30_NUMBER C30_TYPE_SEQ |  |
| LOLOC31 | Collection Drawer/ Drawee | C31_GROUP C31_NUMBER C31_TYPE_SEQ |  |
| LOLOC32 | Collection Payment | C32_GROUP C32_NUMBER C32_TYPE_SEQ |  |

### 28. Business Rules and Glossary (Useful Topics)

| ## | Topic Description |
| --- | --- |
| 1 | Transaction is considered as Released if [TI]_RELEASE_CODE_2>299 |
| 2 | Transaction is considered as On Hold or Partially Released if [TI]_RELEASE_CODE_1>0 OR [TI]_RELEASE_CODE_2>0 |
| 3 | Link between transaction tables includes mandatory transaction Group/Prefix (1 char) [TI]_LC_GROUP, transaction Number (6 chars) [TI]_LC_Number, and optional transaction Sequence (3 chars or number) [T1]_TYPE_SEQ |
| 4 | Link to “Rules” table (LTABLE) includes Number TBF_NUM, Location (empty if shared rule) TBF_LOCATION, and ID TBF_ID fields |
| 5 | Link to “Account Master” table (LACTM00) includes Account ID AM0_ACCOUNT_NUM field |
| 6 | Typical link between transaction tables works as INNER JOIN |
| 7 | Typical link between transaction table and Rule or Account Master table works as LEFT JOIN |
| 8 | “Base”, “MYR”, “MRT” amount is amount in bank native country currency |
| 9 | Loan transaction table (LLNIS05) stores original transaction with empty LNI_ORIG_RECORD field. Duplicated record stores “000” in this field. Filter condition is LNI_ORIG_RECORD<>’000’ |
| 10 | Accounting Entries table LACTG04 field AG4_REC_TYPE_SEQ is entry number per transaction |
| 11 | LC Amendment sequence is previous sequence (issue or amendment) + 1. Latest Collection Amendment sequence is always 0. Previous Amendment sequence = Amendment counter + 1. Collection Issue sequence is 0, if no Amendments, and 1 if at least one amendment exists, but Amendment counter C30_AMEND_CNT is always 0. The changes in the sequence are synchronized with LLOGA table, but not synchronized with shadow XLOGA |
| 12 | Obligation code (liability) definitions (rule “214”) contain mnemonics codes (GL numbers) in Counter fields :TCT1 – debit mnemonics for LC, TCT5 – credit for LC, TCT6 – debit for Loan, TCT11 – debit Loan interest, etc. |
| 13 | Regular (screen LI42) LC Cash Collateral fields are located in LOLOC00, but if rule=”998GLCASH” TIN5=”Y” (for NCB) then in LOLOC55. Cash Collateral accounting history fields are located in LACTG03, but for loan in LLNIS04 |
| 14 | Commissions exist for LC and Collections (Issues, Amendments, Payments). For LC Issue commissions (proportional and flat, screen LI42, LOLOC00) defined per customer account, but can be waived (indicator). Rule 214 TCT2 and TCT3 define GL mnemonics for 2 types of commissions. Collection commissions (screen DI10, LOLOC30) amount is manual input. The GL mnemonics is also manual input, but default value from rule=703, TDS2. Notice, rule 214 is typically sharable, but rule 703 not. Actual commissions (history) are accounting entries in LACTG02 |
| 15 | Accrual (accumulated earning) data is accumulated in LACCR table on daily basis as result of Accrual process. The data are represent calculated earning from commissions (or similar) per day on transaction. The data (amounts) are moved to GL table (LGLGX) on daily basis |
| 16 | General Ledger table (LGLGX) is populated by data on daily basis as result of online and batch transactions with corresponding mnemonics. In the end of day the records are moved to LG entries history table (LACTG04). The LACTG04 keeps track about all GL entries and related transaction, but product type recognition (AG4_GL_TYPE_CODE) is ambiguous |
| 17 | “End of Day” batch procedure on daily basis appends data into some report tables (LGREC, LL387, LL388, etc.). The report tables accumulate accounting data broken by mnemonics, not by customers |
| 18 | LC cancellation process includes 3 steps: (1) Define candidates by date range (using C00_EXPR_LATE) or by transaction number. The defined candidates are stored in LCANL01 table and have C00_CANCL_PEND_IND=’Y’, C00_DEL_CANDTE_IND=’N’. (2) Release the candidate. C00_CANCL_PEND_IND=’N’, C00_DEL_CANDTE_IND=’Y’, C00_CONF_CURR_BAL=0 C00_UNCNF_CURR_BAL=0, pass corresponding GL entries. (3) Purge cancelled transactions. After this step the cancelled transaction are removed from LOLOC00 |
| 19 | Collection is simplified LC product. The collection issue is created if involved parties trust each other. In this case Bank role is not guarantee of the finance obligation, but only collect of payments. Commission is much lower than in LC product. Incoming collection means payment is collected by bank: payer=customer, presenter=beneficiary XC0_COLL_TYPE = 'I' (?). Outgoing collection means payment is provided by bank: payer=beneficiary, presenter=customer. For Europe customers the collection is likely than LC. Collection type recognition (when XC0_COLL_TYPE is empty) can be based on rule 704 (collection prefix=group) TIN8 (values “I”, “O”, “D”,” “) or (if TIN8=” “) rule 703 (collection suffix) TIN3 (values “I”, “O”, “D”, “R”, “Y”) |
| 20 | Tables LOLOC02, LOLOC05, LOLOC06, LOLOC07, LOLOC43 are part of the same Banktrade process: LC Payment. Each LC payment creates at least 1 record in all these tables, but stored data in the tables are different: LOLOC02 stores commissions, charges, etc.; LOLOC05 stores whole payment amount (and acceptance transaction data); LOLOC06 stores payee data (one record per payee) per payment transaction; LOLOC07 stores drawing and transfer amounts: LOLOC43 stores discrepancy indicator, etc. |
| 21 | Discrepancy indicator (C43_DISCREPANT_PMT) turns ON by the following actions: (1) in Payment Log get new sequence; (2) create discrepancy note via Discrepancy Screen; (3) Payment Update. After these steps the LOLOC43.C43_DISCREPANT_PMT get value ’Y’. Note rules settings allow to get all these steps in one step: Payment Create |
| 22 | All SWIFT messages are stored in LTXTV table as text in field XTX_LINE_ARRAY. Incoming SWIFT messages have TX0_APPL_ID=”I”. Message type (like MT700) is located in field TX0_ST_SWIFT_NAME. However, this field is populated only for outgoing messages. For incoming messages there is no indicator of SWIFT message type except message content in the field XTX_LINE_ARRAY |
| 23 | Pending Release indicator is [TI]_RELEASE_CODE_2<300 |
| 24 | Additional charges for LC Issue, Amendment, Payment: LDFPY03.DP3_CHRG_AMT_1, DP3_CHRG_AMT_2, DP3_CHRG_AMT_3, DP3_CHRG_AMT_4. Each transaction may have unlimited number of additional charges. The additional charges are grouped by 4 per row. Each row has it sequence number per transaction. Each additional charge has own sequence (matched with transaction sequence) DP3_CHG_TK_TRNS_x, mnemonics DP3_CHRG_MNEM_CD_x (linked to rule 300), etc. When a charge is created, transaction sequence is saved into DP3_CRT_SEQ_NO_x. When a charge is taken, transaction sequence is saved into DP3_CHG_TK_TRNT_x. |
| 25 | Regular LC stages are (1) Create Import LC Usance (payment delayed=acceptance) or Sight (payment followed according to payment terms), (2) Release LC, (3) Create Payment, (4) when maturity go to Maturity Maintenance and process acceptance for that LC. LC Maturity Maintenance process indicator C05_MTR_ACPT_REL_I=’Y’. It corresponds to amount C05_ACCEPTANCE_AMT, LLOGA.LGA_REC_TYPE = '07' and acceptance release date LLOGA.LGA_AUTH_REL_DATE2 |
| 26 | Payment terms are selected based on Tenor Sight (presented in C00_TENORCODE_ORIG/LATE). If Tenor Sight=Y, it means Customer must pay directly after LC release (C00_TENORCODE_ORIG / LATE=S). If Tenor Sight<>Y (C00_TENORCODE_ORIG/LATE<>S) the payment terms are defined in C00_TENOR_TEXT, C00_TENORDAYS_LATE, C00_TENORDATE_LATE |
| 27 | When LC issue/payment/amendment for import/export transaction is cancelled it is appeared in LCANL01. Note CN1_TYPE_REC=’A’ if cancellation is active |
| 28 | For Export LC Issue (Advise) transaction is saved in LOLOC00 (XL0_RECORD_TYPE = 00) and LOLOC40 (XL40_RECORD_TYPE = 40), Amendment – LOLOC01 (XL1_RECORD_TYPE = 01, C01_AMEND_ADJ_IND=’N’) and LOLOC41 (XL41_RECORD_TYPE = 40), Adjustment - LOLOC01 (XL1_RECORD_TYPE = 11, C01_AMEND_ADJ_IND=’J’) and LOLOC41 (XL41_RECORD_TYPE = 42). Release date for Issue (Advise) is LOLOC00. C00_ISSUE_DATE, for Amendment/adjustment - LOLOC01.C01_AMDADJ_REL_DAT. Payment (if it is Export Usance[delayed Payment]=Acceptance) LOLOC05.C05_AN_RELEASE_DT with LOLOC05.C05_CREATE_ACCEPT=’Y’. Payment (if it Export Sight [regular payment]) is saved in LOLOC02, 05, 06, 07, 43. LOLOC05.C05_AN_RELEASE_DT with LOLOC05.C05_CREATE_ACCEPT<>’Y’ |
| 29 | Collection Issue is stored in LOLOC30. Collection may be Usance (delayed, C30_ACCEPT_REQ_ IND=’Y’) or Sight but Collection payment (LOLOC32) cannot be Usance, only Sight |
| 30 | Table LACTM01 is not used in latest Banktrade versions. It was replaced by LTRFL where commissions terms are differed by account or transaction (LTR_COMMS_TYPE), transaction type (LTR_REC_TYPE). In case of transaction fields XLC_TR_TRANS_NUMBR and XLC_TR_TRANS_SEQ must be matched to the transaction attributes. Account to match is customer/applicant for import LC and beneficiary for export LC |
| 31 | Total Fees Collected for LC from its issuance to the time the report is run - LACTG02 |
| 32 | Fees (commissions) frequency (for standby ) value (M-monthly, Q-quarterly, S-semi-annually, A-annually, E-on expire, F-fixed ) is stored in LOLOC00.C00_COMM_PERD_TYPE |
| 33 | LC Issue can have Participants – other Banks to share finance of the LC. If Participants involved (C00_PARTICIP_IND=Y), then correspondent records (child) are created in LOLOC03 to describe Participants (account, amount, percent) and in LOLOC00 new LC Issues (C00_LC_TYPE=P) to share the parent LC open amount (C00_TRANS_FR_LC_NO). Current balance of all participated items is stored in LOLOC40.C40_PARTC_CURR_BAL of parent LC and for each participated item in LOLOC40.C40_PARTC_CURR_BAL of child LC (C00_LC_TYPE=P) |
| 34 | Report to show our participated letters of credit, the participant and the percentage participated: there is a record in table LOLOC03 for each participant |
| 35 | Voucher keeps general ledger entries per transaction. Advice is text document to bank/client to notify that transaction is done. Tracer is notification about mistake found in account reconciliation |
| 36 | Fields C00__1ST_AUTHORIZER, C00__2ND_AUTHORIZER store unique authorization code of worker that made transaction release. Link to AUT_AUTH_KEY field (via CAST in T-SQL) allows get worker name (AUT_AUTH_NAME) and ID (AUT_DEPT_WORK_CODE) without rule 106 |
| 37 | Amendment covers changes of basic (external) attributes of LC Issue: open amounts, expiry date, etc. Adjustment covers changes of internal attributes of LC: charges, commissions, debit/credit accounts, etc. Amendment changes are transferred to original LC record as modification of balance, late expiry date, etc. |
| 38 | Additional Party1and 2 for LC issue (screen AIX1) data is located in LTXTV table with XTX_LC_NUMBER='Tran#' AND TX0_DOC_TYPE='K' AND TX0_SOURCE_IND='EI' on XTX_LINE_ARRAY lines (each line occupy 65 chars) as first 35 chars: original “name/address party1” line1-6, original “free text party1” line 7-12, current “name/address party1” line 13-18, current “free text party1” lines 19-24 , reserved line 25, original “name/address party2” line26-31, original “free text party2” line 32-37, current “name/address party2” line 38-43, current “free text party2” lines 44-49 , reserved line 50 |
| 39 | For LC Payment (screen AI7D) presents located in LTXTV table with XTX_LC_NUMBER='Tran#' AND TX0_DOC_TYPE='K' AND TX0_SOURCE_IND=PY' (as sample) Confirming Bank (original lines 33-36, current lines 37-40), Paying Bank (original lines 8-11, current lines 12-15), Accepting Bank (original lines 16-19, current lines 20-23), etc. Drawing Bank data is located in LOLOC55 (XL55_DRFTS_ON_TXT1, XL55_DRFTS_ON_TXT2, XL55_DRFTS_ON_TXT3, XL55_DRFTS_ON_TXT4) |
| 40 | For LC Issue exchange rate should be retrieved from C40_BOOK_EXCH_RATE and interpreted based on C40_BOOK_EXRT_IND (“D” means “divide”) |
| 41 | For LC Amendment exchange rate should be retrieved from C41_BOOK_EXCH_RATE and interpreted based on C41_BOOK_EXRT_IND (“D” means “divide”) |
| 42 | For LC Payment/Drawing exchange rate should be retrieved from C43_DRAW_EXCH_RATE and interpreted based on C43_DRAW_EXCH_RT_I (“D” means “divide”) |
| 43 | For Loan Issue exchange rate should be retrieved from LNI_EXCHGE_RT_DISP. It is “multiply” if LNI_EXCHGE_RT_DISP= LNI_EXCHANGE_RATE. Otherwise it is “divide” |
| 44 | For Loan Payment exchange rate should be retrieved from LNP_EXCH_RATE_DISP. It is “multiply” if LNP_EXCH_RATE_DISP = LNP_EXCHANGE_RATE. Otherwise it is “divide” |
| 45 | LTICK table include one “header” record per date (XTKLR_YYMMDD_DATE, format yymmdd) and multiple “detail” records linked to transactions. “Header” record always has TIK_SEQ_NO_COUNT=0 and no transaction attributes. “Detail” records have TIK_SEQ_NO_COUNT>0 and transaction attributes (TIK_PREFIX, TIK_LC_NUMBER, etc.) |
| 46 | LC type is defined by C00_LC_TYPE”: I' - import LC; 'E' - export LC; 'P' - participant; 'B' - bonds/guaranties; 'O' - pass-on-guaranties; 'L' - shipping guaranties, related to LC; 'C' - shipping guaranties, related to collections; 'A' - shipping guaranties, stand-alone. All C00_LC_TYPE<>'E' are import. |
| 47 | LC Commissions total are stored when condition C00_WAIVE_COMM_IND<>'Y' in C00_TOT_CM_OVR_AMT, C00_ADV_COMM_OVERR |
| 48 | Outstanding LC condition is C00_CONF_CURR_BAL + C00_UNCNF_CURR_BAL > 0 |
| 49 | For Import LC C00_UNCNF_OPEN_AMT = 0, customer is customer, beneficiary is beneficiary. For Export LC C00_UNCNF_OPEN_AMT may be > 0, customer is issuing bank, beneficiary is fake beneficiary. |
| 50 | LC cash collateral balance is C00_CASH_COLL_BAL > 0. However if rule 998GLCASH TIN5=Y, then C55_AD_CASH_COLBAL>0 |
| 51 | Stand-by LC (LC created for future use, but customer pays regular commissions) indicator is C00_STAND_BY_IND=’Y’ |
| 52 | L/C Renewal Event indicator C00_EXPR_LATE<> C00_EXPR_DATE_ORIG and record in LTXTV with TX0_SOURCE_IND='CO’ and pattern 'AUTO EXTENSION EFFECTED ON’ in XTX_LINE_ARRAY |
| 53 | L/C Stan-by periodic fee Event indicator LACTG02. AG2_CMSN_TYPE_CODE='SB' and AG2_CMSN_STATUS_CD='T' |
| 54 | L/C Draw Event indicator LLOGA.LGA_REC_TYPE='03' |
| 55 | L/C Increase Event indicator LOLOC01.C01_CONF_ACTION_CD='I' and LLOGA.LGA_REC_TYPE = '02' |
| 56 | L/C Decrease Event indicator LOLOC01.C01_CONF_ACTION_CD='D' and LLOGA.LGA_REC_TYPE = '02' |
| 57 | Collection: Commissions C30_COMM_AMT>0 and C30_AMEND_CNT=0 |
| 58 | Loan type LNI_LOAN_TYPE: ‘B’ - Bill Receivable; ‘E’ - Export Negotiation; ‘G’ - Shipping Guarantees; ‘P’ - Packing Credit; ‘S’ - Straight Loan; ‘T’ - Trust Receipt; ‘I’ - Passive Loan |
| 59 | Loan product code field LNI_PRODUCT_CODE. Loan parent product field LNI_SYSTEM_IND: 'L' – LC, 'C' - Collection |
| 60 | Outstanding Loans criteria LNI_PRINCPL_OUTSTD > 0 |
| 61 | Acceptance indicator C05_CREATE_ACCEPT='Y and amount is C05_ACCEPTANCE_AMT |
| 62 | Acceptance type C05_LC_TYPE: 'E' – export: ‘I’ - import |
| 63 | Outstanding Acceptance C05_ACCEPTANCE_AM>0 |
| 64 | Banker’s Acceptance indicator C05_DISC_ACCEPT='Y' |
| 65 | Top level Facility FC0_FACILITY_ID =TBF_ID TBF_NUM='215' AND TBF_COUNTER_10 = 0 |
| 66 | Facility parent field FC0_RELATED_FR_FAC |
| 67 | Link between Loan (LLNIS05) and Accounting History (LACTG04) tables depends on loan type. For LC Payment loan TRIM(LNI_TRN_NUMBER) IS NOT NULL and AG4_LC_PREFIX // LPAD(AG4_LC_NUMBER,6,'0') = LNI_TRN_NUMBER and AG4_LC_SEQUENCE = LNI_TRN_SEQ_NO. For stand alone loan TRIM(LNI_TRN_NUMBER) IS NULL and AG4_LC_PREFIX=LNI_GROUP_PREFIX AND AG4_LC_NUMBER =LNI_GROUP_NUMBER. Both types include common part LNI_ORIG_RECORD <>'000' and AG4_GL_TYPE_CODE IN ('Y', 'A','X','M','Z,'R') |
| 68 | LCROS is operational table that does not store accrual details like single transaction amounts, but keeps accumulated amounts in accrual process. LACCR is accrual reporting table which actually stores the accrual details correspondent to accounting history table LACTG04. To use LACCR make sure that it is not purged or cleaned up. Link between LACTG04 and LACCR may be presented as AG4_LC_PREFIX // LPAD (LACTG04.AG4_LC_NUMBER,6,0) = ACR_TRANSACTION_NO and LPAD(AG4_LC_SEQUENCE,3,0) = ACR_TRANS_SEQ and AG4_TRAN_CREATE_DT = ACR_ACCRUED_TO_DT AND AG4_TRANS_AMOUNT = ACR_ CURRENT_ACCRL. Mnemonic AG4 and LACCR equal only for credit. Accrual debit saves in LACCR same mnemonic as per credit, but in AG4 linked via R300TD3 debit mnemonic. AG4 account is not customer (or other party) account, but content of R300TD2 mnemonic description. AG4_GL_TYPE_CODE=’A’ for accrual, but if accrual involved into cancelation the AG4_GL_TYPE_CODE=’C’, into standby AG4_GL_TYPE_CODE=’S’ |
| 69 | Facility is active if FC0_APPROVE_IND='Y' and FC0_BLOCKED_IND<>'Y'. In use indicator XFC_FCL_IN_USE_IND=’Y’ is for pausing facility usage during update by user. In case of expire date Banktrade allows usage of the facility but with warning and request for additional authorization. |
| 70 | Mature (closed) acceptance is C05_MTR_ACPT_REL_I='Y' |
| 71 | Fields C40_SHIP_TO and C40_SHIP_FROM are used for shipping attributes instead of C00_SHIP_TO and C00_SHIP_FROM |
| 72 | Loan settled criteria LNI_PRINCPL_OUTSTD=0 AND LNI_INTERST_OUTSTD=0 AND LNI_CHARGE_AMT_1 = LNI_CHG_AMT_1_PAID AND LNI_CHARGE_AMT_2 = LNI_CHG_AMT_2_PAID AND LNI_TRACE_FEES_TOT=LNI_TRAC_FEES_PAID |
| 73 | LC Usance (payment delayed=acceptance) sometimes is called as LC Deferred Balance. For such LC current balance is sum of C00_CONF_OPEN_BAL+C00_UNCNF_OPEN_BAL+NVL((SELECT SUM(C05_ACCEPTANCE_AMT) FROM LOLOC05 WHERE C05_GROUP=C00_GROUP AND C05_NUMBER=C00_NUMBER AND C05_CREATE_ACCEPT='Y' AND C05_MTR_ACPT_REL_I<>'Y' AND C05_RELEASE_CODE_2>299),0) in Oracle syntax |
| 74 | LC amendment to change open amount stores just the increase/decrease amount but not new open amount. LC issue record keep original open amount but modified balance. To get LC actual (“face”) the following formula is applied in Banktrade: if L0-ORIG-CURRENCY-CODE = L0-CURRENCY-CODE then L0-CONFIRM-OPEN-AMT+L0-UNCONFIRM-OPEN-AMT+L0-CONFIRM-AMEND-ADJ+L0-UNCONFIRM-AMEND-ADJ else L0-CONFIRM-AMEND-ADJ+L0-UNCONFIRM-AMEND-ADJ+L55-CONFIRM-OPEN-AMT-LATEST+L55-UNCONF-OPEN-AMT-LATEST. In SQL the following expression: CASE WHEN C00_ORIG_CURR_CODE = C00_CURRENCY_CODE THEN C00_CONF_OPEN_AMT+C00_UNCNF_OPEN_AMT+C00_CONF_AMEND_ADJ + C00_UNCNF_AMND_ADJ WHEN XL55_CNF_OPN_AM_LT IS NOT NULL THEN C00_CONF_AMEND_ADJ + C00_UNCNF_AMND_ADJ+XL55_CNF_OPN_AM_LT + XL55_UNC_OPN_AM_LT ELSE C00_CONF_AMEND_ADJ + C00_UNCNF_AMND_ADJ END |
| 75 | To get total commissions and expenses (charges) per LC issue it is possible to sum credit amounts from LACTG04 with filtration by appropriate mnemonics which are customer specific. However, the other option (LACTG02) seems simpler: LEFT JOIN (SELECT AG2_LC_PREFIX, AG2_LC_NUMBER, SUM(AG2_COMMISSION_AMT) Amount FROM LACTG02 WHERE AG2_CMSN_TYPE_CODE IN ('IM','IB','MU','IA','IT','PT') AND AG2_CMSN_STATUS_CD = 'T' GROUP BY AG2_LC_PREFIX, AG2_LC_NUMBER) LACTG02 ON AG2_LC_PREFIX=C00_GROUP AND AG2_LC_NUMBER=CAST(C00_NUMBER AS INTEGER) |
| 76 | The regular way to get sum of all LC issue related payments is sum of all drawing amounts (10,screen LP25) from LOLOC07 for all released payment records. However, Banktrade allows to overdraw balance (make it negative). To avoid such case better to get sum of payments from LLOGA table (type=’03’): LEFT JOIN (SELECT LGA_PREFIX, LGA_NUMB, SUM(CASE C43_DISB_EXCH_RT_I WHEN 'D' THEN (LGA_CONFIRM_AMT+LGA_UNCONFIRM_AMT)/C06_PAYEE_EXCH_RT ELSE (LGA_CONFIRM_AMT + LGA_UNCONFIRM_AMT)*C06_PAYEE_EXCH_RT END) Amount FROM LLOGA INNER JOIN LOLOC06 ON LGA_PREFIX=C06_GROUP AND LGA_NUMB=C06_NUMBER AND LGA_SEQ= CAST(C06_TYPE_SEQ AS INTEGER) INNER JOIN LOLOC43 ON LGA_PREFIX=C43_GROUP AND LGA_NUMB=C43_NUMBER AND LGA_SEQ = CAST(C43_TYPE_SEQ AS INTEGER) WHERE LGA_AUTH_REL_CODE2>299 AND LGA_REC_TYPE = '03' GROUP BY LGA_PREFIX, LGA_NUMB) LLOGA ON LGA_PREFIX=C00_GROUP AND LGA_NUMB=C00_NUMBER |
| 77 | Collection cancellation indication is existing of correspondent to transaction number (not sequence) in LCANL01 table: LEFT JOIN LCANL01 ON CN1_LC_GROUP=C30_GROUP AND CN1_LC_NUMBER= C30_NUMBER AND CN1_RECORD_TYPE='30' AND CN1_TYPE_REC<>'D' |
| 78 | For Collection Issue exchange rate should be retrieved from C31_BOOK_EXCH_RATE and interpreted based on C31_BOOK_EXRT_IND (“D” means “divide”) |
| 79 | The Collection actual (“face”) open amount is located in latest Amendment (sequence 000) as well as latest balance |
| 80 | Reimbursement is product to replace direct transfer amount in required foreign currency to target bank by transfer correspondent amount in existing currency to intermediate bank. The intermediate bank provides transfer required amount of required foreign currency to target bank. Customer in reimbursement transactions is issued bank. Reimbursement tables (LOLOC20 – issue, amendment, LOLOC22 - payment) have similar structure and functions as correspondent Collection tables. |
| 81 | Periodic commission (tier pricing) can be identified via LPRTR.XPR_TR_PRD_CMM_IND=’Y’ |
| 82 | Commission in tables LDFPY03 and LACTG04 can be identified via rule 300 (mnemonics) TCT4=1 |
| 83 | Taken commission in table LACTG02 can be identified via AG2_CMSN_TYPE_CODE IN ('IS','MU', 'SB','CA','IM','IT', 'AM','MN','PM','AT', 'PA', 'AC','DI','MC', 'MP','PI','MC','MN', 'CA') with AG2_CMSN_STATUS_CD='T' |
| 84 | Weekends and holidays are configured in rule 908 counters with item WEEKEND and HOLIDAYxx. |
| 85 | Collection maturity date is related to creating of collection acceptance. The criteria is C30_TENORDOC_AGNST='D/A' |
| 86 | Loan group means a few loans with same prefix and number but different sequence in table LLNIS05 |
| 87 | Loan payment number does not include loan number. Link between payment number and loan number provided in table LLNPY. LLOGA table provides loan payment identification by LGA_REC_TYPE = '72', but payment amount can be retrieved from LNP_PRINCPL_PD_BC (base currency), LNP_PRINCPL_PD_LC (LC currency), LNP_PRINCPL_PD_PC (loan currency) |
| 88 | Link between LACTG04 and LOLOC30 (sequence specific): AG4_GL_TYPE_CODE IN ('I','A') AND AG4_LC_PREFIX = C30_GROUP AND LPAD(AG4_LC_NUMBER,6,'0') = C30_NUMBER AND AG4_LC_SEQUENCE = C30_AMEND_CNT |
| 89 | Link between LACTG04 and LLOGA: LGA_PREFIX = AG4_LC_PREFIX AND TO_NUMBER(LGA_NUMB) = AG4_LC_NUMBER AND LGA_SEQ = CASE WHEN LGA_REC_TYPE='30' THEN TO_NUMBER(C30_TYPE_SEQ) ELSE AG4_LC_SEQUENCE END AND (AG4_GL_TYPE_CODE = 'L' AND LGA_REC_TYPE IN ('00') OR AG4_GL_TYPE_CODE = 'N' AND LGA_REC_TYPE IN ('01') OR AG4_GL_TYPE_CODE = 'J' AND LGA_REC_TYPE IN ('02') OR AG4_GL_TYPE_CODE = 'P' AND LGA_REC_TYPE IN ('03','22','32','41','92','98','80') OR AG4_GL_TYPE_CODE = 'C' AND LGA_REC_TYPE IN ('04','34') OR AG4_GL_TYPE_CODE = 'A' AND LGA_REC_TYPE IN ('51','52','30','90','73,’08’') OR AG4_GL_TYPE_CODE = 'D' AND LGA_REC_TYPE IN ('06','09') OR AG4_GL_TYPE_CODE = 'S' AND LGA_REC_TYPE IN ('08','40') OR AG4_GL_TYPE_CODE = 'R' AND LGA_REC_TYPE IN ('10','76') OR AG4_GL_TYPE_CODE = 'B' AND LGA_REC_TYPE IN ('53') OR AG4_GL_TYPE_CODE = 'M' AND LGA_REC_TYPE IN ('07','55','73','74')OR AG4_GL_TYPE_CODE = 'I' AND LGA_REC_TYPE IN ('30','90') OR AG4_GL_TYPE_CODE = 'F' AND LGA_REC_TYPE IN ('35','F3') OR AG4_GL_TYPE_CODE = 'T' AND LGA_REC_TYPE IN ('42','93') OR AG4_GL_TYPE_CODE = 'W' AND LGA_REC_TYPE IN ('43') OR AG4_GL_TYPE_CODE = 'K' AND LGA_REC_TYPE IN ('F6') OR AG4_GL_TYPE_CODE = 'Q' AND LGA_REC_TYPE IN ('F') OR AG4_GL_TYPE_CODE = 'Y' AND LGA_REC_TYPE IN ('70') OR AG4_GL_TYPE_CODE = 'Z' AND LGA_REC_TYPE IN ('72') OR AG4_GL_TYPE_CODE = 'X' AND LGA_REC_TYPE IN ('F') OR AG4_GL_TYPE_CODE = 'V' AND LGA_REC_TYPE IN ('99') OR AG4_GL_TYPE_CODE = 'O' AND LGA_REC_TYPE IN ('74') ) |
| 90 | Banktrade stores Fax and Email addresses under rule 998FAX[Acronym], 998EMAIL[Acronym] in TDS2. LACTM00 is source of Acronyms. The LAABR is index table for acronyms. Banktrade “multi-email address” option uses up to 6 addresses from LACTM00. To activate “multi-email address” option rule 998EMAILDEFAULT set TI12=Y |
| 91 | Banktrade indication of ClientTrade account is rule 908CB[Acronym] |
| 92 | LC issue tolerance (+/- percent) affects initial balance (not open amount) and LC issue amount in LLOGA. For example, Open=1000, tolerance=1, initial balance=1010, LLOGA amount=1010. If C00_ABOUT_MODIFER=’Y’ the tolerance is set as C00_PCT_MODIFER=10.00 (10%) without possibility to change. If C00_ABOUT_MODIFER=’N’ and C00_PCT_MODIFER_TP=’+’ or ‘-‘ then, if C00_PCT_MODIFER<>0 use it to calculate tolerance as percent, otherwise use amount C00_AMT_MODIFIER. If C00_ABOUT_MODIFER<>’Y’ and C00_PCT_MODIFER_TP is empty then no tolerance |
| 93 | Rule 111 (officer code) may be interpreted as business segment and linked to AM00 Officer Code |
| 94 | Amendment decrease amount C01_AB_INCR_DEC_IN=’D’ |
| 95 | From BTv14.0 commission type hard-coded identification LACTG02.AG2_CMSN_TYPE_CODE is not mandatory because commission input is combined on the same screen with charges input where user can select commission/charges identification from correspondent mnemonic (rule 300 SUBSTRING(TBF_SUB_FLD,1,2)). For Oracle use utl_raw.cast_to_varchar2 to convert raw data |
| 96 | Banktrade does not support acceptance balance C05_ACCEPT_BAL for all cases. To replace use C05_ACCEPTANCE_AMT if acceptance is not matured and 0 when matured |
| 97 | Manual LC issue identified by LTRIM(C00_INC_SWIFT_IND // C00_CTR_TRADE_IND) = '' |
| 98 | LC Advised means C00_CONF_CURR_BAL=0 AND C00_UNCNF_CURR_BAL>0. LC Confirmed means C00_CONF_CURR_BAL>0 AND C00_UNCNF_CURR_BAL=0 |
| 99 | Delayed LC payment (payments scheduled by future event, not Acceptance) can be activated with rule 998DLPREL TIN1=’Y’. With payment “release”, a record created in LTICK table TIK_LC_TYPE_CODE='DPR' AND TIK_PREFIX=C05_GROUP AND TIK_LC_NUMBER = C05_NUMBER AND TIK_LC_SEQUENCE = to_number(LOLOC05.C05_TYPE_SEQ, '999') without actual release on payment level. The actual release is occurred according to value XTKLR_YYMMDD_DATE (XTKLR_DD_IN, XTKLR_MM_IN, XTKLR_YY_IN). The criteria in payment table is C05_CREDIT_VALUEDT>='1'//TO_CHAR(sysdate, 'yymmdd') AND C05_CREATE_ACCEPT<>'Y' |
| 100 | LC Payment rate C06_PAYEE_EXCH_RT, currency C06_PAYEE_CURR_CD, amount C07_DRAWING_AMT_01+ …+C07_DRAWING_AMT_10, negotiation charge C02_NEGOT_BNK_CHRG, negotiation currency C07_NEGBK_CHGS_CUR |
| 101 | Released Payments criteria C02_RELEASE_CODE_2>=300, date C02_RELEASE_DATE, amount C07_DRAWING_AMT_01+ …+C07_DRAWING_AMT_10 |
| 102 | Import D.C. Shipment (Import Documentary Collection Shipment) is Shipment transaction (C00_LC_TYPE=’C’) derived from incoming collection (C30_RELATED_SG_NO=C00_GROUP// C00_NUMBER and C00_TRANS_FR_LC_NO=C30_GROUP//C30_NUMBER) |
| 103 | Import/Export D.C. Returned Unpaid/Unaccepted is returned to sender under “payment equal to UNPAID or UNACCEPTED” based on “Hold” release code in rule 903 (default value 151), that is C32_RELEASE_CODE1=151 or C32_RELEASE_CODE2=151 |
| 104 | Export D.C. Avalized Draft is Collection with Guarantee of Payment. Such transaction is derived from Rule 703 item (suffix)=32 and identified as C30_SUFFIX=’32’ |
| 105 | Mnemonics linked to collections are stored in Rule 703 TDS2. Rule 300 is definition for the Mnemonics. Counter TCT4=1 or 2 identify income mnemonics (fee, charge) |
| 106 | “Ever Green Standby” criteria C00_EXPR_LATE=999999 |
| 107 | Clean Acceptance (no linked LC) criteria C05_GROUP='A' |
| 108 | LC Liability amount C00_CONF_OPEN_AMT+C00_CONF_AMEND_ADJ (no unconfirmed) |
| 109 | To handle up to 5 digits WorkerNo, Banktrade has mechanism (activated via rule) to convert WorkerNo from base 10 to other base. For example, WorkerNo=122 (base 10) is presented as 3-byte code as 01y. If conversion is set, rule 106 TBF_ID=01y as well as other fields with WorkerNo (LUSER, LAUDT, etc.). When user enters 122 on Banktrade GUI, it automatically is converted to 01y and appears as WorkerId=01y. |
| 110 | Additional parties’ data can be found in LTXTV table. SWIFT related information is kept in XTX_LINE_ARRAY field. For each transaction (LC issue, payment, etc.) there can be up to 4 records with TX0_DOC_TYPE value 'K','L','M','N' sequentially and TX0_SOURCE_IND = 'EI'. Each additional party SWIFT IDs on the left (A) and on the right (B) can be found by parsing XTX_LINE_ARRAY field (XYYYYYY is a transaction number) as per statement SELECT SUBSTR(XTX_LINE_ARRAY,231,20) A,SUBSTR(XTX_LINE_ARRAY,2636,20) B FROM BII14T1.LTXTV WHERE TX0_SOURCE_IND = 'EI' AND TX0_DOC_TYPE IN ('K','L','M','N') AND XTX_LC_NUMBER = 'XYYYYYY' Checkbox ‘More Additional Parties’ adds a new record to LTXTV table for that transaction (first one with TX0_DOC_TYPE= ‘K’, second one ‘L’ and third one ‘M’ and fourth one ‘N’) |
| 111 | SWIFTID on the MT747 field can be found in one of fields C50_REIM_SW_ID_ORG (original) or C50_REIM_SW_ID_LAT (latest) in LOLOC50 table as per statement SELECT C50_REIM_SW_ID_ORG, C50_REIM_SW_ID_LAT FROM BII14T1.LOLOC50 WHERE C50_GROUP='X' AND C50_NUMBER='YYYYYY' |
| 112 | To calculate date for 14 days+Expiry Date as (DB2 syntax) SELECT NUM2DATE(C00_EXPR_LATE)+14 DAYS FROM BII14T1.LOLOC00 WHERE C00_GROUP='X' AND C00_NUMBER='YYYYYY' To calculate the number of days for Maturity Date–Acceptance Date as (DB2 syntax) SELECT ABS(DAYS(NUM2DATE(C05_DATE_DUE_HERE))-DAYS(NUM2DATE(XL5_ACP_RELES_DATE))),C05_ACCEPT_NO_DAYS FROM BII14T1.LOLOC05 WHERE C05_RELEASE_CODE_2>299 AND C05_GROUP='X' AND C05_NUMBER='YYYYYY' |
| 113 | If counter 10 of rule 703 for the Collection suffix is greater than 0, then the Collection is avalized/guaranteed – which is interpreted as Confirmed amount of Collection transaction. Otherwise Collection transaction open amount can be interpreted as Unconfirmed. |
| 114 | Processing margin balance is cash collateral balance C55_CASH_COLL_BAL, C55_CASH_COLL_BAS Processing margin is cash collateral original amount C55_CASH_COL_ORGA, C55_CASH_COL_ORGB |
| 115 | Documentary Collection is related to import or export of good, the client needs to present documents to be sent in collection in order to get paid If third (3) character of LTABL.TBF_DESCRIPTION_2 is ‘D’ for LTABL.TBF_NUM = ‘703’ AND LTABL.TBF_ID= LOLOC30.C30_SUFFIX then it is Documentary Collection |
| 116 | Clean Collection is related to the presentation of checks, traveler checks or draft to be collected If third (3) character of LTABL.TBF_DESCRIPTION_2 is ‘C’ for LTABL.TBF_NUM = ‘703’ AND LTABL.TBF_ID= LOLOC30.C30_SUFFIX then it is Clean Collection |
| 117 | Direct Collection is only related to outgoing (Export) the exporter gets Bank’s remittance letters with a range of numbers. the exporter (drawer or presenter) will use those remittance letters (or letter of instructions) to send the documents to the buyer (importer or drawee) The exporter presents a copy of such letter to his/her bank so the bank can record the transaction and collect the funds If LOLOC30.C30_GROUP= ‘D’ or if LOLOC30.C30_GROUP<> ‘D’ and LOCLOC30.XC0_COLL_TYPE = ‘D’ then it is Direct Collection |
| 118 | Multi-Draft Collection is a set of documents with instructions to collect funds in installments (30, 60, etc. days). What our system does is record those installment under consecutive collection numbers and split the amounts among those collections If LOLOC31.XC1_NMBR_OF_DRFTS >0 OR LOLOC301.XC1_MAN_DRF_CL_NMB <> ‘ ’ then it is Multi-Draft Collection. Note if LOLOC31.XC1_NMBR_OF_DRFTS >0 then it is Main Draft . If LOLOC301.XC1_MAN_DRF_CL_NMB <> ‘ ’ then it is Sub Draft |
| 119 | Table LLNBL15 stores all loan accrual data |
| 120 | Get loan related “taken” commissions from LACTG02 with inner join to LLNIS05 original record |
| 121 | Loan disbursement amount LLNIS03.XLN3_PY_PAY_DSB_AM |
| 122 | Passive Loan type LLNIS05.LNI_LOAN_TYPE=’I’, active loans LNI_LOAN_TYPE<>’I’ |
| 123 | Manual GL transaction indicator AG4_GL_TYPE_CODE=’V’ |
| 124 | Contract means specific agreement per transaction to apply exchange rate (usually for customer payment, but sometimes for issue). There is debit, credit, multiple contracts. Corresponding contract (size CHAR(15)) values are stored in corresponding payment tables. In case of multiple contract, payment table contract value=’*’. It means corresponding data (contract, exchange rates, etc.) are located in LDFPY02 table |
| 125 | LDFPY00, 01, 02, 03, 04 tables to store charges and payments after calculation or not paid. Charges are 3rd party service provided via bank (cable, mail, SWIFT, etc.), commissions are bank service |
| 126 | AG2_APPL_TYPE defines product (LC-Letter of Credit, CL, LN, etc.), XAF_TRN_TYPE defines event (I-issue, A, J, P, etc.), AG2_FOR_ACCOUNT_CD defines commission payer type (B-beneficiary, C-customer, etc.) |
| 127 | In case of “manual GL” LGA_REC_TYPE ='99' and XLA_REF_REC_TYPE value defines related product-event code according to LGA_REC_TYPE hard-coded values. Actual “manual GL” transaction number is XLA_REF_TRAN_NUMBR, XLA_REF_SEQ1, XLA_REF_SEQ2 to be found in transaction tables (LOLOC00, LOLOC30, LLNIS05, etc.) |
| 128 | In Banktrade LC Account Party very often is called Applicant Export LC: Customer=Customer, Counter Party Bank=Applicant, Counter Party=Beneficiary Import LC: Customer=Customer, Counter Party Bank=Advising Bank, Counter Party=Applicant Incoming Collection: Customer=Payer, Counter Party Bank=Payer, Counter Party=Presenter Outgoing Collection: Customer=Presenter, Counter Party Bank=Presenter, Counter Party=Payer |
| 129 | Terminology: LC Import=LC Issued=LC Issuance=LC Opening=LC Issue, LC Export=LC Received=LC Advising, Import LC Payment=Import LC Settlement, Incoming Collection=Inward Collection, Outgoing Collection=Outward Collection, Incoming Collection Payment=Inward Collection Settlement, Outgoing Collection Payment=Outward Collection Settlement, Loan=Bill Purchased Guarantee Received=Pass-On Guarantee Guarantee Issued=All other Guarantee except Pass-On |
| 130 | Advising Bank (intermediate bank) appears in LC transaction when Issued Bank has no account in Beneficiary Bank. In can be no Advising Bank or multiple Advising Banks per LC transaction. |
| 132 | Declaration transaction is transaction follow up any transaction with foreign currency. Main tables: LDCIA00(central) , LDSFN (cross-ref), LDCIA01/02/03/3A/04/05 (header Format 1/2/3/3A/4/5), LDCDT11/12/02/31/32/3A/05 (details Format 1/2/3/3A/5) |
| 133 | Remittance transaction is check to pay for group of outgoing clean collections linked to the same customer and currency. Main tables: LRM00 (header), LRM01 (details==collections) |
| 134 | LDFPY00, LDFPY01 tables serve to stores deferred income payment transactions (DP0_PAYM_DATE is transaction number (7) – actual date, DP0_PAY_SEQ is sequence (3) per date) identified in LLOGA as LGA_REC_TYPE=98. Each payment (from customer) covers commissions, charges, fee, etc. from multiple regular transactions (LC, COL, etc.). User has GUI to choose transactions (up to 30 in one payment) to be included into the payment. LDFPY00 is deferred payment header record (DP0_TOTAMT_APPLIED is total amount from customer, DP0_LIQUIDATN_AMT is used portion of the total amount, DP0_UNUSED_AMOUNT is unused portion to be return to customer), but LDFPY01 contains details per each regular transaction included into the payment. |
| 135 | LGLXL contains general ledger data before release/approve. To separate status (release/not release) link to corresponding transaction table (issue, amendment, payment) is mandatory. After release corresponding records from LGLXL are moved to LACTG04 table. Manual GL transactions are not stored in LGLXL. XLCGLXL_RECRD_TYPE has value as per field LGA_REC_TYPE |
| 136 | LACTG04.AG4_ACCOUNT_NUMBER is regular customer account (15). For extended customer account (35 chars) use XAF_04_ACC_NMB_EXT |
| 137 | LGLGX is used for automatic (GLF_TRAN_TYPE_CODE=’A’) entries and manual GL (GLF_TRAN_TYPE_CODE=’M’). Field GLF_ACT_STATUS_IND<>'Y' (or blank?) means unreleased manual GL transaction. GLF_REF_TO_NUMBER is related (parent) transaction |
| 138 | LOLOC06 store payees (one payee per record) linked to a payment. LOLOC07 store payment parts (up to 10 broken to confirmed and unconfirmed portions). The payee set is related to payment distribution (according to it contribution to LC) and not related to payment parts. User has options to enter payment parts (confirmed/unconfirmed) or just drawing amount. After payment release actual amounts for the payment (confirmed/unconfirmed) are stored in LLOGA. |
| 139 | Fields XL2_RECORD_SEQUENC, XL5_RECORD_SEQUENC, XL7_RECORD_SEQUENC identify modification of payment/acceptance as XXXIYY, where I value ‘A’ means acceptance, ‘P’ – payment, XXX – sequential number of acceptance modification, YY – sequential number of payment modification. In any case actual (late) payment/acceptance is identified by value ‘000000’ in these fields. |
| 140 | LTICK.TIK_LC_TYPE_CODE field defines type future event (automatic). For example, ‘DPR’ means deferred payment release set release date of delayed payment. |
|  |  |
|  |  |
|  |  |

### 29. Sample Report and SQL Query (example output)

| LC Number | Release Date | Customer Name | Type | Product | Liability Code | Currency Code | Open Amount | O/S Balance | Balance in Base |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
| … |  |  |  |  |  |  |  |  |  |
| Total |  |  | XXX |  | XXX.XX |  |  |  |  |

