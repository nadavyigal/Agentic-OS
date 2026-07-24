# Weekly Executive Summary - 2026-07-24

- Status: current, with explicit source and cohort caveats
- Reviewed: 2026-07-24
- Evidence refresh: `./agentic-os morning`, 2026-07-24 09:03 IDT
- Portfolio trust: `Refresh required`. Both apps are live, but the ground-truth guard misclassifies descriptive post-release phase text as pre-launch, product repos are dirty, and the Resumely parser selected an older side-branch progress file instead of newer `main`.
- Open executive decisions: 0 rows with Status `Open` in `executive-os/EXECUTIVE-DECISIONS.md`.
- New executive decisions logged: none. Current evidence supports carrying forward and clarifying existing decisions, not adding a new row.
- Sources: `dashboard/status.json`, `DASHBOARD.md`, `PROJECT-STATUS.md`, `dashboard/portfolio-hq-manual.json` (as of 2026-07-22), `distribution-os/weekly-growth-review.md`, `executive-os/EXECUTIVE-DASHBOARD.md`, `executive-os/EXECUTIVE-DECISIONS.md`, `executive-os/EXECUTIVE-METRICS.md`, `executive-os/reviews/2026-07-21-coo-operating-review.md`, and the current `main` task progress in both iOS repos.

## Operating Read

Both apps are live on the July 22 builds: RunSmart 1.1.2 (27) and Resumely 1.4.5 (15). The refreshed ground-truth layer saw 18 RunSmart and 94 Resumely live users over seven days. Those counts confirm live traffic, not activation. Source: `dashboard/status.json` `groundTruth`; `dashboard/portfolio-hq-manual.json` `activationHeadline`.

Resumely remains the primary product. Its current `main` is 1.4.6 (16), merged and release-validated, carrying WP-53 recovery protection plus the export-success review prompt. It has **not** been archived, uploaded, or submitted. The physical recovery/export smoke remains open. The live 1.4.5 build still exposes the recovery defect WP-53 fixes. Source: Resumely iOS `tasks/progress.md` on `main`; `PROJECT-STATUS.md`.

Resumely has no valid pre-1.4.5 activation baseline. `optimized_preview_rendered` was defective before 1.4.5, so the older 0%, 10%, and 12.5% figures are measurement artifacts, not low baselines. The working milestone remains `optimized_preview_rendered`; `export_success` is a downstream diagnostic. The first valid cohort began when 1.4.5 went live on 2026-07-22. The planned reads are a 2026-07-29 monotonicity check and a 2026-08-05 definitive count toward EXD-022. Source: `dashboard/portfolio-hq-manual.json` `activationHeadline` and `funnels`; EXD-022.

RunSmart's earlier "broken for everyone" sign-in conclusion was refuted by a genuine revoke-and-retry success. The remaining fact is narrower: code-1000 failures occurred on three real devices, with cause still unnamed. Live 1.1.2 carries `has_underlying_error`; one real failure decides whether the next action is a named precondition fix or the conditional fallback packet. RunSmart 1.1.3 (28), containing the repaired route feature, merged to `main` on 2026-07-24 and is ready for founder archive. Source: EXD-023; RunSmart iOS `tasks/progress.md` and `main` version metadata.

## Plan Progress

| Plan | Index status | Milestone progress | CEO recommendation |
|---|---|---|---|
| `executive-os/BUSINESS-GTM-PLAN-V0.md` | `needs_next_packet` | Both apps are live, but Resumely's first valid cohort is immature and RunSmart's sign-in cause is unnamed | COO drafts one post-read packet after the 2026-08-05 Resumely read and the first decisive RunSmart failure event; no monetization or volume GTM before evidence changes |
| RunSmart Hebrew-first distribution playbook | `needs_next_packet` | Preserved and parked by EXD-016 until 2026-08-01 | COO drafts a dated 2026-08-01 revisit packet; do not publish or activate the playbook now |
| RunSmart iOS GTM plan | `needs_next_packet` | Product is live, but sign-in reliability and activation remain unresolved | COO drafts a sign-in-and-cohort-gated packet after the diagnostic read; do not draft a volume-launch packet |
| Resumely 1.4.6 release | current execution lane outside `planExecution` | Merged and release-validated; physical smoke, archive, upload, and submission remain | Finish the founder release gate; do not start another Resumely feature lane first |
| Indexed research briefs | `research_only` | Inputs remain available | No execution assignment this week |

Source: `dashboard/status.json` `planExecution`; EXD-016; EXD-022; EXD-023; Resumely iOS `tasks/progress.md`.

## Top 3 Priorities

1. **Ship Resumely 1.4.6 safely.** Run the physical recovery/export smoke, then archive and upload the already-validated build. It carries the fix for the live 1.4.5 recovery defect.
2. **Take the first honest Resumely activation reads.** On July 29, confirm the funnel is monotonic. On August 5, count clean `optimized_preview_rendered` activations toward EXD-022's target of 20. Do not compare them with the invalid pre-1.4.5 figures.
3. **Finish RunSmart's bounded release and diagnosis.** Archive the already-merged 1.1.3 route repair, then use the first real 1.1.2 `sign_in_failed` event's `has_underlying_error` value to choose the next sign-in action. Do not guess from tiny rates.

## Key Decisions

There are no open rows in `EXECUTIVE-DECISIONS.md`, so no new executive decision is required this week.

| Standing decision | Recommendation this week |
|---|---|
| EXD-022 | Hold: the activation gate is at least 20 clean activations on a working milestone, with no calendar deadline. August 1 is a written checkpoint, not a verdict. |
| EXD-023 | Hold the conditional RunSmart fallback. The "broken for everyone" framing is refuted; wait for the first live `has_underlying_error` value. |
| EXD-015, as superseded by EXD-022 on target wording | Keep Resumely primary. The old 20%-by-August-1 target is no longer authoritative. |
| 2026-07-18 Adaptive Coach decision in `DECISIONS.md` | Preserve active investment in the approved Phase 1 plan, but do not expand it this week while the two release/measurement gates above are open. Garmin remains paused. |
| EXD-009 / Gate A | Keep monetization and Premium CTAs closed until valid activation evidence supports reopening. |
| EXD-016 | Keep RunSmart Hebrew-first distribution parked until the August 1 revisit. |

## Contradictions And Resolution

1. `dashboard/status.json`, `DASHBOARD.md`, and `PROJECT-STATUS.md` label both apps as contradicting their live state even though their phase text explicitly says post-release work. The guard is treating any phase that does not contain a canonical `LIVE` token as pre-launch. Both apps are live; the trust warning is a source-shape defect, not evidence they are pre-launch.
2. The refreshed parser selected Resumely's older `codex/wp-53-optimization-id-preservation` progress file, while Resumely `main` already contains merged PRs #120-#122 and 1.4.6 release readiness. Use `main` for release state and preserve the branch-selection conflict until the product checkout is reconciled.
3. The stranded draft of this review said Resumely 1.4.6 was in App Store review. Resumely `main` says the opposite: nothing has been archived, uploaded, or submitted. This review corrects the current artifact and keeps the false claim named here.
4. `executive-os/CEO-OS.md` still names RunSmart as primary and describes pre-release stages. EXD-015 makes Resumely primary, while the 2026-07-18 decision permits bounded Adaptive Coach investment. The later durable decisions control; the older strategy text remains preserved.
5. `executive-os/EXECUTIVE-METRICS.md` still reports Resumely 0/73 against a 20%-by-August-1 target. EXD-022 supersedes the target, and WP-51 proves the old milestone never fired reliably. Do not cite that row as a current baseline.
6. The stranded draft proposed a new "no RunSmart feature expansion" decision. That would conflict with the 2026-07-18 Adaptive Coach decision, so it was not logged or carried forward.
7. The generated `decisionBoard` still contains build-8 rejection, voice-coach, Resumely upload-path, and old web-rollout questions. The durable executive log has zero open decisions; these generated rows are stale historical prompts, not CEO decisions.

## Stop-Doing List

- Do not call old Resumely activation figures low; they are invalid.
- Do not open RunSmart's fallback packet or change sign-in architecture before the decisive diagnostic property arrives.
- Do not start another Resumely feature lane before 1.4.6 completes its founder release gate.
- Do not turn seven-day live-user counts into activation rates.
- Keep Gate A, paid acquisition, Garmin relaunch engineering, and RunSmart Hebrew publishing closed or parked.
- Do not deploy, publish, migrate, or change production systems from this review.

## Delegation List

| Priority | Owner / workflow | Assignment |
|---|---|---|
| Resumely 1.4.6 | Founder release session | Run physical recovery/export smoke, then archive, validate, upload, and submit |
| Resumely measurement | Analytics / CEO OS | Run the July 29 monotonicity check and August 5 clean activation count |
| RunSmart 1.1.3 | Founder release session | Archive and upload the already-merged route repair |
| RunSmart sign-in | Analytics / CEO OS | Read `has_underlying_error` on the first real 1.1.2 failure and route the next action from the value |
| Three `needs_next_packet` plans | COO OS | Draft the gated packets described in Plan Progress at their evidence checkpoints |
| Source reconciliation | Maintainer workflow | Reconcile product checkouts/progress sources and make live phase labels explicit without changing product behavior |
| Finance visibility | Founder | Build the one-time recurring-cost list before the next CFO review |

## Top Risks

1. **Resumely's recovery defect is live until 1.4.6 ships.** The fix is merged but still behind the founder release gate.
2. **The first valid Resumely cohort is immature.** Any verdict before the July 29/August 5 reads would recreate the measurement mistakes EXD-022 corrected.
3. **RunSmart sign-in fails for an unknown subset.** The all-users outage claim is false, but the surviving device failures still block a clean activation read.
4. **Portfolio trust is degraded by source selection and dirty repos.** The dashboard selected stale branch progress for Resumely and misclassified live phase text.
5. **Financial visibility remains absent.** Revenue, costs, burn, and runway are `unknown - need: App Store Connect/RevenueCat, provider billing, cash on hand, and a manual cost list`.

## Recommended Next Actions

1. Founder: complete the Resumely 1.4.6 physical smoke and release gate.
2. Founder: archive and upload RunSmart 1.1.3; do not add scope.
3. Analytics: run Resumely's July 29 and August 5 reads with founder/QA/bot exclusions.
4. Analytics: read RunSmart's first real `has_underlying_error` value and route the next action from it.
5. COO: prepare the three gated next packets only at their named evidence checkpoints.
6. Maintainer: reconcile the product progress sources and stale generated decision board.
7. Founder: create the recurring-cost list before the next monthly finance review.

## Dashboard Updates Applied

- Replaced the stale July 17 release and sign-in framing with the July 24 release-ready state.
- Corrected the false claim that Resumely 1.4.6 was already in App Store review.
- Restored `optimized_preview_rendered` as the working activation milestone and marked all pre-1.4.5 Resumely baselines invalid.
- Carried EXD-022 and EXD-023 forward without creating a conflicting new decision.
- Preserved the 2026-07-17 review as history.
