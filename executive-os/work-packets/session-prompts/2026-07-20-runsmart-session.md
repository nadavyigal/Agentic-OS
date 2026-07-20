# RunSmart iOS — consolidated session (2026-07-20)

Repo: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Context you can trust

1.1.0 (24) is **LIVE** (released 2026-07-19T21:48:08Z, store-verified via Apple's lookup API). It shipped Adaptive Coach Phase 1 flag-ON against `coach_message` edge v10, and **none** of the sign-in wall fixes, so the activation cliff is live for every new download. 1.1.1 (25) exists in the project but has not shipped.

A founder clean-install on 2026-07-20 09:21-09:27 UTC completed sign-in, onboarding, HealthKit, first run and plan generation end to end, with 0 `sign_in_failed`.

## Do these in order

**1. Review and merge PR #105** (`claude/wp51-app-version-super-property`) — adds `app_version`/`app_build` as PostHog super properties and dedupes `onboarding_started`. 317 tests pass (xcresult-verified), red state confirmed on the dedupe test. This is the release blocker: `app_version` was set on 2 of 3,813 events over 60 days, so no funnel could be split by build.

**2. Device-verify the super property actually lands.** Build 1.1.1 (25) to a physical device, trigger any event, and confirm in PostHog project **171597** that it carries `app_version=1.1.1` and `app_build=25`. The unit tests prove the mapping, not that the SDK call works. Five minutes; skipping it risks a second blind release.

**3. Run the real S0 — this gates everything below it.** Founder-only, physical device, live App Store build. Use an Apple ID that has **never authorized RunSmart** (check Settings > Apple ID > Sign in with Apple; remove RunSmart if listed, or use a different Apple ID). The 2026-07-20 test does NOT close this: SIWA authorization survives account deletion and reinstall, so it exercised the already-authorized path. The 7 production `ASAuthorizationError 1000` failures came from Apple IDs that had never seen RunSmart. Record: completes, or fails with 1000. Screenshot it.

**4. If sign-in succeeds, stay on the device** and capture, in the same session: S6 empty-goal evidence and S1 plan-generation failure/retry evidence. Both are listed as open on the FTUX track and both need a physical device.

**5. Fold your remaining work into 1.1.1**, then archive, export with `ExportOptionsAppStoreUpload.plist`, upload, create the version in ASC and submit. Verify the archived `Info.plist` before uploading.

**6. Triage three stale open PRs.** #96 (1.0.9 post-live evidence docs — the version is superseded; merge as history or close), #97 (adaptive side-by-side preview), #87 (FTUX audit). Decide each; don't leave them open by default.

## Constraints

- Do NOT build E1 assignment instrumentation. Founder decision: deferred until sign-in works AND at least 10 clean mature-D7 entrants exist.
- Do NOT chase Adaptive Coach Phase 2. Its gate (>=20 real `adaptive_coach_shown`, founder/QA-excluded) cannot fill while the sign-in wall stands.
- Any activation query must exclude zero-distance or invalid-duration HealthKit rows. The product-side guard is scoped to a later release.
- Keep `share_progress_tapped`; `share_progress_completed` stays parked.
- No new SPM dependencies without asking. No edge-function deploy without explicit approval.

## Validation

Full suite via `xcodebuild test` on iPhone 17 / iOS 26.5 with `-derivedDataPath` under `/private/tmp` (iCloud xattrs break CodeSign otherwise — see `tasks/lessons.md`). Report the pass count read from the xcresult bundle, not pipe output.

## Known traps (from ERRORS.md)

- Exclusion rules protect against inflated numbers, not deleted signal. Any excluded person carrying an ERROR event must be individually re-examined, not swept.
- Never state a version or review status from memory. Verify against Apple's lookup API: `curl -s "https://itunes.apple.com/lookup?bundleId=com.runsmart.lite&country=us"`.

## Completion gate

Update `tasks/progress.md`, `tasks/todo.md`, `tasks/session-log.md`. Push and report push state. Report what was NOT done.
