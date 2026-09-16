# Build decision record

**Skill:** Strategic Ninja (`strategic-ninja`, originally built as `marketing-brand-strategy`) v1.0.0 · **Built:** 2026-09-17 · **Inputs:** *Claude Super Prompt v1.1* (build instruction), *Research Synthesis and Decisions*, and three research papers: *Marketing AI Agent Strategy Blueprint* by ChatGPT, Claude and Gemini (cited below as **CG**, **CL**, **GE** with their own section names).

This record lists what was adopted, adapted, rejected and deferred, and why. It does not repeat the ecosystem research. Third-party resources actually inspected are in [source-register.md](source-register.md).

## 1. Environment and host verification

| Item | Finding (verified 2026-09-17) | Consequence |
|---|---|---|
| Host | Claude Code desktop app on macOS; personal skills live in `~/.claude/skills/<name>/` | Primary install target; package is a portable Agent Skills folder |
| Agent Skills specification ([agentskills.io/specification](https://agentskills.io/specification)) | `name` ≤64 chars, lowercase letters/digits/hyphens, matches folder; `description` ≤1,024 chars; optional `license`, `compatibility` (≤500), `metadata`, `allowed-tools`; root file under 500 lines and about 5,000 tokens recommended; references one level deep | Frontmatter uses only `name`, `description`, `metadata`. SKILL.md is 134 lines and about 4,100 tokens (estimate). Every module is linked directly from SKILL.md |
| Claude Code skills documentation | Description plus `when_to_use` truncated at 1,536 chars in the listing; Claude Code-only fields break app upload | No Claude Code-only fields used |
| Claude app upload ([help article](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)) | Zip with the skill folder at the root; article states a **200-character** description limit, which conflicts with the 1,024-character specification and Anthropic's `quick_validate.py` (1,024) | **Unresolved discrepancy.** The description is 719 characters to trigger well in Claude Code. If an app upload rejects it, shorten the description (a 200-character alternative is given in the README) |
| Python | System Python 3.9.6; no pandas, SciPy or jsonschema installed | Scripts use only the standard library; `records.py` uses `jsonschema` if present, otherwise a built-in subset validator |
| Tools | Web fetch and search, GitHub CLI, browser, subagents available; no `claude` CLI on PATH | Sources and repositories verified online; behavioural evaluation run through subagents. Automatic triggering in a live session **not tested** |

## 2. Principal synthesis decisions (as required by the instruction)

| Question | Decision | Paper basis |
|---|---|---|
| One strategist or a team of agents? | One accountable strategist; subagents optional for bounded review, parallel research or re-computation | CG *Recommended technical pattern* (adopted); GE *Final question* multi-agent orchestration (rejected); CL *Part X* (adapted) |
| Fixed pipeline or adaptive routing? | Ten-stage reasoning process with entry, reuse and return conditions (SKILL.md §3) | CG *Recommended strategic operating system*, *Finalization decision tree* (adapted); CL *Part VI* re-enterable stages (adopted); GE *Part VI* deterministic sequence (rejected) |
| Must every insight contain tension? | No. Evidence → observation → contrast → mechanism → insight; tension optional | CG *Improved Insight Engine* (adopted); CL *Part VII* tension gate and GE *Part VII* "Aha" test (rejected) |
| Must every recommendation be unique? | No. Competitor-substitution test applies to positioning and advantage claims only | GE *Part XIII* "Only-We" veto (rejected as universal); CG *Core anti-patterns* substitution test (adapted) |
| Which brand doctrine wins? | None. Question-to-lens selector (references/brand-growth.md) | CG *Strategy synthesis: reconcile the schools* (adopted); CL *Part V* FMCG vs premium routing (rejected); GE *Part V* penetration-before-loyalty and 60/40 (rejected) |
| Must every claim have two sources? | No. Corroboration proportional to materiality; lineage tracking | CG *Evidence quality: decision matrix* (adopted); CL *Part XII–XIII* ≥2-source rule (rejected) |
| Hardcode Tanzania statistics? | No. Dated, verified observation records with review conditions; source policy is durable | CG *Tanzania intelligence layer* (adopted); CL *Part VIII* baselines and GE *Part VIII* mandatory constraints (rejected) |
| Can uncertainty stop work? | Blocks unsupported claims and commitments only; supported / conditional / research-first recommendations | Synthesis correction 5; gcamilo repository evaluation finding (see source register) |
| Does a quality score prove quality? | No. Gate verdicts plus defect records; behavioural evaluation against a baseline | CG *Strategic Red Team*, *Testing framework* (adopted); CL *Part XIV* label-count metrics (rejected) |
| Is a full agent framework required? | No. Markdown modules, JSON records and standard-library scripts | CG *Recommended technical pattern* (adopted); LangGraph and CrewAI-style infrastructure (rejected for v1) |

## 3. Adopted and adapted from each paper

**ChatGPT paper (architecture, reasoning, evidence, local validation, memory)**
- *Problem Reframing Protocol* and six problem levels → references/diagnosis.md §2–3 (adopted).
- *Strategic question cascade* with confirming signal and falsifier → hypothesis record fields (adopted).
- *Insight Card* → insights schema and templates/insight-card.md (adapted: tension optional, status labels added).
- *Strategic horizon* table → SKILL.md §2 and workflows/multi-year-strategy.md (adapted).
- *Evidence quality* six dimensions → references/evidence-model.md §3 (adopted); source classes kept only as a discovery aid.
- *Tanzania intelligence layer* local statuses → market applicability enum (adapted to add scope and a "not applicable" option).
- *Context engineering and strategic memory* four layers and provenance/expiry → references/memory.md (adopted); "update memory only with approved learning" adapted into an authorisation-based write rule.
- *Operating modes* and *Strategic Sparring Partner* → SKILL.md §2 routing and workflows/sparring.md (adapted: fewer, sharper questions plus a point of view).
- *Storytelling and deck architecture* audience storylines → references/storytelling.md §5 (adopted).
- *Strategic Red Team* gates and defect format → references/red-team.md (adopted, with verdicts NOT APPLICABLE and RETEST_CONDITION added per instruction).
- *Core anti-patterns* → anti-pattern library (extended per instruction).
- *Testing framework* scenarios → evals/behavioral/cases.json (extended to 25 cases in three tiers).
- *Proposed directory architecture* → simplified (no `config/`, `memory/` or `AGENTS.md`; one integrations file; schemas consolidated into two files).

**Claude paper (methods, framework selection, research discipline, analytics, quality checks)**
- *Part IV* deep dives: "when it breaks down" per framework, depth modes, can/cannot conclude, quote-anchored qualitative evidence → method cards in references/*.md and references/insight.md §6 (adapted).
- *Part V* Rumelt and where-to-play/how-to-win pairing, jobs and switching → references/strategic-choice.md method cards (adapted, summarised in own words).
- *Part IX* strategic data interrogation and recipe list → references/analytics.md §5 and scripts/commercial_analysis.py (adopted: price-volume-mix, buyers × frequency, contribution, profiling; deferred: cohort, clustering and seasonality scripts).
- *Part XI* modes → routing table (adopted).
- *Part XIV* tiered evaluation (standard/ambiguous/adversarial), pairwise vs baseline → evals/behavioral (adopted); hard-gate tuning lesson → SKILL.md rules 5 and 12.

**Gemini paper (commercial action, persistent context, perspectives, argument separate from rendering)**
- *Part IV* presentation-skill JSON outline separate from rendering → schemas/outline.schema.json and `records.py outline` (adapted; original implementation).
- *Stage 7 Design* connecting strategy to pricing, channels and operations → references/action-measurement.md §1–2 (adopted).
- *Part IV* competitive-intelligence "claims vs traction" → references/research.md §5 signal table (adapted, with limits on what visibility shows).
- *Part IV* multi-persona data analysis → optional independent review or re-computation only (adapted; no standing personas).
- *Part XIII* So-What check, vertical/horizontal logic → references/analytics.md §8 reporting contract and references/storytelling.md §2 (adopted).
- *Part X* persistent brand memory → governed engagement files with staleness propagation (adapted; no session hooks).

## 4. Rejected recommendations (important ones)

| Recommendation | Source | Reason |
|---|---|---|
| Deterministic 12-stage pipeline that must never be skipped | GE *Part VI* | Different tasks need different entry points; causes process theatre |
| Standing multi-agent "CSO + analyst + insight + local expert" orchestration | GE *Final question* | Coordination overhead; one accountable argument |
| Penetration before loyalty as a core principle; 60/40 as a rule | GE *Core principles*, *Part V*; CL *Part V* | Conditions differ (subscriptions, premium, B2B); ratios are contextual evidence |
| Only-We test rejects any strategy a competitor could execute | GE *Part XIII* | Wrongly rejects effective availability, price or service fixes |
| Hardcoded Tanzanian constraints (44.7% smartphone, 87m mobile money accounts, 90% informal retail) as mandatory filters | GE *Part VIII*, *Final deliverable* | Unverified or out-of-scope aggregates; national figures cannot settle segment questions |
| Hardcoded baseline statistics in the source stack | CL *Part VIII*, *Recommendations* | They age quickly; kept as dated, refreshable observation records instead |
| Sheng as part of Tanzanian cultural context | CL *Part VIII* | Kenyan urban vernacular; Tanzanian language use must be validated locally |
| Mandatory tension or "Aha" gate for insights | CL *Part VII*; GE *Part VII* | Operational and commercial insights can be decisive without tension |
| Measuring success by evidence-label counts | CL *Part I*, *Part XIV* | Rewards appearance, not decision quality |
| ≥2-source cross-validation for every key claim | CL *Part IV* §3 | A single direct source can be the best evidence; repeats are not independent |
| Illustrative research budget tiers and fixed sample-size folklore | CG *Research plan template*, *Common research designs* | The instruction forbids generic budgets and folklore; cost drivers described instead |
| Red Team that "actively destroys" the strategy | GE *Part XI* | Replaced with evidence-based, constructive defect records |
| Numeric strategy scores | CL creative-director pattern; CG noted as a risk | Verdicts and defects instead |
| Session-end hooks that update memory automatically | GE *Part IV* | Markdown instructions cannot create hooks; automatic promotion of beliefs is unsafe |

## 5. Corrections to inferences in the papers (carried into the skill)

1. **Inflation → pack response.** The NBS August 2026 figures are verified (headline 4.3%, transport 13.8%; Mainland NCPI, p.2 Table 1). The skill still treats them as context that does not establish a firm's cost exposure or the right pack strategy (markets/tanzania.md §5.4).
2. **Subscriptions → reach.** TCRA's June 2026 report counts 116,952,295 telecom subscriptions (SIMs active in 90 days, including machine-to-machine) against a World Bank 2025 population estimate of 70,545,865. The skill encodes the safeguard and uses this as a worked example. The synthesis document had said TCRA figures were not verified; this build extracted them from the report tables.
3. **Informal retail share.** Not encoded; category and channel scope rules instead.
4. **Process compliance ≠ decision quality.** The gcamilo evaluation measures label use and has mixed pairwise results; the evaluation here judges behaviour against case-specific expectations.

## 6. Corrections or clarifications to the build instruction

No consequential technical error was found. Clarifications made:
- The instruction lists `anthropics/skills` for "available authoring and document capabilities". Verified that the pptx, xlsx and docx skills carry **proprietary** terms and the root has no licence file. They are treated only as optional runtime capabilities; no material was used. skill-creator (Apache-2.0) validation rules informed the independent checks in `scripts/check_package.py`; no code was copied.
- The 200 vs 1,024 description limit conflict for the Claude app is recorded above rather than resolved by guesswork.
- The instruction's claim-type list includes hypothesis and assumption; the record model keeps them in a separate hypothesis register (as the instruction's record table also specifies) so they cannot be cited as observed facts.

## 7. Deferred (explicitly out of version 1)

| Item | Reason for deferral | Where it would go |
|---|---|---|
| Scripts for cohorts, survey weighting, segmentation stability, time series | Method guidance provided; established libraries should be used when installed | scripts/ + references/analytics.md §7 |
| Verified historical precedent library | Needs sourced, scoped cases; fictional teaching cases only in v1 | examples/ (separate labelled section) |
| Sector packs (FMCG, telecoms, financial services, health) | Build after real-use gaps are observed | references/ |
| Automated refresh or monitoring of Tanzania observations | Requires a configured scheduled capability and access policy | integrations/ |
| Additional market modules | Contract defined in markets/tanzania.md §1 | markets/ |
| Rendering integration tests with document or presentation skills | Proprietary components; not needed for the argument contract | integrations/ |
| Trigger-accuracy tests in a live Claude Code session; human expert review; repeated runs | Not available in this build session; see evals/results/validation-report.md | evals/ |
