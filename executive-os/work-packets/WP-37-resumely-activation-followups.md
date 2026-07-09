# Work Packet WP-37 - Resumely Activation Follow-ups (Jul-8 walkthrough)

- Status: **IN PROGRESS** (S1 live 1.4; S2/S3/S5 done; S4 coded pending ship; Verify read filed)
- Created: 2026-07-08
- Source: Builder OS vault `02-Products/ResumeBuilder/2026-07-08-resumely-activation-walkthrough-friction-report.md` — full production walkthrough by Claude (Fable 5), both surfaces, every finding with blind repro
- Mode: Builder
- Workflow pattern: one story at a time (implement → lint+tests → evidence → next)
- Input trust: trusted internal (findings reproduced live against production 2026-07-08)
- Outcome loop: Resumely 20% real (founder-excluded) activation / 30 days, launch→export (founder decision 2026-07-02, EXD-013/EXD-015)
- Related: WP-29 (web funnel P0s, DONE), WP-36 (export instrumentation), PR #90 (iOS upload friction, merged-not-shipped), EXD-018 (monetization gate closed), vault [[2026-07-02-priority-reset-resumely-primary]]
- Success signal: the shipped App Store build opens the file picker in one tap; the web anon rate-limit path never wipes user input; and a builder can execute each story below blind from its initiation prompt.

## Headline decision this packet encodes

**The export button is not the wall.** The Jul-8 walkthrough proved the web loop works end to end (landing → signup → optimize → `/api/download/{id}?fmt=pdf` → 200). The activation wall is one step earlier on iOS and it is **shipped**: live 1.3 (8) still has the two-tap upload sheet + empty-Recents picker. PR #90 fixes both but is in **no App Store build** (1.3(8) was cut 07-05; PR #90 merged 07-08). So **S1 is the whole ballgame** — it converts already-merged code into shipped activation. Everything else is cleanup ranked below it. Do **not** redesign the export screen (EXD-018 gate closed; export works).

## Model Routing (per GLOBAL-TOOL-USAGE.md tiers)

Cheapest capable model per story; Opus only where correctness/judgment is the risk; HUMAN gate where Apple signing or a data-exposure call is involved.

| Story | Work type | Route | Repo |
|---|---|---|---|
| S1 ship iOS upload fixes | Release/signing (Apple Distribution) + on-device smoke | **HUMAN gate → Sonnet** (smoke) | iOS |
| S2 web rate-limit input preservation | Feature fix against an established pattern (WP-29 S3) | **Sonnet** (Codex also fits) | Web |
| S3 iOS guest saved-resume verification | Root-cause: is it a real cross-user leak or leftover state? | **investigator → Opus if real** | iOS |
| S4 iOS add-job above the fold | Layout-only SwiftUI change | **Sonnet** (Haiku/Codex fine) | iOS |
| S5 web fragment filter + console quiet | Mostly mechanical extraction filter | **Haiku/Codex**, Sonnet code-review | Web |
| Verify | Re-run funnel read after S1 is live | **Sonnet** | analytics |

## Repos

- **ResumeBuilder iOS (Resumely):** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP` — Swift + WKWebView, SwiftUI V2 (`@Observable`/`@MainActor`), live build 1.3 (8), branch tip `41d6fce` (PR #90 merged).
- **ResumeBuilder Web:** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-` — Next.js + Supabase, `main` carries all of WP-29.

## Read First (every story)

- Builder OS vault `02-Products/ResumeBuilder/2026-07-08-resumely-activation-walkthrough-friction-report.md` (findings + repro)
- Target repo `tasks/lessons.md` and `tasks/ERRORS.md` (iOS) / `tasks/lessons.md` (web)
- iOS: `.agents/product-marketing.md` (Fit/Match positioning — never "pass ATS")

---

## S1 — Ship the merged iOS upload fixes to the App Store — **HUMAN gate + iOS**

**Why #1:** PR #90's one-tap picker + "Files · iCloud Drive · Downloads" cue + Story-4 cancel tracking are on `main` (`41d6fce`) but in **no shipped build**. Live 1.3 (8) still opens `UploadSheetView` (an intermediate sheet) before the OS picker and lands users on an empty "Recents." This is the exact step the funnel drops at (8 uploaded → 2 optimized). Shipping is the highest-leverage activation action available and needs no new code.

**Repo:** iOS. **Files:** `ResumeBuilder IOS APP.xcodeproj/project.pbxproj` (version bump only), `Features/V2/Home/HomeTabView.swift` (verify, no change).

**Founder-gated (only the founder can do these):** Apple Distribution signing identity is not on the build machine — Product → Archive → Validate → Distribute → submit is manual in Xcode Organizer. Claude/Codex can do everything up to the archive.

**Model:** HUMAN gate for signing/submission; Sonnet for the version bump + on-device smoke script.

**Initiation prompt (paste to Claude Code / Codex in the iOS repo):**
> Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`. Read `tasks/lessons.md` and `tasks/progress.md` first. Goal: cut a release build from current `main` (`41d6fce`, PR #90 merged) that carries the one-tap upload picker and empty-Recents location cue, so the live App Store build stops opening the intermediate `UploadSheetView` before the OS picker. Steps: (1) confirm `main` is at `41d6fce` and `HomeTabView.swift`'s upload CTA sets `isImporterPresented = true` directly (no `UploadSheetView` presentation on the primary path). (2) Bump `CURRENT_PROJECT_VERSION` 8 → 9, keep `MARKETING_VERSION 1.3` (or 1.4 if the founder says so). (3) Build + full test suite on iPhone 17 simulator (Debug), then a Release generic-iOS compile with `CODE_SIGNING_ALLOWED=NO` as an archive proxy. (4) On a booted simulator or device, smoke the upload path: launch guest → tap "Choose a file" → confirm the OS file picker opens in ONE tap (no intermediate sheet) → confirm the empty-Recents case shows the "Files · iCloud Drive · Downloads" cue. Capture a screenshot. (5) STOP and hand off to the founder for Xcode Organizer archive → validate → submit (Apple Distribution signing is founder-only). Do not deploy or submit yourself. Update `tasks/progress.md`. No new dependencies. No monetization/export UX changes (EXD-018 closed).

**Acceptance:** a build cut from `main` where the upload CTA opens the picker in one tap on a real run; version bumped; suite green; handoff note names the exact commit + build number for the founder to submit. Funnel re-read (Verify story) after it's live shows the pre-picker drop moving on non-founder traffic.

---

## S2 — Web: preserve upload + JD on the anonymous rate-limit path — **Sonnet**

**Why:** WP-29 S3 stopped the form wiping on *server-validation* errors, but the *rate-limit* path still clears everything. Live repro (2026-07-08, twice): submit resume + 100+ word JD from a rate-limited IP → "You have used your free checks for now" → tap "Back to checker" → file and JD are gone (`input[type=file].files.length === 0`, textarea empty). A returning user re-does all their work at the most fragile moment.

**Repo:** Web. **Files:** `src/components/landing/UploadForm.tsx` (holds `resumeFile`/`jobDescription`/`jobDescriptionUrl` state, lines ~35-37), `src/components/landing/RateLimitMessage.tsx` (has `onBackToChecker` callback, line ~11), and their common parent (likely `src/app/[locale]/page.tsx` or `ats-checker/page.tsx`) that toggles between the form and the rate-limit card.

**Model:** Sonnet (Codex fits).

**Initiation prompt (paste to Codex / Claude Code in the web repo):**
> Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`. Read `tasks/lessons.md` and `tasks/ERRORS.md` first. Bug (reproduced live twice on production 2026-07-08): on the landing anonymous ATS check, when the server returns the rate-limit state ("You have used your free checks for now"), the app renders `RateLimitMessage`, and tapping its "Back to checker" (`onBackToChecker`) returns to an EMPTY form — the uploaded resume file and pasted job description are both wiped. This is the same class of input-loss WP-29 S3 fixed for the validation path, but the rate-limit path was missed. Fix: keep the `resumeFile`, `jobDescription`, and `jobDescriptionUrl` state alive across the rate-limit → back-to-checker transition (do not unmount/reset `UploadForm` state; `onBackToChecker` should just switch the view back, not clear inputs). If the limit state can be known before the user uploads, also surface it earlier — optional, only if low-risk. Add focused test coverage: a rate-limit response followed by "Back to checker" preserves file + JD. Validation: focused tests, `npm run check:i18n`, targeted eslint, `git diff --check`, `npm run lint`, `npm run build`. `npx tsc --noEmit` may still fail on pre-existing unrelated errors — none in your touched files. Do not touch monetization/pricing (EXD-018). Scope gate: if this expands past 3 files, stop and surface. Update `tasks/progress.md`.

**Acceptance:** a rate-limited submit preserves file + JD after "Back to checker"; a forced rate-limit in a test shows the message without clearing input; lint/build green.

---

## S3 — iOS: verify the guest saved-resume list is empty for a genuinely new user — **investigator (Opus if real)**

**Why:** On a reinstalled app in guest mode (never signed in this session), "Use a saved resume" loaded six real files titled "Nadav Yigal CV 2024," "Updated cv - Nadav 2026" — the founder's actual resumes. Most likely a persisted anon/auth token on that simulator from prior founder testing (leftover state), NOT a real cross-user leak. But a saved-resume list is backend-auth-gated, so if a real new install sees seeded data it is a **data-exposure P0** and jumps ahead of everything. Not filed as confirmed — must be verified.

**Repo:** iOS. **Files (read to understand the auth/session boundary):** `Features/Tailor/SavedResumePickerSheet.swift`, `Features/V2/Home/HomeTabView.swift` (`showLibraryPicker`), the resume-library service + whatever persists the anon/auth token (`App/AppState.swift`, `Core/API/`).

**Model:** investigator first (read-only root-cause); escalate to Opus only if it turns out to be a real leak needing a fix.

**Initiation prompt (paste to the `investigator` agent in the iOS repo):**
> Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`. Read `tasks/ERRORS.md` and `tasks/lessons.md` first. Question to answer (do NOT write app code yet): does a genuinely first-time guest user — clean install, never signed in, no prior stored token — see an EMPTY "Use a saved resume" list, or do they see seeded resumes? Observed 2026-07-08: on a reinstalled simulator app in guest mode, the saved-resume picker showed six real founder resumes ("Nadav Yigal CV 2024"). Determine whether this is (a) leftover persisted anon/auth session state on that specific simulator (expected, benign) or (b) a real cross-user data leak where any new install can pull another user's resumes (data-exposure P0). Trace how `SavedResumePickerSheet` / the resume-library service authenticates: what identity does it query with for a guest, where is the anon/auth token persisted, and can a brand-new device with no token retrieve resumes tied to a real account. To confirm empirically: describe the exact wipe needed (uninstall + clear the app's stored token/keychain/anon id) and, if you can, reproduce on a fully clean simulator. Report one of: "empty for a real new guest — was leftover simulator state, close it" OR "real leak — here is the code path and the fix," with file:line evidence. If (b), escalate: this is a P0 ahead of S1.

**Acceptance:** a documented verdict with evidence — either closed as leftover state, or a filed P0 with repro + the offending code path.

---

## S4 — iOS: lift the Add-Job input above the fold after file selection — **Sonnet**

**Why:** After a resume is selected, the "Add Job / URL or paste description" card sits below the fold behind the tab bar; the user must scroll to reach the very next required step. Minor, but it's invisible at the moment it becomes actionable.

**Repo:** iOS. **Files:** `Features/V2/Home/HomeTabView.swift` (the `ScrollView` at ~line 53; the `jobInputCard`; the step cards).

**Model:** Sonnet (Haiku/Codex fine — layout only).

**Initiation prompt (paste to Codex / Claude Code in the iOS repo):**
> Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`. Read `tasks/lessons.md` first (note the V2 folder rule and `@Observable`/`@MainActor` rule). UX fix in `Features/V2/Home/HomeTabView.swift`: after a résumé is selected (step 1 done, `jobInputCard` becomes the active step 2), the job URL/paste input sits below the fold behind the tab bar and needs a manual scroll to reach. Make the job input visible without a manual scroll once a file is selected — e.g. use `ScrollViewReader` to `scrollTo` the job-input anchor when selection completes, or reorder so the active step is in view. Keep the 100pt tab-bar clearance. Do not fake any state; only reveal what already exists. Validation: Debug build on iPhone 17 simulator, and a simulator smoke on iPhone SE + iPhone 17 confirming the job field is visible without scrolling right after selecting a file (screenshot both). Focused tests if any view-model logic changes (there likely is none). No new dependencies; no changes outside `HomeTabView.swift` unless a shared anchor is needed. Update `tasks/progress.md`.

**Acceptance:** on iPhone SE and iPhone 17, after selecting a file the job URL/paste field is visible without a manual scroll; build + smoke green with screenshots.

---

## S5 — Web: filter sentence fragments from "Key requirements" + quiet the false anon-conversion error — **Haiku/Codex, Sonnet review**

**Why:** The export page's Job-summary "Key requirements" list surfaced fragment tokens ("We", "go") alongside real requirements (same class as WP-29 P1-7, still open from that packet's own follow-up). Separately, `Anonymous ATS session conversion failed: {"error":"Session not found."}` (404) fires on signup even when no anon session exists — benign console noise that could mask a real S5 carryover failure.

**Repo:** Web. **Files:** render site `src/app/[locale]/dashboard/optimizations/[id]/page.tsx` (~line 188, `jdData.parsed_data.requirements.slice(0,3)`) — trace upstream to where `parsed_data.requirements` is written (the JD parse/extraction step) and filter there; `src/components/auth/auth-form.tsx` (the anon-session conversion call) for the console-quiet.

**Model:** Haiku/Codex background for the filter; Sonnet code-review on the extraction change.

**Initiation prompt (paste to Codex in the web repo):**
> Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`. Read `tasks/lessons.md` first. Two small, independent cleanups. (1) The export page "Job summary → Key requirements" list shows sentence fragments as requirements (observed live: "We", "go" alongside real items like "SQL", "leadership"). Render site: `src/app/[locale]/dashboard/optimizations/[id]/page.tsx` around line 188 reads `jdData.parsed_data.requirements`. Trace where `parsed_data.requirements` is populated during job-description parsing and add stop-word / fragment filtering there (drop bare pronouns and <2-word fragments like "We", "go"), reusing any existing stop-phrase list in the repo rather than adding a new one — check `src/lib/agent/tools/` and the ats-check path first. (2) On signup, `auth-form.tsx` logs `Anonymous ATS session conversion failed: Session not found` (404) even when there is no anon session to convert; guard the conversion call so it is skipped (or the error swallowed quietly) when no anon session id exists, so a real conversion failure isn't masked by noise. Validation: focused tests where practical, `npm run check:i18n`, targeted eslint, `git diff --check`, `npm run lint`, `npm run build`. Do NOT reintroduce "ATS score" phrasing; keep Fit/Match language. Scope gate: >3 files → stop and surface. Update `tasks/progress.md`. Have a Sonnet code-reviewer check the extraction filter change specifically.

**Acceptance:** a fresh optimization's Key requirements contains no fragment tokens; no false 404 conversion error on a signup with no prior anon check; lint/build green.

---

## Constraints (all stories)

- One story at a time; lint + tests green before "done"; evidence in the story report.
- No deploy, migration, or App Store submission without explicit founder "yes" in the current message.
- Monetization gate stays closed (EXD-018): no Premium / Stripe / paywall / export-screen-redesign work.
- No new npm/SPM dependencies without asking. No secrets in code.
- iOS: new screens in `Features/V2/`; `@Observable`/`@MainActor` only; `Endpoint` enum via `APIClient`, never hardcoded URLs.
- Scope gate: if any story expands past 3 unexpected files, stop and surface.
- Exclude QA traffic from metrics (`nadav.yigal+fable-qa*` aliases) per posthog-founder-account-exclusion.

## Validation

- Per-story acceptance criteria above, plus each repo's lint/test suite.
- iOS: Xcode build + relevant `ResumeBuilder IOS APPTests/` suites green before "done"; simulator/device smoke for any UI change.
- Web: existing eval harness stays green; `npm run build` passes.
- Verify story: after S1 is live on the App Store, re-run the founder-excluded funnel (`resume_upload_cta_seen → resume_upload_cta_tapped → resume_file_picker_opened → resume_file_selected → optimization_completed → export_success`, `$lib=resumely-ios-urlsession`, exclude prefixes `067544b5`, `761e5b1b`, `a6441489`, `712cf425`) and file the delta.

## Progress

- 2026-07-08: Packet created from the Jul-8 walkthrough friction report. Not started. S1 is the priority — it ships already-merged code; everything else ranks below it.
- 2026-07-08: **S1 executed (agent).** `main` at `41d6fce`; build **1.3 (9)** cut; Debug tests green; Release compile green; upload hero smoke on iPhone 17 sim (build 9, location cues visible). **Blocked on founder:** Xcode Organizer archive → validate → distribute → submit (Apple Distribution signing). Uncommitted in iOS repo: `project.pbxproj` version bump only.
- 2026-07-08: **S2 executed (agent).** Web rate-limit path now preserves `UploadForm` state across rate-limit → back-to-checker; tests + lint + build green. Uncommitted in web repo: `FreeATSChecker.tsx`, test file.
- 2026-07-08: **S3 closed (investigator, no code).** Guest saved-resume list showing founder CVs was leftover Keychain-restored Supabase session on the test simulator, not a cross-user leak. Library API is auth-gated end-to-end.
- 2026-07-09: **S4 executed (agent).** `ScrollViewReader` scrolls to job input after resume select; iOS Debug build green. Pending 1.4.1 ASC submit.
- 2026-07-09: **S5 executed (agent).** JD requirement fragment filter + quiet 404 anon conversion; tests + build green. Pending web deploy.
- 2026-07-09: **Verify read (post-1.4 live).** PostHog project `270848`, iOS `$lib=resumely-ios-urlsession`, since `2026-07-08`: 3 `resume_upload_cta_seen` → 1 tapped → 1 picker opened → 1 file selected → 0 optimization → 0 export. Sample too small for delta vs pre-1.4 baseline (60d clean: 10 picker / 5 selected); re-read in 7–14d.
