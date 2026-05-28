# Distribution Command Center

The single page that answers: what is this week about, what is shipping, what is blocked. Update at the start and end of every distribution cycle. The Notion Command Center database mirrors this — Notion is the dashboard, this file is the source the agent reads.

## This Week

- **Week of**: 2026-05-27
- **Focused product**: RunSmart
- **Other product status**: scaffold installation sprint (ResumeBuilder — scaffold populated + installed in web repo 2026-05-28; first ASO session ready to run)
- **Theme**: ASO finalization — lock the listing and analytics before App Store submission
- **Top 3 experiments** (link to rows in `experiment-log.md`):
  1. rs-aso-001 (score 24) — Description rewrite with approved Garmin sentence
  2. rs-analytics-001 (score 22) — Instrument activation funnel events before launch
  3. rs-aso-002 (score 18) — Screenshot caption overlays (A variants approved)
- **Assets in flight**:
  - `distribution-os/projects/runsmart/scaffold/drafts/2026-05-27-rs-aso-001/description.txt` — approved description draft, ready to copy to fastlane
  - `RunSmart iOS/.agent-os/distribution/screenshot-overlay-copy.md` — approved A variants, ready to render
  - `RunSmart iOS/.agent-os/distribution/analytics-instrumentation-spec.md` — ready for product-code session
  - `ResumeBuilder Web/.agent-os/distribution/` — scaffold v1 installed 2026-05-28; first ASO session ready
- **Awaiting founder review**:
  - rs-aso-001: copy `drafts/2026-05-27-rs-aso-001/description.txt` → `fastlane/metadata/en-US/description.txt`
  - rs-aso-002: render screenshot overlays from approved copy table
  - rs-analytics-001: execute spec in a product-code session
- **Awaiting external response**:
  - App Store review submission — target submit 2026-06-01 (soft; may slip if overlays or analytics not done)
  - App Store review process: expect 24–48h after submission
- **Blocked**:
  - All acquisition metrics blocked until App Store submit + review approval
  - Email rs-email-001 blocked until rs-analytics-001 (analytics) done — need user events to fire before email triggers are meaningful

## Current Channel Status

### RunSmart

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | in progress | Founder — copy description.txt, render overlays, submit | Build uploaded 2026-05-19; rs-aso-001 + rs-aso-002 assets ready |
| Landing pages (PLG) | not started | Agent — next focus week | Blocked on App Store submission first |
| LinkedIn founder updates | not started | Founder — write + post | Deferred to launch week |
| Running SEO | not started | Agent — next focus week | |
| Runna comparison | not started | Agent — plan next | |
| Garmin / Strava content | not started | Agent — plan next | |
| Beginner challenges | paused | — | Conditional on challenge feature ship |
| Partnerships | not started | Agent — next focus week | |
| Lifecycle email | planned | Product session | 3 email drafts ready; Resend + Supabase spec ready |
| Community research | not started | — | Observation only |

### ResumeBuilder

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | not started | Agent — first ASO session | Scaffold installed 2026-05-28; app-store-program.md needs real metadata from iOS repo |
| Web landing pages with App Store CTA | not started | Agent — next focus week | iOS-first model; every mobile CTA points to App Store |
| Free ATS tool (web → app) | not started | Agent — confirm scope with founder | Web tool result page hands off to App Store install |
| Directories | not started | Agent — use directories.md + workflow 06 | 10-directory first-pass list ready in scaffold |
| Lifecycle email | not started | Agent — next focus week | Needs analytics instrumentation first |
| Conversion optimization | not started | Agent — next focus week | Signup → editor → export funnel |
| Hebrew market | not started | Agent — confirm RTL + pricing first | RTL PDF and pricing decisions blocking |
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

## This Week's Done Definition

A week is done when:

1. The weekly cycle workflow has been run end to end
2. The top 3 experiments either have approved assets or are explicitly deferred
3. `weekly-growth-review.md` has the week's report appended
4. `experiment-log.md` and `metrics-dashboard.md` are current
5. The Notion Command Center is synced with this file
