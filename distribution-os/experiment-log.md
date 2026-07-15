# Experiment Log

Source of truth for distribution experiments at the cross-product level. Notion's Experiment Backlog database mirrors this. When a row changes status, update both.

Schema reference: `data/experiment-schema.md`. Template: `templates/experiment-card-template.md`. Scoring: see "Experiment Scoring" below.

## Active

| ID | Product | Channel | Hypothesis | Metric | Score | Status | Start | End |
|---|---|---|---|---|---|---|---|---|
| rs-aso-001 | RunSmart | ASO | Rewriting the App Store description with approved Garmin sentence and tighter opening will produce a clear, credible listing that converts at ≥35% (product page → install) after first 100 impressions | App Store product page → install conversion rate | 24 | awaiting review | — | — |
| rs-analytics-001 | RunSmart | Analytics infra | Instrumenting onboarding_completed, plan_generated, and run_logged before launch will make the first 30 days of installs measurable, enabling data-driven iteration from week 2 | Activation funnel measurable in PostHog (all 3 events firing in production) | 22 | awaiting review | — | — |
| rs-onboarding-001 | RunSmart | Onboarding | Moving users from plan_generated to first run with a concrete first-run commitment and local reminder will improve first-run activation before D7 can be evaluated | Ordered clean funnel: plan_generated → first_run_cta_tapped → reminder/run_started → run_completed | 21 | shipped in 1.0.7 (21) — measuring clean cohort | 2026-06-30 | — |
| rb-cro-001 | ResumeBuilder Web | CRO | The six WP-43 Tier A entry-funnel changes will increase the share of qualified landers who submit the free checker | `ats_checker_hero_cta_clicked → ats_checker_submitted` | unscored | shipped in PR #115 — measuring | 2026-07-11 | — |
| rs-aso-003 | RunSmart | ASO | Post-launch ASO cleanup, first-review prompt, subtitle/keyword review, and screenshot captions will improve App Store product page → install conversion once baseline impressions exist | App Store product page → install conversion rate; rating count | 20 | reviewed — founder action needed | — | — |
| rs-aso-002 | RunSmart | ASO | Adding approved A-variant caption overlays to all 5 screenshot slots will improve App Store conversion rate vs bare UI screenshots, measured at next keyword report | App Store product page → install conversion rate (compare pre/post in App Store Connect) | 18 | awaiting review | — | — |
| rs-email-001 | RunSmart | Lifecycle email | Sending welcome + plan-nudge + 2-day no-show emails via Resend/Supabase will increase week-1 activation rate (plan generated → first run logged) vs no email baseline | Week-1 activation rate in PostHog (target ≥60% of plan-generated users log first run within 7 days) | 17 | awaiting product session | — | — |
| rb-aso-001 | ResumeBuilder iOS | ASO | Writing the Resumely App Store listing (subtitle Option A, keywords field v1, description v1) will produce a conversion-optimised listing ready for first submission and establish a baseline for subsequent A/B iteration | App Store product page → install conversion rate; keyword impressions on tracked terms after listing goes live | 21 | approved — ready to file in ASC | — | — |
| rb-aso-002 | ResumeBuilder iOS | ASO | Producing a 5-slot screenshot brief with keyword-rich captions (indexed since 2025) and structured copy overlays will give the listing strong visual conversion signals from day one | App Store product page → install conversion rate (compare vs no-screenshot baseline) | 20 | approved — screenshots exported; PR #34 ready to merge; upload to ASC pending | — | — |
| rb-dir-001 | ResumeBuilder iOS | Directory | Submitting Resumely to 5 AI/career directories (Futurepedia, TAAFT, Toolify, AI Tool Hunt, Launching Next) will produce initial backlinks and referral traffic to the web funnel that feeds App Store installs | Directory referral sessions in Search Console / Vercel; backlinks indexed in Google Search Console | 15 | awaiting review + App Store URL | — | — |
| rb-he-aso-001 | ResumeBuilder iOS | Hebrew ASO | Publishing a Hebrew subtitle, keyword field, promo text, and 5 screenshot captions (Fit-First framing, per WP-31) will improve Israeli storefront App Store product page → install conversion within a 21-day measurement window | App Store Connect Israeli storefront install rate, before/after | unscored (see `hebrew-first-playbook.md` experiment menu) | published — measuring; founder-confirmed live 2026-07-15, actual publish timestamp and ASC baseline unlogged | unknown (live by 2026-07-15) | TBD — 21 days after actual publish date |

## Queued (Approved, Not Started)

| ID | Product | Channel | Hypothesis | Metric | Score | Decided At |
|---|---|---|---|---|---|---|

## Evidence-Gated (Not Started)

| ID | Product | Channel | Gate | Metric | Status |
|---|---|---|---|---|---|
| rb-cro-002 | Resumely iOS | CRO | On/after 2026-07-18: at least 3 of 5 relevant observed users lack a usable local resume file; otherwise target the measured downstream step | Share reaching first diagnosis without selecting a file; overall D7 export activation | WP-44 S2 gated — no UI/API work before gate |

## Done — Worked

| ID | Product | Channel | Hypothesis | Result Summary | Lesson Captured? |
|---|---|---|---|---|---|

## Done — Did Not Work

| ID | Product | Channel | Hypothesis | Result Summary | Lesson Captured? |
|---|---|---|---|---|---|
| rb-he-comm-001 | ResumeBuilder iOS | Community (Facebook groups) | Founder posting a Hebrew, Fit-First-framed post in 3 Israeli job-seeker/tech Facebook groups will produce measurable Israeli storefront install lift plus qualitative engagement within 7 days | Went live 2026-07-05; closed inconclusive 2026-07-12 with 3 visible reactions and 1 comment across 3 posts, no visible qualitative product feedback, and no available ASC Israeli-storefront before/after comparison. The experiment failed to produce a measurable answer, not proof the channel cannot work. | Yes — require unique per-group campaign links, verified analytics access before publish, and a same-day manual log. See WP-32 and `hebrew-first-playbook.md`. |

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
