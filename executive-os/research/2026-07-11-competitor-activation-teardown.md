# Research Brief: Live Competitor Activation Teardown (2026)

- Date: 2026-07-11
- Researcher / agent: Analysis OS via Grok live-web sprint (Cursor)
- Question (and why it matters now): What are top resume-builder and running-coach apps doing on 2026 first-run / activation, and what are users complaining about in recent App Store reviews and on X/Reddit — so we copy proven patterns onto RunSmart and Resumely instead of guessing while EXD-013 still holds (activation unproven; monetization/GTM locked).
- Tools available: web search / fetch — yes
- Our funnel anchors (internal, 2026-07-05 readout — do not treat as new measurement):
  - RunSmart: install → onboarding collapse (~95% drop); plan → run wall (0 runs in mature organic cohort)
  - Resumely: optimization → export wall (corrected: 8 clean uploads → 2 optimizations → **0 clean exports**)

---

## Activation Pattern Library (what works)

| Pattern | Who uses it | What it does | Copy for us? |
|---|---|---|---|
| **Pre-paywall personalization + value summary** | Runna | Long quiz (26–36 screens) builds a plan, then shows a summary of the user’s choices before a soft free-trial paywall | Partial — confidence + summary yes; full 36-screen length **no** for cold organic without brand |
| **Confidence over speed** | Runna | ~12 min onboarding optimizes for “I can do this race,” not fastest time-to-home | Yes for RunSmart copy/structure of the plan reveal |
| **Post-plan first-workout orientation** | Runna | After paywall/plan: race-time estimates, run-type guide with coach video, first easy run on the calendar | **Yes — primary RunSmart plan→run copy** |
| **Soft paywall + dismissible trial** | Runna | Free trial, annual highlighted, X-out available | Not now (EXD-013); park until Gate A |
| **Account + permissions, product free forever** | Nike Run Club | ~9-step account/profile/permissions; no paywall; Guided Runs/plans later | Free baseline sets category expectation; do not copy account-heavy flow without a product tour |
| **Hardware-native plan → watch sync** | Garmin Coach | Free coach plans inside Connect; aha is first synced workout on wrist | Analog for RunSmart: HealthKit / watch connect must sit on the path to first run (WP-40 already aimed here) |
| **Unlimited free usable export** | Teal | Unlimited PDF/DOCX downloads on free; gates AI depth / keyword depth, not first export | **Yes — primary Resumely export-break copy** |
| **Match score before apply** | Teal | Show competitiveness vs a job before submit | Yes as confidence step before/with export |
| **Import / AI / template entry paths** | Kickresume | New, AI-generate, Import PDF, Use Example — after account gate | Yes for Resumely entry; avoid account-before-value if possible |
| **Guest / free build then pay for depth** | Rezi (partial) | Free builder + scanner; lifetime PDF cap (3) | Builder-first yes; lifetime PDF cap **anti-pattern** |

## Complaint Theme Matrix (what fails)

| Theme | Running | Resume | Severity for activation |
|---|---|---|---|
| **Paywall before usable output** | Runna trial/cancel friction; Strava/Garmin locking year-recaps of *user’s own data* | Resume.io TXT-only free; Kickresume “upgrade to download” when premium options used; Rezi 3-lifetime PDF cap | Critical — kills trust at the exact aha moment |
| **Billing / cancel dark patterns** | Runna Trustpilot: hard cancel, continued billing | Resume.io: $2.95→~$30/4wk, refund window from signup not charge — dominates Reddit/Trustpilot | High — reputation; avoid entirely |
| **Long setup without early magic** | NRC: account-first, weak Guided Run / plan orientation | Kickresume: must register before exploring | High for cold installs (RunSmart install→onboarding) |
| **Plan rigidity / hardness** | Runna: beginners report too-hard workouts; want more easy days (Lifehacker / forums) | — | Medium — RunSmart safety/readiness wedge |
| **Tracking / sync bugs** | NRC: treadmill accuracy, audio ducking, Watch sync; Runna: sync edges | — | High for RunSmart first-run reliability |
| **Generic / unhelpful AI** | Strava Athlete Intelligence (Reddit study: tone, context, agency tensions) | Teal/Rezi/Kickresume: AI bullets feel generic; need heavy edit | Medium — do not oversell AI |
| **Rebuild / upload friction** | — | Rezi: removed easy existing-resume upload; rebuild from scratch | High for Resumely upload step |
| **Export / formatting bugs** | — | Kickresume Play reviews: PDF download errors; Rezi slow/buggy PDF | High — matches our export wall |

---

## 1. Facts

### Running coaches

1. Runna’s first-run is a long personalization funnel (documented at ~26–36 screens): goal/race → ability → days → prefs → optional strength → **plan summary → soft free-trial paywall → plan generation → coach welcome → run-types guide → home**. [S1][S2][S3][S4]
2. A Nov 2025 UX Collective teardown timed Runna onboarding at ~12 minutes and argued the product optimizes for **confidence**, not speed; post-onboarding includes estimated race times (with/without Runna), run-type explainers, and the first easy workout on the plan. [S4]
3. ScreensDesign (2026 product audit) describes Runna’s paywall as a **soft free-trial** after a pre-paywall value summary, with annual highlighted. [S2]
4. Lifehacker: Runna’s core value requires subscription; ~1-week free trial; Week 1 accessible; beginners on forums report plans can feel too hard / too few easy runs. [S5]
5. Trustpilot for runna.com surfaces recurring **billing/cancel** complaints (trial hard to cancel, continued charges). [S6]
6. Nike Run Club onboarding is short (~9 steps) and **account/permissions-centric**; product is fully free (no paywall). ScreensDesign notes onboarding misses orientation to Guided Runs / Plans. [S7]
7. A 2026-04-24 review intel pass on NRC lists top complaint themes: indoor/treadmill tracking inaccuracy, audio/music glitches, Watch sync pain, static plans vs adaptive competitors. App Store review samples echo indoor tracking and Watch sync. [S8][S9]
8. Strava put **Year in Sport 2025** behind Premium (~$80/yr); press + Reddit + X framed it as paying to see your own data. Athlete Intelligence drew Reddit criticism for generic AI summaries (academic analysis of r/Strava threads). [S10][S11][S12]
9. Garmin Coach remains a **free** plan builder inside Connect: pick distance/coach → mileage/pace → days → race date → create → **sync workout to watch**. Forum reports show race-date window / save bugs during setup. [S13][S14]
10. Garmin Connect **Rundown** (2025 year recap) requires Connect+; Reddit/press backlash mirrors Strava (paywall on packaged user data). [S15]

### Resume builders

11. Teal’s first-party positioning: unlimited resume create + **unlimited PDF/DOCX download free**; no “pay to export.” Paid Teal+ gates deeper AI / keyword analytics. Match Score vs a job is a core free confidence moment. [S16][S17]
12. 2026 reviews of Teal: free export praised; complaints cluster on Teal+ price / weekly billing default, cancel friction, generic AI, some ATS/export formatting issues. [S17][S18]
13. Rezi free plan: **3 PDF downloads for the life of the account** (not per month); AI limited; Pro ~$29/mo or Lifetime ~$149. Recurring complaints: download cap surprise, removed easy upload of existing resume (rebuild), generic AI, clunky UI. [S19][S20][S21]
14. Kickresume requires account before exploring. Entry paths: blank, AI, Import PDF, Example. Free download only if user avoids premium-marked options; otherwise **“upgrade to download”** (help article Dec 2025). Independent 2026 reviews say free users often hit watermark / non-PDF / section caps. [S22][S23][S24]
15. Resume.io free plan: **TXT-only download** (unusable for applications); PDF behind pay. Dominant complaint theme across Trustpilot / Reddit / 2026 reviews is **billing**: $2.95 trial auto-renews to ~$29.95 every 4 weeks; refund window from registration. [S25][S26]

### Our portfolio (internal)

16. As of 2026-07-05 activation reread: RunSmart mature organic D7 run activation **0/12**; Resumely clean D7 optimization activation **0/37**, with corrected all-time funnel guest→upload→optimize→export ending at **0 clean exports**. [S27]

## 2. Sources

| # | Source | Type | Reliability | Date |
|---|---|---|---|---|
| S1 | Revyl Atlas Runna screen map / onboarding flow | Secondary (flow audit) | Medium | accessed 2026-07-11 |
| S2 | ScreensDesign — Runna showcase (26 steps, soft trial paywall) | Secondary | Medium | accessed 2026-07-11 |
| S3 | LinkedIn / Atlas commentary — 36-screen Runna onboarding + sunk cost before paywall | Community | Low–Medium | accessed 2026-07-11 |
| S4 | Rosie Hoggmascall, UX Collective — “How to nail onboarding — Runna” | Secondary | High (detailed first-person teardown) | 2025-11-01 |
| S5 | Lifehacker — Runna review (trial, Week 1, beginner hardness) | Secondary | Medium–High | accessed 2026-07-11 |
| S6 | Trustpilot — runna.com | Community | Medium (selection bias) | accessed 2026-07-11 |
| S7 | ScreensDesign — Nike Run Club showcase | Secondary | Medium | accessed 2026-07-11 |
| S8 | Marlvel intel report — NRC 2026-04-24 | Secondary (review aggregation) | Medium | 2026-04-24 |
| S9 | Apple App Store — NRC reviews page samples | Primary / Community | Medium | accessed 2026-07-11 |
| S10 | Ars Technica / Gadgets & Wearables — Strava Year in Sport paywall | Secondary press | High | 2025-12 |
| S11 | User quotes on X cited in Ars (e.g. Dominik Sklyarov) | Community | Medium | 2025-12 |
| S12 | arXiv:2604.23830 — Reddit tensions with Strava AI feedback | Secondary research | High | 2026 |
| S13 | Wareable / Run Mummy Run — Garmin Coach setup guides | Secondary | High | accessed 2026-07-11 |
| S14 | Garmin forums — Coach race calendar / plan save issues | Community | Medium | accessed 2026-07-11 |
| S15 | Android Authority / NotebookCheck / Reddit coverage — Garmin Rundown paywall | Secondary + Community | High | 2025-12 |
| S16 | tealhq.com/tools/resume-builder (first-party free export claims) | Vendor / Primary | High for “what they claim”; Medium for conversion | accessed 2026-07-11 |
| S17 | AIToolsPolice — Teal Review 2026 | Secondary | Medium–High | 2026 |
| S18 | Trustpilot / ResumeCoach — Teal complaints | Community / Secondary | Medium | 2025–2026 |
| S19 | AIToolsPolice — Rezi Review 2026 | Secondary | Medium–High | 2026-06-20 (self-dated) |
| S20 | Trustpilot — rezi.io (“Overpriced Only 3 downloads…”) | Community | Medium | accessed 2026-07-11 |
| S21 | Curra / TealHQ post — Rezi upload removed, rebuild friction | Secondary / Community | Medium | accessed 2026-07-11 |
| S22 | Enhancv — Kickresume review (account gate, download paths) | Secondary (competitor blog — caution) | Medium | accessed 2026-07-11 |
| S23 | Kickresume Help — “What is upgrade to download?” | Primary | High | 2025-12-02 |
| S24 | SoundCV — Kickresume Review 2026 (free PDF limits) | Secondary (competitor — caution) | Medium | 2026 |
| S25 | AIToolsPolice / ResuFit / Enhancv — Resume.io 2026 | Secondary | Medium–High | 2026 |
| S26 | Trustpilot — resume.io (billing dominance) | Community | Medium | accessed 2026-07-11 |
| S27 | `executive-os/reviews/2026-07-05-activation-reread.md` | Internal | High | 2026-07-05 |

(Full claim-level detail in Evidence Table below.)

## 3. Assumptions

- US / English App Store + web reviews are a usable proxy for patterns; IL/Hebrew App Store nuance for Resumely is **unknown — need: Hebrew review scrape**.
- Screen counts from Atlas/ScreensDesign reflect recent live builds but were not re-verified on a physical device in this sprint.
- “Recent” complaints = roughly last 6–12 months of press/reviews; Year-in-Sport / Rundown spikes are late-2025 and still culturally active in 2026.
- Teal’s marketing claim of unlimited free PDF is treated as fact for competitive positioning; live account verification not performed.
- Kickresume mobile marketing claims “unlimited free export” in places; help docs + independent reviews show **conditional** free export — we treat the conditional model as the operational truth.
- Runna’s long onboarding works partly because of pre-install brand/community (Reddit ~47k members cited in S4); copying length without that brand will worsen RunSmart’s install→onboarding drop.

## 4. Insights

1. **Running category has split activation strategies:** Runna sells *belief + personalized plan* before money; NRC sells *free tracking/community* with weak first-run education; Garmin sells *watch-synced workout* as aha. RunSmart’s zero runs mean we are failing the Garmin-style aha (start a real run) more than the Runna-style “feel coached” aha.
2. **Do not cargo-cult Runna’s 36 screens.** Their length is a conversion machine *after* trust and acquisition already exist. For a low-awareness App Store install with a 95% onboarding drop, length is poison. Steal the **post-plan orientation** and **confidence copy**, not the quiz length.
3. **Category backlash is about gating the user’s own output.** Strava Year in Sport, Garmin Rundown, Resume.io PDF, Kickresume upgrade-to-download, Rezi’s 3 PDFs — same emotional crime. Resumely’s 0 clean exports is the same crime from the user’s point of view even if we did not intend a paywall.
4. **Teal won the resume activation narrative** by putting usable export in free forever and charging for AI *depth*. That matches our prior WP-2 pricing research and is the clearest Resumely fix pattern.
5. **NRC shows free ≠ activated.** Account/permissions without Guided Run / plan orientation leaves users in a feature swamp. RunSmart must end onboarding on a **single next action: start today’s (or next) run**.
6. **AI praise is fragile.** Across Strava AI and resume builders, users punish generic tone. Activation copy should promise a concrete artifact (plan workout / exportable resume), not “AI magic.”

## 5. Opportunities

See opportunity cards below. Ranked for activation only (EXD-013).

| Rank | Opportunity | Product | Funnel break | Score sum (Impact+Conf+Fit − Effort − Risk; Effort/Risk inverted as 6−x) |
|---|---|---|---|---|
| 1 | First free usable PDF after optimize | Resumely | optimize → export | Highest |
| 2 | Post-plan “first workout” hero + run-type explainer | RunSmart | plan → run | High |
| 3 | Defer account/permissions until after first value | Both | install → onboarding / guest → upload | High |
| 4 | Match/confidence reveal before export CTA | Resumely | optimize → export | Medium–High |
| 5 | Progressive profile (short first-run quiz) | RunSmart | install → onboarding | Medium |
| 6 | Explicit anti-patterns checklist for monetization later | Both | future paywall | Park until Gate A |

### Opportunity Card: Resumely first free PDF

- **Opportunity name:** Guaranteed first usable PDF export after optimization (Teal pattern)
- **Product:** Resumely iOS / ResumeBuilder Web
- **User problem:** Users who optimize still never leave with a file (0 clean `export_success`)
- **Evidence:** Facts 11–15, 16; Complaint matrix export row
- **Target user:** First-session organic job seekers
- **Business value:** Unlocks D7 activation definition (optimize is not enough if export is the real job-to-be-done)
- **Implementation complexity:** Low–Medium (UX + instrumentation; confirm no soft gate)
- **Data / API dependencies:** Existing export path; PostHog `export_success`
- **Revenue potential:** Indirect — required before any paywall credibility
- **Strategic fit:** EXD-013 activation-first; aligns WP-2 “never gate activation”
- **Risks:** Leaving export free forever must stay policy until Gate A; do not invent a trial PDF trap
- **Confidence:** High

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 5 | 5 | 2 | 2 | 5 | 2 |

**Recommended next step:** Open a scoped work packet: audit every path from `optimization_completed` → export CTA → file in Files app; remove friction; guarantee one free PDF.

### Opportunity Card: RunSmart first-workout hero

- **Opportunity name:** Post-plan first-workout hero CTA + run-type explainer (Runna post-onboarding pattern)
- **Product:** RunSmart iOS
- **User problem:** Users who get a plan never start a run
- **Evidence:** Facts 1–2, 16; Pattern library row “Post-plan first-workout”
- **Target user:** New installs who complete plan generation
- **Business value:** Directly attacks plan→run wall (0 `run_started`)
- **Implementation complexity:** Medium
- **Data / API dependencies:** Plan model; `run_started` / `run_completed`; HealthKit path (WP-40)
- **Revenue potential:** Indirect
- **Strategic fit:** CEO OKR D7 activation; pairs with WP-40 HealthKit in primary flow
- **Risks:** Adding another screen without a one-tap Start Run CTA recreates Runna length without Runna brand
- **Confidence:** High

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 5 | 4 | 3 | 2 | 5 | 2 |

**Recommended next step:** After WP-40 stories land, packet a single “Day 1 workout” surface: what / why / Start Run.

### Opportunity Card: Defer gates until after value

- **Opportunity name:** Value-first gating (account / HealthKit / paywall after aha)
- **Product:** RunSmart iOS / Resumely iOS
- **User problem:** Cold users abandon before seeing value (RunSmart onboarding drop; resume tools that demand signup first)
- **Evidence:** Facts 3, 6, 14; NRC/Kickresume account-first critique
- **Target user:** First-session organic
- **Business value:** More users reach the aha denominator
- **Implementation complexity:** Medium–High (auth, permissions, guest continuity)
- **Revenue potential:** Indirect
- **Strategic fit:** Activation-first
- **Risks:** Guest→account merge bugs; Apple permission best practices
- **Confidence:** Medium

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 4 | 3 | 4 | 2 | 5 | 3 |

**Recommended next step:** Audit current gate order vs “first value”; only change if a gate sits before aha.

### Opportunity Card: Match/confidence before export

- **Opportunity name:** Show fit/match confidence immediately before export CTA (Teal Match Score pattern)
- **Product:** Resumely iOS
- **User problem:** Optimize completes but users do not feel “done enough” to export
- **Evidence:** Fact 11; Insight 4
- **Target user:** Users who hit `optimization_completed`
- **Business value:** Raises export conversion without new AI cost
- **Implementation complexity:** Low if fit score already exists
- **Data / API dependencies:** Fit-check / match events already in funnel
- **Revenue potential:** Indirect
- **Strategic fit:** Activation; Fit-First lineage
- **Risks:** Score without export still fails the job-to-be-done
- **Confidence:** Medium

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 3 | 4 | 2 | 2 | 4 | 2 |

**Recommended next step:** Pair with Opportunity 1 — score + one-tap Export on same screen.

### Opportunity Card: Short progressive onboarding (RunSmart)

- **Opportunity name:** Progressive profile — 3–5 critical questions, rest later
- **Product:** RunSmart iOS
- **User problem:** Install → onboarding collapse
- **Evidence:** Facts 1–4 vs 6; Assumption on brand/length
- **Target user:** Cold App Store installs
- **Business value:** More users reach plan_generated
- **Implementation complexity:** Medium
- **Data / API dependencies:** Onboarding events
- **Revenue potential:** Indirect
- **Strategic fit:** Activation
- **Risks:** Weaker plan quality if too few inputs — mitigate with defaults + later edit
- **Confidence:** Medium

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 4 | 3 | 3 | 2 | 4 | 3 |

**Recommended next step:** Diff current onboarding step count vs “minimum to generate a safe Week 1 plan.”

## 6. Risks

- Copying Runna’s length without Runna’s brand worsens install→onboarding.
- Copying resume paywall patterns (Resume.io / Rezi caps) would cement Resumely’s export failure.
- Review sample bias: angry billing reviews dominate Trustpilot; underweights happy silent users.
- Device-unverified screen flows may be slightly stale vs live App Store builds.
- Monetization temptation: soft paywalls work for Runna *after* value — using them before our aha violates EXD-013.

## 7. Recommendations

1. **Resumely:** Treat “first free usable PDF after optimize” as non-negotiable activation policy (Teal). Ship friction audit + fix before any paywall work.
2. **RunSmart:** Steal Runna’s *post-plan* confidence kit (first workout hero, why this run, Start Run) and Garmin’s *sync-to-device-on-path* logic (WP-40), not Runna’s quiz length.
3. **Both:** Adopt an explicit anti-pattern list: TXT-only export, lifetime download caps, upgrade-to-download after sunk editing, paywalling “your own data” recaps, hard-to-cancel trials.
4. **Do not** unlock monetization experiments from this brief; EXD-013 stands until activation moves.

## 8. Open Questions

- Exact live screen count / copy on RunSmart and Resumely first-run vs competitors (device side-by-side) — **unknown — need: 30-min device teardown**.
- Whether Resumely’s export wall is discoverability, bug, Hebrew copy, or intentional premium gate — **unknown — need: WP-style export path audit** (partially in WP-36 lineage).
- Hebrew App Store complaint themes for Resumely competitors — **unknown**.
- Whether Runna still offers meaningful Week-1 free without trial account in all geos — **unknown — need: fresh install**.

## 9. Decision Needed

**Whether to open one activation work packet prioritizing Resumely first free PDF + export path audit** (Recommendation 1), with RunSmart first-workout hero queued behind WP-40.

---

**Confidence:** Medium–High — live web + primary help/vendor pages + internal readout; no device installs this sprint.
**Recommended next step:** Draft a work packet `WP-XX-resumely-first-free-export-activation` that audits `optimization_completed` → `export_success`, guarantees one usable free PDF, and instruments drop-offs — then run it after founder confirms (no build until approved).

---

## Evidence Table: Competitor activation claims

| Claim | Source | Source type | Reliability | Date | Evidence summary | Contradictions | Confidence | Implication |
|---|---|---|---|---|---|---|---|---|
| Runna onboarding is 26–36 screens ending in soft trial paywall after plan summary | S1 S2 S3 | Secondary / Community | Medium | 2026 | Atlas/ScreensDesign/LinkedIn agree on long funnel + soft paywall | Exact count varies 26 vs 36 | Medium | Pattern: sunk cost + summary before ask |
| Runna optimizes onboarding for confidence (~12 min); post-plan run-type guide + first easy run | S4 | Secondary | High | 2025-11 | Detailed UX teardown | Single author journey | High | Copy post-plan orientation, not length |
| Runna Week 1 / trial; beginners find plans hard | S5 | Secondary | Medium–High | 2026 | Lifehacker + forum notes | Pricing figures vary by region/time | Medium | Safety/easy-day wedge for RunSmart |
| Runna billing/cancel complaints common | S6 | Community | Medium | 2026 | Trustpilot themes | Happy users underrepresented | Medium | Avoid hard-cancel trials |
| NRC: short account onboarding, no paywall, weak feature orientation | S7 | Secondary | Medium | 2026 | ScreensDesign | Flow may change by platform | Medium | Free ≠ activated |
| NRC complaints: treadmill, audio, Watch sync | S8 S9 | Secondary / Community | Medium | 2026 | Aggregator + App Store samples | Not all recent | Medium | First-run reliability matters |
| Strava Year in Sport paywalled; Reddit/X anger | S10 S11 | Press / Community | High | 2025-12 | Multiple outlets | — | High | Don’t gate user’s own data |
| Strava AI feedback contested on Reddit | S12 | Research | High | 2026 | 297 threads analyzed | Academic, not App Store | High | Don’t overclaim AI coaching |
| Garmin Coach free; aha = synced watch workout | S13 | Secondary | High | 2026 | Setup guides | Requires Garmin hardware | High | Device connect on path to first run |
| Garmin Coach setup date/save friction | S14 | Community | Medium | 2026 | Forum thread | May be intermittent bugs | Medium | Setup bugs kill plan start |
| Garmin Rundown behind Connect+; backlash | S15 | Press / Community | High | 2025-12 | Parallel to Strava | — | High | Same anti-pattern |
| Teal: unlimited free PDF export; gate AI depth | S16 S17 | Vendor / Secondary | High / Medium–High | 2026 | First-party + reviews | Marketing emphasis | High | Best resume activation model |
| Teal+ price / cancel / generic AI complaints | S17 S18 | Secondary / Community | Medium | 2025–26 | Consistent themes | — | Medium | Charge depth not export |
| Rezi: 3 lifetime PDFs; upload removed; rebuild pain | S19 S20 S21 | Secondary / Community | Medium–High | 2026 | Multiple 2026 reviews | — | High | Anti-pattern for Resumely |
| Kickresume: account-first; upgrade-to-download if premium options | S22 S23 S24 | Mixed | Medium–High | 2025–26 | Help article confirms upgrade wall | Vendor pages claim freer exports | Medium | Conditional free = perceived trap |
| Resume.io: TXT free; trial billing dominates complaints | S25 S26 | Secondary / Community | High | 2026 | Consensus across sources | — | High | Never copy |
| RunSmart 0 D7 runs; Resumely 0 clean exports | S27 | Internal | High | 2026-07-05 | PostHog readout | Small n | High | Map copy to these breaks |

---

## Funnel map (pattern → our break)

| Pattern / anti-pattern | RunSmart install→onboarding | RunSmart plan→run | Resumely upload | Resumely optimize→export |
|---|---|---|---|---|
| Runna long quiz | Avoid for cold installs | — | — | — |
| Runna plan summary + confidence copy | Partial (short version) | Yes | — | — |
| Runna first-workout hero / run types | — | **Primary copy** | — | — |
| NRC account-first, no tour | Avoid | — | Avoid signup-before-value | — |
| Garmin sync-to-device aha | — | **Primary (WP-40)** | — | — |
| Teal unlimited free PDF | — | — | — | **Primary copy** |
| Teal match score | — | — | — | Yes with export CTA |
| Rezi 3-PDF / no upload | — | — | Avoid rebuild-only | Avoid caps |
| Kickresume upgrade-to-download | — | — | — | Avoid |
| Resume.io TXT / billing traps | — | — | — | Avoid |
| Strava/Garmin “pay for your data” | — | Avoid future recap gates | — | Avoid |

---

## Updates logged

- Research brief filed: `executive-os/research/2026-07-11-competitor-activation-teardown.md`
- Competitor scaffold watch notes: see companion one-line updates in distribution-os scaffolds (same day)
- No EXECUTIVE-DECISIONS change — decision still pending founder on WP open
