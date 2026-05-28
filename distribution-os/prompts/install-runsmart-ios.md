# Install Prompt — RunSmart iOS Distribution

Paste this into Codex or Claude Code while sitting inside the RunSmart iOS repo root: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`.

---

You are installing the Distribution OS into the RunSmart iOS app repo. Distribution OS lives globally at `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/`. RunSmart Web (the GTM source) lives at `/Users/nadavyigal/Documents/RunSmart`.

Hard constraints:

- Do not edit product source code (Swift, Xcode project files, app assets, app config). You may create files only inside `.agent-os/distribution/`, `.agents/`, and `tasks/`.
- Do not add new dependencies anywhere.
- Do not publish anything externally.
- Free / low-cost channels first. No paid ads.
- One product focus: RunSmart iOS. ASO is Tier A.

## Pre-Flight Reading

Read in order. State the objective in one sentence after step 5.

1. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/distribution-context.md`
2. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/operating-principles.md`
3. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/projects/runsmart.md`
4. `/Users/nadavyigal/Documents/Projects /Agentic OS/PROJECT-BRIDGES/runsmart-distribution.md`
5. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/data/connectors.md`

## Step 1 — Install Scaffold (todo item 1)

Copy the RunSmart scaffold into this repo:

```
mkdir -p .agent-os/distribution
cp -R "/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/projects/runsmart/scaffold/"* .agent-os/distribution/
```

Verify: list the files copied. Confirm `gtm-plan.md` and `app-store-program.md` are present.

## Step 2 — Mirror Positioning For marketingskills (todo item 2)

```
mkdir -p .agents
cp .agent-os/distribution/product-positioning.md .agents/product-marketing.md
```

This file is what every skill in `marketingskills/` looks for first. Do not edit `.agents/product-marketing.md` directly going forward; edit `.agent-os/distribution/product-positioning.md` and re-mirror.

## Step 3 — Pull Real Data Into The Scaffold (todo item 3)

For each scaffold file below, do the following pass:

### `app-store-program.md`

Find the current App Store listing fields. Search this repo for:

- Existing fastlane metadata: `fastlane/metadata/en-US/*.txt` (name, subtitle, keywords, description, promotional_text)
- Any `AppStoreConnect/`, `AppStore/`, `Resources/AppStore/`, `marketing/aso/` folders
- Any `metadata.json`, `app-store.md`, `aso.md` files
- TestFlight notes (`fastlane/metadata/.../release_notes.txt`)
- Any screenshots under `fastlane/screenshots/` or `screenshots/`

For each field present in the repo: paste the current value into `app-store-program.md` under "Current State". For each field missing: leave a `<fill>` placeholder and add it to the open questions list.

If no App Store metadata exists yet, mark the app status as "pre-submission" and capture every field that needs to be authored.

### `metrics.md`

Look for analytics wiring:

- PostHog initialization (search for `PostHog`, `posthog`, `usePostHog`)
- Any analytics config file
- Any in-app events list

For each metric in `metrics.md`, decide:

- `tracked` — event exists in code, value reachable
- `not tracked` — needs instrumentation
- `unknown` — exists in PostHog but we have no recent number

Fill the "Tracked Keywords" table with whatever exists in the metadata. Leave a `<fill>` placeholder for each unknown number; do not invent.

### `lifecycle-program.md`

Look for email triggers, push notification setup, or any onboarding flow code references in fastlane metadata or marketing material. For each stage, mark `live` / `draft` / `not started`.

### `assets-needed.md`

Add any asset gaps you discover during the audit (missing screenshots, missing onboarding email, etc.).

### `competitors.md`

Confirm or amend the existing competitor list against any market research material you find in `/Users/nadavyigal/Documents/RunSmart/docs/` or in this repo's `docs/`.

Output: a single message summarizing what you found, what is filled, what is still `<fill>`, what is `unknown`.

## Step 4 — GTM Pull-In And Amend (new)

Run `distribution-os/workflows/13-gtm-plan.md`.

### 4a. Locate the RunSmart Web GTM

Search RunSmart Web at `/Users/nadavyigal/Documents/RunSmart/` for GTM source material. Try in order:

- `docs/agent-os/gtm/`
- `docs/gtm/`
- `docs/product/gtm-plan.md`
- `docs/product/positioning.md`
- `marketing/gtm/`
- `tasks/gtm.md`
- Any file with "gtm", "go-to-market", "positioning", "channels" in the name

If you find more than one, prefer the most recently modified file.

### 4b. Inherit + amend

Build `.agent-os/distribution/gtm-plan.md` by filling the template at `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/templates/gtm-plan-template.md`. For each web block:

- Carry as-is, edit, drop, or net new (per the workflow's inheritance map)
- Add iOS-specific reality everywhere it matters: ASO, App Store funnel, post-install lifecycle, in-app pricing, Apple's cut, Family Sharing, App Store launch cycle

The pricing block is a hard checkpoint. If you cannot confirm the iOS pricing model from the repo or me, leave it unfilled and put it at the top of open questions.

### 4c. Walk Through Open Questions From `projects/runsmart.md`

These are blocking enough to surface interactively. For each, propose your best read of the answer based on the repo, then ask me to confirm or correct. Capture the resolved answer in the matching scaffold file.

1. **Monetization status on iOS**: is there a paid tier live, in TestFlight, or planned? What model (subscription, one-off, credits)? Where does paywall live? Resolved answer goes into `gtm-plan.md` section 7 (Pricing) and `lifecycle-program.md`.

2. **Garmin and Strava integration depth**: which integrations are live in this iOS build? Which features are gated by them? Resolved answer goes into `app-store-program.md` (description block) and `competitors.md`.

3. **Hebrew market**: is Hebrew in scope for RunSmart iOS in the next 90 days? Default is no for RunSmart. Resolved answer goes into `gtm-plan.md` section 8 and `app-store-program.md` localization block.

4. **Apple attribution**: is the web-to-App-Store attribution wired with `at=` (affiliate token) and `ct=` (campaign token) parameters? Resolved answer goes into `app-store-program.md` "Web → App Store Attribution" block. If not wired, add a row in `assets-needed.md`.

5. **Android**: is an Android version planned this year? Affects whether ASO workflow expands to Google Play. Resolved answer goes into `gtm-plan.md` section 13 and decision log.

6. **App Store status**: pre-submission, TestFlight, soft launch, or App Store live? This decides which ASO tasks are urgent.

For each answered question, append a line to `gtm-plan.md` section 17 (Decision Log): `YYYY-MM-DD: <decision> — <reason>`.

## Step 5 — Set Up First Weekly Cycle (followup)

Create or append `tasks/MEMORY.md` with:

```
## YYYY-MM-DD — Distribution OS installed for RunSmart iOS
Worked on: Distribution OS install + GTM v0
Completed: scaffold installed, positioning mirrored, app-store-program audited, gtm-plan v0 drafted from RunSmart Web GTM
In progress: open questions resolved → see gtm-plan.md decision log
Decisions: <list founder confirmations from step 4c>
Next session: run first weekly distribution cycle
  Prompt to use: Read and execute: /Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/prompts/weekly-distribution-run.md
  Suggested theme for first week: ASO listing audit + rewrite (the highest-leverage RunSmart iOS surface)
  Pre-work the founder should do before the cycle:
    - Export App Store Connect impressions / installs (last 30 days) into Drive 05 Metrics Exports/App Store Connect/
    - Confirm App Store status (pre-submission / TestFlight / live)
    - Capture screenshots of any current ASO listing state
```

## Step 6 — Final Report

Single message to me containing:

- What was installed (file paths)
- What `app-store-program.md` looks like now (filled vs `<fill>`)
- The GTM inheritance map result (carry / edit / drop / net new counts)
- Founder open-question answers captured
- The list of items still requiring me (`<fill>` placeholders + `unknown` metrics)
- The confirmed prompt for next session

Stop. Do not run the weekly cycle. Do not publish anything.
