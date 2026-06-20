# Work Packet WP-9

- Status: open
- Created: 2026-06-20
- Source: RunSmart ASO audit rs-aso-003 (`distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-aso-003-listing-audit/aso-review.md`) + onboarding review rs-onboarding-001
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: runsmart-growth
- Success signal: subtitle + keyword field updated in App Store Connect; first-review prompt live in a build; screenshot caption headlines designed and uploaded. First non-zero App Store rating recorded.
- Escalation: none

# Work Packet

## Owner Role
Growth / iOS (local)

## Project
RunSmart iOS
- App: RunSmart: AI Run Coaching — id6768297840, `com.runsmart.lite`
- Web/metadata repo: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
- Live listing: https://apps.apple.com/il/app/runsmart-ai-run-coaching/id6768297840

## Goal
Address the three highest-value findings from the ASO audit: lift store conversion and break the zero-ratings ceiling that is currently capping installs (and therefore the D7 gate).

## Context
v1.0.3 is live but has **zero App Store ratings** (no social proof), screenshots are **raw UI with no caption headlines**, and the subtitle **duplicates title words** ("Run", "coaching") that are already indexed. The live title (`RunSmart: AI Run Coaching`) is good — do not change it. Repo fastlane metadata is stale vs the live listing; App Store Connect is the source of truth.

## Tasks (each independent; ship in any order)

### 1. First-review prompt (app change — biggest lever)
- Add `SKStoreReviewController.requestReview()` after a genuine positive moment: first `run_completed`, or completion of the first plan week. Gate to max 3/365 days (Apple limit) and never on a failure/error screen.
- Suggested home: post-run summary (`Features/Run/PostRunSummaryView.swift`) or an aha-moment hook.
- Tie-in: this is also onboarding finding F3.

### 2. Subtitle + keyword field rewrite (App Store Connect metadata — <1 hr, no build)
- Subtitle: from `Run coaching that fits today` → `Adaptive plans, daily readiness` (30/30). Stops re-indexing words already in the title; adds `adaptive`, `plans`, `readiness`.
- Keyword field (≤100 bytes, comma-no-space): avoid any word in the title/subtitle (`runsmart, ai, run, coaching, adaptive, plans, readiness`). Suggested: `marathon,beginner,5k,10k,interval,training,garmin,strava,recovery,gps,couch to 5k` (trim to fit).
- Update the live listing in ASC, then re-sync `fastlane/metadata/en-US/{subtitle,keywords}.txt` so the repo matches reality.

### 3. Screenshot caption headlines (design + asset upload)
- The 5 frames (today → plan → run → report → profile) need a one-line benefit headline overlaid on each. First 3 are what 90% of searchers see; captions are Apple-indexed since 2025.
- Draft copy (from the audit):
  - Today: "Know what to run, every morning"
  - Plan: "A plan that adapts when life does"
  - Run: "GPS tracking + a plain-language debrief"
  - Report: "See your effort, not just your pace"
  - Profile: "Garmin & Apple Health, made useful"
- Produce both device sizes (iPhone_17_Pro_Max + iPhone_17e), upload to ASC. Hebrew locale gets its own pass later.

## Constraints
- Do NOT change the live title `RunSmart: AI Run Coaching` — it already does the keyword work and differentiates from the same-named incumbent (RunSmart Online LLC).
- Metadata edits (task 2) need no new build; task 1 needs a build + resubmission; task 3 needs only asset upload.
- Do not invent rating/conversion results; attach before/after evidence per GLOBAL-QA-RULES.md.
- Do not touch unrelated files. Keyword/subtitle changes go through App Store Connect, then mirror to fastlane — never the reverse (the repo is stale).

## Validation
- Task 1: review prompt appears on a physical device after a completed run; capped correctly; never on an error state. First non-zero rating appears in ASC.
- Task 2: live ASC subtitle = `Adaptive plans, daily readiness`; keyword field has no word duplicated from title/subtitle; fastlane files re-synced to match.
- Task 3: 5 captioned screenshots per device live on the listing; captions match the approved copy.
- Re-pull the rs-aso-003 score after changes; Visual Assets and Ratings dimensions should rise.
