# Workflow A: Diagnose an ambiguous business or marketing problem

Use when the cause of a performance problem is unclear, the brief is solution-shaped ("we need a new campaign"), or leadership disagrees about what is wrong. Demonstration: [../examples/demo-a-diagnosis/](../examples/demo-a-diagnosis/README.md).

Methods: [../references/diagnosis.md](../references/diagnosis.md), [../references/analytics.md](../references/analytics.md), [../references/research.md](../references/research.md), [../references/insight.md](../references/insight.md), [../references/red-team.md](../references/red-team.md). Tanzania: [../markets/tanzania.md](../markets/tanzania.md).

## Entry and exit

- **Enter** at step 1 with a brief; at step 3 if data are already supplied and the frame is clear; at step 5 if analysis exists and needs interpretation.
- **Exit** with a diagnosis labelled *supported*, *leading hypothesis with conditions*, or *unresolved with a discriminating test*, plus the implication for what to do next.
- **Hand over** to [annual-strategy.md](annual-strategy.md), [campaign-strategy.md](campaign-strategy.md) or [positioning-gtm.md](positioning-gtm.md) if the user wants the response built.

## Steps

### 1. Orient (always)
- Read everything supplied first. Note what each file can and cannot show.
- Write the decision frame: decision, decision-maker, outcome, success metric, baseline, horizon, scope, constraints.
- Separate objective, symptom, suspected cause and proposed solution. Restate a solution-shaped brief without the solution.
- Ask at most two or three questions, and only if the answers would change the analysis. Otherwise state assumptions and continue.

*Output (quick)*: two or three sentences framing the real question. *Output (standard/deep)*: [../templates/engagement-frame.md](../templates/engagement-frame.md); start `records.json` if the work will continue.

### 2. Build competing explanations
- Classify candidate problem levels: commercial, market/category, customer, brand, communications, execution.
- Write three to six hypotheses that genuinely compete, including the user's preferred explanation.
- For each: predicted evidence, falsifier, decision consequence, cheapest discriminating check.
- Prioritise by decision impact × uncertainty ÷ cost of learning.

*Output*: hypothesis table (prose for quick work; `hypotheses` records for standard/deep).

### 3. Check the data and decompose
- Profile data files; confirm grain, units, periods, coverage, definitions (sell-in vs sell-out, gross vs net).
- Decompose the outcome: price/volume/mix, channel/region/SKU contribution, buyers × frequency where data exist.
- Follow the largest or most decision-relevant branch one level deeper; stop when the next split would not change the decision.
- Record computed findings with the command used.

*Transition*: if definitions or data quality undermine comparison, say so and either repair (ask for missing data) or bound the analysis.

### 4. Gather discriminating evidence
- Check readily available evidence that separates hypotheses: distribution and out-of-stocks, price position versus competitors, category and competitor trends, brand measures, campaign reach and response, qualitative accounts.
- Search deliberately for evidence against the leading hypothesis.
- For Tanzania: check scope (Mainland/Zanzibar, region, urban/rural, channel) and label proxy evidence.

*Stop* when further accessible evidence would not change the diagnosis at the confidence the decision needs, or when the remaining question needs new primary research.

### 5. Explain
- Move from pattern to mechanism for the leading explanation; state the strongest alternative and why it is weaker.
- Accept operational or commercial explanations without inventing a consumer tension.
- Keep contradictions visible.

### 6. Verify
- Reload [../references/red-team.md](../references/red-team.md). Apply at least: problem framing, evidence, logic/causality, local validity (if relevant), clarity.
- Check the anti-patterns most likely here: solution smuggling, correlation as causation, bridge as cause, invented psychology, national average applied to a segment.
- Repair the failing layer; allow up to two repair passes.

### 7. State the diagnosis and implication
Deliver:
1. **The binding constraint** and its level, in one or two sentences.
2. **Decisive evidence** and why alternatives were ruled out or remain open.
3. **Confidence and what could change it.**
4. **Implication**: what kind of response follows, what does not (e.g. "fix availability before increasing media").
5. **Next step**: either the recommended response direction, or the smallest test that would resolve remaining uncertainty.

For standard/deep work, record defects and gate results; validate records with `python3 scripts/records.py validate`.

## Proportionality

- *Quick* (a chat question): frame, two or three competing explanations, the first two checks to run, provisional view.
- *Standard*: steps 1–7 with key records and a short memo.
- *Deep*: full records, analysis files, independent review if available, and a storyline for leadership.

## Common failures to avoid

- Accepting "weak advertising" or "low awareness" without testing price, availability, distribution, category and execution.
- Stopping at a long questionnaire instead of making provisional progress.
- Reading the largest component of a decomposition as the cause.
- Declaring the diagnosis "verified" before investigation.
