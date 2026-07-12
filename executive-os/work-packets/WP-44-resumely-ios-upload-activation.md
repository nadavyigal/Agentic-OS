# WP-44 — Resumely iOS Upload Activation: Picker Landing + No-File Fallback Inputs

- **Status:** Evidence-gated — S1 blocked and dropped; S2 waits for 2026-07-18 plus 3-of-5 observation gate; S3 later
- **Mode:** Builder
- **Workflow pattern:** normal, one story at a time, device QA per story
- **Input trust:** trusted local context, live product walkthrough evidence
- **Project:** Resumely iOS, `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- **PR:** [nadavyigal/ResumeBuilder-IOS-APP #92](https://github.com/nadavyigal/ResumeBuilder-IOS-APP/pull/92), merged as the investigation record
- **Full packet:** `tasks/work-pack-wp-44-ios-upload-activation.md` in the product repo
- **Companion packet:** WP-43 (web entry-funnel activation) — same activation loop, web + iOS twin findings
- **Success signal:** rising share of first-session users who reach the first diagnosis WITHOUT selecting a file (paste/scan), plus higher `resume_file_picker_opened → resume_file_selected` on the file path

## Source

Live iOS Simulator first-time-user walkthrough of Resumely 1.4.1 (11) (Claude session, 2026-07-11), driven via computer-use in the Simulator GUI, not a code-read.

## Finding

The app's own Home UI is already strong (above-fold CTA, branded dropzone, Step-1-of-3 disclosure). The drop is confirmed at the handoff to Apple's system file picker: tapping "Choose a file" opens iOS Files on "Recents" showing **"No Recents,"** and Browse → "On My iPhone" shows **"On My iPhone is Empty."** Root cause: first-time mobile users frequently have no resume file on the phone at all (it's on their laptop, in email, or on LinkedIn) — no picker UX change fixes that.

## Three stories

1. **S1 (dropped from active path):** the directory hint has no populated destination because the app has no iCloud Documents capability. Do not add the capability or ship a wrapper with identical behavior without a separate founder decision.
2. **S2 (evidence-gated root-cause fix):** "No file on your phone? Paste your resume text" fallback feeding the same diagnosis path. Activate only after the 2026-07-18 gate if at least 3 of 5 relevant observed users lack a usable local file.
3. **S3:** on-device VisionKit scan/OCR feeding the S2 text path — no new dependency, nothing leaves the device.

Explicitly rejected: importing a resume from a LinkedIn profile URL (ToS violation + the same datacenter-IP thin-scrape failure already documented for LinkedIn job descriptions on the web side).

## Next step

Observe five relevant first sessions and re-run WP-41 on 2026-07-18. If the 3-of-5 local-file gate opens, extend the existing authenticated `/api/upload-resume` multipart contract to accept exactly one of `resume` or `resumeText`, reuse the existing response/persistence pipeline, and use the iOS fields-only multipart helper. Do not use `/api/agent/run`. Keep S3 behind a shipped and measured S2.
