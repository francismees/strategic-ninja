# Workflow B: Build an annual marketing or brand strategy from mixed evidence

Use when the user needs a client's annual marketing, brand or commercial plan built from a mix of sales data, tracker or survey results, qualitative research, market statistics and prior plans. (This is the skill's *Build Strategy* mode: building a client's strategy.) Demonstration: [../examples/demo-b-annual-strategy/](../examples/demo-b-annual-strategy/README.md).

Methods: [../references/diagnosis.md](../references/diagnosis.md), [../references/research.md](../references/research.md), [../references/analytics.md](../references/analytics.md), [../references/insight.md](../references/insight.md), [../references/strategic-choice.md](../references/strategic-choice.md), [../references/brand-growth.md](../references/brand-growth.md), [../references/action-measurement.md](../references/action-measurement.md), [../references/storytelling.md](../references/storytelling.md), [../references/red-team.md](../references/red-team.md), [../references/memory.md](../references/memory.md). Tanzania: [../markets/tanzania.md](../markets/tanzania.md).

## Entry and exit

- **Enter** at step 1. Reuse an existing diagnosis (Workflow A) or prior records if they are current; check review flags first.
- **Exit** with a strategy document or storyline communicating the decision, diagnosis, decisive evidence, opportunity, alternatives, choice and non-choices, action system, economics, risks and assumptions, measurement and next decisions — plus records for standard/deep work.

## Steps

### 1. Orient and inventory evidence
- Decision frame: what the plan must decide (growth sources, investment allocation, portfolio moves, brand role), decision-maker, horizon (annual), budget constraints, success metric and **baseline**.
- Evidence inventory: list each file with what it measures, period, scope, method and limitations. Create source records for material sources.
- Read any existing context and last year's plan. Treat claims repeated from earlier plans as assumptions until evidence supports them.

### 2. Learn from last year
- What was planned, what happened, and what explains the gap? Separate execution failures from strategy failures.
- Record learnings in their proper state (observed results vs interpretations).

### 3. Diagnose the growth situation
- Decompose performance: price/volume/mix; channel, region, SKU contributions; buyers × frequency where data allow; share versus market.
- Category and competitor context: category growth, share movement, competitor moves (with evidence type labelled).
- Brand health: measures that matter to the growth mechanism (retrieval in buying situations, asset attribution, consideration, perceived value), not awareness alone.
- Customer evidence: behaviour first, then qualitative explanation. Keep quote provenance.
- Local validity: scope every Tanzanian claim; label proxies.
- Reconcile conflicting evidence (e.g. tracker says consideration rose while sales fell): investigate scope, population, period and definitions before concluding.

*Output*: diagnosis statement naming the binding constraint(s) and the evidence, with alternatives considered.

### 4. Find the insights and opportunities
- Run the Insight Engine on the most decision-relevant patterns. Accept operational, commercial and channel insights; do not force a consumer tension.
- Translate insights into opportunity spaces with their commercial mechanism.
- Identify the growth task: which lever (penetration, frequency, price/mix, distribution, retention, new occasions) must move, and for whom.

### 5. Develop and evaluate alternatives
- Build at least two credible routes plus the status quo. Make them differ in real choices (where to play, how to win, lever, resource allocation, risk).
- Use creativity methods if routes are thin; label speculative routes.
- Evaluate each: commercial mechanism, customer value, brand credibility, competitive response, capabilities, resources, risks, time to impact, reversibility, critical assumptions. Use ranges and break-even logic rather than invented forecasts.

### 6. Choose
- Apply the recommendation contract: what to do, why this route, why now, non-choices, what must be true, how to learn, reversal triggers.
- State the recommendation type: supported, conditional or research-first.
- Record the option with supporting records and assumptions.

### 7. Design the action system and measurement
- Actions tied to the chosen route and the diagnosed constraint across the levers needed (product, price-pack, distribution, trade, brand, communications, customer experience, capabilities).
- Each action: intended change, mechanism, owner role, resource basis, dependencies, timing, metric, review condition, reversal trigger. Mark unknown budgets and owners honestly.
- Measurement plan across exposure, behavioural response, brand effects and business outcomes, with baselines, sources, cadence and decision rules. Include pilots where evidence is weak.
- Communications work: follow the communications chain and write the creative brief only after the task is established.

### 8. Verify
- Distinct review pass with [../references/red-team.md](../references/red-team.md): all gates that apply to an annual plan (problem framing, evidence, logic, insight, meaningful choice, commercial mechanism, customer relevance, competitive response, brand credibility, local validity, feasibility, measurement, clarity).
- Defect records for material CONCERN/FAIL; repair the failing layer; up to two repair passes; bound what remains provisional.
- Run `python3 scripts/records.py validate --records records.json`.

### 9. Articulate
- Build the storyline (annual plan sequence in [../references/storytelling.md](../references/storytelling.md)) with assertion titles, keeping uncertainty in the sections it affects.
- For decks, write `outline.json` and run `python3 scripts/records.py outline --outline outline.json --records records.json`.
- Render a file only if a rendering capability exists; otherwise deliver the storyline and exhibit briefs.

### 10. Save or propose context
- If persistence is authorised: save records, context summary and outline in the engagement folder.
- Otherwise: provide a proposed context update.

## Output shape (default)

1. Decision and recommendation (one paragraph).
2. What happened and why (diagnosis with decisive evidence).
3. Where growth will come from (opportunity and growth task).
4. Options considered and why this route.
5. Choices and non-choices.
6. Action system (table) with owners, resources, timing.
7. Economics (ranges, break-evens, sensitivities).
8. Risks, assumptions and reversal triggers.
9. Measurement plan and learning agenda.
10. Decisions needed now.
Appendix: evidence register and records.

## Proportionality

- A user who asks for "a quick view of next year's priorities" gets a one-page provisional plan with the key assumptions and the evidence to gather.
- A full annual plan with data uses all steps.
- Five-year or three-year questions use [multi-year-strategy.md](multi-year-strategy.md).
