# Strategic Ninja

A strategic thinking partner for experienced practitioners in business, marketing, brand, commercial strategy, consumer insight and communications. It is particularly strong in Tanzania.

It helps you:
- understand what is happening and determine what matters;
- find defensible opportunities and choose a course of action;
- explain why that choice should work;
- see exactly which evidence, assumptions and calculations a recommendation rests on.

It is a portable [Agent Skills](https://agentskills.io/specification) package. It needs no database, framework or paid service. Its scripts use only the Python standard library.

## Install

### Claude Code (verified host for this build)

Copy the folder into your personal skills directory, then start or continue a Claude Code session:

```bash
cp -R strategic-ninja ~/.claude/skills/
```

For a single project instead, copy it to `.claude/skills/strategic-ninja/` inside that project. Claude Code watches skill folders, so no restart is normally needed.

### Claude apps (upload)

Build the upload archive with `python3 scripts/check_package.py --zip ../dist/strategic-ninja.zip` (the zip has the skill folder at its root) and upload it via **Customize → Skills**. Code execution must be enabled for the scripts. Anthropic's help article states a 200-character description limit, which conflicts with the 1,024-character limit in the Agent Skills specification. If the upload rejects the description, replace it with this 191-character version:

> Strategy partner for marketing, brand and commercial decisions: diagnose problems, analyse sales data, find insights, build or critique strategies and briefs. Tanzania market module included.

Upload was not tested in this build.

### Other Agent Skills hosts

Place the folder where the host loads skills. The frontmatter uses only specification fields (`name`, `description`, `metadata`). The folder must be named `strategic-ninja` to match the `name` field.

## Invoke

The skill triggers automatically on strategy, brand, marketing, insight, research, analytics or Tanzania market requests. In Claude Code you can also type `/strategic-ninja` followed by your request. You don't need to choose a mode. It infers task mode, depth, horizon and output from what you ask, and you can override them in plain language ("quick view", "go deep", "just the storyline").

## What it does

| Capability | Where it lives |
|---|---|
| Diagnose ambiguous or solution-shaped problems | [workflows/diagnose.md](workflows/diagnose.md), [references/diagnosis.md](references/diagnosis.md) |
| Build annual marketing and brand strategies from mixed evidence | [workflows/annual-strategy.md](workflows/annual-strategy.md) |
| Critique and improve existing strategies and decks | [workflows/critique-and-improve.md](workflows/critique-and-improve.md), [references/red-team.md](references/red-team.md) |
| Campaigns and briefs, positioning and GTM, multi-year strategy, executive summaries and deck storylines, sparring | [workflows/](workflows/campaign-strategy.md) (short compositions of the shared modules) |
| Evidence discipline: claim types, confidence, lineage, contradictions | [references/evidence-model.md](references/evidence-model.md) |
| Research design and competitor signals | [references/research.md](references/research.md) |
| Reconciled calculations: price-volume-mix, buyers × frequency, contribution and share, data profiling, join checks | [scripts/commercial_analysis.py](scripts/commercial_analysis.py), [references/analytics.md](references/analytics.md) |
| Insight Engine with explicit inference limits | [references/insight.md](references/insight.md) |
| Strategic choice, brand and growth methods | [references/strategic-choice.md](references/strategic-choice.md), [references/brand-growth.md](references/brand-growth.md) |
| Action systems, measurement and pilots | [references/action-measurement.md](references/action-measurement.md) |
| Argument structure and a renderer-neutral storyline contract | [references/storytelling.md](references/storytelling.md), [schemas/outline.schema.json](schemas/outline.schema.json) |
| Traceable records, staleness propagation, readable registers | [schemas/records.schema.json](schemas/records.schema.json), [scripts/records.py](scripts/records.py), [references/memory.md](references/memory.md) |
| Tanzania local reasoning, source registry, dated verified observations | [markets/tanzania.md](markets/tanzania.md), [markets/tanzania-sources.md](markets/tanzania-sources.md), [markets/tanzania-observations.json](markets/tanzania-observations.json) |

## Example requests

- **Quick:** "Gut check: is 'Refreshingly Tanzanian' a strong tagline for a new soda? Two lines." You get a short, proportionate answer, not a strategy process.
- **Analytical:** "Here's our sales file by SKU and region for 2025 and 2026. Where did the revenue change come from?" It checks the data contract, runs a reconciled price-volume-mix bridge and reports the finding, method, uncertainty, interpretations and consequence.
- **Sparring:** "Push back on my idea to move 40% of trade spend to modern trade." You get a point of view, the evidence that would change it, and a few sharp questions.
- **Full strategy:** "Build our 2027 brand plan from these files: panel data, tracker, interviews and last year's plan." You get a diagnosis, alternatives, a choice with non-choices, an action system, economics, measurement, a validated storyline and traceable records.

The worked demonstrations use synthetic data: [examples/](examples/README.md).

## Dependencies

| Item | Required? | Notes |
|---|---|---|
| File reading | Required for supplied material | Works with pasted text if files cannot be read |
| Python 3.8+ | Optional | For the scripts. Without it, the skill does small calculations by hand and gives exact recipes |
| `jsonschema` package | Optional | `records.py` uses it if installed; otherwise it falls back to a built-in validator for the schema subset used |
| Web search or fetch | Optional | For research and refreshing local statistics; without it the skill works from supplied material and labels gaps |
| Document or presentation skills | Optional | For rendering files from a validated storyline; otherwise it delivers the storyline and exhibit briefs |
| Subagents | Optional | For bounded independent review or parallel research |

Fallbacks and honesty rules: [integrations/capabilities.md](integrations/capabilities.md).

## Keeping engagement records

For multi-session work, keep records **in your workspace, not in the skill folder**. For example: `strategy-context/<client>/<brand>/<market>/<engagement>/records.json`. Start from [templates/engagement-records.json](templates/engagement-records.json).

```bash
python3 scripts/records.py validate --records records.json
python3 scripts/records.py impact --records records.json --changed ASM-001 --set status=refuted --reason "..." --apply
python3 scripts/records.py render --records records.json --output records.md
python3 scripts/records.py outline --outline outline.json --records records.json
```

Run the scripts from this skill's folder, or give their full path.

## Validation and provenance

- Deterministic checks: `python3 scripts/check_package.py --run-fixtures` ([check_package.py](scripts/check_package.py), [run_fixtures.py](scripts/run_fixtures.py)). Details in [evals/README.md](evals/README.md).
- What was tested, what failed and what was not run: [evals/results/validation-report.md](evals/results/validation-report.md).
- Build decisions, including what was adopted, adapted, rejected and deferred from the three research papers: [provenance/build-decisions.md](provenance/build-decisions.md).
- Third-party resources inspected, licences and reuse decisions: [provenance/source-register.md](provenance/source-register.md).

## Known limitations

- Behavioural evaluation used the same model family as judge, on a limited number of cases. It is provisional evidence, not proof that the skill improves real strategy work. Human expert review has not been done.
- Automatic triggering was not tested in a live Claude Code session. Claude app upload was not tested.
- Tanzania observations are a small, dated set verified on 2026-09-17. Refresh material figures before use.
- Advanced statistical methods (survey weighting, cohorts, segmentation stability, time series) have method guidance but no dedicated scripts.
- Teaching cases and demonstrations are fictional. No verified historical precedent library is included yet.
- The skill cannot monitor, refresh or learn in the background. Memory is explicit files read and written when you invoke it.

## Licence

No licence has been chosen yet. Add one before sharing. Third-party material is not included; see the source register.
