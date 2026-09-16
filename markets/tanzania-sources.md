# Tanzania source registry

Routes below were checked on **2026-09-17** unless stated. Websites change: re-check the route when you use it, record the access date and exact locator, and label failures rather than filling gaps from memory. Reasoning rules for using these sources are in [tanzania.md](tanzania.md). Source class helps discovery; it does not set confidence ([../references/evidence-model.md](../references/evidence-model.md)).

## Contents
1. Official statistics
2. Central bank and finance
3. Regulators and revenue authorities
4. Company filings
5. International and development sources
6. Other signals
7. Access notes and known pitfalls

## 1. Official statistics

| Source | Verified route | Formats and access | Cadence observed | Measures and cautions |
|---|---|---|---|---|
| National Bureau of Statistics (NBS) | https://www.nbs.go.tz/statistics — topic pages: CPI `/statistics/topic/consumer-price-index-2026`; Census `/statistics/topic/census-2022` and https://sensa.nbs.go.tz/; Household Budget Survey `/statistics/topic/household-budget-survey-hbs`; Labour force `/statistics/topic/labour-and-employment-report`; GDP `/statistics/topic/gross-domestic-product-gdp`; national accounts `/statistics/topic/annual-national-accounts-publications`; advance release calendar page for FY 2025-2026 | PDF releases; CPI also XLS summary; GDP XLS/XLSX; HBS PDF and ZIP. No registration for publications | CPI monthly (released around the 8th–10th); GDP quarterly; national accounts annual; labour force key findings annual | NCPI covers **Mainland only** (26 regional headquarters; base 2020 = 100; weights from HBS 2017/18). Last full HBS fieldwork 2017/18; a 2024/25 pilot report exists. One GDP XLSX file name did not match its quarter — check contents, not file names |
| NBS microdata catalogue (NADA) | https://microdata.nbs.go.tz/index.php/catalog | Study metadata open; **microdata download requires a free registered account** | Per study | Check questionnaire, sampling and weights documentation before analysis |
| Tanzania Integrated Statistical Portal (TISP) | https://tisp.nbs.go.tz/ | Interactive dashboards (JavaScript); download buttons present in the application; not tested | Not verified | Record the indicator definition and update date shown in the dashboard |
| Office of the Chief Government Statistician, Zanzibar (OCGS) | http://www.ocgs.go.tz — CPI publications `/publication-report/140`; monthly news summaries | PDF | Zanzibar CPI monthly | **Separate from NBS Mainland CPI.** HTTPS was misconfigured at check; plain HTTP worked |

## 2. Central bank and finance

| Source | Verified route | Formats and access | Cadence observed | Measures and cautions |
|---|---|---|---|---|
| Bank of Tanzania (BoT) | https://www.bot.go.tz/ — Monthly Economic Review `/Publications/Filter/1`; Quarterly Statistical Bulletin `/Publications/Filter/50`; financial inclusion reports under `/DFDI/Publications` | PDF | Monthly Economic Review monthly; bulletin quarterly | The `/Statistics` page returned a login page at check; payment-systems spreadsheet links returned 404. Site defaults to Kiswahili. Mobile money statistics count accounts and transactions, not unique users |
| FSDT — FinScope Tanzania | https://www.fsdt.or.tz/finscope/ | Summary PDFs download directly; 2023 full report and datasets sit behind a request form | Irregular editions: 2006, 2009, 2013, 2017, 2023 | Demand-side financial inclusion survey of adults; check age definition, sample and fieldwork dates |

## 3. Regulators and revenue authorities

| Source | Verified route | Formats and access | Cadence observed | Measures and cautions |
|---|---|---|---|---|
| Tanzania Communications Regulatory Authority (TCRA) | https://www.tcra.go.tz/publications/statistics — quarterly report pages such as `/publications/statistics/2026/q4` | PDF (tables extractable) | Quarterly (June 2026 quarter published August 2026) | **Subscriptions = SIMs used at least once in 90 days**, including machine-to-machine SIMs and fixed lines. Penetration can exceed 100% and the report does not state its population denominator. Not unique people |
| Tanzania Revenue Authority (TRA) | https://www.tra.go.tz/resource-center/14 (collection statistics by fiscal year) | XLSX/XLS | Updated quarterly within fiscal-year files | Revenue collections, not consumption; listing dates may lag file updates |
| Zanzibar Revenue Authority | https://www.zanrevenue.org/ | Website | — | `zra.go.tz` resolved but timed out at check; OCGS links to zanrevenue.org |
| Tanzania Bureau of Standards (TBS) | https://www.tbs.go.tz/certified-product-companies | HTML table (company, product, brand, licence, standard, dates) | Updated continuously | Certification status, useful for competitor and category mapping; not sales |
| Tanzania Medicines and Medical Devices Authority (TMDA) | https://www.tmda.go.tz/pages/approved-product-information; registered medicines portal https://imis2.tmda.go.tz/portal/#/public/registered-medicines | HTML list, PDFs, JavaScript portal | Not verified | Product approvals for regulated categories |
| Fair Competition Commission (FCC) | https://fcc.go.tz/ — Publications → Decisions | JavaScript listing | Not verified | Merger and competition decisions |
| Energy and Water Utilities Regulatory Authority (EWURA) | https://www.ewura.go.tz/publications/petroleum-price | PDF (monthly cap prices) | Monthly | Fuel cap prices; relevant to distribution cost context, not a firm's actual costs |

## 4. Company filings

| Source | Verified route | Formats and access | Cautions |
|---|---|---|---|
| Dar es Salaam Stock Exchange (DSE) | https://dse.co.tz/listed/company/financial/statement (select company and report type) | PDF annual, interim and quarterly reports; free download | `www.dse.co.tz` failed at check (certificate problem); use `dse.co.tz`. Company reports establish what the company reports; segment definitions vary |

## 5. International and development sources

| Source | Verified route | Formats and access | Cautions |
|---|---|---|---|
| World Bank Indicators API | `https://api.worldbank.org/v2/country/TZA/indicator/<CODE>?format=json` (responded at check) | JSON; open | Many values are modelled estimates; record indicator code, definition and `lastupdated` |
| World Bank Global Findex | https://www.worldbank.org/en/publication/globalfindex (data download page linked) | XLSX, CSV, DTA; open | Survey of adults 15+; account ownership includes mobile money accounts per indicator definition |
| IMF Tanzania | https://www.imf.org/en/countries/tza | Web and PDF | Blocked automated access from the checking network (403); may need a normal browser |
| African Development Bank Tanzania | https://www.afdb.org/en/countries/east-africa/tanzania | Web and PDF | Automated access blocked at check; `dataportal.afdb.org`, `opendata.go.tz` and `data.go.tz` did not resolve. A Knoema-run Tanzania data portal exists at https://tanzania.opendataforafrica.org/ (sign-up links present; data coverage not verified) |
| UN agencies, GSMA and other international industry research | Use the original report pages; verify on use | Varies | Check methodology and whether figures are modelled, surveyed or reported |

## 6. Other signals

Use with explicit limitations; they indicate, they do not establish:
- **Reputable Tanzanian journalism** (national dailies, business press): useful for events, launches and policy changes; trace statistics back to original releases.
- **Company websites and press releases**: what the company claims.
- **Ad libraries and observed advertising**: presence and messages, not spend or effect.
- **Search and social signals**: relative interest and conversation, not demand volume or representativeness; urban and connected audiences over-represented.
- **Store checks and field visits**: direct observation of availability and price at the outlets visited; not representative without a sampling plan.
- **Industry reports from commercial providers**: check methodology disclosure, sample, and whether figures are forecasts.

## 7. Access notes and known pitfalls

- Many official sources publish PDFs; extract tables carefully and record page and table numbers.
- Publication dates and data periods often differ by months or years.
- Mainland and Zanzibar statistics are frequently separate.
- Several government sites default to Kiswahili; English versions may lag.
- Investment portals and news sites often republish official figures; cite the original.
- When a site is unreachable, record the attempt and date, and do not substitute a remembered figure.
