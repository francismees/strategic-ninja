# Analytics

Use this module whenever data is supplied or an analytical claim is made. It covers data checks, the runnable decomposition recipes, recursive interrogation, statistical method choice and how to report findings. Evidence terms follow [evidence-model.md](evidence-model.md).

## Contents
1. Principles
2. Before any analysis: the data contract
3. Runnable recipes (`scripts/commercial_analysis.py`)
4. Decomposition conventions
5. Recursive interrogation
6. Descriptive, predictive and causal claims
7. Method selection for advanced questions
8. Reporting an analytical finding
9. Charts
10. When computation is unavailable

## 1. Principles

- The point is a strategically meaningful driver, not a display of technique.
- Use execution tools for non-trivial calculations. Use established libraries (pandas, statsmodels, SciPy, scikit-learn, DuckDB) when they are available and the question needs them; do not reimplement them.
- Prefer the simplest defensible analysis. Do not run many cuts or correlations until one tells an attractive story; label exploratory findings and account for small bases and multiple comparisons.
- Never infer an unobserved dimension. Sales totals alone cannot establish penetration, frequency, retention or motivations.
- Save the inputs, commands and outputs needed to reproduce every computed finding.

## 2. Before any analysis: the data contract

Establish and write down:

| Check | Questions |
|---|---|
| Grain and keys | What does one row represent? Which columns uniquely identify it? Duplicates? |
| Units | Units, cases, litres, kg, packs? Did pack sizes or unit definitions change? |
| Currency and basis | Which currency? Gross or net? Before or after returns, discounts, promotions, tax? Nominal or real? |
| Period | Calendar, fiscal, 52 vs 53 weeks, partial periods? Same length? |
| Population / denominator | Of what is this a share or rate? Eligible population, market definition, panel universe? |
| Coverage | Which outlets, regions, channels, customers are included or missing? |
| Missingness | Which values are missing and why? Unknown is never zero. |
| Definitions | Sell-in vs sell-out; revenue share vs volume share; reported vs like-for-like; subscriptions vs people |
| Joins | Do keys match? Would a join fan out or drop rows? |
| Changes | Reclassification, new/discontinued SKUs, distribution changes, price list changes, exchange-rate movements |

Run `profile` first when a file arrives, and `join-check` before combining tables. Never silently drop rows or force incompatible datasets together. If comparability fails, say what is not comparable and what could be compared instead.

## 3. Runnable recipes

All recipes are in `scripts/commercial_analysis.py` (Python 3.8+ standard library). Each validates its inputs, fails with a named error code on invalid or non-comparable data, reconciles components to the observed total within a declared tolerance, and records provenance (file hash, arguments, version, timestamp). Output is JSON by default; `--format md` gives a readable summary.

| Recipe | Question | Required inputs | Key failure codes |
|---|---|---|---|
| `profile` | What is in this file? Duplicates, missing values, unit changes? | CSV; optional `--grain`, `--key-col`, `--unit-col`, `--period-col` | (reports problems as warnings) |
| `pvm` | Did revenue change through price, volume, mix, new or discontinued items? | Long CSV: period, item key, quantity, revenue and/or price; optional unit, currency, dims, period length | `MISSING_VALUES`, `DUPLICATE_GRAIN`, `UNIT_CHANGE`, `MIXED_UNITS`, `MIXED_CURRENCY`, `PERIOD_LENGTH_MISMATCH`, `PRICE_REVENUE_MISMATCH`, `ZERO_QUANTITY_WITH_REVENUE`, `AMBIGUOUS_NUMBER_FORMAT` |
| `buyers` | Did volume change through more buyers (penetration), more occasions per buyer, or more units per occasion? | One row per period (optionally per segment): buyers, occasions, units (counts form) or buyers, frequency, units per occasion, volume (rates form); a time window; optional eligible population | `WINDOW_UNDEFINED`, `WINDOW_MISMATCH`, `IDENTITY_MISMATCH`, `BUYERS_EXCEED_POPULATION`, `OCCASIONS_BELOW_BUYERS`, `ZERO_BASE_NOT_DECOMPOSABLE` |
| `contribution` | Which segments, channels, regions, SKUs or brands contributed to change? Did share move? | Period, group, value; optional unit, measure, market definition, declared market total | `MIXED_UNITS`, `MIXED_MEASURES`, `DEFINITION_CHANGED`, `SHARE_EXCEEDS_TOTAL`, `INCONSISTENT_DENOMINATOR` |
| `join-check` | Is it safe to join these tables? | Two CSVs and key columns | `JOIN_FANOUT`, `JOIN_INCOMPLETE` |

Example commands (run from the skill directory, adapt column names):

```bash
python3 scripts/commercial_analysis.py profile --input sales.csv --grain period,sku --key-col sku --unit-col unit --period-col period
python3 scripts/commercial_analysis.py pvm --input sales.csv --key sku --period-col period --base 2025 --current 2026 \
  --quantity-col units --revenue-col net_revenue --unit-col unit --currency-col currency --revenue-basis net --format md
python3 scripts/commercial_analysis.py buyers --input panel.csv --period-col year --base 2025 --current 2026 \
  --buyers-col buyers --occasions-col occasions --units-col units --population-col households --window-col window_days
python3 scripts/commercial_analysis.py contribution --input channels.csv --period-col year --base 2025 --current 2026 \
  --group-col channel --value-col value --unit-col unit --measure-col measure --complete-market
```

Deterministic fixtures with independently derived expected results are in `evals/fixtures/analytics/` and run with `python3 scripts/run_fixtures.py`.

## 4. Decomposition conventions

### Price-volume-mix (`pvm`)

An *item* is the combination of `--dims` and `--key` (e.g. region × SKU). Items are classified as continuing (quantity > 0 in both periods), new (zero or absent base) or discontinued (zero or absent current).

For continuing items, with base average price P̄₀ = base revenue ÷ base quantity:

- **Price effect** = Σ (p₁ − p₀) × q₁ (interaction allocated to price; default), or Σ (p₁ − p₀) × q₀ with the interaction Σ (p₁ − p₀)(q₁ − q₀) reported separately (`--interaction separate`).
- **Volume effect** = (Q₁ − Q₀) × P̄₀.
- **Mix effect** = Σ q₁ × p₀ − Q₁ × P̄₀.
- **New items** = current revenue of new items; **discontinued items** = minus base revenue of discontinued items.

Components reconcile exactly to the revenue change. Worked example: 100 units at 10 becoming 90 units at 12 → revenue 1,000 → 1,080 (+80): price +180, volume −100, mix 0. Revenue grew because price rose while volume fell 10%; that is price-led growth with a volume warning, not a healthy growth signal by itself.

Notes:
- Mix depends on granularity. A different `--dims` choice changes the price/mix split, not the total.
- Volume and mix require one common unit. Convert pack sizes to a common volume unit first.
- Realised price (revenue ÷ quantity) includes promotions and discounts if revenue is net of them. To separate promotion from base price, you need promoted and non-promoted volume.
- Growth rates are not computed for zero bases; new items are reported in currency, not as infinite growth.
- For margin, run the same bridge on gross profit per unit or pair revenue PVM with a cost bridge; revenue growth can dilute margin.

### Buyers × frequency × units (`buyers`)

Identity: volume = eligible population × penetration × occasions per buyer × units per occasion (or buyers × occasions per buyer × units per occasion without a population). Attribution uses the Shapley method: each factor's effect is its average marginal contribution over all orderings, which is exact and does not depend on the order chosen.

Requirements: a defined eligible population (for penetration), the same time window in both periods (52-week buyers are not comparable with 12-week buyers), unique buyer counts, and consistent sources. Panel and survey estimates carry sampling error that the identity does not show.

### Contribution and share (`contribution`)

- Contribution to total growth (pp) = group change ÷ base-period denominator × 100.
- Share of total change = group change ÷ total change (undefined when total change is zero).
- Share change (pp) = current share − base share, using the same denominator definition in both periods.
- A brand can grow in absolute terms and lose share when the market grows faster; the recipe flags this with `--focus-group`.
- If the groups do not cover the whole market, shares are shares of the supplied set. Declare `--market-total-col` or `--complete-market`.

## 5. Recursive interrogation

Interrogate an important aggregate only as far as the data and the decision justify. Useful questions, in roughly this order:

1. Is the change real? (definitions, coverage, period length, reclassification, one-offs)
2. Price or volume? (and mix, new and discontinued items)
3. Which customers, SKUs, channels, regions or occasions?
4. Distribution or rate of sale? (numeric/weighted distribution vs sales per stocking outlet)
5. Acquisition or repeat? Penetration or frequency? (requires buyer-level data)
6. Promotion or base?
7. Profitable or margin-diluting?
8. Sustained or one-off?
9. Compared with which baseline: last year, plan, category, competitor, control group?

Stop when the next split would not change the decision or the data cannot answer it. State the next question the data cannot answer and what data would.

## 6. Descriptive, predictive and causal claims

| Claim type | Example | What it needs |
|---|---|---|
| Descriptive | "Volume fell 6%, concentrated in Mwanza wholesale." | Correct data and definitions |
| Predictive | "Outlets with coolers are likely to sell more next quarter." | A model validated out of sample; no causal claim |
| Causal | "The campaign increased sales by 4%." | A design that rules out plausible alternatives |

- A media–sales correlation does not establish incremental ROI. Seasonality, distribution, pricing, competitor activity and reverse causality (spending more when sales are expected to be high) can all produce it.
- A competitor launch coinciding with decline suggests a hypothesis to test (where did we lose volume, and did they gain it there?).
- A reconciled bridge is necessary arithmetic validation, not causal proof.
- Causal designs, in rough order of strength: randomised experiment (e.g. geo or outlet randomisation); matched control regions or outlets with difference-in-differences (needs parallel pre-trends); interrupted time series with a clear break and no concurrent changes; regression with controls (weakest; state what could still confound). State the identification assumption and its main threats.

## 7. Method selection for advanced questions

These methods need not have custom scripts. Use established tools, explain assumptions and prefer the simplest defensible approach.

| Question | Consider | Watch for |
|---|---|---|
| Survey estimates for a population | Weighting to known population margins; report weighted bases and design effect | Small subgroup bases; weighting cannot fix missing groups in the frame |
| Is a difference between groups real? | Confidence intervals for proportions/means; effect sizes alongside tests; chi-square/Fisher for categorical | Many comparisons (adjust or treat as exploratory); statistical vs commercial significance |
| Retention and churn | Cohort tables by acquisition period; survival curves; revenue retention vs logo retention | Mixing cohorts of different ages; changing definitions of "active" |
| Segmentation | Start from behaviours or needs that change the decision; clustering only if it adds; test stability (re-run on subsamples, different seeds, time periods); check size, reachability, distinctiveness in behaviour and commercial value | Unstable clusters named as durable audiences; demographic labels treated as explanations |
| Trends and forecasts | Plot first; decompose trend and seasonality; look for structural breaks; hold out recent periods; use ranges | Over-fitted models; point forecasts over long horizons |
| Drivers of an outcome in a survey | Regression with care about correlated predictors; stated vs derived importance | Treating driver models as causal |
| Price response | Historical price variation with controls; conjoint or choice experiments designed before fieldwork; in-market price tests | Stated willingness to pay overstates; elasticities from promotions differ from base price changes |
| Did an intervention work? | Experiment or quasi-experiment (section 6) | Declaring success from exposure metrics |

When clusters or segments are offered: reject, qualify or retest unstable segments rather than naming them as durable audiences.

## 8. Reporting an analytical finding

Every substantive analytical output states:

1. **Finding** — what the data show, with numbers, units, base and period.
2. **Method and scope** — recipe or method, convention, coverage and exclusions.
3. **Important uncertainty** — data limitations, sampling error, comparability issues.
4. **Plausible interpretations** — at least the leading explanation and a credible alternative.
5. **Strategic consequence** — what this changes in the diagnosis or choice.
6. **Next decision or test** — what to do or learn next.

Record computed findings as `computed` claims with the command in `basis.calculation` and the input source IDs.

## 9. Charts

Use a chart to answer a specific question. Show units, bases, periods and sources on the chart. Prefer bridges (waterfalls) for decompositions, indexed lines for trends, and simple bars for comparisons. Avoid dual axes and 3D effects. A chart without a question is decoration.

## 10. When computation is unavailable

Say so. For small cases, show the calculation step by step so the user can check it. For larger data, give the exact recipe or command, the input format required and the checks to run. Never report numbers as computed when they were not.
