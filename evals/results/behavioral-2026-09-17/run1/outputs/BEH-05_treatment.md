# TV ROI: what this data can and can't support

## Bottom line

I can't give you a TV ROI figure from this file that would stand up in a budget review. I'd also advise against using the figure the data seems to give you.

There are two problems:

1. **There's no money in the file.** ROI needs your TV cost and the contribution each extra case earns. The file only has GRPs and cases, so the most I can calculate is extra cases per GRP.
2. **TV and season move in lockstep.** Every heavy-TV week is a high-season week, and every light-TV week is a low-season week. No week has heavy TV in low season or light TV at peak. So the data look the same whether TV is driving sales or TV was simply booked into the weeks when sales were going to rise anyway.

What you *can* defend now is a break-even argument plus a test that settles the question. Details below.

## What the data show

The file covers 16 weeks: 1,075 GRPs and 977,000 cases. There are no missing values and no duplicate weeks.

| Season | Weeks | Avg GRPs per week | Avg sales per week ('000 cases) |
|---|---|---|---|
| Low | 1–4, 14–16 (7 weeks) | 40 | 51.4 |
| Shoulder | 5–6, 12–13 (4 weeks) | 65 | 60.0 |
| High | 7–11 (5 weeks) | 107 | 75.4 |

- **GRPs and sales track each other almost perfectly** (correlation 0.998). A straight line fits every week to within about 1,300 cases: weekly sales ≈ 37,200 cases + 355 cases per GRP.
- **Season and TV are nearly the same variable.** The season labels alone explain 92% of the week-to-week movement in GRPs and 93% of the movement in sales.

## The tempting number, and why it won't hold

The straight line implies 355 extra cases per GRP. Over the 16 weeks that's about 381,000 cases, or "TV drove 39% of sales." Finance can take that apart with one question: *wouldn't sales have peaked in weeks 7–11 anyway?* The file can't answer it.

I tried several ways around the season problem:

| Reading | Extra cases per GRP | Implied TV cases over 16 weeks (vs. no TV) | What must be true |
|---|---|---|---|
| Straight line, no season adjustment | 355 (95% CI 342–368) | ~381k (39% of sales) | Season has no effect of its own |
| Adjusted for the three season bands | 319 (95% CI 277–360) | ~343k (35%) | Weekly weights *within* each band weren't planned around expected demand |
| Low-season weeks only | 250 (95% CI 111–389) | ~269k (28%) | Low-season weight differences had nothing to do with demand, and the same response holds at peak weights |
| TV just follows the seasonal curve | 0 | 0 | Weights were planned from the sales forecast |

Here's why the adjusted readings still aren't proof:

- **The season bands are too broad.** In high season, GRPs peak in week 9 (120) and so do sales (79,000 cases). In shoulder season, the weeks nearest the peak have both more GRPs and more sales. Within each band, TV still follows the same seasonal hump, so adjusting for the bands removes only part of the season effect.
- **The low-season weeks are the best clue in the file.** Demand looks flat in those weeks, and GRPs repeat a 40/35/45 pattern. If that pattern came from spot availability or a rotation, rather than expected demand, it works almost like a small natural test. But it rests on 7 weeks, a 10-GRP range and sales rounded to the nearest thousand cases, which is why the range is so wide. **Ask your agency how those weekly weights were set.**
- **You never had a week without TV.** The lightest week had 35 GRPs, so any "sales without TV" figure, including the 16-week totals above, goes beyond the data.
- **Anything else that follows the season gets credited to TV.** Price, promotions, distributor stocking, competitor activity and holidays aren't in the file. If these are sell-in (shipments to distributors) rather than sell-out figures, distributors stocking up before peak could create this pattern on its own.
- **Carryover and diminishing returns can't be measured here.** I tested whether last week's GRPs add anything. The effect was small and couldn't be separated from this week's GRPs. Sixteen weeks of such tightly linked data can't show either effect reliably.

One more check: a fit this tight (R² 0.996) is also what you'd see if the media plan had been built from the sales forecast. Confirm that both columns are actuals, not planned figures.

## How to defend the budget honestly

**1. Make a break-even case now.** Get two numbers from finance and your agency:

- **Cost per GRP in TZS.** Use actual billed spend including agency fees. Either list production separately or spread it across the period.
- **Contribution per case in TZS.** Take off trade and distributor margins, discounts and variable costs. Don't use revenue per case, because that overstates the return.

Then:

- **Break-even cases per GRP** = cost per GRP ÷ contribution per case
- **Short-term ROI** = (extra cases per GRP × contribution per case − cost per GRP) ÷ cost per GRP

Compare your break-even figure with the table above:

- **Below about 110 cases per GRP** (the low end of the most cautious reading): TV clears the bar even if roughly two-thirds of the link with sales is really seasonal. That's a strong, honest position, though still not proof.
- **Between about 110 and 250:** TV pays back only if the low-season clue holds. Defend the budget as conditional on the test below.
- **Above about 250:** TV pays back only on the readings most open to the season objection. Don't lead with ROI; lead with the test.

This counts short-term weekly sales only. It leaves out longer-term brand effects, which would raise the true return. It also ignores diminishing returns at peak weights, which would lower the return on the last GRPs you buy.

**2. Commit to a test that settles it.** From strongest to weakest:

- **Regional weight test, if your TV buy can be split by region.** Run heavier weight in some regions and lighter weight in matched regions. Measure regional sell-out or distributor sales, and use at least 8 weeks of earlier data to confirm the regions moved together before the test. Agree the decision rule up front, for example: keep current weight if the heavy regions beat their matched regions by at least the break-even cases per GRP.
- **Planned on/off variation, if the buy is national only.** In a low or shoulder period, alternate heavy and light two-week blocks on a fixed schedule that nobody adjusts to the sales forecast. Two-week blocks stop carryover from blurring the result. Testing in low season puts fewer sales at risk, but a low-season effect may not carry over to peak, so say so up front.
- **Better history in the meantime.** Two or more years of weekly data would show the same season at different TV weights. Add price, promotions, distribution and competitor TV, and a proper model becomes possible. It's still weaker evidence than a test.

**3. A line for the budget meeting:**

> "TV weight and sales move together very closely, and even within the same season, heavier TV weeks sold more: roughly 250–320 extra cases per GRP. Because we schedule TV into peak demand, we're not claiming that as proven ROI. At our cost per GRP, TV needs [X] cases per GRP to break even. We propose holding the budget while we run a [regional / on-off] test that gives a clean answer by [date]."

## What I need to finish the calculation

- Cost per GRP, or total TV spend for these 16 weeks
- Contribution per case
- Whether sales are sell-in or sell-out
- How the weekly GRPs were planned

Send the first two and I'll run the break-even and ROI scenarios straight away.

---

*How I checked this: every number comes from your file. I checked the file for gaps and duplicates, then ran regressions: all weeks together, with season bands, within each band, and with last week's GRPs added. I then reviewed the work myself against the skill's standards for evidence, cause and effect, commercial logic and measurement. Nobody else reviewed it.*
