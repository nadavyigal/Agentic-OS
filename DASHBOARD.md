# Portfolio Dashboard

Last updated: 2026-06-24 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## ⚠️ Status Contradicts Reality

- [HARD] RunSmart is declared 'Garmin Gate-4 brand resubmission readiness — all code-side work complete and merged to `main`; blocked only on Apple App Review (external, async) before the Garmin reply can go out, per founder's sequencing rule (live build must not contradict submitted Garmin screenshots)' but PostHog shows 11 live users in 7d.
- [HARD] RunSmart App Store state is LIVE (undated) but declared state is 'Garmin Gate-4 brand resubmission readiness — all code-side work complete and merged to `main`; blocked only on Apple App Review (external, async) before the Garmin reply can go out, per founder's sequencing rule (live build must not contradict submitted Garmin screenshots)'.

- Proposed fix (confirm before write): Ground truth contradicts declared status. Proposed next step: confirm and update the relevant tasks/progress.md status lines. No files were auto-edited.

## Executive Summary

RunSmart iOS — Garmin Gate-4 brand resubmission readiness — all code-side work complete and merged to `main`; blocked only on Apple App Review (external, async) before the Garmin reply can go out, per founder's sequencing rule (live build must not contradict submitted Garmin screenshots): Once Apple approves and the build goes live, reply to Garmin's ticket (213145/213165) with the corrected Gate-4 evidence package. Separately, two non-blocking follow-ups were opened during today's device checklist and are tracked but not started: (a) `garmin_connections.scopes` is an empty array in production despite an active, healthy connection — Permissions UI cosmetically shows everything "Off"; (b) some `garmin_activities` rows carry `sport: "wheelchair_push_walk"` or `"unknown"` and are excluded from the running feed — unclear yet whether this is a genuine Garmin API classification or a mapping gap · Resumely iOS — Post-launch — D7 Gate A monitoring. App is live; no approval pending. Next build (1.1 (6)) pending to carry ATS copy fix: (1) D7 readout ~7 days after go-live (~2026-06-28) — pull 7-day activation funnel from PostHog dashboard 1720819. (2) Bump to 1.1 (6), archive, and submit to carry PR #70 ATS copy fix. (3) Regenerate App Store screenshots before next submission. (4) Monitor reviews + crash/error events · RunSmart Web — Garmin Gate-4 brand resubmission — web/backend side complete; blocked on iOS 1.0.4(17) Apple App Review before replying to Garmin again · ResumeBuilder AI (Web) — ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building)

Best next action: Resumely iOS: (1) D7 readout ~7 days after go-live (~2026-06-28) — pull 7-day activation funnel from PostHog dashboard 1720819. (2) Bump to 1.1 (6), archive, and submit to carry PR #70 ATS copy fix. (3) Regenerate App Store screenshots before next submission. (4) Monitor reviews + crash/error events

## Run Center

- Last refresh: 2026-06-24 13:28
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Garmin Gate-4 brand resubmission readiness — all code-side work complete and merged to `main`; blocked only on Apple App Review (external, async) before the Garmin reply can go out, per founder's sequencing rule (live build must not contradict submitted Garmin screenshots) | Once Apple approves and the build goes live, reply to Garmin's ticket (213145/213165) with the corrected Gate-4 evidence package. Separately, two non-blocking follow-ups were opened during today's device checklist and are tracked but not started: (a) `garmin_connections.scopes` is an empty array in production despite an active, healthy connection — Permissions UI cosmetically shows everything "Off"; (b) some `garmin_activities` rows carry `sport: "wheelchair_push_walk"` or `"unknown"` and are excluded from the running feed — unclear yet whether this is a genuine Garmin API classification or a mapping gap | Yes | Fresh | High |
| Resumely iOS | Post-launch — D7 Gate A monitoring. App is live; no approval pending. Next build (1.1 (6)) pending to carry ATS copy fix | (1) D7 readout ~7 days after go-live (~2026-06-28) — pull 7-day activation funnel from PostHog dashboard 1720819. (2) Bump to 1.1 (6), archive, and submit to carry PR #70 ATS copy fix. (3) Regenerate App Store screenshots before next submission. (4) Monitor reviews + crash/error events | Yes | Fresh | High |
| RunSmart Web | Garmin Gate-4 brand resubmission — web/backend side complete; blocked on iOS 1.0.4(17) Apple App Review before replying to Garmin again | Once iOS 1.0.4(17) is live on the App Store, reply to Garmin's ticket (213145/213165) with the corrected Gate-4 evidence (brand fixes to shots 01/04/05, new shot 06 Garmin Wellness, now with a real in-app entry point per iOS WP-15/PR #61). Separately tracked, not blocking: Gate 2's `GC_ACTIVITY_UPDATE`/`USER_DEREG` Partner Verification coverage gap remains open (needs a real webhook receipt for each, then a portal re-run); `garmin_connections.scopes` is an empty array in production despite healthy active connections (cosmetic Permissions-UI bug); some `garmin_activities` rows are tagged `sport: "wheelchair_push_walk"`/`"unknown"` and excluded from the running feed (unclear yet if genuine Garmin classification or a mapping gap — investigation prompt not yet written for this one) | Yes | Fresh | Medium |
| ResumeBuilder AI (Web) | ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building) | Story 2 was investigated, not implemented — traced the d30a6841 optimization back to its pre-optimization source resume (`resumes.raw_text` for resume_id b797b20e) and confirmed it has ZERO quantified metrics anywhere in the original, founder-authored text (only "15+ years" in the summary). The AI optimizer correctly preserved this truthfully per its "never fabricate metrics" rule — `metrics_presence: 0` is accurate, not a defect. No fix implemented. Founder decision needed: ship a UX nudge prompting users with metric-free resumes to add real numbers (new feature, out of this session's scope), or accept the score as correctly reflecting genuinely metric-free input | Yes | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; optionally add GLOBAL-OUTPUT-CONTRACT.md (deferred from the prompt study); add no further loop cards unless current and non-duplicative | Yes | Fresh | High |

## Stranded Work

11 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] preserve/apple-garmin-sync-docs: unmerged commits, never pushed, last commit 2026-06-21
- [RunSmart iOS] 3 uncommitted file(s) in the primary working tree
- [Resumely iOS] feat/localization-updates: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] pr-72-review: unmerged commits, never pushed, last commit 2026-06-22
- [Resumely iOS] 1 uncommitted file(s) in the primary working tree
- [RunSmart Web] 15 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] main is 1 commit(s) behind origin (pull needed)
- [ResumeBuilder AI (Web)] fix/pdf-parse-xref-error: unmerged commits, never pushed, last commit 2026-06-03
- [ResumeBuilder AI (Web)] pr-83-review: unmerged commits, never pushed, last commit 2026-06-22
- [ResumeBuilder AI (Web)] 4 uncommitted file(s) in the primary working tree
- [Agentic OS] 4 uncommitted file(s) in the primary working tree

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

- Resumely iOS: validated 2026-06-21, latest commit is newer.
- ResumeBuilder AI (Web): validated 2026-06-22, latest commit is newer.
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
