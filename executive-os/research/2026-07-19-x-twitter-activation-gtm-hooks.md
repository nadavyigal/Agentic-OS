# X/Twitter → Activation & GTM Hooks — Resumely + RunSmart

- **Date:** 2026-07-19
- **Session:** Portfolio HQ launch pad — “X/Twitter trend + user-language pass”
- **Objective:** Cluster current job-hunt / ATS / beginner-running pain into decision-ready activation + GTM hooks; name what not to claim.
- **Companion:** Extends (does not replace) `executive-os/research/2026-07-11-demand-mining-right-user-fit.md`
- **Status:** draft · founder review before any publish

## Methodology (honesty first)

| Source | Result |
|---|---|
| Native `x.com` search (Playwright) | **Login wall** — no native X posts captured this session |
| Reddit direct | Still unreliable/blocked for raw threads (same gap as 07-11) |
| Primary community | HealthUnlocked C25K (fresh pull); None to Run App Store–style quotes |
| 2026 press / category analysis | ATS “invisible not rejected,” ghost jobs, AI “resume soup” |
| Prior portfolio research | Blind ChatGPT language + Relph/BJSM study bank (07-11) |

**Rule for this brief:** Prefer attributable phrases. No invented tweets. Where X is cited as a *venue* (press says “TikTok/Reddit/Threads”), treat as secondary.

---

## Language clusters (evidence → phrase)

### Resumely / job search

| Cluster | Exact-ish phrases | Source |
|---|---|---|
| Silence ≠ personal failure | “The most frustrating part… is not rejection, it is silence.” | FastApply 2026 job-hunt essay [R1] |
| Invisible, not auto-rejected | “not rejected — they are invisible inside the system”; recruiters search ATS like a database | Economic Times / Reddit-developer ATS story [R2] |
| Fake “75% rejected” meme | Popular “75% auto-rejected by ATS” claim is debunked / vendor-era folklore | ResumeAdapter ATS stats 2026; FastApply [R3][R1] |
| Keyword gap (real wall) | Experience/skills don’t mirror JD wording; “missing exact-match keywords” | ResumeAdapter 10k-scan report [R4] |
| Pretty-resume penalty | Two-column / icons / “My Journey” headers scramble parse | Same ATS test narrative [R2] |
| Ghost jobs | “You applied to forty jobs… Zero replies… ghost jobs”; volume isn’t the strategy | Ghost-job roundups + LinkedIn-style posts [R5][R6] |
| AI slop / soup | “resume soup”; “complete AI dross”; “really obvious it was written by ChatGPT”; “flowery prose” | Aggregated recruiter Reddit + Blind (07-11) [R7][R8] |
| AI tells (copyable) | spearheaded / leveraged / synergy / dynamic / passionate; uniform bullets | AI-resume detection guides [R9] |

### RunSmart / beginner running

| Cluster | Exact-ish phrases | Source |
|---|---|---|
| Can’t do minute one | “I can’t manage the first 60 seconds!!”; “When I started I couldn’t run for 60sec” | HealthUnlocked “Literally can’t run” [S1] |
| Self-blame | “Feeling disheartened and defeated before I’d even started” | Same thread [S1] |
| Peer fix | “SLOW DOWWWWWWNNNN!!”; “C25K is about stamina, not speed”; “Doing too much too soon” | Mentors on same thread [S1] |
| Plan vs person | “the plan was failing them, not the other way around”; “too hard… too soon”; “I was failing W1D1. Over and over.” | None to Run [S2] |
| Identity block | “I’m not a runner. Those people are crazy.” / “too old, too heavy…” | None to Run success stories [S2] |
| Walk dignity | “Walking is not failing”; “run-walk is not just allowed, it’s smart” | Beginner-plan guides + HU culture [S3] |
| Aggressive AI-plan fear | Cautionary tales (stress fractures / shin splints / burnout) around race-aggressive coach apps | Women’s Running / The5KRunner via 07-11 [S4] |
| Study anchors (keep precise) | Only **27.3%** finished 9-week C25K (Relph 2023); single-run spike >10% of longest-in-30d raises overuse risk (Frandsen BJSM 2025) | Peer-reviewed [S5][S6] |

---

## 1) Resumely — activation + GTM hooks

Activation wall today (directional 07-19): people *do* upload/optimize; **export** is rare. Hooks must pull the right job (tailor → export for *this* role), not more “score theater.”

### Activation hooks (in-product / first session)

| # | Hook (user language) | Where it lands | Done when |
|---|---|---|---|
| A1 | “You’re not rejected — you’re invisible. Let’s make this posting find you.” | First job paste / fit-check screen | User pastes a real JD before upload |
| A2 | “Sound like you, not resume soup.” | Before/after optimize preview | User reviews one bullet and keeps/edits voice |
| A3 | “Keywords you already earned — just said differently.” | Diagnosis / match explanation | User sees 3 concrete JD↔resume gaps, not a vanity % |
| A4 | “Pretty layout can make you unreadable. Export something a parser can eat.” | Export CTA | `export_success` on first session |
| A5 | “One role. One tailored PDF. Volume is not the strategy.” | Post-export / second-job prompt | Second job started *after* first export |

### GTM hooks (external — draft only)

| # | Channel idea | Angle | Measurement |
|---|---|---|---|
| G1 | App Store / web hero | Anti-slop: tailor to *this* job without ChatGPT voice | Install → export (founder-excluded) |
| G2 | Free web ATS / fit tool | “Invisible check”: keyword + parse warnings → App Store CTA | Tool completers → install |
| G3 | Short social (LinkedIn/X when logged in) | Ghost-job / silence empathy → “stop spraying; tailor one” | Unique campaign link + PostHog |
| G4 | Hebrew ASO (when EXD-016 unparks) | Same anti-silence / anti-slop, local phrasing | Separate campaign IDs |

### Testable copy lines (approve before ship)

1. “Silence isn’t a verdict. Make your resume searchable for *this* job.”
2. “AI that keeps your voice — not another bowl of resume soup.”
3. “See the keyword gaps. Fix them. Export a clean PDF.”
4. “One tailored application beats twenty identical ones.”

---

## 2) RunSmart — activation + GTM hooks

Activation wall today: installs exist; **plan → run** dies. Hooks must reduce shame + make “today’s first easy win” the north star — not race aggression (wrong-fit traffic).

### Activation hooks (in-product / first session)

| # | Hook (user language) | Where it lands | Done when |
|---|---|---|---|
| B1 | “Can’t manage 60 seconds? That’s where we start — not where you fail.” | Onboarding first screen / empty goal | Onboarding completed without race-PB framing |
| B2 | “SLOW DOWN. Walk breaks are the plan.” | Plan preview + today workout | Plan generated with explicit walk-run dignity |
| B3 | “Open app → know today’s effort in 30 seconds.” | Today / home after auth | User reaches Today with a clear session |
| B4 | “First session ends with a win — not gasping.” | Pre-run / empty-state CTA | `run_started` then `run_completed` (any distance) |
| B5 | “If it feels too hard, the plan backs off — you don’t.” | Failure / skip / rest affordance | User can skip/rest without dead-end |

### GTM hooks (external — draft only)

| # | Channel idea | Angle | Measurement |
|---|---|---|---|
| H1 | App Store subtitle / first lines | Failure-friendly + walk-run; Relph/BJSM proof lines (exact wording) | Install → onboarding → plan → run |
| H2 | Comparison content (later) | Not “faster than Runna” — “gentler when you’re not feeling 100%” | Wrong-fit bounce rate proxy |
| H3 | Beginner communities (observe-only until founder okays post) | HU / C25K language: slow, repeat weeks, no shame | Qualitative only unless unique links exist |
| H4 | TikTok/Reels style (draft) | “W1D1 failing on loop” → app shows shorter intervals | Views ≠ activation; track App Store |

### Testable copy lines (approve before ship)

1. “If Couch to 5K felt too hard, start slower — on purpose.”
2. “Walk breaks aren’t cheating. They’re how beginners stick.”
3. “Only ~27% finish a classic 9-week C25K in one UK study. The plan should meet you halfway.”
4. “Today: one easy session. Not a race block.”

---

## 3) What NOT to claim

### Resumely — do not claim

| Claim | Why not |
|---|---|
| “75% of resumes are auto-rejected by ATS” | Debunked meme; damages trust with informed seekers/recruiters [R1][R3] |
| “Guarantees interviews / jobs” | Unprovable; ghost jobs exist outside the resume |
| “Beats ATS detectors / undetectable AI” | Wrong enemy; ATS isn’t an AI-writing detector [R9] |
| “Gameable Match Score = hireability” | Users already hate gameable scores; keep diagnostic |
| “We eliminate ghost jobs” | Out of product scope |
| Any unpaid activation % as proven lift | Mature D7 still 0/73 (07-12); 07-19 funnel is directional only |

### RunSmart — do not claim

| Claim | Why not |
|---|---|
| Medical / physio / injury-prevention guarantees | Not clinicians; N2R-style disclaimers apply |
| “Never get injured with RunSmart” | Unprovable; BJSM is risk association, not a product claim |
| Vague “follows the 10% rule” | Frandsen signal is **single-session vs longest-in-30d**, not classic weekly 10% |
| “Better than Runna for everyone” / elite PB machine | Wrong-fit magnet; injuries narrative cuts both ways |
| “Cures asthma / replaces doctor” | HU users need clinical caveats |
| Proven D7 activation % | Still 0/13 mature (07-12); directional funnel ≠ success story |

### Portfolio-wide — do not claim

- Paid ads or monetization before EXD-013 activation understanding
- Hebrew-first RunSmart distribution before EXD-016 unpark
- Native “viral on X” proof from this session (login wall — no posts captured)

---

## Decision pack (founder)

**Ship-now (low eng, high language fit)**  
1. Resumely: one App Store / web line from A2 + A4 (anti-soup + export).  
2. RunSmart: one App Store first-screen / subtitle from B1 + B2 (60-second dignity + walk breaks).  
3. Keep Match Score / plan preview copy diagnostic, never “guaranteed.”

**Do next session**  
- When X login is available: scrape 30 live posts each for `#jobsearch` / ATS silence and `#beginnerrunner` / C25K — replace secondary clusters with native quotes.  
- Draft full ASO variants (one per product) citing Relph/BJSM + anti-soup — founder approve before ASC edit.

**Park**  
- Community posting, paid boost, ghost-job detector features, race-comparison war pages.

**Confidence:** ~72% on language fit and “what not to claim”; ~40% that these hooks alone move activation without the plan→run / export product walls.

---

## Sources

| ID | Source | Type |
|---|---|---|
| R1 | FastApply — “Why Am I Not Hearing Back… 2026” | Secondary analysis |
| R2 | Economic Times — ATS developer test story | Secondary of Reddit primary |
| R3 | ResumeAdapter — ATS Statistics 2026 | Vendor analysis (useful on meme debunk) |
| R4 | ResumeAdapter — 2026 ATS Rejection Report | Vendor pipeline (label as such) |
| R5 | Jobeezy / MintCareer / HireFlow ghost-job guides 2026 | Secondary |
| R6 | LinkedIn-style “volume is not the strategy” posts | Secondary social |
| R7 | Applied AI Tools / Leon Consulting — Reddit recruiter AI-resume roundups | Secondary of Reddit |
| R8 | TeamBlind ChatGPT resume thread (via 07-11 brief) | Community primary |
| R9 | CVHive / Hiration AI-resume detection guides | Secondary |
| S1 | HealthUnlocked — “Literally can’t run” | Community primary |
| S2 | None to Run homepage + reviews (fetched 2026-07-19) | Vendor + hosted reviews |
| S3 | Beginner 5K plan guides (run-walk dignity) | Secondary |
| S4 | Women’s Running / The5KRunner (via 07-11) | Secondary press |
| S5 | Relph et al. IJERPH 2023 | Primary research |
| S6 | Frandsen et al. BJSM 2025 | Primary research |

---

## Updates logged

- Filed: `executive-os/research/2026-07-19-x-twitter-activation-gtm-hooks.md`
- Native X still a gap — do not pretend otherwise
- No EXD change; no external publish
