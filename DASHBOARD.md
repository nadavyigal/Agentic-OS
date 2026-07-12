# Portfolio Dashboard

Last updated: 2026-07-12 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — PHASE 2 — Release 1.0.8 (22) (WP-37/38/40 bundle): Confirm ASC upload processing; TestFlight smoke; re-run WP-42 on clean 1.0.8 cohort after users onboard · Resumely iOS — Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists: Re-run PostHog picker→file-selected funnel on **2026-07-25** (or minimum check **2026-07-18**) for clean `marketing_version=1.4.1` cohort; see deferred-read entry above for query definition · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

Best next action: Resumely iOS: Re-run PostHog picker→file-selected funnel on **2026-07-25** (or minimum check **2026-07-18**) for clean `marketing_version=1.4.1` cohort; see deferred-read entry above for query definition

## Run Center

- Last refresh: 2026-07-12 14:12
- Localhost: `http://127.0.0.1:8787/portfolio-hq.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | PHASE 2 — Release 1.0.8 (22) (WP-37/38/40 bundle) | Confirm ASC upload processing; TestFlight smoke; re-run WP-42 on clean 1.0.8 cohort after users onboard | No | Fresh | Medium |
| Resumely iOS | Post-launch — 1.4.1 (11) live; picker→file-selected funnel read **deferred** until post-live cohort exists | Re-run PostHog picker→file-selected funnel on **2026-07-25** (or minimum check **2026-07-18**) for clean `marketing_version=1.4.1` cohort; see deferred-read entry above for query definition | Yes | Fresh | High |
| RunSmart Web | Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes | **Still paused.** Restoring actual sync for the 9 reauth_required users needs either a working production/commercial credential set (WP-26 Steps 3-4) or pointing real users at the Evaluation-tier Internal Test app (the same Terms violation that got the old app deactivated) — there is no maintenance-mode-compatible fix available. This is a fact worth surfacing at the day-30 revisit (~2026-08-01), not a reason to resume now. See Agentic OS WP-26/27/28 for the paused relaunch scope | Yes | Fresh | High |
| ResumeBuilder AI (Web) | WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next | WP-29 S5 — design and implement anonymous session carryover after signup so the first dashboard is not empty | Yes | Fresh | High |
| Agentic OS | Advanced OS patterns lean pilot | Merge PR #25, then run ./agentic-os refresh once to confirm the full pipeline regenerates the new page end to end; run the second COO operating review to close the pilot's validation gate | Yes | Fresh | High |

## Stranded Work

18 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] codex/wp40-release-closeout: unmerged commits, never pushed, last commit 2026-07-12
- [RunSmart iOS] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart iOS] preserve/apple-garmin-sync-docs: unmerged commits, never pushed, last commit 2026-06-21
- [RunSmart iOS] worktree on detached, 1 uncommitted file(s) at /private/tmp/rs-release-108-22/repo
- [Resumely iOS] feat/localization-updates: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] pr-72-review: unmerged commits, never pushed, last commit 2026-06-22
- [Resumely iOS] 1 uncommitted file(s) in the primary working tree
- [RunSmart Web] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart Web] pr-108-review: unmerged commits, never pushed, last commit 2026-06-30
- [RunSmart Web] 8 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] fix/posthog-expert-event-dedupe: 1 unpushed commit(s), last commit 2026-07-09
- [ResumeBuilder AI (Web)] fix/ats-keyword-phrase-quality: unmerged commits, remote branch deleted, last commit 2026-06-22
- [ResumeBuilder AI (Web)] fix/pdf-parse-xref-error: unmerged commits, never pushed, last commit 2026-06-03
- [ResumeBuilder AI (Web)] pr-83-review: unmerged commits, never pushed, last commit 2026-06-22
- [ResumeBuilder AI (Web)] worktree on codex/fix-web-export-observability at /Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai--export-observability
- [ResumeBuilder AI (Web)] 2 uncommitted file(s) in the primary working tree
- [Agentic OS] main has 10 unpushed commit(s)
- [Agentic OS] 11 uncommitted file(s) in the primary working tree

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

- RunSmart Web: validated 2026-07-03, latest commit is newer.
- ResumeBuilder AI (Web): validated 2026-07-03, latest commit is newer.
- Agentic OS: validated 2026-07-10, latest commit is newer.

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
