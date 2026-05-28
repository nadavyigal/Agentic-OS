# Sprint Prompt: ResumeBuilder iOS — Get App Store Ready
**Date:** 2026-05-28
**Goal:** Verify the core loop works on a real device, close all open iOS issues, implement PostHog analytics, generate screenshots, complete App Store metadata, and archive build 1 so it is ready to submit tomorrow.
**Repo:** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
**Backend:** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`

---

## Session Start — Read These First (in order)

1. `tasks/lessons.md` — never repeat a logged failure
2. `tasks/MEMORY.md` — last 2 entries
3. `tasks/todo.md` — open items
4. `tasks/session-log.md` — last 2 entries
5. `tasks/progress.md` — current status, blockers, risks
6. `/Users/nadavyigal/Documents/Projects /Agentic OS/PROJECT-BRIDGES/exec-reviews/2026-05-26-resumebuilder-ios.md` — distribution reality check
7. `docs/qa/app-store-readiness-checklist.md` — submission checklist to work toward
8. `docs/qa/testflight-checklist.md` — TestFlight gate (must pass before App Store checklist)

State in one sentence what the north-star metric is and whether the core loop has been verified on a real device.

---

## Phase 1 — Real-Device Smoke Test (HARD GATE)

This phase must pass before any code is written. Do not skip it.

On a physical iPhone with a live Supabase account:

1. Clean install (delete and reinstall, or use a fresh device).
2. Sign in with Apple.
3. Upload a text-based PDF (exported from Pages or Word — not scanned, not image-only).
4. Tap optimize with a real job description pasted.
5. Confirm the Optimized tab preview renders (local HTML appears, then backend design HTML loads).
6. Switch between Traditional / Modern / Creative / Corporate design categories.
7. Apply one design template.
8. Run Expert workflow with evidence text entered.
9. Apply Expert changes and confirm ATS score refresh appears.
10. Trigger export / download PDF.

For each step: record pass / fail / partial. If any step fails, diagnose root cause before proceeding.

**Blocker rule:** If optimize or preview fails on device with a known-good text PDF, fix the root cause before moving to Phase 2. Do not proceed to analytics or screenshots with a broken core loop.

If smoke passes: record it in `tasks/session-log.md` as the first confirmed device smoke.

---

## Phase 2 — Close Open Issues

Work through every unchecked `- [ ]` item in `tasks/todo.md`:

**Priority 1 — Required before archive:**
- Create the bundled PR for end-to-end live stabilization (PRs #24–30 + hotfix). Use `/ship` skill or create manually via `gh pr create`.
- Verify `ApplicationExpertReportItem.id` maps correctly to a real backend run ID (from the risk log in `tasks/progress.md`).

**Priority 2 — Backend (required before Resume Library re-enable):**
- Implement `/api/v1/resumes` list/save/rename/delete/download endpoints in the backend repo.
- Once implemented, set `RuntimeFeatures.isResumeLibraryEnabled = true` in iOS and re-run tests.
- If backend work takes more than 90 minutes, defer and keep `isResumeLibraryEnabled = false` for the initial App Store submission. Document the deferral in `tasks/todo.md`.

**Priority 3 — Nice to have before archive:**
- Fix `/api/v1/styles/history` returning 500 or document it as "not available in v1.0" in the backend.

After each fix: run `xcodebuild test` and confirm tests still pass (minimum: existing count, currently 33).

---

## Phase 3 — PostHog Analytics

PostHog is not yet integrated in ResumeBuilder iOS. Implement it now.

**Architecture:**
- Add PostHog iOS SDK via Swift Package Manager: `https://github.com/PostHog/posthog-ios`
- Create `Services/Analytics/AnalyticsService.swift`: a `protocol AnalyticsTracking` with a live `PostHogAnalyticsService` and a `NullAnalyticsService` (for tests/previews).
- Create `Services/Analytics/AnalyticsEvents.swift`: typed static helpers for all events. Call sites never import PostHog directly — they call `Analytics.track*(...)`.
- Init PostHog in `AppDelegate` or `ResumeBuilderApp.swift` using the project token from the PostHog dashboard (add as `POSTHOG_API_KEY` in Info.plist — do not hardcode).

**Events to instrument (minimum set for v1.0):**

| Event | Where |
|---|---|
| `app_launched` | App init |
| `sign_in_completed` | After Sign in with Apple succeeds |
| `sign_out` | Sign out action |
| `upload_started` | When user picks a PDF |
| `upload_completed` | PDF preflight passed, sent to backend |
| `upload_failed` | Preflight rejection or backend 422 |
| `optimize_started` | Optimize button tapped with job description |
| `optimize_completed` | Backend returns optimization ID |
| `optimize_failed` | Backend error or timeout |
| `preview_viewed` | Optimized tab preview renders |
| `design_category_switched` | User taps a design category |
| `design_applied` | Apply Design succeeds |
| `expert_run_started` | Expert workflow triggered |
| `expert_applied` | Expert Apply succeeds |
| `paywall_shown` | PaywallView appears |
| `purchase_completed` | StoreKit purchase succeeds |
| `purchase_failed` | StoreKit purchase error |
| `export_triggered` | Export / download PDF tapped |
| `export_completed` | PDF download finishes |

**Tests:** Add `AnalyticsServiceTests.swift` with smoke tests verifying the `NullAnalyticsService` swallows calls without crashing and that each event function is callable.

After implementation:
- Build must pass: `xcodebuild build ... CODE_SIGNING_ALLOWED=NO`
- Tests must pass: all previous tests still passing + new analytics tests
- Confirm in PostHog dashboard (or via `NullAnalyticsService` in tests) that events are structured correctly.

---

## Phase 4 — App Store Screenshots

Generate screenshot sets for both required display classes.

**Required sets:**
- iPhone 6.7-inch (iPhone 16 Pro Max or 15 Plus): minimum 3, target 5 screens
- iPhone 6.5-inch (iPhone 14 Plus or 13 Pro Max): minimum 3, target 5 screens

**Screens to capture (in order):**
1. Tailor tab with a resume uploaded and job description pasted (pre-optimize state)
2. Optimized tab showing the preview with a clean resume rendered
3. Design tab showing the template gallery with one selected
4. Expert tab or optimized resume with ATS score visible
5. Me / Profile tab with credits visible

**Method:** Use Xcode Simulator screenshot tool or Fastlane `snapshot` if configured. Use a clean test account with realistic data (not placeholder/mock content). Screenshots must show real app UI — no lorem ipsum, no "Test User", no debug overlays.

Save screenshots to `fastlane/screenshots/en-US/` following the naming convention from `docs/qa/app-store-readiness-checklist.md`.

Verify dimensions with `sips -g pixelWidth -g pixelHeight <file>`.

---

## Phase 5 — App Store Metadata

Work through `docs/qa/app-store-readiness-checklist.md` — App Store Connect Metadata section:

- **App name:** "Resumely" (confirm this is the final name — if not, flag before setting)
- **Subtitle (30 chars max):** "AI Resume Optimizer" or equivalent — clear value prop, no trademark issues
- **Description (4000 chars):** Cover: ATS score check, AI-powered optimization for specific jobs, professional design templates, Expert review mode, PDF export. No placeholder text. No claims that cannot be demonstrated in review.
- **Keywords (100 chars):** `resume,ATS,job,AI,optimizer,career,CV,interview,hiring,template`
- **Category:** Productivity (primary), Business (secondary)
- **Privacy policy URL:** must be live — confirm the URL resolves before submitting
- **Support URL:** must be live
- **Age rating:** 4+

Write or update `fastlane/metadata/en-US/` files (name.txt, subtitle.txt, description.txt, keywords.txt) so they are ready for `fastlane deliver` or manual paste into App Store Connect.

---

## Phase 6 — IAP Products Verification

In App Store Connect, verify:
- [ ] All credit pack products are configured with the exact product IDs that `StoreKitManager.swift` expects
- [ ] Products are in "Ready to Submit" state
- [ ] Pricing is correct
- [ ] No sandbox-only product IDs appear in the production scheme

If any product is missing or mismatched, add/fix it now — a mismatch causes rejection.

---

## Phase 7 — App Store Readiness Checklist Pass

Run through all items in `docs/qa/app-store-readiness-checklist.md` and `docs/qa/testflight-checklist.md`. Mark each item pass/fail. Any unchecked item that cannot be resolved today must be explicitly recorded as a known gap with a plan to resolve before submission tomorrow.

**Minimum passing criteria for "ready to archive":**
- Real-device smoke passed (Phase 1)
- Core open issues closed or explicitly deferred (Phase 2)
- PostHog integrated and building (Phase 3)
- Screenshots exist in correct dimensions (Phase 4)
- All metadata written (Phase 5)
- IAP products verified (Phase 6)
- No placeholder UI visible in screenshots
- All loading, empty, and error states implemented (no blank white screens)
- Crash-free on clean install confirmed (Phase 1 covers this)

---

## Phase 8 — Archive + Upload (Not Submit)

Once all phases above pass:

1. Bump build number if needed (confirm current is 1, target is 1 for initial submission).
2. Archive in Xcode: **Product → Archive** with `Any iOS Device (arm64)`.
3. Export for App Store Connect distribution.
4. Upload via Xcode Organizer or Transporter.
5. Confirm upload completes. Do NOT click Submit for Review — submission is tomorrow.

Record the upload timestamp and build number in `tasks/session-log.md`.

---

## Session Close

Update all of the following before ending the session:
- `tasks/todo.md` — mark completed items, add any new blockers found
- `tasks/session-log.md` — full session entry
- `tasks/progress.md` — update status, last validation, current branch, blockers

---

## Scope Guards

- Do not add new product features in this session — only close open issues and complete the readiness work above.
- Do not re-introduce mock services or mock data paths.
- Do not commit secrets, API keys, or Apple credentials to the repo.
- If the real-device smoke (Phase 1) fails and cannot be fixed in under 60 minutes, stop and surface the blocker — do not proceed to analytics or screenshots.
- Scope gate: if a fix expands to touch more than 3 unexpected files, stop and surface before continuing.

---

## Done Definition

- [ ] Real-device smoke passed and recorded in session-log
- [ ] All critical open issues closed or explicitly deferred
- [ ] Bundled stabilization PR created
- [ ] PostHog integrated, building, and tests passing
- [ ] App Store screenshots generated and dimension-verified
- [ ] All metadata written to `fastlane/metadata/en-US/`
- [ ] IAP products verified
- [ ] App Store readiness checklist completed (gaps documented)
- [ ] Build archived and uploaded to App Store Connect
- [ ] `tasks/session-log.md`, `tasks/todo.md`, `tasks/progress.md` updated
