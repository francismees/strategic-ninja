# Capabilities and fallbacks

The core skill works with supplied evidence and ordinary file access. Tools extend what it can do; they do not define the reasoning. Before relying on a capability, check that it is actually available in this session. Never claim an action you did not perform.

## Contents
1. Detecting what is available
2. Capability table
3. Independent review and parallel work
4. Honest reporting
5. Host notes

## 1. Detecting what is available

- Look at the tools you have been given in this session (file reading, code execution, web search or fetch, browser, document or presentation skills, connectors, subagents, scheduled tasks).
- Do not assume that one host's capabilities exist in another. Claude Code, the Claude apps, Cowork-style sessions and API deployments differ in file persistence, network access, code execution and available skills.
- If unsure whether a tool works, try a small, harmless call (e.g. run `python3 --version`) before planning around it.

## 2. Capability table

| Capability | Use it for | If unavailable |
|---|---|---|
| File reading (PDF, XLSX, CSV, DOCX, PPTX, images) | Read supplied first-party data, research, decks and briefs before anything else | Ask the user to paste the relevant sections or tables; state which files could not be read |
| Code execution (Python 3.8+) | `scripts/commercial_analysis.py`, `scripts/records.py`, statistical libraries if installed | Do small calculations step by step in the response; provide the exact command or recipe for larger ones; say the script was not run |
| Spreadsheet capability (e.g. an available spreadsheet skill) | Reading complex workbooks, writing formatted analysis workbooks with working formulas | Deliver CSV or Markdown tables and the formulas in text |
| Web search and page fetch | Desk research, source verification, disconfirming evidence, refreshing local statistics | Work from supplied material; list sources to check and why; label remembered context as unverified |
| Browser automation | JavaScript-heavy sources, ad libraries, portals that block simple fetches | Record that the source could not be accessed; do not substitute a remembered figure |
| Structured web extraction connectors (e.g. crawling or scraping tools) | Collecting competitor pages or price lists at scale, within site terms | Manual sampling of a few pages with locators |
| Document or presentation rendering (e.g. docx, pptx or PDF skills) | Turning a validated outline and exhibit briefs into a file | Deliver the storyline and exhibit briefs in Markdown; say no file was produced |
| Subagents | Bounded independent review; parallel research across independent source families; independent re-computation | Perform a distinct self-review pass and label it as such |
| Persistent file storage | Engagement records and context across sessions ([../references/memory.md](../references/memory.md)) | Provide a proposed context update for the user to save |
| Scheduled or background tasks | Periodic refresh of a statistic or tracker, if the user explicitly sets one up | None: the skill does not monitor or refresh anything by itself |
| Data connectors (CRM, analytics, social listening, retail audit, media data) | Direct access to client data the user has authorised | Ask for exports; document the extract date and filters |

Respect site terms, robots restrictions, privacy and the user's data permissions. Do not enter credentials or personal data to reach a source; ask the user.

## 3. Independent review and parallel work

Use additional agents only when the work is genuinely independent or verification benefits from separation, and only when the host supports it and the user's setup authorises it.

- **Independent red-team review**: give the reviewer the draft, the evidence files or records, and [../references/red-team.md](../references/red-team.md), without the generating conversation. Ask for gate verdicts and defect records. Report that the review was performed by a separate agent.
- **Parallel research**: split by independent source families (official statistics, company filings, competitor observation), each returning source records with locators.
- **Re-computation**: an independent agent re-runs a calculation from raw inputs.

Do not create a cast of role-playing specialists. One strategist remains accountable for the argument.

## 4. Honest reporting

State in the response, briefly and in plain terms, only what the user needs to rely on the answer:
- Files that could not be read.
- Whether numbers were calculated from their data, done by hand, or not computed.
- Sources checked online (with date) and sources that could not be reached.
- For reviews and audits: whether the review was independent or a self-review.
- Whether records were saved, or only proposed.
- Whether a presentation or document file was produced, or only a storyline.

Do not narrate internal process or name this skill's files, gates or scripts in user-facing text.

## 5. Host notes

- **Claude Code**: skills load from `~/.claude/skills/<name>/` (personal) or `.claude/skills/<name>/` (project). File reading, local code execution and file writes usually work, subject to the user's permissions. Web access depends on configured tools.
- **Claude apps with custom skills**: skills run where code execution is enabled; file persistence between conversations and network access may be limited. Prefer proposed context updates unless persistence is clearly available.
- **API deployments**: dependencies must be present in the execution environment; the scripts here need only the Python standard library.

These notes describe typical behaviour verified at build time; check the current host documentation when behaviour matters.
