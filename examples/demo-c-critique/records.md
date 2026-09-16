# Engagement records: ENG-pesalo-2027-critique

> **Synthetic teaching fixture — not real client data.**

- **Decision:** Whether the board should approve TZS 2.5 billion for Pesalo's 2027 Gen Z campaign and Pesalo Gold launch, and what to fund instead if not
- **Decision-maker:** Pesalo board (fictional)
- **Audience:** CEO and board (fictional)
- **Client / brand / category / market:** Pesalo (fictional) / Pesalo (fictional mobile savings wallet) / Mobile savings and wallets / Tanzania (national claims in the deck; operating data company-wide)
- **Horizon:** annual
- **Outcome:** Profitable growth in active savers
- **Success metric:** Active savers (monthly active users with at least one deposit) and 90-day retention
- **Baseline:** Q2 2026: 210,000 monthly active users of 1,400,000 registered; 30-day retention of new users 22%
- **Scope:** Critique of the 2027 strategy deck and a repaired storyline
- **Mode / depth:** critique_red_team / standard
- **Constraints:** Board meeting in two weeks; Budget request TZS 2.5 billion
- **Unresolved questions:** Do users whose first cash-out fails churn more than others?; Would target users pay TZS 5,000 a month for Pesalo Gold?; Does radio cause sign-ups once salary timing is controlled?

## Sources

| ID | Title | Publisher | Locator | Data period | Geography | Method | Lineage | Limitations |
|---|---|---|---|---|---|---|---|---|
| SRC-C01 | Pesalo 2027 Growth Strategy deck (synthetic) | Pesalo management (fictional) | Slides 1-12 and Appendix A | Q2 2026 operating data; claims undated | Tanzania | Management presentation | original  | Advocacy document; most claims unsourced |
| SRC-C02 | Pesalo operating data, Q2 2026 (deck Appendix A, synthetic) | Pesalo operations (fictional) | Appendix A | April-June 2026 | All Pesalo users | Platform transaction data | original  | Summary figures only; no cohort breakdown by first cash-out outcome |
| SRC-C03 | Weekly sign-ups with radio and salary-week flags (synthetic) | Pesalo growth team (fictional) | All 26 rows | 26 weeks, Q2-Q3 2026 | National | Platform counts with media calendar flags | original  | Observational; no regional control |
| SRC-C04 | One-star app review sample (synthetic) | Pesalo insights team (fictional) | Theme table | April-June 2026 | App store reviewers | Thematic coding | original  | Reviewers are self-selected and dissatisfied; not representative of all users |
| SRC-C05 | Nairobi Fintech Youth Report 2025 (fictional, as cited on slide 5) | unknown: publisher not named in the deck | Slide 5 citation only; report not supplied | unknown: not stated | Nairobi, Kenya | unknown: not stated | unknown  | Report not supplied; Kenyan evidence; method unknown |
| SRC-TZ-TCRA-2026-Q2 | Communications Sector Performance Report, quarter ending June 2026 | Tanzania Communications Regulatory Authority (TCRA) | p.7-8 glossary (definition of subscription; penetration); p.10 snapshot; p.13 Table 1.1.1; p.14 Tables 1.1.1.1-1.1.1.2; p.35 Table 1.9.1.1 | April-June 2026 (end-June stock figures) | United Republic of Tanzania | Regulatory returns from licensed operators | original  | Counts subscriptions (SIMs used at least once in 90 days), including machine-to-machine SIMs and fixed lines; not unique people. Penetration denominator not stated in the report. |
| SRC-TZ-WB-WDI-POP | World Development Indicators: Population, total (SP.POP.TOTL), Tanzania | World Bank | API record for date 2025; database lastupdated 2026-07-13 | 2025 | United Republic of Tanzania | World Bank estimate compiled from census and projection sources | derived  | Modelled estimate for a non-census year; may differ from NBS projections |

## Claims and findings

| ID | Statement | Type | Basis | Confidence | Market applicability | Verification | Used by |
|---|---|---|---|---|---|---|---|
| CLM-C01 | The deck states that 117 million mobile users in Tanzania equal 117 million potential Pesalo customers | observed | SRC-C01 | high — Directly read from the deck | not_applicable (Content of the deck) | verified | HYP-C03; OPT-C01 |
| CLM-TZ-004 | TCRA reported 116,952,295 telecom subscriptions at end-June 2026 (mobile 116,850,926; fixed 101,369), of which 1,233,467 were machine-to-machine SIMs. | observed | SRC-TZ-TCRA-2026-Q2 | high — Regulator's administrative data for exactly this measure | local_verified (United Republic of Tanzania, telecom subscriptions (not people)) | verified | CLM-TZ-008 |
| CLM-TZ-006 | TCRA defines a subscription as a SIM used at least once for voice, SMS or data in the past 90 days, and reports penetration of 167.0% (telecom) and 89.7% (internet) without stating the population denominator. | observed | SRC-TZ-TCRA-2026-Q2 | high — Definitions and figures read directly from the report | local_verified (TCRA reporting definitions) | verified | CLM-TZ-008 |
| CLM-TZ-007 | The World Bank estimates Tanzania's total population in 2025 at 70,545,865. | observed | SRC-TZ-WB-WDI-POP | medium — Authoritative compiler but a modelled estimate between censuses | local_verified (United Republic of Tanzania, total population) | verified | CLM-TZ-008 |
| CLM-TZ-008 | Telecom subscription counts cannot be read as unique people or audience reach: end-June 2026 subscriptions (about 117.0 million) exceed the estimated 2025 total population (about 70.5 million) of all ages. | inference | CLM-TZ-004; CLM-TZ-006; CLM-TZ-007 | high — Follows arithmetically from two direct measures and the stated definition | local_verified (United Republic of Tanzania) | unverified |  |
| CLM-C02 | Only 15% of registered accounts were active in a 30-day window (210,000 of 1,400,000), and 22% of users who registered in Q2 were retained at 30 days | computed | SRC-C02 | medium — First-party data; retention definition not documented | local_verified (Pesalo users) | reproduced | ASM-C01; HYP-C01; INS-C01; OPT-C02; OPT-C03 |
| CLM-C03 | 18% of cash-out attempts failed in Q2 2026 (468,000 of 2.6 million), attributed by operations to agent float shortages | observed | SRC-C02 | medium — Platform counts; cause attribution by operations not independently checked | local_verified (Pesalo agent network) | verified | HYP-C01; INS-C01; OPT-C02 |
| CLM-C04 | 41 of 120 sampled one-star reviews mention failed withdrawals or agents without cash, the most common theme | observed | SRC-C04 | low — Self-selected dissatisfied reviewers | local_supported (Pesalo reviewers) | verified | HYP-C01; INS-C01; OPT-C02 |
| CLM-C05 | Radio weeks averaged 42% more sign-ups than non-radio weeks, but five of eight radio weeks were salary weeks; within salary and non-salary weeks the differences were 9% and 5% on very few weeks | computed | SRC-C03 | medium — Simple, reproducible; small strata | local_verified (Pesalo sign-ups) | reproduced | HYP-C02 |
| CLM-C06 | The deck cites a Nairobi report that Kenyan youth adopted savings apps rapidly | observed | SRC-C05 | low — Report not supplied; method unknown | regional_proxy (Nairobi youth) | unverified | OPT-C01 |

## Hypotheses and assumptions

| ID | Kind | Proposition | Confirming signal | Falsifier | Support | Status | Decision impact | Validation step | Used by |
|---|---|---|---|---|---|---|---|---|---|
| HYP-C01 | hypothesis | Failed cash-outs, driven by agent float shortages, are a major cause of Pesalo's early churn | 30-day retention markedly lower for users whose first cash-out failed than for those whose first cash-out succeeded | Similar retention regardless of first cash-out outcome | mixed | open | If true, reliability fixes should come before acquisition spend | Cohort analysis of Q2 registrants by first cash-out outcome (first-party data, days not months) | OPT-C02 |
| HYP-C02 | hypothesis | Radio advertising increases sign-ups | Higher sign-ups in radio regions than matched holdout regions in the same weeks | No difference in a regional holdout test | untested | open | Determines whether radio deserves acquisition budget | Regional holdout test once retention is fixed | OPT-C01 |
| HYP-C03 | hypothesis | Young Tanzanians want savings to feel like a game and reject banks | Research with target users showing gamified saving increases saving behaviour | Research showing reliability, fees or access matter more | unsupported | open | Would shape positioning and product | Switching interviews with active and lapsed savers | OPT-C01 |
| ASM-C01 | assumption | 100,000 users will pay TZS 5,000 a month for Pesalo Gold in year one | Priced test conversion consistent with target | Low conversion in a priced test | untested | open | Drives part of the budget request | Priced test with existing active savers | OPT-C01; OPT-C03 |

## Insights

| ID | Explanation | Observation | Contrast | Mechanism | Tension | Alternatives | Confidence | Status | Implication |
|---|---|---|---|---|---|---|---|---|---|
| INS-C01 | Pesalo's growth problem looks like a leaking bucket rather than a shortage of sign-ups | Most new users stop transacting within a month, cash-out failures are frequent, and failed withdrawals dominate one-star reviews | Acquisition ambition in the deck versus retention and reliability in the appendix | Users who cannot withdraw their savings when needed lose trust and stop using the wallet, so acquisition spend buys churn | — | Users sign up for a one-off purpose and never intended to save; Fees or app crashes drive churn more than cash-out failures | low | mechanism_hypothesis | Fund reliability and onboarding before scaled acquisition; measure the churn link first |

## Options and decisions

| ID | Title | Status | Recommendation type | Decision state | Mechanism | Assumptions | Non-choices | Reversal triggers |
|---|---|---|---|---|---|---|---|---|
| OPT-C01 | Deck proposal: viral Gen Z campaign plus Pesalo Gold (TZS 2.5 billion) | rejected | not_recommended | proposed_by_analyst | acquisition, price: More downloads and subscription revenue | ASM-C01; HYP-C02 |  |  |
| OPT-C02 | Fix the leaking bucket first: cash-out reliability and onboarding, measure the churn link, then gated acquisition | selected | conditional | proposed_by_analyst | retention, acquisition, cost: Higher retention raises the value of every acquired user and lowers effective acquisition cost | HYP-C01 | No viral influencer campaign in H1 2027; No Pesalo Gold launch before a priced test; No national radio expansion before a holdout test | No retention difference by first cash-out outcome: re-diagnose (fees, crashes, purpose of sign-up) |
| OPT-C03 | Pesalo Gold subscription | deferred | research_first | proposed_by_analyst | price, margin: Subscription revenue | ASM-C01 |  | Test conversion far below the level needed to cover costs |

## Actions

| ID | Decision | Action | Intended change | Owner role | Timing | Resource basis | Metrics | Reversal trigger | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACT-C01 | OPT-C02 | Sign the float-rebalancing partner for the top 2,000 agents (kept from slide 10) | Fewer failed cash-outs | Head of agent network | Q4 2026 | unknown: partner fee not quoted | MET-C01 | Failure rate not below 8% after three months: change partner or model | proposed |
| ACT-C02 | OPT-C02 | Cohort analysis of Q2-Q3 registrants: 30- and 90-day retention by first cash-out outcome | Evidence on the churn mechanism | Data analytics lead | Within 3 weeks | Internal analyst time | MET-C02 | Not applicable (analysis) | proposed |
| ACT-C03 | OPT-C02 | Redesign onboarding around a first successful deposit and withdrawal (guided first save, nearest reliable agent) | New users complete a successful first cycle | Product lead | Q1 2027 | Product team capacity | MET-C02; MET-C03 | No retention improvement after two monthly cohorts | proposed |
| ACT-C04 | OPT-C02 | Regional holdout test for radio before any national expansion | Causal evidence on radio | Growth marketing manager | Q2 2027 | Part of existing media budget | MET-C04; MET-C05 | No sign-up or active-saver difference between regions | proposed |

## Metrics

| ID | Definition | Level | Leading/lagging | Baseline | Target rationale | Source | Cadence | Decision rule |
|---|---|---|---|---|---|---|---|---|
| MET-C01 | Cash-out success rate at top 2,000 agents and network-wide | operational | leading | 82% network-wide (Q2 2026) | At least 92% within three months; based on eliminating most float-related failures (to be refined once failure causes are broken out) | Transaction logs | Weekly | Below 90% after three months: escalate |
| MET-C02 | 30- and 90-day retention of monthly registrant cohorts, split by first cash-out outcome | behavioural_response | leading | 30-day retention 22% (Q2 2026 registrants); split unknown: not yet analysed | Set after the cohort analysis | Transaction logs | Monthly | Release acquisition budget only when 30-day retention exceeds the agreed threshold |
| MET-C03 | Active savers: monthly active users with at least one deposit | business_outcome | lagging | unknown: deposit-active count not reported (210,000 monthly active users of any transaction) | Set once baseline is extracted | Transaction logs | Monthly | Flat active savers after two quarters: re-diagnose |
| MET-C04 | Sign-ups and 30-day active savers in radio test regions versus holdout regions | behavioural_response | leading | Pre-period levels by region (to be extracted) | Detect a difference large enough to justify cost | Transaction logs by region | Weekly during test | No meaningful difference: do not expand radio |
| MET-C05 | Radio reach in test regions | exposure_output | leading | unknown: test not yet run | Delivery check only | Station logs and media reports | Weekly during test | Under-delivery invalidates the test week |

## Red-team defects

| ID | Claim/section | Gate | Verdict | Defect | Evidence | Consequence | Fix | Retest | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEF-C01 | Slide 2: 117 million mobile users = 117 million potential customers | local_validity | FAIL | Subscriptions are presented as people and as addressable customers | TCRA counts about 117.0 million subscriptions (SIMs active in 90 days, incl. machine-to-machine) against a population of about 70.5 million of all ages (CLM-TZ-004, CLM-TZ-006, CLM-TZ-007) | Market size overstated many times over; targets and budget built on it are unfounded | Size the market with unique adults with mobile money access in target areas, from survey data, and state the scope | Market size built from a people-based source with scope and date | repaired |
| DEF-C02 | Slide 3: SWOT presented as strategy | meaningful_choice | FAIL | A SWOT list replaces diagnosis and choice; 'leverage strengths to capture opportunities' excludes nothing | No diagnosis or trade-offs in the deck | No basis for allocating the budget | State the diagnosis (retention and reliability), the guiding choice and non-choices | Storyline contains a diagnosis, a choice and explicit non-choices | repaired |
| DEF-C03 | Slide 4: Gen Z crave instant gratification and hate banks | customer_relevance | FAIL | Invented psychology and a demographic stereotype used as an insight | No research cited; appendix and reviews point to reliability, not gamification (CLM-C04) | Product and campaign built on an unsupported motive | Remove; replace with a hypothesis to test through switching interviews with active and lapsed savers | Qualitative evidence from target users | repaired |
| DEF-C04 | Slide 5: Kenyan youth adoption proves Tanzania will follow | local_validity | FAIL | Regional proxy presented as proof | Report not supplied; Kenyan scope; no Tanzanian adoption evidence (CLM-C06) | Adoption forecast unfounded | Remove as proof; if relevant, list as a hypothesis with a local validation step | Tanzanian evidence on savings app adoption | repaired |
| DEF-C05 | Slide 6: 'smart savings for smart people' | brand_credibility | CONCERN | Generic positioning that any competitor could use | Competitor substitution test fails; no proof point | No distinctive reason to choose or trust Pesalo | Defer positioning until the reliability promise can be proven; then test a reliability-based proposition | Proposition with proof, tested with target users | bounded_provisional |
| DEF-C06 | Slide 7: Pesalo Gold, 100,000 subscribers at TZS 5,000 a month | commercial_mechanism | FAIL | Premium subscription target without willingness-to-pay evidence; the target is almost half of current monthly active users | No pricing research or test; 210,000 monthly active users (CLM-C02) | Revenue plan and budget request overstated | Priced test with active savers before any launch decision | Test conversion and retention of subscribers | bounded_provisional |
| DEF-C07 | Slide 8: viral TikTok challenge, 10 million views | problem_framing | FAIL | Virality treated as the strategy before the business problem and communications task are established | Appendix shows 22% 30-day retention; no evidence awareness is the constraint | Spend buys downloads that churn | Hold acquisition campaigns until retention improves; define the communications task afterwards | Retention above agreed threshold and a defined communications task | repaired |
| DEF-C08 | Slide 9: radio ROI is proven | logic_causality | FAIL | Correlation presented as causal ROI; radio weeks coincided with salary weeks | Five of eight radio weeks were salary weeks; stratified differences 5-9% on tiny numbers of weeks (CLM-C05) | Media budget justified by a confounded association | State as unproven; run a regional holdout test | Holdout test result | repaired |
| DEF-C09 | Slide 11: KPIs (awareness, followers, downloads) | measurement | FAIL | Exposure and vanity metrics only; no retention, active savers or unit economics | KPI list on slide 11 | Success could be declared while the business loses users | Measure cash-out success, cohort retention, active savers and acquisition cost per retained saver | Measurement plan includes behavioural and business outcomes with decision rules | repaired |
| DEF-C10 | Deck overall: acquisition strategy ignores the appendix | evidence | FAIL | The deck's own data show a retention and reliability constraint that the strategy does not address | 15% of registered accounts active; 22% 30-day retention; 18% cash-out failures (CLM-C02, CLM-C03) | TZS 2.5 billion would be spent filling a leaking bucket | Rebuild around reliability and retention; make acquisition conditional | Storyline leads with retention diagnosis and conditional acquisition | repaired |

## Gate verdicts

| Gate | Verdict | Reason | Defects |
|---|---|---|---|
| problem_framing | FAIL | Virality and Gen Z ambition treated as the strategy; business constraint not diagnosed | DEF-C07; DEF-C10 |
| evidence | FAIL | Key claims unsourced or misread; appendix contradicts strategy | DEF-C10 |
| logic_causality | FAIL | Confounded radio association presented as ROI | DEF-C08 |
| insight | FAIL | Stereotype presented as insight | DEF-C03 |
| meaningful_choice | FAIL | SWOT instead of choice; no non-choices | DEF-C02 |
| commercial_mechanism | FAIL | No unit economics; subscription target unsupported | DEF-C06 |
| customer_relevance | FAIL | Invented psychology | DEF-C03 |
| competitive_response | NOT_TESTED | No competitor data in the deck |  |
| brand_credibility | CONCERN | Generic positioning | DEF-C05 |
| local_validity | FAIL | Subscriptions as people; Kenyan proxy as proof | DEF-C01; DEF-C04 |
| feasibility | PASS | The one operational action (float partner) is feasible and addresses a measured problem |  |
| measurement | FAIL | Vanity metrics only | DEF-C09 |
| clarity | CONCERN | Slides are clear but argue for the wrong problem |  |
