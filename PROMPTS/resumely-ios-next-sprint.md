# Resumely iOS — Next Sprint Prompt

**Date generated:** 2026-06-02
**For:** New Claude Code session opened inside `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

Paste this entire prompt at the start of a new session in the Resumely iOS repo.

---

## Session Context

You are opening a new Claude Code session for **Resumely iOS** — the native SwiftUI iOS app for resume optimization.

Read these files before doing anything, in order:

1. `~/.claude/MEMORY.md` — global decisions. Never contradict a logged decision without flagging it.
2. `~/.claude/ERRORS.md` — global failed approaches.
3. `tasks/MEMORY.md` — project-specific decisions and session history.
4. `tasks/ERRORS.md` — project-specific failed approaches.
5. `tasks/lessons.md` — iOS build/API/SwiftUI lessons learned (critical: several Swift 6 and XCTest isolation bugs documented here).
6. `tasks/todo.md` — current checklist and completed story status.
7. `docs/specs/resumely-pre-submission-ux-ui-transformation.md` — if you need context on the UX transformation that just landed.

## Current State (as of 2026-06-02)

**What is done:**
- PR #36 UX/UI transformation: all 7 stories complete, merged. Guest-first home, export-first Optimized, locked Design/Expert for guests, UX polish.
- PostHog `AnalyticsService` integrated (PR #35 into #36): `app_launched` and `optimize_completed` events wired, PII guard, double-fire de-dup.
- Resume optimization waiting animation: inline scan loader in Home and Tailor.
- Live flow fixes: design apply no longer fails on secondary customize 404, PDF export has WKWebView retention/timeout/backend fallback.
- Build, tests, launch smoke: 55/55 passing on iPhone 17 simulator (2026-06-01). Build must use DerivedData at `/tmp/resumebuilder-derived` to avoid codesign extended-attribute failures.

**What is NOT done (gates for submission):**
1. `export_success` PostHog event — not wired or confirmed. This is the core conversion event.
2. Real-device smoke test with a **live authenticated account**: never run. Must cover optimize → design apply → PDF export → Expert cover letter.
3. Fastlane / ASC API key — **founder action required**. Cannot be delegated to agent. Screenshots and metadata cannot be uploaded without this.
4. App Store Connect submission — blocked on items above.

**Active blockers (human action required):**
- Set up Fastlane with ASC API key so `deliver` can upload screenshots and metadata.
- Once credentials exist: open App Store Connect, select processed build, confirm privacy questionnaire / age rating / category, submit.

**Backend not live:**
- `/api/v1/resumes` (Resume Library list/save/rename/delete) — mock service active. Do not build against it this sprint.
- `/api/v1/styles/history` — returns 500; workaround is to not call it.

## Sprint Objective

**Ship Resumely to the App Store.**

Three stories in priority order:

---

### Story 1 — Wire `export_success` PostHog event (agent task, ~2h)

**Why:** Export is the core conversion action. Zero visibility into it post-launch.

**Scope:**
- Find all code paths where PDF/share export completes successfully: `ResumeExportAction`, `HTMLPDFExporter`, the share sheet completion handler.
- Fire `AnalyticsService.shared.track(.exportSuccess)` (or equivalent enum case) on a confirmed success path only — not on cancel or error.
- Add `export_success` to the `AnalyticsEvent` enum in `Core/Analytics/AnalyticsService.swift`.
- Write a focused unit test that verifies the event fires exactly once on export completion.
- Build and run tests: must pass 55+/55 before story is done.
- Do not fire the event in preview/simulator paths where there is no real PDF.

**Definition of done:**
- `export_success` fires in the success path, not on cancel or error.
- No double-fire on the same export action.
- Focused test: 1 test, must pass.
- `xcodebuild build` and `xcodebuild test` green (use DerivedData at `/tmp/resumebuilder-derived`).

---

### Story 2 — Authenticated real-device smoke test checklist (agent-assisted, human-executed)

**Why:** Simulator smoke has passed. Real device with a live account has never been tested.

**What to prepare (agent task):**
- Write a smoke test checklist markdown file at `docs/qa/resumely-smoke-test-real-device.md`.
- Checklist must cover these flows in order, with an expected result for each:
  1. Cold launch as guest — verify Home loads, guest CTA visible.
  2. Sign in with a live account — verify Me tab shows correct name/email.
  3. Upload a text-based PDF resume — verify upload completes without error.
  4. Tap Optimize — verify scan animation appears, optimization completes, lands on Optimized tab.
  5. Apply a Design — verify design apply does not show error (secondary customize 404 is acceptable noise).
  6. Export PDF from Optimized — verify share sheet appears with a real PDF file (not placeholder), verify `export_success` fires in PostHog (check PostHog Live Events).
  7. Open Expert tab — create a Cover Letter for a linked application, verify asset appears under Me → Applications.
  8. Check PostHog Live Events for: `app_launched` (once), `optimize_completed` (once), `export_success` (once).

**Human executes the checklist** after agent writes it. Sign off "PASS" or note failures.

**Definition of done:**
- Checklist file written and committed.
- Human executes and signs off.

---

### Story 3 — App Store Connect submission (human-only, agent assists with checklist)

**Why:** This is the final gate.

**What agent prepares:**
- Write a submission checklist at `docs/qa/resumely-asc-submission-checklist.md` covering:
  - Fastlane / ASC API key setup steps (reference Fastlane docs; do not hardcode credentials).
  - Archive and upload build via Xcode Organizer or `xcodebuild archive`.
  - Upload screenshots from `dist/app-store-screenshots/rb-aso-002/`.
  - Fill in App Store Connect metadata: app name, subtitle, description, keywords, category (Productivity), age rating (4+), privacy policy URL.
  - Enter demo credentials (non-personal test account).
  - Confirm privacy questionnaire.
  - Submit for review.

**Human executes** the checklist.

**Definition of done:**
- Checklist file written and committed.
- Human confirms build submitted to App Store review.

---

## What to NOT Do This Sprint

- Do not start the Resume Library backend integration (`/api/v1/resumes`).
- Do not add Hebrew/RTL support.
- Do not expand PostHog beyond `export_success` — scope is locked.
- Do not start new feature work (subscription/paywall, new Expert workflows, etc.) until submission.
- Do not touch the ResumeBuilder Web repo from this session.
- Do not run migrations, push to production, or change App Store Connect without explicit confirmation.

## Build Commands

```bash
# Always use /tmp derivedData to avoid codesign failures
xcodebuild build \
  -project "ResumeBuilder IOS APP.xcodeproj" \
  -scheme "ResumeBuilder IOS APP" \
  -destination "platform=iOS Simulator,name=iPhone 17" \
  -derivedDataPath /tmp/resumebuilder-derived

xcodebuild test \
  -project "ResumeBuilder IOS APP.xcodeproj" \
  -scheme "ResumeBuilder IOS APP" \
  -destination "platform=iOS Simulator,name=iPhone 17" \
  -derivedDataPath /tmp/resumebuilder-derived
```

## State the Objective Before Starting

Before touching any file, write one sentence: what you are implementing, what the deliverable is, and what success looks like.

## End of Session

Before closing, update `tasks/session-log.md` and `tasks/todo.md`. If any new build or test pattern is discovered, add it to `tasks/lessons.md`.
