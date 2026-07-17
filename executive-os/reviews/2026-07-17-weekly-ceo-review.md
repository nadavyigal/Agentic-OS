# Weekly Executive Summary - 2026-07-17

- Status: current with explicit trust caveats
- Reviewed: 2026-07-17
- Portfolio trust: `Refresh required`. Evidence refreshed 2026-07-17 09:15 IDT, but one unrelated dirty Agentic OS worktree remains open and the consolidated `main` commits were not yet pushed when the review snapshot was taken. Source: `dashboard/status.json` `portfolioTrust` and `repoIntegrity`.
- Open executive decisions: 0 rows with Status `Open` in `executive-os/EXECUTIVE-DECISIONS.md`.
- New executive decisions logged: none. The relevant 2026-07-16 calls already exist in `DECISIONS.md`; this review carries them forward without duplicating them.
- Sources: `dashboard/status.json`, `DASHBOARD.md`, `PROJECT-STATUS.md`, `dashboard/portfolio-hq-manual.json`, `distribution-os/weekly-growth-review.md`, `executive-os/EXECUTIVE-DASHBOARD.md`, `executive-os/EXECUTIVE-DECISIONS.md`, `executive-os/EXECUTIVE-METRICS.md`, and `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Operating Read

Resumely remains the primary product through the 2026-08-01 activation window. Release A 1.4.2 (12) is live, Story 7 is complete, Story 8 is the active lane, and WP-46 continues Stories 9-13 toward one 1.5.0 readiness handoff after the current work integrates. RunSmart 1.0.9 (23) is live, but two clean public entrants both produced non-cancel sign-in failures and no completion. That is a P0 signal to reproduce on the founder device, not proof of an outage at n=2. Source: `dashboard/portfolio-hq-manual.json` as of 2026-07-16 and `DECISIONS.md` entries dated 2026-07-15 and 2026-07-16.

The 2026-07-12 mature read remains the decision baseline: Resumely 0/73 real D7 activation and RunSmart 0/13. The newer exact-version release cohorts are immature, including Resumely 1.4.2 at 0/0 clean entrants. No monetization, paid acquisition, GTM-volume expansion, or product-lift claim is unlocked. Source: `executive-os/EXECUTIVE-METRICS.md` and `dashboard/portfolio-hq-manual.json` `activationHeadline`.

## Plan Progress

| Plan | Index status | Milestone progress | CEO recommendation |
|---|---|---|---|
| `executive-os/BUSINESS-GTM-PLAN-V0.md` | needs_next_packet | Activation and release facts have moved far beyond the original pre-launch framing | COO drafts one post-cohort decision packet after the July 22/25 reads; no monetization or GTM-volume execution before evidence changes |
| `docs/superpowers/plans/2026-06-22-runsmart-hebrew-first-distribution-playbook.md` | needs_next_packet | Useful plan, but EXD-016 parks execution until 2026-08-01 | COO drafts a dated 2026-08-01 revisit packet; no publishing or campaign execution now |
| RunSmart iOS `.agent-os/distribution/gtm-plan.md` | needs_next_packet | Product is live, but sign-in and activation evidence do not support volume | COO drafts a gated next packet tied to successful sign-in verification and a valid cohort, not a launch-volume packet |
| Resumely FTUX WP-46 | current execution track outside `planExecution` | Release A live; Story 7 complete; Story 8 active; Stories 9-13 queued sequentially | Preserve the existing Story 7-8 owner, then execute WP-46 without parallel duplication or App Store action |
| Seven indexed research briefs | research_only | Inputs remain available | No execution assignment this week |

Source: `dashboard/status.json` `planExecution`, `dashboard/portfolio-hq-manual.json`, EXD-016, and `executive-os/work-packets/WP-46-resumely-ftux-release-b-c-continuation.md`.

## Top 3 Priorities

1. **Verify RunSmart sign-in on the public build now.** Make one founder-device Sign in with Apple attempt and record the exact result. If it fails, inspect shipped provisioning, the App Store capability, and Supabase Apple provider configuration before changing app code. Source: `dashboard/portfolio-hq-manual.json` founder command and RunSmart track.
2. **Finish the active Resumely lane, then continue the approved 1.5.0 sequence.** Do not duplicate Stories 7-8. After Story 8 integrates, verify the Story 9 evidence contract and deliver Stories 9-13 one at a time through WP-46. Stop before archive, TestFlight, or App Store actions. Source: `dashboard/portfolio-hq-manual.json`, `DECISIONS.md` 2026-07-15/16, and WP-46.
3. **Protect the measurement contract while cohorts mature.** Merge the current evidence branches after review, record WP-31's actual publish timestamp and Israeli storefront baseline, and run the July 22/25 checkpoints without converting immature 0/0 cohorts into activation rates. Source: `dashboard/portfolio-hq-manual.json`, `distribution-os/weekly-growth-review.md` week of 2026-07-14, and `EXECUTIVE-METRICS.md`.

## Key Decisions

There are no open rows in `EXECUTIVE-DECISIONS.md`, so no new executive decision is required this week.

| Standing decision | Recommendation this week |
|---|---|
| EXD-015 | Keep Resumely primary through the 2026-08-01 read; RunSmart Garmin remains maintenance/background work |
| 2026-07-16 RunSmart evidence decision in `DECISIONS.md` | Defer E1 until sign-in works and at least 10 clean mature-D7 entrants exist |
| 2026-07-16 Resumely release decision in `DECISIONS.md` | Keep one 1.5.0 Release B+C target, sequentially, with no App Store action authorized |
| EXD-009 / Gate A | Keep monetization and Premium CTAs closed until activation evidence supports reopening |
| EXD-016 | Keep RunSmart Hebrew-first distribution parked until 2026-08-01 |

## Contradictions And Resolution

1. `dashboard/status.json`, `DASHBOARD.md`, and `PROJECT-STATUS.md` still describe Resumely 1.4.1 (11) with no active story, while the founder-confirmed manual layer records 1.4.2 (12) live, Story 7 complete, Story 8 active, and WP-46 queued. Use the dated manual layer for this week's sequencing and keep the parser lag visible until the product progress source is reconciled.
2. `executive-os/CEO-OS.md` still says RunSmart is primary and describes both products as pre-release. EXD-015 and the 2026-07-02 durable decision make Resumely primary through 2026-08-01. The durable decision controls; the strategy document is stale and is not silently rewritten in this review.
3. The pre-review `EXECUTIVE-DASHBOARD.md` still listed build 8 review, Resumely device smoke, and the voice-coach flag as current. Both apps are now live on newer versions and the voice-coach decision is closed. This review replaces the current dashboard view while the 2026-07-09 review remains preserved as history.
4. `EXECUTIVE-METRICS.md` correctly carries the mature 2026-07-12 activation baseline, but its Apps Blocked row names RunSmart 1.0.8 and Resumely 1.4.1. The correct current release layer is 1.0.9 and 1.4.2; do not reinterpret the older cohort as exact-version evidence.
5. Agentic OS evidence is refreshed today, but `portfolioTrust` remains `Refresh required` because of one retained dirty worktree and unpushed local commits at snapshot time. Release/readiness claims therefore cite the founder-confirmed manual evidence explicitly instead of inheriting an actionable trust label.

## Stop-Doing List

- Do not change RunSmart code or production configuration until the sign-in signal is reproduced.
- Do not build E1 assignment instrumentation until sign-in works and the clean mature-D7 denominator reaches 10.
- Do not start another Resumely Story 7-8 session, alter the live 1.4.2 app, or perform archive/TestFlight/App Store actions.
- Do not resume Garmin relaunch engineering, WP-34, RunSmart Hebrew distribution, paid acquisition, or monetization this week.
- Do not report 0/0 as 0%, or cite the disputed Resumely cumulative export count as confirmed.
- Do not publish another community experiment without unique campaign links and verified analytics access.

## Delegation List

| Priority | Owner/workflow | Assignment |
|---|---|---|
| RunSmart public sign-in | Founder device session | Reproduce or disprove once; capture UTC and exact visible result |
| Resumely Story 8 | Existing Claude Code session | Finish and integrate without parallel duplication |
| Resumely Stories 9-13 | WP-46 after Story 8 | Execute sequentially; stop at release-readiness handoff |
| Three `needs_next_packet` plans | COO OS | Draft the gated packets described in Plan Progress; do not activate parked work |
| Evidence branches and parser lag | Maintainer / review workflow | Review and merge evidence, then reconcile product progress sources |
| WP-31 measurement | Distribution workflow plus founder ASC access | Record publish timestamp, baseline, and 21-day read date |
| July 22/25 cohort reads | Analytics / CEO OS | Run the frozen, founder-excluded queries and preserve denominator rules |

## Top Risks

1. **RunSmart sign-in may be a public P0.** The signal spans both clean entrants, but n=2 is too small to call an outage. Delay has high cost because no downstream activation can occur without sign-in. Source: `dashboard/portfolio-hq-manual.json`.
2. **Resumely may ship more FTUX work before it has a clean release cohort.** Release A has 0 clean post-release entrants, so Story 9 credibility and Story 10 event integrity must stay gated and testable. Source: `dashboard/portfolio-hq-manual.json` Resumely track.
3. **Evidence can disappear on branches or drift between manual and parsed layers.** Current audit/report artifacts remain branch-only, and the parser still reports Resumely 1.4.1. Source: `dashboard/portfolio-hq-manual.json` Artifacts and `dashboard/status.json`.
4. **Portfolio trust is not actionable yet.** One dirty worktree remains and this review began with local commits ahead of origin. Source: `dashboard/status.json` `portfolioTrust`.
5. **Financial visibility remains absent.** Revenue, costs, burn, and runway are unknown; only marketing spend at `$0` is tracked. Need: App Store Connect/RevenueCat, provider billing, cash on hand, and a manual cost list. Source: `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Recommended Next Actions

1. Founder: run one RunSmart public sign-in attempt and record the result.
2. Existing Resumely session: finish Story 8 and integrate it.
3. WP-46 owner: after integration, verify Story 9's contract and execute Stories 9-13 sequentially.
4. Maintainer: merge current evidence after review and reconcile the stale Resumely progress source.
5. Distribution: capture WP-31 publish time and Israeli storefront baseline before the measurement window ages further.
6. Analytics: run the July 22 directional checks and the preferred July 25 Resumely read without forcing a verdict below the cohort minimum.
7. Finance: create the one-time manual recurring-cost list before the next monthly review.

## Dashboard Updates Applied

- Replaced stale build-8/device-smoke focus with the current sign-in, Resumely FTUX, and measurement priorities.
- Replaced stale open questions with a zero-open-decision board plus standing recommendations.
- Added the source contradictions, current risks, plan routing, and dated next actions.
- Preserved the full 2026-07-09 weekly review at `executive-os/reviews/2026-07-09-weekly-ceo-review.md`.
