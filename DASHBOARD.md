# Portfolio Dashboard

Last updated: 2026-06-30 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — LIVE on App Store as marketing version `1.0.4`; `1.0.5 (18)` upload/submission/live confirmation remains founder-only. Garmin external reply remains gated until `1.0.5 (18)` is genuinely live and all 6 Gate-4 screenshots are recaptured against that live build: Founder uploads/submits `1.0.5 (18)` to App Store Connect, waits for approval, confirms `1.0.5 (18)` live from App Store/ASC, then recaptures all 6 Gate-4 screenshots and sends the Garmin reply with the new zip. The `plan_run_cta_tapped` cohort cannot be measured until build 18 ships · Resumely iOS — Post-launch — v1.2 (7) live; verifying production funnel events and planning next ASO/outreach iteration: (1) Verify production PostHog project 270848 receives upload-funnel and `fit_check_*` events now that 1.2 (7) is live. (2) Read results of the founder's zero-budget outreach wave. (3) Use the clean post-1.2 funnel read to decide whether ASO volume, lifecycle messaging, monetization, or backend/state follow-ups are next · RunSmart Web — `1.0.5 (18)` confirmed live on App Store (2026-06-30). Gate-4 Garmin reply is ALMOST READY — blocked only on screenshot recapture and re-zip against the live build · ResumeBuilder AI (Web) — ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building)

Best next action: Resumely iOS: (1) Verify production PostHog project 270848 receives upload-funnel and `fit_check_*` events now that 1.2 (7) is live. (2) Read results of the founder's zero-budget outreach wave. (3) Use the clean post-1.2 funnel read to decide whether ASO volume, lifecycle messaging, monetization, or backend/state follow-ups are next

## Run Center

- Last refresh: 2026-06-30 14:13
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | LIVE on App Store as marketing version `1.0.4`; `1.0.5 (18)` upload/submission/live confirmation remains founder-only. Garmin external reply remains gated until `1.0.5 (18)` is genuinely live and all 6 Gate-4 screenshots are recaptured against that live build | Founder uploads/submits `1.0.5 (18)` to App Store Connect, waits for approval, confirms `1.0.5 (18)` live from App Store/ASC, then recaptures all 6 Gate-4 screenshots and sends the Garmin reply with the new zip. The `plan_run_cta_tapped` cohort cannot be measured until build 18 ships | No | Fresh | High |
| Resumely iOS | Post-launch — v1.2 (7) live; verifying production funnel events and planning next ASO/outreach iteration | (1) Verify production PostHog project 270848 receives upload-funnel and `fit_check_*` events now that 1.2 (7) is live. (2) Read results of the founder's zero-budget outreach wave. (3) Use the clean post-1.2 funnel read to decide whether ASO volume, lifecycle messaging, monetization, or backend/state follow-ups are next | No | Fresh | High |
| RunSmart Web | `1.0.5 (18)` confirmed live on App Store (2026-06-30). Gate-4 Garmin reply is ALMOST READY — blocked only on screenshot recapture and re-zip against the live build | Screenshot recapture on live `1.0.5 (18)` device — 6 screens: 01-03 connection flow (verify Garmin wordmark logo shows), 04-06 activity/recovery/wellness (verify "Garmin Forerunner 265" or actual device name shows). Re-zip, fill `[SCREENSHOT_ZIP_FILENAME]` in draft, send | Yes | Fresh | Medium |
| ResumeBuilder AI (Web) | ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building) | Story 2 was investigated, not implemented — traced the d30a6841 optimization back to its pre-optimization source resume (`resumes.raw_text` for resume_id b797b20e) and confirmed it has ZERO quantified metrics anywhere in the original, founder-authored text (only "15+ years" in the summary). The AI optimizer correctly preserved this truthfully per its "never fabricate metrics" rule — `metrics_presence: 0` is accurate, not a defect. No fix implemented. Founder decision needed: ship a UX nudge prompting users with metric-free resumes to add real numbers (new feature, out of this session's scope), or accept the score as correctly reflecting genuinely metric-free input | Yes | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; optionally add GLOBAL-OUTPUT-CONTRACT.md (deferred from the prompt study); add no further loop cards unless current and non-duplicative | No | Fresh | High |

## Stranded Work

11 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] main has 1 unpushed commit(s)
- [RunSmart iOS] preserve/apple-garmin-sync-docs: unmerged commits, never pushed, last commit 2026-06-21
- [Resumely iOS] main has 1 unpushed commit(s)
- [Resumely iOS] codex/fitcheck-service: unmerged commits, remote branch deleted, last commit 2026-06-23
- [Resumely iOS] feat/localization-updates: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] pr-72-review: unmerged commits, never pushed, last commit 2026-06-22
- [RunSmart Web] 8 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] fix/pdf-parse-xref-error: unmerged commits, never pushed, last commit 2026-06-03
- [ResumeBuilder AI (Web)] pr-83-review: unmerged commits, never pushed, last commit 2026-06-22
- [ResumeBuilder AI (Web)] 1 uncommitted file(s) in the primary working tree
- [Agentic OS] main has 2 unpushed commit(s)

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

- Resumely iOS: validated 2026-06-26, latest commit is newer.
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
