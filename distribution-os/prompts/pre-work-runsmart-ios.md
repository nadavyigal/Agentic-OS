# Pre-Work Prompt — RunSmart iOS Distribution Foundation

Paste this into Claude Code while sitting inside the RunSmart iOS repo root:
`/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

Run this session **before** the weekly distribution cycle. It builds the four pieces the weekly cycle assumes exist.

---

Hard constraints (same as install):

- Do not edit product source code (Swift, Xcode project files, app assets, app config).
- Do not add new dependencies.
- Do not publish anything externally.
- Write only to `.agent-os/distribution/`, `.agents/`, `tasks/`, and the prompts folder.
- Founder approves all copy before it is rendered or submitted anywhere.

---

## Pre-Flight Reading

Read in order. State the objective in one sentence after step 3.

1. `.agent-os/distribution/product-positioning.md`
2. `.agent-os/distribution/app-store-program.md`
3. `.agent-os/distribution/gtm-plan.md` — sections 0–8 and §17 (decision log) only

---

## Step 1 — Screenshot Overlay Copy (todo item 1)

The 5 primary screenshot slots are staged in `fastlane/screenshots/en-US/` but have no caption overlay text. The App Store listing is weaker without them. This step authors the copy.

### 1a. Load the positioning context

Read `.agents/product-marketing.md`. Note the one-liner, the subtitle, and the top differentiators.

### 1b. Read the screenshot filenames and infer the screen being shown

```
01_today    → Today screen: next recommended workout, readiness context
02_plan     → Training plan calendar view
03_run      → Live GPS run recording
04_report   → Post-run debrief / report
05_profile  → Profile with stats, Garmin/Health connections
```

### 1c. Author overlay copy for each slot

For each screenshot, write:

- **Headline** (4–6 words, bold, top or bottom overlay): the one thing this screen proves about the product. Avoid generic words like "smart", "powerful", "easy".
- **Subline** (8–12 words, lighter weight): one concrete detail that earns the headline. Use the user's language, not product language.

Produce this as a table:

| Slot | Screen | Headline | Subline |
|---|---|---|---|
| 01 | Today | | |
| 02 | Plan | | |
| 03 | Run | | |
| 04 | Report | | |
| 05 | Profile | | |

Write 2 headline variants per slot so the founder can choose. Label them A and B.

Constraints:
- Headline must not repeat the app name.
- Must not use: "AI-powered", "smart", "personalized", "seamless", "powerful", "easy".
- Must be true to what the screen actually shows — do not claim features not visible.
- The set of 5 headlines should tell a connected story: today's plan → following it → recording the run → learning from it → seeing the whole picture.

### 1d. Save the output

Write the approved copy (after founder selects A or B per slot) to:
`.agent-os/distribution/screenshot-overlay-copy.md`

Format:
```
# Screenshot Overlay Copy — RunSmart iOS
Status: draft | approved

| Slot | Headline | Subline |
|---|---|---|
| 01 | | |
...
```

Ask the founder to confirm A or B for each slot before writing the "approved" version.

---

## Step 2 — Garmin Feature Audit (todo item 2)

The App Store description mentions Garmin. The founder confirmed some Garmin features are TestFlight-only. We must not claim in the public listing what isn't shipped.

### 2a. Scan the source

Read these files (do not edit any of them):

- `IOS RunSmart app/Features/Wellness/GarminWellnessViews.swift`
- `IOS RunSmart app/Features/Wellness/MorningCheckinView.swift`
- `IOS RunSmart app/Features/Activity/ActivityTabView.swift`
- `IOS RunSmart app/Features/Run/PostRunSummaryView.swift`
- `IOS RunSmart app/Services/ActivityConsolidationService.swift`
- `docs/qa/testflight-readiness-audit-2026-05-23.md`
- `docs/qa/sprint-10-testflight-closeout-report.md`
- `docs/runsmart-lite-testflight-checklist.md`

For each Garmin-related feature you find, assess:

- **What does it do** (one sentence)
- **Is it gated** (feature flag, conditional compile, TestFlight-only entitlement, or unreachable UI path in the release build)?
- **Safe to claim in App Store description**: yes / no / conditional

### 2b. Produce the audit table

| Feature | What it does | Gated? | Safe to claim? |
|---|---|---|---|
| | | | |

### 2c. Propose an updated description sentence for Garmin

Current description says: *"optional connected signals from Apple Health and Garmin"*

Based on the audit, write a replacement sentence that is:
- Accurate to what is fully shipped (not TestFlight-only)
- Specific enough to attract Garmin-owning searchers
- Not a legal / reviewer liability

Ask the founder to approve before updating.

### 2d. Update `app-store-program.md`

Replace the Garmin mention in the Current State block with the approved sentence. Add an "Audit" section noting which features are TestFlight-gated with the date verified.

---

## Step 3 — Analytics Instrumentation Brief (todo item 3)

PostHog is wired but the three most important activation events do not fire. This step produces the instrumentation spec so the founder or a code session can add them.

Do not edit any Swift files. Read-only.

### 3a. Locate the onboarding completion point

Read `IOS RunSmart app/Features/Onboarding/OnboardingView.swift`.

Find the line or function where the onboarding flow transitions out to the main app (e.g., a dismiss, a navigation push to the Today tab, or a completion callback). Note the exact file path and line number.

### 3b. Locate the plan generation completion point

Search for where a new training plan is first persisted or returned to the UI. Likely in:

- `IOS RunSmart app/Services/Supabase/TrainingPlanRepository.swift`
- Any `PlanGenerationService` or equivalent
- Where the coach API call completes and saves a plan

Find the point immediately after the plan object is available to the UI.

### 3c. Locate the run-logged completion point

Find where a completed run is confirmed and saved. Likely in:

- `IOS RunSmart app/Features/Run/PostRunSummaryView.swift`
- Or wherever the user taps "Done" / "Save" after a run and the activity is written to the store

### 3d. Write the instrumentation spec

Produce a file at:
`.agent-os/distribution/analytics-instrumentation-spec.md`

Format per event:

```
## Event: onboarding_completed
File: IOS RunSmart app/Features/Onboarding/OnboardingView.swift
Line: ~<N>
Where: <describe the exact location — e.g., "inside the completion closure of saveProfileAndContinue()">
Code to add:
    RunSmartAnalytics.track("onboarding_completed", properties: [
        "goal": goal.rawValue,
        "experience_level": experienceLevel.rawValue
    ])
Notes: only fire once per user; wrap in a guard against re-fire if the view can re-appear
```

Do the same for `plan_generated` and `run_logged`.

Note: do not add the code to the Swift files in this session. The spec is for a separate product-code session. Flag it clearly at the top of the file.

---

## Step 4 — Email Platform Brief (todo item 4)

Email is the highest-leverage lifecycle channel and it is completely unwired. This step produces the platform recommendation and drafts the 3 most important emails.

### 4a. Evaluate platform options

The project uses Supabase for auth and backend. Read:

- `IOS RunSmart app/Services/Supabase/SupabaseSession.swift` (to confirm auth events available)

Evaluate these options for the founder:

| Option | Auth hook ease | Cost at <1K users | Reliability | Notes |
|---|---|---|---|---|
| Resend (via Supabase webhook) | | | | |
| Postmark (via Supabase webhook) | | | | |
| Supabase built-in email (SMTP relay) | | | | |

Give a recommendation with a 2-sentence rationale. Do not set anything up — produce the brief only.

### 4b. Draft 3 lifecycle emails

Write full copy for:

1. **Welcome** (fires when account is created or onboarding completed)
2. **Plan-generated nudge** (fires 4–6 hours after the first training plan is created, if no run logged yet)
3. **2-day no-show** (fires 48 hours after a scheduled run is missed with no log)

For each email:

```
Subject line (A and B variants):

Preview text (90 chars max):

Body:
[Draft — plain text version]

CTA button text:

CTA deep link placeholder: runsmart://[screen]
```

Tone: calm, personal, non-pushy. The same voice as the app's push notification copy. No urgency language ("Last chance!", "Don't miss out").

### 4c. Save the output

Write to two files:

- `.agent-os/distribution/email-platform-brief.md` (platform recommendation + Supabase hook spec)
- `.agent-os/distribution/email-drafts/welcome.md`
- `.agent-os/distribution/email-drafts/plan-generated-nudge.md`
- `.agent-os/distribution/email-drafts/2-day-no-show.md`

Mark each draft with `status: draft` in the frontmatter.

---

## Step 5 — Update Assets Needed and Memory

### `assets-needed.md`

For each item completed or clarified in this session, update the Status column:

- Screenshot overlay copy → change "needed" to "draft — awaiting founder approval" (or "approved" if confirmed)
- Garmin feature audit → change "needed" to "done — see app-store-program.md audit section"
- Analytics events → change "needed" to "spec ready — see analytics-instrumentation-spec.md"
- Email platform setup → change "needed" to "brief ready — see email-platform-brief.md; emails in draft"

### `tasks/MEMORY.md`

Append:

```
## YYYY-MM-DD — Distribution OS pre-work session
Worked on: Screenshot overlay copy, Garmin audit, analytics spec, email platform brief
Completed: [list what was finished and approved]
In progress: [list what is in draft / awaiting approval]
Decisions: [any founder choices made this session]
Next session: run first weekly distribution cycle
  Prompt to use: Read and execute: /Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/prompts/weekly-distribution-run.md
  Suggested theme: ASO listing audit + rewrite
  Pre-work done: screenshot copy [approved/draft], Garmin description [approved/draft], analytics spec [ready], email drafts [ready]
```

---

## Step 6 — Final Report

Single message containing:

- Screenshot overlay copy (the table, A and B variants per slot) — awaiting founder A/B selection
- Garmin audit table + proposed description sentence
- Analytics spec summary (3 events, 3 file locations)
- Email platform recommendation (1 sentence) + the 3 email drafts
- `assets-needed.md` status updates
- Confirmed next session prompt

Stop. Do not run the weekly cycle. Do not publish anything.
