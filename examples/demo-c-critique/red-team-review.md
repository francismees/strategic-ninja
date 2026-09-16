# Red-team review: Pesalo 2027 Growth Strategy

> **Synthetic demonstration.** Pesalo and its data are fictional; TCRA and World Bank figures are real and verified. This review shows the output of [Workflow C](../../workflows/critique-and-improve.md) at standard depth ("red-team this before the board").

**Reviewed:** [data/original-strategy-deck.md](data/original-strategy-deck.md) (12 slides and an appendix)
**Review type:** self-review against [references/red-team.md](../../references/red-team.md), with evidence files opened; not an independent agent
**Evidence opened:** deck appendix, [weekly sign-ups](data/weekly_signups_q2q3.csv), [review sample](data/app_review_sample.md), and the TCRA and World Bank observations in `markets/tanzania-observations.json`
**Could not check:** the Nairobi report cited on slide 5 (not supplied)

## Verdict

**Not presentable as validated.** The deck asks for TZS 2.5 billion to acquire users, but its own appendix shows the business losing most new users within a month and failing nearly one in five cash-outs. Several load-bearing claims fail:
- a misread market size;
- invented consumer psychology;
- a Kenyan proxy used as proof;
- a confounded radio claim presented as ROI;
- vanity KPIs.

One element is sound and should be kept: fixing agent float.

## What is strong

- **Slide 10 is right.** A measured operational problem (18% cash-out failure) is tied to a specific fix, a float-rebalancing partner. Competitors could do the same, but that is not a reason to reject it: it addresses a real constraint.
- The appendix reports honest operating data, which made this critique possible.
- The ambition to grow young savers is a legitimate objective, even though the deck does not yet show how to achieve it.

## Material defects (most consequential first)

| # | Slide | Gate | Defect | Evidence | Consequence | Required fix |
|---|---|---|---|---|---|---|
| 1 | Overall | Evidence | Strategy ignores the deck's own retention and reliability data | 15% of registered accounts active; 22% 30-day retention; 18% cash-out failures | TZS 2.5bn spent filling a leaking bucket | Rebuild around reliability and retention; make acquisition conditional |
| 2 | 2 | Local validity | "117 million mobile users = 117 million potential customers" | TCRA counts about 117.0m **subscriptions** (SIMs active in 90 days, including machine-to-machine SIMs). The population of all ages is about 70.5m (World Bank 2025) | Market size overstated many times over | Size the market from people-based survey data for adults with mobile money access in target areas |
| 3 | 9 | Logic / causality | "Radio ROI is proven: sign-ups 40% higher in radio weeks" | Five of eight radio weeks were salary weeks. Within salary and non-salary weeks, the difference is 9% and 5% on very few weeks ([analysis](analysis/signups_stratified.md)) | Media spend justified by timing, not radio | Call radio unproven; run a regional holdout test |
| 4 | 8 | Problem framing | Viral TikTok challenge treated as the strategy | No evidence awareness or sign-ups are the constraint | Downloads that churn | Hold acquisition campaigns until retention improves; define the communications task afterwards |
| 5 | 7 | Commercial mechanism | Pesalo Gold: 100,000 subscribers at TZS 5,000 a month | No willingness-to-pay evidence. The target is nearly half of current monthly active users | Revenue and budget overstated | Run a priced test with active savers before any launch decision |
| 6 | 4 | Customer relevance / insight | "Gen Z crave instant gratification and hate banks" | No research. Reviews point to withdrawal failures, not a wish for gamification | Product and campaign built on an invented motive | Remove; test motives through interviews with active and lapsed savers |
| 7 | 5 | Local validity | Kenyan adoption "proves" Tanzania will follow | Report not supplied; Kenyan scope; no Tanzanian evidence | Adoption forecast unfounded | Remove as proof; keep as a hypothesis with a local validation step |
| 8 | 3 | Meaningful choice | SWOT presented as the strategy | "Leverage strengths to capture opportunities" excludes nothing | No basis for allocating budget | State the diagnosis, the guiding choice and the non-choices |
| 9 | 11 | Measurement | KPIs are awareness, followers and downloads | No retention, active savers or unit economics | Success declared while users leave | Measure cash-out success, cohort retention, active savers, and cost per retained saver |
| 10 | 6 | Brand credibility (CONCERN) | "Smart savings for smart people" | Fails the competitor-substitution test; no proof point | No reason to choose or trust Pesalo | Defer until reliability can be promised with proof, then test a proposition |

Full defect records with retest conditions: [records.json](records.json) (DEF-C01 to DEF-C10), readable in [records.md](records.md).

## Gate verdicts

| Gate | Verdict | Reason |
|---|---|---|
| Problem framing | FAIL | Virality and Gen Z ambition stand in for a diagnosis |
| Evidence | FAIL | Key claims unsourced or misread; appendix contradicts the strategy |
| Logic / causality | FAIL | Confounded radio association presented as ROI |
| Insight | FAIL | Stereotype presented as insight |
| Meaningful choice | FAIL | SWOT instead of choice; no non-choices |
| Commercial mechanism | FAIL | No unit economics; unsupported subscription target |
| Customer relevance | FAIL | Invented psychology |
| Competitive response | NOT TESTED | No competitor information in the deck |
| Brand credibility | CONCERN | Generic positioning |
| Local validity | FAIL | Subscriptions read as people; Kenyan proxy used as proof |
| Feasibility | PASS | The float-partner action is feasible and addresses a measured problem |
| Measurement | FAIL | Vanity metrics only |
| Clarity | CONCERN | Clear slides arguing for the wrong problem |

## What the structural validator caught, and what it could not

I converted the deck into an outline ([analysis/original-outline.json](analysis/original-outline.json)) and ran `scripts/records.py outline` ([result](analysis/original-outline-check.json)). It flagged six structural problems:
- diagnosis and measurement sections with no evidence;
- three sections resting on uncertain evidence without stating uncertainty;
- a "supported" storyline built on an option recorded as not recommended.

It did **not** flag the market-size error on slide 2. That slide cites a real, verified record of what the deck says, so it is structurally valid. Only reading it against the TCRA definitions shows it is wrong. Semantic defects need judgement; a validator pass is not a quality pass.

## Repair

The repaired storyline is in [improved-storyline.md](improved-storyline.md), with its outline in [improved-outline.json](improved-outline.json) (validated: [check](analysis/improved-outline-check.json)). It keeps the float fix and leads with the retention diagnosis. Acquisition and Gold are held behind evidence gates. Uncertainty stays on the slides it affects. One repair pass was used.

**Remaining uncertainty:**
- Failed cash-outs may not be the main driver of churn; a three-week cohort analysis will tell.
- The float partner's cost is not yet quoted.
- Positioning stays open until reliability can be promised credibly.
- Passing these gates would still not prove the plan will work.
