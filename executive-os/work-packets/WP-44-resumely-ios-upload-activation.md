# WP-44 — Resumely iOS Upload Activation: Picker Landing + No-File Fallback Inputs

- **Status:** Ready for execution — PR open, not yet merged
- **Mode:** Builder
- **Workflow pattern:** normal, one story at a time, device QA per story
- **Input trust:** trusted local context, live product walkthrough evidence
- **Project:** Resumely iOS, `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- **PR:** [nadavyigal/ResumeBuilder-IOS-APP #92](https://github.com/nadavyigal/ResumeBuilder-IOS-APP/pull/92) on branch `docs/wp-44-ios-upload-activation`
- **Full packet:** `tasks/work-pack-wp-44-ios-upload-activation.md` in the product repo (on the PR branch)
- **Companion packet:** WP-43 (web entry-funnel activation) — same activation loop, web + iOS twin findings
- **Success signal:** rising share of first-session users who reach the first diagnosis WITHOUT selecting a file (paste/scan), plus higher `resume_file_picker_opened → resume_file_selected` on the file path

## Source

Live iOS Simulator first-time-user walkthrough of Resumely 1.4.1 (11) (Claude session, 2026-07-11), driven via computer-use in the Simulator GUI, not a code-read.

## Finding

The app's own Home UI is already strong (above-fold CTA, branded dropzone, Step-1-of-3 disclosure). The drop is confirmed at the handoff to Apple's system file picker: tapping "Choose a file" opens iOS Files on "Recents" showing **"No Recents,"** and Browse → "On My iPhone" shows **"On My iPhone is Empty."** Root cause: first-time mobile users frequently have no resume file on the phone at all (it's on their laptop, in email, or on LinkedIn) — no picker UX change fixes that.

## Three stories

1. **S1 (app-only):** replace SwiftUI `.fileImporter` with a `UIDocumentPickerViewController` wrapper setting `directoryURL` so the picker opens on Browse/a populated directory instead of empty Recents.
2. **S2 (root-cause fix):** "No file on your phone? Paste your resume text" fallback feeding the same diagnosis path. Backend text-endpoint dependency explicitly flagged, not assumed.
3. **S3:** on-device VisionKit scan/OCR feeding the S2 text path — no new dependency, nothing leaves the device.

Explicitly rejected: importing a resume from a LinkedIn profile URL (ToS violation + the same datacenter-IP thin-scrape failure already documented for LinkedIn job descriptions on the web side).

## Next step

Execute via Codex or Cursor from the PR branch. S1 is shippable immediately with no dependency; S2/S3 need the backend text-endpoint check first (see packet). Physical-device QA required for S1/S2 — the simulator has no user files to test the "no file present" case against.
