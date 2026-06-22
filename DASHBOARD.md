# Portfolio Dashboard

Last updated: 2026-06-22 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — LIVE on App Store since 2026-06-19 — post-launch iteration on v1.0.3 build 16. Garmin readiness HRV source attribution is implemented locally on PR #55 branch: PR #55 review plus real-device/TestFlight evidence that Garmin Connect HRV samples arrive in HealthKit with the expected Garmin source metadata. Separately, decide whether to flip VOICE_COACH_ENABLED now that the app is live · Resumely iOS — Post-launch — D7 Gate A monitoring. App is live; no approval pending. Next build (1.1 (6)) pending to carry ATS copy fix: (1) D7 readout ~7 days after go-live (~2026-06-28) — pull 7-day activation funnel from PostHog dashboard 1720819. (2) Bump to 1.1 (6), archive, and submit to carry PR #70 ATS copy fix. (3) Regenerate App Store screenshots before next submission. (4) Monitor reviews + crash/error events · RunSmart Web — Garmin production enablement (web/backend audit + hardening) · ResumeBuilder AI (Web) — ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building)

Best next action: Resumely iOS: (1) D7 readout ~7 days after go-live (~2026-06-28) — pull 7-day activation funnel from PostHog dashboard 1720819. (2) Bump to 1.1 (6), archive, and submit to carry PR #70 ATS copy fix. (3) Regenerate App Store screenshots before next submission. (4) Monitor reviews + crash/error events

## Run Center

- Last refresh: 2026-06-22 16:46
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | LIVE on App Store since 2026-06-19 — post-launch iteration on v1.0.3 build 16. Garmin readiness HRV source attribution is implemented locally on PR #55 branch | PR #55 review plus real-device/TestFlight evidence that Garmin Connect HRV samples arrive in HealthKit with the expected Garmin source metadata. Separately, decide whether to flip VOICE_COACH_ENABLED now that the app is live | No | Fresh | High |
| Resumely iOS | Post-launch — D7 Gate A monitoring. App is live; no approval pending. Next build (1.1 (6)) pending to carry ATS copy fix | (1) D7 readout ~7 days after go-live (~2026-06-28) — pull 7-day activation funnel from PostHog dashboard 1720819. (2) Bump to 1.1 (6), archive, and submit to carry PR #70 ATS copy fix. (3) Regenerate App Store screenshots before next submission. (4) Monitor reviews + crash/error events | No | Fresh | High |
| RunSmart Web | Garmin production enablement (web/backend audit + hardening) | Founder reviews `docs/garmin-application/10-MARC-LUSSI-GATE-1-4-EMAIL-DRAFT.md` and zip, then sends from hello@runsmart.ai (email sending is explicitly founder-only, not automated). Separately: founder decision needed on whether to click "Apply for Production Key" in Garmin API Tools now (Active User/HTTP/Ping/Pull/Setup all pass; only GC_ACTIVITY_UPDATE + USER_DEREG coverage remain unfilled and can't be synthetically generated) | Yes | Fresh | High |
| ResumeBuilder AI (Web) | ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building) | Story 2 was investigated, not implemented — traced the d30a6841 optimization back to its pre-optimization source resume (`resumes.raw_text` for resume_id b797b20e) and confirmed it has ZERO quantified metrics anywhere in the original, founder-authored text (only "15+ years" in the summary). The AI optimizer correctly preserved this truthfully per its "never fabricate metrics" rule — `metrics_presence: 0` is accurate, not a defect. No fix implemented. Founder decision needed: ship a UX nudge prompting users with metric-free resumes to add real numbers (new feature, out of this session's scope), or accept the score as correctly reflecting genuinely metric-free input | Yes | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; optionally add GLOBAL-OUTPUT-CONTRACT.md (deferred from the prompt study); add no further loop cards unless current and non-duplicative | Yes | Fresh | High |

## Stranded Work

7 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] main has 1 unpushed commit(s)
- [RunSmart iOS] main is 1 commit(s) behind origin (pull needed)
- [RunSmart iOS] garmin/ios-v1.0.4-brand-completeness: 2 unpushed commit(s), last commit 2026-06-22
- [RunSmart Web] main is 1 commit(s) behind origin (pull needed)
- [RunSmart Web] 1 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] 2 uncommitted file(s) in the primary working tree
- [Agentic OS] 12 uncommitted file(s) in the primary working tree

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
