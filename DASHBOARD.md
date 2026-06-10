# Portfolio Dashboard

Last updated: 2026-06-09 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — App Store Review Response: Run visual QA on reviewer device classes, archive/export build 12 with distribution signing, inspect archive provenance, upload to App Store Connect, and resubmit with the updated reviewer response · Resumely iOS — App Store submission readiness: Founder installs device binary on real device, signs in, smokes optimize→design→expert→export, screenshots PostHog Live Events (app_launched + optimization_completed + export_success), then archives via Xcode Organizer for ASC upload · RunSmart Web — Sprint 11 backend support / reference · ResumeBuilder AI (Web) — PDF parse/render-preview rollout

Best next action: Resumely iOS: Founder installs device binary on real device, signs in, smokes optimize→design→expert→export, screenshots PostHog Live Events (app_launched + optimization_completed + export_success), then archives via Xcode Organizer for ASC upload

## Run Center

- Last refresh: 2026-06-09 11:18
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | App Store Review Response | Run visual QA on reviewer device classes, archive/export build 12 with distribution signing, inspect archive provenance, upload to App Store Connect, and resubmit with the updated reviewer response | Yes | Fresh | High |
| Resumely iOS | App Store submission readiness | Founder installs device binary on real device, signs in, smokes optimize→design→expert→export, screenshots PostHog Live Events (app_launched + optimization_completed + export_success), then archives via Xcode Organizer for ASC upload | Yes | Needs Review | High |
| RunSmart Web | Sprint 11 backend support / reference | Triage modified/untracked files before more web work. | Yes | Stale | Low |
| ResumeBuilder AI (Web) | PDF parse/render-preview rollout | Leave parked unless Resumely smoke exposes backend parse/render issues. | Yes | Fresh | Medium |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; add no further loop cards unless it remains current and non-duplicative | Yes | Fresh | High |

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

- Agentic OS: validated 2026-06-05, latest commit is newer.

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
