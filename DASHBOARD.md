# Portfolio Dashboard

Last updated: 2026-06-04 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — App Store Review: After review approval — merge version-2 to main, update PROJECT-STATUS.md, publish launch post · Resumely iOS — App Store submission readiness: Unlock/authorize Apple Distribution private-key access in Keychain/Xcode, then export/upload the existing archive through Xcode Organizer/App Store Connect · RunSmart Web — Sprint 11 backend support / reference · ResumeBuilder AI (Web) — PDF parse/render-preview rollout

Best next action: Resumely iOS: Unlock/authorize Apple Distribution private-key access in Keychain/Xcode, then export/upload the existing archive through Xcode Organizer/App Store Connect

## Run Center

- Last refresh: 2026-06-04 13:47
- Localhost: `http://127.0.0.1:8789/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | App Store Review | After review approval — merge version-2 to main, update PROJECT-STATUS.md, publish launch post | Yes | Fresh | High |
| Resumely iOS | App Store submission readiness | Unlock/authorize Apple Distribution private-key access in Keychain/Xcode, then export/upload the existing archive through Xcode Organizer/App Store Connect | Yes | Fresh | High |
| RunSmart Web | Sprint 11 backend support / reference | Triage modified/untracked files before more web work. | Yes | Needs Review | Medium |
| ResumeBuilder AI (Web) | PDF parse/render-preview rollout | Leave parked unless Resumely smoke exposes backend parse/render issues. | Yes | Fresh | Medium |
| Agentic OS | Dashboard trust upgrade (top-tier roadmap execution) | All roadmap phases (0–6) shipped. Remaining optional: Phase 2.3 web-repo progress.md seeding (on hold), Phase 6.3 opt-in pre-commit hook, and the INTENT-LOG audit on 2026-06-16 | Yes | Fresh | High |

## Decision Board

| Decision | Project | Recommendation | Urgency |
| --- | --- | --- | --- |
| RunSmart iOS: build 8 rejection response scope | RunSmart iOS | Minimal fix targeting only the rejection reason. Ship as build 9. Save v2 feature scope for after approval. | Conditional — only if build 8 is rejected |
| RunSmart iOS: when to flip VOICE_COACH_ENABLED in Vercel | RunSmart iOS | Flip after approval + physical-device voice QA passes. Do not flip before the app is live. | Post-approval |
| Resumely iOS: App Store upload path | Resumely iOS | Manual Xcode Organizer path. EXD-006 resolved: no Fastlane, no .p8 key found. Xcode Organizer is the path. | High — next action after device smoke |
| ResumeBuilder Web rollout timing | ResumeBuilder AI Web | Defer unless Resumely smoke finds backend blockers. | Low |

## Agent Delegation

- **Release Manager**: Run Resumely iOS live-device smoke, then prepare ASC upload. Evidence: PROJECT-STATUS.md, dashboard/status.json, ResumeBuilder iOS tasks/session-log.md
- **CEO OS**: Resolve the next portfolio decision and keep focus tight. Evidence: executive-os/EXECUTIVE-DASHBOARD.md, dashboard/status.json decisionBoard
- **Director / Orchestrator**: Turn the current Action Board into one reviewable work packet. Evidence: dashboard/status.json priorityBoard and projectHealth
- **QA**: Verify dashboard or product readiness with evidence. Evidence: GLOBAL-QA-RULES.md, dashboard runCenter checksRun

## Evidence Gaps

- Agentic OS: validated 2026-06-02, latest commit is newer.

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
