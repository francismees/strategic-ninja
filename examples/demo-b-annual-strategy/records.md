# Engagement records: ENG-fizzi-2027-annual-plan

> **Synthetic teaching fixture — not real client data.**

- **Decision:** Choose Fizzi Cola's 2027 growth route and allocate the flat TZS 3,200 million marketing and trade budget
- **Decision-maker:** CEO and commercial leadership, Fizzi Beverages (fictional)
- **Audience:** Leadership team and board (fictional)
- **Client / brand / category / market:** Fizzi Beverages (fictional) / Fizzi Cola (fictional) / Carbonated soft drinks / Tanzania Mainland: Dar es Salaam, Mwanza, Arusha, Dodoma
- **Horizon:** annual
- **Outcome:** Return Fizzi to buyer growth in Dar es Salaam and Mwanza in 2027 without diluting margin
- **Success metric:** Household penetration (52-week panel) in Dar es Salaam and Mwanza, with volume and contribution as outcomes
- **Baseline:** 52 weeks to June 2026: penetration 34% Dar es Salaam, 30% Mwanza; Dar es Salaam volume +2.3%, Mwanza -7.0% versus prior 52 weeks
- **Scope:** Brand, pack, channel and communications choices for 2027 in four regions
- **Mode / depth:** build_strategy / standard
- **Constraints:** Budget flat at TZS 3,200 million; Distributor service in Mwanza and Arusha still being repaired (Demo A); No premium product development capacity in 2027
- **Unresolved questions:** Does the cooler uplift hold outside the Dar es Salaam pilot outlets?; Which brand comes to mind for a cold drink on the way home?; How many high-footfall outlets have a 350 ml baseline near 59 litres per week?

## Sources

| ID | Title | Publisher | Locator | Data period | Geography | Method | Lineage | Limitations |
|---|---|---|---|---|---|---|---|---|
| SRC-B01 | Demo A diagnosis records (H1 2026) | Strategy team (fictional) | INS-A01, OPT-A01, CLM-A02, CLM-A03 | H1 2025 vs H1 2026 | Four regions | Prior diagnosis reused after checking for review flags (none open) | derived  | Inherits Demo A limits: sell-in data, rough rate-of-sale proxy |
| SRC-B02 | Household panel by region, 52 weeks to June 2025 and June 2026 (synthetic) | Household panel provider (fictional) | All 4 rows | 52 weeks to June 2025; 52 weeks to June 2026 | Dar es Salaam and Mwanza households | Household purchase panel, projected | original  | Household (not individual) purchases; out-of-home consumption under-recorded; projection error not supplied |
| SRC-B03 | Household panel by pack, Dar es Salaam (synthetic) | Household panel provider (fictional) | All 6 rows | 52 weeks to June 2025; 52 weeks to June 2026 | Dar es Salaam households | Household purchase panel, projected, by pack | original  | Out-of-home single-serve purchases likely under-recorded, so 350 ml buyer counts are conservative |
| SRC-B04 | Cooler pilot, 22 cooler outlets and 22 matched outlets (synthetic) | Fizzi Beverages trade marketing (fictional) | All 4 rows | 10 weeks before and after March 2026 installation | Dar es Salaam dukas near transport stages | Matched comparison, not randomised | original  | Small, one city, matched not randomised; visibility and chilling effects not separated |
| SRC-B05 | Commuter and duka shopper intercept interviews, May 2026 (synthetic) | Insights team (fictional) | Respondents R01-R10 | May 2026 | Two Dar es Salaam bus stages; one Mwanza market street | Short intercept interviews in Kiswahili; analyst glosses | original  | Ten interviews at three locations; glosses not independently verified; explains mechanisms, not prevalence |
| SRC-B06 | 2026 annual plan deck (synthetic) | Fizzi Beverages marketing (fictional) | Item 1 (plan slide 9) | unknown: no data cited on the slide | Tanzania (unspecified) | unknown: planning assertion without cited basis | unknown  | Same sentence repeated in 2024, 2025 and 2026 plans with no underlying data |
| SRC-B07 | Retail audit, Q2 2025 and Q2 2026 (synthetic) | Audit supplier (fictional) | Item 2 (audit table 4) | Q2 2025 and Q2 2026 | Audited urban outlets, Dar es Salaam and Mwanza | Store audit projected to audited universe | original  | Urban audited universe; informal outlets under-covered |
| SRC-B08 | Route supervisor reports on competitor activity (synthetic) | Fizzi Beverages sales team (fictional) | Item 3 | 2025 to June 2026 | Dar es Salaam | Field observation estimates, not counts | original  | Estimate range only; no competitor sales data |
| SRC-B09 | East Africa On-the-Go Drinks 2025 (fictional regional study) | Research firm (fictional) | Item 4 | 2025 | Nairobi, Kenya | Survey | original  | Kenyan city; transfer to Tanzania untested |
| SRC-B10 | Budget, cooler quote and margin estimate (synthetic) | Fizzi Beverages finance and procurement (fictional) | Items 5-6 | 2026 estimates for 2027 | Company-wide | Budget allocation, supplier quote, finance estimate | original  | Margin is an internal estimate; quote may change with volume |
| SRC-B11 | Brand tracker H1 2026 (synthetic) | Research agency (fictional) | Summary table | H1 2025 and H1 2026 waves | Urban Dar es Salaam, Mwanza, Arusha | Face-to-face survey | original  | No situational retrieval measure; urban only |
| SRC-TZ-NBS-NCPI-2026-08 | National Consumer Price Index (NCPI) for August 2026 | National Bureau of Statistics (NBS), Tanzania | p.2, Table 1: 'TOTAL - ALL ITEMS INDEX' and '7 Transport', 12-month change | August 2026 compared with August 2025 | Tanzania Mainland | Consumer price index, base 2020 = 100 | original  | Mainland only; household consumer prices, not firm costs |

## Claims and findings

| ID | Statement | Type | Basis | Confidence | Market applicability | Verification | Used by |
|---|---|---|---|---|---|---|---|
| CLM-B01 | In Dar es Salaam, Fizzi household penetration fell from 36% to 34% while purchase occasions per buyer rose from 12 to 13; volume grew 2.3%, with a penetration effect of -330,000 litres offset by a frequency effect of +462,000 litres | computed | SRC-B02 | medium — Reconciled panel decomposition; projection error not supplied | local_verified (Dar es Salaam households) | reproduced | INS-B01; OPT-B03 |
| CLM-B02 | In Mwanza, penetration fell from 34% to 30% and volume fell 7.0%, mostly through fewer buying households | computed | SRC-B02 | medium — Reconciled panel decomposition; smaller panel | local_verified (Mwanza households) | reproduced |  |
| CLM-B03 | In Dar es Salaam the 350 ml pack lost buyers (penetration 21.7% to 18.4%; bottles -12.2%) while the 1.25 L pack grew 21.9% through more buyers and higher frequency (7 to 8 occasions); 500 ml fell 2.9% | computed | SRC-B03 | medium — Reconciled; out-of-home 350 ml purchases likely under-recorded | local_verified (Dar es Salaam households) | reproduced | HYP-B01; INS-B01; OPT-B01; OPT-B03 |
| CLM-B04 | Cooler outlets sold about 20.9 more litres of 350 ml per week than their matched-control counterfactual (49% uplift) in the ten weeks after installation; the 500 ml effect was small | computed | SRC-B04 | medium — Matched comparison with pre-period; small sample, one city | local_supported (Dar es Salaam dukas near transport stages) | reproduced | ASM-B02; CLM-B05; HYP-B01; INS-B01; OPT-B01 |
| CLM-B05 | At pilot-level uplift a cooler pays back in about 3.1 years; a two-year payback needs about 29 incremental litres per week, implying outlets with a 350 ml baseline near 59 litres per week | estimate | SRC-B04; SRC-B10; CLM-B04 | low — Built on a small pilot and internal estimates | local_supported (Dar es Salaam high-footfall dukas) | unverified | OPT-B01 |
| CLM-B06 | Six of ten interviewees described cold availability as deciding an on-the-go purchase, and none raised price as a barrier | observed | SRC-B05 | low — Small purposive sample at three locations | local_supported (Commuters at two Dar es Salaam stages and one Mwanza street) | verified | HYP-B01; INS-B01 |
| CLM-B07 | R02 (Dar es Salaam bus stage): "Fizzi ilikuwa ya moto, nikachukua hii" (analyst gloss: "Fizzi was warm, so I took this one") | observed | SRC-B05 | medium — Exact quote from transcript excerpt; single respondent | local_supported (One respondent, Dar es Salaam) | verified | HYP-B01; INS-B01 |
| CLM-B08 | The claim that modern trade will reach 25% of category value by 2027 appears unchanged in the 2024, 2025 and 2026 plans with no supporting data | observed | SRC-B06 | high — Directly observed in the plan documents | not_applicable (Internal planning documents) | verified | ASM-B01; INS-B02; OPT-B04 |
| CLM-B09 | Modern trade share of urban category value was 14% in both Q2 2025 and Q2 2026 | observed | SRC-B07 | medium — Direct category measure; informal outlets under-covered | local_verified (Audited urban outlets, Dar es Salaam and Mwanza) | verified | INS-B02 |
| CLM-B10 | Route supervisors estimate that Bora Cola placed branded coolers in 1,500-2,500 Dar es Salaam dukas near transport stages during 2025 | observed | SRC-B08 | low — Supervisor estimates, not counts | local_supported (Dar es Salaam dukas near stages) | verified | HYP-B01; HYP-B02 |
| CLM-B11 | A Nairobi survey reports rising single-serve chilled purchases and faster growth for 250 ml than 350 ml packs | observed | SRC-B09 | low — Regional proxy with unknown method detail | regional_proxy (Nairobi urban adults) | verified |  |
| CLM-B12 | The 2027 budget is TZS 3,200 million (flat); coolers cost TZS 1.6 million installed plus TZS 0.25 million a year to maintain; 350 ml contribution is about TZS 700 per litre | observed | SRC-B10 | medium — Internal figures; margin is an estimate | not_applicable (Company figures) | verified |  |
| CLM-B13 | Tracker consideration (52% to 51%) and value perception (58% to 57%) were stable; the tracker does not measure brand retrieval in specific buying situations | observed | SRC-B11 | medium — Consistent survey measures | local_supported (Urban Dar es Salaam, Mwanza, Arusha) | verified | HYP-B02; HYP-B03 |
| CLM-TZ-002 | Transport division prices rose 13.8% over the 12 months to August 2026 in the Mainland NCPI | observed | SRC-TZ-NBS-NCPI-2026-08 | high — Official release, direct measure | local_verified (Tanzania Mainland, household transport prices) | verified |  |

## Hypotheses and assumptions

| ID | Kind | Proposition | Confirming signal | Falsifier | Support | Status | Decision impact | Validation step | Used by |
|---|---|---|---|---|---|---|---|---|---|
| HYP-B01 | hypothesis | Fizzi is losing 350 ml buyers in Dar es Salaam mainly because cold Fizzi is often unavailable at on-the-go purchase points, where a competitor has expanded coolers | 350 ml buyer loss concentrated among out-of-home or commuter purchasers; cooler outlets recover 350 ml sales; switching accounts cite warm or absent Fizzi | 350 ml losses equal in outlets with and without competitor coolers; cooler uplift disappears in replication; switching accounts cite price or taste | mixed | open | Determines whether chilled availability or communications and price should lead the 2027 plan | Phase 1 rollout with matched controls; add outlet-level check of competitor cooler presence |  |
| HYP-B02 | hypothesis | Fizzi comes to mind less often than Bora Cola for a cold drink on the way home | Lower situational retrieval for Fizzi than Bora among commuters | Equal or higher retrieval for Fizzi | untested | open | If true, communications linking Fizzi to the moment should accompany cooler placement | Add a situational retrieval question to the Q4 2026 tracker wave |  |
| HYP-B03 | hypothesis | A premium Fizzi tier at +30% would add incremental margin in 2027 | Premium CSD tier sales growing in target outlets; priced test shows incremental buyers | No premium tier traction; cannibalisation of core | untested | open | Would divert budget and management attention from buyer recovery | Premium tier sell-out analysis before any 2028 test | OPT-B02 |
| ASM-B01 | assumption | Modern trade will reach 25% of category value by 2027 | Audit modern trade share rising several points a year | Audit share flat or falling | untested | refuted | Justified shifting 40% of trade budget to modern trade listings | Check audit trend | OPT-B04 |
| ASM-B02 | assumption | The cooler uplift observed in the Dar es Salaam pilot (about 49%) will be of similar size in other high-footfall Dar es Salaam clusters and in Mwanza | Phase 1 uplift within 15 points of pilot versus matched controls | Phase 1 uplift below 25% | untested | accepted_for_planning | Determines whether the cooler programme pays back | Phase 1 with matched controls, including 30 Mwanza outlets | OPT-B01 |
| ASM-B03 | assumption | Distributor service in Mwanza and Arusha will be restored by the end of Q1 2027 | Numeric distribution back within 3 points of 2025 levels | Distribution still below 45% at end of Q1 2027 | untested | accepted_for_planning | Mwanza cooler placements depend on reliable supply | Monthly audit | OPT-B01 |

## Insights

| ID | Explanation | Observation | Contrast | Mechanism | Tension | Alternatives | Confidence | Status | Implication |
|---|---|---|---|---|---|---|---|---|---|
| INS-B01 | Fizzi's growth problem in Dar es Salaam is not loyalty or price: it is losing the on-the-go moment to whoever has the cold bottle there | Dar es Salaam volume grew only because existing home buyers bought more often, while the brand lost 350 ml buyers | 350 ml versus 1.25 L buyers; cooler versus matched outlets; penetration versus frequency effects | The 350 ml purchase is an immediate, on-the-go decision made at the moment a cold drink is available; where cold Fizzi is absent, buyers take a cold competitor or skip | People want a cold drink the moment they step off the bus; Fizzi is often warm or missing at that moment | 350 ml buyers moved to other categories (water, juice) for reasons unrelated to cold availability; Panel under-records out-of-home purchases, exaggerating the 350 ml buyer loss | medium | defensible | Recruit and win back buyers through chilled availability at high-footfall on-the-go points, backed by communication of the moment, rather than frequency promotions or premiumisation |
| INS-B02 | The modern-trade budget shift rests on a repeated assumption that the only category data contradict | Three annual plans assumed modern trade would reach a quarter of category value; audit share stayed at 14% | Planning assumption versus audit trend | An unsourced planning sentence was carried forward each year and became treated as fact | — | Audit under-covers new modern trade formats | medium | defensible | Do not move 40% of trade budget to modern trade in 2027 |

## Options and decisions

| ID | Title | Status | Recommendation type | Decision state | Mechanism | Assumptions | Non-choices | Reversal triggers |
|---|---|---|---|---|---|---|---|---|
| OPT-B01 | Win the on-the-go cold moment: chilled 350 ml availability at high-footfall clusters with communications of the moment, on a repaired supply base | selected | conditional | proposed_by_analyst | penetration, distribution, volume: Chilled availability converts on-the-go moments into purchases, recovering lost 350 ml buyers; communications strengthen retrieval at those moments | ASM-B02; ASM-B03 | No premium tier launch in 2027; No shift of 40% of trade budget to modern trade; No football sponsorship; No national cooler roll-out before the Phase 1 gate | Phase 1 uplift below 25% versus controls: stop expansion and reassess on-the-go strategy; Situational retrieval research shows Fizzi already leads and uplift is visibility-only: shift spend from communications to placement |
| OPT-B02 | Launch a premium Fizzi tier at +30% | rejected | not_recommended | proposed_by_analyst | price, mix, margin: Higher price per litre from trading up existing buyers |  |  |  |
| OPT-B03 | Drive frequency among existing buyers with 1.25 L family promotions | rejected | not_recommended | proposed_by_analyst | frequency, volume: Promotions increase occasions per buyer |  |  |  |
| OPT-B04 | Continue the 2026 plan: shift 40% of trade budget to modern trade listings | rejected | not_recommended | proposed_by_analyst | distribution: Presence in a channel assumed to be growing | ASM-B01 |  |  |

## Actions

| ID | Decision | Action | Intended change | Owner role | Timing | Resource basis | Metrics | Reversal trigger | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACT-B01 | OPT-B01 | Complete availability repair in Mwanza and Arusha wholesaler-served dukas (continuation of Demo A actions) | Distribution back to 2025 levels | Regional sales manager, Lake and Northern zones | Q4 2026 to Q1 2027 | Within existing trade budget; van-sales cost if triggered | MET-B05 | Distribution below 45% at end of Q1 2027: change distributor | in_progress |
| ACT-B02 | OPT-B01 | Phase 1: place 150 coolers in Dar es Salaam high-footfall outlets with the highest 350 ml baselines (target near 59 litres a week) and 30 in Mwanza after supply recovers, with 60 matched control outlets | More on-the-go buyers find cold Fizzi at the moment of purchase | Head of trade marketing | Q1-Q2 2027 | TZS 288 million installed for 180 coolers plus TZS 45 million a year maintenance, from the flat budget | MET-B01; MET-B02; MET-B03 | Incremental 350 ml sales below 25 litres a week versus controls or uptime below 90% | planned |
| ACT-B03 | OPT-B01 | Communications linking Fizzi to the cold drink on the way home, concentrated around cooler clusters (outdoor at stages, radio in drive time); brief written after the Q4 2026 retrieval read | Fizzi comes to mind for the on-the-go cold moment | Marketing director | Q2-Q4 2027 | Reallocation of part of national media weight; amount set after the retrieval read | MET-B01; MET-B04; MET-B07 | No retrieval gain in cooler clusters versus non-cooler clusters by Q4 2027 | planned |
| ACT-B04 | OPT-B01 | Add a situational retrieval question (brand that comes to mind for a cold drink on the way home) to the Q4 2026 tracker wave, with a commuter boost sample | Baseline for HYP-B02 | Insights manager | Q4 2026 | Existing tracker budget plus boost sample cost (to be quoted) | MET-B04 | Not applicable (measurement action) | planned |
| ACT-B05 | OPT-B01 | Keep modern trade investment at 2026 levels; review audit share every six months instead of moving 40% of trade budget | Budget not moved on an unsupported assumption | Commercial director | 2027 | No incremental cost | MET-B06 | Modern trade share up 2 points or more in two consecutive half-years: revisit allocation | planned |

## Metrics

| ID | Definition | Level | Leading/lagging | Baseline | Target rationale | Source | Cadence | Decision rule |
|---|---|---|---|---|---|---|---|---|
| MET-B01 | Fizzi household penetration, 52-week panel, Dar es Salaam and Mwanza | business_outcome | lagging | 52 weeks to June 2026: Dar es Salaam 34%, Mwanza 30% | Stop the decline in 2027 (Dar es Salaam at least 34%); stretch 35% if Phase 2 proceeds; Mwanza recovery depends on supply repair | Household panel | Quarterly (rolling 52 weeks) | Penetration still falling at 52 weeks to December 2027 despite placements: reassess route |
| MET-B02 | 350 ml litres per outlet per week, Phase 1 cooler outlets versus matched controls, relative to pre-period | behavioural_response | leading | Pre-period levels measured per outlet before installation | At least 25 incremental litres a week to proceed to Phase 2 (break-even analysis in analysis/cooler_economics.md) | Distributor outlet sales and field audits | Monthly | Below 25 litres a week at gate: stop expansion |
| MET-B03 | Cooler uptime: share of visits where the cooler is working and stocked with Fizzi | operational | leading | unknown: not measured in pilot | At least 90% to protect payback | Field audit visits | Monthly | Below 90% for two months: fix maintenance before adding coolers |
| MET-B04 | Share of commuters naming Fizzi for a cold drink on the way home (situational retrieval), cooler clusters versus other areas | brand_effect | lagging | unknown: first measured in the Q4 2026 wave | Set after baseline; test for a gain in cooler clusters versus other areas | Brand tracker with commuter boost | Half-yearly | No difference by Q4 2027: stop cluster communications |
| MET-B05 | Numeric distribution in wholesaler-served dukas, Mwanza and Arusha | operational | leading | H1 2026: Mwanza 37%, Arusha 38% | Within 3 points of H1 2025 levels (58% and 55%) by end of Q1 2027 | Monthly field audit | Monthly | Below 45% at end of Q1 2027: change distributor |
| MET-B06 | Modern trade share of urban category value (audit) | business_outcome | lagging | 14% (Q2 2026) | Monitoring metric, no target | Retail audit | Semi-annual | Up 2 points or more in two consecutive half-years: revisit trade allocation |
| MET-B07 | Reach of on-the-go communications among commuters in cooler clusters | exposure_output | leading | unknown: campaign not yet run | Delivery check only; not a success measure | Media delivery reports | Monthly during flight | Under-delivery: correct placement; never used alone to judge success |

## Red-team defects

| ID | Claim/section | Gate | Verdict | Defect | Evidence | Consequence | Fix | Retest | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEF-B01 | Consumer mechanism for 350 ml buyer loss (INS-B01) | customer_relevance | CONCERN | Mechanism rests partly on ten interviews at three locations | Panel and pilot data support the pattern; interviews explain it but cannot size it | The share of buyer loss due to cold availability could be smaller than implied | Keep recommendation conditional; add situational retrieval measurement and Phase 1 controls | Phase 1 gate and Q4 2026 tracker results | bounded_provisional |
| DEF-B02 | Cooler economics (CLM-B05, OPT-B01) | commercial_mechanism | CONCERN | At pilot outlet baselines the payback is about 3.1 years, longer than a typical two-year hurdle | Break-even calculation in analysis/cooler_economics.md; outlet baseline distribution unknown | A broad roll-out could destroy value | Target high-baseline outlets; gate expansion on measured uplift; obtain outlet sales ranking | Outlet ranking shows enough outlets near 59 litres a week and Phase 1 uplift meets the gate | bounded_provisional |
| DEF-B03 | Competitive response to Fizzi cooler placements | competitive_response | CONCERN | Competitor response (exclusivity deals, price moves) not assessed; competitor cooler count is an estimate | Only supervisor estimates (CLM-B10) | Placements could be blocked or uplift eroded | Record competitor cooler presence in Phase 1 outlet audits; prepare a response plan for exclusivity demands | Phase 1 audit data on competitor presence | open |
| DEF-B04 | First draft proposed a 250 ml pack launch citing the Nairobi on-the-go study | local_validity | FAIL | Kenyan survey used as evidence for Tanzanian pack demand | CLM-B11 is a regional proxy; no Tanzanian 250 ml evidence | A pack launch could be committed on evidence that has not been shown to transfer | Remove from the recommendation; record as an open question for a 2028 pack test | Tanzanian pack-size evidence obtained | repaired |

## Change log

| ID | Date | Record | Field | Previous | New | Reason | Flagged |
|---|---|---|---|---|---|---|---|
| CHG-001 | 2026-09-17 | ASM-B01 | status | accepted_for_planning | refuted | Audit shows modern trade share flat at 14% (CLM-B09); assumption was one repeated planning statement (CLM-B08) | OPT-B04 |

## Gate verdicts

| Gate | Verdict | Reason | Defects |
|---|---|---|---|
| problem_framing | PASS | Decision, baseline and constraints explicit; growth task framed as buyer recovery |  |
| evidence | PASS | Load-bearing claims trace to panel, pilot and audit data with limits stated; planning assertion recognised as one lineage |  |
| logic_causality | CONCERN | Pilot is matched rather than randomised; mechanism conclusions bounded | DEF-B01 |
| insight | PASS | Consumer and channel insights with contrasts, mechanisms and alternatives; tension used only where interviews evidence it |  |
| meaningful_choice | PASS | Four routes including status quo; explicit non-choices |  |
| commercial_mechanism | CONCERN | Payback marginal at pilot baselines; gated | DEF-B02 |
| customer_relevance | CONCERN | Small qualitative base | DEF-B01 |
| competitive_response | CONCERN | Competitor response not assessed | DEF-B03 |
| brand_credibility | PASS | Recommendation relies on availability and situational relevance, not unproven brand claims |  |
| local_validity | PASS | Kenyan proxy removed from support after first-draft FAIL (DEF-B04 repaired); CPI used only as context | DEF-B04 |
| feasibility | CONCERN | Number of high-baseline outlets unknown; cooler uptime unmeasured | DEF-B02 |
| measurement | PASS | Chain from exposure to penetration with controls and decision rules |  |
| clarity | PASS | Governing thought and storyline validated against records |  |
