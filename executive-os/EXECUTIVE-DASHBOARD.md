# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-06-05 IDT

## Executive Summary

RunSmart iOS — App Store Review: After review approval — merge version-2 to main, update PROJECT-STATUS.md, publish launch post · Resumely iOS — App Store submission readiness: Upload the screenshot folders in App Store Connect, then authorize the Apple Distribution key and upload the build · RunSmart Web — Sprint 11 backend support / reference · ResumeBuilder AI (Web) — PDF parse/render-preview rollout

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
| RunSmart iOS | High | tasks/progress.md | Build 8 archived and uploaded 2026-06-03. All tests passed. Visual QA passed on iPhone 17 Pro, iPhone 17 Pro Max, iPad Air 11-inch (M3). Onboarding scroll fix confirmed in code review and build. Bug review passed (checks A, B, E, F, G automated; checks C, D require manual verification after sign-in). Executive OS gate passed |
| Resumely iOS | High | tasks/progress.md | App Store screenshot correction pass (2026-06-05): 10 fresh native simulator captures validated as unique opaque RGB PNGs at the portal-requested 1242x2688; screenshots 1, 6, and 10 visually inspected |
| RunSmart Web | Medium | derived | Not parsed |
| ResumeBuilder AI (Web) | Medium | derived | Not parsed |
| Agentic OS | High | tasks/progress.md | 35 parser unit tests passed; ./agentic-os verify passed with JSON, fallback sync, confidence, links, and git diff checks on 2026-06-05 |

## Risk Board

- RunSmart iOS: Apple review outcome is external
- Resumely iOS: App Store Connect export stalls in `codesign` while using Apple Distribution private key `71915959D76E14CED4D4153118972F034D338A50` (local Keychain permission/unlock required)
- Resumely iOS: `/api/v1/resumes` still returns production Next.js 404 HTML, so Resume Library remains disabled
- RunSmart Web: Dirty local tree with many modified/untracked files, including duplicate ` 2` files.
- ResumeBuilder AI (Web): Dirty fix/pdf-parse-xref-error branch.
- ResumeBuilder AI (Web): docs/plan.rollout.md tasks are unchecked.
- Dirty local repo state: RunSmart iOS, Resumely iOS, RunSmart Web, ResumeBuilder AI (Web), Agentic OS.

## Next Recommended Actions

1. RunSmart iOS: After review approval — merge version-2 to main, update PROJECT-STATUS.md, publish launch post
1. Resumely iOS: Upload the screenshot folders in App Store Connect, then authorize the Apple Distribution key and upload the build
