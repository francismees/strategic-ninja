# Engagement records: ENG-fizzi-h1-2026-diagnosis

> **Synthetic teaching fixture — not real client data.**

- **Decision:** Whether to brief a new advertising campaign for H2 2026 or address a different constraint on Fizzi Cola volume
- **Decision-maker:** CEO, Fizzi Beverages (fictional)
- **Audience:** CEO and leadership team (fictional)
- **Client / brand / category / market:** Fizzi Beverages (fictional) / Fizzi Cola (fictional) / Carbonated soft drinks / Tanzania Mainland: Dar es Salaam, Mwanza, Arusha, Dodoma
- **Horizon:** campaign_quarter
- **Outcome:** Return H2 2026 volume to H2 2025 levels
- **Success metric:** Net sales volume (thousand litres) versus same half of prior year, with outlet-level availability as leading indicator
- **Baseline:** H1 2026 volume 3,021 thousand litres versus 3,315 in H1 2025 (-8.9%)
- **Scope:** Four regions and three channels in the supplied data; competitor sales not available
- **Mode / depth:** diagnose / standard
- **Constraints:** Decision on agency brief requested within one month; H2 media budget not yet approved
- **Unresolved questions:** Are wholesalers destocking in addition to losing outlet availability?; What is the 500 ml price gap outside Dar es Salaam?; What would weekly delivery service cost with Distributor B?

## Sources

| ID | Title | Publisher | Locator | Data period | Geography | Method | Lineage | Limitations |
|---|---|---|---|---|---|---|---|---|
| SRC-A01 | Company net sales to trade by region, channel and SKU, H1 2025 and H1 2026 (synthetic) | Fizzi Beverages finance team (fictional) | All 48 rows | January-June 2025 and January-June 2026 (181 days each) | Dar es Salaam, Mwanza, Arusha, Dodoma | Invoice data: sell-in to modern trade, to dukas by direct van, and to wholesalers serving dukas | original  | Sell-in, not consumer sell-out; wholesaler channel sales can differ from outlet sales if stock levels change; four regions only |
| SRC-A02 | Outlet distribution field audit, H1 2025 and H1 2026 (synthetic) | Fizzi Beverages sales operations (fictional) | All 8 rows | H1 2025 and H1 2026 audit waves | Duka channels in the four regions (modern trade not audited) | Field visits recording whether Fizzi is stocked and out of stock | original  | Outlet selection method not documented; sample estimates; modern trade not covered |
| SRC-A03 | Brand tracker summary, H1 2025 and H1 2026 waves (synthetic) | Research agency (fictional) | Summary table | H1 2025 and H1 2026 waves | Urban Dar es Salaam, Mwanza, Arusha | Face-to-face survey | original  | Urban only; Dodoma not covered; claimed purchase; regional bases around 150 give wide margins of error |
| SRC-A04 | Media and trade notes including CEO brief (synthetic) | Fizzi Beverages marketing and sales (fictional) | Bullets 1-4 | H1 2025 to July 2026 | All four regions; price checks Dar es Salaam only | Internal records and field price checks | original  | Delivery-frequency complaint is a single email; price checks only in Dar es Salaam |

## Claims and findings

| ID | Statement | Type | Basis | Confidence | Market applicability | Verification | Used by |
|---|---|---|---|---|---|---|---|
| CLM-A01 | Net sales fell 6.1% (6,215 to 5,838 TZS million) and volume fell 8.9% (3,315 to 3,021 thousand litres); the bridge is price +166.9, volume -551.2, mix +7.4 TZS million | computed | SRC-A01 | medium — Reproducible and reconciled, but sell-in data | local_verified (Fizzi sales to trade, four regions) | reproduced | HYP-A03 |
| CLM-A02 | Wholesaler-served dukas in Mwanza (-150, -35.7%) and Arusha (-116, -31.4%) account for 90.5% of the 294 thousand-litre volume decline; every other region-channel group moved between -2.1% and +0.6% | computed | SRC-A01 | medium — Reconciled contribution analysis on sell-in data | local_verified (Fizzi sales to trade, four regions) | reproduced | CLM-A04; CLM-A10; HYP-A02; HYP-A04; HYP-A05; INS-A01; OPT-A01 |
| CLM-A03 | Numeric distribution in wholesaler-served dukas fell from 58% to 37% in Mwanza and from 55% to 38% in Arusha, while out-of-stock rates rose from 11% to 34% and 12% to 31%; other duka channels moved by at most one point | observed | SRC-A02 | medium — Direct outlet observation; sample of 120 with undocumented selection | local_verified (Duka channels in the four regions) | verified | CLM-A04; CLM-A10; HYP-A02; INS-A01; OPT-A01 |
| CLM-A04 | Volume per point of numeric distribution in the affected groups was essentially unchanged (Mwanza 7.24 to 7.30; Arusha 6.73 to 6.68 thousand litres per point) | computed | SRC-A01; SRC-A02; CLM-A02; CLM-A03 | low — Proxy combining sell-in volume with a sampled audit measure | local_verified (Wholesaler-served dukas, Mwanza and Arusha) | reproduced | CLM-A10; HYP-A02; INS-A01; OPT-A01 |
| CLM-A05 | Tracker advertising recall fell from 34% to 29% while prompted awareness (91% to 90%) and consideration (52% to 51%) were stable | observed | SRC-A03 | medium — Consistent survey measure; urban only | local_supported (Urban Dar es Salaam, Mwanza, Arusha CSD buyers) | verified | HYP-A01; OPT-A02; OPT-A03 |
| CLM-A06 | Claimed past-4-week purchase of Fizzi fell in Mwanza (37% to 29%) and Arusha (36% to 30%) but was unchanged in Dar es Salaam (40%) | observed | SRC-A03 | low — Regional bases around 150; claimed behaviour | local_supported (Urban Mwanza, Arusha, Dar es Salaam) | verified | CLM-A10; INS-A01 |
| CLM-A07 | TV and radio weight was cut 20% (1,450 to 1,160 GRPs) with the same weekly pattern in every region | observed | SRC-A04 | medium — Internal media plan record; delivery not independently verified | local_verified (All four regions) | verified | CLM-A10; HYP-A01; OPT-A03 |
| CLM-A08 | Wholesaler supply in Mwanza and Arusha moved from Distributor A to Distributor B in January 2026, and one sales email reports fortnightly rather than weekly deliveries | observed | SRC-A04 | low — Distributor change is recorded; delivery frequency rests on one email | local_verified (Mwanza and Arusha wholesaler channel) | verified | CLM-A10; HYP-A02; INS-A01 |
| CLM-A09 | The 500 ml list price rose 5% in January 2026; in 40 Dar es Salaam dukas Fizzi 500 ml moved from 3% to 9% above the main competitor's shelf price | observed | SRC-A04 | medium — Direct price checks, Dar es Salaam only | local_verified (Dar es Salaam dukas) | verified | HYP-A03; OPT-A04 |
| CLM-A10 | The H1 decline is primarily an availability loss in wholesaler-served dukas in Mwanza and Arusha following the distributor change, not a four-region demand or advertising problem | inference | CLM-A02; CLM-A03; CLM-A04; CLM-A06; CLM-A07; CLM-A08 | medium — Several independent first-party signals align; sell-in and small survey bases limit precision | local_verified (Fizzi in the four regions) | unverified |  |

## Hypotheses and assumptions

| ID | Kind | Proposition | Confirming signal | Falsifier | Support | Status | Decision impact | Validation step | Used by |
|---|---|---|---|---|---|---|---|---|---|
| HYP-A01 | hypothesis | Weaker advertising (lower weight or worn-out creative) caused the volume decline | Losses spread across regions and channels in line with the uniform media cut; consideration and claimed purchase falling everywhere | Losses concentrated in specific channels and regions while the media cut was uniform; consideration stable | unsupported | weakened | If true, a communications response would be justified; if false, a new campaign would not recover volume | Compare volume and consideration by region against the uniform GRP cut; later, a regional weight test once availability is restored | OPT-A02 |
| HYP-A02 | hypothesis | The distributor transition reduced outlet availability in wholesaler-served dukas in Mwanza and Arusha, causing most of the decline | Losses concentrated in affected region-channels; distribution and out-of-stocks worsened there; rate of sale where stocked stable | Distribution stable in affected groups, or rate of sale where stocked falling | supported | supported | Prioritise route-to-market repair over a new campaign | Measure wholesaler fill rate and delivery frequency; track recovery against control groups after service fixes | OPT-A01 |
| HYP-A03 | hypothesis | A widening 500 ml price gap to the main competitor explains the small 500 ml declines outside the affected channels | 500 ml declines larger where the gap widened most; 350 ml (no price change) stable | No relationship between gap and 500 ml rate of sale; similar gaps in regions without decline | mixed | open | Could justify a 500 ml price or pack response later | Price checks in all four regions and rate of sale by price-gap band | OPT-A04 |
| HYP-A04 | hypothesis | Wholesaler destocking makes the sell-in decline in the affected groups larger than the outlet-level sales decline | Wholesaler stock cover falling; outlet purchases from wholesalers declining less than sell-in | Wholesaler stock cover stable or rising | mixed | open | Affects the size of expected recovery, not the direction of the recommendation | Stock counts at the top 20 wholesalers in Mwanza and Arusha |  |
| HYP-A05 | hypothesis | A category-wide decline in carbonated soft drinks explains the fall | Declines across all regions and channels; competitor volumes also falling | Most groups flat while a few collapse | unsupported | weakened | Would redirect effort to category or portfolio responses | Obtain category or competitor data if available |  |

## Insights

| ID | Explanation | Observation | Contrast | Mechanism | Tension | Alternatives | Confidence | Status | Implication |
|---|---|---|---|---|---|---|---|---|---|
| INS-A01 | Fizzi is not losing demand; it is losing shelves. The distributor transition removed the product from a fifth of wholesaler-served dukas in Mwanza and Arusha | Volume losses are concentrated in two region-channel groups that lost numeric distribution after a distributor change | Affected groups versus all other region-channel groups; before versus after the January 2026 distributor switch | Less frequent deliveries left wholesalers and then dukas out of stock, so purchases were lost where the product was absent; where stocked, it sold at a similar rate | — | Wholesaler destocking exaggerates the sell-in decline (open, HYP-A04); Unmeasured local competitor activity in Mwanza and Arusha | medium | defensible | A new advertising campaign would not restore volume while the product is missing from these outlets |

## Options and decisions

| ID | Title | Status | Recommendation type | Decision state | Mechanism | Assumptions | Non-choices | Reversal triggers |
|---|---|---|---|---|---|---|---|---|
| OPT-A01 | Restore availability in wholesaler-served dukas in Mwanza and Arusha first; hold the new-campaign brief | selected | supported | proposed_by_analyst | distribution, volume: Restoring numeric distribution to 2025 levels at an unchanged rate of sale would recover most of the lost volume |  | No new campaign creative in H2 2026 until availability recovers; No national price change on the basis of Dar es Salaam price checks alone | Availability restored to within 3 points of 2025 levels but volume still more than 10% below control groups: reopen the communications and category diagnosis |
| OPT-A02 | Brief a new advertising campaign now (CEO proposal) | rejected | not_recommended | proposed_by_analyst | penetration: More memorable advertising increases brand retrieval and purchase |  |  |  |
| OPT-A03 | Decide H2 media weight with a regional weight test after availability recovers | deferred | research_first | proposed_by_analyst | penetration, frequency: If lower weight erodes brand retrieval over time, restoring it should protect future volume |  | No national weight restoration before the test reads | No difference between regions after 12 weeks |
| OPT-A04 | Investigate the 500 ml price gap before any price move | selected | research_first | proposed_by_analyst | price, volume: If the gap suppresses rate of sale, narrowing it could recover volume at a margin cost |  | No price change before the four-region read | Gap unrelated to rate of sale: close the question |

## Actions

| ID | Decision | Action | Intended change | Owner role | Timing | Resource basis | Metrics | Reversal trigger | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACT-A01 | OPT-A01 | Agree a weekly delivery service level (calls and fill-rate target) with Distributor B for Mwanza and Arusha wholesalers | Wholesalers receive weekly deliveries and stop running out | Regional sales manager, Lake and Northern zones | Weeks 1-4 | unknown: service upgrade cost not yet quoted | MET-A01; MET-A02 | No improvement in delivery frequency by week 6: activate ACT-A02 | proposed |
| ACT-A02 | OPT-A01 | Temporary direct van-sales cover for the top duka clusters in Mwanza and Arusha if weekly service is not in place by week 6 | Top-cluster dukas restocked directly | Head of route-to-market | Weeks 6-18 if triggered | Estimate from existing Dar es Salaam van-route costs; to be quantified before launch | MET-A01; MET-A03 | Route contribution negative after eight weeks | proposed |
| ACT-A03 | OPT-A01 | Hold the new-campaign agency brief; keep current creative on air at the approved weight until availability recovers | Media budget not spent against unavailable product | Marketing director | H2 2026, reviewed at end of Q3 | Existing media plan | MET-A03; MET-A04 | Availability recovered but volume still more than 10% below control groups: reopen communications diagnosis | proposed |
| ACT-A04 | OPT-A04 | Run 500 ml price checks in 40 dukas per region and analyse rate of sale by price-gap band | Decision-grade evidence on price position | Insights manager | Weeks 2-8 | Existing field audit team | MET-A05 | Not applicable (learning action) | proposed |

## Metrics

| ID | Definition | Level | Leading/lagging | Baseline | Target rationale | Source | Cadence | Decision rule |
|---|---|---|---|---|---|---|---|---|
| MET-A01 | Numeric distribution and out-of-stock rate in wholesaler-served dukas, Mwanza and Arusha (field audit, 120 outlets each) | operational | leading | H1 2026: Mwanza 37% distribution, 34% out of stock; Arusha 38%, 31% | Return to within 3 points of H1 2025 (58% and 55%) by end of Q4 2026 | Monthly field audit | Monthly | Below 45% by end of Q3: escalate to van-sales cover or distributor change |
| MET-A02 | Distributor B delivery frequency and order fill rate to wholesalers | operational | leading | unknown: not currently measured; one report of fortnightly deliveries | Weekly deliveries; fill-rate target to be agreed in the service level | Distributor delivery logs | Weekly | Weekly delivery not achieved by week 6: trigger ACT-A02 |
| MET-A03 | Volume in affected groups (Mwanza and Arusha wholesaler-served dukas) versus control groups (Dodoma and Dar es Salaam wholesaler-served dukas), indexed to the same half of 2025 | business_outcome | lagging | H1 2026 index: affected groups 66 (524/790); control groups 98 (628/640) | Affected-group index within 5 points of control groups by H1 2027 | Company sales to trade; outlet sell-out if available | Monthly | Availability restored but index gap above 10 points: reopen diagnosis |
| MET-A04 | Tracker consideration, ad recall and claimed past-4-week purchase by region | brand_effect | lagging | H1 2026: consideration 51%, ad recall 29%; claimed purchase Dar es Salaam 40%, Mwanza 29%, Arusha 30% | Consideration stable or rising; claimed purchase in Mwanza and Arusha returning towards 2025 levels as availability recovers | Brand tracker | Half-yearly | Consideration falls in regions with stable availability: prioritise the media weight test (OPT-A03) |
| MET-A05 | 500 ml shelf price gap to main competitor by region and 500 ml rate of sale by gap band | operational | leading | Dar es Salaam +9% (H1 2026); other regions unknown: not yet checked | Not a target metric; decision input | Field price checks and sales data | Once, then quarterly if relevant | Clear rate-of-sale drop above a gap threshold: develop price-pack options; otherwise close |

## Red-team defects

| ID | Claim/section | Gate | Verdict | Defect | Evidence | Consequence | Fix | Retest | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEF-A01 | Diagnosis relies on sell-in volume (CLM-A01, CLM-A02) | evidence | CONCERN | Sell-in can differ from outlet sales when wholesaler stock changes | No sell-out or wholesaler stock data supplied; outlet audit and regional tracker purchase measures point the same way | Size of the demand loss and speed of recovery could be misjudged | Bound the claim; add wholesaler stock counts (HYP-A04) and track outlet-level recovery | Wholesaler stock counts available | bounded_provisional |
| DEF-A02 | Rate of sale where stocked is flat (CLM-A04) | logic_causality | CONCERN | Proxy divides sell-in volume by a sampled distribution measure rather than measuring outlet rate of sale | No outlet-level sales data | Could hide a demand decline among stocked outlets | State as low-confidence proxy; confirm with outlet sell-out from a sample of stocked dukas | Outlet sell-out sample for stocked dukas in affected groups | bounded_provisional |
| DEF-A03 | Action plan economics (OPT-A01) | feasibility | CONCERN | Cost of distributor service upgrade or van routes unknown | No quotes supplied | Payback not yet demonstrated | Obtain quotes before committing beyond week 6; compare with volume at stake | Quotes obtained and compared with contribution at stake | open |

## Gate verdicts

| Gate | Verdict | Reason | Defects |
|---|---|---|---|
| problem_framing | PASS | Solution-shaped brief restated; objective, symptom, suspected cause and proposed solution separated |  |
| evidence | CONCERN | Sell-in data and small regional survey bases; bounded (DEF-A01) | DEF-A01 |
| logic_causality | CONCERN | Decomposition kept separate from causal explanation; rate-of-sale proxy is weak (DEF-A02) | DEF-A02 |
| insight | PASS | Operational insight with contrast, mechanism and alternatives; no invented tension |  |
| meaningful_choice | PASS | Four options including the CEO proposal; explicit non-choices |  |
| commercial_mechanism | PASS | Distribution-to-volume mechanism with volume at stake stated |  |
| customer_relevance | NOT_APPLICABLE | No consumer-motivation claims made; problem is operational |  |
| competitive_response | NOT_TESTED | No competitor data for Mwanza or Arusha |  |
| brand_credibility | NOT_APPLICABLE | No positioning claims |  |
| local_validity | PASS | Claims scoped to regions and channels; price evidence limited to Dar es Salaam and labelled |  |
| feasibility | CONCERN | Service upgrade costs unknown (DEF-A03) | DEF-A03 |
| measurement | PASS | Leading operational measures, controls and decision rules defined |  |
| clarity | PASS | Memo leads with decision and binding constraint |  |
