# Portfolio Dashboard

Last updated: 2026-06-12 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — 1.0.2 (build 14) development and App Store resubmission prep: Push feat/wp6-aha-moments-ios, merge to main, then archive and upload 1.0.2 build 14 to App Store Connect and resubmit with the reviewer response · Resumely iOS — App Store submission readiness: Rebuild on real device, sign in, smoke optimize → Improve ATS → Preview & Export PDF → Submit Package → Save Package to Me → open package in Me → share resume PDF/copy cover letter/tap Submit at Job Link · RunSmart Web — Implement Story 1 for the RunSmart Web Today page improvement · ResumeBuilder AI (Web) — PDF parse/render-preview rollout

Best next action: Resumely iOS: Rebuild on real device, sign in, smoke optimize → Improve ATS → Preview & Export PDF → Submit Package → Save Package to Me → open package in Me → share resume PDF/copy cover letter/tap Submit at Job Link

## Run Center

- Last refresh: 2026-06-12 10:13
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | 1.0.2 (build 14) development and App Store resubmission prep | Push feat/wp6-aha-moments-ios, merge to main, then archive and upload 1.0.2 build 14 to App Store Connect and resubmit with the reviewer response | No | Fresh | Medium |
| Resumely iOS | App Store submission readiness | Rebuild on real device, sign in, smoke optimize → Improve ATS → Preview & Export PDF → Submit Package → Save Package to Me → open package in Me → share resume PDF/copy cover letter/tap Submit at Job Link | Yes | Fresh | High |
| RunSmart Web | Implement Story 1 for the RunSmart Web Today page improvement | Run the first planning prompt from the final installation report to convert the next product idea into a brief, spec, and small implementation stories | No | Fresh | Medium |
| ResumeBuilder AI (Web) | PDF parse/render-preview rollout | Leave parked unless Resumely smoke exposes backend parse/render issues. | No | Fresh | Medium |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; add no further loop cards unless it remains current and non-duplicative | Yes | Fresh | High |

## Stranded Work

4 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] main is 2 commit(s) behind origin (pull needed)
- [RunSmart iOS] fix/code-review-p0-identity: unmerged commits, never pushed, last commit 2026-06-11
- [Resumely iOS] 4 uncommitted file(s) in the primary working tree
- [Agentic OS] 2 uncommitted file(s) in the primary working tree

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

- RunSmart iOS: validated 2026-06-11, latest commit is newer.
- RunSmart Web: validated 2026-05-12, latest commit is newer.

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
