# WP-2 Monetization Spec — Ready-to-Build
## RunSmart + Resumely Freemium Implementation Spec

- Date: 2026-06-04
- Role: CFO OS
- Status: Ready to build — implement after first-cohort activation data (EXD-009)
- Research source: research/WP-2-competitor-pricing-research.md
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

**Free tier philosophy:** The "this coach knows me" moment is free — onboarding through week 1. Gating week 2 is when the adaptation value is first felt, which is the right upgrade moment (confirmed by Runna's model).

**Subscription shape:** Annual-first (market standard; Runna $120/year, Strava $80/year). Monthly is available as the fallback.

**Price cell:** `NEEDS_DATA` — set from D7 activation cohort. Expected range $79-$120/year / $10-$14/month (market). Do not hardcode.

---

### Resumely

| Feature | Free | Pro |
|---|---|---|
| Resume import (PDF/LinkedIn) or build from scratch | Yes | Yes |
| AI-powered optimization — 1 full round (analyze, improve bullets, keyword match) | Yes | Yes |
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

**Free tier philosophy:** The user must see a better resume and export it once, free — this is the activation moment that drives conversion. Teal and Rezi both allow this. Gating before the first export = activation killing (Jobscan gets criticized for this).

**Subscription shape:** Weekly as the primary urgency tier (matches Teal's $9/week; job seekers are sprint-mode); monthly as standard; annual for power users. No lifetime plan until conversion data suggests it.

**Price cell:** `NEEDS_DATA` — set from D7 activation cohort. Expected range $9-$13/week / $25-$30/month / $79-$96/year (market). Do not hardcode.

---

## 2. Paywall Placement Spec

### RunSmart

| Field | Value |
|---|---|
| Screen | Plan Detail view — week 2 workout cards |
| Gate type | Soft gate: week 2 plan is visible (titles, distances) but locked — tapping reveals upgrade prompt |
| Trigger event | User taps any week 2+ workout detail, OR plan_adapt_triggered fires |
| CTA headline | "Your plan adapted to week 1 — unlock to continue" |
| CTA sub-text | "Your coach updated [X] sessions based on how last week went." |
| CTA primary button | "Unlock Pro" |
| CTA secondary | "Remind me later" (7-day snooze) |
| Dismiss behavior | User can see week 2 list but not workout detail |
| Urgency lever | Show the specific adaptation (e.g., "Tuesday's run moved from 8km to 6km — your recovery matters"). This is the personalization proof. |
| PostHog event at show | `paywall_shown` — see Section 3 |

### Resumely

| Field | Value |
|---|---|
| Screen | Optimize flow — second job description entry (or second download attempt) |
| Gate type | Soft gate: show ATS score delta preview for the second job ("Your resume scores X% for this role — see the fixes") but block the detailed analysis and download |
| Trigger event | `second_optimize_attempted` or `second_export_attempted` |
| CTA headline | "Tailor your resume to every job" |
| CTA sub-text | "You've already improved your resume once. Pro unlocks unlimited tailoring so every application is your best." |
| CTA primary button | "Unlock Pro" |
| CTA secondary | "Use my existing resume" (lets them download the already-optimized version, not the new one) |
| Dismiss behavior | User can still export the first optimized resume; they just can't run a new optimization |
| Urgency lever | Show the specific score improvement they're missing ("Resume scores 61% for this job — Pro would bring it to 88%") |
| PostHog event at show | `paywall_shown` — see Section 3 |

---

## 3. PostHog Events — Activation to Conversion Funnel

These events are required to read the funnel before and after the paywall is live. Instrument these before flipping the paywall switch.

### RunSmart Events

```
onboarding_completed
  properties: goal_type, experience_level, target_race

plan_generated
  properties: plan_type, duration_weeks, target_race

first_run_logged
  properties: distance_km, source (manual | gps | garmin)

week1_completed        ← activation milestone
  properties: runs_completed, runs_missed, avg_pace

plan_adapt_triggered   ← precursor to paywall; plan changed based on week 1
  properties: changes_count, reason

paywall_shown
  properties: trigger_event, screen, plan_week

upgrade_cta_clicked
  properties: trigger_event, screen, plan_week, cta_variant

subscription_started
  properties: plan_type (monthly | annual), price_usd

subscription_cancelled
  properties: plan_type, weeks_active, reason (if captured)
```

### Resumely Events

```
resume_import_started
  properties: source (pdf | linkedin | scratch)

first_optimize_completed  ← activation start
  properties: score_before, score_after, keywords_added

resume_previewed
  properties: template_id, score_after

first_export_completed    ← activation complete
  properties: format (pdf | docx)

second_optimize_attempted  ← paywall trigger precursor
  properties: job_title, score_current

second_export_attempted    ← alternative paywall trigger
  properties: is_new_version (bool)

paywall_shown
  properties: trigger_event, screen

upgrade_cta_clicked
  properties: trigger_event, screen, cta_variant

subscription_started
  properties: plan_type (weekly | monthly | annual), price_usd

subscription_cancelled
  properties: plan_type, days_active, reason (if captured)
```

**Funnel to read:**
- RunSmart: `plan_generated` → `week1_completed` → `paywall_shown` → `upgrade_cta_clicked` → `subscription_started`
- Resumely: `first_optimize_completed` → `first_export_completed` → `second_optimize_attempted` → `paywall_shown` → `upgrade_cta_clicked` → `subscription_started`

**Activation metric to declare before monetizing (EXD-009):**
- RunSmart: D7 activation = `week1_completed` / `plan_generated` ≥ threshold (set after first 50 users)
- Resumely: D7 activation = `first_export_completed` / `resume_import_started` ≥ threshold

---

## 4. StoreKit / IAP Product IDs (Draft — No Prices)

Prices are `NEEDS_DATA`. Only IDs and descriptions are drafted here. No product should be created in App Store Connect until EXD-009 green light.

### RunSmart

```
com.runsmart.pro.monthly
  - Display name: RunSmart Pro
  - Type: Auto-renewable subscription
  - Duration: 1 month
  - Price: NEEDS_DATA (market range $10-$14/month)
  - Free trial: 7 days

com.runsmart.pro.annual
  - Display name: RunSmart Pro — Annual
  - Type: Auto-renewable subscription
  - Duration: 1 year
  - Price: NEEDS_DATA (market range $79-$120/year)
  - Free trial: 7 days
  - Introductory offer: first month free (optional — decide from data)
```

Subscription group: `RunSmart Pro` (one group; monthly and annual are the two options)

### Resumely

```
com.resumely.pro.weekly
  - Display name: Resumely Pro — Weekly
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
  - Display name: Resumely Pro — Annual
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

**How to run:**
- Use PostHog feature flags to control which price is shown in the paywall CTA copy (e.g., "Unlock for $X/month").
- RevenueCat pricing experiments if integrated; otherwise use StoreKit 2 native A/B with App Store Connect pricing tiers.
- Do not change the product ID — change the displayed price only (within the App Store pricing tier system).

### RunSmart Price Experiment

- Variants (3-way): Annual at price A vs B vs C (set actual $ values from market positioning after cohort 1)
- Primary metric: `subscription_started` within 7 days of `paywall_shown`
- Secondary metric: 30-day retention of subscribers
- Minimum sample: 100 paywall exposures per variant before reading
- Duration: run until 95% statistical significance or 6 weeks, whichever comes first
- Decision: pick the variant with highest `subscription_started` rate, weighted by 30-day retention

### Resumely Price Experiment

- First experiment: weekly vs monthly as the CTA default (which tier drives higher total revenue)
- Second experiment: price of the default tier (set actual $ after cohort 1)
- Primary metric: `subscription_started` within 3 days of `paywall_shown` (shorter window; job seekers decide fast)
- Minimum sample: 100 paywall exposures per variant
- Duration: run until 95% statistical significance or 4 weeks

**Logging:** Log experiment start, winner, and decision in EXECUTIVE-DECISIONS.md when the experiment runs.
