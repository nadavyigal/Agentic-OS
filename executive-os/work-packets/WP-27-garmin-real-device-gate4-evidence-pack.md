# Work Packet WP-27 - Garmin: Real-Device Gate-4 Evidence Pack for the Commercial Resubmission

- Status: Open
- Created: 2026-07-02
- Source: Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md` (PR #13, merged), step 4 of the synthesis action plan
- Mode: Builder
- Workflow pattern: normal
- Input trust: trusted internal (App Store Connect state needs founder confirmation — HUMAN checkpoint below)
- Outcome loop: RunSmart Garmin production approval
- Related: WP-26 (this packet's output is WP-26's Step 3/4 dependency), `docs/garmin-application/GARMIN-STATUS.md`
- Success signal: 6 Garmin UX screenshots exist, captured on a real device against the confirmed-live build, using the pristine official Garmin Connect tile asset, with no remaining "Garmin Wellness" references anywhere in the app

## Owner Role

RunSmart iOS operator

## Project

RunSmart iOS

Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Goal

Produce evidence that cannot trigger a fourth rejection: real-device screenshots (not simulator), captured against the build that is actually live on the App Store, with the pristine unaltered official Garmin Connect brand asset, and zero remaining references to the invented "Garmin Wellness" term Marc rejected on 2026-07-01.

## Context

Three Gate-4 rejections in nine days (2026-06-22, 2026-06-26, 2026-07-01) each addressed the immediate complaint but left a next one unaddressed — the pattern the STORM analysis flags as the biggest controllable risk in the whole Garmin thread. `GARMIN-STATUS.md` records that the last resubmission (1.0.6/19, sent same-day as the fixes) was rejected same-day because "Garmin Wellness" is not a recognized term in Garmin's brand guidelines at all — it needed removing, not re-skinning, and the fix (rename to "Wellness Trends" across `SecondaryFlowView.swift`, `ProfileTabView.swift`, `RunSmartGate4ScreenshotMode.swift`) is merged. Two things are still explicitly flagged as unverified in `GARMIN-STATUS.md`: whether the Garmin Connect tile asset (`GarminConnectTile.imageset/garmin-connect-tile.jpg`, 512x512 lossy JPEG) is genuinely the pristine file from Garmin's brand-asset kit rather than a re-saved capture, and whether 1.0.7 (20) is actually confirmed live.

This evidence pack is a hard input to WP-26 — do not let WP-26 file the commercial application's Production submission without it.

## Read First

- `docs/garmin-application/GARMIN-STATUS.md` (Gate 4 section, full rejection history)
- Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md`
- `Garmin_Developer_API_Brand_Guidelines.pdf` and `Brand_Requirements_Summary.jpg` (Garmin-provided assets, from the email chain — pages 2 and 4 specifically)
- `GarminConnectBrandMark.swift`, `ProfileTabView.swift` (`ConnectedServiceTile`), `SecondaryFlowView.swift`

## Task

1. **HUMAN checkpoint — confirm live build.** Ask the founder to confirm in App Store Connect: is iOS build 1.0.7 (20) actually live on the App Store right now, or still 1.0.6 (19)? Do not assume from `tasks/progress.md` — that file can go stale relative to Apple's own state (see `~/.claude/ERRORS.md` 2026-06-30 "Stating product status from memory"). Cite the exact confirmed version/build and source.
2. **Verify the tile asset.** Re-download the official Garmin Connect square tile directly from `developer.garmin.com/brand-guidelines/connect/` (or the attached brand-asset kit from the email thread). Compare byte-for-byte / visually against the current `GarminConnectTile.imageset/garmin-connect-tile.jpg`. If they differ at all, replace the asset with the freshly downloaded original — do not re-export, re-save, or recompress it.
3. **Grep for stray "Garmin Wellness" references.** Confirm the 2026-07-01 rename (`GarminWellnessViews`/`.garminWellness`/"Garmin Wellness" → `WellnessTrendsView`/`.wellnessTrends`/"Wellness Trends") is complete across code, strings files, and any App Store metadata/screenshots that might still say the old term.
4. **Recapture all 6 screenshots on a real physical device** (not simulator) against the confirmed-live build from Step 1:
   - Screens 01-03: Garmin Connect connection screen, showing the official untouched tile.
   - Screens 04-06: activity feed, Recovery dashboard, Wellness Trends — each showing device-model attribution (e.g. "Garmin Forerunner 965"), not the bare word "Garmin."
5. **Re-verify each screenshot against the brand PDF's pages 2 and 4** line by line before packaging — this is the step every prior rejection skipped.
6. Zip the 6 screenshots with a clear naming convention (`runsmart-garmin-screenshots-ios-<date>.zip`), matching the format Marc's replies have consistently required.
7. Hand off the zip + confirmed build/version + tile-asset confirmation to WP-26 for inclusion in the single consolidated resubmission.

## Constraints

- Real device only. No simulator screenshots go into this evidence pack, ever — this was explicitly called out as a rejection risk in WP-24.
- Do not alter, crop, recolor, or reshape the official Garmin Connect tile in any way (`.clipShape` and similar were the exact bug in the 2026-07-01 rejection).
- Do not resubmit anything to Garmin from this packet — evidence prep only. Submission is WP-26.
- No unrelated iOS changes bundled into this packet.

## Validation

- Founder-confirmed live build/version cited with source (App Store Connect, not `progress.md`).
- Tile asset diff shows either "identical to official kit" or "replaced with official kit" — one or the other, explicitly stated.
- Grep for "Garmin Wellness" (case-insensitive) across the iOS repo returns zero hits outside historical docs/changelogs.
- All 6 screenshots reviewed against brand PDF pages 2+4 with a pass/fail note per screenshot.

## Completion Gate

Report:

- Confirmed live App Store version/build and how it was verified.
- Tile asset status (identical / replaced) with source of the replacement file.
- Grep result for stray "Garmin Wellness" references.
- Screenshot zip location and per-screenshot brand-guideline check result.
- What was NOT done, and explicit confirmation this evidence is ready to hand to WP-26 (or what's still blocking it).
