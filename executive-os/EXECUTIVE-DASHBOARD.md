# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-07-09 IDT (Monthly CFO Review run this date — see Financial Snapshot)

## Executive Summary

RunSmart iOS — PHASE 2 — Activation diagnostics + record-run polish follow-ups (WP-38 closed): S13 only if HealthKit accuracy gate clears; otherwise next work packet from Agentic OS · Resumely iOS — Post-launch — activation measurement is hardened; WP-37 S1/S4 shipped to `main`; S2/S3/S5 are web-side (separate repo), already shipped per that repo's progress log: Founder submits 1.4.1 (11); then re-read the PostHog picker→file-selected funnel 7-14d post-1.4 for a real cohort · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

## CEO Focus

- RunSmart iOS: WP-40 (HealthKit activation & discoverability) in progress — S1 moves the real Connect action out of Profile into the primary post-onboarding flow. Directly targets the plan→run activation break ahead of the 2026-07-12 re-read.
- Resumely iOS: founder submits 1.4.1 (11) to ASC, then re-read the PostHog picker→file-selected funnel 7-14d post-1.4 for a real cohort.
- Distribution: WP-31 (Hebrew ASO, founder-approved) and WP-32 (Resumely FB-groups posting, founder-requested) are ready to execute but not yet reflected in `distribution-os/weekly-growth-review.md` (log stale since week of 2026-06-21) — close that gap before next Distribution Review.

## Financial Snapshot

Needs Data - no revenue/cost instrumentation wired. Monthly CFO Review run 2026-07-09 (first run of this workflow): all revenue, cost, margin, and runway lines remain `Needs Data`; only known figure is $0 marketing spend (default, no paid ads). Top recommendation: build a one-time manual cost list before next review. Full report: `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Open Decisions

- RunSmart iOS: WP-40 build has started per founder confirmation (2026-07-09) — EXD-021 flagged HealthKit as "a direction, not yet a scoped work packet... founder to confirm before build starts"; that condition is now satisfied, noted on EXD-021.
- Portfolio hygiene: 13 stranded-work items across 5 repos (`PROJECT-STATUS.md` Stranded Work), including Agentic OS's own 9 uncommitted files — decide whether to run a cleanup packet now or explicitly hold until after the 2026-07-12 activation re-read.
- RunSmart Web: Garmin's 9 `reauth_required` users have no maintenance-mode-compatible fix (per WP-26/27/28 status) — restoration is gated on the founder's עוסק מורשה registration completing (EXD-017/EXD-021), no fixed date yet.

## Status Confidence

How much each project's state is backed by parsed local task files versus narrative only.

| Project | Confidence | Source | Last Validation |
| --- | --- | --- | --- |
| RunSmart iOS | High | tasks/progress.md | 2026-07-09 — WP-38 S14 Debug build **SUCCEEDED** post-review; PR #83 merged to `f9d7c89` |
| Resumely iOS | High | tasks/progress.md | 2026-07-09 — Debug build **SUCCEEDED**; `.gstack/` gitignore hygiene fix committed (`597bf9f`); no new device QA since 2026-07-08 (`resume_upload_cta_seen/tapped`, `resume_file_picker_opened` PostHog QA rows still current from that date) |
| RunSmart Web | High | tasks/progress.md | 2026-07-03 — see Last Completed Story for today's checks. 2026-07-02 — credential-guard focused tests passed, 13 tests. Connection-gate focused Garmin suite passed, 36 tests; `npm run type-check` passed; targeted `npx eslint` on changed TS/TSX files exited 0 with 14 existing warnings in `components/device-connection-screen.tsx` and `components/profile-screen.tsx`. Read-only Vercel production env listing confirmed no `GARMIN_TEST_CLIENT_ID` / `GARMIN_TEST_CLIENT_SECRET`, no `GARMIN_CONNECT_ENABLED`, and no production env rotation |
| ResumeBuilder AI (Web) | High | tasks/progress.md | WP-29 S4 branch `codex/wp29-s4-disable-premium-cta` — focused pricing/upgrade tests 2/2 passed, `npm run check:i18n` passed, targeted eslint passed, full `npm run lint` passed with existing warnings only, `npm run build` passed. `npx tsc --noEmit` still fails on pre-existing contract/security test typing and stale export errors, none in touched S4 files |
| Agentic OS | High | tasks/progress.md | ./agentic-os verify passed with JSON, fallback sync, confidence, freshness, drift, packet hygiene, links, and git diff checks on 2026-06-12 |

## Risk Board

- RunSmart iOS: Re-check Finder `* 2.*` duplicates before next Release archive
- RunSmart iOS: physical lock-screen Live Activity capture still owed for S14b
- Resumely iOS: Missing `tasks/ERRORS.md` and `docs/agent-os/project-context.md` from required read list
- Resumely iOS: automated tapping of the system Files picker close button is blocked by app-scoped snapshots/no raw coordinate tap
- RunSmart Web: Garmin relaunch work is paused by decision, not blocked on founder action. `GARMIN_TEST_CLIENT_ID` / `GARMIN_TEST_CLIENT_SECRET` remain intentionally absent from production
- RunSmart Web: the WP-26 Internal Test app credentials stay non-production only, per WP-25's credential guard
- ResumeBuilder AI (Web): Gate A remains closed by decision
- ResumeBuilder AI (Web): do not wire Stripe or re-enable Premium CTAs until the gate is explicitly reopened

## Next Recommended Actions

1. RunSmart iOS: continue WP-40 S1-S4 (HealthKit connect into primary flow, auto-import, value surfacing, funnel verification); report per-story per the packet's completion gate.
2. Resumely iOS: founder submits 1.4.1 (11); then re-read the PostHog picker→file-selected funnel 7-14d post-1.4 for a real cohort.
3. Distribution: log the WP-31/WP-32 cycle into `distribution-os/weekly-growth-review.md` so the next Distribution Review has current data instead of the 2026-06-21 entry.
4. Portfolio hygiene: triage the 13 stranded-work items (`PROJECT-STATUS.md`), starting with Agentic OS's own 9 uncommitted files and ResumeBuilder AI Web's unpushed `fix/posthog-expert-event-dedupe` commit (2026-07-09, still fresh — push before it goes stale too).
5. Both apps: hold for the 2026-07-12 activation re-read before any monetization, paywall, or GTM-volume move (EXD-013, EXD-015).
6. Research (2026-07-11): competitor activation teardown filed at `executive-os/research/2026-07-11-competitor-activation-teardown.md` — next decision is whether to open a Resumely first-free-PDF export activation packet (Teal pattern) after founder confirm.
