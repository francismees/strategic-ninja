# Demo A: diagnosing an ambiguous, solution-shaped problem

> **Synthetic demonstration.** Fizzi Beverages and all data are fictional. Any resemblance to real companies is coincidental.

**Brief (from [data/media_and_trade_notes.md](data/media_and_trade_notes.md)):** "Sales are falling because our advertising is weak. Please prepare an agency brief for a new campaign by next month."

**Workflow:** [../../workflows/diagnose.md](../../workflows/diagnose.md) at standard depth.

## Inputs

| File | What it is |
|---|---|
| [data/sales_h1.csv](data/sales_h1.csv) | Company net sales to trade (sell-in) by region, channel and SKU, H1 2025 and H1 2026 |
| [data/volume_by_region_channel.csv](data/volume_by_region_channel.csv) | The same volumes aggregated by region and channel for contribution analysis |
| [data/distribution_audit.csv](data/distribution_audit.csv) | Field audit of numeric distribution and out-of-stocks in duka channels |
| [data/tracker_summary.md](data/tracker_summary.md) | Brand tracker summary |
| [data/media_and_trade_notes.md](data/media_and_trade_notes.md) | Media weight, distributor change, price checks and the CEO brief |

## Outputs

| File | What it shows |
|---|---|
| [diagnosis-memo.md](diagnosis-memo.md) | The deliverable: diagnosis, alternatives checked, recommendation, actions, measures, limits |
| [records.json](records.json) / [records.md](records.md) | Traceable records: sources, claims, hypotheses, insight, options, actions, metrics, defects, gate verdicts |
| [analysis/profile.json](analysis/profile.json) | Data profile (no duplicates at the declared grain) |
| [analysis/pvm_region_channel_sku.json](analysis/pvm_region_channel_sku.json) | Revenue bridge, reconciled |
| [analysis/pvm_sku_only.json](analysis/pvm_sku_only.json) | A deliberately wrong run without region and channel dimensions: the script refuses with `DUPLICATE_GRAIN` instead of silently summing |
| [analysis/volume_contribution.json](analysis/volume_contribution.json) | Contribution of each region-channel group to the volume decline |

## What the demo shows

- The solution-shaped brief is reframed without dismissing the CEO's concern.
- Competing explanations (advertising, distribution, price, category, destocking) are tested with discriminating evidence.
- Arithmetic (where the decline arose) is kept separate from explanation (why).
- The insight is operational, with no invented consumer tension.
- The recommendation includes non-choices, owners, measures, a reversal trigger, and an honest statement of unknown costs.
- Uncertainty (sell-in data, a rough proxy, small survey bases) is visible in the memo, not buried.

## Reproduce

From the skill directory:

```bash
python3 scripts/commercial_analysis.py pvm --input examples/demo-a-diagnosis/data/sales_h1.csv --key sku --dims region,channel \
  --period-col period --base 2025H1 --current 2026H1 --quantity-col volume_000_litres --revenue-col net_revenue_tzs_m \
  --unit-col unit --currency-col currency --period-days-col period_days --revenue-basis net --format md
python3 scripts/commercial_analysis.py contribution --input examples/demo-a-diagnosis/data/volume_by_region_channel.csv \
  --period-col period --base 2025H1 --current 2026H1 --group-col group --value-col value --unit-col unit --measure-col measure --complete-market --format md
python3 scripts/records.py validate --records examples/demo-a-diagnosis/records.json
```

The memo and records were written by the skill author following the workflow. They are not an independent model run; behavioural evaluation results are reported separately in `evals/results/`.
