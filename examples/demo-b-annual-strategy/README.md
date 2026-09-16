# Demo B: building an annual strategy from mixed evidence

> **Synthetic demonstration.** Fizzi Beverages, competitors, data, respondents and quotations are fictional. The NBS CPI figure is real and verified (see `markets/tanzania-observations.json`).

**Request:** "Build the 2027 brand and marketing plan for Fizzi Cola. Budget is flat at TZS 3.2bn. Use what we have."

**Workflow:** [../../workflows/annual-strategy.md](../../workflows/annual-strategy.md) at standard depth, reusing the diagnosis from [Demo A](../demo-a-diagnosis/README.md) after checking it had no open review flags.

## Mixed evidence supplied

| File | Evidence type | Notable limitation |
|---|---|---|
| [data/panel_region.csv](data/panel_region.csv) | Household panel by region (buyers, occasions, litres) | Out-of-home purchases under-recorded |
| [data/panel_pack_dar.csv](data/panel_pack_dar.csv) | Household panel by pack, Dar es Salaam | Same |
| [data/cooler_pilot.csv](data/cooler_pilot.csv) | Matched cooler pilot | Small, one city, not randomised |
| [data/interviews_excerpt.md](data/interviews_excerpt.md) | Ten intercept interviews in Kiswahili with glosses | Explains mechanisms, not prevalence |
| [data/tracker_2026h1.md](data/tracker_2026h1.md) | Brand tracker | No situational retrieval measure |
| [data/market_and_plan_notes.md](data/market_and_plan_notes.md) | Last plan's assumption, retail audit, competitor estimates, Nairobi study, budget and cost quotes, NBS CPI context | Mixed quality by item; Nairobi study is a regional proxy |

## Outputs

| File | What it shows |
|---|---|
| [strategy-2027.md](strategy-2027.md) | The plan: decision, diagnosis, growth task, options, choices and non-choices, actions, economics, risks, measurement, decisions needed |
| [outline.json](outline.json) | Renderer-neutral deck storyline, validated against the records |
| [records.json](records.json) / [records.md](records.md) | Sources, claims, hypotheses and assumptions, insights, options, actions, metrics, defects, gate verdicts, change log |
| [analysis/buyers_by_region.json](analysis/buyers_by_region.json), [analysis/buyers_by_pack_dar.json](analysis/buyers_by_pack_dar.json) | Penetration × frequency × units decompositions (Shapley attribution, reconciled) |
| [analysis/cooler_economics.md](analysis/cooler_economics.md) | Break-even and payback calculation |

## What the demo shows

- Reuse of prior valid work (Demo A) instead of restarting.
- A growth diagnosis that separates penetration from frequency and finds the buyer loss hidden by volume growth.
- A consumer insight with an evidenced tension, and a separate channel insight with no tension.
- **Memory discipline:** a planning assumption repeated across three annual plans was treated as one unsupported lineage. It was then refuted against audit data using `scripts/records.py impact --apply`. That flagged the dependent option (OPT-B04) for review and logged the change (CHG-001). The flag was resolved after review.
- Four genuinely different routes, explicit non-choices, and a conditional recommendation with gates.
- Economics as break-even logic rather than invented forecasts.
- A repaired FAIL: a Kenyan proxy was removed from the recommendation, and the removal is recorded as DEF-B04.
- A storyline that keeps uncertainty on the slides it affects. The outline validator confirms it does not state the recommendation more strongly than the records.

## Reproduce

```bash
python3 scripts/commercial_analysis.py buyers --input examples/demo-b-annual-strategy/data/panel_pack_dar.csv --period-col period \
  --base 52w_to_Jun2025 --current 52w_to_Jun2026 --buyers-col buyers --occasions-col occasions --units-col bottles \
  --population-col households --window-col window --segment-col pack --format md
python3 scripts/records.py validate --records examples/demo-b-annual-strategy/records.json
python3 scripts/records.py outline --outline examples/demo-b-annual-strategy/outline.json --records examples/demo-b-annual-strategy/records.json
```

The plan and records were written by the skill author following the workflow. Behavioural evaluation of the skill against a no-skill baseline is reported separately in `evals/results/`.
