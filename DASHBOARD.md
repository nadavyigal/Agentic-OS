# Portfolio Dashboard

Last updated: 2026-06-17 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — Live on App Store; monitor launch analytics and complete the real-device/TestFlight authenticated smoke follow-up: Wait for build 15 processing, update App Store Connect App Privacy and App Review notes with the delete-account screen recording, run the live smoke on an Apple-auth-capable physical device/TestFlight build, then select build 15 and resubmit · Resumely iOS — Live on App Store; monitor Gate A analytics through the D7 dashboard (deadline 2026-06-21): Ship build with PR #60 events to App Store; fix /api/v1/resumes 404 in web repo and re-enable isResumeLibraryEnabled · RunSmart Web — Today page improvement planning, post Aha Moments merge · ResumeBuilder AI (Web) — Pre-launch support for Resumely iOS submission; PDF parse/render-preview rollout parked

Best next action: Resumely iOS: Ship build with PR #60 events to App Store; fix /api/v1/resumes 404 in web repo and re-enable isResumeLibraryEnabled

## Run Center

- Last refresh: 2026-06-17 19:18
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Live on App Store; monitor launch analytics and complete the real-device/TestFlight authenticated smoke follow-up | Wait for build 15 processing, update App Store Connect App Privacy and App Review notes with the delete-account screen recording, run the live smoke on an Apple-auth-capable physical device/TestFlight build, then select build 15 and resubmit | Yes | Fresh | High |
| Resumely iOS | Live on App Store; monitor Gate A analytics through the D7 dashboard (deadline 2026-06-21) | Ship build with PR #60 events to App Store; fix /api/v1/resumes 404 in web repo and re-enable isResumeLibraryEnabled | Yes | Fresh | High |
| RunSmart Web | Today page improvement planning, post Aha Moments merge | Implement Story 1 (Today content inventory and preservation map) before any Today redesign work | Yes | Fresh | High |
| ResumeBuilder AI (Web) | Pre-launch support for Resumely iOS submission; PDF parse/render-preview rollout parked | Enable Resume Library in iOS (flip RuntimeFeatures.isResumeLibraryEnabled = true); PDF + DOCX upload smoke test | No | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; add no further loop cards unless it remains current and non-duplicative | Yes | Fresh | High |

## Stranded Work

17 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] worktree on claude/tender-thompson-60f370 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/tender-thompson-60f370
- [RunSmart iOS] worktree on claude/youthful-moore-9d85c7 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/youthful-moore-9d85c7
- [RunSmart iOS] 22 uncommitted file(s) in the primary working tree
- [Resumely iOS] main is 7 commit(s) behind origin (pull needed)
- [Resumely iOS] claude/relaxed-northcutt-cb6240: unmerged commits, remote branch deleted, last commit 2026-06-16
- [Resumely iOS] feat/localization-updates: unmerged commits, remote branch deleted, last commit 2026-06-16
- [Resumely iOS] monitization: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] worktree on codex/post-live-d7-readout at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-d7-readout
- [Resumely iOS] worktree on codex/resumely-release-qa at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP-resumely-release-qa
- [Resumely iOS] worktree on claude/focused-raman-18ce50 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/focused-raman-18ce50
- [Resumely iOS] worktree on version-2 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/relaxed-northcutt-cb6240
- [Resumely iOS] worktree on claude/reverent-buck-a366b2 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/reverent-buck-a366b2
- [Resumely iOS] worktree on codex/posthog-device-qa at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder-IOS-APP-posthog-device-qa
- [Resumely iOS] 40 uncommitted file(s) in the primary working tree
- [RunSmart Web] fix/garmin-ios-branch-fixes: 1 unpushed commit(s), last commit 2026-06-16
- [RunSmart Web] 4 uncommitted file(s) in the primary working tree
- [Agentic OS] 13 uncommitted file(s) in the primary working tree

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

- RunSmart Web: validated 2026-06-12, latest commit is newer.
- ResumeBuilder AI (Web): validated 2026-06-16, latest commit is newer.
- Agentic OS: validated 2026-06-12, latest commit is newer.

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
