# Portfolio Dashboard

Last updated: 2026-06-02 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS v1.0 build 6 is in App Store review context and should stay frozen. Resumely iOS cleared analytics and UX/export gates on June 1, so the next constraint is an authenticated real-device smoke plus App Store Connect upload. RunSmart Web and ResumeBuilder Web are support repos and need dirty-tree triage before more implementation.

Best next action: Resumely iOS: run the authenticated device smoke from tasks/session-log.md, verify PostHog/export coverage, then upload screenshots/listing and submit. RunSmart iOS: monitor Apple review and do not mutate v1.0 release artifacts.

## Run Center

- Last refresh: 2026-06-02 15:52
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | App Store submission sprint (Build 6) | Run a short simulator UI smoke through each root tab after the existing release branch is ready for interactive QA | Yes | Fresh | High |
| Resumely iOS | Pre-release (TestFlight prep) | Upload rb-aso-002 screenshots to App Store Connect once an ASC API key/session is available, then confirm Privacy Policy and Support URLs | Yes | Fresh | High |
| RunSmart Web | Sprint 11 backend support / reference | Triage modified/untracked files before more web work. | Yes | Fresh | Medium |
| ResumeBuilder AI (Web) | PDF parse/render-preview rollout | Leave parked unless Resumely smoke exposes backend parse/render issues. | Yes | Fresh | Medium |
| Agentic OS | Cross-project status and executive refresh | Run dashboard JSON checks. | No | Fresh | Medium |

## Decision Board

| Decision | Project | Recommendation | Urgency |
| --- | --- | --- | --- |
| RunSmart 1.0.1 smallest safe scope | RunSmart iOS | Wait for v1.0 review outcome, then cherry-pick the highest-impact Sprint 11 stories. | Medium |
| Resumely iOS App Store upload path | Resumely iOS | Use Fastlane if credentials are available; otherwise manual portal upload after smoke passes. | High |
| ResumeBuilder Web rollout timing | ResumeBuilder AI Web | Defer unless Resumely smoke finds backend blockers. | Medium |

## Agent Delegation

- **Release Manager**: Run Resumely iOS live-device smoke, then prepare ASC upload. Evidence: PROJECT-STATUS.md, dashboard/status.json, ResumeBuilder iOS tasks/session-log.md
- **CEO OS**: Resolve the next portfolio decision and keep focus tight. Evidence: executive-os/EXECUTIVE-DASHBOARD.md, dashboard/status.json decisionBoard
- **Director / Orchestrator**: Turn the current Action Board into one reviewable work packet. Evidence: dashboard/status.json priorityBoard and projectHealth
- **QA**: Verify dashboard or product readiness with evidence. Evidence: GLOBAL-QA-RULES.md, dashboard runCenter checksRun

## Validation

- dashboard/status.json parsed
- embedded dashboard JSON parsed
- project-status.html fallback sync checked
- source confidence and freshness validated
- git diff --check
