# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-07-17 IDT

## Executive Summary

Resumely is primary through the 2026-08-01 activation window. Release A 1.4.2 (12) is live, Story 8 is the active FTUX lane, and WP-46 queues Stories 9-13 toward one 1.5.0 readiness handoff. RunSmart 1.0.9 (23) is live, but its n=2 public sign-in failure signal needs one founder-device reproduction before any code or configuration change. Mature activation remains Resumely 0/73 and RunSmart 0/13 from the 2026-07-12 read; newer exact-version cohorts are immature. Sources: `dashboard/portfolio-hq-manual.json`, `EXECUTIVE-METRICS.md`, and `DECISIONS.md`.

## Top 3 Priorities

1. Verify RunSmart public-build Sign in with Apple once on the founder device; reproduce before changing code or production configuration.
2. Finish the existing Resumely Story 8 lane, then execute WP-46 Stories 9-13 sequentially toward a 1.5.0 readiness handoff; no App Store action.
3. Protect measurement: land current evidence after review, record WP-31 publish/baseline data, and run the July 22/25 cohort checks without turning 0/0 into 0%.

Source: `executive-os/reviews/2026-07-17-weekly-ceo-review.md`.

## Financial Snapshot

Revenue, costs, margin, burn, and runway are `unknown - need: App Store Connect/RevenueCat, provider billing, cash on hand, and a manual cost list`. Marketing spend is the only known figure at `$0`. Source: `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Decision Board

- Open executive decisions: 0.
- Keep Resumely primary through 2026-08-01 (EXD-015).
- Defer RunSmart E1 until sign-in works and at least 10 clean mature-D7 entrants exist (`DECISIONS.md`, 2026-07-16).
- Keep Resumely Release B+C as one sequential 1.5.0 target; no archive, TestFlight, or App Store action is authorized (`DECISIONS.md`, 2026-07-16).
- Keep Gate A, paid acquisition, RunSmart Hebrew distribution, and Garmin relaunch engineering closed or parked under their existing decisions.
- New durable decision this review: none.

## Plan Board

- `BUSINESS-GTM-PLAN-V0.md`: COO drafts a post-cohort decision packet after the July 22/25 reads.
- RunSmart Hebrew-first playbook: COO drafts a 2026-08-01 revisit packet; execution remains parked under EXD-016.
- RunSmart iOS GTM plan: COO drafts a sign-in and cohort-gated packet, not a volume-launch packet.
- Seven research briefs remain `research_only`; no execution assignment this week.

Source: `dashboard/status.json` `planExecution`.

## Contradictions

- Parsed status still says Resumely 1.4.1 with no active story; the dated founder-confirmed layer says 1.4.2 live, Story 7 complete, Story 8 active, and WP-46 queued.
- `CEO-OS.md` still names RunSmart as primary and describes pre-release stages; EXD-015 makes Resumely primary through 2026-08-01.
- `EXECUTIVE-METRICS.md` uses the correct mature activation baseline but names prior live versions in its blocked-app row.
- Portfolio evidence refreshed today, but trust is still `Refresh required` because one unrelated dirty worktree remains and the snapshot began with local commits ahead of origin.

Resolution: use the dated manual evidence for current release sequencing, preserve the mature cohort contract for decisions, and keep the parser lag visible until its source is reconciled.

## Risk Board

- RunSmart sign-in: possible public P0, but n=2 is not enough to declare an outage.
- Resumely measurement: Release A has 0 clean post-release entrants, so no exact-version activation claim is valid yet.
- Evidence durability: several current audit and measurement artifacts remain branch-only.
- Portfolio trust: one unrelated dirty worktree remains open; do not treat generated readiness claims as automatically authoritative.
- Distribution: WP-31 publish time and Israeli storefront baseline are still missing; WP-32 closed inconclusive because attribution was absent.
- Finance: revenue, costs, burn, and runway remain unknown.

## Weekly Review

- Current review: `executive-os/reviews/2026-07-17-weekly-ceo-review.md`.
- Prior review preserved: `executive-os/reviews/2026-07-09-weekly-ceo-review.md`.
- No new row added to `EXECUTIVE-DECISIONS.md`; evidence supports carrying forward existing decisions, not creating a new one.

## Next Actions

1. Founder runs one RunSmart public sign-in attempt and records UTC plus exact result.
2. Existing Resumely session finishes and integrates Story 8.
3. WP-46 continues Stories 9-13 only after the active work integrates.
4. Review and merge the current evidence branches, then reconcile the stale Resumely progress source.
5. Record WP-31 publish timestamp and App Store Connect Israeli storefront baseline.
6. Run July 22 directional checks and the preferred July 25 Resumely cohort read.
7. Build the one-time manual recurring-cost list before the next CFO review.
