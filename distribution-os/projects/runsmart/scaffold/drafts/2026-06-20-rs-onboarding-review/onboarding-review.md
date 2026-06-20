# RunSmart — Onboarding / Activation Review (rs-onboarding-001)

**Date:** 2026-06-20
**Skill used:** `.agents/skills/marketing/onboarding/SKILL.md`
**App:** RunSmart: AI Run Coaching (live v1.0.3, `com.runsmart.lite`)
**Gate context:** D7 retention gate dated 2026-06-24 (4 days out).
**Data source:** PostHog project "Running coach" (171597) — live funnel + retention, last 90 days. Flow grounded in the live native iOS code (`Features/Onboarding/OnboardingView.swift`, `Services/Analytics/AnalyticsEvents.swift`).

---

## Headline

**The binding constraint is volume, not onboarding design.** The 5-step onboarding flow is healthy (80% of those who start it finish, ~50s median). What's killing activation sits *around* it: 77% of users who open the app never start onboarding, and only 1 in 5 who get a plan ever log a run. And the whole thing runs on ~44 users in 90 days — too little to evaluate a D7 gate at all.

---

## The real funnel (last 90 days, PostHog)

| Step | Users | Conv. from top | Drop from previous |
|---|---|---|---|
| app_launched | 44 | 100% | — |
| onboarding_started | 10 | 23% | **−77%** ← biggest drop |
| onboarding_completed | 8 | 18% | −20% (healthy) |
| plan_generated | 5 | 11% | −38% |
| run_completed | 1 | 2% | **−80%** ← second biggest |

**D7 retention (app_launched → return):** effectively **0%**. The two largest single-day cohorts (10 users on 2026-05-28, 8 on 2026-06-10) had **zero** return by day 7. Sample is far too small to be conclusive, but there is no positive D7 signal in the data.

---

## What this means for the 2026-06-24 gate

The gate is, in practice, **un-evaluable** on current traffic. 44 first-time launches and 1 logged run over 90 days cannot produce a trustworthy D7 number. Passing/failing a retention gate now would be measuring noise. **Recommendation: re-frame the gate** — before D7 retention can mean anything, the top of the funnel (installs → onboarding-started → first run) has to carry enough volume. That makes the ASO install work (rs-aso-003 / WP-9) the prerequisite for the retention gate, not a parallel track.

---

## The onboarding flow (for reference — it is NOT the problem)

5 steps, fully instrumented (`onboarding_started`, `_step_completed`, `_completed`):
1. Goal (First 5K / 10K PR / Half / Marathon / Just Run More)
2. Runner experience (Getting started → Race focused)
3. Weekly rhythm (runs/week + preferred days)
4. Privacy (coaching tone + "Smart return reminders" toggle + Garmin/HealthKit preview + 21-Day Rookie Challenge callout)
5. Completion → "Open Today to see your first workout" → `plan_generated`

This converts 10→8 (80%) in ~50s. It is good. Do not redesign it.

---

## Findings → Impact → Recommendation → Priority

**F1 — 77% never start onboarding (44→10).** *Impact: the single largest leak.* The app opens onto a mandatory Apple Sign-In wall (`Features/Auth/SignInView.swift`) before any value is shown. Cold App Store visitors hit a login gate and bounce. *Recommendation: let the user reach the goal-picker (step 1) BEFORE forcing sign-in, and only gate plan-save behind auth — or, minimum, make the sign-in screen sell the value (one line + the same dark hero) instead of a bare button.* **Priority: P0 (highest in-app lever).**

**F2 — Plan→run collapse, 5→1 (20%).** *Impact: the actual D7 driver dies here.* Logging a first run is what predicts D7, but nothing drives the user from "plan generated" to "record a run." The completion screen points to Today, then stops. *Recommendation: end onboarding with a concrete first-run commitment ("Your first run is [Easy 3K] — start it now / remind me [day] 7am"), and default the "Smart return reminders" toggle ON (it's currently an opt-in buried in step 4). The local reminder is your cheapest D7 lever.* **Priority: P0.**

**F3 — No first-rating prompt.** *Impact: zero App Store ratings → ASO conversion ceiling (see rs-aso-003).* *Recommendation: fire `SKStoreReviewController` after the first completed run / first plan-week. Ties into WP-9 item 1.* **Priority: P1.**

**F4 — Volume.** *Impact: nothing above can be measured.* *Recommendation: ASO + install push (WP-9) is the prerequisite. Re-baseline this review once ≥100 onboarding_started/week exist.* **Priority: P0 (strategic).**

---

## Single highest-impact fix before the gate

If only one thing ships before 2026-06-24: **default "Smart return reminders" ON and add a first-run reminder at the end of onboarding (F2).** It's a small, low-risk change to `OnboardingView.swift` / notification scheduling, and the local return reminder is the most direct nudge toward the day-7 return that the gate measures. F1 (sign-in wall) is higher leverage but a bigger change; queue it next.

*No app code was changed by this review. All fixes require app work + founder approval. The funnel/retention numbers are live from PostHog project 171597 and will move as volume grows.*
