# Workflow C: Critique and improve an existing strategy

Use when the user supplies a strategy, plan, brief, positioning or deck and wants it reviewed, stress-tested or improved. Demonstration: [../examples/demo-c-critique/](../examples/demo-c-critique/README.md).

Methods: [../references/red-team.md](../references/red-team.md) (gates, verdicts, defect records, anti-patterns), [../references/evidence-model.md](../references/evidence-model.md), [../references/strategic-choice.md](../references/strategic-choice.md), [../references/storytelling.md](../references/storytelling.md). Load other modules only for the defects you find (e.g. [../references/analytics.md](../references/analytics.md) for a causal claim, [../markets/tanzania.md](../markets/tanzania.md) for local claims).

## Respect the request

- **"Quick look" or short critique**: give the three to five defects that matter most, each with consequence and repair. No full gate table.
- **"Review this deck's storyline"**: address the storyline; flag material logic or evidence gaps; do not restart the whole strategy process.
- **"Red-team this before the board"**: full gate review with defect records and a repaired version where feasible.
- **"Improve this"**: critique first, then repair at the failing layer; show what changed and why.

Do not manufacture disagreement. If the strategy is sound, say so, name what makes it sound, and suggest improvements that raise decision quality.

## Steps

### 1. Understand what the document is trying to do
- Identify the decision it supports, the audience, the recommendation and the argument's structure (governing thought, supporting reasons, evidence).
- Extract load-bearing claims: those that, if wrong, would change the recommendation. List them with where they appear.

### 2. Inspect the evidence
- For each load-bearing claim, find the evidence cited. Open supplied files and check the claim at its locator: does the source say this, for this scope, period and population?
- Classify each claim (observed, computed, inference, hypothesis, assumption, estimate) and note where the document presents one type as another (an assumption written as a fact; a correlation written as a cause).
- Check lineage: are several citations one original source?
- For Tanzania: check scope and proxy use.

### 3. Apply the gates
- Reload [../references/red-team.md](../references/red-team.md). Apply the relevant gates with verdicts (PASS, CONCERN, FAIL, NOT TESTED, NOT APPLICABLE) and reasons.
- Check the anti-pattern library where relevant, especially: fabricated or unsourced statistics, observation as insight, solution smuggling, objectives or activities as strategy, framework substitution, correlation as causation, scope inflation, well-worded uniqueness, exposure as impact, polish over argument, copied tactics.
- Also check calibration: do not fail a sensible shared action for lacking uniqueness; do not fail a sound operational insight for lacking a human tension.

### 4. Write defect records
For every material CONCERN or FAIL:

```text
CLAIM_OR_SECTION / GATE_TESTED / DEFECT / EVIDENCE_OR_MISSING_EVIDENCE
STRATEGIC_CONSEQUENCE / REQUIRED_FIX / RETEST_CONDITION
```

Order defects by consequence for the decision, not by document order. Where the issue is uncertainty rather than error, state what is not established, why it matters and the smallest validation step.

### 5. Decide what the defects mean
- **Presentable as is** — no material failures.
- **Presentable with qualification** — concerns that can be stated honestly (e.g. conditional recommendation with a test).
- **Not presentable as validated** — material FAIL on a load-bearing claim; useful parts may still be presented as provisional.

### 6. Repair (if asked to improve)
- Repair at the failing layer: evidence problems get re-sourcing or downgraded claims; unsupported mechanisms become hypotheses with tests; incoherent choices get rebuilt options; exposure metrics get behavioural and business measures.
- Keep what is sound. Do not rewrite the voice or structure without reason.
- Never strengthen a claim beyond its evidence while rewriting; keep uncertainty visible in the section it affects.
- If the storyline is being rebuilt, produce assertion titles and, for decks, an `outline.json` checked with `python3 scripts/records.py outline`.
- Allow up to two repair passes; report anything unresolved.

### 7. Retest
- Re-apply the gates that failed. Mark each defect repaired, bounded as provisional, or unresolved.
- State plainly that passing gates does not prove the strategy will succeed.

## Output shape

1. **Verdict** in one or two sentences (presentable / with qualification / not as validated) and why.
2. **What is strong** (brief, specific).
3. **Material defects** as defect records or a compact table, most consequential first.
4. **Repaired version** (if requested): revised argument, storyline or sections, with a change log.
5. **Remaining uncertainty and next validation steps.**

## Honesty about the review

Say whether the review was a self-review or performed by an independent agent with only the document, evidence and standards. Say which evidence files were opened and which claims could not be checked.
