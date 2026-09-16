# Validation report: strategic-ninja v1.0.0

> The skill was renamed from `marketing-brand-strategy` to `strategic-ninja` (Strategic Ninja) after this validation. Only names and paths changed; the checks were re-run after the rename (see [package-check-latest.json](package-check-latest.json)). Raw evaluation transcripts keep the original wording.

**Date:** 2026-09-17 · **Environment:** Claude Code desktop app on macOS, Python 3.9.6 (standard library only)

This report separates four things:
- what is implemented;
- what was actually tested, and whether it passed or failed;
- what was not run;
- what was deferred.

It also separates "the package works" from "the skill has been shown to be better at real strategy work". The first is supported by evidence. The second is **not established**.

## 1. Summary

| Question | Answer |
|---|---|
| Does the package conform to the Agent Skills specification for Claude Code? | Yes. Deterministic checks PASS: frontmatter, size, links, routing, JSON, records, scripts. Claude app upload was not tested; the description length limit is uncertain there (see §5) |
| Do the three required workflows work end to end? | Demonstrated with synthetic engagements (Demos A, B, C). Records and storylines validate, and calculations reconcile. The demos were written by the builder following the workflows; they are not independent runs |
| Do the calculations reconcile and fail transparently? | Yes. 31 analytics fixtures PASSED, with expected values derived by hand. Invalid inputs produce named errors |
| Is traceability usable? | Yes. 8 records fixtures PASSED; the three demo record sets validate; staleness propagation flags the dependent decision chain |
| Does the skill change behaviour in the intended direction? | Provisionally yes, with recorded weaknesses. Across 14 blinded, same-model-judged cases, the skill passed 14 and the baseline 13, and judges preferred the skill in 11. The first version produced over-long answers and referred to itself; after a repair, these improved on 5 re-run cases, with mixed preferences (§3) |
| Is the skill shown to improve real strategy work? | **Not established.** No human expert review, small sample, same model family judging, and no real client use |

## 2. Deterministic checks

| Check | Command | Result | Evidence |
|---|---|---|---|
| Analytics fixtures (31) | `python3 scripts/run_fixtures.py` | **PASSED 31/31** | [deterministic-latest.json](deterministic-latest.json) |
| Records and outline fixtures (8) | same | **PASSED 8/8** | same |
| Runner can detect failure | Temporary fixture with a wrong expected value (180 vs 181) and a non-existent flag | **PASSED** (runner reported FAIL as intended; fixture removed) | Build log |
| Package checks | `python3 scripts/check_package.py --run-fixtures` | **PASSED** (0 errors; see [package-check-latest.json](package-check-latest.json)) | Frontmatter, SKILL.md size, links, direct routing of every module, reachability, hygiene, privacy scan, records and outlines, observation records, script compilation |
| Demo records validate | via package check | **PASSED** (Demos A, B, C: 0 errors) | `examples/*/records.json` |
| Demo storylines validate | via package check | **PASSED** (Demo B `outline.json`, Demo C `improved-outline.json`) | `examples/*` |
| Original flawed deck fails the storyline check | `records.py outline` on `examples/demo-c-critique/analysis/original-outline.json` | **As expected: invalid, with 6 errors.** The market-size error on slide 2 was *not* caught structurally and needed semantic review | [check output](../../examples/demo-c-critique/analysis/original-outline-check.json) |
| Required fixed-unit case (100 × 10 → 90 × 12) | `pvm-01` | **PASSED**: revenue 1,000 → 1,080; price +180, volume −100, mix 0; flagged as price-led growth with falling volume | fixture file |
| Multi-SKU mix, new and discontinued items | `pvm-03` | **PASSED**: bridge 90 + 0 + 100 + 300 − 150 = 340 | fixture file |
| Zero and missing bases | `pvm-04`–`pvm-07`, `buyers-07` | **PASSED**: no infinities or fabricated growth rates; explicit errors or notes | fixture files |
| Buyer × frequency × units | `buyers-01`, `buyers-02` | **PASSED** (Shapley attribution exact to 1e-6) | fixture files |
| Share, contribution and denominators | `contribution-01`–`05` | **PASSED** | fixture files |
| Invalid grain, units, periods, joins | `pvm-08`–`15`, `buyers-03`–`08`, `join-01` | **PASSED** (named errors) | fixture files |
| Memory revision makes a downstream recommendation stale | `records-04`, `records-05`; Demo B CHG-001 | **PASSED** | fixture files; Demo B records |

What these checks cannot show: source truth, insight quality, strategic fit or causality.

## 3. Behavioural evaluation

Full report: [behavioral-2026-09-17/README.md](behavioral-2026-09-17/README.md).

| Item | Status |
|---|---|
| 14 cases: 12 development and 2 held-out; 7 standard, 5 adversarial, 2 ambiguous | **RUN**. Skill: 14 PASSED. Baseline: 13 PASSED, 1 FAILED (BEH-06; a second judge later passed the same baseline answer) |
| Pairwise preference, run 1 | Skill preferred 11/14; baseline preferred 3/14 (BEH-13, BEH-17, BEH-20) |
| Skill-condition failures found | **FAILED quality expectations, not case verdicts:** over-long answers (+27% words overall); references to the skill in 5/14 answers; outside statistics that did not fit (2 cases); missing quote IDs (1 case); less concrete on a board decision (1 case) |
| Repair and re-run (5 cases) | **RUN.** Skill mentions fell to 0/5 and every answer got shorter. Preferences: skill 3/5, baseline 2/5 (BEH-02 flipped to baseline, BEH-17 flipped to skill, BEH-13 stayed baseline) |
| Repairs not re-tested | `integrations/capabilities.md` §4 and `references/brand-growth.md` §10 (**NOT RUN**) |
| Remaining 13 of the 25 development cases (BEH-03, 04, 07, 09, 10, 11, 14, 15, 18, 19, 21, 23, 24) | **NOT RUN** in this build |
| Repeated runs for variance | **NOT RUN** |
| Human expert review | **NOT RUN** |
| Native triggering in a live Claude Code session | **NOT RUN** (no `claude` CLI available; skill loaded by instruction in subagents) |

## 4. Implementation status against the Version 1 definition of done

| Requirement | Status | Evidence |
|---|---|---|
| Package conforms to the verified Agent Skills requirements; SKILL.md routes to every module | **Implemented and tested** (deterministic) | Package check: frontmatter, routing, links |
| Three required workflows work end to end | **Implemented and demonstrated** with synthetic data; not independently run as whole workflows | [Demo A](../../examples/demo-a-diagnosis/README.md), [Demo B](../../examples/demo-b-annual-strategy/README.md), [Demo C](../../examples/demo-c-critique/README.md) |
| Records internally consistent and traceable, without audit notation in executive prose | **Implemented and tested** (structure). Prose quality checked in the demos by the builder | Schemas, validator, demo memos |
| Analytical recipes reconcile and fail transparently | **Implemented and tested** | 31 fixtures |
| Tanzania reasoning applies safeguards without hardcoded stale conclusions | **Implemented.** Behaviour partly tested (BEH-08 and HELDOUT-01 passed; BEH-07 and BEH-09 not run) | markets/*, run report |
| Red Team uses gates and defect records; failures repaired, bounded or reported | **Implemented; demonstrated** in Demos A–C | Demo records and reviews |
| Adversarial, qualitative, memory and deterministic fixtures with observable expectations; honest statuses | **Implemented**; statuses recorded here | evals/ |
| Source/reuse register complete for material actually used; notices included | **Implemented.** No third-party material copied, so no notices required; courtesy acknowledgements included | [../../provenance/source-register.md](../../provenance/source-register.md) |
| README allows install and invocation and explains dependencies, fallbacks and limits | **Implemented**; installation into Claude Code not executed in this session | [../../README.md](../../README.md) |
| Report distinguishes implemented from tested, and usable from demonstrated superior | This document | — |

## 5. Known limitations and open issues

1. **Claude app description limit.** The help article states 200 characters; the specification and Anthropic's validator allow 1,024. The skill uses 719 characters for better triggering. A 191-character alternative is in the README. Upload was not tested.
2. **Answer length.** After repair, skill answers were still longer than the baseline in 2 of 5 re-run cases. Watch this in real use.
3. **Concreteness on board decisions.** BEH-13 was preferred to the baseline in neither run. A module change was made (`brand-growth.md` §10) but not re-tested.
4. **Judge reliability.** Same-model judges disagreed on at least one baseline verdict. Verdicts are provisional.
5. **Tanzania observations.** A small, dated set verified on 2026-09-17: NBS CPI, OCGS CPI (news summary only), TCRA June 2026 quarter, World Bank population and Findex account ownership. Review conditions apply. The TCRA direct PDF URL was not captured; the listing page is recorded.
6. **Source access.** Several sources blocked automated access or failed at check (BoT statistics page, IMF, AfDB, ZRA domain, `www.dse.co.tz`). These are recorded in the source registry.
7. **Validator scope.** `records.py` uses a built-in JSON Schema subset validator when `jsonschema` is absent (it was absent here). Semantic checks cannot judge whether evidence supports an assertion.
8. **Demonstrations** were written by the builder; they show intended reasoning, not independent performance.

## 6. Deferred (by design)

See [../../provenance/build-decisions.md](../../provenance/build-decisions.md) §7:
- scripts for cohorts, survey weighting, segmentation stability and time series;
- a verified historical precedent library;
- sector packs;
- automated refresh of observations;
- additional market modules;
- rendering integration tests;
- native trigger tests;
- repeated runs;
- human expert review.

## 7. How to reproduce

```bash
cd strategic-ninja
python3 scripts/check_package.py --run-fixtures
python3 scripts/run_fixtures.py --verbose
```

Behavioural protocol: [../behavioral/rubric.md](../behavioral/rubric.md) and [../README.md](../README.md).
