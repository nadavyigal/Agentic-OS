# Portfolio Dashboard

Last updated: 2026-07-21 IDT

Local evidence mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, the previous EOD handoff, and the freshest task/plan evidence across active worktrees. PostHog decision snapshots remain a separately dated manual layer.

## Executive Summary

RunSmart iOS — Public 1.1.1 (25) reinstall journey — mechanics PASS, S0 still eligibility-blocked; three telemetry defects found (2026-07-21): Once 1.0.9 (23) is approved and live: verify WP-43/45 events firing in PostHog for real users, then Experiment E1 (coach preview). If App Review flags S6 or S1 (the waived items), they are the first place to look. Known analytics semantics to remember when reading funnels: onboarding_step_abandoned fires on any backgrounding; plan_generation_timed_out duration inflates if backgrounded mid-poll · Resumely iOS — Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists: Re-run PostHog picker→file-selected funnel on **2026-07-25** (or minimum check **2026-07-18**) for clean `marketing_version=1.4.1` cohort; see deferred-read entry above for query definition · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

Best next action: Resumely iOS: Re-run PostHog picker→file-selected funnel on **2026-07-25** (or minimum check **2026-07-18**) for clean `marketing_version=1.4.1` cohort; see deferred-read entry above for query definition

## Run Center

- Last refresh: 2026-07-21 14:30
- Localhost: `http://127.0.0.1:8787/portfolio-hq.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Public 1.1.1 (25) reinstall journey — mechanics PASS, S0 still eligibility-blocked; three telemetry defects found (2026-07-21) | Once 1.0.9 (23) is approved and live: verify WP-43/45 events firing in PostHog for real users, then Experiment E1 (coach preview). If App Review flags S6 or S1 (the waived items), they are the first place to look. Known analytics semantics to remember when reading funnels: onboarding_step_abandoned fires on any backgrounding; plan_generation_timed_out duration inflates if backgrounded mid-poll | Yes | Fresh | High |
| Resumely iOS | Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists | Re-run PostHog picker→file-selected funnel on **2026-07-25** (or minimum check **2026-07-18**) for clean `marketing_version=1.4.1` cohort; see deferred-read entry above for query definition | Yes | Fresh | High |
| RunSmart Web | Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes | **Still paused.** Restoring actual sync for the 9 reauth_required users needs either a working production/commercial credential set (WP-26 Steps 3-4) or pointing real users at the Evaluation-tier Internal Test app (the same Terms violation that got the old app deactivated) — there is no maintenance-mode-compatible fix available. This is a fact worth surfacing at the day-30 revisit (~2026-08-01), not a reason to resume now. See Agentic OS WP-26/27/28 for the paused relaunch scope | Yes | Stale | Medium |
| ResumeBuilder AI (Web) | WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next | WP-29 S5 — design and implement anonymous session carryover after signup so the first dashboard is not empty | Yes | Fresh | High |
| Agentic OS | Daily portfolio operations and evidence reconciliation | In the Resumely iOS repo, review and merge `claude/session-ec92e2`, then prepare 1.4.4 with a fresh build number and the documented release/physical QA gates. Do not archive or upload without explicit founder authorization | Yes | Fresh | High |

## Stranded Work

63 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] main is 8 commit(s) behind origin (pull needed)
- [RunSmart iOS] backup-7b15df1-docs: unmerged commits, never pushed, last commit 2026-07-13
- [RunSmart iOS] claude/1-1-1-submitted-for-review: unmerged commits, remote branch deleted, last commit 2026-07-20
- [RunSmart iOS] claude/bold-noyce-678ace: unmerged commits, remote branch deleted, last commit 2026-07-14
- [RunSmart iOS] claude/runsmart-ios-signin-wall-95dcb4: unmerged commits, remote branch deleted, last commit 2026-07-20
- [RunSmart iOS] claude/session-2026-07-20-wp51-merge-triage: unmerged commits, remote branch deleted, last commit 2026-07-20
- [RunSmart iOS] claude/wp51-app-version-super-property: unmerged commits, remote branch deleted, last commit 2026-07-20
- [RunSmart iOS] claude/wp51-device-verification: unmerged commits, remote branch deleted, last commit 2026-07-20
- [RunSmart iOS] codex/adaptive-coach-device-qa-fixture: unmerged commits, remote branch deleted, last commit 2026-07-19
- [RunSmart iOS] codex/docs-1.0.9-activation-read: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] codex/wp40-release-closeout: unmerged commits, never pushed, last commit 2026-07-12
- [RunSmart iOS] docs/1.0.9-asc-submission-waiver: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] docs/public-108-smoke-2026-07-13: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] fix/zero-streak-profile: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart iOS] preserve/apple-garmin-sync-docs: unmerged commits, never pushed, last commit 2026-06-21
- [RunSmart iOS] release/1.0.9-build23: unmerged commits, remote branch deleted, last commit 2026-07-15
- [RunSmart iOS] worktree on codex/weekly-release-cadence at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app-telemetry-repair
- [RunSmart iOS] worktree on feat/adaptive-coach-phase1 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/adaptive-coach-phase1
- [RunSmart iOS] worktree on fix/zero-streak-profile, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/bold-noyce-678ace
- [RunSmart iOS] worktree on fix/flexweek-duplicate-slot-ids at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/flexweek-dup-id-fix
- [RunSmart iOS] worktree on claude/runsmart-ios-signin-wall-95dcb4, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/runsmart-1-0-9-verification-f8e8a2
- [RunSmart iOS] worktree on claude/runsmart-ftux-audit-240648, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/runsmart-ftux-audit-240648
- [RunSmart iOS] worktree on claude/1-1-1-submitted-for-review at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/runsmart-session-prompt-a6406d
- [RunSmart iOS] worktree on codex/docs-1.0.9-activation-read at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /runsmart-1.0.9-activation-read
- [RunSmart iOS] worktree on codex/runsmart-adaptive-preview at /Users/nadavyigal/Documents/Projects /runsmart-adaptive-preview
- [RunSmart iOS] 6 uncommitted file(s) in the primary working tree
- [Resumely iOS] claude/release-b-story-9: 1 unpushed commit(s), last commit 2026-07-16
- [Resumely iOS] codex/wp46-story-10: 3 unpushed commit(s), last commit 2026-07-18
- [Resumely iOS] codex/wp46-story-11: 1 unpushed commit(s), last commit 2026-07-18
- [Resumely iOS] codex/wp46-story-12: 2 unpushed commit(s), last commit 2026-07-18
- [Resumely iOS] codex/wp46-story-13: 6 unpushed commit(s), last commit 2026-07-19
- [Resumely iOS] chore/release-c-1.4.3-version-bump: unmerged commits, remote branch deleted, last commit 2026-07-19
- [Resumely iOS] claude/activation-cliff-plan: unmerged commits, remote branch deleted, last commit 2026-07-19
- [Resumely iOS] claude/release-c-story-13-submit-769148: unmerged commits, remote branch deleted, last commit 2026-07-19
- [Resumely iOS] claude/resumely-ios-activation-cohort-2ab57e: unmerged commits, remote branch deleted, last commit 2026-07-20
- [Resumely iOS] codex/wp45-s0-measurement-contract: unmerged commits, never pushed, last commit 2026-07-12
- [Resumely iOS] feat/localization-updates: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] pr-72-review: unmerged commits, never pushed, last commit 2026-06-22
- [Resumely iOS] worktree on codex/release-a-measurement-baseline-2026-07-16 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-measurement-baseline
- [Resumely iOS] worktree on codex/reconcile-release-a-1.4.2 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-release-a-reconcile
- [Resumely iOS] worktree on codex/wp46-story-10 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-story-10
- [Resumely iOS] worktree on codex/wp46-story-11 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-story-11
- [Resumely iOS] worktree on codex/wp46-story-13 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-story-13
- [Resumely iOS] worktree on claude/release-b-story-9 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-story-9
- [Resumely iOS] worktree on claude/resumely-1-4-4-version-bump, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/resumely-1-4-4-release-416c92
- [Resumely iOS] worktree on claude/release-c-story-13-submit-769148, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/resumely-release-a-b-landing-325d9a
- [Resumely iOS] 7 uncommitted file(s) in the primary working tree
- [RunSmart Web] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart Web] pr-108-review: unmerged commits, never pushed, last commit 2026-06-30
- [RunSmart Web] 8 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] fix/posthog-expert-event-dedupe: 1 unpushed commit(s), last commit 2026-07-09
- [ResumeBuilder AI (Web)] fix/ats-keyword-phrase-quality: unmerged commits, remote branch deleted, last commit 2026-06-22
- [ResumeBuilder AI (Web)] fix/pdf-parse-xref-error: unmerged commits, never pushed, last commit 2026-06-03
- [ResumeBuilder AI (Web)] pr-83-review: unmerged commits, never pushed, last commit 2026-06-22
- [ResumeBuilder AI (Web)] worktree on codex/fix-web-export-observability at /Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai--export-observability
- [ResumeBuilder AI (Web)] 10 uncommitted file(s) in the primary working tree
- [Agentic OS] main has 2 unpushed commit(s)
- [Agentic OS] dashboard/ftux-submissions-and-artifacts: 3 unpushed commit(s), last commit 2026-07-16
- [Agentic OS] claude/activation-autopsy-2026-07-19: unmerged commits, remote branch deleted, last commit 2026-07-19
- [Agentic OS] worktree on detached at /Users/nadavyigal/Documents/Projects /Agentic OS/.claude/worktrees/agentic-os-session-ae5ec5
- [Agentic OS] worktree on claude/resumely-session-70fcda, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /Agentic OS/.claude/worktrees/resumely-session-70fcda
- [Agentic OS] 18 uncommitted file(s) in the primary working tree

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

- Resumely iOS: validated 2026-07-11, latest commit is newer.
- RunSmart Web: validated 2026-07-03, latest commit is newer.
- ResumeBuilder AI (Web): validated 2026-07-03, latest commit is newer.

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
