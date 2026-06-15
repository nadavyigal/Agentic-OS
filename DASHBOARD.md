# Portfolio Dashboard

Last updated: 2026-06-15 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — 1.0.2 build 15 - App Store Connect processing and resubmission prep: Wait for build 15 processing, update App Store Connect App Privacy and App Review notes with the delete-account screen recording, run the live smoke on an Apple-auth-capable physical device/TestFlight build, then select build 15 and resubmit · Resumely iOS — Product experience polish: Complete an authenticated real-device smoke with delete-account/re-register, upload a real resume/job, optimize through diagnosis, export/share PDF, then validate/upload the archive from Xcode Organizer with App Store distribution signing · RunSmart Web — Today page improvement planning, post Aha Moments merge · ResumeBuilder AI (Web) — Pre-launch support for Resumely iOS submission; PDF parse/render-preview rollout parked

Best next action: Resumely iOS: Complete an authenticated real-device smoke with delete-account/re-register, upload a real resume/job, optimize through diagnosis, export/share PDF, then validate/upload the archive from Xcode Organizer with App Store distribution signing

## Run Center

- Last refresh: 2026-06-15 16:04
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | 1.0.2 build 15 - App Store Connect processing and resubmission prep | Wait for build 15 processing, update App Store Connect App Privacy and App Review notes with the delete-account screen recording, run the live smoke on an Apple-auth-capable physical device/TestFlight build, then select build 15 and resubmit | No | Fresh | High |
| Resumely iOS | Product experience polish | Complete an authenticated real-device smoke with delete-account/re-register, upload a real resume/job, optimize through diagnosis, export/share PDF, then validate/upload the archive from Xcode Organizer with App Store distribution signing | Yes | Fresh | High |
| RunSmart Web | Today page improvement planning, post Aha Moments merge | Implement Story 1 (Today content inventory and preservation map) before any Today redesign work | Yes | Fresh | High |
| ResumeBuilder AI (Web) | Pre-launch support for Resumely iOS submission; PDF parse/render-preview rollout parked | PDF + DOCX upload end-to-end smoke test (top risk before App Store approval), then replace the APP_STORE_URL placeholder (id000000000) in src/app/[locale]/ats-checker/page.tsx | No | Needs Review | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; add no further loop cards unless it remains current and non-duplicative | Yes | Needs Review | High |

## Stranded Work

10 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] worktree on claude/tender-thompson-60f370 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/tender-thompson-60f370
- [RunSmart iOS] worktree on claude/youthful-moore-9d85c7 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/youthful-moore-9d85c7
- [Resumely iOS] claude/gracious-curie-fcd112: 2 unpushed commit(s), last commit 2026-06-14
- [Resumely iOS] claude/sweet-agnesi-7d2c70: 1 unpushed commit(s), last commit 2026-06-14
- [Resumely iOS] worktree on claude/busy-babbage-13492c at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/busy-babbage-13492c
- [Resumely iOS] worktree on claude/gracious-curie-fcd112 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/gracious-curie-fcd112
- [Resumely iOS] worktree on claude/sweet-agnesi-7d2c70 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/sweet-agnesi-7d2c70
- [Resumely iOS] 4 uncommitted file(s) in the primary working tree
- [RunSmart Web] 3 uncommitted file(s) in the primary working tree
- [Agentic OS] 11 uncommitted file(s) in the primary working tree

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
