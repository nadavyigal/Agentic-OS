# WP-2 Monetization Spec — Ready-to-Build
## RunSmart + Resumely Freemium Implementation Spec

- Date: 2026-06-04
- Role: CFO OS
- Status: Ready to build, implement after first-cohort activation data (EXD-009)
- Research source: `executive-os/research/WP-2-competitor-pricing-research.md`
- Decisions: EXD-005, EXD-009

**Constraint:** Do not implement a paywall or set a price until activation data is readable. This spec exists so implementation is instant when the green light arrives.

---

## 1. Free vs Paid Feature Matrix

### RunSmart

| Feature | Free | Pro |
|---|---|---|
| Onboarding + goal setting | Yes | Yes |
| AI training plan generated (week 1, full) | Yes | Yes |
| GPS run tracking | Yes | Yes |
| First run logged + weekly stats | Yes | Yes |
| Basic Garmin / Apple Watch sync (data read) | Yes | Yes |
| Run history + pace/distance charts | Yes | Yes |
| Week 1 adherence summary | Yes | Yes |
| Basic post-run debrief (distance, pace, HR) | Yes | Yes |
| Weeks 2+ of adaptive plan (Flex Week, plan adjusts to actual runs) | No | Yes |
| Advanced Garmin / HRV / readiness integration | No | Yes |
| Voice coach cues during runs | No | Yes |
| Long-horizon race plans (marathon, ultra, multi-cycle) | No | Yes |
| Cross-training + strength session integration | No | Yes |
| Deep post-run debrief (AI analysis of pacing, load, recovery) | No | Yes |
| Goal race pace predictions + race-day strategy | No | Yes |

**Free tier philosophy:** The "this coach knows me" moment is free, covering onboarding through week 1. Gating week 2 is when the adaptation value is first felt, which is the right upgrade moment (confirmed by Runna's model).

**Subscription shape:** Annual-first (market standard; Runna $120/year, Strava $80/year). Monthly is available as the fallback.

**Price cell:** `NEEDS_DATA`, set from D7 activation cohort. Expected range $79-$120/year / $10-$14/month (market; source: `executive-os/research/WP-2-competitor-pricing-research.md`). Do not hardcode.

---

### Resumely

| Feature | Free | Pro |
|---|---|---|
| Resume import (PDF/LinkedIn) or build from scratch | Yes | Yes |
| AI-powered optimization, 1 full round (analyze, improve bullets, keyword match) | Yes | Yes |
| Resume preview (see the improved version) | Yes | Yes |
| 1 PDF export / download | Yes | Yes |
| Basic ATS score check (score + top 5 missing keywords) | Yes | Yes |
| 1 starter design template | Yes | Yes |
| Per-job AI tailoring (additional job descriptions) | No | Yes |
| Additional exports and downloads | No | Yes |
| Full ATS deep-dive (all keywords, section-by-section analysis) | No | Yes |
| Unlimited cover letter generation | No | Yes |
| Expert modes: LinkedIn optimization, interview prep, salary negotiation scripts | No | Yes |
| Premium design templates (beyond starter) | No | Yes |
| Job application tracker | No | Yes |

**Free tier philosophy:** The user must see a better resume and export it once, free. This is the activation moment that drives conversion. Teal and Rezi both allow this. Gating before the first export is the market anti-pattern (Jobscan gets criticized for exactly this).

**Subscription shape:** Weekly as the primary urgency tier (matches Teal's $9/week; job seekers are sprint-mode); monthly as standard; annual for power users. No lifetime plan until conversion data suggests it.

**Price cell:** `NEEDS_DATA`, set from D7 activation cohort. Expected range $9-$13/week / $25-$30/month / $79-$96/year (market; source: `executive-os/research/WP-2-competitor-pricing-research.md`). Do not hardcode.

---

## 2. Paywall Placement Spec

### RunSmart

| Field | Value |
|---|---|
| Screen | Plan Detail view, week 2 workout cards |
| Gate type | Soft gate: week 2 plan is visible (titles, distances) but locked; tapping reveals upgrade prompt |
| Trigger event | User taps any week 2+ workout detail, OR `runsmart.retention.plan_adapt_triggered` fires |
| CTA headline | "Your plan adapted to week 1. Unlock to continue." |
| CTA sub-text | "Your coach updated [X] sessions based on how last week went." |
| CTA primary button | "Unlock Pro" |
| CTA secondary | "Remind me later" (7-day snooze) |
| Dismiss behavior | User can see week 2 list but not workout detail |
| Urgency lever | Show the specific adaptation (e.g., "Tuesday's run moved from 8km to 6km. Your recovery matters."). This is the personalization proof. |
| PostHog event at show | `runsmart.monetization.paywall_shown` (see Section 3) |

### Resumely

| Field | Value |
|---|---|
| Screen | Optimize flow, second job description entry (or second download attempt) |
| Gate type | Soft gate: show ATS score delta preview for the second job ("Your resume scores X% for this role, see the fixes") but block the detailed analysis and download |
| Trigger event | `resumebuilder.monetization.second_optimize_attempted` or `resumebuilder.monetization.second_export_attempted` |
| CTA headline | "Tailor your resume to every job" |
| CTA sub-text | "You've already improved your resume once. Pro unlocks unlimited tailoring so every application is your best." |
| CTA primary button | "Unlock Pro" |
| CTA secondary | "Use my existing resume" (lets them download the already-optimized version, not the new one) |
| Dismiss behavior | User can still export the first optimized resume; they just can't run a new optimization |
| Urgency lever | Show the specific score improvement they're missing ("Resume scores 61% for this job. Pro would bring it to 88%.") |
| PostHog event at show | `resumebuilder.monetization.paywall_shown` (see Section 3) |

---

## 3. PostHog Events — Activation to Conversion Funnel

These events are required to read the funnel before and after the paywall is live. Instrument these before flipping the paywall switch.

**Event names must conform to `distribution-os/data/metrics-schema.md` naming rule: `{product}.{stage}.{metric_name}`, lowercase, dot-separated.**

### RunSmart Events

```text
runsmart.activation.onboarding_completed
  properties: goal_type, experience_level, target_race

runsmart.activation.plan_generated
  properties: plan_type, duration_weeks, target_race

runsmart.activation.first_run_logged
  properties: distance_km, source (manual | gps | garmin)

runsmart.retention.week1_completed        <- activation milestone
  properties: runs_completed, runs_missed, avg_pace

runsmart.retention.plan_adapt_triggered   <- precursor to paywall; plan changed based on week 1
  properties: changes_count, reason

runsmart.monetization.paywall_shown
  properties: trigger_event, screen, plan_week

runsmart.monetization.upgrade_cta_clicked
  properties: trigger_event, screen, plan_week, cta_variant

runsmart.revenue.subscription_started
  properties: plan_type (monthly | annual), price_usd

runsmart.revenue.subscription_cancelled
  properties: plan_type, weeks_active, reason (if captured)
```

### Resumely Events

```text
resumebuilder.activation.resume_import_started
  properties: source (pdf | linkedin | scratch)

resumebuilder.activation.first_optimize_completed  <- activation start
  properties: score_before, score_after, keywords_added

resumebuilder.activation.resume_previewed
  properties: template_id, score_after

resumebuilder.activation.first_export_completed    <- activation complete
  properties: format (pdf | docx)

resumebuilder.monetization.second_optimize_attempted  <- paywall trigger precursor
  properties: job_title, score_current

resumebuilder.monetization.second_export_attempted    <- alternative paywall trigger
  properties: is_new_version (bool)

resumebuilder.monetization.paywall_shown
  properties: trigger_event, screen

resumebuilder.monetization.upgrade_cta_clicked
  properties: trigger_event, screen, cta_variant

resumebuilder.revenue.subscription_started
  properties: plan_type (weekly | monthly | annual), price_usd

resumebuilder.revenue.subscription_cancelled
  properties: plan_type, days_active, reason (if captured)
```

**Funnel to read:**
- RunSmart: `runsmart.activation.plan_generated` -> `runsmart.retention.week1_completed` -> `runsmart.monetization.paywall_shown` -> `runsmart.monetization.upgrade_cta_clicked` -> `runsmart.revenue.subscription_started`
- Resumely: `resumebuilder.activation.first_optimize_completed` -> `resumebuilder.activation.first_export_completed` -> `resumebuilder.monetization.second_optimize_attempted` -> `resumebuilder.monetization.paywall_shown` -> `resumebuilder.monetization.upgrade_cta_clicked` -> `resumebuilder.revenue.subscription_started`

**Activation metric to declare before monetizing (EXD-009):**
- RunSmart: D7 activation = `runsmart.retention.week1_completed` / `runsmart.activation.plan_generated` >= threshold (set after first 50 users)
- Resumely: D7 activation = `resumebuilder.activation.first_export_completed` / `resumebuilder.activation.resume_import_started` >= threshold

---

## 4. StoreKit / IAP Product IDs (Draft, No Prices)

Prices are `NEEDS_DATA`. Only IDs and descriptions are drafted here. No product should be created in App Store Connect until EXD-009 green light.

### RunSmart

```text
com.runsmart.pro.monthly
  - Display name: RunSmart Pro
  - Type: Auto-renewable subscription
  - Duration: 1 month
  - Price: NEEDS_DATA (market range $10-$14/month)
  - Free trial: 7 days

com.runsmart.pro.annual
  - Display name: RunSmart Pro Annual
  - Type: Auto-renewable subscription
  - Duration: 1 year
  - Price: NEEDS_DATA (market range $79-$120/year)
  - Free trial: 7 days
  - Introductory offer: first month free (optional, decide from data)
```

Subscription group: `RunSmart Pro` (one group; monthly and annual are the two options)

### Resumely

```text
com.resumely.pro.weekly
  - Display name: Resumely Pro Weekly
  - Type: Auto-renewable subscription
  - Duration: 1 week
  - Price: NEEDS_DATA (market range $9-$13/week)
  - Free trial: none (high urgency, short horizon)

com.resumely.pro.monthly
  - Display name: Resumely Pro
  - Type: Auto-renewable subscription
  - Duration: 1 month
  - Price: NEEDS_DATA (market range $25-$30/month)
  - Free trial: 3 days

com.resumely.pro.annual
  - Display name: Resumely Pro Annual
  - Type: Auto-renewable subscription
  - Duration: 1 year
  - Price: NEEDS_DATA (market range $79-$96/year)
  - Free trial: 7 days
```

Subscription group: `Resumely Pro` (one group; weekly, monthly, and annual)

Note on Resumely weekly: Teal's $9/week tier captures high-urgency job seekers who are actively applying. This tier should be the top CTA at the paywall if D7 activation data shows short-burst usage patterns (session clustering).

---

## 5. Price Experiment Plan

**When to run:** After 300 total paywall exposures per app (minimum for statistical signal). Do not guess before this threshold.

**How to run (Apple compliance):**

Per Apple guidelines, the paywall must display the actual StoreKit-provided localized price. Use `Product.displayPrice` (StoreKit 2) or `SKProduct.localizedPrice` (StoreKit 1) at runtime. Never hardcode a price string in CTA copy.

To run a price experiment, vary the StoreKit product ID loaded by the paywall per user. Each variant maps to a different App Store Connect pricing tier (a separate product ID with a different price set in App Store Connect). Use RevenueCat Offerings or App Store Connect product configuration to assign variants, then display the localized price returned by StoreKit for whatever product ID the user is shown.

Do not change the CTA display text to a price that differs from what StoreKit will actually charge. Doing so creates a UI/charge mismatch that is a review violation.

PostHog feature flags control which product ID the paywall loads, not the displayed price string.

### RunSmart Price Experiment

- Variants (3-way): Annual product ID A vs B vs C, each pointing to a different App Store pricing tier (set actual $ values after cohort 1, within $79-$120/year range)
- Primary metric: `runsmart.revenue.subscription_started` within 7 days of `runsmart.monetization.paywall_shown`
- Secondary metric: 30-day retention of subscribers
- Minimum sample: 100 paywall exposures per variant before reading
- Duration: run until 95% statistical significance or 6 weeks, whichever comes first
- Decision: pick the variant with highest subscription rate, weighted by 30-day retention

### Resumely Price Experiment

- First experiment: weekly vs monthly as the CTA default (which tier drives higher total revenue per activated user)
- Second experiment: price of the default tier (set actual $ after cohort 1, within market range)
- Primary metric: `resumebuilder.revenue.subscription_started` within 3 days of `resumebuilder.monetization.paywall_shown` (shorter window; job seekers decide fast)
- Minimum sample: 100 paywall exposures per variant
- Duration: run until 95% statistical significance or 4 weeks

**Logging:** Log experiment start, winner, and decision in `executive-os/EXECUTIVE-DECISIONS.md` when the experiment runs.
