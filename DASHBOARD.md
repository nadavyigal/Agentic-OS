# Portfolio Dashboard

Last updated: 2026-06-21 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — Post-launch iteration — v1.0.3 build 16 archive + TestFlight upload pending: Open Xcode → Product → Archive → upload to TestFlight. Once TestFlight processing done (~10-20 min), submit to App Store · Resumely iOS — D7 Gate A — awaiting Apple approval: (1) Confirm Apple approval + monitor for rejection notes. (2) D7 readout on or after 2026-06-24 via connected PostHog plugin — pull 7-day activation funnel from dashboard 1720819. (3) Close PR #68 after merge · RunSmart Web — Today page improvement planning, post Aha Moments merge · ResumeBuilder AI (Web) — ATS scoring pipeline error sweep — LinkedIn scrape-blocking fix implemented, awaiting production verification on Vercel preview

Best next action: Resumely iOS: (1) Confirm Apple approval + monitor for rejection notes. (2) D7 readout on or after 2026-06-24 via connected PostHog plugin — pull 7-day activation funnel from dashboard 1720819. (3) Close PR #68 after merge

## Run Center

- Last refresh: 2026-06-21 07:39
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Post-launch iteration — v1.0.3 build 16 archive + TestFlight upload pending | Open Xcode → Product → Archive → upload to TestFlight. Once TestFlight processing done (~10-20 min), submit to App Store | Yes | Fresh | High |
| Resumely iOS | D7 Gate A — awaiting Apple approval | (1) Confirm Apple approval + monitor for rejection notes. (2) D7 readout on or after 2026-06-24 via connected PostHog plugin — pull 7-day activation funnel from dashboard 1720819. (3) Close PR #68 after merge | Yes | Fresh | Medium |
| RunSmart Web | Today page improvement planning, post Aha Moments merge | Implement Story 1 (Today content inventory and preservation map) before any Today redesign work | Yes | Fresh | High |
| ResumeBuilder AI (Web) | ATS scoring pipeline error sweep — LinkedIn scrape-blocking fix implemented, awaiting production verification on Vercel preview | After preview verification passes, merge fix/linkedin-guest-scrape and remove (or keep 404-gated) the debug route; only revisit a residential proxy if LinkedIn 429s the Vercel IP at scale (fetchHtml() seam is ready) | No | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; add no further loop cards unless it remains current and non-duplicative | Yes | Fresh | High |

## Stranded Work

13 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] cursor/e7-wearable-depth-trends: unmerged commits, never pushed, last commit 2026-06-12
- [RunSmart iOS] worktree on claude/tender-thompson-60f370 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/tender-thompson-60f370
- [RunSmart iOS] worktree on claude/youthful-moore-9d85c7 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/youthful-moore-9d85c7
- [RunSmart iOS] 8 uncommitted file(s) in the primary working tree
- [Resumely iOS] worktree on claude/focused-raman-18ce50 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/focused-raman-18ce50
- [Resumely iOS] worktree on claude/relaxed-northcutt-cb6240 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/relaxed-northcutt-cb6240
- [Resumely iOS] worktree on claude/reverent-buck-a366b2 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/reverent-buck-a366b2
- [Resumely iOS] worktree on chore/progress-ats-fix-pending-release, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/upbeat-matsumoto-a92be3
- [Resumely iOS] 10 uncommitted file(s) in the primary working tree
- [RunSmart Web] fix/garmin-ios-branch-fixes: unmerged commits, never pushed, last commit 2026-06-16
- [RunSmart Web] 1 uncommitted file(s) in the primary working tree
- [Agentic OS] main has 1 unpushed commit(s)
- [Agentic OS] 1 uncommitted file(s) in the primary working tree

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
