# Portfolio Dashboard

Last updated: 2026-07-17 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — PHASE 2 — Release 1.0.8 (22) (WP-37/38/40 bundle): Monitor Apple review of build 8 (submitted 2026-06-03); check App Store Connect for outcome. · Resumely iOS — Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists: Founder: unlock iPhone 13 → install: xcrun devicectl device install app --device 4A1D6EF2-8945-55B8-931A-46980B2A27E2 '/var/tmp/resumebuilder-device-derived/Build/Products/Debug-iphoneos/ResumeBuilder IOS APP.app' · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

Best next action: Resumely iOS: Founder: unlock iPhone 13 → install: xcrun devicectl device install app --device 4A1D6EF2-8945-55B8-931A-46980B2A27E2 '/var/tmp/resumebuilder-device-derived/Build/Products/Debug-iphoneos/ResumeBuilder IOS APP.app'

## Run Center

- Last refresh: 2026-07-17 14:36
- Localhost: `http://127.0.0.1:8787/portfolio-hq.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | PHASE 2 — Release 1.0.8 (22) (WP-37/38/40 bundle) | Monitor Apple review of build 8 (submitted 2026-06-03); check App Store Connect for outcome. | No | Unknown | Unknown |
| Resumely iOS | Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists | Founder: unlock iPhone 13 → install: xcrun devicectl device install app --device 4A1D6EF2-8945-55B8-931A-46980B2A27E2 '/var/tmp/resumebuilder-device-derived/Build/Products/Debug-iphoneos/ResumeBuilder IOS APP.app' | No | Unknown | Unknown |
| RunSmart Web | Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes | Triage modified/untracked files before more web work. | No | Unknown | Unknown |
| ResumeBuilder AI (Web) | WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next | Leave parked unless Resumely smoke exposes backend parse/render issues. | No | Unknown | Unknown |
| Agentic OS | Advanced OS patterns lean pilot | Finish dashboard-trust reconciliation, push Agentic OS main, then use the refreshed one-move recommendation for today's work | Yes | Fresh | Medium |

## Stranded Work

1 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [Agentic OS] 15 uncommitted file(s) in the primary working tree

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

- Agentic OS: validated 2026-07-13, latest commit is newer.

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
