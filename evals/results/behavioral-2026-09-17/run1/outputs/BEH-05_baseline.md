# TV ROI: what this data can and can't support

## Short answer

I can't calculate a TV ROI from this file yet, and the number it seems to show would be risky to defend:

1. **There's no spend or profit data in it.** ROI needs TV spend and margin per case. The file only has GRPs and cases, so the most I can estimate is **cases sold per GRP**.
2. **That volume estimate is probably too high.** You ran the most TV in exactly the weeks when seasonal demand was highest. So this data can't tell "TV sold more cases" apart from "we put TV where sales were going to be high anyway."

Finance will likely spot the second problem quickly. If you walk in with the headline figure, it will hurt TV's case more than an honest range would. Below is what the data does show, what you can safely say, and how to get a number that holds up.

---

## What the data shows

Over 16 weeks you ran 1,075 GRPs and sold 977k cases.

| Estimate | Cases per GRP | Share of 16-week volume credited to TV* | What it assumes |
|---|---|---|---|
| Simple fit of sales against GRPs (correlation 0.998) | ~355 | 39% (381k cases) | Season has no effect of its own |
| Same fit, allowing for season (low / shoulder / high) | ~320 | 35% (343k cases) | Changes in GRPs *within* a season aren't driven by demand |
| Low-season weeks only (7 weeks, 35–45 GRPs) | ~250 (roughly 110–390, statistically) | 27% (269k cases) | Same, on the cleanest part of the data |

*Cases per GRP × total GRPs, assuming the effect stays in a straight line all the way down to zero GRPs.

The direction is consistent: in every season, heavier weeks sold more. Weekly weight ranged from 35 to 120 GRPs, and the response doesn't obviously flatten at the top. But there are too few weeks to judge whether you've hit diminishing returns.

## Why these numbers won't hold up yet

- **TV weight follows the season.** You averaged 40 GRPs a week in low season, 65 in shoulder and 107 in high. About 92% of the swing in weekly GRPs is simply the season changing, so TV and season are nearly impossible to separate.
- **The simple fit implies you have no seasonality.** At 355 cases per GRP, TV gets credit for the whole high-season lift. Without TV, high-season weeks would sell only about 200 cases more than low-season weeks. Even allowing for season, the season itself is worth only about 2,600 cases a week (~5%). **Does that match what you know about this category?** Think harvest cash flow, holidays, weather, trade restocking. High season is about 24k cases a week above low season. Any part of that gap you think the season would have delivered anyway should come off TV's credit.
- **You never ran a light week.** The lowest weight was 35 GRPs. No week in the data shows sales with little or no TV, so the "no-TV" sales level (~37–41k cases a week) is a guess beyond the data, not something you observed.
- **There's no lingering TV effect.** Sales dropped back the moment GRPs dropped. Weeks 14–16 look the same as weeks 1–3, even right after a nine-week heavy flight. TV usually keeps working for a while after it airs. When it doesn't seem to, that often means sales and GRPs are both just following the calendar.
- **Other sales drivers aren't in the file.** There's no price, promotions, distribution, competitor activity or other media. If any of these also rose in high season, their effect is currently counted as TV. And 16 weeks is a very small sample.

## How to turn this into ROI once you have the inputs

**TV ROI = (extra cases from TV × contribution margin per case − total TV cost) ÷ total TV cost**

- Use **contribution margin per case**, after distributor/retailer margins and VAT. Don't use revenue.
- Count **total TV cost**: airtime plus production and agency fees.
- A quicker test: **break-even cost per GRP = cases per GRP × margin per case.**

*Illustrative only.* This assumes TZS 3,000 contribution per case; swap in your real figure:

| Cases per GRP | Break-even total cost per GRP |
|---|---|
| 250 (cautious) | TZS 750,000 |
| 320 (allowing for season) | TZS 960,000 |
| 355 (simple fit) | TZS 1,065,000 |

- **If your real total cost per GRP is below the cautious line:** TV pays back even on the most conservative reading. That's a much stronger argument than any single ROI figure.
- **If it only pays back at the 355 line:** the case depends on the estimate most likely to be inflated.

## What you can safely say in the budget meeting

- "Sales and TV weight move together very closely. Even within the same season, heavier weeks sold more: roughly 250–360 cases per GRP."
- "That fits with TV working. But because our TV plan follows the season, we can't yet pin down exactly how big the effect is. At our cost per GRP, TV [pays back / breaks even] even at the cautious end." *(Fill in once cost and margin are in.)*
- "We're running a test next low season to get a clean number."

Avoid saying "TV drives 35–40% of our volume." It's the easiest claim to knock down.

## How to get a number that holds up

1. **This week: cost and margin.** Send weekly TV spend (or total cost per GRP) and contribution per case. I'll turn the ranges above into an ROI range.
2. **This month: more history.** Pull 2–3 years of weekly sales and GRPs, plus price, promotions and distribution. **Last year's sales for the same weeks** is the most useful addition, because it shows the seasonal pattern independently of this year's TV plan. Any period when TV was scheduled differently is especially valuable.
3. **Next low season: run a test that separates TV from the season.**
   - **Option A:** halve the weight, or go off air, for 3–4 weeks. Compare those weeks with the same weeks last year and the weeks around them.
   - **Option B:** if you can buy or measure by region (regional stations, distributor-level sales), hold one comparable region back instead. This gives a cleaner result.
   - **The cost is limited.** Going off air for three weeks at 40 GRPs risks about 30–43k cases on current estimates (roughly half that if you halve the weight), partly offset by the airtime you don't pay for. In return you get a TV number nobody can argue with at the next budget round.
