# Metrics Schema

Canonical metric names and definitions used by `metrics-dashboard.md`, Notion Metrics Log, and every report.

## Naming Rule

`{product}.{stage}.{metric_name}` — lowercase, dot-separated, no spaces.

Examples:

- `runsmart.acquisition.app_store_conversion_rate`
- `runsmart.activation.first_plan_generated`
- `runsmart.retention.week1_adherence`
- `resumebuilder.acquisition.organic_search_clicks`
- `resumebuilder.activation.first_export`
- `resumebuilder.monetization.paid_conversion_rate`

## Stages

| Stage | Definition |
|---|---|
| `acquisition` | Reaching and getting attention from a qualified user |
| `activation` | First meaningful product use |
| `retention` | Continued use over time |
| `revenue` | Money in (paid users, MRR, ARR) |
| `referral` | User-driven acquisition (referrals, organic shares) |

## Canonical Metrics

### RunSmart

| Name | Definition | Source | Unit |
|---|---|---|---|
| `runsmart.acquisition.app_store_impressions` | Total impressions of the App Store product page | App Store Connect | count |
| `runsmart.acquisition.app_store_install_rate` | Installs / product page views | App Store Connect | percentage |
| `runsmart.acquisition.app_store_keyword_rank.{keyword}` | Daily ranking position for a tracked keyword | App Store Connect | integer (1 best) |
| `runsmart.acquisition.web_landing_to_appstore_click_rate` | App Store CTA clicks / page views | PostHog | percentage |
| `runsmart.activation.first_open_to_onboarding_complete` | % of first-opens completing onboarding | PostHog | percentage |
| `runsmart.activation.first_plan_generated` | % of new physical App Store installers generating a first plan; leading first-value metric | PostHog | percentage |
| `runsmart.activation.first_run_committed` | % of plan-generated users choosing Start now or Remind me in the shipped first-run CTA; verified-value metric | PostHog | percentage |
| `runsmart.activation.first_run_logged` | % of new physical App Store installers reaching `run_completed` within 7 days; primary activation | PostHog | percentage |
| `runsmart.retention.week1_adherence` | Planned sessions completed / prescribed in week 1 | App backend | percentage |
| `runsmart.retention.second_planned_workout_14d` | % of activated users completing a second planned workout within 14 days | App backend / PostHog | percentage |
| `runsmart.retention.weekly_active_runners` | Distinct runners with a session in trailing 7 days | App backend / PostHog | count |
| `runsmart.revenue.paid_users` | Active paid subscribers | App Store / Stripe | count |
| `runsmart.revenue.mrr` | Monthly recurring revenue | App Store / Stripe | currency |

### ResumeBuilder

| Name | Definition | Source | Unit |
|---|---|---|---|
| `resumebuilder.acquisition.organic_search_impressions` | Search Console impressions | Search Console | count |
| `resumebuilder.acquisition.organic_search_clicks` | Search Console clicks | Search Console | count |
| `resumebuilder.acquisition.indexed_pages` | URLs in index | Search Console | count |
| `resumebuilder.acquisition.signups` | Distinct accounts created | Supabase / PostHog | count |
| `resumebuilder.acquisition.directory_referrals` | Signups attributed to a directory referrer | PostHog (utm) | count |
| `resumebuilder.activation.first_resume_started` | % of new first-seen users supplying resume input and adding a job; setup diagnostic | PostHog | percentage |
| `resumebuilder.activation.first_job_diagnosis` | % of new first-seen users reaching `free_ats_completed` or the first job-specific diagnosis; first-value metric | PostHog | percentage |
| `resumebuilder.activation.first_optimized_viewed` | % of optimization completers reaching `optimized_viewed`; verified-value metric | PostHog | percentage |
| `resumebuilder.activation.first_resume_exported` | % of new first-seen users reaching `export_success` within 7 days; primary activation | PostHog | percentage |
| `resumebuilder.activation.signup_to_export_median` | Median time from first seen to first successful export | PostHog | hours |
| `resumebuilder.retention.returned_within_14_days` | % of activated users returning or starting another job/resume cycle within 14 days | PostHog | percentage |
| `resumebuilder.revenue.paid_conversion_rate` | Paid users / signups | Stripe + PostHog | percentage |
| `resumebuilder.revenue.mrr` | MRR | Stripe | currency |

## When Adding A New Metric

1. Place it under the correct product and stage
2. Use the naming rule
3. Add it to `metrics-dashboard.md` table
4. Add the canonical row here
5. If it replaces an older metric, keep both for one month, then retire

## Comparison Rules

- Compare period to period of equal length (week vs week, month vs month)
- Use trailing windows for retention (trailing 7-day active, not Mon–Sun)
- Cohort-based metrics by signup week, not by event week
- For seasonality-sensitive metrics, also compare to same period prior year if data exists

## Anomaly Threshold

Default thresholds for flagging in `analyze-growth-results.md`:

- Rate metrics: >= 20% relative change from 4-week average
- Count metrics: >= 30% relative change from 4-week average
- New low for a retention metric: always flag
- New high for a revenue metric: confirm attribution before celebrating
