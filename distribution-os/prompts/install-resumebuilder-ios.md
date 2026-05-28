# Install Prompt — ResumeBuilder iOS Distribution

Paste this into Codex or Claude Code while sitting inside the ResumeBuilder iOS repo root: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`.

---

You are installing the Distribution OS into the ResumeBuilder iOS app repo. Distribution OS lives globally at `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/`. ResumeBuilder Web (the GTM source) lives at `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`.

Hard constraints:

- Do not edit product source code (Swift, Xcode project files, app assets, app config). You may create files only inside `.agent-os/distribution/`, `.agents/`, and `tasks/`.
- Do not add new dependencies anywhere.
- Do not publish anything externally.
- Free / low-cost channels first. No paid ads.
- One product focus: ResumeBuilder iOS. ASO is Tier A. Web is a feeder to App Store install.

## Pre-Flight Reading

Read in order. State the objective in one sentence after step 5.

1. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/distribution-context.md`
2. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/operating-principles.md`
3. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/projects/resumebuilder.md`
4. `/Users/nadavyigal/Documents/Projects /Agentic OS/PROJECT-BRIDGES/resumebuilder-distribution.md`
5. `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/data/connectors.md`

## Step 1 — Install Scaffold (todo item 1)

```
mkdir -p .agent-os/distribution
cp -R "/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/projects/resumebuilder/scaffold/"* .agent-os/distribution/
```

Verify: list the files copied. Confirm `gtm-plan.md`, `app-store-program.md`, and `hebrew-program.md` are present.

## Step 2 — Mirror Positioning For marketingskills (todo item 2)

```
mkdir -p .agents
cp .agent-os/distribution/product-positioning.md .agents/product-marketing.md
```

Source of truth is `.agent-os/distribution/product-positioning.md`; re-mirror when it changes.

## Step 3 — Pull Real Data Into The Scaffold (todo item 3)

For each scaffold file below, do the following pass:

### `app-store-program.md`

Find the current App Store listing fields. Search this repo for:

- Existing fastlane metadata: `fastlane/metadata/en-US/*.txt` and `fastlane/metadata/he/*.txt` (name, subtitle, keywords, description, promotional_text)
- Any `AppStoreConnect/`, `AppStore/`, `Resources/AppStore/`, `marketing/aso/` folders
- Any `metadata.json`, `app-store.md`, `aso.md` files
- TestFlight notes
- Screenshots under `fastlane/screenshots/` or `screenshots/`

For each field present: paste the current value into `app-store-program.md` under "Current State". For each missing: leave a `<fill>` placeholder. Capture both English and Hebrew metadata states.

### `metrics.md`

Look for analytics wiring (PostHog initialization, event registry, attribution tagging). For each metric, mark `tracked` / `not tracked` / `unknown`. Do not invent numbers.

### `lifecycle-program.md`

Look for email triggers, push notification setup, onboarding flow references. For each stage, mark `live` / `draft` / `not started`.

### `directories.md`

Confirm whether a directory submission pack already exists (in the web repo's `marketing/` or this repo's `marketing/aso/` or Drive `04 Content Assets/Directory Submissions/`). If a pack exists, note its location. If not, add it as the next high-priority asset.

### `assets-needed.md`

Add any gaps you discover (missing screenshots, missing Hebrew assets, missing lifecycle email).

### `competitors.md`

Confirm against material in the web repo (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/docs/`) or this repo. Update Teal / Rezi / Kickresume positions if their listings have changed.

Output: a single message summarizing what you found, what is filled, what is still `<fill>` or `unknown`.

## Step 4 — GTM Pull-In And Amend (new)

Run `distribution-os/workflows/13-gtm-plan.md`.

### 4a. Locate the ResumeBuilder Web GTM

Search ResumeBuilder Web at `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/` for GTM source material. Try:

- `docs/agent-os/gtm/`
- `docs/gtm/`
- `docs/product/gtm-plan.md`
- `docs/product/positioning.md`
- `marketing/gtm/`
- `tasks/gtm.md`
- Any file with "gtm", "go-to-market", "positioning", "channels" in the name

Prefer the most recently modified file when there are several.

### 4b. Inherit + amend

Build `.agent-os/distribution/gtm-plan.md` by filling the template at `/Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/templates/gtm-plan-template.md`. Apply the inheritance map ruthlessly:

- The Hebrew variant is a material differentiator and must show up in audience, channels, and pricing
- The web SEO and programmatic SEO work that produced web signups must be re-framed for App Store install conversion
- ATS-aware claims must reflect what the iOS app actually does, not what the web app does, if they differ
- The credit / pricing system on iOS may not match web — flag any divergence

Pricing is a hard checkpoint. If web sells subscription and iOS uses in-app credits (or vice versa), capture both pricing models and the cross-platform restore policy.

### 4c. Walk Through Open Questions From `projects/resumebuilder.md`

For each, propose your best read of the answer based on the repo, then ask me to confirm. Capture the resolved answer in the matching scaffold file.

1. **App Store status**: pre-submission, TestFlight, soft launch, or live? Decides ASO urgency.

2. **iOS pricing model**: in-app purchase, subscription, credit system, or free? How does it relate to the web's paid offering? Cross-platform restore? Goes into `gtm-plan.md` section 7.

3. **Hebrew on iOS**: separate App Store listing region or one listing with multiple locales? Authored Hebrew metadata? PDF / template RTL fully end-to-end on iOS? Goes into `app-store-program.md` localization, `hebrew-program.md`, and `gtm-plan.md` section 8.

4. **ATS parser parity**: does the iOS app run the same parser as web, or a subset? Affects what claims are defensible on the App Store. Goes into `app-store-program.md` description and `messaging.md`.

5. **Apple attribution**: are web-to-App-Store CTAs wired with `at=` and `ct=` parameters yet? Affects every web-feeder experiment. If not wired, top of `assets-needed.md`.

6. **Free ATS tool MVP**: lives on web today (or planned)? Result page hands off to App Store install? Affects whether free tool is Tier A right now.

7. **Apple Search Ads**: explicitly out of scope until organic ASO proves — confirm.

For each answer, append to `gtm-plan.md` section 17 (Decision Log): `YYYY-MM-DD: <decision> — <reason>`.

## Step 5 — Set Up First Weekly Cycle (followup)

Create or append `tasks/MEMORY.md` with:

```
## YYYY-MM-DD — Distribution OS installed for ResumeBuilder iOS
Worked on: Distribution OS install + GTM v0
Completed: scaffold installed, positioning mirrored, app-store-program audited, gtm-plan v0 drafted from ResumeBuilder Web GTM
In progress: open questions resolved → see gtm-plan.md decision log
Decisions: <list founder confirmations from step 4c>
Next session: run first weekly distribution cycle
  Prompt to use: Read and execute: /Users/nadavyigal/Documents/Projects /Agentic OS/distribution-os/prompts/weekly-distribution-run.md
  Suggested theme for first week: ASO listing setup + rewrite (English; Hebrew metadata prep as secondary)
  Pre-work the founder should do before the cycle:
    - Export Search Console (web) + App Store Connect (if listing exists) into Drive 05 Metrics Exports/
    - Confirm App Store status (pre-submission / TestFlight / live)
    - Capture iOS pricing model decision so paywall + landing copy align
```

## Step 6 — Final Report

Single message to me containing:

- What was installed (file paths)
- `app-store-program.md` filled vs `<fill>` summary (English + Hebrew)
- GTM inheritance map result (carry / edit / drop / net new counts)
- Founder open-question answers captured
- Pricing-block status (filled / blocking question / divergence between web and iOS)
- The list of items still requiring me
- The confirmed prompt for next session

Stop. Do not run the weekly cycle. Do not publish anything.
