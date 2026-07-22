# Portfolio Dashboard

Last updated: 2026-07-22 IDT

Local evidence mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, the previous EOD handoff, and the freshest task/plan evidence across active worktrees. PostHog decision snapshots remain a separately dated manual layer.

## Executive Summary

RunSmart iOS — Post-release watch. Nothing to build until the instrument reports: **Read `has_underlying_error` from the first real `sign_in_failed` on 1.1.2 (target 2026-07-29, T+7).** The verdict is the property value, not the count, and one event decides it. **True** → read `underlying_error_domain`/`_code`, name the precondition (device not signed into iCloud vs Apple ID without 2FA vs genuine app fault), fix with copy plus a precondition check. **False** → a genuinely bare 1000 the device cannot diagnose, which opens **WP-53** (email or guest fallback) on evidence rather than by elimination. **Third possible outcome, name it in advance:** code-1000 volume drops with `has_underlying_error` never going true — that means the iCloud-naming copy was the fix and WP-53 stays closed. Do not read a quiet funnel as "no data". Cheap prior check at T+1 (2026-07-23): confirm events arrive carrying `app_version` 1.1.2, which also re-validates the 1.1.1 fix for analytics losing app version/build after a fresh install · Resumely iOS — Post-release watch on the repaired instrument. The 1.4.5 cohort is accumulating; no read is valid yet: **In date order, and do not collapse them into one read.** (1) **T+1, 2026-07-23:** confirm events arrive carrying `app_version` 1.4.5 — cheapest check that the build reaches real installs. (2) **T+7, 2026-07-29:** monotonicity check, `optimized_preview_rendered` >= `export_success` on a fresh read. This validates the WP-51 instrument and is **not** an activation figure; reporting it as one repeats the error WP-50 corrected. (3) **2026-08-01:** EXD-022 reporting checkpoint — report the clean-activation count honestly, "too early" included; no verdict authority. (4) **T+14, 2026-08-05:** first definitive 1.4.5 cohort read against the >=20 clean-activation gate. Then **WP-48 S2-B** (`is_internal_tester` classifier on Debug/TestFlight builds), the last known measurement defect and the reason 27% of persons still contaminate raw reads, then **WP-56** (file picker, 27 open → 13 select, 48% abandonment with healthy steps either side), deliberately queued behind WP-51 so the gain is countable. Also still open: the deferred Hebrew/RTL PDF gate and triage of stale PRs #100, #96, #86 · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

Best next action: Resumely iOS: **In date order, and do not collapse them into one read.** (1) **T+1, 2026-07-23:** confirm events arrive carrying `app_version` 1.4.5 — cheapest check that the build reaches real installs. (2) **T+7, 2026-07-29:** monotonicity check, `optimized_preview_rendered` >= `export_success` on a fresh read. This validates the WP-51 instrument and is **not** an activation figure; reporting it as one repeats the error WP-50 corrected. (3) **2026-08-01:** EXD-022 reporting checkpoint — report the clean-activation count honestly, "too early" included; no verdict authority. (4) **T+14, 2026-08-05:** first definitive 1.4.5 cohort read against the >=20 clean-activation gate. Then **WP-48 S2-B** (`is_internal_tester` classifier on Debug/TestFlight builds), the last known measurement defect and the reason 27% of persons still contaminate raw reads, then **WP-56** (file picker, 27 open → 13 select, 48% abandonment with healthy steps either side), deliberately queued behind WP-51 so the gain is countable. Also still open: the deferred Hebrew/RTL PDF gate and triage of stale PRs #100, #96, #86

## Run Center

- Last refresh: 2026-07-22 20:35
- Localhost: `http://127.0.0.1:8787/portfolio-hq.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Post-release watch. Nothing to build until the instrument reports | **Read `has_underlying_error` from the first real `sign_in_failed` on 1.1.2 (target 2026-07-29, T+7).** The verdict is the property value, not the count, and one event decides it. **True** → read `underlying_error_domain`/`_code`, name the precondition (device not signed into iCloud vs Apple ID without 2FA vs genuine app fault), fix with copy plus a precondition check. **False** → a genuinely bare 1000 the device cannot diagnose, which opens **WP-53** (email or guest fallback) on evidence rather than by elimination. **Third possible outcome, name it in advance:** code-1000 volume drops with `has_underlying_error` never going true — that means the iCloud-naming copy was the fix and WP-53 stays closed. Do not read a quiet funnel as "no data". Cheap prior check at T+1 (2026-07-23): confirm events arrive carrying `app_version` 1.1.2, which also re-validates the 1.1.1 fix for analytics losing app version/build after a fresh install | Yes | Fresh | Medium |
| Resumely iOS | Post-release watch on the repaired instrument. The 1.4.5 cohort is accumulating; no read is valid yet | **In date order, and do not collapse them into one read.** (1) **T+1, 2026-07-23:** confirm events arrive carrying `app_version` 1.4.5 — cheapest check that the build reaches real installs. (2) **T+7, 2026-07-29:** monotonicity check, `optimized_preview_rendered` >= `export_success` on a fresh read. This validates the WP-51 instrument and is **not** an activation figure; reporting it as one repeats the error WP-50 corrected. (3) **2026-08-01:** EXD-022 reporting checkpoint — report the clean-activation count honestly, "too early" included; no verdict authority. (4) **T+14, 2026-08-05:** first definitive 1.4.5 cohort read against the >=20 clean-activation gate. Then **WP-48 S2-B** (`is_internal_tester` classifier on Debug/TestFlight builds), the last known measurement defect and the reason 27% of persons still contaminate raw reads, then **WP-56** (file picker, 27 open → 13 select, 48% abandonment with healthy steps either side), deliberately queued behind WP-51 so the gain is countable. Also still open: the deferred Hebrew/RTL PDF gate and triage of stale PRs #100, #96, #86 | Yes | Fresh | Medium |
| RunSmart Web | Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes | **Still paused.** Restoring actual sync for the 9 reauth_required users needs either a working production/commercial credential set (WP-26 Steps 3-4) or pointing real users at the Evaluation-tier Internal Test app (the same Terms violation that got the old app deactivated) — there is no maintenance-mode-compatible fix available. This is a fact worth surfacing at the day-30 revisit (~2026-08-01), not a reason to resume now. See Agentic OS WP-26/27/28 for the paused relaunch scope | Yes | Fresh | High |
| ResumeBuilder AI (Web) | WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next | WP-29 S5 — design and implement anonymous session carryover after signup so the first dashboard is not empty | Yes | Fresh | High |
| Agentic OS | Daily portfolio operations and evidence reconciliation | Fix the two red eval harnesses — they are the only deterministic quality gates the products have and both have been down for over a week. Start with the RunSmart plan-generator eval (`gh run view --log` on the newest failure; the step fails before writing `report.json`, so check the OPENAI_API_KEY repo secret first). Then, in the Resumely iOS repo, review and merge `claude/session-ec92e2` and prepare 1.4.4 | Yes | Fresh | High |

## Stranded Work

34 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] backup-7b15df1-docs: unmerged commits, never pushed, last commit 2026-07-13
- [RunSmart iOS] docs/1.0.9-asc-submission-waiver: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] docs/public-108-smoke-2026-07-13: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] fix/zero-streak-profile: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart iOS] preserve/apple-garmin-sync-docs: unmerged commits, never pushed, last commit 2026-06-21
- [RunSmart iOS] release/1.0.9-build23: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] worktree on feat/adaptive-coach-phase1 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/adaptive-coach-phase1
- [RunSmart iOS] worktree on fix/zero-streak-profile, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/bold-noyce-678ace
- [RunSmart iOS] worktree on fix/flexweek-duplicate-slot-ids at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/flexweek-dup-id-fix
- [RunSmart iOS] worktree on claude/healthkit-sync-journey-d6ce3e at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/healthkit-sync-journey-d6ce3e
- [RunSmart iOS] worktree on claude/apple-chain-diagnosis-252a35, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/lucid-swanson-18f638
- [RunSmart iOS] 1 uncommitted file(s) in the primary working tree
- [Resumely iOS] codex/wp46-story-10: 3 unpushed commit(s), last commit 2026-07-18
- [Resumely iOS] codex/wp46-story-11: 1 unpushed commit(s), last commit 2026-07-18
- [Resumely iOS] codex/wp46-story-12: 2 unpushed commit(s), last commit 2026-07-18
- [Resumely iOS] chore/release-c-1.4.3-version-bump: unmerged commits, remote branch deleted, last commit 2026-07-19
- [Resumely iOS] feat/localization-updates: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] pr-72-review: unmerged commits, never pushed, last commit 2026-06-22
- [Resumely iOS] worktree on codex/wp46-story-10 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-story-10
- [Resumely iOS] worktree on codex/wp46-story-11 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-story-11
- [Resumely iOS] worktree on detached at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/resumely-ios-1-4-5-prep-07f44c
- [Resumely iOS] 7 uncommitted file(s) in the primary working tree
- [RunSmart Web] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart Web] pr-108-review: unmerged commits, never pushed, last commit 2026-06-30
- [RunSmart Web] 8 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] fix/posthog-expert-event-dedupe: 1 unpushed commit(s), last commit 2026-07-09
- [ResumeBuilder AI (Web)] fix/ats-keyword-phrase-quality: unmerged commits, remote branch deleted, last commit 2026-06-22
- [ResumeBuilder AI (Web)] fix/pdf-parse-xref-error: unmerged commits, never pushed, last commit 2026-06-03
- [ResumeBuilder AI (Web)] pr-83-review: unmerged commits, never pushed, last commit 2026-06-22
- [ResumeBuilder AI (Web)] 10 uncommitted file(s) in the primary working tree
- [Agentic OS] dashboard/ftux-submissions-and-artifacts: 3 unpushed commit(s), last commit 2026-07-16
- [Agentic OS] worktree on detached at /Users/nadavyigal/Documents/Projects /Agentic OS/.claude/worktrees/agentic-os-session-ae5ec5
- [Agentic OS] 16 uncommitted file(s) in the primary working tree

## Work Packet Hygiene

- None. Active/open packet states match the current project status.

## Decision Board

| Decision | Project | Recommendation | Urgency |
| --- | --- | --- | --- |
| RunSmart iOS: build 8 rejection response scope | RunSmart iOS | Minimal fix targeting only the rejection reason. Ship as build 9. Save v2 feature scope for after approval. | Conditional — only if build 8 is rejected |
| RunSmart iOS: when to flip VOICE_COACH_ENABLED in Vercel | RunSmart iOS | Flip after approval + physical-device voice QA passes. Do not flip before the app is live. | Post-approval |
| Resumely iOS: App Store upload path | Resumely iOS | Manual Xcode Organizer path. EXD-006 resolved: no Fastlane, no .p8 key found. Xcode Organizer is the path. | High — next action after device smoke |
| ResumeBuilder Web rollout timing | ResumeBuilder AI Web | Defer unless Resumely smoke finds backend blockers. | Low |

## Agent Delegation

- **Release Manager**: Handle an App Store review outcome without reopening completed submission work. Evidence: PROJECT-STATUS.md, dashboard/status.json, ResumeBuilder iOS tasks/session-log.md
- **CEO OS**: Resolve the next portfolio decision and keep focus tight. Evidence: executive-os/EXECUTIVE-DASHBOARD.md, dashboard/status.json decisionBoard
- **Director / Orchestrator**: Turn the current Action Board into one reviewable work packet. Evidence: dashboard/status.json priorityBoard and projectHealth
- **QA**: Verify dashboard or product readiness with evidence. Evidence: GLOBAL-QA-RULES.md, dashboard runCenter checksRun

## Evidence Gaps

- Agentic OS: validated 2026-07-21, latest commit is newer.

## Drift Warnings

- None. Curated narrative matches the parsed source for all High-confidence projects.

## Validation

- parser unit tests
- dashboard/status.json parsed
- embedded dashboard JSON parsed
- project-status.html fallback sync checked
- source confidence and freshness validated
- drift warnings checked
- git diff --check
