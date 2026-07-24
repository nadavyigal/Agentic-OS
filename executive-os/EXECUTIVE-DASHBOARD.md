# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-07-24 IDT

## Executive Summary

Resumely remains primary. Both apps are live on the July 22 builds: RunSmart 1.1.2 (27) and Resumely 1.4.5 (15). Resumely 1.4.6 (16) is merged and release-validated but has not been archived, uploaded, or submitted; it carries WP-53 recovery protection for a defect still affecting live 1.4.5 users. RunSmart 1.1.3 (28) is merged and ready for founder archive. Resumely's first valid activation cohort starts with 1.4.5 because the prior milestone was defective; RunSmart sign-in fails for some users, not all, and the next action depends on one diagnostic property. Sources: `dashboard/status.json`, `dashboard/portfolio-hq-manual.json`, both iOS repos' `main` task progress, EXD-022, and EXD-023.

## Top 3 Priorities

1. Ship Resumely 1.4.6 safely: physical recovery/export smoke, then founder archive and upload.
2. Run the first valid Resumely reads: July 29 for funnel monotonicity and August 5 for the clean activation count toward EXD-022.
3. Archive RunSmart 1.1.3, then use the first real 1.1.2 `has_underlying_error` value to choose the sign-in response.

Source: `executive-os/reviews/2026-07-24-weekly-ceo-review.md`.

## Financial Snapshot

Revenue, costs, margin, burn, and runway are `unknown - need: App Store Connect/RevenueCat, provider billing, cash on hand, and a manual cost list`. Marketing spend is the only known figure at `$0`. Source: `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Decision Board

- Open executive decisions: 0.
- EXD-022: activation gate is at least 20 clean activations on a working milestone, with no calendar deadline. August 1 is a written checkpoint, not a verdict.
- EXD-023: the "sign-in broken for everyone" framing is refuted. Keep the fallback conditional on the first live `has_underlying_error` value.
- EXD-015: Resumely remains primary; its old target wording is superseded by EXD-022.
- 2026-07-18 Adaptive Coach decision: approved Phase 1 investment remains valid, but there is no reason to expand it this week. Garmin remains paused.
- EXD-009 / Gate A and EXD-016 remain closed or parked.
- New durable decision this review: none.

## Plan Board

- `BUSINESS-GTM-PLAN-V0.md`: COO drafts a post-read packet after the August 5 Resumely read and the first decisive RunSmart failure event.
- RunSmart Hebrew-first playbook: COO drafts a dated August 1 revisit packet; execution remains parked.
- RunSmart iOS GTM plan: COO drafts a sign-in-and-cohort-gated packet, not a volume-launch packet.
- Indexed research briefs remain `research_only`; no execution assignment this week.

Source: `dashboard/status.json` `planExecution`.

## Contradictions

- The ground-truth guard misclassifies descriptive post-release phase text as pre-launch even though both apps are live.
- The parser selected older Resumely side-branch progress; `main` has 1.4.6 merged and ready for founder archive.
- A stranded draft said Resumely 1.4.6 was in App Store review; `main` explicitly says nothing was archived, uploaded, or submitted.
- `CEO-OS.md` still names RunSmart as primary; later durable decisions make Resumely primary while allowing bounded Adaptive Coach work.
- `EXECUTIVE-METRICS.md` still carries an invalid Resumely pre-1.4.5 baseline and the superseded 20%-by-August-1 target.
- The generated decision board still contains old build-8, voice-coach, upload-path, and rollout prompts despite zero open durable decisions.

Resolution: use current `main` product progress for release state, EXD-022/023 for decisions, and the July 22 manual evidence layer for cohort rules. Preserve the older files as historical evidence until their owners reconcile them.

## Risk Board

- Resumely's recovery defect remains live until 1.4.6 ships.
- Resumely's first valid cohort is immature; early rates would be misleading.
- RunSmart sign-in still fails on an unknown subset of devices/accounts.
- Portfolio trust is degraded by dirty repos, stale branch selection, and live-phase parser false positives.
- Revenue, costs, burn, and runway remain unknown.

## Weekly Review

- Current review: `executive-os/reviews/2026-07-24-weekly-ceo-review.md`.
- Prior review preserved: `executive-os/reviews/2026-07-17-weekly-ceo-review.md`.
- No new row added to `EXECUTIVE-DECISIONS.md`; evidence supports clarification, not a new durable decision.

## Next Actions

1. Founder completes Resumely 1.4.6 physical smoke, archive, validation, upload, and submission.
2. Founder archives and uploads RunSmart 1.1.3 without adding scope.
3. Analytics runs Resumely's July 29 monotonicity check and August 5 clean activation count.
4. Analytics reads RunSmart's first real `has_underlying_error` value and routes the next action.
5. COO drafts the three gated next packets only at their named checkpoints.
6. Maintainer reconciles product progress sources and stale generated decision prompts.
7. Founder creates the recurring-cost list before the next CFO review.
