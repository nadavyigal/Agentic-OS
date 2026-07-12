# Distribution Command Center

The single page that answers: what is this week about, what is shipping, what is blocked. Update at the start and end of every distribution cycle. The Notion Command Center database mirrors this — Notion is the dashboard, this file is the source the agent reads.

## This Week

- **Week of**: 2026-07-07
- **Focused product**: ResumeBuilder iOS (Hebrew-first distribution — WP-31 ASO, WP-32 community)
- **Other product status**: RunSmart iOS — activation-gated, not distribution-gated; WP-40 HealthKit activation in progress, GTM volume on hold until plan→run activation improves
- **Theme**: Log the WP-31 (Hebrew ASO) and WP-32 (Facebook-groups community) experiments into the distribution cycle — both were founder-approved/requested on 2026-07-04/05 but had not yet been reflected in `experiment-log.md` or `weekly-growth-review.md`.
- **Top 3 experiments** (link to rows in `experiment-log.md`):
  1. rb-he-aso-001 — Hebrew ASO pass (WP-31); founder-approved, asset pack not yet drafted
  2. rs-onboarding-001 (score 21) — WP-40 HealthKit activation now supersedes this as the live RunSmart activation lever; first-run commitment work stays queued behind it
  3. rb-he-comm-001 — closed inconclusive 2026-07-12; 3 reactions and 1 comment across 3 posts, no qualitative feedback, ASC lift unknown; do not repeat without trackable links and verified analytics access
- **Assets in flight**:
  - `distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-onboarding-review/onboarding-review.md` — reviewed, needs founder approval before product work
  - `distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-aso-003-listing-audit/aso-review.md` — reviewed, needs founder approval before ASC / app changes
  - WP-31 Hebrew ASO asset pack (subtitle, keywords, promo text, 5 captions, reviewer note) — not yet drafted in `distribution-os/projects/resumebuilder/scaffold/drafts/`
- **Awaiting founder action**:
  - `rs-onboarding-001` is now `executive-os/work-packets/WP-20-runsmart-first-run-activation-build.md`; hold behind WP-40 per EXD-021.
  - Export App Store Connect Israeli storefront baseline (installs) so WP-31/WP-32 before/after comparisons are possible.
  - Confirm RTL PDF export status with product QA before any Hebrew ASO copy references it (WP-31 blocker).
  - Supply/confirm the WP-32 target-group shortlist and log manual engagement (comments/reactions/replies) for the 3 posted groups before the 2026-07-12 window closes.
- **Awaiting external response**:
  - App Store Connect Israeli storefront install data for the 2026-07-05 → 2026-07-12 WP-32 window.
  - App Store Connect metrics export for the live RunSmart listing.
- **Blocked**:
  - WP-31 asset drafting has not started — no draft post/copy pack filed yet despite founder approval.
  - No App Store metadata, screenshot, notification, review-prompt, or Hebrew ASO copy change should publish without explicit founder approval.

## Current Channel Status

### RunSmart

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | reviewed | Founder — approve metadata/screenshot/review-prompt next steps | rs-aso-003 audit found stale repo metadata vs live ASC, zero ratings, and missing screenshot captions |
| Onboarding / activation | queued | RunSmart iOS — execute WP-20 | rs-onboarding-001 found onboarding completion healthy, but app launch → onboarding start and plan → run are the leaks |
| Landing pages (PLG) | paused | Agent — later focus week | Resume after ASO baseline and first-run activation path are clearer |
| LinkedIn founder updates | draft | Founder — review existing launch post when useful | Not the binding constraint this week |
| Running SEO | not started | Agent — next focus week | |
| Runna comparison | not started | Agent — plan next | |
| Garmin / Strava content | not started | Agent — plan next | |
| Beginner challenges | paused | — | Conditional on challenge feature ship |
| Partnerships | paused | Agent — next focus week | Wait for conversion baseline before outreach |
| Lifecycle email | planned | Product session | Revisit after first-run reminder path is approved |
| Community research | not started | — | Observation only |

### ResumeBuilder

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | awaiting review | Founder — review rb-aso-001 listing copy + rb-aso-002 screenshot brief | Listing copy v1 drafted 2026-05-28; subtitle/keywords/description ready for review |
| Web landing pages with App Store CTA | not started | Agent — next focus week | iOS-first model; every mobile CTA points to App Store |
| Free ATS tool (web → app) | not started | Agent — confirm scope with founder | Web tool result page hands off to App Store install |
| Directories | awaiting review | Founder — review directory pack; press submit after App Store live | rb-dir-001 pack drafted for 5 directories; blocked on App Store URL |
| Lifecycle email | not started | Agent — next focus week | Needs analytics instrumentation first |
| Conversion optimization | not started | Agent — next focus week | Signup → editor → export funnel |
| Hebrew market | measuring | Founder — log WP-32 engagement; Agent — draft WP-31 asset pack | WP-31 (Hebrew ASO) founder-approved, not yet drafted; WP-32 (FB-groups) posted 2026-07-05 in 3 groups, 7-day window closes 2026-07-12 |
| Programmatic SEO | not started | Agent — after ASO proves | Demoted to Tier B until ASO + landings prove install |
| Career coach partnerships | not started | Agent — next focus week | |
| LinkedIn job-seeker content | not started | Deferred | Tier C |

Status values: `not started` · `planned` · `in progress` · `awaiting review` · `approved` · `published` · `measuring` · `learned` · `paused` · `killed`

## Last Week's Decisions

- 2026-05-27: Screenshot A variants approved for all 5 slots (rs-aso-002 ready to render)
- 2026-05-27: Garmin description sentence approved; full description draft filed (rs-aso-001 ready to apply)
- 2026-05-27: v1.0 ships free; paid tier TBD
- 2026-05-27: Android out of scope for 2026; Hebrew ASO in scope
- 2026-05-27: Email platform = Resend via Supabase Edge Functions (free 3K/mo)
- 2026-05-28: Distribution scaffold installed in both product repos — RunSmart iOS (missing scaffold files added; curated files preserved) and ResumeBuilder Web (full scaffold v1)
- 2026-07-04: Founder approved `hebrew-first-playbook.md`; `rb-he-aso-001` promoted to WP-31 (Hebrew ASO pass)
- 2026-07-05: Founder requested and manually posted `rb-he-comm-001` (WP-32, Facebook-groups) in 3 Israeli job-seeker/tech groups, ahead of WP-31 publishing (explicit sequencing override, noted in WP-32)
- 2026-07-12: `rb-he-comm-001` closed inconclusive. The posts generated 3 visible reactions and 1 comment total; ASC install lift could not be read. Future community tests require unique per-group campaign links and analytics access confirmed before publishing.

## This Week's Done Definition

A week is done when:

1. The weekly cycle workflow has been run end to end
2. The top 3 experiments either have approved assets or are explicitly deferred
3. `weekly-growth-review.md` has the week's report appended
4. `experiment-log.md` and `metrics-dashboard.md` are current
5. The Notion Command Center is synced with this file
