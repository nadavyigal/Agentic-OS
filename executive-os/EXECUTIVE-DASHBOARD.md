# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-06-05 IDT

## Executive Summary

RunSmart iOS — App Store Review: Monitor App Store Connect; if Apple responds, handle only the review outcome before starting new release scope · Resumely iOS — App Store Review: Monitor App Store Connect; if Apple responds, handle only the review outcome before starting post-launch scope · RunSmart Web — Sprint 11 backend support / reference · ResumeBuilder AI (Web) — PDF parse/render-preview rollout

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
| RunSmart iOS | High | tasks/progress.md | Founder confirmed App Store Connect submission of RunSmart 1.0.1 build 9 on 2026-06-05. Local release archive validation and git diff checks passed before the founder-controlled upload; Apple review result is pending |
| Resumely iOS | High | tasks/progress.md | Founder confirmed App Store Connect submission of Resumely 1.0 build 1 on 2026-06-05. The submitted screenshot set had already passed count, dimension, uniqueness, opacity, and targeted visual checks; Apple review result is pending |
| RunSmart Web | Medium | derived | Not parsed |
| ResumeBuilder AI (Web) | Medium | derived | Not parsed |
| Agentic OS | High | tasks/progress.md | 35 parser unit tests passed; ./agentic-os verify passed with JSON, fallback sync, confidence, links, and git diff checks on 2026-06-05 |

## Risk Board

- RunSmart iOS: Apple review outcome is external
- Resumely iOS: Apple review outcome is external
- Resumely iOS: `/api/v1/resumes` still returns production Next.js 404 HTML, so Resume Library remains disabled
- RunSmart Web: Dirty local tree with many modified/untracked files, including duplicate ` 2` files.
- ResumeBuilder AI (Web): Dirty fix/pdf-parse-xref-error branch.
- ResumeBuilder AI (Web): docs/plan.rollout.md tasks are unchecked.

## Next Recommended Actions

1. RunSmart iOS: Monitor App Store Connect; if Apple responds, handle only the review outcome before starting new release scope
1. Resumely iOS: Monitor App Store Connect; if Apple responds, handle only the review outcome before starting post-launch scope
