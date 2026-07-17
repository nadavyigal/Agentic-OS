# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-07-17 IDT

## Executive Summary

RunSmart iOS — PHASE 2 — Release 1.0.8 (22) (WP-37/38/40 bundle): Monitor Apple review of build 8 (submitted 2026-06-03); check App Store Connect for outcome. · Resumely iOS — Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists: Founder: unlock iPhone 13 → install: xcrun devicectl device install app --device 4A1D6EF2-8945-55B8-931A-46980B2A27E2 '/var/tmp/resumebuilder-device-derived/Build/Products/Debug-iphoneos/ResumeBuilder IOS APP.app' · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

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
| RunSmart iOS | Unknown | none | Not parsed |
| Resumely iOS | Unknown | none | Not parsed |
| RunSmart Web | Unknown | none | Not parsed |
| ResumeBuilder AI (Web) | Unknown | none | Not parsed |
| Agentic OS | Medium | tasks/progress.md | Pending refreshed `./agentic-os morning` after the 2026-07-13 founder evidence reconciliation |

## Risk Board

- RunSmart iOS: None — awaiting Apple review
- Resumely iOS: PostHog read blocked on calendar (no post-live 1.4.1 traffic yet)
- Resumely iOS: missing `tasks/ERRORS.md` and `docs/agent-os/project-context.md` from required read list
- Resumely iOS: automated tapping of the system Files picker close button is blocked by app-scoped snapshots/no raw coordinate tap
- RunSmart Web: Garmin relaunch work is paused by decision, not blocked on founder action. `GARMIN_TEST_CLIENT_ID` / `GARMIN_TEST_CLIENT_SECRET` remain intentionally absent from production
- RunSmart Web: the WP-26 Internal Test app credentials stay non-production only, per WP-25's credential guard
- ResumeBuilder AI (Web): Gate A remains closed by decision
- ResumeBuilder AI (Web): do not wire Stripe or re-enable Premium CTAs until the gate is explicitly reopened

## Next Recommended Actions

1. RunSmart iOS: Monitor Apple review of build 8 (submitted 2026-06-03); check App Store Connect for outcome.
1. Resumely iOS: Founder: unlock iPhone 13 → install: xcrun devicectl device install app --device 4A1D6EF2-8945-55B8-931A-46980B2A27E2 '/var/tmp/resumebuilder-device-derived/Build/Products/Debug-iphoneos/ResumeBuilder IOS APP.app'
