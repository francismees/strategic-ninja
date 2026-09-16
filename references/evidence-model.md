# Evidence model

This file defines claim types, confidence, verification status, market applicability, sources, lineage, contradictions, IDs and revision behaviour once. Every other module uses these meanings. Field-level structure lives in [../schemas/records.schema.json](../schemas/records.schema.json); `scripts/records.py validate` enforces both the schema and the semantic rules below.

## Contents
1. Claim types
2. Confidence, verification and market applicability
3. Assessing evidence
4. Sources and lineage
5. Contradictions
6. Records, IDs and traceability
7. Unknowns
8. Revisions and staleness
9. Writing evidence into prose

## 1. Claim types

| Type | Meaning | Must carry | Common mistake |
|---|---|---|---|
| Observed / reported fact (`observed`) | Directly supported within a specified source and scope | At least one source ID and a locator | Treating "the company reports X" as independent proof that X is true |
| Computed finding (`computed`) | Reproducible calculation from identified inputs | Input source IDs and the calculation (script command or formula) | Presenting a computed ratio without denominator, period or unit |
| Inference (`inference`) | Interpretation whose reasoning and dependencies are explicit | Records or sources it depends on, and the reasoning | Hiding a leap inside confident wording |
| Hypothesis (`hypothesis`) | Proposed explanation awaiting adequate testing | Confirming signal, falsifier, decision impact | Calling an untested diagnosis "the problem" |
| Assumption (`assumption`) | Premise accepted provisionally for planning | Why it is reasonable, what would falsify it, review condition | Letting repetition in old decks turn it into fact |
| Estimate / forecast (`estimate`) | Modelled quantity | Method, key assumptions, uncertainty or range | Single-point forecasts over long horizons |

Hypotheses and assumptions live in the hypothesis register (`hypotheses` in the records file, IDs `HYP-` / `ASM-`). Observed, computed, inferred and estimated claims live in `claims` (`CLM-`).

**Recommendations and decisions are not evidence.** They are linked records (`OPT-`, `ACT-`) that depend on evidence. A user-approved decision is a decision, not evidence that it worked. A launch is an event, not a successful outcome.

## 2. Confidence, verification and market applicability

Keep these three properties separate. A claim can be verified against its source, low-confidence for the decision, and only a regional proxy.

**Confidence** answers: how much should this claim bear in the decision? Use `high`, `medium`, `low` or `unknown`, always with a short reason. Do not use percentages or scores to express confidence in a judgement.

- *High*: direct measure of the question, traceable provenance, adequate method, fits the geography and period, and either corroborated independently or the best possible direct source for a narrow claim.
- *Medium*: useful but with one material limitation (proxy measure, dated period, partial coverage, single interested source).
- *Low*: several limitations, indirect, or conflicting evidence unresolved.
- *Unknown*: not yet assessed or the source cannot be inspected.

**Verification status** answers: what has actually been checked?

- `verified` — checked against the source at the stated locator in this work.
- `reproduced` — calculation re-run from inputs and reconciled.
- `unverified` — not checked (e.g. user-supplied figure, secondary citation, remembered fact). Never upgrade from memory.
- `contested` — credible conflicting evidence exists and is retained (see section 5).
- `superseded` — replaced by a newer record (`superseded_by`).

**Market applicability** answers: does this hold for the target market and scope? It is relative to the engagement's market and must name a `scope` (e.g. "Tanzania Mainland, urban adults") and a reason.

- `local_verified` — direct evidence for the stated local scope. It does not mean universally certain.
- `local_supported` — local signals support it but evidence is not definitive (small base, indirect, non-representative).
- `regional_proxy` — evidence from a comparable market (e.g. Kenya, Uganda); transfer untested.
- `global_hypothesis` — mechanism or finding from elsewhere; local applicability untested.
- `unknown` — insufficient evidence to judge.
- `not_applicable` — the claim is not geographic (e.g. an arithmetic identity).

Market-specific rules for classification and transfer are in [../markets/tanzania.md](../markets/tanzania.md).

## 3. Assessing evidence

Assess evidence against the question it must answer, not by source class alone. A company's transaction data can be definitive about its own sales and weak about category demand; an official census can be authoritative and too old for a digital-behaviour question.

| Dimension | Ask |
|---|---|
| Directness | Does it measure the question, or a proxy? |
| Provenance | Who produced it, why, and can it be traced to an original? |
| Method quality | How was it collected, sampled, defined and analysed? |
| Geographic fit | Which country, sub-national area, urban/rural, channel? |
| Period relevance | What is the data period (not only the publication date)? Has anything material changed since? |
| Independent corroboration | Is there evidence with a separate origin? Or only one interested source? |

Seek corroboration **in proportion to materiality and uncertainty**. There is no universal two-source quota. A narrow claim directly measured by an official dataset may need no second source; a load-bearing market-size estimate from a commercial report should be triangulated. When a single direct source is the best available evidence, record that fact in the confidence reason.

Source class (official statistics, regulator, company filing, industry research, journalism, social signal...) helps discovery and sets expectations. It does not determine confidence by itself.

## 4. Sources and lineage

Every source record captures: what it is (title, URL or file, publisher/owner), where exactly the evidence sits (page, table, sheet, cell range, timestamp, respondent ID), publication date, data period, geography, population or sample, method, access date, limitations, and lineage.

**Lineage** prevents false corroboration.

- `original` — the source produced the evidence.
- `derived` — the source reports someone else's evidence; list the original in `derived_from` when known.
- Three articles repeating one press release are one lineage. Two consultancy reports citing the same survey are one lineage.
- When the original cannot be located, keep `origin: "unknown"` and lower confidence accordingly.

**Citations must resolve.** Cite supplied files by name and locator, or real URLs you actually opened. Never invent URLs. Treat exported citation tokens that do not resolve (for example tokens copied from another chat's export) as unresolved pointers, not sources.

**First-party data first.** Read the data and documents the user supplied before searching broadly.

## 5. Contradictions

1. Do not average incompatible numbers or pick the convenient one.
2. Check whether the conflict is real: compare scope, population, definitions, units, method, data period, and whether one source measures subscriptions while another measures people.
3. If the difference is explained, record both claims with their scopes; the conflict dissolves into two compatible statements.
4. If it is not explained, mark both claims `contested`, link them with `contradicts`, state what would resolve it, and show the range or both values where the conflict matters to the decision.
5. A contradiction between survey, sales and interview evidence is often informative (stated vs revealed behaviour, different populations, different periods). Treat it as a lead, not noise.

## 6. Records, IDs and traceability

Record chain:

```text
Source (SRC) → claim / computed finding (CLM) → hypothesis / assumption (HYP, ASM) → insight (INS)
→ option / decision (OPT) → action (ACT) → metric (MET) → learning (LRN)
Red-team defects (DEF) and change log entries (CHG) point at any of the above.
```

- IDs are stable within an engagement: `PREFIX-` followed by letters, digits, `.`, `_` or `-` (e.g. `CLM-012`, `HYP-price-gap`). Never reuse an ID for a different record.
- **Dependents are derived, not stored.** A record lists what it depends on (sources, records, evidence, assumptions, decision link). `scripts/records.py impact` computes what depends on a record, so there is one source of truth.
- **Link-type rules** (checked by the validator): claim bases point to sources or evidence records; insights cite claims, hypotheses or sources; options cite evidence and list assumptions as `HYP`/`ASM`; actions link to an `OPT`; metrics link to `ACT`s; learnings cite metrics or actions.
- Type-specific requirements (checked): `observed` claims need a source; `computed` claims need a calculation; `inference` claims need reasoning and at least one dependency; `estimate` claims need method and uncertainty; `verified` status needs a locator; verbatim quotes need a respondent or source ID and a translation status.
- **Material recommendations must be traceable.** A selected or conditional option needs supporting records; a conditional option needs at least one assumption or condition; a research-first option needs a stated discriminating test in its conditions.

Scale the records to the work. Quick answers need no records file. Standard work may keep only the load-bearing sources, claims, hypotheses and the decision. Deep work keeps full registers.

## 7. Unknowns

- Unknown is honest and never zero. A missing baseline is `"unknown: no pre-campaign tracker wave"`, not `0`.
- Any required text field may be `"unknown: <reason>"`. The validator warns when "unknown" appears without a reason.
- A calculation with an unknown input produces an unknown result with the reason propagated, not a number.

## 8. Revisions and staleness

- When a material source, claim or assumption changes, log a change entry (`CHG-`) with previous value, new value, reason and author.
- Run `scripts/records.py impact --changed <ID>` to list every downstream insight, option, action and metric. With `--apply`, the script adds unresolved review flags to those records and logs the change.
- A flagged record is not wrong; it must be reviewed before being presented as current. Resolve flags explicitly.
- Refresh a material statistic when its age, changed conditions or decision sensitivity requires it. When a refresh fails, keep the old record, state its date, and label the limitation. Never update a figure from memory.

## 9. Writing evidence into prose

Executive prose should read naturally. Carry the evidence status in words where it changes interpretation:

- "Distributor-reported sell-in rose 8%; we have no sell-out data, so we cannot yet tell whether shelves are moving."
- "Our working assumption, untested, is that price rather than availability drove trial."
- "Kenyan evidence suggests this; we have not found Tanzanian data, so treat it as a lead to test."

Put IDs, full confidence reasons and locators in the records, an evidence appendix or footnotes, not in every sentence. Never strengthen a claim when summarising it.
