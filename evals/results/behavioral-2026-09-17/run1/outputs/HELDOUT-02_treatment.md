# Refill-reminder SMS: recommendation for Monday

## The call

**Yes. Switch it on for all 40 branches.** Do it as a fast rollout in waves over the next 4–5 weeks, not as another test. Keep a small holdout group for 6 months and agree a few guardrails.

This is about as clean as commercial evidence gets. The upside is big and the cost is tiny. What's left to worry about is running it well, not whether it works.

## Why

**1. The evidence is solid.** Patients were randomly assigned, there were 8,400 of them over three refill cycles, and the result held in all four cities. It was also tested on the same group you'd roll out to: opted-in chronic-care patients.

| 12 weeks | Reminder | Control | Difference |
|---|---|---|---|
| Refills per patient | 2.31 | 1.87 | +0.44 (+24%) |
| Share of due refills collected (if 3 were due) | ~77% | ~62% | +15 pts |
| Patients with zero refills | 9% | 17% | −8 pts (nearly halved) |
| Opt-outs | 0.6% | – | about 25 patients |

The analyst's p<0.001 holds up. I checked the zero-refill numbers myself: the 95% confidence interval runs from 6.6 to 9.4 fewer patients per hundred with no refill. It isn't a close call.

**2. The economics are lopsided.**
- **Per patient, per 12 weeks:** 0.44 extra refills × TSh 8,640 gross margin per refill is **about TSh 3,800 of extra gross margin**. Three reminders cost **TSh 90**. That's roughly TSh 42 of margin for every TSh 1 spent on SMS.
- **Break-even:** 0.01 extra refills per patient, **about 2% of the effect we measured.** The effect could be 40 times smaller and still pay. Even if the extra refills were half-size baskets *and* the effect were half as big, you'd get about TSh 950 of margin per patient against TSh 90 of SMS.

Network-wide, per year: my estimate for 31,000 patients, one SMS per refill cycle, extra refills at the average basket, before any setup cost or staff time.

| If the real effect is... | Extra refills/yr | Extra revenue | Extra gross margin | SMS cost |
|---|---|---|---|---|
| As in the pilot (+0.44) | ~59,000 | ~TSh 2.1bn | ~TSh 510M | ~TSh 12M |
| Half | ~30,000 | ~TSh 1.1bn | ~TSh 255M | ~TSh 12M |
| A quarter | ~15,000 | ~TSh 530M | ~TSh 128M | ~TSh 12M |

**3. Waiting costs money.** If the pilot result holds, every week without reminders gives up roughly TSh 8–10M of gross margin. Hypertension and diabetes patients also keep missing refills they would otherwise have collected.

## What could make the gain smaller (none of it changes the call)

- **Earlier pickups vs. patients who actually stopped.** A 12-week window can count refills that were simply collected earlier. The drop in zero-refill patients says much of the gain is real. The pilot ended in July, so August–September data will show whether control patients "caught up". Ask the analyst to check.
- **The effect may fade.** 12 weeks can't show whether it lasts. The holdout below will.
- **The other 28 branches.** Their locations, patient data and systems weren't part of the pilot. Similar results across Dar es Salaam, Dodoma, Mwanza and Mbeya are encouraging. Still, each branch should go live only once its data checks out.
- **Only hypertension and diabetes were tested.** If the 31,000 includes other chronic conditions, switch them on too, because the economics still work. Track them as a separate group. For sensitive conditions, first confirm consent and neutral message wording.
- **Assignment by patient ID.** Ask the analyst to confirm both groups had similar refill histories before the pilot started.

## How to roll it out

1. **Pick the holdout first.** Randomly set aside 5% of patients across all branches (~1,550) for 6 months, then switch them on too. That group is big enough to show if the effect halves, and it costs about TSh 13M of gross margin. If the MD isn't comfortable holding reminders back from patients, drop it and compare the rollout waves instead. That comparison is weaker.
2. **Week 1:** switch on (or keep on) everyone in the 12 pilot branches, since the system already works there.
3. **Weeks 2–5:** bring in the other 28 branches in 2–3 waves. A branch goes live when:
   - its phone numbers and refill due dates have been checked
   - a test batch of SMS has been delivered
   - its main hypertension and diabetes lines are in stock

   At pilot rates, reminders add about 4 refills a day at an average branch, so stock matters more than staff time. A reminder that sends a patient to an empty shelf is worse than no reminder.
4. **Don't change the message while you scale.** Use the exact pilot wording. Keep condition and drug names out of the text. Confirm the opt-in consent covers these reminders at every branch.

## Guardrails (suggested, for the meeting to agree)

| Watch | Trigger | Action |
|---|---|---|
| SMS delivery rate, by branch | Below 90% | Fix the phone data before continuing in that branch |
| Opt-out rate | Above 2% (over 3× the pilot) | Review the wording and timing |
| Reminded patients who find their medicine out of stock | A repeated pattern at any branch | Fix stock ordering for chronic-care lines |
| Extra refills vs. the holdout, at 12 and 24 weeks | Below 0.10 per patient | Refresh the message. Below 0.01 (break-even), stop |

## Before Monday, ask the analyst for

- The confidence interval on the +0.44 refill difference, not just the p-value.
- Whether both groups had similar refill histories before the pilot.
- The August–September catch-up check.
- How many SMS were actually billed and delivered, to confirm the TSh 90 per patient. If the message runs to two SMS parts, the cost doubles, which still doesn't matter.

These make the value estimate more precise. They shouldn't hold up the decision.

## After rollout

Even with reminders, 9% of patients didn't collect a single refill. The next thing to test is a second SMS or a pharmacist phone call for anyone who hasn't refilled 5–7 days after their due date. Test it the same way the reminders were tested, with a randomly chosen comparison group.

---

**One line for the meeting:** "In a randomised pilot with 8,400 patients, SMS reminders raised refills by 24% and nearly halved the share of patients with no refill at all. Every TSh 1 of SMS brought back about TSh 42 of gross margin. We recommend rolling out to all 40 branches over five weeks, holding back 5% of patients for six months to confirm the effect lasts, and watching SMS delivery and stock."
