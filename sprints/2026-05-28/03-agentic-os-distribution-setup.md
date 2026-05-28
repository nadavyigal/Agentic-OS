# Sprint Prompt: Agentic OS — Configure Distribution OS for Both Products
**Date:** 2026-05-28
**Goal:** Install and populate the `.agent-os/distribution/` scaffold in both project repos, configure the distribution command center to reflect both products as active, and sync the dashboard.
**Agentic OS path:** `/Users/nadavyigal/Documents/Projects /Agentic OS`
**RunSmart Web path:** `/Users/nadavyigal/Documents/RunSmart`
**ResumeBuilder Web path:** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`

---

## Session Start — Read These First

1. `distribution-os/distribution-command-center.md` — current state and week's focus
2. `distribution-os/operating-principles.md` — rules governing all distribution work
3. `PROJECT-BRIDGES/runsmart-distribution.md` — what distribution files should exist for RunSmart
4. `PROJECT-BRIDGES/resumebuilder-distribution.md` — what distribution files should exist for ResumeBuilder
5. `distribution-os/projects/runsmart/scaffold/README.md` — install instructions for RunSmart
6. `distribution-os/projects/resumebuilder/scaffold/README.md` — install instructions for ResumeBuilder

Then read source content for populating the scaffold files:
7. `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/docs/product-strategy-2026-05.md` — RunSmart positioning, audience, competitors
8. `PROJECT-BRIDGES/runsmart-ios.md` — RunSmart product context
9. `distribution-os/projects/runsmart/scaffold/drafts/2026-05-27-rs-aso-001/description.txt` — approved App Store description for RunSmart
10. `PROJECT-BRIDGES/resumebuilder-ios.md` — ResumeBuilder product context
11. `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/docs/product/product-vision.md` — ResumeBuilder vision
12. `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP/docs/product/current-product-state.md` — current feature state

State in one sentence what is missing for each product before starting.

---

## Phase 1 — Populate RunSmart Scaffold Files

The scaffold template files already exist at:
`distribution-os/projects/runsmart/scaffold/`

For each file below, read the template, then populate it with real RunSmart content synthesized from the source docs read above. Do not leave placeholder text. Do not invent data — if a field is unknown, write "TBD — requires founder input" rather than guessing.

**Files to populate:**

**`product-positioning.md`**
- One-sentence positioning statement
- Primary ICP (The Rookie, 28-45), secondary ICP (The Striver, 25-40 with wearable)
- Acquisition wedge: runners who churned from Runna citing injury or plan rigidity
- Category: AI running coach (not a training plans app)
- Core value props: readiness-aware daily guidance, proof of progress week-over-week, injury-safe defaults
- Pricing: v1.0 ships free; paid tier TBD

**`audience.md`**
- Primary segment with demographics, psychographics, pain points, and win condition
- Secondary segment with the same
- Channels where each segment can be reached

**`competitors.md`**
- Runna: primary competitor — strengths, weaknesses, where RunSmart wins
- TrainingPeaks, Run Trainer, Nike Run Club: brief notes
- Positioning table (already in product-strategy doc — adapt it)

**`messaging.md`**
- Headline: "The running coach that knows your body, not just your schedule"
- Value props mapped to each ICP
- Proof points (HealthKit/Garmin integration, 10% rule, readiness gate, AI coach conversations)
- What NOT to say (medical claims, guaranteed results, Garmin partnership claims)

**`app-store-program.md`**
- App name: RunSmart
- Subtitle: (derive from product-strategy doc — clear benefit, 30 chars)
- Keywords: running, coach, AI, training plan, marathon, 5K, HealthKit, Garmin, pace, interval
- Description: populated from approved draft at `drafts/2026-05-27-rs-aso-001/description.txt`
- Screenshot strategy: Today tab, Plan tab, Run tab, Coach conversation, Activity/Report
- Category: Health & Fitness
- Localization plan: English first; Hebrew in scope (flag as future)

**`channels.md`**
- Tier A (high-conviction, start here): ASO, running SEO, Runna comparison page, LinkedIn founder cadence
- Tier B (next): lifecycle email, coach/physical therapist partnerships, Garmin/Strava content
- Tier C (later): community research, beginner challenge virality, Android
- Each channel: status (not started / in progress / live), owner, next step

**`gtm-plan.md`**
- Phase 1: App Store submission (this week) → approval (24-48h) → launch tweet + LinkedIn post
- Phase 2: First 100 users — organic SEO + Runna comparison page
- Phase 3: First paid tier TBD
- Success metrics: installs, D1/D7/D30 retention, activation rate (user completes first AI-coached run)

**`metrics.md`**
- North-star: activation rate (user completes first AI-coached run within 7 days of install)
- Leading indicators: installs, onboarding completion rate, first run completion rate
- Current baseline: all zero until App Store goes live
- Data source: PostHog (instrumented in iOS as of this sprint)

**`weekly-plan.md`**
- This week: submit App Store → approval → launch comms
- Next week: first 100 users acquisition — Runna comparison page + LinkedIn post
- Two weeks: first lifecycle email draft live

**`seo-program.md`**, **`lifecycle-program.md`**, **`experiment-backlog.md`**, **`assets-needed.md`**, **`lessons.md`**
- Populate with minimal stubs appropriate to pre-launch state. Mark all programs as "not started" or "planned" as appropriate.

---

## Phase 2 — Install RunSmart Scaffold

From inside the RunSmart Web repo (`/Users/nadavyigal/Documents/RunSmart`):

```bash
mkdir -p .agent-os/distribution
mkdir -p .agents
```

Copy each populated scaffold file from `distribution-os/projects/runsmart/scaffold/` into `/Users/nadavyigal/Documents/RunSmart/.agent-os/distribution/`.

Mirror positioning for marketing skills compatibility:
```bash
cp .agent-os/distribution/product-positioning.md .agents/product-marketing.md
```

Commit to the RunSmart Web repo:
```bash
git add .agent-os/ .agents/
git commit -m "feat(dist): install Distribution OS scaffold for RunSmart v1.0"
```

Verify: `ls /Users/nadavyigal/Documents/RunSmart/.agent-os/distribution/` should list all scaffold files.

---

## Phase 3 — Populate ResumeBuilder Scaffold Files

The scaffold template files exist at:
`distribution-os/projects/resumebuilder/scaffold/`

Populate each file with real ResumeBuilder content from source docs. ResumeBuilder is iOS-first — web exists to feed App Store installs.

**`product-positioning.md`**
- One-sentence positioning: AI-powered resume optimizer that tailors your resume to a specific job, scores it against ATS, applies a professional design, and exports a ready-to-send PDF.
- Primary ICP: Job seeker (25-40), actively applying, frustrated that generic resumes get no callbacks
- Platform: iOS-first; web companion
- Monetization: Credits model (buy credits to run optimizations)
- App name: Resumely

**`audience.md`**
- Primary segment: active job seekers, 25-40, submitting 5-20 applications/month
- Secondary segment: career changers needing to reposition a resume for a new industry
- Hebrew market: noted as in-scope future segment

**`competitors.md`**
- Resume.io, Zety, Kickresume: web-first, design-focused, no job-tailoring AI
- Teal, Rezi: job-specific ATS optimization — closest competitors
- LinkedIn Easy Apply: ecosystem play, no design/export control
- Positioning: RunSmart wins when the user wants job-specific AI tailoring + professional design + PDF export in one native iOS flow

**`messaging.md`**
- Headline: "Your resume, tailored for every job"
- Value props: ATS score check, job-specific AI optimization, 4 professional design templates, Expert review mode, clean PDF export
- What NOT to say: guaranteed interview, ATS "hack", resume writing service claims

**`app-store-program.md`**
- App name: Resumely
- Subtitle: "AI Resume Optimizer" (30 chars)
- Keywords: resume, ATS, job, AI, optimizer, career, CV, interview, hiring, template
- Description: synthesize from product-vision.md and current-product-state.md — cover all 5 tabs, no placeholder text
- Screenshot strategy: Tailor tab (pre-optimize), Optimized preview, Design gallery, Expert tab, Profile/credits
- Category: Productivity (primary), Business (secondary)
- IAP: credit packs — note product IDs must match StoreKitManager.swift expectations

**`gtm-plan.md`**
- Phase 1: App Store submission (tomorrow) → approval → TestFlight internal track first
- Phase 2: External TestFlight testers (5-10 non-developers)
- Phase 3: App Store launch + first directory submissions
- Phase 4: SEO landing pages feeding App Store CTA
- Success metrics: core loop completion rate (upload → optimize → preview → export)

**`metrics.md`**
- North-star: core loop completion rate (upload PDF → optimize → preview renders without error)
- Leading indicators: installs, sign-in rate, optimize attempts, preview render success rate
- Current baseline: all zero (no TestFlight users yet)
- Data source: PostHog (being instrumented this sprint)

**`directories.md`**
- List: Product Hunt, Futurepedia, There's An AI For That, AppAdvice, TopApps.ai
- Status: all not submitted yet
- Note: submit after App Store approval, not before

**`weekly-plan.md`**, **`channels.md`**, **`seo-program.md`**, **`lifecycle-program.md`**, **`experiment-backlog.md`**, **`assets-needed.md`**, **`lessons.md`**, **`hebrew-program.md`**
- Populate with minimal stubs. Mark all programs as "not started" or "planned" except app-store-program which is "in progress".

---

## Phase 4 — Install ResumeBuilder Scaffold

From inside the ResumeBuilder Web repo (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`):

```bash
mkdir -p .agent-os/distribution
mkdir -p .agents
```

Copy each populated scaffold file from `distribution-os/projects/resumebuilder/scaffold/` into `.agent-os/distribution/`.

Mirror positioning:
```bash
cp .agent-os/distribution/product-positioning.md .agents/product-marketing.md
```

Commit to the ResumeBuilder Web repo:
```bash
git add .agent-os/ .agents/
git commit -m "feat(dist): install Distribution OS scaffold for ResumeBuilder iOS v1.0"
```

---

## Phase 5 — Update Distribution Command Center

Edit `distribution-os/distribution-command-center.md`:

- Update **This Week** block:
  - Week of: 2026-05-28
  - Focused product: Both (RunSmart submitting today; ResumeBuilder submitting tomorrow)
  - Theme: App Store submission sprint — both apps
  - Top experiments: rs-aso-001 (description applied), rb-aso-001 (first ResumeBuilder listing draft), rs-analytics-001 (PostHog instrumented)
- Update **Current Channel Status** for both products:
  - RunSmart ASO: "submitting today — build 6 uploading"
  - ResumeBuilder ASO: "in progress — archive ready, submit tomorrow"
  - All other channels: carry forward existing status
- Update **This Week's Done Definition** to include both scaffold installs and both submissions

---

## Phase 6 — Sync Dashboard

Edit `dashboard/status.json`:
- RunSmart iOS: status → "submitting", last_updated → today's date
- ResumeBuilder iOS: status → "pre-release / archive ready", last_updated → today's date
- RunSmart Web: status → "distribution OS installed"
- ResumeBuilder Web: status → "distribution OS installed"

Commit at the Agentic OS level:
```bash
git add distribution-os/projects/ dashboard/status.json distribution-os/distribution-command-center.md
git commit -m "feat(dist): configure Distribution OS for RunSmart + ResumeBuilder; update command center"
```

---

## Scope Guards

- Do not edit product feature code in any of the app repos. This session only installs and populates distribution files.
- Do not publish, post, or submit anything externally — all output is internal drafts and config files.
- Do not invent positioning, pricing, or product claims. Synthesize only from the source docs listed in Session Start.
- If a scaffold file requires data not available in the source docs (e.g., exact Resend API key, exact PostHog project ID), write "TBD — requires founder input" in that field rather than guessing.

---

## Done Definition

- [ ] `product-positioning.md`, `audience.md`, `competitors.md`, `messaging.md`, `app-store-program.md`, `gtm-plan.md`, `metrics.md`, `channels.md`, `weekly-plan.md` populated for RunSmart (no placeholder text)
- [ ] RunSmart scaffold installed at `/Users/nadavyigal/Documents/RunSmart/.agent-os/distribution/`
- [ ] `/Users/nadavyigal/Documents/RunSmart/.agents/product-marketing.md` created
- [ ] RunSmart scaffold committed to RunSmart Web repo
- [ ] Same scaffold files populated for ResumeBuilder (no placeholder text)
- [ ] ResumeBuilder scaffold installed at `.agent-os/distribution/` in ResumeBuilder Web repo
- [ ] ResumeBuilder scaffold committed to ResumeBuilder Web repo
- [ ] `distribution-os/distribution-command-center.md` updated to reflect both products active
- [ ] `dashboard/status.json` updated
- [ ] Agentic OS changes committed
