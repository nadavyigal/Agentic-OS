# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-07-08 IDT

## Executive Summary

RunSmart iOS — PHASE 2 — Activation diagnostics + Garmin maintenance (EXD-015): Re-run PostHog funnel on **2026-07-08+** for build-21-only users (`filterTestAccounts=true`). WP-34 closed/parked per EXD-019 — not a pending decision. Then WP-27 Gate-4 screenshots if Garmin path resumes · Resumely iOS — Post-launch — activation measurement hardening before export/paywall/monetization work: Complete Story 1 authenticated QA smoke with a reliable credential/device or fix secure-field automation, then update PostHog evidence before starting Story 2 · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

## CEO Focus

- Resumely iOS: founder device smoke on iPhone 13, then Xcode Organizer archive + ASC upload.
- RunSmart iOS: monitor build 8 review — approved triggers GTM; rejected triggers minimal fix as build 9.
- RunSmart iOS: GTM plan at .agent-os/distribution/gtm-plan.md is ready to activate on approval.

## Financial Snapshot

Needs Data - no revenue/cost instrumentation wired.

## Open Decisions

- RunSmart iOS: if build 8 rejected again, decide minimal fix scope vs. expanding v2 feature set before resubmit.
- RunSmart iOS: when to flip VOICE_COACH_ENABLED=true in Vercel (voice coach is in build 8 but feature flag is off).
- ResumeBuilder Web: defer rollout unless Resumely smoke exposes backend blockers.

## Status Confidence

How much each project's state is backed by parsed local task files versus narrative only.

| Project | Confidence | Source | Last Validation |
| --- | --- | --- | --- |
| RunSmart iOS | High | tasks/progress.md | 2026-07-05 — Release archive **SUCCEEDED** (clean worktree, ~10 min). ASC upload **SUCCEEDED** (`ExportOptionsAppStoreUpload.plist`). Archive metadata: `RunSmart` / `com.runsmart.lite` / `1.0.7` / `21` / `ITSAppUsesNonExemptEncryption=false` / dSYM present. Known HKWorkout deprecation warning only |
| Resumely iOS | High | tasks/progress.md | 2026-07-06 — focused `AnalyticsServiceTests` 12/12; full simulator suite 121 passed, 1 skipped, 0 failed; Debug simulator build succeeded; PostHog project `270848` confirmed fresh `app_launched` rows with `app=resumely_ios`, `marketing_version=1.3`, `build_number=8`, `anonymous_session_id`, and `is_internal_tester=true` |
| RunSmart Web | High | tasks/progress.md | 2026-07-03 — see Last Completed Story for today's checks. 2026-07-02 — credential-guard focused tests passed, 13 tests. Connection-gate focused Garmin suite passed, 36 tests; `npm run type-check` passed; targeted `npx eslint` on changed TS/TSX files exited 0 with 14 existing warnings in `components/device-connection-screen.tsx` and `components/profile-screen.tsx`. Read-only Vercel production env listing confirmed no `GARMIN_TEST_CLIENT_ID` / `GARMIN_TEST_CLIENT_SECRET`, no `GARMIN_CONNECT_ENABLED`, and no production env rotation |
| ResumeBuilder AI (Web) | High | tasks/progress.md | WP-29 S4 branch `codex/wp29-s4-disable-premium-cta` — focused pricing/upgrade tests 2/2 passed, `npm run check:i18n` passed, targeted eslint passed, full `npm run lint` passed with existing warnings only, `npm run build` passed. `npx tsc --noEmit` still fails on pre-existing contract/security test typing and stale export errors, none in touched S4 files |
| Agentic OS | High | tasks/progress.md | ./agentic-os verify passed with JSON, fallback sync, confidence, freshness, drift, packet hygiene, links, and git diff checks on 2026-06-12 |

## Risk Board

- RunSmart iOS: (1) Post-fix cohort not yet measurable same-day as upload. (2) Local main worktree has Finder duplicate `* 2.swift` files that block archive — release built from clean detached worktree at `6ed8b97`
- RunSmart iOS: clean duplicates before next local archive
- Resumely iOS: Simulator secure password entry via MCP UI automation did not enter a valid password, so no fresh PostHog `$create_alias` / `$identify` row was captured
- Resumely iOS: missing `tasks/ERRORS.md` and `docs/agent-os/project-context.md` from required read list
- RunSmart Web: Garmin relaunch work is paused by decision, not blocked on founder action. `GARMIN_TEST_CLIENT_ID` / `GARMIN_TEST_CLIENT_SECRET` remain intentionally absent from production
- RunSmart Web: the WP-26 Internal Test app credentials stay non-production only, per WP-25's credential guard
- ResumeBuilder AI (Web): Gate A remains closed by decision
- ResumeBuilder AI (Web): do not wire Stripe or re-enable Premium CTAs until the gate is explicitly reopened

## Next Recommended Actions

1. RunSmart iOS: Re-run PostHog funnel on **2026-07-08+** for build-21-only users (`filterTestAccounts=true`). Then WP-27 Gate-4 screenshots if Garmin path resumes
1. Resumely iOS: Complete Story 1 authenticated QA smoke with a reliable credential/device or fix secure-field automation, then update PostHog evidence before starting Story 2
