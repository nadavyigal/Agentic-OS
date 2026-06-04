# Design: Pre-Launch Sprint — Two-Track GTM Prep

- Date: 2026-06-04
- Status: Approved
- Author: Brainstorming session (superpowers:brainstorming)
- Scope: Cross-project (RunSmart iOS primary, Resumely iOS secondary)
- Related decisions: EXD-005, EXD-007, EXD-009
- Related work packets: WP-3, WP-4, WP-5 (to be created)

---

## 1. Problem Statement

RunSmart iOS is in Apple review and could be approved any day. As of 2026-06-04, there is no ready launch post, no community targeting, no Product Hunt listing, no lifecycle email, and no App Store listing has been audited for conversion. If Apple approves today, the launch moment is wasted.

Resumely iOS is one keychain unlock away from submission. Its launch window follows closely.

This sprint closes both gaps before either app goes live.

---

## 2. Goals

1. Stage every asset needed to fire a RunSmart launch within hours of Apple approval.
2. Audit and rewrite both App Store listings so they convert from day one.
3. Seed Notion's Campaign Calendar and Content/Asset Pipeline with all sprint assets.
4. Land all assets in the correct Google Drive folders.
5. Do the same for Resumely (at reduced scope — LinkedIn + Reddit only, no social accounts yet).

---

## 3. Non-Goals

- No paid advertising. No automation platforms.
- No Notion database creation (databases already exist per `data/notion-map.md`).
- No feature work in either product repo.
- No publishing without explicit founder approval (`Approved: yes — [date]` in asset header).
- No lifecycle email automation — Gmail send is manual for the first cohort.
- No Runna comparison page (deferred to Distribution OS Week 2).
- No programmatic SEO (deferred).
- No Hebrew market content (deferred to Resumely post-launch).

---

## 4. Track A — Launch Window Assets

### 4.1 RunSmart (7 assets, time-critical)

All assets are drafts for founder review. Nothing publishes until approved.

| ID | Asset | Channel | Format | Drive path |
|---|---|---|---|---|
| A1 | Founder launch post | LinkedIn | 200-250 word personal story, no ad-copy tone | `RunSmart IOS Marketing/04 Content Assets/LinkedIn/launch-post-v1.md` |
| A2 | Page launch post | Facebook (RunSmart page) | Short post + App Store CTA | `RunSmart IOS Marketing/04 Content Assets/Facebook/page-launch-post-v1.md` |
| A3 | Facebook group posts | Facebook groups (3 variants) | Authentic runner voice, link in comments not body | `RunSmart IOS Marketing/04 Content Assets/Facebook/group-posts/` |
| A4 | Instagram launch post | Instagram | Caption + designed card brief + Reel brief (two deliverables in one file) | `RunSmart IOS Marketing/04 Content Assets/Instagram/launch-post-v1.md` |
| A5 | Reddit community posts | r/running, r/C25K, r/Garmin (3 variants) | Native Reddit format, no promotional language | `RunSmart IOS Marketing/04 Content Assets/Reddit/launch-posts/` |
| A6 | Product Hunt listing | Product Hunt | Name, tagline (≤60 chars), description (≤260 chars), maker first comment | `RunSmart IOS Marketing/04 Content Assets/ProductHunt/listing-v1.md` |
| A7 | Welcome lifecycle email | Gmail (RunSmart) | Plain-text, personal tone, no HTML template needed for v1 | `RunSmart IOS Marketing/04 Content Assets/Email/welcome-v1.md` |

**Asset-level writing notes:**

- **A1 (LinkedIn):** Founder voice. Story arc: problem I lived as a runner → why I built RunSmart → what it does in one sentence → call to download. No bullet lists. Ends with App Store link.
- **A2 (Facebook page):** Shorter than LinkedIn (100-120 words). Lead with the outcome, not the feature. Include a screenshot. App Store link in post.
- **A3 (Facebook groups):** Three variants targeting different intent clusters:
  - Beginner/C25K groups: "I just started running again and built this to keep me on track" angle
  - Garmin-focused groups: "Built something that actually uses your Garmin data to adjust your plan" angle
  - General running groups: "Adaptive AI training plans for runners who miss workouts" angle
  - Format rule: post as a runner, not as a founder. Link goes in first comment after initial engagement.
- **A4 (Instagram):** Two deliverables in one file:
  1. Caption (150-200 chars + hashtags): hook line, outcome, App Store CTA
  2. Designed card brief: what the visual should show (suggested: dark background, key stat or tagline, app icon). Canva-ready format.
  3. Reel brief: 15-30 second concept (screen recording of onboarding + plan generation, voiceover script)
- **A5 (Reddit):** Must feel native. No links in body text — App Store link goes in comments when asked. Lead with a personal running story or question, mention the app naturally. Separate version per sub for different angles.
- **A6 (Product Hunt):** Standard PH format. Tagline must describe the outcome, not the technology ("Your adaptive AI running coach" not "AI-powered running plan generator"). Maker comment: personal story + what makes it different from Strava/Runna.
- **A7 (Email):** Triggered after first onboarding completion. Single goal: confirm the plan was generated and set expectation for week 1. No upsell. Sign off as Nadav, not "The RunSmart Team."

### 4.2 Resumely (3 assets, secondary priority, staged)

These are staged drafts. Resumely submission is still pending, so these fire after that approval.

| ID | Asset | Channel | Format | Drive path |
|---|---|---|---|---|
| R1 | Founder launch post | LinkedIn | Skeleton draft (full copy pass after RunSmart launches) | `ResumeBuilder IOS Marketing/04 Content Assets/LinkedIn/launch-post-v1.md` |
| R2 | Community posts | Reddit (r/resumes, r/jobs) | 2 native variants | `ResumeBuilder IOS Marketing/04 Content Assets/Reddit/launch-posts/` |
| R3 | Welcome lifecycle email | Email (lifecycle) | Plain-text skeleton | `ResumeBuilder IOS Marketing/04 Content Assets/Email/welcome-v1.md` |

---

## 5. Track B — ASO Hardening (both apps)

### 5.1 Structure per app

Each app produces two documents:

**Audit doc** (`aso-audit-{date}.md`):
- Current listing: title, subtitle, top keywords, description (first 170 chars), screenshot titles
- Gap analysis: keyword density in title/subtitle vs. best practice, clarity of value prop in first sentence, presence of outcome language, social proof signals
- Competitor snapshot: 2-3 direct competitors, what their listings say, gaps we can exploit

**Rewrite doc** (`aso-rewrite-{date}.md`):
- Optimized title (max 30 chars): primary keyword + brand
- Optimized subtitle (max 30 chars): secondary keyword + differentiator
- Keyword strategy: top 10 targets (primary + long-tail) with rationale
- Optimized description: outcome-led first sentence, features as proof of outcome, no keyword stuffing
- Screenshot title copy (5 screens): each title acts as a standalone ad, ordered by persuasion arc

### 5.2 RunSmart keyword hypotheses (starting point for audit)

- Primary: "running coach", "run training plan", "5k training app"
- Differentiated: "adaptive running plan", "garmin running coach", "beginner running AI", "AI running coach"
- Long-tail: "marathon training plan app", "couch to 5k AI", "running plan that adapts"

### 5.3 Resumely keyword hypotheses (starting point for audit)

- Primary: "resume builder", "resume optimizer", "ATS resume app"
- Differentiated: "AI resume tailoring", "resume job description match", "ATS resume checker"
- Long-tail: "resume optimizer for job applications", "AI resume builder iPhone"

### 5.4 Drive paths

| App | Audit | Rewrite |
|---|---|---|
| RunSmart iOS | `RunSmart IOS Marketing/04 Content Assets/ASO Assets/aso-audit-2026-06-04.md` | `RunSmart IOS Marketing/04 Content Assets/ASO Assets/aso-rewrite-2026-06-04.md` |
| Resumely iOS | `ResumeBuilder IOS Marketing/04 Content Assets/ASO Assets/aso-audit-2026-06-04.md` | `ResumeBuilder IOS Marketing/04 Content Assets/ASO Assets/aso-rewrite-2026-06-04.md` |

**Constraint:** RunSmart listing changes must be submitted as part of an app update or standalone metadata-only submission. Timing: target submission alongside or immediately after v1.0.1 approval. Resumely: target before first submission if possible; otherwise as first post-launch update.

---

## 6. Infrastructure

### 6.1 Google Drive folders to create

These subfolders are missing from the current Drive tree (not in original `google-drive-map.md`):

```
RunSmart IOS Marketing/
  04 Content Assets/
    Facebook/
      group-posts/
    Instagram/
    Reddit/
    ProductHunt/

ResumeBuilder IOS Marketing/
  04 Content Assets/
    Reddit/
```

All other folders already exist per `data/google-drive-map.md`.

### 6.2 Notion rows

Every asset above gets a row created in the **Content/Asset Pipeline** database with:
- Product: RunSmart or ResumeBuilder
- Asset title: asset name from the tables above
- Channel: per asset
- Funnel stage: `acquisition`
- Status: `draft`
- Draft link: Google Drive path (URL after file is created)
- Approved?: unchecked until founder approves

One campaign row per product in the **Campaign Calendar**:
- RunSmart: `RunSmart — Launch Window Sprint`, status `drafting`, target publish date: `TBD (on Apple approval)`
- ResumeBuilder: `Resumely — Launch Window Sprint (Staged)`, status `drafting`, target publish date: `TBD (after submission + approval)`

The existing **Social Media Calendar** in Notion becomes the per-post publishing scheduler. Once an asset is approved, the founder adds a target publish date in the Social Media Calendar view. The Content/Asset Pipeline is the source of truth; the Social Media Calendar is the scheduling view.

### 6.3 Gmail (RunSmart)

The RunSmart Gmail account (the dedicated account referenced in the session — exact address to be confirmed by founder) is the `From` address for A7. For v1, the founder sends manually to the first cohort. No automation tooling. The email draft (A7) is written to be sent as-is from Gmail compose.

---

## 7. Work Packets

Three work packets implement this sprint:

| WP | Name | Priority | Contents |
|---|---|---|---|
| WP-3 | RunSmart Launch Window | High — time-gated | A1-A7 + Drive folder creation for RunSmart + Notion rows |
| WP-4 | ASO Hardening | High — evergreen | Both apps ASO audit + rewrite + Drive paths + Notion rows |
| WP-5 | Resumely Launch Window | Medium — staged | R1-R3 + Drive paths + Notion rows (secondary, fires after Resumely submission) |

Each work packet follows the format of WP-1 and WP-2 (`executive-os/work-packets/`): goal, context, read-first, tasks, deliverables, validation.

---

## 8. Approval Gates

| Gate | Asset scope | Who approves | How |
|---|---|---|---|
| Pre-publish review | Every asset | Founder | Add `Approved: yes — [date]` to asset file header in Drive |
| Social post | A1, A2, A3, A4, A5, R1, R2 | Founder | Founder posts manually; never auto-published |
| Email trigger | A7, R3 | Founder | Founder sends manually from Gmail for first cohort |
| App Store listing | Track B rewrites | Founder | Founder approves before submitting metadata change |
| Product Hunt | A6 | Founder | Founder triggers the PH listing on the day |

---

## 9. Success Criteria

- WP-3 done: all 7 RunSmart launch assets exist in Drive as `status: draft`, Notion rows populated
- WP-4 done: 4 ASO documents (2 audits + 2 rewrites) exist in Drive as `status: draft`
- WP-5 done: all 3 Resumely launch assets exist in Drive as `status: draft`
- Founder can approve and publish any asset within 30 minutes of reading it
- Nothing is published without `Approved: yes` in the file header

---

## 10. Open Questions

- What is the exact Gmail address for the RunSmart lifecycle email (from address)?
- Is there a Resumely Facebook page in the pipeline for post-launch, or confirmed LinkedIn + Reddit only for the foreseeable future?
- For the Instagram Reel brief (A4): should it reference real app footage (screen recording) or a conceptual animation? This affects whether Reel production is founder-dependent or agent-completable.
