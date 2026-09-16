# Tanzania market module

Use this module whenever the target market is Tanzania (Mainland, Zanzibar or any part of either), or when evidence from elsewhere is being applied to Tanzania. It is the default local specialisation; do not impose it on unrelated markets. Market applicability labels are defined in [../references/evidence-model.md](../references/evidence-model.md). Sources: [tanzania-sources.md](tanzania-sources.md). Dated verified observations: [tanzania-observations.json](tanzania-observations.json).

This module holds reasoning rules and source policy, not a static fact pack. Statistics belong in dated source and claim records that can be refreshed.

## Contents
1. Market module contract (for replacing or adding markets)
2. Scope distinctions
3. Classifying local propositions
4. Transferring evidence from elsewhere
5. Analytical safeguards
6. Culture and language
7. Formal and informal trade
8. Refreshing local facts
9. Worked safeguard examples

## 1. Market module contract

A market module (this one, or one written for another country) provides:
1. Scope distinctions that matter for analysis in that market.
2. A source registry with verified routes, formats, access conditions and pitfalls.
3. Dated observation records with definitions, scope and review conditions.
4. Analytical safeguards specific to the market's data.
5. Culture and language validation rules.
To add a market, create `markets/<country>.md`, `markets/<country>-sources.md` and `markets/<country>-observations.json` with the same structure, and add them to the module map in `SKILL.md`.

## 2. Scope distinctions

Specify the scope of every material local claim. Distinguish, whenever relevant:

- **Country vs Mainland vs Zanzibar.** Statistics may cover the United Republic, Mainland only or Zanzibar only. The NBS national CPI covers Mainland; Zanzibar's CPI is published by OCGS (see observations file). Do not merge them silently.
- **Region and city.** Dar es Salaam, Arusha, Mwanza, Dodoma, Mbeya, Zanzibar Town and rural districts are not interchangeable in income, channel structure, language use, infrastructure or competition.
- **Urban vs rural**, and within urban areas, central vs peri-urban.
- **Income, life stage and household context** — only with evidence for the relevant group.
- **Category, channel and occasion** — a statistic about one category or channel does not describe another.
- **Measure and unit** — people, households, adults 15+, adults 16+, subscriptions, SIMs, accounts, active users, outlets.

## 3. Classifying local propositions

Every important proposition used for a Tanzanian decision gets a market applicability status with a scope and reason:

| Status | Use when | Example (illustrative) |
|---|---|---|
| Local verified | Direct evidence for the stated local scope | NBS Mainland CPI figure for a given month |
| Local supported | Local signals support it but not definitively (small base, partial coverage, indirect) | Twelve interviews in Dar es Salaam suggesting a pack-size preference |
| Regional proxy | Evidence from a comparable market (Kenya, Uganda, Rwanda...) | A Kenyan mobile-commerce adoption study |
| Global hypothesis | Mechanism or finding from elsewhere, untested here | A European price-elasticity finding |
| Unknown | Insufficient evidence | Size of an informal sub-channel with no measurement |

"Locally verified" means direct evidence supports the stated scope. It does not mean universally certain or true for other regions, categories or periods.

## 4. Transferring evidence from elsewhere

When a global or regional finding is proposed for Tanzania:

1. **Use direct local evidence first when it exists.** Do not force a global → regional → local detour when local evidence already answers the question.
2. **Identify the mechanism.** Why did it work there (income, infrastructure, retail structure, regulation, culture, competition)?
3. **Check whether the enabling conditions hold** in the Tanzanian scope in question.
4. **Use regional comparison only if it helps** explain or bound the mechanism.
5. **Assess fit**: cultural and language fit; commercial fit (price points, margins, channel economics, payment methods); infrastructure fit (power, cold chain, connectivity, logistics).
6. **Label the status** (regional proxy or global hypothesis) and specify the **local validation** needed — the smallest test, data source or research that would confirm or reject transfer.

Never import evidence from Nairobi as evidence about Dar es Salaam, or Kenyan Sheng as Tanzanian youth language, without local justification.

## 5. Analytical safeguards

1. **Subscriptions are not people.** Subscriptions, SIMs, devices, accounts, registered users, active users and unique people are different measures. TCRA counts subscriptions (SIMs used at least once in 90 days, including machine-to-machine SIMs) and reports penetration above 100%. Mobile money figures are accounts, not unique users. Do not convert these into audience reach. Smartphone or device ratios do not automatically equal target-audience reach either: ownership, sharing, access, data affordability and usage for the relevant task all matter.
2. **National averages do not settle segment questions.** Do not rule out an app, e-commerce route, premium proposition or modern trade opportunity solely from aggregate national data. The relevant question is whether the target segment, in its locations and occasions, has the access, income and behaviour required. Seek segment evidence or make a proportionate conditional judgement with a validation step.
3. **Category and channel scope.** A reported food-retail share for informal outlets does not describe all retail categories, all regions or the brand's own channel mix. Check what was measured, where, by whom and how.
4. **Inflation is not cost exposure.** Headline or divisional CPI does not by itself establish a company's cost exposure, its buyers' price response or the correct pricing and pack response. Those need the company's cost structure, price elasticity evidence and channel data.
5. **Publication date is not data period.** Surveys can be published years after fieldwork (for example, the last full Household Budget Survey fieldwork was 2017/18). Record both.
6. **Official and commercial figures can diverge.** Subscription-based and survey-based internet measures differ by definition. Cite which one and why it fits the decision.
7. **Secondary coverage is not a new source.** News and investment-portal articles often restate NBS, TCRA or BoT releases. Trace to the original; count one lineage.

## 6. Culture and language

- Cultural themes are **research lenses, not permanent consumer truths**. A theme becomes usable evidence only with local data for the relevant audience and category.
- Mobile money, informal trade, music, football, religion, family, community and social aspiration enter an analysis **only when relevant to the decision and evidenced**. A list of familiar references is not local expertise.
- **Kiswahili register** (formal, conversational, youth or regional usage) must be validated in context with native speakers from the target audience. Mark translations and copy that has not been locally reviewed.
- Do not assume Sheng, Nairobi slang or Kenyan cultural references apply. Tanzanian urban vernacular has its own forms; validate them locally.
- Religion and community norms may affect categories such as alcohol, finance, food and media; treat them with evidence and respect, never as caricature.
- Avoid homogenising "African consumers" or "Tanzanian consumers". Specify who.

## 7. Formal and informal trade

- Neither formal nor informal trade is homogeneous. Informal trade includes dukas, kiosks, mama lishe food vendors, street vendors (machinga), wholesalers and open markets, with different credit terms, pack needs, stock levels, cold chain and ordering patterns. Formal trade includes supermarkets, pharmacies, petrol forecourts, e-commerce and institutional buyers.
- Ask what share of *this category's* sales, *in these regions*, flows through each channel, and what evidence establishes it (audit coverage often under-represents informal outlets).
- Physical availability analysis should reach outlet level where data allow: numeric and weighted distribution, out-of-stocks, chilled availability, price at shelf, and route-to-market (direct, distributor, wholesaler, van sales).
- Payment and credit practices (cash, mobile money, supplier credit) can shape pack sizes, price points and ordering frequency; establish them with evidence for the channel in question.

## 8. Refreshing local facts

- Refresh a material statistic when its age, changed conditions or decision sensitivity requires it. Monthly CPI and quarterly TCRA data age fast; census data age slowly for structure but not for digital behaviour.
- Check the source route in [tanzania-sources.md](tanzania-sources.md); record access date, locator and data period.
- When access fails (site down, gated data), keep the previous dated record, label the limitation, and say what could not be refreshed. Never update from memory.
- Observations in [tanzania-observations.json](tanzania-observations.json) include review conditions; treat them as expired once those conditions pass.

## 9. Worked safeguard examples

**SIMs presented as people.** A brief says "117 million Tanzanians have mobile phones, so SMS reaches everyone." TCRA's June 2026 report counts about 117 million telecom subscriptions — SIMs used in the past 90 days, including machine-to-machine SIMs — while the World Bank's 2025 population estimate is about 70.5 million. The subscription count exceeds the population because people hold multiple SIMs and devices hold SIMs. Correct statement: subscription counts show widespread mobile connectivity but cannot establish how many unique people, or which target audience, an SMS campaign reaches. Next step: use unique-reach data from the chosen operator or platform, or survey-based phone access for the target group. (Figures and locators: observations file.)

**National average used to reject a segment opportunity.** "Smartphone use is low nationally, so an app for pharmacy restocking will fail." The decision concerns pharmacy owners in urban centres, a segment whose smartphone access and data use may differ sharply from the national average. Proportionate judgement: the national figure does not settle it; check device and connectivity among target pharmacy owners (a short field check of 30–50 outlets would do), and consider a USSD or WhatsApp-based fallback to keep the route robust.

**Kenyan evidence used for Tanzania.** A Kenyan study shows strong uptake of a buy-now-pay-later product among urban informal traders. Status: regional proxy. Transfer test: similar mechanism (cash-flow gaps) is plausible, but credit regulation, mobile money provider features, trader credit practices and default risk may differ. Validation: small pilot with Tanzanian traders and a partner provider, measuring uptake and repayment.

**Inflation used to prescribe shrinkflation.** "Transport inflation is 13.8%, so we must cut pack sizes." The divisional CPI figure is verified for Mainland August 2026, but it does not establish the company's distribution cost share, pass-through, competitors' responses or shoppers' reactions to smaller packs. Next step: cost-structure analysis, price-pack ladder review by channel and a pack or price test.
