# Business + GTM Plan v0 - RunSmart iOS & Resumely iOS

Date: 2026-06-02 IDT
Owner: Nadav (solo founder)
Status: v0 planning artifact. Planning only - no product repo changes. No financial, App Store, PostHog, conversion, CAC, or LTV numbers are invented.

## How To Read This Document

Every claim is tagged so you can tell evidence from guess:

- **[FACT]** - sourced from a file in this OS or a logged decision. Source named where useful.
- **[ASSUMPTION]** - a reasonable working hypothesis, not yet validated. Treat as directional.
- **[MISSING]** - data we do not have and need before acting.
- **[DECISION]** - a choice the founder must make; not resolvable from current files.

Sources read: `DASHBOARD.md`, `PROJECT-STATUS.md`, `PROJECTS.md`, `PROJECT-PATHS.md`, `dashboard/status.json`, `PROJECT-BRIDGES/runsmart-ios.md`, `PROJECT-BRIDGES/resumebuilder-ios.md`, `PROJECT-BRIDGES/runsmart-distribution.md`, `PROJECT-BRIDGES/resumebuilder-distribution.md`, `GLOBAL-WORKFLOWS.md`, `GLOBAL-STANDARDS.md`, `GLOBAL-TASTE.md`, `distribution-os/distribution-context.md`, `distribution-os/first-4-week-plan.md`, `distribution-os/channel-backlog.md`, `distribution-os/metrics-dashboard.md`, `distribution-os/projects/runsmart.md`, `distribution-os/projects/resumebuilder.md`, `executive-os/CEO-OS.md`, `executive-os/CFO-OS.md`, `executive-os/EXECUTIVE-METRICS.md`, `executive-os/EXECUTIVE-DASHBOARD.md`, `executive-os/EXECUTIVE-DECISIONS.md`, `executive-os/EXECUTIVE-BACKLOG.md`, `DECISIONS.md`, `OWNER.md`.

Brand vs repo naming (per `GLOBAL-TASTE.md`): the product brand is **Resumely**; the repo is **ResumeBuilder iOS**. Brand name in product voice, repo name in code paths.

---

# 1. Executive Summary

**Where the business stands today.** [FACT] Two iOS apps are at the App Store gate and neither is live. RunSmart iOS v1.0 build 6 is in App Store review context and is frozen; Resumely iOS is pre-submission, having cleared analytics and UX/export gates on 2026-06-01, and now needs an authenticated real-device smoke followed by an App Store Connect upload (`PROJECT-STATUS.md`, `EXECUTIVE-DASHBOARD.md`). [FACT] There is no revenue, no live funnel data, and no monetization wired anywhere in the portfolio; every financial cell in the Executive OS is `Needs Data` (`EXECUTIVE-METRICS.md`, `CFO-OS.md`). [FACT] PostHog is integrated in both iOS apps, but live event receipt is unverified for RunSmart and unverified-in-production for Resumely (`EXECUTIVE-BACKLOG.md` analytics-sprint-001/002, EXD-002/004).

**The single gate.** [FACT] Shipping is the one constraint blocking everything downstream - revenue, activation data, and distribution all depend on at least one app being live (`CEO-OS.md` OKR 1). Until then, business and GTM planning is preparation, not execution.

**What the next 30 days should achieve.**
1. Get Resumely iOS submitted (device smoke → ASC upload → submit).
2. Get RunSmart iOS through Apple review without mutating v1.0 artifacts.
3. Confirm PostHog events actually land for both apps so day-1 cohorts are not blind.
4. Stand up the **first ASO listings** for both apps (the #1 acquisition channel for both per `channel-backlog.md`), ready to publish on approval.
5. Resolve two business decisions that are currently blocking all monetization thought: **the monetization model** and **whether the two apps share any brand/distribution assets**.

The 30-day objective is not revenue. It is **"both apps live (or in review) with verified analytics and ASO listings ready, and the monetization model decided."** Revenue experiments cannot start until there is a live listing and a funnel to read.

---

# 2. Product Portfolio Strategy

## RunSmart iOS

| Field | Value |
|---|---|
| Role in portfolio | **[FACT]** Primary product; premium native mobile coach (`CEO-OS.md`, `PROJECTS.md`). |
| Target user | **[FACT]** Beginner-to-intermediate runners; Garmin / Apple Watch / Strava owners; goal-anchored (5K–marathon) or habit-anchored (`distribution-os/projects/runsmart.md`). |
| Core problem | **[FACT]** Static one-size training plans don't adapt to the runner's real life, recovery, or progress (`distribution-os/projects/runsmart.md`). |
| Product promise | **[FACT]** Adaptive coaching that responds to your actual life: adaptive plan generation, post-run debrief, readiness check, race strategy (`distribution-context.md`). |
| Strategic value | **[ASSUMPTION]** Highest-conviction product; defensible via adaptive logic + integrations moat; founder's primary focus. |
| Revenue potential | **[MISSING]** No pricing, no conversion data. Subscription-shaped category, but unquantified. |
| Current readiness | **[FACT]** v1.0 build 6 in review context, frozen; 1.0.1 fast-follow spec exists (`PROJECT-STATUS.md`). |
| Main blocker | **[FACT]** Apple review outcome (external, out of our control). |
| Recommended priority | **[FACT]** Primary. Do not split focus during the submission sprint (`CEO-OS.md` focus rules). |

## Resumely iOS

| Field | Value |
|---|---|
| Role in portfolio | **[FACT]** Secondary native app (`CEO-OS.md`, `PROJECTS.md`). |
| Target user | **[FACT]** Active job seekers, career switchers, people polishing a resume for a specific role; mobile-first; English primary, Hebrew secondary (`distribution-os/projects/resumebuilder.md`). |
| Core problem | **[FACT]** Resumes fail ATS parsing and aren't tailored to the specific job, costing interviews (`distribution-os/projects/resumebuilder.md`). |
| Product promise | **[FACT]** Paste a posting, tailor in minutes, export from your phone; ATS-aware optimization + templates that parse (`distribution-os/projects/resumebuilder.md`). |
| Strategic value | **[ASSUMPTION]** Faster value loop (one resume = immediate output) and a transaction-shaped need; useful portfolio diversifier against RunSmart's habit-formation curve. |
| Revenue potential | **[MISSING]** No pricing, no conversion data. Transaction/subscription hybrid is plausible but unquantified. |
| Current readiness | **[FACT]** Pre-submission; cleared analytics + UX/export gates 2026-06-01; needs device smoke + ASC upload (`PROJECT-STATUS.md`). |
| Main blocker | **[FACT]** Authenticated real-device smoke + ASC upload path (Fastlane vs manual portal) (`DASHBOARD.md` Decision Board). |
| Recommended priority | **[FACT]** Secondary; kept behind RunSmart for time (`CEO-OS.md`). But it is **closer to a submit action** this week than RunSmart is. |

## Portfolio Questions

- **Which app is primary?** **[FACT]** RunSmart. Settled across `CEO-OS.md`, `PROJECTS.md`, `OWNER.md`. Not re-opened here.
- **Which app is secondary?** **[FACT]** Resumely.
- **Nuance worth naming:** **[ASSUMPTION]** Although RunSmart is the strategic primary, Resumely is the nearer-term *shippable* app this week (RunSmart is frozen waiting on Apple). The right read is "RunSmart owns strategic priority; Resumely owns this week's submit action." These do not conflict - one is a focus rule, the other is a queue position.
- **Should they share brand/distribution assets or stay separate?** **[DECISION]** The OS treats them as separate products with separate audiences and separate distribution files (`distribution-context.md`, both bridges). **Recommendation: keep brand and audience separate, share only the operating layer** (Distribution OS workflows, ASO skill, lifecycle email backbone, analytics conventions, Executive OS). There is no audience overlap between runners and job seekers, so a shared brand would dilute both. This is consistent with current OS structure; the decision is to *ratify* it, not change it.

---

# 3. Business Plan v0

## RunSmart iOS

- **Business model options** - **[ASSUMPTION]** (a) Freemium subscription (free plan + paid adaptive coaching/insights), (b) free trial → subscription, (c) one-time unlock. Category norm leans subscription. **[DECISION]** Not chosen yet.
- **Target customer** - **[FACT]** Beginner-to-intermediate goal/habit runners with a wearable.
- **Value proposition** - **[FACT]** A calm coach that adapts to your life and tells you the one next thing to do (`GLOBAL-TASTE.md` RunSmart profile).
- **Pricing assumptions** - **[MISSING]** No price point exists in any file. Do not assume one.
- **Monetization readiness** - **[FACT]** Not ready. No paywall, no IAP/subscription wired, no RevenueCat (`CFO-OS.md` all `unknown`).
- **First possible paid feature** - **[ASSUMPTION]** Adaptive plan regeneration + post-run debrief depth, gated behind a paywall after a free first plan. Validate before building.
- **What not to monetize yet** - **[ASSUMPTION]** First plan generation, the readiness check, and the basic run log. These are the activation moment; gating them kills the funnel before it produces data.
- **Key costs** - **[MISSING]** AI/API (OpenAI), Supabase, hosting, PostHog - all `unknown - need: provider billing` (`CFO-OS.md`).
- **Required metrics** - **[FACT]** D7 activation (install → run_completed), WAU, plan adherence, App Store conversion (`metrics-dashboard.md`, `CEO-OS.md` OKR 2).
- **Main business risks** - **[ASSUMPTION]** Subscription fatigue in fitness; integration dependency (Garmin/Apple); activation cliff if onboarding is heavy.
- **30-day business objective** - Live or approved on App Store with verified analytics and an ASO listing ready. No monetization yet.
- **90-day business objective** - **[FACT/ASSUMPTION]** Read first-cohort D7 activation (OKR 2 target ≥30%, directional), then decide whether to turn on a paywall.

## Resumely iOS

- **Business model options** - **[ASSUMPTION]** (a) Pay-per-export/credit, (b) subscription for unlimited tailoring, (c) freemium (free score, paid optimized export). The "score free, pay to export the optimized version" pattern fits the free-tool wedge in `distribution-os/projects/resumebuilder.md`. **[DECISION]** Not chosen.
- **Target customer** - **[FACT]** Active job seekers and career switchers, mobile-first.
- **Value proposition** - **[FACT]** ATS-aware, job-tailored resume you can export from your phone, that a hiring manager respects (`GLOBAL-TASTE.md` Resumely profile).
- **Pricing assumptions** - **[MISSING]** No price point exists. **[FACT]** Open question logged: "What is the current paid tier on iOS?" (`distribution-os/projects/resumebuilder.md`).
- **Monetization readiness** - **[FACT]** Not ready. No paywall confirmed; pricing copy undefined.
- **First possible paid feature** - **[ASSUMPTION]** Paid export of the optimized/ATS-tailored resume after a free score/preview.
- **What not to monetize yet** - **[ASSUMPTION]** The ATS score and the first tailored preview. These prove value and drive activation.
- **Key costs** - **[MISSING]** AI/API, Supabase, hosting, PostHog - `unknown` (`CFO-OS.md`).
- **Required metrics** - **[FACT]** D7 activation (install → optimize_completed), signups, editor→export rate, return within 14 days (`metrics-dashboard.md`, OKR 2).
- **Main business risks** - **[ASSUMPTION]** Episodic use (job seekers churn once hired - low LTV per user); crowded resume-tool market; ATS claims must match actual parser behavior (`resumebuilder.md` constraint).
- **30-day business objective** - Submitted to App Store with verified analytics + ASO listing ready.
- **90-day business objective** - Read first-cohort activation (OKR 2 target ≥40%, directional) and validate willingness to pay for export.

## Portfolio-Level

- **Revenue goal assumptions** - **[MISSING]** No basis for a revenue number. OKR 2 sets the *first* revenue signal as "≥1 paid subscriber across the portfolio" (`CEO-OS.md`) - a validation milestone, not a forecast.
- **Cost assumptions** - **[MISSING]** All cost lines `unknown`. **[FACT]** Marketing spend default is $0 - no paid ads (`EXECUTIVE-METRICS.md`, `distribution-context.md`).
- **Data missing before real forecasting** - **[MISSING]** App Store installs, conversion rate, activation rate, trial→paid, churn, AI cost per action, cash on hand. All required before any forecast (`CFO-OS.md`).
- **First realistic monetization experiment** - **[ASSUMPTION]** Resumely "free score → paid optimized export" is the fastest to test because the value is immediate and transactional; runs after Resumely is live with a working export funnel.
- **What must be validated before spending money** - **[FACT]** Activation and retention must be visible before any paid acquisition (`CEO-OS.md` focus rule 5). No spend until an organic channel proves repeatably (`distribution-context.md`).

---

# 4. GTM Plan v0

Channel scores are **[FACT]** from `channel-backlog.md`. For both apps, **ASO is the #1 channel (score 21, Tier A)** and is the primary acquisition surface.

## RunSmart iOS

| Element | Plan |
|---|---|
| Launch wedge | **[FACT]** Adaptive plan generation + free benchmark/route content as warm wedge. |
| First audience | **[FACT]** Beginner-to-intermediate runners with a wearable, triggered by a race signup, injury return, or restart. |
| First acquisition channel | **[FACT]** ASO (Tier A, score 21). |
| App Store / ASO plan | **[FACT]** ASO audit + listing rewrite via `marketingskills/skills/aso/SKILL.md`; founder approves copy before submission (`distribution-os/projects/runsmart.md`). |
| Landing / SEO plan | **[FACT]** Product-led landing pages (Tier A, 20) → App Store; running long-tail SEO is Tier B (heavier load). |
| LinkedIn founder plan | **[FACT]** One repeatable founder cadence, "lesson learned / behind the scenes" angle (Tier B, 16). Founder posts manually. |
| Directory / community / partnership plan | **[FACT]** Coach/club/podcast partnerships (Tier A, 17), relationship-driven; community = observation only, no spam. |
| Email / lifecycle plan | **[FACT]** Lifecycle backbone (Tier A, 19): welcome + plan-generated nudge + week-1 adherence digest. |
| Product-led activation plan | **[FACT]** Funnel: install → onboarding → first plan → first run → second run (retention signal) (`metrics-dashboard.md`). |
| First 7-day objective | Listing live/ready + ASO copy approved + analytics confirmed firing. |
| First 30-day objective | First install cohort with a readable activation funnel; one A-channel experiment live. |

## Resumely iOS

| Element | Plan |
|---|---|
| Launch wedge | **[FACT]** Paste-a-posting → tailor in minutes → export from phone; free ATS score as the warm wedge. |
| First audience | **[FACT]** Active job seekers, mobile during commute/lunch/between interviews. |
| First acquisition channel | **[FACT]** ASO (Tier A, 21). |
| App Store / ASO plan | **[FACT]** ASO audit + listing setup, English first, Hebrew metadata variant prepared; founder approves before submission (`resumebuilder.md`). |
| Landing / SEO plan | **[FACT]** Web landing → App Store CTA (Tier A, 20); programmatic SEO demoted to Tier B (feeder) until ASO + landings prove install conversion. |
| LinkedIn founder plan | **[FACT]** Job-seeker content is Tier C / optional. Low priority. |
| Directory / community / partnership plan | **[FACT]** Directory submissions with App Store URL (Tier A, 17); career-coach/HR partnerships Tier B. |
| Email / lifecycle plan | **[FACT]** Post-install lifecycle (Tier A, 20): welcome + didn't-start-in-24h + activation-hit + 14-day return. |
| Product-led activation plan | **[FACT]** Funnel: install → first resume started → first export → returned within 14 days; conversion review on first-run → first export is the most leveraged surface. |
| First 7-day objective | Submitted to App Store; ASO listing + Hebrew metadata prepared; analytics confirmed firing. |
| First 30-day objective | First cohort with readable install → optimize → export funnel; free-tool web→app handoff scoped. |

---

# 5. Analytics and Metrics Plan

**[FACT]** Both apps have PostHog integrated; live receipt is the open item (EXD-002/004, `EXECUTIVE-BACKLOG.md`).

## RunSmart iOS

- **North-star metric** - **[FACT]** Weekly active runners (opened + interacted in last 7 days) (`metrics-dashboard.md`).
- **Activation event** - **[FACT]** `run_completed` within 7 days of install (OKR 2). Onboarding-complete + first plan generated is the leading activation gate.
- **Funnel events** - **[FACT]** Wired already: app_launched, sign_in, onboarding_started/completed, plan_generated, run_started, run_completed, run_abandoned, post_run_card, coach_thread, plan_viewed, route_selected, tab_viewed, garmin_sync, healthkit_sync (`EXECUTIVE-BACKLOG.md` analytics-sprint-001).
- **Retention signal** - **[FACT]** Second run logged; week-1 plan adherence; week-4 continued use (`metrics-dashboard.md`).
- **Revenue signal** - **[MISSING]** None wired (no RevenueCat/IAP).
- **PostHog / App Store data needed** - **[MISSING]** App Store installs (ASC) to anchor the install→activation funnel; confirmed event receipt in PostHog.
- **What is missing today** - **[FACT]** Verification that events land in PostHog from the production build (token may not be set in prod config) - analytics-sprint-001, cap 2h.

## Resumely iOS

- **North-star metric** - **[ASSUMPTION]** Weekly active users; longer-term, resumes exported (the value moment).
- **Activation event** - **[FACT]** `optimize_completed` within 7 days of install (OKR 2); `export_success` is the value confirmation.
- **Funnel events** - **[FACT]** Minimal set wired: app_launched, optimize_completed, export_success (≤5 events, EXD-004, analytics-sprint-002).
- **Retention signal** - **[FACT]** Returned within 14 days; second resume (`metrics-dashboard.md`).
- **Revenue signal** - **[MISSING]** None wired.
- **PostHog / App Store data needed** - **[MISSING]** Live event coverage verified during the authenticated device smoke; App Store installs from ASC.
- **What is missing today** - **[FACT]** Real-device authenticated smoke confirming PostHog Live Events + export coverage from a keyed build (`PROJECT-STATUS.md` Action Board).

---

# 6. Monetization and CFO View

No numbers invented. Every unknown is tagged with the source needed (mirrors `CFO-OS.md`).

- **Known financial picture** - **[FACT]** Zero revenue. Zero monetization wired. Marketing spend $0 (no paid ads). That is the entire known picture.
- **Missing financial data** - **[MISSING]** Revenue by product/platform, App Store proceeds, subscription revenue, refunds (need ASC/RevenueCat/Stripe); AI/API, hosting, Supabase, Vercel, PostHog costs (need provider billing); cash on hand (need owner); conversion, activation, trial→paid, churn, LTV, CAC (need PostHog/RevenueCat).
- **Cost categories to track** - **[FACT]** AI/API, hosting, Supabase, Vercel, PostHog, design/tooling, contractor, marketing (`CFO-OS.md`). Start the manual cost list now - it is the one source the founder can fill without instrumentation.
- **Pricing assumptions** - **[MISSING]** None exist for either app. Do not assume a price.
- **Budget constraints** - **[FACT]** Free/low-cost-first; no paid acquisition until an organic channel proves and ROI hypothesis is clear (`distribution-context.md`, `CEO-OS.md`).
- **No-spend rules** - **[FACT]** No paid ads by default; Apple Search Ads explicitly out of scope until organic ASO proves (`resumebuilder.md`); no new dependencies/tools without founder approval.
- **First monetization experiment** - **[ASSUMPTION]** Resumely "free score → paid optimized export" once Resumely is live and export works. Must include a price, a hypothesis, and a validation window before any build.
- **Monetization decisions not ready yet** - **[DECISION]** (1) Subscription vs one-time vs credit for each app; (2) what is free vs paid (the activation gate); (3) RevenueCat vs StoreKit-direct; (4) whether to introduce monetization before or after reading first-cohort activation. None are decidable without a live funnel.

---

# 7. CEO Decisions Needed

Per `CEO-OS.md`: every open question gets a recommendation, not just a summary.

| # | Decision | Why it matters | Options | Recommended | Urgency | Risk if delayed |
|---|---|---|---|---|---|---|
| D1 | **Monetization model per app** (subscription / one-time / credit / freemium) | Gates every pricing, paywall, and CFO workflow; nothing in Section 6 can advance without it | Subscription / one-time / freemium hybrid / decide-after-activation | **[ASSUMPTION]** Decide the *shape* now (freemium with a clear free activation moment), set the *price* after first-cohort activation data | Medium | Monetization workflows stay frozen; first revenue signal (OKR 2) slips |
| D2 | **Resumely ASC upload path** | Blocks Resumely submission this week | Fastlane (if API key available) / manual portal upload | **[FACT]** Fastlane if credentials exist, else manual portal after smoke passes (`DASHBOARD.md`) | High | Resumely submission stalls; Q2 OKR 1 KR2 at risk |
| D3 | **Ratify separate-brand portfolio model** | Determines whether to invest in shared vs separate distribution assets | Separate brands / shared umbrella brand | **[ASSUMPTION]** Keep brands separate, share only the operating layer (matches current OS) | Medium | Wasted asset work; diluted positioning on both apps |
| D4 | **RunSmart 1.0.1 scope** | Defines next RunSmart work after review outcome | Wait then cherry-pick Sprint 11 / ship broad 1.0.1 | **[FACT]** Wait for v1.0 review outcome, then cherry-pick highest-impact Sprint 11 stories (`DASHBOARD.md`) | Medium (gated by Apple) | Risk of mutating frozen v1.0 artifacts |
| D5 | **Monetize-before-or-after-activation** | Controls whether a paywall ships at launch or after data | Paywall at launch / paywall after reading D7 activation | **[ASSUMPTION]** After - read activation first (consistent with focus rule 5) | Medium | Premature paywall suppresses the activation funnel that produces decision data |

---

# 8. COO Execution Plan (30 Days)

Separated by work type. **[FACT]** Action Board items are from `PROJECT-STATUS.md`; the rest are this plan's additions, tagged.

### Now
- **Manual founder:** Decide D2 (Resumely ASC upload path). **[FACT]**
- **Local repo (Resumely iOS):** Run authenticated real-device smoke through optimize → design → expert → preview/export. **[FACT]**
- **Local repo (Resumely iOS):** Verify PostHog Live Events + export coverage from a keyed build. **[FACT]**
- **Manual founder (RunSmart iOS):** Monitor App Store review; keep v1.0 frozen. **[FACT]**

### Week 1
- **Local repo (Resumely iOS):** Upload screenshots/listing and submit after smoke passes. **[FACT]**
- **Local repo (RunSmart iOS):** Verify PostHog token in production/App Store build config; confirm `app_launched` in PostHog (analytics-sprint-001, cap 2h). **[FACT]**
- **Global OS:** Start the manual cost list in CFO OS (the one financial source fillable without instrumentation). **[ASSUMPTION]**
- **Manual founder:** Make D1 *shape* decision (freemium vs subscription vs one-time). **[ASSUMPTION]**

### Week 2
- **Global OS / Research:** ASO audit + listing rewrite for RunSmart iOS via the ASO skill; founder approves copy. **[FACT]** (`first-4-week-plan.md` week 2)
- **Global OS / Research:** ASO audit + listing setup for Resumely iOS (English + Hebrew metadata variant prepared). **[FACT]**
- **Global OS:** Draft RunSmart lifecycle email backbone (welcome + plan-generated nudge + week-1 adherence). **[FACT]**
- **Manual founder:** Ratify D3 (separate brands). **[ASSUMPTION]**

### Week 3
- **Global OS / Research:** Resumely directory submission pack v1 (web + App Store URL). **[FACT]**
- **Global OS:** Resumely post-install lifecycle backbone draft. **[FACT]**
- **Global OS:** RunSmart product-led landing page draft (one page) → App Store. **[ASSUMPTION]**
- **QA/release:** If RunSmart approved, scope 1.0.1 from Sprint 11 (D4). **[FACT]**

### Week 4
- **Global OS:** Measure cumulative effect; define the PostHog activation funnel for whichever app is live (analytics-sprint-003). **[FACT]**
- **Global OS:** Re-score channels; propose month-2 focus pattern. **[FACT]** (`first-4-week-plan.md` week 4)
- **Manual founder:** Decide D5 (monetize before/after activation) once a funnel is readable. **[ASSUMPTION]**

### Later
- **[FACT]** Both apps: revenue/cost/activation dashboards once App Store data exists.
- **[FACT]** Resumely: Resume Library backend, PDF/export QA expansion, Hebrew/RTL.
- **[FACT]** RunSmart: Garmin webhook audit, post-launch activation funnel review.
- **[ASSUMPTION]** First monetization experiment (Resumely free-score → paid-export).

### Blocked
- **[FACT]** RunSmart App Store review outcome (depends on Apple).
- **[FACT]** Resumely ASC upload until credentials or portal session available.
- **[FACT]** Resumely Resume Library until `/api/v1/resumes` returns JSON.
- **[MISSING]** All monetization/forecast work until a live funnel exists.

---

# 9. Risk Review

| Risk type | Risk | Tag | Mitigation |
|---|---|---|---|
| App Store | RunSmart review delay/rejection (24–72h typical, up to 14 days on rejection) | [FACT] `CEO-OS.md` | Keep v1.0 frozen; do not mutate release artifacts; have 1.0.1 scope ready but unbuilt |
| App Store | Resumely ASC upload blocked (no Fastlane key / portal session) | [FACT] `EXECUTIVE-DASHBOARD.md` | Resolve D2 now; manual portal fallback |
| Analytics | Events don't actually land in PostHog → blind day-1 cohort | [FACT] EXD-002 | analytics-sprint-001/002 verification before launch; cap 2h/2d |
| Monetization | No model, no price, no paywall → no revenue path | [DECISION] D1 | Decide model shape now, price after activation data |
| Monetization | Resumely episodic use → low LTV per user | [ASSUMPTION] | Validate willingness-to-pay on export before investing in retention |
| Positioning | Brand dilution if apps blur together | [DECISION] D3 | Ratify separate-brand model; share only operating layer |
| Positioning | RunSmart drifting into a dashboard, not a coach | [FACT] `GLOBAL-TASTE.md` | Taste Check gate; one clear next action, hide raw math |
| Execution | Splitting focus across two submissions at once | [FACT] `CEO-OS.md` | One product per focus week; Resumely submits, RunSmart monitors |
| Execution | Dirty local trees (RunSmart Web, both iOS, ResumeBuilder Web) | [FACT] `EXECUTIVE-DASHBOARD.md` | Triage dirty trees before more implementation |
| Channel | Over-reliance on ASO with no data to optimize it | [ASSUMPTION] | Treat first listing as v1; iterate after install/conversion data lands |
| Channel | Paid-ads temptation before organic proof | [FACT] `distribution-context.md` | No-spend rule until an organic channel proves repeatably |
| Product quality | Resumely WKWebView PDF/export fragility; Swift 6 concurrency | [FACT] `resumebuilder-ios.md` | Device smoke with visual output checks before submit |
| Product quality | RunSmart integration claims (Garmin/HealthKit) exceeding actual behavior | [FACT] `runsmart-ios.md` | No implied background GPS/sync without repo evidence |

---

# 10. Work Packets Needed

Copy-ready outlines for work that must execute **inside local repos**. Global OS work stays in this OS and is not packetized here. Each packet respects "do not change product repos beyond its stated scope."

### WP-1 - Resumely iOS: Authenticated device smoke + submit package
- **Owner role:** Release Manager
- **Project:** ResumeBuilder iOS (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`)
- **Goal:** Confirm the submit build works on a real authenticated device and analytics fire, then upload + submit.
- **Read first:** local `AGENTS.md`, `CLAUDE.md`, `tasks/progress.md`, `tasks/session-log.md`, `tasks/lessons.md`.
- **Task:** Run smoke through optimize → design → expert → preview/export; verify PostHog Live Events + `export_success`; resolve ASC upload path (D2); upload screenshots/listing; submit.
- **Validation:** Smoke screenshots, PostHog event evidence, ASC upload confirmation. Record in `tasks/session-log.md`.
- **What not to touch:** No new events beyond the wired ≤5; no new dependencies; no RunSmart logic.

### WP-2 - RunSmart iOS: Verify PostHog event receipt (analytics-sprint-001)
- **Owner role:** QA / Release Manager
- **Project:** RunSmart iOS (`/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`)
- **Goal:** Confirm wired analytics events actually land in PostHog from the production build.
- **Read first:** local `AGENTS.md`, `CLAUDE.md`, `tasks/todo.md`, `AnalyticsEvents.swift`, `RunSmartLiteAppShell.swift`.
- **Task:** Verify PostHog token/host in production config; confirm ≥1 event (`app_launched`) in PostHog; if missing, add token via build config (never hardcoded).
- **Validation:** PostHog screenshot showing the event; note token source. Cap 2h.
- **What not to touch:** Do not add events; do not mutate frozen v1.0 release artifacts; no hardcoded secrets.

### WP-3 - RunSmart iOS: Scope 1.0.1 from Sprint 11 (only after review outcome)
- **Owner role:** Product Manager / Director
- **Project:** RunSmart iOS
- **Goal:** Convert Sprint 11 specs into a scoped, reviewable 1.0.1 implementation plan.
- **Read first:** `docs/specs/README.md`, 1.0.1 UX redesign spec, `tasks/todo.md`, `tasks/session-log.md`.
- **Task:** Cherry-pick highest-impact stories; produce a small reviewable plan. **Gated on D4 and Apple review outcome - do not start before approval.**
- **Validation:** A plan file with story list + acceptance criteria; no code yet.
- **What not to touch:** No implementation until v1.0 review resolves; keep v1.0 frozen.

### WP-4 - RunSmart Web: Dirty-tree triage
- **Owner role:** QA / Release Manager
- **Project:** RunSmart Web (`/Users/nadavyigal/Documents/RunSmart`)
- **Goal:** Triage modified/untracked files before more web work.
- **Read first:** `tasks/MEMORY.md`, `tasks/ERRORS.md`, `git status`.
- **Task:** Classify dirty files (keep/commit/discard); leave the tree clean. Support repo only.
- **Validation:** Clean `git status` or a documented decision per file.
- **What not to touch:** No new features; no voice work until triage done.

### WP-5 - ResumeBuilder Web: Hold (conditional)
- **Owner role:** Release Manager
- **Project:** ResumeBuilder Web (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`)
- **Goal:** Leave parked unless the Resumely iOS smoke exposes backend parse/render blockers.
- **Read first:** `tasks/MEMORY.md`, `docs/agent-os/project-context.md`.
- **Task:** Only act if WP-1 surfaces a backend dependency (e.g., PDF parse/render). Otherwise no work.
- **Validation:** N/A unless triggered.
- **What not to touch:** No rollout enablement unless triggered by WP-1 findings.

> No work packet is created for Global Agentic OS / Distribution OS items (ASO drafts, lifecycle email drafts, channel re-scoring) - those execute in this OS per the COO plan, not in product repos.

---

# 11. Business + GTM Alignment Review

- **Where business model and GTM are aligned** - **[FACT]** Both lead with ASO + product-led activation, and both defer paid acquisition until activation/retention is visible. GTM's "prove organic first" and the business plan's "no spend until validated" are the same rule.
- **Where they conflict** - **[ASSUMPTION]** GTM is ready to drive installs (ASO, listings, lifecycle), but the business model has no paywall or price, so installs cannot convert to revenue. We can acquire but not monetize. This is acceptable for v0 (data-gathering phase) only if we accept that the first 30–60 days produce *activation data, not revenue*.
- **Missing assumptions** - Price points (both apps); what is free vs paid (the activation gate); attribution tagging (`at=`/`ct=` params for Resumely web→app - open question in `resumebuilder.md`).
- **Missing data** - **[MISSING]** Installs, conversion, activation, cost-per-action, cash on hand. Everything needed to connect GTM spend-readiness to a business case.
- **Decisions required before execution** - D1 (model), D2 (ASC path), D5 (monetize timing). D2 blocks this week; D1/D5 block monetization but not launch.
- **What should be deferred** - **[FACT]** Programmatic SEO (Resumely, demoted to feeder), beginner challenges (RunSmart, gated on feature), paid acquisition, revenue dashboards, LTV/CAC analysis. All deferred until a live funnel exists.

---

# 12. Executive OS Gaps Revealed

What this planning sprint shows the future Executive OS must support. **[FACT]** Phase 1 (CEO/CFO/Analysis spine) is live; these are gaps against doing real business+GTM planning.

- **CEO needs** - A standing **portfolio-priority vs shippable-queue** distinction (RunSmart is strategic-primary but Resumely is this-week's-ship). The current focus rules collapse these into one ordering; the OS needs to hold both. A live **decision-status tracker** linking each `EXECUTIVE-DECISIONS.md` row to the work it blocks.
- **COO needs** - A first-class **work-packet protocol and registry** (this plan invented WP-1..5 ad hoc). The OS has prompts but no standing COO execution layer that separates manual / global-OS / local-repo / research / QA work and tracks packet status.
- **CFO needs** - A **manual cost-list intake** (the one financial source fillable today) and a **pricing-decision workflow**. `CFO-OS.md` Phase 2 lists pricing/monetization agents as backlog; this sprint shows they're needed *before* launch, not after. Also a **"what's free vs paid" activation-gate template**.
- **Analysis needs** - A **willingness-to-pay / monetization-model research workflow** (subscription vs one-time vs credit per category). `EXECUTIVE-BACKLOG.md` lists market/competitor research as Phase 2; D1 cannot be made well without it.
- **Chief of Staff needs** - A **30-day operating-rhythm template** that merges the distribution first-4-week plan with the executive cadence into one founder-facing weekly view. Today they live in separate files (`distribution-os/first-4-week-plan.md` vs `executive-os/EXECUTIVE-RHYTHM.md`).
- **Risk Review needs** - A **standing risk register** (Phase 2 backlog item `risk-register-template`). This plan's Section 9 had to be assembled by hand from scattered risk boards.
- **Work packet protocol needs** - A **template + status lifecycle** (proposed → ready → in-repo → validated) and a rule that global-OS work is *not* packetized while local-repo work *is*. This sprint applied that rule manually; the OS should encode it.

---

# Final Recommendation - Single Best Next Action

**Run the Resumely iOS authenticated device smoke (WP-1) and resolve the ASC upload path (D2), so Resumely can be submitted this week.**

Why this and not anything else: RunSmart (the strategic primary) is frozen and waiting on Apple - there is no founder action that moves it. Resumely is the one app where a founder action this week changes the outcome, and getting a second app into review is what unlocks the first readable funnel, which in turn unblocks every monetization and forecasting decision (D1, D5, the entire CFO view). Everything else in this plan - ASO drafts, lifecycle emails, pricing - is preparation that pays off only after an app is live. Ship the submittable one first.
