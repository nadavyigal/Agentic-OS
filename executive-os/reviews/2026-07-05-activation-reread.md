# D7 Activation Readout #2 — 2026-07-05

Second portfolio D7 readout from live PostHog data. Methodology matches WP-17 / the 2026-06-24 baseline: founder, QA, bot, and known internal persons excluded before quoting organic numbers. Run by the founder via Cursor; filed here to close WP-17.

## Headline

| App | vs Readout #1 (2026-06-24) | Readout #2 (today) | Target | Verdict |
|---|---|---|---|---|
| RunSmart iOS | 0% (0/10 beta cohort) | 0% (0/12 mature organic) | ≥30% | First true App Store cohort. Still zero runs. |
| Resumely | 0% confirmed real organic (0/35) | 0% confirmed real organic (0/37 mature) | ≥40% | 2 new raw D7 completers; both founder-attributed. |

Portfolio call (unchanged from EXD-013): activation is still unproven on both apps. Do not unlock monetization, paid acquisition, or GTM volume yet.

## RunSmart iOS — PostHog project 171597

Canonical metric: `Application Installed → run_completed` within 7 days.

| Cohort | Denominator | D7 activated | Rate | Supporting funnel (7d window) |
|---|---|---|---|---|
| Mature organic (install 2026-06-19 to 2026-06-28) | 12 | 0 | 0% | onboarding 1/19 (5%), plan 1/19 (5%), run_started 0, run_completed 0 |
| All since App Store launch (install 2026-06-19+) | 19 | 0 | 0% | 7 users still inside D7 window (installed 2026-06-29+) |

What changed since readout #1: cohort definition shifted from pre-App Store beta/TestFlight (n=10) to first live App Store builds (1.0.3 live 2026-06-19). Sample grew, but activation did not move off zero. The plan→run gap persists: 1 user reached `plan_generated`, zero reached `run_started` or `run_completed`.

Acquisition trend (weekly installs): 2026-06-15: 3 · 2026-06-22: 9 · 2026-06-29: 7.

Exclusions: founder person IDs (`82f3c85c…`, `aa28b5c7…`) appear in identify events but are not in the `Application Installed` cohort — no founder installs detected in this cohort.

Named drop-off: Install → onboarding (94.7% drop). Plan → run is a complete wall (0%).

## Resumely — PostHog project 270848

Canonical metric: `first-seen (app_launched OR $pageview) → optimization_completed` within 7 days.

| Cohort | Denominator | D7 activated (cleaned) | Rate |
|---|---|---|---|
| Mature (first-seen ≤ 2026-06-28) | 37 | 0 | 0% |
| All since 2026-06-10 | 44 | 0 | 0% |

Exclusions applied: person `067544b5` (automation/bot, confirmed WP-16); persons `761e5b1b`, `a6441489`, `712cf425` (founder dogfood pattern — IL geo + posthog-node double-send, same logic as readout #1). PostHog cohort "Founder + QA exclusion" (id 394227) exists but email is not on event properties in this project; exclusions done by known person IDs.

Raw signal (before exclusion): 2 users hit D7 `optimization_completed` — `761e5b1b` (iOS, IL) and `a6441489` (posthog-node backend), both matching the founder-attribution pattern. iOS funnel (`app_launched → optimization_completed`, 7d window, test accounts filtered): 44 → 0 (0%).

Platform split (cleaned cohort): 46 iOS-first, 14 web-first users since 2026-06-10.

~~Supporting funnel (cleaned, all-time, not 7d-windowed): `guest_mode_started` 46 users ever engaged → `resume_upload_succeeded` **1 user ever** → `fit_check_completed` 19 → `optimization_completed` 4 (all founder/bot after attribution) → `export_success` 3.~~

~~Named drop-off: **upload is still the bottleneck.** Massive traffic reaches guest mode and fit-check, but almost nobody completes a real upload.~~

**CORRECTED same day (2026-07-05) — see Correction section below.** The line above used the wrong event name for uploads. Corrected funnel: `guest_mode_started` 46 → `resume_uploaded` (correct event) **8** → `optimization_completed` **2** → `export_success` **0**.

Named drop-off (corrected): **export is the bottleneck, not upload.** 8 real people uploaded a resume and 2 completed an optimization, but zero real (non-founder) people have ever exported in 60 days.

Acquisition trend (weekly `app_launched`): 2026-06-08: 6 · 2026-06-15: 16 · 2026-06-22: 28 · 2026-06-29: 5.

## OKR 2 check

| Target | Still valid? | Rationale |
|---|---|---|
| RunSmart ≥30% D7 activation | Hold | Right north star, but 0/12 mature with no run signal means the target is aspirational, not directional yet. |
| Resumely ≥40% D7 activation | Hold | Same. 0/37 mature real organic. Corrected 2026-07-05: optimization→export friction, not upload friction, is the leading hypothesis — see Correction section. WP-18 scope should be re-checked against this. |

## What this readout does NOT change

- EXD-013 stands: investigate activation now, not monetize/GTM.
- RunSmart plan→run diagnostic (WP-15) is still the priority product investigation.
- Resumely activation friction diagnostic (WP-18) is still the priority before new features — re-scoped same day from upload to optimization→export (see Correction section).
- Measurement integrity work (WP-30) is paying off on Resumely exclusions, but web `$pageview` attribution still needs clean platform splits in dashboards.

## Recommended next reads

- RunSmart: re-read 2026-07-12 when the 7 immature installs (2026-06-29 to 2026-07-03) mature.
- Resumely: re-read 2026-07-12 when the 7 immature users (first-seen after 2026-06-28) mature. Watch whether any non-founder user hits `resume_uploaded` or `export_success`.

## Correction — 2026-07-05 (same day, found while rebuilding the vault activation dashboard)

**Bug:** the original "Supporting funnel" line above cited `resume_upload_succeeded` for the upload step. Root cause identified precisely (not just a naming duplicate): `resume_upload_succeeded` is **new instrumentation shipped by WP-18** (PR #80, still "In Review" / not yet broadly merged/live) — one of 9 new upload-journey events WP-18 added to fill in what its own diagnosis called a "measurement black box." It has only 13 events / 1 distinct person all-time because it isn't live for most users yet, not because upload is rare. The actual established terminal upload event — the one WP-18's own 2026-06-24 diagnosis confirmed as "the terminal event that fires" — is `resume_uploaded` (90 events / 11 distinct people all-time, 87 iOS + 3 web). Readout #2 queried the not-yet-rolled-out event instead of the established one.

**Verification (live HogQL, project 270848, 60-day window):**

| Event | Total events | Distinct people (all-time) |
|---|---|---|
| `guest_mode_started` | 119 | 48 |
| `fit_check_completed` | 104 | 19 |
| `resume_uploaded` (correct) | 90 | 11 |
| `optimization_started` | 50 | 4 |
| `resume_upload_started` | 22 | 1 |
| `export_success` | 20 | 3 |
| `resume_upload_succeeded` (WP-18's new event, PR #80 still in review — do not use until merged/live) | 13 | 1 |
| `resume_upload_failed` | 3 | 1 |

Founder/QA/bot exclusion applied to distinct people per event (excluding `a6441489` = nadav.yigal@gmail.com, `761e5b1b`, `712cf425` = founder dogfood pattern, `067544b5` = automation/bot):

- `resume_uploaded`: 11 distinct → **8 clean**.
- `optimization_completed`: 6 distinct (`a6441489`, `761e5b1b`, `712cf425`, `067544b5`, `eb943c28`, `1c4937d7`) → **2 clean** (`eb943c28`, `1c4937d7` — no email captured on these persons, so this identification rests on process of elimination against the known founder/bot IDs, not a positive confirmation; flag for the next readout to double-check).
- `export_success`: 3 distinct (`a6441489`, `761e5b1b`, `712cf425`) → **0 clean**. All three exports in the last 60 days are founder-pattern accounts.

**Corrected all-time funnel (founder/QA/bot excluded):** `guest_mode_started` 46 → `resume_uploaded` 8 → `optimization_completed` 2 → `export_success` 0.

**What this changes:** the narrative flips from "almost nobody uploads" to "uploads and optimizations happen at a real (if low) rate, but nobody has ever exported." This reconciles the original discrepancy (upload count 1 vs optimization count 4, which is logically impossible) and is closer to — though not identical to — the 2026-07-03 30-day funnel's "9 uploaded" figure (different window and slightly different exclusion set, but same order of magnitude, unlike the "1 ever" figure this replaces).

**Action:** WP-18 (Resumely upload/import friction diagnostic) should be re-checked — its scope may need to shift toward the optimization→export step, since the corrected data shows upload is not the near-total wall it was reported as. Not re-scoped in this file; flagged for whoever picks up WP-18 next.
