# Behavioural evaluation rubric and protocol

Use with [cases.json](cases.json). The purpose is to test the skill's actual behaviour against a no-skill baseline, not to score appearances. Do not reward evidence-label counts, length, number of frameworks, or the model's own stated confidence.

## 1. Setup

1. **Same model, same brief, same files, same tools, comparable effort** for both conditions.
   - *Baseline*: the model answers the case prompt with the fixture files available, without the skill.
   - *Treatment*: the same, with the skill loaded (in Claude Code: installed skill; in a harness: the agent is told to read `SKILL.md` and follow it).
2. Copy fixture files to a neutral folder so the baseline cannot read the skill.
3. Save each final user-facing response verbatim to a file.
4. **Blind** the judge: label responses "Response 1" and "Response 2" in a randomised order per case and record the mapping separately.
5. Where feasible, repeat unstable cases (a case whose verdict differs across two runs) and report both runs.
6. Keep some **held-out** prompts written by someone who has not read the skill, to reduce teaching to the test.

## 2. What the judge receives

- The case: prompt, fixture files, failure tested, expected behaviour, prohibited behaviour, pass evidence.
- The two responses, blinded.
- This rubric.
The judge does not receive the skill files.

## 3. Per-response judgement

For each response:

1. **Expected behaviour items**: mark each MET, PARTLY MET or NOT MET, quoting or pointing to the relevant passage.
2. **Prohibited behaviour items**: mark each PRESENT or ABSENT, with the passage if present.
3. **Case verdict**:
   - **PASS**: no prohibited behaviour present, and the pass evidence is clearly shown (most expected items MET, none of the essential ones NOT MET).
   - **FAIL**: any prohibited behaviour present, or the pass evidence absent.
   - **UNCLEAR**: cannot be judged from the response (explain).
4. **Quality dimensions** (qualitative notes, not scores): diagnosis quality; unsupported material claims (list them); causal overclaims; evidence traceability; local validity; trade-offs and choice; commercial coherence; clarity; usefulness to a senior practitioner; amount of human correction needed before use (none / light / substantial).

## 4. Pairwise judgement

- Which response would a senior strategist rather receive for this request, and why (one short paragraph)?
- Options: Response 1, Response 2, or no meaningful difference.
- Note any case where the treatment is worse (e.g. over-process, excessive caution, too long for the request).

## 5. Reporting

Report for each run: date, model, number of cases, conditions, blinding and order method, judge model or human, raw verdicts per case and condition, pairwise preferences, notable failures with quotes, and limitations. Never convert verdicts into a single quality score. Do not present model-judged results as independent field validation; state that same-model judging is provisional evidence.

## 6. Status vocabulary for the validation report

- **PASSED**: run and passed as defined above.
- **FAILED**: run and failed; keep the raw output and the repair made, if any.
- **NOT RUN**: defined but not executed in this build.
- **DEFERRED**: intentionally postponed with a reason.
