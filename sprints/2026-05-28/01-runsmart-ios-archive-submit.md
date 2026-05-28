# Sprint Prompt: RunSmart iOS — Archive Build 6 + App Store Submit
**Date:** 2026-05-28
**Goal:** Finish all pending plan tasks, bump to build 6, archive, upload, and submit RunSmart to App Store review today.
**Repo:** `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

---

## Session Start — Read These First (in order)

1. `tasks/lessons.md` — never repeat a logged failure
2. `tasks/MEMORY.md` — last 2 entries for context
3. `tasks/todo.md` — current task state
4. `docs/qa/app-store-connect-closeout-2026-05-24.md` — archive preflight gate and portal values
5. `docs/qa/app-store-readiness-checklist.md` — submission checklist
6. `docs/qa/app-review-notes-2026-05-19.md` — reviewer notes to paste into App Store Connect
7. `docs/superpowers/plans/2026-05-27-flex-week-deploy-analytics-intervention.md` — check every checkbox; complete any unchecked tasks before archiving

State the current build number and confirm it will be bumped to 6 before archiving.

---

## Phase 1 — Complete Pending Plan Tasks

Read `docs/superpowers/plans/2026-05-27-flex-week-deploy-analytics-intervention.md` and execute every unchecked `- [ ]` step in order. This plan covers:
- Deploy `flex_week` Supabase Edge Function to production via `scripts/deploy-coach-message.sh`
- PostHog init in `RunSmartLiteAppShell.swift` from Info.plist keys
- `RunSmartAnalytics.swift` — all PostHog capture calls
- `FlexWeekAdjustmentHistory.swift` — UserDefaults persistence
- `GentleCoachInterventionCard.swift` — Story 9 card
- Analytics event call sites wired in FlexWeekFlowView, FlexWeekEntryView, FlexWeekReasonPicker
- Unit tests in `FlexWeekAnalyticsTests.swift`

After completing the plan:
- Run `xcodebuild -project "IOS RunSmart app.xcodeproj" -scheme "IOS RunSmart app" -destination "platform=iOS Simulator,name=iPhone 17 Pro" CODE_SIGNING_ALLOWED=NO build` and confirm it succeeds.
- Run focused readiness tests: `xcodebuild ... -only-testing:"IOS RunSmart appTests/RunSmartReadinessTests" test` and confirm pass.

Do NOT proceed to Phase 2 if either build or tests fail.

---

## Phase 2 — Apply Approved ASO Description

The approved App Store description draft is at:
`/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/projects/runsmart/scaffold/drafts/2026-05-27-rs-aso-001/description.txt`

Copy its contents into `fastlane/metadata/en-US/description.txt`, replacing whatever is currently there.

Confirm the file is saved and the description contains no placeholder text, medical claims, or overpromised AI guarantees. Cross-check against `docs/qa/app-store-connect-closeout-2026-05-24.md` compliance notes.

---

## Phase 3 — Archive Preflight Gate

Run every check in the preflight gate from `docs/qa/app-store-connect-closeout-2026-05-24.md`:

1. `git status --short` — review; no unrelated dirty files in the app target
2. Confirm no untracked Swift files: `git ls-files --others --exclude-standard "IOS RunSmart app/**/*.swift"`
3. Confirm screenshots exist and pass dimension checks:
   - `fastlane/screenshots/en-US/iPhone_17_Pro_Max_01_today.png` through `_05_profile.png` — must be 1320x2868
   - `fastlane/screenshots/en-US/iPhone_17e_01_today.png` through `_05_profile.png` — must be 1170x2532
   - Use `sips -g pixelWidth -g pixelHeight <file>` to verify each.
4. Confirm `PrivacyInfo.xcprivacy` is present and covers UserID, Health, Fitness, PreciseLocation.
5. Confirm bundle id `com.runsmart.lite`, display name `RunSmart`, version `1.0` in the built app.

Do NOT archive if any preflight check fails.

---

## Phase 4 — Bump Build Number to 6

In Xcode (or via `agvtool`), set CURRENT_PROJECT_VERSION and MARKETING_VERSION to confirm version stays `1.0` and build number becomes `6`.

Verify with: `agvtool what-version` and `agvtool what-marketing-version`.

Commit the build number bump:
```
git add "IOS RunSmart app.xcodeproj/project.pbxproj"
git commit -m "chore: bump build number to 6 for App Store submission"
```

---

## Phase 5 — Archive + Export + Upload

1. In Xcode: **Product → Archive** with the `IOS RunSmart app` scheme and a connected device or `Any iOS Device (arm64)` destination.
2. In Organizer: **Distribute App → App Store Connect → Upload**.
3. Select: App Thinning = None, Rebuild from Bitcode = off (unless required), Include symbols = yes.
4. Confirm upload completes without error. Note the upload timestamp.

If Xcode Organizer upload fails, use `xcrun altool` or Transporter as fallback.

---

## Phase 6 — App Store Connect Portal Checklist

Open App Store Connect → RunSmart → the newly uploaded build.

Work through every item in `docs/qa/app-store-connect-closeout-2026-05-24.md` Post-Upload Portal Checklist:

- [ ] Confirm build finishes processing (may take 5–30 min after upload).
- [ ] Select build 6 for the submission.
- [ ] Upload screenshot sets: 6.9-inch (5 frames) and 6.1-inch (5 frames) from `fastlane/screenshots/en-US/`.
- [ ] Set category: Health & Fitness.
- [ ] Confirm age rating resolves to 4+.
- [ ] Paste reviewer notes from `docs/qa/app-review-notes-2026-05-19.md` into the Reviewer Information field.
- [ ] Enter demo credentials directly in App Store Connect (do not commit to repo).
- [ ] Confirm privacy questionnaire matches `docs/qa/app-store-connect-closeout-2026-05-24.md` values.
- [ ] Confirm support URL: `https://www.runsmart-ai.com/support`
- [ ] Confirm privacy URL: `https://www.runsmart-ai.com/privacy`
- [ ] Confirm marketing URL: `https://www.runsmart-ai.com`
- [ ] Verify no metadata claims medical diagnosis, live in-run AI coaching, guaranteed plan changes, or unsupported Garmin/HealthKit behavior.

---

## Phase 7 — Submit for Review

Click **Submit for Review** in App Store Connect.

Record in `tasks/todo.md`:
- Submission timestamp
- Build number submitted
- Any portal-only items still pending (demo credentials entered, confirmation of screenshots uploaded)

Update `tasks/session-log.md` with a session entry covering what was done, what passed, and what the submission status is.

---

## Scope Guards

- Do not touch any product feature code that is not part of the 2026-05-27 plan.
- Do not change production auth, Supabase, HealthKit, Garmin, or location behavior.
- Do not store demo credentials, Apple credentials, or private device identifiers in any repo file.
- If build or tests fail in Phase 1, stop and surface the error — do not skip to archiving.
- If any preflight gate item fails in Phase 3, stop and surface it — do not archive.

---

## Done Definition

- [ ] All unchecked tasks in `2026-05-27-flex-week-deploy-analytics-intervention.md` are complete
- [ ] Approved description is in `fastlane/metadata/en-US/description.txt`
- [ ] Build compiles and readiness tests pass
- [ ] All preflight gate checks pass
- [ ] Build 6 is archived and uploaded to App Store Connect
- [ ] Portal checklist complete
- [ ] "Submit for Review" clicked
- [ ] `tasks/session-log.md` and `tasks/todo.md` updated with submission status
