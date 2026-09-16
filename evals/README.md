# Evaluations

Two kinds of evidence, kept separate:

1. **Deterministic checks** prove structure and arithmetic: package validity, links, schemas, ID resolution, staleness propagation, storyline evidence links, and calculations that reconcile against independently derived expected values. They cannot prove source truth, insight quality, strategic fit or causality.
2. **Behavioural evaluations** test what the skill actually does with realistic requests, compared with the same model without the skill. Model-judged results are provisional evidence, not field validation.

Current results: [results/validation-report.md](results/validation-report.md).

## Deterministic checks

Run from the skill folder:

```bash
python3 scripts/run_fixtures.py --verbose        # analytics and records fixtures
python3 scripts/check_package.py --run-fixtures  # package checks plus fixtures
```

| Fixture set | What each fixture stores |
|---|---|
| [fixtures/analytics/](fixtures/analytics/) | Raw input CSV, recipe arguments, calculation convention, tolerance, hand-derived expected values (with the derivation written out), edge-case expectation and expected failure behaviour. Covers fixed-unit and multi-SKU price-volume-mix, interaction conventions, new/discontinued items, zero and missing bases, buyer × frequency × units with defined windows, Shapley attribution, contribution and share with consistent denominators, and invalid inputs (duplicate grain, unit changes, mixed units/currency/measures, unequal periods, broken joins, ambiguous number formats) |
| [fixtures/records/](fixtures/records/) | Engagement records and outlines with expected validator outcomes: valid engagement, broken links and claim-type errors, untraceable recommendations, a memory revision that must flag the dependent decision chain, a stale decision after revision, schema and locator errors, and storylines that strengthen claims or hide uncertainty |

Expected values were derived by hand (arithmetic shown in each fixture's `derivation`) rather than generated with the functions under test. A deliberate mutation (a wrong expected value) was confirmed to fail the runner during the build.

## Behavioural evaluations

- **Cases:** [behavioral/cases.json](behavioral/cases.json). There are 25 cases in three tiers: standard, ambiguous and adversarial. Each has the failure it tests, the prompt, fixture files, expected behaviour, prohibited behaviour and the evidence needed for a pass.
- **Fixtures:** [behavioral/fixtures/](behavioral/fixtures/). All are synthetic and marked as such.
- **Protocol and rubric:** [behavioral/rubric.md](behavioral/rubric.md). Same model, brief, files and tools for both conditions; fixtures copied to a neutral folder; responses blinded and order-randomised; the judge does not see the skill; verdicts, not scores.
- **Recorded runs:** [results/](results/). Raw responses, blind mapping, judgements and the summary are kept, including failures.

### Running a behavioural evaluation yourself

1. Copy `behavioral/fixtures/` to a folder outside the skill.
2. For each case, run the prompt in a fresh session **without** the skill (baseline) and **with** the skill (treatment). In Claude Code, install the skill for the treatment run and remove it or use a separate profile for the baseline. Save both final responses.
3. Randomise which response is "Response 1" per case and record the mapping.
4. Give a judge (a human strategist is best; a separate model session is acceptable as provisional evidence) the rubric, the case and the two blinded responses.
5. Record verdicts and preferences per the rubric. Keep raw outputs. Repeat any case whose verdict differs across runs.

## Status vocabulary

PASSED · FAILED · NOT RUN · DEFERRED, as defined in [behavioral/rubric.md](behavioral/rubric.md) §6.
