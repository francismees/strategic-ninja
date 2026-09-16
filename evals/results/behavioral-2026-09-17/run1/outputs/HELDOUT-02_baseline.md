# I'd switch the refill-reminder SMS on at all 40 branches

My recommendation is to switch it on across all 40 branches now, in fast waves over about 5 weeks. We don't need another pilot.

The test is clean and the effect is large. The payback is so lopsided that it would still be worth doing if the real effect were a small fraction of what we measured. The risks are in running it (refill-date data, stock and privacy), not in whether it works.

---

## Why

### 1. The result holds up

- **The test design is strong.** Patients were randomised, with 4,200 in each group, over 3 refill cycles. The result held in all four cities.
- **Refills went up 23.5%.** Reminded patients completed 2.31 refills each, against 1.87 without reminders.
- **Far fewer patients stopped refilling.** The share with zero refills fell from 17% to 9%. The margin of error on that 8-point gap is roughly ±1.4 points, so it isn't noise.
- **Patients didn't mind.** Only 0.6% asked to opt out.

### 2. The money works even if the real effect is much smaller

| Per patient, per 12 weeks | |
|---|---|
| Extra refills | 0.44 |
| Extra gross margin (0.44 × TSh 36,000 × 24%) | **TSh 3,800** |
| SMS cost (3 messages × TSh 30) | TSh 90 |
| Return on SMS spend | **~42 : 1** |

**Full network, per year (31,000 opted-in patients):**

| Scenario | Gross margin added | SMS cost | Net |
|---|---|---|---|
| Pilot effect holds | TSh 511M | TSh 12M | **TSh 499M** |
| Half the effect | TSh 255M | TSh 12M | TSh 243M |
| A quarter of the effect | TSh 128M | TSh 12M | TSh 116M |

- **Break-even is tiny.** SMS costs are covered at 0.01 extra refills per patient per 12 weeks, which is about 2% of the lift we measured.
- **Longer messages don't change the answer.** If Swahili messages run to two SMS parts (TSh 180 per patient), the return is still about 21:1.
- **Setup costs pay back fast.** Integration and training would pay for themselves within weeks.
- **These figures leave out retention.** About 8% more patients stay active instead of lapsing (roughly 2,500 across the network). Their value after the 12 weeks isn't counted above.

### 3. Waiting costs money

About 27,000 opted-in patients get no reminder today. That figure assumes the pilot's reminder group is still switched on. Each week of delay gives up roughly **TSh 8–10M of gross margin**, and some of the patients who lapse won't come back.

---

## What could make this wrong, and how to protect against it

| Risk | Why it matters | Safeguard |
|---|---|---|
| **The other 28 branches may respond less well** | All 12 pilot branches are in major cities. Branches in smaller towns may have weaker patient data, different phone access or different habits. | A small, time-limited control group in the new branches (see below). The case still works if the effect is cut by 75%. |
| **Some of the lift may be timing, not new sales** | A 12-week window misses control patients who refilled late but did refill. | Before Monday, the analyst compares refills in August and September for both groups (the data already exists). If the control group caught up, lower the forecast. The halving of zero-refill patients suggests most of the lift is real. |
| **The random split may not be clean** | Splitting by patient ID ranges (not odd/even or random) could mix up long-standing and newer patients. | Confirm both groups had the same refill rates *before* May. |
| **Refill due dates may be wrong outside the pilot** | A reminder at the wrong time is noise at best, and at worst a reason to opt out. | Check each branch before switching it on: days' supply recorded at dispensing, and valid phone numbers. |
| **Stock-outs** | Expect about 1,000–1,100 extra chronic refills a week, around 28 per branch. A reminded patient who finds no metformin or amlodipine is a lost sale and a health risk. | Give procurement the expected extra demand by product before each wave, and review stock-out logs from the pilot branches. |
| **The margin assumption may be too high** | The extra refills may be smaller baskets, or insurance-paid (NHIF or private) with a different margin and slower cash. | Recalculate using the actual extra refills. This is unlikely to reverse the decision. |
| **Privacy** | Health data is sensitive personal data under the Personal Data Protection Act 2022, and family members often share phones. | The message must not name the condition or the medicine. Compliance should confirm the opt-in wording covers reminders and that the SMS provider has proper data-processing terms. |
| **Promotion rules** | A reminder that pushes offers could be treated as promoting medicines. | Keep it a pure service message, with no discounts and no product names. |
| **Expired prescriptions** | Reminders will bring back patients whose prescription is due for renewal. | Flag those patients so the pharmacist refers them for a clinic review instead of dispensing on an expired prescription. |

---

## Rollout plan

1. **Week 1: pilot branches.** Switch on reminders for the 4,200 control patients at the 12 pilot branches. The system is already proven there.
2. **Weeks 2–5: the other 28 branches.** Roll out in two waves. Each branch goes live only after the data, phone-number and stock checks above.
3. **Same message.** Use the exact tested text. Any rewording is untested, so if we want better wording, A/B test it after launch.
4. **Control group.** In the 28 new branches, hold back reminders from 5% of patients (about 1,100) for 12 weeks, then switch them on.
   - This confirms the effect carries over beyond the four pilot cities and shows whether it fades as patients get used to the messages.
   - It costs about TSh 4M in margin.
   - It's time-limited, so we aren't withholding an adherence aid for good.
5. **Monthly tracking, by branch:**
   - refills per patient
   - share of patients with zero refills
   - opt-outs
   - SMS delivery rate
   - stock-outs on reminded products

---

## Before Monday (a few hours of analyst time)

- **Pre-May check:** did both groups have the same refill rates before the test?
- **Catch-up check:** did the control group catch up in August and September?
- **Margin check:** what were the actual basket size and margin on the extra refills (cash vs insurance)?
- **Stock check:** were any reminded patients turned away because of stock-outs?

None of these is likely to change the decision. They firm up the forecast figure the MD will quote.

---

## What to ask the meeting to decide

1. **Approval** to send the tested reminder to all opted-in hypertension and diabetes patients at all 40 branches.
2. **Budget** of about TSh 12M a year for SMS (up to about TSh 24M if messages run to two parts), plus one-off setup.
3. **Owners:**
   - Ops: branch checks and stock
   - Analyst: control group and monthly tracking
   - Compliance: consent and message wording
4. **The next opportunity.** With reminders on, each opted-in patient is worth about TSh 16,000 a year in net margin. That easily justifies a push at the counter to sign up chronic-care patients who haven't opted in. That's probably worth more than the switch-on itself.
