# Storytelling and deliverables

Use this module to structure an argument for an audience: memos, one-pagers, board papers, workshop materials and deck storylines. The strategy skill owns the argument; any available document or presentation capability owns rendering and technical validation ([../integrations/capabilities.md](../integrations/capabilities.md)). Outline contract: [../schemas/outline.schema.json](../schemas/outline.schema.json).

## Contents
1. Argument first
2. Governing thought and supporting logic
3. Situation, complication, question, answer
4. Assertion-evidence sections and slides
5. Audience storylines
6. Keeping uncertainty visible
7. The outline contract
8. Rendering and fallbacks
9. Failure modes

## 1. Argument first

Build the argument before any formatting. A good deliverable lets a busy reader grasp the decision, the reasons and the ask in under a minute. Presentation polish, jargon and length never compensate for a weak argument; the Red Team checks for this ([red-team.md](red-team.md)).

## 2. Governing thought and supporting logic

- **Governing thought**: one or two sentences stating the recommendation or central conclusion, including its condition if it is conditional.
- **Supporting reasons**: typically three to five points that together justify the governing thought. Each answers the reader's natural question ("why?", "how?", "how do you know?").
- **Evidence** under each reason actually supports that reason.

Two checks:
- **Vertical**: each point is supported by the points beneath it and answers the question raised by the point above.
- **Horizontal**: points at the same level are of the same kind, do not overlap, and together cover the question; sequence them in a logical order (time, structure, importance, or causal chain).

These are semantic checks that need judgement; no validator can prove them.

## 3. Situation, complication, question, answer

A useful opening pattern, used flexibly:

- **Situation**: what the reader already accepts.
- **Complication**: what changed or what is at risk.
- **Question**: the question this raises for the decision-maker.
- **Answer**: the governing thought.

For a workshop, the answer may be an explicit set of open choices rather than a conclusion. Do not pretend a final answer exists when it does not.

## 4. Assertion-evidence sections and slides

- Each section or slide title is a full-sentence assertion ("Volume fell because stocked outlets dropped by a fifth", not "Volume trends").
- The body is evidence that supports that assertion: a chart that answers it, a table, a quote set with IDs, a bridge.
- Read the titles in sequence: they should form the argument on their own.
- Every exhibit shows units, bases, periods and sources.

## 5. Audience storylines

| Deliverable | Typical sequence |
|---|---|
| Board decision | Decision required → economics and stakes → diagnosis and evidence → options considered → recommendation and conditions → risks → ask |
| Executive one-pager | Situation → problem → decisive evidence → recommendation → implications and conditions → decisions required |
| Annual brand/marketing plan | Last year's learning → what changed in the category → diagnosis → growth task and sources → choices and non-choices → action system and budget basis → measurement → asks |
| Campaign strategy | Business objective → behavioural challenge → audience and occasion → barrier and evidence → communications task → proposition → channel roles → measures |
| Positioning / GTM | Market and alternatives → target and context → value and proof → route to market and pricing → launch sequence → risks and tests |
| Multi-year strategy | Structural drivers → scenarios → strategic position and capabilities → no-regret moves and options → signposts and triggers → investment staging |
| Workshop | Question → evidence → competing explanations → choices to make → criteria → what we need to learn |

These are starting points; adapt to what the audience must decide.

## 6. Keeping uncertainty visible

- Put material uncertainty where it changes interpretation — in the section it affects, not only in an appendix.
- Carry the recommendation type into the storyline: a conditional recommendation stays conditional; a research-first recommendation leads with the test.
- When rewriting or shortening, never strengthen a claim beyond its evidence. "Early pilot data suggest" must not become "proven".
- Use plain language for evidence status ("company-reported", "our estimate", "untested assumption", "Kenyan evidence, not yet validated here").

## 7. The outline contract

For decks and structured documents, produce an outline JSON following [../schemas/outline.schema.json](../schemas/outline.schema.json):

- Top level: engagement ID, title, audience, format, decision requested, governing thought, recommendation type.
- Each section: ID (`S01`…), role (context, complication, diagnosis, evidence, insight, alternatives, recommendation, action, economics, risk, measurement, ask, appendix), assertion, the audience decision it supports, evidence IDs from the records file, recommended exhibit, notes, uncertainty, source locators.

Validate with:

```bash
python3 scripts/records.py outline --outline outline.json --records records.json
```

The validator checks structure, that evidence IDs resolve, that diagnosis/evidence/insight/recommendation/economics/risk/measurement sections cite records, that decision records are not cited as evidence for factual sections, that sections citing uncertain evidence state their uncertainty, and that the storyline's recommendation type is not stronger than the recorded option. It cannot judge whether the evidence truly supports each assertion or whether the sequence persuades; review that yourself.

## 8. Rendering and fallbacks

- If a presentation or document capability is available and the user wants a file, pass it the outline and exhibit briefs; let that capability handle layout and file validation.
- If none is available, deliver the storyline (assertion titles, section content, exhibit briefs with data and sources, speaker notes) in Markdown. Say plainly that no presentation file was produced.
- Do not copy another tool's internal instructions or scripts to imitate rendering.

## 9. Failure modes

- Topic titles instead of assertions.
- Exhibits that do not prove their titles.
- An executive summary that differs from the body.
- Uncertainty hidden in the appendix.
- A storyline that pretends the workshop has already decided.
- Conditional recommendations presented as settled.
- Beautiful slides with no traceable evidence.
