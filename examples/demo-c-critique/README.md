# Demo C: critiquing and improving an existing strategy

> **Synthetic demonstration.** Pesalo, its deck, data and reviews are fictional. The TCRA subscription and World Bank population figures used to test slide 2 are real and verified (see `markets/tanzania-observations.json`).

**Request:** "Red-team this strategy before it goes to the board, then fix it."

**Workflow:** [../../workflows/critique-and-improve.md](../../workflows/critique-and-improve.md) at standard depth.

## Inputs

| File | What it is |
|---|---|
| [data/original-strategy-deck.md](data/original-strategy-deck.md) | The deck under review: 12 slides and an operating-data appendix |
| [data/weekly_signups_q2q3.csv](data/weekly_signups_q2q3.csv) | Weekly sign-ups with radio and salary-week flags |
| [data/app_review_sample.md](data/app_review_sample.md) | Coded sample of one-star reviews |

## Outputs

| File | What it shows |
|---|---|
| [red-team-review.md](red-team-review.md) | Verdict, strengths, ten defects most consequential first, gate verdicts, validator limits |
| [improved-storyline.md](improved-storyline.md) | Repaired storyline with assertion titles and visible uncertainty |
| [improved-outline.json](improved-outline.json) | Renderer-neutral outline for the repaired deck (validates) |
| [records.json](records.json) / [records.md](records.md) | Sources, claims (including real TCRA and World Bank records), hypotheses, insight, options, actions, metrics, defect records, gate verdicts |
| [analysis/signups_stratified.md](analysis/signups_stratified.md) | Why the radio claim is confounded |
| [analysis/original-outline.json](analysis/original-outline.json) and [analysis/original-outline-check.json](analysis/original-outline-check.json) | The original deck as an outline, and the validator's six structural errors |
| [analysis/improved-outline-check.json](analysis/improved-outline-check.json) | The repaired outline passing structural checks |

## What the demo shows

- A proportionate but complete red-team for a board pre-read, with defects ordered by consequence.
- Calibration: the sound operational action (the float partner) is kept even though a competitor could copy it.
- Each anti-pattern named and repaired at the right layer:
  - subscriptions presented as people;
  - invented psychology;
  - a regional proxy used as proof;
  - correlation presented as ROI;
  - premium without willingness-to-pay evidence;
  - virality treated as the strategy;
  - SWOT treated as the strategy;
  - vanity KPIs.
- The retention constraint hidden in the deck's own appendix becomes the governing thought, stated conditionally with a fast test.
- Honest limits: the structural validator caught six problems but not the market-size error, which needed judgement.

## Reproduce

```bash
python3 scripts/records.py validate --records examples/demo-c-critique/records.json
python3 scripts/records.py outline --outline examples/demo-c-critique/analysis/original-outline.json --records examples/demo-c-critique/records.json
python3 scripts/records.py outline --outline examples/demo-c-critique/improved-outline.json --records examples/demo-c-critique/records.json
```

The review and repaired storyline were written by the skill author following the workflow. Behavioural evaluation against a no-skill baseline is reported separately in `evals/results/`.
