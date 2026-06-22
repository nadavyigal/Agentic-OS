# Portfolio Dashboard

Last updated: 2026-06-21 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — LIVE on App Store since 2026-06-19 — post-launch iteration on v1.0.3 build 16. Next train is Garmin readiness work, not another App Store submission: Garmin readiness Story 1 — physical TestFlight smoke evidence for the readiness flow. Separately, decide whether to flip VOICE_COACH_ENABLED now that the app is live · Resumely iOS — Post-launch — D7 Gate A monitoring. App is live; no approval pending: (1) D7 readout ~7 days after the confirmed go-live date — pull 7-day activation funnel from PostHog dashboard 1720819. Exact readout date depends on the App Store live date (confirm with founder). (2) Monitor reviews + crash/error events · RunSmart Web — Garmin production enablement (web/backend audit + hardening) · ResumeBuilder AI (Web) — ATS scoring pipeline error sweep — LinkedIn scrape-blocking fix implemented, awaiting production verification on Vercel preview

Best next action: Resumely iOS: (1) D7 readout ~7 days after the confirmed go-live date — pull 7-day activation funnel from PostHog dashboard 1720819. Exact readout date depends on the App Store live date (confirm with founder). (2) Monitor reviews + crash/error events

## Run Center

- Last refresh: 2026-06-21 13:48
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | LIVE on App Store since 2026-06-19 — post-launch iteration on v1.0.3 build 16. Next train is Garmin readiness work, not another App Store submission | Garmin readiness Story 1 — physical TestFlight smoke evidence for the readiness flow. Separately, decide whether to flip VOICE_COACH_ENABLED now that the app is live | Yes | Fresh | High |
| Resumely iOS | Post-launch — D7 Gate A monitoring. App is live; no approval pending | (1) D7 readout ~7 days after the confirmed go-live date — pull 7-day activation funnel from PostHog dashboard 1720819. Exact readout date depends on the App Store live date (confirm with founder). (2) Monitor reviews + crash/error events | Yes | Fresh | Medium |
| RunSmart Web | Garmin production enablement (web/backend audit + hardening) | Founder approval to apply migration 20260621000000_restrict_garmin_worker_rpc_grants.sql; then manual Gate 2/3/4 portal+email tasks (see tasks/work-pack-garmin-gate-1-4.md) | No | Fresh | High |
| ResumeBuilder AI (Web) | ATS scoring pipeline error sweep — LinkedIn scrape-blocking fix implemented, awaiting production verification on Vercel preview | After preview verification passes, merge fix/linkedin-guest-scrape and remove (or keep 404-gated) the debug route; only revisit a residential proxy if LinkedIn 429s the Vercel IP at scale (fetchHtml() seam is ready) | No | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; optionally add GLOBAL-OUTPUT-CONTRACT.md (deferred from the prompt study); add no further loop cards unless current and non-duplicative | Yes | Fresh | High |

## Stranded Work

14 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] cursor/e7-wearable-depth-trends: unmerged commits, never pushed, last commit 2026-06-12
- [RunSmart iOS] worktree on claude/tender-thompson-60f370 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/tender-thompson-60f370
- [RunSmart iOS] worktree on claude/youthful-moore-9d85c7 at /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/.claude/worktrees/youthful-moore-9d85c7
- [RunSmart iOS] 8 uncommitted file(s) in the primary working tree
- [Resumely iOS] main is 2 commit(s) behind origin (pull needed)
- [Resumely iOS] worktree on claude/focused-raman-18ce50 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/focused-raman-18ce50
- [Resumely iOS] worktree on claude/relaxed-northcutt-cb6240 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/relaxed-northcutt-cb6240
- [Resumely iOS] worktree on claude/reverent-buck-a366b2 at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/reverent-buck-a366b2
- [Resumely iOS] worktree on chore/progress-ats-fix-pending-release, 1 uncommitted file(s) at /Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/.claude/worktrees/upbeat-matsumoto-a92be3
- [Resumely iOS] 11 uncommitted file(s) in the primary working tree
- [RunSmart Web] claude/dedup-imported-skill-packs: unmerged commits, remote branch deleted, last commit 2026-06-20
- [RunSmart Web] worktree on claude/pensive-dewdney-b2a0a4, 1 uncommitted file(s) at /Users/nadavyigal/Documents/RunSmart/.claude/worktrees/pensive-dewdney-b2a0a4
- [ResumeBuilder AI (Web)] main is 4 commit(s) behind origin (pull needed)
- [Agentic OS] 8 uncommitted file(s) in the primary working tree

## Work Packet Hygiene

- None. Active/open packet states match the current project status.

## Decision Board

| Decision | Project | Recommendation | Urgency |
| --- | --- | --- | --- |
| RunSmart iOS: build 8 rejection response scope | RunSmart iOS | Minimal fix targeting only the rejection reason. Ship as build 9. Save v2 feature scope for after approval. | Conditional — only if build 8 is rejected |
| RunSmart iOS: when to flip VOICE_COACH_ENABLED in Vercel | RunSmart iOS | **PARKED** — keep flag false until Garmin Story 1 + activation readout; then physical voice QA before flip. See `executive-os/research/2026-06-22-voice-coach-flip-storm-deep-research.md`. | Parked |
| Resumely iOS: App Store upload path | Resumely iOS | Manual Xcode Organizer path. EXD-006 resolved: no Fastlane, no .p8 key found. Xcode Organizer is the path. | High — next action after device smoke |
| ResumeBuilder Web rollout timing | ResumeBuilder AI Web | Defer unless Resumely smoke finds backend blockers. | Low |

## Agent Delegation

- **Release Manager**: Handle an App Store review outcome without reopening completed submission work. Evidence: PROJECT-STATUS.md, dashboard/status.json, ResumeBuilder iOS tasks/session-log.md
- **CEO OS**: Resolve the next portfolio decision and keep focus tight. Evidence: executive-os/EXECUTIVE-DASHBOARD.md, dashboard/status.json decisionBoard
- **Director / Orchestrator**: Turn the current Action Board into one reviewable work packet. Evidence: dashboard/status.json priorityBoard and projectHealth
- **QA**: Verify dashboard or product readiness with evidence. Evidence: GLOBAL-QA-RULES.md, dashboard runCenter checksRun

## Evidence Gaps

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
