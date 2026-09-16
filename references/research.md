# Research

Use this module to plan and conduct research around a decision: desk research, competitor intelligence, qualitative work, surveys, behavioural analysis and experiments. Evidence recording follows [evidence-model.md](evidence-model.md). Market sources for Tanzania are in [../markets/tanzania-sources.md](../markets/tanzania-sources.md). Planning template: [../templates/research-plan.md](../templates/research-plan.md).

## Contents
1. Organise research around the decision
2. Choosing a method
3. Desk research procedure
4. Searching for disconfirmation
5. Competitor intelligence: what signals can and cannot show
6. Qualitative evidence
7. Surveys and quantitative research design
8. Synthetic respondents and personas
9. Stopping rules
10. What not to do

## 1. Organise research around the decision

Start from the most consequential uncertainty, not from a topic list. For each gap specify:

| Field | Question |
|---|---|
| Question | What exactly do we need to know? |
| Why it matters | Which hypothesis or option does it affect? What would change? |
| Method | Desk, first-party analysis, qualitative, survey, behavioural analysis, experiment, mixed |
| Likely sources | Where the evidence probably is, including supplied files |
| Stopping condition | When we know enough for this decision |
| Decision rule | Which result would change the recommendation, and how |

Order gaps by decision impact × uncertainty ÷ cost/time. A gap that cannot change the decision is not a research priority, however interesting.

## 2. Choosing a method

| Question type | Suitable methods | Main limitations |
|---|---|---|
| What happened, where? | First-party sales/distribution analysis, retail audit, tracker trends | Coverage, definitions (sell-in vs sell-out), reclassification |
| How many / how common? | Representative survey, administrative or census data | Sampling frame, non-response, self-report, weighting |
| Why do people behave this way? | In-depth interviews, observation/ethnography, diary studies, switching interviews | Not prevalence; interviewer and recall effects |
| What will people do if we change X? | Experiment or pilot, conjoint/choice modelling designed before fieldwork, historical natural variation | Validity outside test conditions; stated vs revealed preference |
| Did our action cause the change? | Randomised test, matched control regions/outlets, difference-in-differences, interrupted time series | Assumptions must be defended; contamination; power |
| What is the market structure / competitor position? | Filings, regulator data, retail audit, price and distribution checks, ad libraries | Visibility ≠ performance; partial coverage |
| What is already known? | Evidence synthesis of prior studies and internal research | Publication bias; heterogeneous definitions |

Mixed methods often work best: qualitative work to find mechanisms, quantitative to size them, experiments to test responses.

**Sample size and budget.** Derive sample size from the inferential objective: the smallest difference that matters, expected variability, desired confidence, subgroups that must be read, and design effects from weighting or clustering. Do not use folklore ("n=400 is always enough") or generic research budgets. Never invent supplier quotations; if cost matters, describe the cost drivers (incidence, geography, language, method, sample, travel) and recommend obtaining quotes.

## 3. Desk research procedure

1. **Read what the user supplied first.** Inventory files and what each can show; record sources as you use them.
2. **Write the research questions and hypotheses** being tested (including falsifiers).
3. **Search the most direct source first**: official statistics, regulators, company filings, original studies. Prefer primary documents over articles about them.
4. **Capture source metadata at the moment of use**: locator, publication date, data period, geography, population, method, access date.
5. **Trace to the original.** When an article cites a figure, find the original report; record lineage.
6. **Check definitions and scope** before comparing numbers.
7. **Search for credible conflicting evidence** (section 4).
8. **Summarise what the evidence can and cannot conclude**, with the smallest next validation step for important gaps.

If web access is unavailable, say so, work with supplied material, and list the sources you would check and why. Never fill gaps from memory as if verified; label remembered context as unverified and suggest verification.

## 4. Searching for disconfirmation

For each load-bearing claim or leading hypothesis, deliberately look for what would weaken it:

- Contradicting data for the same market and period.
- Different results in a comparable segment or region.
- Methodological critiques of the source.
- Alternative explanations that fit the same pattern.
- Evidence that the trend reversed or the conditions changed.

Useful query patterns (adapt to the tool): `"<claim>" criticism`, `"<claim>" methodology`, `"<category>" decline <market>`, `"<assumption>" evidence against`, `site:<official domain> <topic>`, `"<company>" annual report filetype:pdf`.

Record what you searched and found, including nulls when they matter ("no Tanzanian data found on X in NBS, TCRA or FSDT publications checked on <date>").

## 5. Competitor intelligence: what signals can and cannot show

Separate five things that are often confused:

| Signal | Can indicate | Cannot establish alone |
|---|---|---|
| Competitor claims (website, ads, press releases, CEO statements) | What they want to be believed; positioning intent | Truth of claims, customer perception, performance |
| Observed behaviour (price checks, pack changes, promotions, launches, hiring) | What they are doing | Why, or whether it works |
| Advertising activity (ad libraries, observed media, creative) | Presence, messages, rough intensity | Spend, reach, effectiveness (library coverage varies by platform and market) |
| Distribution and availability (store checks, audits, route-to-market) | Physical availability, shelf position | Sales velocity unless measured |
| Commercial performance (filings, audits, share data) | Revenue, share, margins where reported | Causes of performance |

Search visibility, backlinks, social activity and ad frequency are signals with limitations; they do not establish sales, share or profitability. Label competitor data by source and date; competitors change prices and campaigns quickly.

To test whether a competitor's winning tactic transfers, use the transfer test in [strategic-choice.md](strategic-choice.md).

## 6. Qualitative evidence

1. **Preserve provenance**: respondent or source ID, context (who, where, when, recruitment criteria), language, and translation status.
2. **Quote exactly.** A verbatim quotation must match the transcript. Mark translations as translated and by whom; preserve the original where possible (e.g. Kiswahili with an English gloss).
3. **Separate three layers**: what respondents said; what was observed they did; the analyst's interpretation.
4. **Code transparently**: note how many respondents expressed a theme and any who contradicted it. Counts in qualitative work describe the sample, not the population. Do not convert them into percentages for a market.
5. **Look for contradictions and edge cases**, not only the dominant theme.
6. **State the inference boundary**: themes suggest mechanisms; they do not establish prevalence, causality or segment size.
7. **Never invent** quotations, participants, motivations or cultural consensus. If a transcript is ambiguous, say it is ambiguous.
8. **In deliverables**, show each quotation with its respondent ID and a short descriptor (e.g. "P3, mother, Dar es Salaam"), the original language where available, and whether the translation was checked.

Switching interviews (asking about the sequence from first thought to purchase, what pushed people away from the old solution, what pulled them to the new one, their anxieties and habits) are a useful structure for demand questions. Ground every force in a quote or observed behaviour; mark inferred forces as inferred.

## 7. Surveys and quantitative research design

- Define the population and sampling frame; state who is excluded (e.g. no phone access, rural areas, non-users).
- Write questions that measure behaviour where possible, with defined recall periods.
- Plan subgroup bases before fieldwork; small bases produce unstable estimates.
- Plan weighting and its effect on precision.
- Pre-specify key analyses to avoid fishing; label exploratory findings.
- For translation, use back-translation or bilingual review and pilot the questionnaire in context.
- Design choice-based research (conjoint, price tests) before fieldwork; it cannot be retrofitted.

Analysis guidance is in [analytics.md](analytics.md).

## 8. Synthetic respondents and personas

Simulated respondents, AI-generated personas and synthetic survey outputs are ideation aids. They can generate hypotheses, draft discussion guides or stress-test messaging logic. They are not evidence of what real people in a market think or do, and must never be reported as validation, prevalence or willingness to pay.

## 9. Stopping rules

Stop and move on when any is true:
- Additional accessible evidence is unlikely to change the decision at the required confidence.
- The agreed effort or time budget is reached.
- The remaining uncertainty can only be resolved with new primary research or an experiment; specify it.

When stopping with gaps, state what is known, what is not, whether the gap could reverse the recommendation, and the smallest next step.

## 10. What not to do

- Count repeated coverage of one source as corroboration.
- Present a publication date as the data period.
- Use a regional or global figure as a local fact.
- Present competitor visibility as competitor performance.
- Run broad searches before reading supplied first-party data.
- Invent supplier costs, sample sizes from folklore, or respondents.
- Continue researching after the decision is already robust to plausible findings.
