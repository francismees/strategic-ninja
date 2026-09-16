# Action, communications and measurement

Use this module to turn a chosen route into an action system, write communications strategy and creative briefs, design measurement and pilots, and review results. Templates: [../templates/action-measurement-plan.md](../templates/action-measurement-plan.md), [../templates/creative-brief.md](../templates/creative-brief.md).

## Contents
1. The action system
2. Levers beyond communications
3. Communications strategy chain
4. The strategic creative brief
5. Measurement design
6. Pilots and experiments
7. Reviewing results (Measure / Learn)
8. Failure modes

## 1. The action system

Connect every major action to the diagnosed obstacle and the desired outcome. For each action record:

| Field | Meaning |
|---|---|
| Decision link | Which chosen option it implements |
| Intended change | The customer behaviour or operational change it must cause |
| Mechanism | Why that change should create value (lever) |
| Owner or owner role | Who is accountable (role if the person is unknown) |
| Resource basis | Budget, people or assets, or "unknown: not yet estimated" |
| Dependencies | What must happen first |
| Timing | When, in which sequence |
| Measure | How we will know the change happened |
| Review condition and reversal trigger | When to check, and what result stops or changes it |

Mark unknown budgets and owners honestly. Do not invent authority, commitments or approvals.

Check the system as a whole:
- **Coherence**: actions reinforce the guiding choice; none contradicts another.
- **Sequencing**: availability before demand creation where availability is the constraint; capability before scale.
- **Cannibalisation and margin**: what else changes when this works?
- **Organisational constraints**: capacity, incentives, decision rights.
- **Competitor response**: what happens if they react?

Activation means market or operational implementation. Producing a deck is an artifact task, not activation.

## 2. Levers beyond communications

Address the levers the diagnosis requires: product or service, price and pack, distribution and availability, trade terms and visibility, brand, communications, customer experience and capabilities. Advertising cannot repair unavailability, poor product quality or broken economics. When communications is not the constraint, say so and redirect effort.

## 3. Communications strategy chain

```text
Business objective → required behaviour → audience and occasion → barrier or opportunity
→ communications task → proposition and support → brand assets and tone → channel roles → measurement
```

- **Business objective**: the commercial outcome (e.g. restore volume in urban single-serve).
- **Required behaviour**: what people must do differently (try, buy more often, choose us at the kiosk, stay subscribed).
- **Audience and occasion**: who, in which situation, with evidence.
- **Barrier or opportunity**: why they are not already doing it (does not come to mind, cannot find it, too expensive per occasion, distrust, habit).
- **Communications task**: what communication can actually do about the barrier (build memory links to a buying situation, reframe value, reassure, remind, announce availability). If communication cannot remove the barrier, state that.
- **Proposition and support**: the single most motivating, true and differentiating thing to say, with proof.
- **Brand assets and tone**: distinctive assets to use; tone appropriate to audience and culture, validated locally.
- **Channel roles**: what each channel does (reach, retrieval at point of purchase, detailed persuasion, conversion), not a channel list.
- **Measurement**: the chain of measures in section 5.

Separate the tasks: marketing strategy (where and how to grow), brand strategy (what the brand should mean and how it is recognised), communications strategy (what communication must do), creative (how to express it). Creative ideas generated before the communications task is established are illustrations, not strategy.

When a leader asks for "a viral campaign", reframe the desired business and behavioural outcome and the communications task before treating virality as the strategy. Virality is a possible distribution mechanism for a message, not an objective.

## 4. The strategic creative brief

A strong brief gives the creative team a clear problem and room for inventive execution. It includes:

1. **Business problem and objective** (one or two sentences).
2. **What we want people to do** (behaviour) and **think or feel** (only if evidenced as a driver).
3. **Who** (audience and occasion, described through behaviour and context, not stereotypes).
4. **The barrier or opportunity** with its evidence.
5. **The communications task**.
6. **The single-minded proposition** and **reasons to believe**.
7. **Mandatories**: brand assets, legal and regulatory requirements, languages.
8. **Tone and cultural guidance** with what is validated and what needs local review (e.g. Kiswahili register).
9. **Channels and formats** with their roles.
10. **How success will be judged**.
11. **What we know and do not know** (evidence status of key claims).

Do not prescribe the execution. Do not include invented consumer quotes or psychology.

## 5. Measurement design

Set the success metric and baseline during orientation. Finalise measurement while designing the intervention, not after the deck is built. Select metrics that test the hypothesised mechanism.

| Level | Examples | What it can show |
|---|---|---|
| Exposure / output | Reach, frequency, impressions, outlets visited, coolers placed, listings gained | That the activity happened |
| Behavioural response | Trial, repeat, visits, sign-ups, rate of sale, basket size, search | That behaviour changed among exposed or treated units |
| Brand effects | Retrieval in buying situations, asset attribution, consideration, perceived value | That memory or perception shifted |
| Business outcome | Volume, revenue, share, margin, retention, customer lifetime value | That value was created |
| Operational | Fill rate, out-of-stock rate, delivery lead time, service levels | That the operation delivers |

For each metric specify: definition, baseline (or "unknown: reason" and how to establish one), target or target-setting method, horizon, data source, cadence, owner role, and the decision rule (what result means continue, change or stop). Include leading indicators that move early and lagging outcomes that confirm value.

Guard against declaring business impact from reach, engagement or an unvalidated proxy. Where attribution matters, plan the comparison (control regions, holdout outlets, pre-period trend) before launch.

## 6. Pilots and experiments

When evidence is weak but action is useful, design a reversible pilot or the smallest credible validation step.

1. **Question**: what exactly must the pilot decide? Which hypotheses does it discriminate between?
2. **Unit**: outlets, districts, customers, time periods.
3. **Comparison**: randomised or matched controls; pre-period data for both groups.
4. **Measures**: primary outcome, leading indicators, guardrails (margin, cannibalisation, stock-outs).
5. **Duration and size**: long enough to cover purchase cycles; large enough that the smallest commercially meaningful effect could be detected (state the assumptions; seek statistical help for formal power calculations).
6. **Decision rule**: pre-agreed result that leads to scale, adapt or stop.
7. **Validity risks**: contamination between test and control, novelty effects, unrepresentative pilot areas, concurrent changes (price moves, competitor launches), measurement changes.

Do not claim a pilot validates a national or multi-year strategy beyond its observed scope. State where the result transfers and what would still need confirming.

## 7. Reviewing results (Measure / Learn)

1. **Compare outcome with expectation** at each level of the chain: did the activity happen, did behaviour change, did brand measures move, did business outcomes follow?
2. **Locate the break**: strong reach with no behaviour change means the message, audience, offer or availability failed — not success. Investigate which mechanism failed.
3. **Consider alternative explanations** for any movement: seasonality, price, distribution, competitor activity, measurement changes.
4. **Record learnings in their proper state** (observed result, computed finding, inference, revised hypothesis). A launch is not an outcome; a user-approved decision is not evidence that it worked.
5. **Update dependent records**: when an assumption is confirmed, weakened or refuted, run `scripts/records.py impact` and review flagged decisions ([memory.md](memory.md)).
6. **Decide**: continue, change or stop, according to the pre-agreed rule; if no rule existed, say so and propose one.

## 8. Failure modes

- Actions without owners, resources or measures.
- Communications prescribed for a distribution or product problem.
- Measurement added after the plan is presented.
- Exposure metrics reported as impact.
- Pilot results generalised to the whole market.
- Campaign success declared from awards, reach or engagement.
- Creative execution briefed before the task is clear.
