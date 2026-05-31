# Experiment Log

Source of truth for distribution experiments at the cross-product level. Notion's Experiment Backlog database mirrors this. When a row changes status, update both.

Schema reference: `data/experiment-schema.md`. Template: `templates/experiment-card-template.md`. Scoring: see "Experiment Scoring" below.

## Active

| ID | Product | Channel | Hypothesis | Metric | Score | Status | Start | End |
|---|---|---|---|---|---|---|---|---|
| rs-aso-001 | RunSmart | ASO | Rewriting the App Store description with approved Garmin sentence and tighter opening will produce a clear, credible listing that converts at ≥35% (product page → install) after first 100 impressions | App Store product page → install conversion rate | 24 | awaiting review | — | — |
| rs-analytics-001 | RunSmart | Analytics infra | Instrumenting onboarding_completed, plan_generated, and run_logged before launch will make the first 30 days of installs measurable, enabling data-driven iteration from week 2 | Activation funnel measurable in PostHog (all 3 events firing in production) | 22 | awaiting review | — | — |
| rs-aso-002 | RunSmart | ASO | Adding approved A-variant caption overlays to all 5 screenshot slots will improve App Store conversion rate vs bare UI screenshots, measured at next keyword report | App Store product page → install conversion rate (compare pre/post in App Store Connect) | 18 | awaiting review | — | — |
| rs-email-001 | RunSmart | Lifecycle email | Sending welcome + plan-nudge + 2-day no-show emails via Resend/Supabase will increase week-1 activation rate (plan generated → first run logged) vs no email baseline | Week-1 activation rate in PostHog (target ≥60% of plan-generated users log first run within 7 days) | 17 | awaiting product session | — | — |
| rb-aso-001 | ResumeBuilder iOS | ASO | Writing the Resumely App Store listing (subtitle Option A, keywords field v1, description v1) will produce a conversion-optimised listing ready for first submission and establish a baseline for subsequent A/B iteration | App Store product page → install conversion rate; keyword impressions on tracked terms after listing goes live | 21 | approved — ready to file in ASC | — | — |
| rb-aso-002 | ResumeBuilder iOS | ASO | Producing a 5-slot screenshot brief with keyword-rich captions (indexed since 2025) and structured copy overlays will give the listing strong visual conversion signals from day one | App Store product page → install conversion rate (compare vs no-screenshot baseline) | 20 | approved — screenshots exported; PR #34 ready to merge; upload to ASC pending | — | — |
| rb-dir-001 | ResumeBuilder iOS | Directory | Submitting Resumely to 5 AI/career directories (Futurepedia, TAAFT, Toolify, AI Tool Hunt, Launching Next) will produce initial backlinks and referral traffic to the web funnel that feeds App Store installs | Directory referral sessions in Search Console / Vercel; backlinks indexed in Google Search Console | 15 | awaiting review + App Store URL | — | — |

## Queued (Approved, Not Started)

| ID | Product | Channel | Hypothesis | Metric | Score | Decided At |
|---|---|---|---|---|---|---|

## Done — Worked

| ID | Product | Channel | Hypothesis | Result Summary | Lesson Captured? |
|---|---|---|---|---|---|

## Done — Did Not Work

| ID | Product | Channel | Hypothesis | Result Summary | Lesson Captured? |
|---|---|---|---|---|---|

## Rejected (Not Worth Running)

| ID | Product | Channel | Hypothesis | Why Rejected |
|---|---|---|---|---|

## Experiment Scoring

Use the experiment card template. The formula:

```
Score = Impact + Confidence + Speed + FounderFit + StrategicFit - Effort
```

All dimensions 1–5. Effort is the only subtracted term. Bigger is better.

| Dimension | What it asks |
|---|---|
| Impact | If this works, how big is the win in users, revenue, or compounding leverage |
| Confidence | How sure are we from prior data, lessons, or precedent that this works |
| Speed | How fast can we know the answer |
| FounderFit | Does this fit the founder's preferred work style and skill |
| StrategicFit | Does this build a moat or compound across weeks |
| Effort | How much time and friction does this require |

| Decision | Threshold |
|---|---|
| Do now | Score >= 15 |
| Later (queue) | 10 <= Score < 15 |
| Reject | Score < 10 |

Tie breakers: prefer cheap reversibility, prefer channels the founder will maintain, prefer compounding over one-shot.

## ID Convention

`{product-prefix}-{channel-prefix}-{nnn}` where:

- `product-prefix`: `rs` (RunSmart) or `rb` (ResumeBuilder)
- `channel-prefix`: `aso`, `seo`, `pseo`, `li`, `dir`, `tool`, `email`, `part`, `cro`, `comm`
- `nnn`: 3 digits, sequential per product+channel

Example: `rs-aso-001`, `rb-pseo-007`
