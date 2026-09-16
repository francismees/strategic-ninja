# Diagnosis

Use this module to orient on the decision, frame the problem and build proportionate competing explanations. The end-to-end procedure is in [../workflows/diagnose.md](../workflows/diagnose.md). Evidence terms follow [evidence-model.md](evidence-model.md).

## Contents
1. Orient: the decision frame
2. Separate objective, symptom, cause and solution
3. Problem levels
4. Hypotheses: prediction, falsifier, decision consequence
5. Method cards: driver tree, hypothesis tree, 5 Whys, first principles
6. Discriminating evidence and prioritisation
7. Stating the diagnosis
8. Failure modes

## 1. Orient: the decision frame

Before analysis, write (or infer and state) a decision frame. Use [../templates/engagement-frame.md](../templates/engagement-frame.md) for standard or deep work.

- **Decision**: a choice someone must make, not a topic. "Whether to cut price on the 500 ml pack in Q1" rather than "pricing".
- **Decision-maker and audience**: who decides, who must be persuaded.
- **Desired outcome and success metric**: what would count as success, measured how.
- **Baseline**: compared with what (last year, plan, category, competitor, a control region)? If unknown, say so; do not invent one.
- **Horizon, scope and constraints**: time, geography, category, budget, capabilities, non-negotiables.
- **Available evidence**: what has been supplied and what it can and cannot show.

If the user gave a topic, not a decision, propose the most plausible decision and proceed; ask only if different decisions would lead to materially different work.

## 2. Separate objective, symptom, cause and solution

Briefs routinely merge these. Pull them apart explicitly:

| Element | Question | Example from "sales are falling because our advertising is weak; we need a new campaign" |
|---|---|---|
| Objective | What outcome is wanted? | Restore volume growth |
| Symptom | What was observed? | Volume down versus last year |
| Possible cause | What might explain it? | Weak advertising (one of several candidates) |
| Proposed solution | What has been suggested? | New campaign |

**Solution smuggling**: when the problem statement already contains the answer ("we need a campaign to fix awareness"), restate the problem without the solution and test the embedded cause alongside alternatives. Do not refuse to help with the campaign; show what would have to be true for it to work and what else could explain the symptom.

## 3. Problem levels

Classify where the binding constraint may sit. More than one level can be true; the diagnosis should name which one binds.

| Level | Diagnostic question | Typical evidence |
|---|---|---|
| Business / commercial | Which outcome is deficient: revenue, margin, cash, share, penetration, retention? Is growth good quality? | P&L, price-volume-mix, margin bridge, customer economics |
| Market / category | Has demand, structure, regulation, channel economics or competitive intensity changed? | Category size and trend, competitor moves, regulatory changes, channel data |
| Customer / consumer | Is the behaviour blocked by need, salience, affordability, trust, habit, access or switching costs? | Behavioural data, research, complaints, qualitative evidence |
| Brand | Is the brand failing on recognition/retrieval, perceived value, relevance, credibility, permission or portfolio clarity? | Tracker, distinctive asset tests, pricing power, research |
| Communications | Is it message, creative, media reach/weight, targeting, or response? | Reach and frequency, recall/attribution, response by exposure |
| Execution | Was a reasonable plan undermined by availability, price execution, quality, service or operations? | Distribution, out-of-stocks, price checks, service metrics |

Chain to follow: **claimed problem → observable symptom → metric gap → possible drivers → discriminating evidence → binding constraint → intervention mechanism.**

## 4. Hypotheses: prediction, falsifier, decision consequence

For each important hypothesis record (in the hypothesis register or in prose for quick work):

- **Proposition**: the proposed explanation.
- **Predicted evidence (confirming signal)**: what we should see if it is true.
- **Plausible falsifier**: what we should see if it is false. Choose observations that could realistically turn up.
- **Present support**: untested, supported, mixed, unsupported, refuted, with the evidence.
- **Decision consequence**: what we would do differently if true versus false. A hypothesis with no decision consequence is not worth researching now.
- **Validation step**: the cheapest evidence that would discriminate.

Example (beverage decline):

| Hypothesis | Predicts | Falsifier | Decision if true |
|---|---|---|---|
| Price gap to competitor widened | Volume loss concentrated where our shelf price rose relative to competitor; competitor gains there | Losses equal in outlets where relative price was unchanged | Price-pack response, not advertising |
| Numeric distribution fell | Losses concentrated in outlets or regions that lost stock; rate of sale in stocked outlets stable | Distribution stable; rate of sale fell | Fix route-to-market first |
| Category contracting | Competitors also declining; our share stable | Our share falling while category flat or growing | Category-level response or portfolio shift |
| Advertising weaker | Declining brand retrieval/consideration among category buyers exposed to media; losses in reach-dependent segments | Retrieval stable; losses concentrated in availability gaps | Communications task |

## 5. Method cards

### Driver tree (arithmetic decomposition)
- **Use when**: an outcome can be broken into additive or multiplicative components (revenue = volume × price; volume = buyers × frequency × units).
- **Not when**: components cannot be measured or the question is why, not where.
- **Inputs**: definitions, data for each component, consistent periods and units.
- **Steps**: write the identity; confirm definitions and denominators; quantify each branch; follow the largest or most decision-relevant branch one level deeper; stop when further splits do not change the decision.
- **Output**: where the change arose, reconciled to the total.
- **Example**: revenue +8% = price +15%, volume −6%, mix −1% (see [analytics.md](analytics.md)).
- **Common failure**: reading the largest component as the cause.
- **Evidence limit**: locates change; does not explain it.

### Hypothesis tree
- **Use when**: several causal explanations compete and evidence is costly.
- **Not when**: the cause is already established by direct evidence, or the task is a quick sparring reply.
- **Inputs**: framed problem, known facts, plausible mechanisms.
- **Steps**: state the governing question; list mutually distinct explanations at the problem-level granularity; for each, write prediction and falsifier; prune branches with no decision consequence; order evidence gathering by discriminating power per unit of effort.
- **Output**: prioritised hypotheses with tests.
- **Example**: the beverage table above.
- **Common failure**: a tree that is exhaustive but has no falsifiers, so every branch stays "possible".
- **Evidence limit**: structures inquiry; proves nothing.

"Mutually exclusive, collectively exhaustive" is a useful aspiration for the top level. Do not force it where causes interact (price and distribution often act together); say so instead.

### 5 Whys
- **Use when**: tracing an operational or execution failure along a plausible causal chain.
- **Not when**: multiple interacting causes exist, or answers would be speculation about consumer psychology.
- **Steps**: ask "why" of the observed failure; require evidence or mark each answer as a hypothesis; stop when the answer is actionable or evidence runs out; check for branches (more than one "because").
- **Common failure**: a single neat chain of unevidenced guesses ending in "culture" or "awareness".

### First principles
- **Use when**: a category convention or inherited assumption may be constraining the options ("our trade must be through wholesalers", "premium cannot sell in rural areas").
- **Steps**: list the assumptions embedded in the current approach; separate physical, economic and regulatory constraints from habits; rebuild the option space from the real constraints; flag which rebuilt options need evidence.
- **Common failure**: declaring a convention false without testing why it exists.

## 6. Discriminating evidence and prioritisation

- Prefer evidence that distinguishes between hypotheses over evidence consistent with all of them. "Sales fell" supports every explanation; "sales fell only in outlets that lost stock" discriminates.
- Prioritise by decision impact × uncertainty ÷ cost and time to learn.
- Check readily available first-party data (sales by outlet, region, SKU; distribution; price checks) before commissioning research.
- A sensible sequence for commercial declines: data quality and definitions → decomposition (price/volume/mix, region/channel/SKU) → availability and price position → category and competitor movement → brand and communications measures → qualitative explanation.

## 7. Stating the diagnosis

A usable diagnosis names:

1. The binding constraint and the level where it sits.
2. The evidence that supports it and the alternatives it beats (and how).
3. What remains uncertain and whether that uncertainty could reverse the next decision.
4. The implication: which kind of response follows and which does not.

Label it honestly: *supported*, *leading hypothesis with conditions*, or *unresolved — here is the test*. A diagnosis can be useful before it is certain.

## 8. Failure modes

- Accepting the brief's diagnosis because the user is senior or confident.
- Refusing to proceed until every question is answered (state assumptions and continue).
- Treating arithmetic decomposition as causal explanation.
- Diagnosing "low awareness" without checking whether awareness is actually the constraint on behaviour.
- Building elaborate trees for a quick question.
- Stopping at the first explanation that fits.
