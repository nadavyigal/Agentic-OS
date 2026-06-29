# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-06-29 IDT

## Executive Summary

RunSmart iOS is live as marketing version `1.0.4`, but build 18 upload/submission/live confirmation remains founder-only and gates the Garmin reply. Resumely iOS is post-launch on v1.2 (7), with production funnel/event verification now the next evidence task. ResumeBuilder AI (Web) PR #97 is merged into `main`; do not keep treating it as active work. Portfolio trust is `Use caution`, not because of a hard contradiction, but because product-repo hygiene and evidence gaps remain.

Sources: `DASHBOARD.md`, `PROJECT-STATUS.md`, `dashboard/status.json`, GitHub PR #97.

## CEO Focus

1. RunSmart: confirm build 18 live state, recapture Gate-4 screenshots, and send Garmin reply only after live-build evidence matches.
2. Resumely: verify production PostHog project 270848 upload-funnel and `fit_check_*` events for v1.2 (7), then read zero-budget outreach results.
3. Hygiene: reduce product-repo drift before trusting the dashboard for release, billing, App Store, or production decisions.

## Financial Snapshot

Needs Data - no revenue/cost source is wired.

- Revenue by product: unknown - need App Store Connect / RevenueCat.
- Subscription revenue: unknown - need RevenueCat / Stripe.
- AI/API cost: unknown - need provider billing.
- Marketing spend: `$0`, tracked manually (`EXECUTIVE-METRICS.md`).

## Open Decisions

No open executive decisions in `EXECUTIVE-DECISIONS.md`.

Standing recommendations:

- Keep freemium model shape, set price only after first-cohort activation data (EXD-005).
- Monetize after activation evidence, not before (EXD-009).
- Keep Fit/Match/self-defined score positioning discipline (EXD-012).
- Investigate activation before monetization or GTM volume (EXD-013).
- Do not send Garmin evidence until RunSmart live build and evidence package agree (EXD-014).

## Status Confidence

How much each project's state is backed by parsed local task files versus narrative only.

| Project | Confidence | Source | Current caveat |
|---|---|---|---|
| RunSmart iOS | High | `tasks/progress.md` | Dirty working tree; build 18 live confirmation is founder-only. |
| Resumely iOS | High | `tasks/progress.md` | Evidence gap after latest commit; one extra worktree retained. |
| RunSmart Web | High | `tasks/progress.md` | Build 18 live state not confirmed; Garmin reply remains blocked. |
| ResumeBuilder AI (Web) | High | `tasks/progress.md` | PR #97 merged on GitHub, local checkout still needs sync before more web work. |
| Agentic OS | High | `tasks/progress.md` | Main is ahead of origin until pushed. |

## Risk Board

- RunSmart: do not recapture/send Garmin evidence until build 18 is confirmed live.
- Resumely: production funnel and `fit_check_*` events need verification before growth or monetization decisions.
- ResumeBuilder AI (Web): PR #97 is merged, but local repo state must be synced before more work.
- Portfolio: product-repo hygiene remains a trust risk; do not treat dashboard state as sufficient for release/billing/App Store actions without source validation.
- Finance: revenue, subscription, cost, and runway remain unknown until real sources are reviewed.

## Weekly Review

Latest review: `WEEKLY-CEO-LATEST.md` (2026-06-29).

Decision of the week: do not replace completed PR work with a new feature sprint. The next portfolio move is evidence discipline: RunSmart live-build/Garmin proof and Resumely production funnel verification.

## Next Recommended Actions

1. RunSmart: founder confirms build 18 live state and gates Garmin evidence.
2. Resumely: verify production event flow and outreach results.
3. Agentic OS: keep PR #97/WP-19 closed, refresh dashboard after local product repos are synced.
4. COO: once evidence gates are clean, draft exactly one next packet from plans marked `needs_next_packet`.
5. CFO/monetization: no action until activation evidence is readable.
