# Work Packet WP-38 - RunSmart Record-Run UX Follow-ups

- Status: **COMPLETE** (2026-07-09) — S9-S11 merged PR #81 (`e5001bd`), S12 merged PR #82 (`cb5d76c`), S14a-d merged PR #83 (`f9d7c89`, CodeRabbit feedback addressed in `7d47cc9`). S13 stays gated (HealthKit accuracy precondition unmet) — does not block packet completion per its own gate.
- Created: 2026-07-09
- Source: WP-37's "Explicitly deferred (with reason)" list, promoted to stories after WP-37 closeout verification (all 8 WP-37 stories confirmed merged to `main` at `4476a7d`, PR #53 closed as fully superseded, local worktree cleaned and rebuilt clean on 2026-07-09)
- Mode: Builder (this packet)
- Workflow pattern: one story at a time, smallest shippable diff, device QA per story
- Outcome loop: RunSmart plan→run activation — same loop as WP-37; these are the items WP-37 explicitly scoped out rather than items found new
- Related: WP-37 (parent packet, closed), `docs/qa/reports/2026-07-08-run-recording-ux-audit.md` (original audit, now committed to RunSmart iOS repo)
- Success signal: same as WP-37 — none of these block "trust on a daily jog" on their own; this packet is about closing the gap to feature-parity/polish once trust is established

## Project

RunSmart iOS: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

Key files: `IOS RunSmart app/Features/Run/RunTabView.swift`, `LiveRunView.swift`, `PostRunSummaryView.swift`, `IOS RunSmart app/Services/Production/RunSmartProductionServices.swift` (`RunRecorder`).

Build note: local worktree's stray Finder `* 2.*` duplicate files were removed 2026-07-09; if Finder/iCloud resync recreates them, `diff` each against its non-` 2.` counterpart before deleting (do not blind-delete) and re-run a clean Debug build before starting any story here.

## Stories

| Story | Source (WP-37 deferred reason) | Proposed change (smallest diff) | Acceptance (device QA) | Model route |
|---|---|---|---|---|
| **S9 — Rename "Time" to "Moving time"** (post-run + live HUD label, P3) | WP-37 noted this was "acceptable at v1; rename opportunistically inside S3's diff if trivial" — S3 shipped without it. | Find every user-facing `"Time"` label tied to the moving-time stat (live HUD, post-run summary, report/history) and relabel to `"Moving time"`. Copy-only change; no new elapsed-time tracking. | Record a run with at least one pause: live HUD, finish summary, and report history all read "Moving time", value unchanged (still excludes paused duration). | Sonnet |
| **S10 — Fix `timeLabel` formatting for runs over 1 hour** | WP-37 noted `timeLabel` renders "90:00" instead of "1:30:00" for runs >1h; bundled as "if free" but never landed. | Locate the shared `timeLabel`/duration-formatting helper used by live HUD, post-run summary, and history rows; branch to `H:MM:SS` once elapsed seconds >= 3600, keep existing `MM:SS` under an hour. Single shared helper — fix once, all call sites inherit it. | Simulate/force a run duration >60 min (accelerate `simctl location` playback or seed test data): live HUD, post-run summary, and report history all show `H:MM:SS`; a 45-min run still shows `MM:SS` unchanged. Add a unit test for the boundary at exactly 60:00. | Sonnet |
| **S11 — Delete-dialog Garmin copy cleanup** | WP-37 found stale Garmin-specific copy in the run-delete confirmation dialog; bundled as "if free" but never landed. | In `RunTabView` (or wherever the delete `confirmationDialog`/`.alert` lives): remove/replace the Garmin-specific wording with source-neutral copy ("Delete this run?" / applies to any source, not just Garmin-synced runs). No logic change — copy only. | Delete a manually-recorded run and a Garmin-synced run (or mock both paths): dialog copy is identical and generic for both, no Garmin-specific language leaks into the non-Garmin path. | Sonnet |
| **S12 — Live per-km splits during recording** (Strava 2025 parity, P2 feature work) | WP-37: "real feature work, not polish; depends on S5's real-split computation landing first." S5 (real GPS-crossing splits) merged as part of WP-37 — this is now unblocked. | Surface `RunRecorder.kilometerSplits(from:)` (already shipped in S5) live during recording: as each km boundary crosses, append a completed-split row to a lightweight live-splits list in `LiveRunView`'s HUD (collapsed/expandable, does not compete with primary time/distance/pace for space). Reuse the S5 split-computation function; no new pace math. | Start a >2km simulated run: after each full km, a new split row appears live in the HUD in real time with the correct per-km pace; splits match the post-run summary's S5 splits exactly once the run ends. | Sonnet |
| **S13 — Live calories/steps** (explicitly low priority, revisit-gated) | WP-37: "benchmark says not table stakes... low-trust filler... contradicts calm-coach taste profile. Revisit only with HealthKit/pedometer integration and a real accuracy story." | **Do not implement without a HealthKit/pedometer accuracy story first.** This story is a placeholder to track the gate condition, not a green light. If picked up: scope must start with confirming HealthKit `HKQuantityTypeIdentifier.activeEnergyBurned`/step-count live-query accuracy on-device before any UI work, and must not fall back to a phone-GPS-only calorie estimate. | N/A until the accuracy gate is cleared — acceptance criteria to be defined at that time. | Sonnet (research phase only) |
| **S14 — Screen-awake, lock-screen/Live Activity controls, haptics, accessibility audit** (stretch bundle, P3) | WP-37: "stretch items from the audit's optional list; none block trust." Bundled together in the original audit as non-blocking nice-to-haves. | Four independent sub-items, land separately, smallest diff each: (a) keep screen awake during an active recording (`UIApplication.shared.isIdleTimerDisabled`), (b) add a Live Activity / lock-screen control surface for pause/finish during a run, (c) haptic feedback pass on start/pause/resume/finish/discard actions, (d) Dynamic Type + VoiceOver audit of `LiveRunView`/`PostRunSummaryView`/`PreRunView`. Split into 4 sub-stories (S14a-S14d) if picked up — do not land as one large diff. | Per sub-item: (a) screen doesn't sleep mid-run, resumes normal timeout after finish/discard; (b) lock screen shows pause/finish controls during a run; (c) haptic fires on each listed action, no double-fire; (d) VoiceOver reads all interactive elements with accurate labels, text scales without clipping at largest Dynamic Type setting. | Sonnet |

### Explicitly deferred (carried forward, unchanged from WP-37)

- **S13's HealthKit accuracy gate** is a hard precondition, not a scheduling note — do not start S13's UI work until that research spike is done and reviewed.

## Constraints

- Smallest shippable diffs; no Garmin (parked, EXD-015), no social, no AI-coach rewrite, no backend changes, no App Store submit from this packet.
- Run-tab scope only; do not touch onboarding/plan generation.
- Physical-device findings trump simulator, same as WP-37.
- Priority order if resourcing is constrained: S9/S10/S11 (cheap copy/formatting fixes) before S12 (real feature work) before S14 (stretch bundle) before S13 (gated, do not start without the accuracy spike).

## Validation

- Unit test for S10's hour-boundary formatting.
- Device smoke per story acceptance column; screenshots into `docs/qa/reports/`.
- `git status --short --branch` + push + PR per session-end rule.

## Completion gate

Report per story: root cause/scope, diff summary, device evidence, what was NOT done. WP-38 is complete when S9-S12 and S14a-S14d land (or are explicitly re-deferred with reason); S13 stays gated on its own precondition and does not block packet completion.

## Progress

- 2026-07-09 — Packet created from WP-37's "Explicitly deferred" list after WP-37 closeout verification (8/8 stories confirmed merged, PR #53 closed, local worktree synced and rebuilt clean). Not started.
