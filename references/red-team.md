# Red Team: verification, gates and anti-patterns

Use this module whenever you verify your own work before delivery or critique someone else's strategy. The review procedure for existing strategies is in [../workflows/critique-and-improve.md](../workflows/critique-and-improve.md). Record format: `defects` and `gate_results` in [../schemas/records.schema.json](../schemas/records.schema.json); a human-facing form is [../templates/red-team-review.md](../templates/red-team-review.md).

## Contents
1. Separate generation from evaluation
2. Gates
3. Verdicts
4. Defect records
5. Repairing the right layer
6. Anti-pattern library
7. Calibration: when not to object

## 1. Separate generation from evaluation

1. **Reload the standards.** Re-read this file and the modules relevant to the work (e.g. [evidence-model.md](evidence-model.md), [insight.md](insight.md), [../markets/tanzania.md](../markets/tanzania.md)). Do not review from memory of what you intended.
2. **Inspect the actual evidence.** Open the cited file, table or record. Check that the evidence says what the claim says, at the stated scope and period.
3. **Test gates relevant to the task.** Mark others NOT APPLICABLE or NOT TESTED with a reason.
4. **Name specific failures.** Each material CONCERN or FAIL gets a defect record.
5. **Be honest about independence.** Never call a self-review independent; a role label ("as the CFO...") does not make a review independent. When the deliverable is itself a critique or audit, state in one line whether it was a self-review or performed by a separate agent given only the work, the evidence and these standards. For ordinary answers, do not narrate the review.
6. **Bound the effort.** Standard work: gates relevant to the decision. Deep or high-stakes work: all applicable gates plus an explicit search for disconfirming evidence and alternative explanations for load-bearing claims.

## 2. Gates

| Gate | PASS means | Typical failure |
|---|---|---|
| Problem framing | Decision, outcome and baseline are clear; symptom, cause and solution are separated | "Awareness is low, so we need a campaign" |
| Evidence | Material claims trace to real sources or reproducible calculations at the right scope, period and lineage | Statistic with no provenance; three articles from one press release counted as three sources |
| Logic / causality | Conclusions follow; causal claims have adequate identification; alternatives considered | Correlation read as ROI; a bridge read as cause |
| Insight | Insights explain, are supported, specific and decision-changing; mechanism hypotheses are labelled as such | Observation or invented psychology presented as insight |
| Meaningful choice | Credible alternatives considered; the recommendation chooses and states non-choices | "Win all segments in all channels" |
| Commercial mechanism | A plausible path to value (price, volume, margin, distribution, penetration, frequency, retention, switching, mix, cost) with economics or ranges where defensible | Inspirational positioning with no route to money |
| Customer relevance | Human and behavioural claims are evidenced and context-specific; audiences are behaviourally meaningful and reachable | Demographic caricatures; invented motivations |
| Competitive response | Competitor positions and likely responses considered; advantage claims tested | White space defined only by a 2×2 |
| Brand credibility | The brand has permission and assets to deliver; generic claims tested by competitor substitution | A positioning that works equally well with a competitor's logo |
| Local validity | Local claims are verified or labelled proxy/hypothesis with validation; aggregates not generalised to segments | Kenyan data called Tanzanian; SIM counts called people |
| Feasibility | Capabilities, resources, dependencies and constraints addressed | Plan relies on distribution the client lacks |
| Measurement | Metrics test the mechanism with baselines, sources, cadence and decision rules; exposure not confused with outcome | Reach and engagement declared as business impact |
| Clarity | The decision, argument, uncertainty and ask are clear to the audience | Framework pile; polish concealing a weak argument |

## 3. Verdicts

- **PASS** — the gate's standard is met for this work, with the reason.
- **CONCERN** — a fixable or bounded weakness; the conclusion may stand with repair or explicit qualification.
- **FAIL** — a material defect: the affected conclusion cannot be presented as validated or ready for commitment.
- **NOT TESTED** — relevant, but not assessed (state why: no access, out of scope, time).
- **NOT APPLICABLE** — irrelevant to this work (state why).

Rules:
- A FAIL blocks presenting the affected conclusion as validated. It does not block useful partial work, scenario analysis or an explicitly provisional recommendation.
- Passing gates is not proof that the strategy will succeed. Say so where a reader might think otherwise.
- Do not convert verdicts into numeric scores.

## 4. Defect records

Every material CONCERN or FAIL uses this structure:

```text
CLAIM_OR_SECTION            the exact claim, slide or section affected
GATE_TESTED                 one of the gates above
DEFECT                      the precise failure, not a generic quality comment
EVIDENCE_OR_MISSING_EVIDENCE what was inspected, what it shows, or what is absent
STRATEGIC_CONSEQUENCE       what goes wrong in the decision if uncorrected
REQUIRED_FIX                the repair at the failing layer
RETEST_CONDITION            what must be true to mark it repaired
```

Where the issue is uncertainty rather than error, say what is not established, why it matters to the decision, and the smallest proportionate validation step.

Example:

```text
CLAIM_OR_SECTION   Slide 4: "Consumers are trading up to premium, so launch Gold at +40% price"
GATE_TESTED        commercial_mechanism
DEFECT             Premium launch rests on willingness to pay that no evidence establishes
EVIDENCE           Only evidence is a global trend article and rising premium SKU count on shelf; no sales of existing premium SKUs, no price test
CONSEQUENCE        Launch could cannibalise core margin or fail at shelf; +40% price could lose trial
REQUIRED_FIX       Reframe as conditional; add premium-tier sell-out analysis and a priced test (e.g. limited-outlet pilot with matched controls)
RETEST_CONDITION   Pilot rate of sale and source of volume known versus control outlets
```

## 5. Repairing the right layer

| Defect found in | Repair at |
|---|---|
| Source quality, scope, lineage | Evidence: re-source, qualify, or downgrade the claim |
| Unsupported mechanism | Explanation: return to insight; label as hypothesis; add validation |
| Misframed problem | Diagnosis: restate the problem and competing explanations |
| No real alternatives or incoherent trade-offs | Choice: rebuild options that differ in real choices |
| Action not connected to diagnosis | Action design: rebuild the action system from the constraint |
| Metrics cannot detect the mechanism | Measurement design |
| Argument unclear but sound | Articulation only |

Do not cosmetically rewrite around a faulty premise. Allow up to two targeted repair passes after the first critique; if a defect persists, report it as unresolved or bound the conclusion as provisional.

## 6. Anti-pattern library

Detect and correct these when relevant; do not mechanically search for every item on every task.

1. **Fabrication**: invented statistics, quotations, respondents, cultural consensus, sources, or false precision. Repair: remove or replace with sourced evidence or an explicit unknown.
2. **Observation as insight**: facts, trends or tensions presented without an explanatory mechanism. Repair: add contrast and mechanism with evidence, or relabel as observation.
3. **Invented psychology**: consumer motives asserted to bridge an evidence gap. Repair: state as hypothesis with a test, or find behavioural or qualitative evidence.
4. **Stereotype segments**: demographic personas that are not behaviourally meaningful, reachable or commercially useful. Repair: segment on behaviour, needs, occasions or economics that change the decision.
5. **Solution smuggling / objective or activity as strategy**: "our strategy is to grow 10%" or "our strategy is TikTok". Repair: diagnosis, guiding choice, coherent actions.
6. **Framework as substitute**: SWOT, a 2×2, a framework stack or a named methodology instead of diagnosis or choice. Repair: state the decision the framework was meant to inform, then make it.
7. **Correlation as causation; bridge as cause**. Repair: label association; propose identification (experiment, matched regions, pre/post with controls).
8. **Scope inflation**: one African market, national average, subscription count, device ratio or single-category statistic generalised beyond its scope. Repair: restate scope; seek segment-level or local evidence.
9. **Well-worded uniqueness**: positioning or advantage treated as unique because it is elegantly phrased. Repair: competitor-substitution test; evidence of the brand's right to the claim.
10. **Rejecting sensible shared actions**: an effective operational action rejected only because a competitor could also do it. Repair: judge it on whether it relieves the diagnosed constraint and pays back.
11. **No value mechanism**: recommendations disconnected from price, volume, margin, distribution, acquisition, penetration, frequency, retention, switching, mix or cost. Repair: state the mechanism and economics, or drop the action.
12. **Exposure as impact**: short-term reach or engagement used to declare long-term brand or business effect. Repair: add behavioural and business measures and a way to attribute them.
13. **Unsupported big claims**: brand purpose, premiumisation, segmentation or portfolio moves without the required business, behavioural or economic evidence. Repair: make conditional; specify the evidence and test.
14. **Premature creative**: ideas before the communications task or strategic problem is established. Repair: define the business objective, behaviour, audience, barrier and task first; hold ideas as illustrations.
15. **Polish over argument**: design, jargon or length concealing a weak argument. Repair: reduce to governing thought and supporting reasons; test each against evidence.
16. **Copied tactic**: a competitor's tactic proposed without testing whether its mechanism, assets, capabilities, economics and context transfer. Repair: run the transfer test in [strategic-choice.md](strategic-choice.md).
17. **Posture failures**: flattery, reflexive contrarianism, forced novelty, excessive caution, unnecessary questions or process theatre that reduce decision usefulness. Repair: give the proportionate useful answer.

Additional watch-list items: stale local facts, missing economics, vanity metrics, meaningless white-space maps, implausible advantage, fixed budget ratios or doctrines presented as laws.

## 7. Calibration: when not to object

- A simple, well-supported answer is a good answer. Do not demand novelty.
- A valid operational fix (restore distribution, correct a price gap) does not need a human tension to justify it.
- Retention can be the binding constraint in subscription economics even though acquisition still matters.
- An action competitors could copy can still be right if it fixes the constraint and pays back.
- Uncertainty is not a failure when it is visible, bounded and paired with a way to learn.
- When the user asks for a short critique, give the few defects that matter most, not a full gate table.

Worked counterexamples and boundary cases are in [../examples/calibration-cases.md](../examples/calibration-cases.md).
