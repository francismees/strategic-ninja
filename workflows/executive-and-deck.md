# Executive summaries, one-pagers and deck storylines

A short composition for articulation tasks. Methods: [../references/storytelling.md](../references/storytelling.md). Evidence status: [../references/evidence-model.md](../references/evidence-model.md). Outline contract: [../schemas/outline.schema.json](../schemas/outline.schema.json). Rendering: [../integrations/capabilities.md](../integrations/capabilities.md).

## Respect the request

If the user asks to improve a storyline or summary, work on that. Flag material logic or evidence gaps and their effect on the argument; do not restart the strategy process unless asked.

## Executive summary or one-pager

1. Identify the decision the reader must make and what they already believe.
2. Write the governing thought: the recommendation (with its condition if conditional) in one or two sentences.
3. Give three to five supporting reasons, each with its decisive evidence (numbers with units, periods and sources).
4. State the main alternative and why it was not chosen.
5. State risks, assumptions and what would change the recommendation.
6. End with the decisions or approvals needed, with dates.
7. Check: does the summary match the body? Is any claim stronger than its evidence? Is material uncertainty visible?

Keep to one page for a one-pager. Use plain language for evidence status rather than audit notation.

## Deck storyline

1. Choose the audience storyline (board, annual plan, campaign, positioning/GTM, multi-year, workshop) from [../references/storytelling.md](../references/storytelling.md).
2. Write slide titles as assertions. Read them in sequence: they must form the argument alone.
3. For each slide, specify the evidence (record IDs if records exist), the exhibit that proves the title, notes, uncertainty and source locators.
4. Put material uncertainty on the slide it affects.
5. For structured work, write `outline.json` and run `python3 scripts/records.py outline --outline outline.json --records records.json`.
6. If a presentation capability exists and a file is wanted, pass it the outline and exhibit briefs. Otherwise deliver the storyline in Markdown and state that no file was produced.
7. Verify with the clarity, evidence and logic gates. A beautiful deck with unsupported claims fails; repair the evidence or qualify the claim, never the design alone.
