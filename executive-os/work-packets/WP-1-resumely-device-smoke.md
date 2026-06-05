# Work Packet WP-1 (Closed)

- Status: Closed - superseded by confirmed submission
- Created: 2026-06-02
- Closed: 2026-06-05
- Source: BUSINESS-GTM-PLAN-V0.md Section 10 (WP-1)
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: resumely-submission
- Success signal: Authenticated device smoke, analytics evidence, export check, and upload-path evidence are complete.
- Routed by: COO OS (first COO Operating Review run)
- Escalation: none (CEO / CFO / Analysis / Risk all No)
- Related decision: EXD-006 (Resumely ASC upload path)

## Closure Note

Resumely 1.0 build 1 was submitted to App Store review on 2026-06-05.
This pre-submission packet is retained as history and must not be copied or
executed. Any device-smoke or analytics validation that was not completed
before submission should be handled only through a new post-submission packet
if Apple feedback or launch verification makes it necessary.

---

# Work Packet

## Owner Role
Release Manager / QA (local iOS)

## Project
Resumely iOS (ResumeBuilder IOS APP)
Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## Goal
Confirm the submit build works end-to-end on a real authenticated device and that analytics fire, producing the evidence needed before the founder triggers the App Store Connect upload.

## Context
Resumely cleared analytics and UX/export gates on 2026-06-01, but the authenticated real-device smoke has not been run and PostHog live-event coverage is unverified in a production-style build. This is the current portfolio bottleneck: it is the one step that moves a second app toward review and unlocks the first readable funnel. RunSmart iOS is frozen in Apple review, so no founder action moves it this week.

## Read First
- AGENTS.md
- CLAUDE.md
- tasks/progress.md (canonical status source for this repo)
- tasks/todo.md
- tasks/session-log.md
- tasks/lessons.md
- Latest submit-package / smoke notes referenced in tasks/session-log.md

## Task
On a real, signed, authenticated device build:
1. Smoke the core path: optimize -> design -> expert -> preview/export.
2. Confirm PostHog Live Events receives app_launched, optimize_completed, and export_success from this build.
3. Confirm export output (PDF / share) renders correctly.
4. Confirm the ASC upload path (EXD-006): Fastlane API key present? If absent, the upload uses the Claude Chrome extension to fill the App Store Connect portal — founder will share a screenshot folder link when we reach that step.
Stop at "ready to upload" with evidence. Do NOT upload or submit in this packet.

## Constraints
- Do not touch unrelated files.
- Do not deploy, submit, bill, email, or change production services without explicit approval.
- Do not invent validation results.
- Do not add events beyond the wired set, and no new dependencies.
- Keep the task to one focused work session.

## Validation
- Device smoke screenshots for each step (optimize, design, expert, preview/export).
- PostHog screenshot showing the 3 events received from this build.
- Export output visual check.
- A clear statement of the ASC upload path (Fastlane key present? yes/no).

## Completion Gate
Before final response, update or report:
- tasks/todo.md
- tasks/progress.md, if present
- tasks/session-log.md
- tasks/lessons.md only if a reusable lesson was learned

## Final Output
- What changed
- Files changed
- Commands run
- Validation evidence
- Remaining risks
- Next recommended action
