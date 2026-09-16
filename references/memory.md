# Context and memory

Use this module when an engagement spans sessions, when prior strategy material exists, when records must be saved or updated, or when an assumption or source changes. Record semantics follow [evidence-model.md](evidence-model.md). Template for proposing updates: [../templates/context-update.md](../templates/context-update.md).

## Contents
1. What memory is (and is not) in this skill
2. Four context layers
3. Workspace layout and namespaces
4. Record states
5. Reading context
6. Writing context: authorisation and fallback
7. Revisions, staleness and learning
8. Rules that prevent stale beliefs becoming facts

## 1. What memory is (and is not) in this skill

- Memory here means **explicit files** (engagement records and a short context summary) that you read and write when invoked, where the host allows file access.
- Markdown instructions do not create background monitoring, session hooks, automatic learning or scheduled refreshes. Retrieval, review and refresh happen only when the skill is invoked or when the user has configured a separate capability (e.g. a scheduled task) that calls it.
- The distributed skill package contains no client data. Engagement files live in the user's workspace, never inside the skill folder.

## 2. Four context layers

| Layer | Contents | Loaded |
|---|---|---|
| Working set | Only the evidence and records needed for the current question | Always, kept small |
| Source and evidence index | Source records and claim summaries with locators back to originals | Searched when needed |
| Durable strategy context | Current decisions, active assumptions, key verified facts, open questions, learnings — each dated and scoped | Read at the start of a related task |
| Raw archive | Original files: decks, reports, datasets, transcripts | Opened only for verification or new analysis |

Compression must not erase caveats, contrary evidence or source scope. Summaries link back to their records and originals.

## 3. Workspace layout and namespaces

Suggested layout in the user's workspace (adapt to the host):

```text
strategy-context/
  <client>/<brand>/<market>/<engagement>/
    records.json        # engagement records (schemas/records.schema.json)
    context.md          # short durable summary with links to record IDs
    outline.json        # storyline, when a deck or document is planned
    analysis/           # inputs, commands and outputs for computed findings
    sources/            # pointers to or copies of raw source files (as permitted)
```

- The engagement `namespace` field is `client/brand/market/engagement` (lowercase slugs).
- Never mix clients in one file. Never move private client context into a shared or public knowledge base.
- Market knowledge that is not client-confidential (e.g. verified public statistics) may be reused across engagements only as dated source and claim records with their original scope.

## 4. Record states

Keep these distinct:

| What | Where it lives |
|---|---|
| Source observations | `sources` + `claims` of type `observed` |
| Computed findings | `claims` of type `computed` with the calculation |
| Inferred beliefs | `claims` of type `inference`, or `insights` |
| Hypotheses and planning assumptions | `hypotheses` (`HYP`, `ASM`) with status and review condition |
| Proposed choices | `options` with `decision_state: proposed_by_analyst` |
| User decisions | `options` with `decision_state: approved_by_user` or `rejected_by_user` |
| Implementation status | `actions.status` |
| Measured outcomes | `metrics` + `learnings`, entering as observed or computed results |
| Superseded knowledge | `verification_status: superseded` with `superseded_by`; never deleted silently |

Each durable item carries its source, confidence, data period, owner where known, `last_verified`, a review or expiry condition, and superseded status where relevant. Material revisions get a change-log entry.

## 5. Reading context

1. At the start of a related task, look for an existing engagement folder or records file before asking the user for context again.
2. Read `context.md` and the records relevant to the question; open raw files only when verification or new analysis is needed.
3. Check dates and review conditions. Treat items past their review condition as needing re-verification; say so if they are material.
4. Check for open review flags (`python3 scripts/records.py validate --records records.json` lists them). Resolve or disclose them before presenting affected conclusions as current.
5. Treat repetition across old decks as one lineage, not corroboration.

## 6. Writing context: authorisation and fallback

- **Authorised and supported** (the user has asked for records to be kept, or the host and project clearly use local engagement files): write routine, reversible records without asking each time. Tell the user briefly what was saved and where.
- **Not authorised or not supported** (no file access, a chat surface without persistence, or no indication the user wants records kept): do not claim to have saved anything. Provide a **proposed context update** using [../templates/context-update.md](../templates/context-update.md) that the user can save.
- **Always ask** before overwriting an established fact, deleting records, or changing a user decision.
- Never silently overwrite. Supersede with a new record and a change entry.

## 7. Revisions, staleness and learning

When a material source, claim or assumption changes:

1. Record the change (new source/claim, or status change on the hypothesis) and log it.
2. Run impact analysis:

   ```bash
   python3 scripts/records.py impact --records records.json --changed ASM-001 \
     --set status=refuted --reason "Q2 audit shows channel share flat (CLM-014)" --author analyst --apply
   ```

   This lists every downstream insight, option, action and metric, adds unresolved review flags to them, and appends a change entry.
3. Review each flagged record: confirm, revise, or mark superseded. Resolve the flag explicitly.
4. Re-run `validate`. A selected option that relies on a refuted assumption fails validation until reviewed.
5. Tell the user which decisions are affected and what the change means for them.

When results arrive after implementation, use the review procedure in [action-measurement.md](action-measurement.md) and record learnings in their proper state.

Without code execution, trace dependencies manually through the records (options list their assumptions and supporting records; actions list their decision; metrics list their actions) and list the affected records in your response.

## 8. Rules that prevent stale beliefs becoming facts

- Repetition in old decks, meetings or memory does not validate an assumption.
- A user-approved decision is a decision, not evidence that it worked.
- A launch is not a successful outcome.
- A learning enters as the claim type its evidence supports; interpretations of results remain inferences until tested.
- Refresh a material statistic when its age, changed conditions or decision sensitivity requires it; if refresh fails, keep the dated record and label the limitation. Never update from memory.
- No automatic promotion: moving a hypothesis to `supported` requires evidence recorded in the file.
