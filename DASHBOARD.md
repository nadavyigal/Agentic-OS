# Portfolio Dashboard

Last updated: 2026-07-08 IDT

Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, task memory/todo/session files, and existing dashboard status. No external dashboards queried.

## Executive Summary

RunSmart iOS — PHASE 2 — Activation diagnostics + Garmin maintenance (EXD-015): Re-run PostHog funnel on **2026-07-08+** for build-21-only users (`filterTestAccounts=true`). Then WP-27 Gate-4 screenshots if Garmin path resumes · Resumely iOS — Post-launch — activation measurement is hardened and the two largest early upload frictions have focused local fixes awaiting review: Wait for a post-fix cohort read of `resume_upload_cta_seen` → `resume_upload_cta_tapped` → `resume_file_picker_opened` → `resume_file_selected`; Story 5 Expert Mode visibility is optional/lower priority · RunSmart Web — Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes · ResumeBuilder AI (Web) — WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next

Best next action: Resumely iOS: Wait for a post-fix cohort read of `resume_upload_cta_seen` → `resume_upload_cta_tapped` → `resume_file_picker_opened` → `resume_file_selected`; Story 5 Expert Mode visibility is optional/lower priority

## Run Center

- Last refresh: 2026-07-08 11:46
- Localhost: `http://127.0.0.1:8787/index.html`
- Safe mode: No App Store, billing, production, email, or external service action is triggered.

## Project Health

| Project | State | Next Action | Dirty | Freshness | Confidence |
| --- | --- | --- | --- | --- | --- |
| RunSmart iOS | PHASE 2 — Activation diagnostics + Garmin maintenance (EXD-015) | Re-run PostHog funnel on **2026-07-08+** for build-21-only users (`filterTestAccounts=true`). Then WP-27 Gate-4 screenshots if Garmin path resumes | Yes | Fresh | High |
| Resumely iOS | Post-launch — activation measurement is hardened and the two largest early upload frictions have focused local fixes awaiting review | Wait for a post-fix cohort read of `resume_upload_cta_seen` → `resume_upload_cta_tapped` → `resume_file_picker_opened` → `resume_file_selected`; Story 5 Expert Mode visibility is optional/lower priority | No | Fresh | High |
| RunSmart Web | Garmin track is maintenance-only per the 2026-07-02 priority-reset decision (Resumely primary). No relaunch work in progress; only breakage fixes | **Still paused.** Restoring actual sync for the 9 reauth_required users needs either a working production/commercial credential set (WP-26 Steps 3-4) or pointing real users at the Evaluation-tier Internal Test app (the same Terms violation that got the old app deactivated) — there is no maintenance-mode-compatible fix available. This is a fact worth surfacing at the day-30 revisit (~2026-08-01), not a reason to resume now. See Agentic OS WP-26/27/28 for the paused relaunch scope | Yes | Fresh | High |
| ResumeBuilder AI (Web) | WP-29 Resumely web funnel P0 fixes — S1-S4 completed; S5 anonymous-session carryover is next | WP-29 S5 — design and implement anonymous session carryover after signup so the first dashboard is not empty | Yes | Needs Review | High |
| Agentic OS | Advanced OS patterns lean pilot | Use the Resumely submission loop in two COO reviews; optionally add GLOBAL-OUTPUT-CONTRACT.md (deferred from the prompt study); add no further loop cards unless current and non-duplicative | No | Fresh | High |

## Stranded Work

24 item(s) at risk of being lost (full list with actions in PROJECT-STATUS.md):

- [RunSmart iOS] claude/ios-docs-sweep-2026-06-19: unmerged commits, remote branch deleted, last commit 2026-06-19
- [RunSmart iOS] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart iOS] preserve/apple-garmin-sync-docs: unmerged commits, never pushed, last commit 2026-06-21
- [RunSmart iOS] worktree on detached, 1 uncommitted file(s) at /private/tmp/runsmart-wp15-release-1783271110
- [RunSmart iOS] 35 uncommitted file(s) in the primary working tree
- [Resumely iOS] codex/fitcheck-service: unmerged commits, remote branch deleted, last commit 2026-06-23
- [Resumely iOS] feat/localization-updates: unmerged commits, never pushed, last commit 2026-06-16
- [Resumely iOS] pr-72-review: unmerged commits, never pushed, last commit 2026-06-22
- [RunSmart Web] garmin/brand-compliance-2026-06-22: unmerged commits, remote branch deleted, last commit 2026-06-22
- [RunSmart Web] pr-108-review: unmerged commits, never pushed, last commit 2026-06-30
- [RunSmart Web] 6 uncommitted file(s) in the primary working tree
- [ResumeBuilder AI (Web)] codex/wp29-s1-optimization-review-crash: 1 unpushed commit(s), last commit 2026-07-03
- [ResumeBuilder AI (Web)] codex/fit-first-triage-story-0: unmerged commits, remote branch deleted, last commit 2026-06-23
- [ResumeBuilder AI (Web)] codex/resumebuilder-posthog-llm-observability: unmerged commits, remote branch deleted, last commit 2026-06-30
- [ResumeBuilder AI (Web)] codex/wp29-s2-en-funnel-messages: unmerged commits, never pushed, last commit 2026-07-03
- [ResumeBuilder AI (Web)] codex/wp29-s3-word-count-errors: unmerged commits, never pushed, last commit 2026-07-03
- [ResumeBuilder AI (Web)] codex/wp29-s4-disable-premium-cta: unmerged commits, never pushed, last commit 2026-07-03
- [ResumeBuilder AI (Web)] codex/wp29-s5-anon-session-handoff: unmerged commits, never pushed, last commit 2026-07-03
- [ResumeBuilder AI (Web)] codex/wp29-s6-cleanup-batch: unmerged commits, never pushed, last commit 2026-07-03
- [ResumeBuilder AI (Web)] fix/ats-keyword-phrase-quality: unmerged commits, remote branch deleted, last commit 2026-06-22
- [ResumeBuilder AI (Web)] fix/pdf-parse-xref-error: unmerged commits, never pushed, last commit 2026-06-03
- [ResumeBuilder AI (Web)] pr-83-review: unmerged commits, never pushed, last commit 2026-06-22
- [ResumeBuilder AI (Web)] 2 uncommitted file(s) in the primary working tree
- [Agentic OS] main has 1 unpushed commit(s)

## Work Packet Hygiene

- ERROR [executive-os/COO-LATEST-REVIEW.md]: COO latest review references build 18, but current RunSmart status is build 21.

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

- RunSmart iOS: validated 2026-07-05, latest commit is newer.
- RunSmart Web: validated 2026-07-03, latest commit is newer.
- ResumeBuilder AI (Web): validated 2026-07-03, latest commit is newer.
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
