# Voice Coach Flip — STORM + Deep Research Brief

- Date: 2026-06-22
- Researcher: Analysis OS (Cursor cloud agent)
- Question: Flip `VOICE_COACH_ENABLED=true` in Vercel now that RunSmart iOS is live, or defer?
- Tools available: web fetch (GitHub public repo `nadavyigal/Running-coach-`), Agentic OS status files. PostHog MCP unavailable. iOS repo private — not readable.
- Workflow: STORM (`PROMPTS/storm-multi-perspective-research.md`) → fan-out deep research (`PROMPTS/analysis-research-sprint.md`)

---

# PHASE 1 — STORM Multi-Perspective Scan

**Topic:** Flip `VOICE_COACH_ENABLED` now vs defer — RunSmart iOS post-launch  
**Caller role:** CEO / Founder  
**Mode:** Ungrounded pass (Step 1–4); sub-7 claims escalated in Phase 2 below.

## STEP 1 — Five Perspectives

### Practitioner (daily runner)

**Position:** Voice coaching only matters if cues land while you are running outdoors with headphones, not in a simulator. A delayed or robotic cue mid-run breaks trust faster than silence. Runners forgive missing features; they do not forgive bad audio during a workout.

**Strongest evidence:** Agentic OS status — physical smoke passed for SIWA/onboarding but **voice coach untested on physical device** (`dashboard/status.json` risks). ASO copy does not promise live in-run voice (`distribution-os/projects/runsmart/scaffold/drafts/2026-05-27-rs-aso-001/description.txt`).

**Only this lens tells you:** The flip is invisible to users until someone runs with audio on a real phone on cellular; that is a different QA session than build-16 smoke.

### Academic (evidence vs belief)

**Position:** Habit formation research emphasizes timely, context-matched cues (implementation intentions). Voice can reinforce behavior if delivered at the right moment with low friction. There is no peer-reviewed evidence that adding TTS coaching at launch improves D7 retention for a pre-revenue app with ~16 users/week.

**Strongest evidence:** RunSmart onboarding review (2026-06-20): D7 retention **un-evaluable** on current volume; binding constraint is funnel volume, not feature depth (`distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-onboarding-review/onboarding-review.md`).

**Only this lens tells you:** Retention impact of voice cannot be validated until activation funnel carries volume; voice is not the current bottleneck.

### Skeptic (counterargument)

**Position:** Flipping before physical QA risks crashes, audio ducking failures, battery drain, and 503/500 errors surfacing to early adopters. The backend has no auth and no Pro gate — if iOS does not gate, you give away a planned paid feature for free while spend is uncapped at the app layer (only throttle + $30 OpenAI project cap).

**Strongest evidence:** Public route code — flag check only, no subscription verification (`v0/app/api/coach/voice-cue/route.ts`, GitHub `Running-coach-`). Monetization spec lists voice as **Pro only** (`executive-os/work-packets/WP-2-monetization-spec.md`).

**Only this lens tells you:** "Flip the flag" is not a 5-minute harmless toggle if the iOS client exposes voice to all users without a paywall.

### Economist (incentives and cost)

**Position:** At ~16 MAU, marginal TTS cost is likely cents per month if usage stays low; the real economic risk is (a) ungated Pro value before monetization, and (b) abuse bypassing in-memory throttle on serverless cold starts. Ring-fenced `OPENAI_VOICE_KEY` with ~$30/month cap limits downside.

**Strongest evidence:** `.env.example` documents dedicated key with ~$30/month budget cap; `estimateCueCostUsd()` in route; throttle 45s / 30 per hour per user/IP.

**Only this lens tells you:** Cost is **capped** at the infrastructure layer (~$30/mo) but **not** at product layer (free Pro feature leak).

### Historian (parallels)

**Position:** Shipping backend-enabled features behind flags before client QA is a common pattern (dark launch). Flipping the flag before device QA inverts the usual order: normally QA on staging with flag on, then prod. RunSmart already shipped iOS code with prod flag off — the parallel is "code complete, ops gate pending," similar to Garmin migration awaiting founder approval.

**Strongest evidence:** Prior exec posture: defer until physical voice QA (`executive-os/EXECUTIVE-DASHBOARD.md`, `DASHBOARD.md` decision board). App-live gate cleared 2026-06-19.

**Only this lens tells you:** The decision is no longer "before vs after App Store" — it is "before vs after a named QA session."

---

## STEP 2 — Contradiction Map

| Clash | Claim A | Claim B | Stronger side | Why |
|---|---|---|---|---|
| Speed vs safety | Flip now — differentiation while early users are forgiving | Defer — bad first voice experience poisons reviews | **B (safety)** until physical QA passes | No voice QA evidence; ASO does not promise voice |
| Retention vs focus | Voice helps second-run / D7 | Funnel volume is the binding constraint (77% never start onboarding) | **B (focus)** | Onboarding review: volume, not features |
| Cost vs value | Cost negligible at 16 users | Giving Pro voice free erodes future paywall | **Depends on iOS gating** | Server has no Pro check — unknown without iOS repo |
| Effort vs impact | Vercel flip is instant | QA + possible iOS fixes are not | **QA effort** | Flip is ops; unblock is QA |

**Question that resolves the biggest conflict:** Does physical-device voice QA pass on build 16 with acceptable latency and graceful failure?

**All lenses agree (likely true):**
- App is live; "don't flip before live" gate is cleared.
- Backend exists and is flag-gated.
- Physical voice QA has not been completed.
- Retention cannot be measured meaningfully at current volume.

**Blind spot none addressed:** Whether iOS client gates voice behind Pro or exposes it to all users when the backend is enabled.

---

## STEP 3 — Synthesis Briefing

### (a) CEO summary

RunSmart is live with voice coach code in the build but the Vercel flag off. The operational question is no longer launch timing — it is whether to enable a ring-fenced TTS endpoint before a 30-minute physical voice QA session. Cost exposure is bounded (~$30/month OpenAI cap + per-user throttle), but product exposure is not: the server does not enforce Pro, so flipping without confirming iOS gating gives away a planned paid feature. Retention upside from voice is speculative at ~16 users/week; the onboarding review shows the binding constraint is install-to-first-run volume, not coaching depth. **Default posture: defer flip until physical voice QA passes** — not because voice is unready in code, but because the only remaining hard gate is unverified real-world behavior. Garmin readiness can run in parallel; QA does not require an App Store submission.

### (b) Five key findings (ranked by reliability)

| # | Finding | Supporting | Challenging |
|---|---|---|---|
| 1 | App-live gate cleared; voice QA gate open | Historian, Practitioner, status files | — |
| 2 | Backend cost capped ~$30/mo + throttle | Economist, Phase 2 code | Skeptic (abuse on cold start) |
| 3 | No server-side Pro gate | Skeptic, monetization spec | Economist (if iOS gates) |
| 4 | Retention impact unmeasurable now | Academic, onboarding review | Practitioner (voice as differentiator) |
| 5 | No documented latency SLO | Skeptic, Practitioner | — |

### (c) Hidden connection

Economist and Skeptic align on a product risk the Practitioner lens frames as UX: **the flag is a monetization and trust lever, not just an ops switch.** Enabling the backend without client Pro gating converts a future paywall feature into a free cost center.

### (d) Action for CEO

Schedule one physical-device voice QA session (outdoor run, headphones, cellular) on build 16 **before** approving the Vercel flip. Parallel: confirm iOS Pro gating behavior in the private repo. Do not block Garmin Story 1 on this — sequence QA, then flip in the same week if pass.

### (e) Frontier question

Would voice cues arriving >8 seconds after the trigger still feel like coaching, or like a podcast interruption?

---

## STEP 4 — Peer Review

| Finding | Confidence | Reason |
|---|---|---|
| App live, flag off | 9/10 | Multiple status sources, dated 2026-06-19 |
| Physical voice QA not done | 9/10 | `dashboard/status.json` risks |
| ~$30/mo hard cap on voice key | 8/10 | `.env.example` + route comments; cap is OpenAI project config, not code-enforced |
| Per-cue cost ~$0.001–0.003 | 7/10 | `estimateCueCostUsd()` in route; depends on cue length |
| Throttle limits abuse | 6/10 | Unit tests exist; in-memory per-instance caveat documented in code |
| Latency acceptable in-run | 3/10 | No SLO, no device measurement |
| Voice improves D7 retention | 2/10 | No voice events; volume too low |
| iOS gates Pro correctly | 2/10 | iOS repo not accessible |
| Simulator QA sufficient | 2/10 | Practitioner + status explicit on physical gap |

**Weakest link:** In-run latency on cellular — needs physical measurement.

**Overrepresented lens:** Skeptic (appropriate for pre-flip decision).

**Missing 6th angle — Legal/compliance:** App Store metadata does not claim live voice coaching; low review risk if flag stays off. If flipped, ensure no marketing overclaim.

**Overall grade:** C+ as a decision-ready brief before Phase 2 — strong on gates and cost ceiling, weak on latency and iOS client behavior.

### Sub-7 claims (escalated to Phase 2)

1. TTS cost is negligible at current scale
2. Rate limits cap spend reliably under abuse
3. Cues arrive fast enough during a run (latency)
4. Prefetch/caching makes latency a non-issue
5. Voice coach improves D7 / second-run retention
6. Shipping voice helps ASO / early reviews
7. Simulator-tested voice is good enough
8. iOS client gates voice behind Pro when backend is on

---

# PHASE 2 — Deep Research (Grounded)

## Evidence Table

| Claim | Source | Type | Reliability | Date | Summary | Contradictions | Confidence | Implication |
|---|---|---|---|---|---|---|---|---|
| Flag returns 503 when not `"true"` | `v0/app/api/coach/voice-cue/route.ts` (GitHub) | Primary (code) | High | 2026-06-21 | `VOICE_COACH_ENABLED !== "true"` → 503 JSON | — | 10/10 | Flip is instant enable |
| TTS = OpenAI `tts-1`, voice `nova`, AAC | Same route | Primary | High | 2026-06-21 | Sequential GPT-4o-mini then TTS fetch | — | 10/10 | Latency = sum of two API calls |
| Cue text max ~25 words, 60 tokens | Route `COACH_SYSTEM_PROMPT` | Primary | High | 2026-06-21 | Short cues | — | 9/10 | ~80–150 chars typical |
| `estimateCueCostUsd`: $15/1M chars TTS + $0.00005 text | Route helper | Primary | High | 2026-06-21 | ~$0.0015–0.003/cue at typical length | OpenAI list price should be verified periodically | 8/10 | See cost model below |
| Throttle: 45s min interval, 30/hr per key | `voice-cue-throttle.ts` | Primary | High | 2026-06-21 | Per userId or IP | In-memory, per serverless instance | 7/10 | Abuse guard, not hard spend cap |
| 6 throttle unit tests pass | `voice-cue-throttle.test.ts` | Primary | High | 2026-06-21 | Vitest coverage for throttle only | No route integration tests | 8/10 | B1 partially validated |
| No route integration tests | Absence in repo | Primary | High | 2026-06-22 | `route.test.ts` does not exist | Dashboard noted "Unknown for B1" | 9/10 | GPT+TTS path unautomated |
| ~$30/mo budget on `OPENAI_VOICE_KEY` | `v0/.env.example` | Internal doc | Medium | 2026-06-21 | Comment only; OpenAI project config | Not enforced in application code | 7/10 | Hard ceiling if configured in OpenAI dashboard |
| No auth / no Pro check on route | Route code | Primary | High | 2026-06-21 | Only flag + throttle | Monetization spec says Pro-only | 10/10 | Product gating must be iOS-side |
| Voice = Pro in monetization spec | `WP-2-monetization-spec.md` | Internal | High | 2026-06-04 | Free vs paid matrix | Server does not enforce | 9/10 | Flip may leak Pro value |
| Paywall not live (EXD-009) | `EXECUTIVE-DASHBOARD.md` | Internal | High | 2026-06-21 | Monetize after D7 readout | — | 9/10 | No revenue offset for voice cost |
| ~16 users/7d | `EXECUTIVE-DASHBOARD.md` | Internal | Medium | 2026-06-21 | Early PostHog | — | 6/10 | Cost model input |
| D7 retention un-evaluable | Onboarding review | Internal (PostHog) | Medium | 2026-06-20 | 44 launches / 90d | — | 8/10 | Cannot A/B voice impact |
| No voice events in iOS analytics list | `dashboard/status.json` | Internal | High | 2026-06-21 | Activation events listed; no `voice_cue_*` client events | Server logs `voice_cue_served` | 8/10 | Retention angle not instrumented on client |
| Physical voice QA not done | `dashboard/status.json` risks | Internal | High | 2026-06-21 | Explicit risk | Build 16 smoke passed other flows | 9/10 | Blocks safe flip |
| Rollback = set flag false in Vercel | Route 503 behavior | Primary | High | 2026-06-22 | Instant backend disable | iOS may show errors if no graceful degrade | 8/10 | Rollback is fast |
| OpenAI tts-1 pricing $15/1M chars | Route comment + historical OpenAI docs | Vendor | Medium | 2026-06-22 | Matches code assumption | Pricing page did not surface tts-1 in fetch | 7/10 | Aligns with estimate function |
| Runna gates adaptive coaching paid; voice depth in market | `WP-2-competitor-pricing-research.md` | Secondary | Medium | 2026-06-04 | Competitor context | NRC free baseline | 6/10 | Voice is premium market norm |
| No latency SLO in spec or code | Absence | — | High | 2026-06-22 | No p50/p95 targets | — | 10/10 | Must derive from measurement |

---

## Angle 1 — Cost Model

**Formula (from route):**

```
cost_per_cue ≈ (cue_chars / 1_000_000) × $15 + $0.00005
```

**Assumptions:**

| Variable | Low | Mid | High |
|---|---|---|---|
| Chars per cue | 80 | 120 | 150 |
| Cues per run | 3 | 8 | 20 |
| Runs per active user / month | 2 | 4 | 8 |

**Per-cue cost (mid):** (120/1e6)×15 + 0.00005 ≈ **$0.00185**

**Monthly projection (before caps):**

| MAU | Mid usage (8 cues × 4 runs) | Notes |
|---|---|---|
| 16 | ~$0.95/mo | Below noise |
| 100 | ~$5.90/mo | Still low |
| 1,000 | ~$59/mo | Exceeds $30 key cap → cues start failing when budget hit |

**Ceilings:**

1. **Application:** 30 cues/hr/user → max ~$0.056/hr/user at mid cue cost
2. **Infrastructure:** ~$30/mo on dedicated OpenAI project (`OPENAI_VOICE_KEY`)

**Verdict (Claim 1 — negligible cost):** **VERIFIED at current scale** (confidence 8/10). At 1k MAU with heavy use, **hard cap binds** — users would see 500 errors, not unbounded bill.

**Verdict (Claim 2 — rate limits cap spend):** **PARTIALLY VERIFIED** (confidence 7/10). Throttle + $30 cap provide defense-in-depth; in-memory throttle is not a perfect abuse barrier on serverless.

---

## Angle 2 — Latency

**Architecture:** Synchronous chain — JSON parse → throttle → `generateText` (gpt-4o-mini, max 60 tokens) → OpenAI TTS HTTP → AAC buffer returned. No streaming. `Cache-Control: no-store`.

**Implicit client constraint:** Server enforces 45s minimum between cues; client should not poll faster.

**No documented SLO** in sprint 11 plan (iOS repo not readable) or web route.

**Reasoned budget (not measured — needs physical QA):**

| Segment | Typical range |
|---|---|
| GPT-4o-mini text | 0.5–3s |
| TTS generation | 1–4s |
| Network (cellular) | 0.5–3s |
| **End-to-end p50 (estimate)** | **2–6s** |
| **End-to-end p95 (estimate)** | **6–12s** |

**Usability heuristic:** Pace/distance cues remain relevant for ~30–60s during steady running. p50 under ~5s is likely acceptable; p95 over ~10s risks feeling late.

**Verdict (Claim 3 — fast enough):** **UNVERIFIED** (confidence 3/10). Needs physical device timestamps.

**Verdict (Claim 4 — prefetch fixes latency):** **UNVERIFIED** (confidence 2/10). Route returns `no-store`; no server-side prefetch. iOS prefetch unknown without repo.

**Measurement plan (founder QA session):**

1. Enable flag on Vercel preview or prod with test user
2. Outdoor run, cellular only, log: tap/trigger → HTTP response → audio start
3. Record 5 cues; compute p50/p95
4. Pass if p50 < 6s and no playback failures; fail if p95 > 12s or crash

---

## Angle 3 — Retention & Monetization

**Internal data:**

- PostHog project 171597: 44 `app_launched` / 90d, 1 `run_completed` — retention gate un-evaluable (onboarding review 2026-06-20)
- iOS wired events (`dashboard/status.json`): no voice-specific client events listed
- Server emits `voice_cue_served` and `voice_cue_throttled` via PostHog server capture

**Monetization:**

- Voice coach = **Pro only** in `WP-2-monetization-spec.md`
- Paywall implementation deferred (EXD-009)
- Server has **no** subscription check

**Competitor context (secondary):**

- Runna charges for adaptive coaching depth ($120/yr); audio coaching is part of premium coaching apps
- Nike Run Club free sets baseline; voice is not required for activation

**Verdict (Claim 5 — D7/retention lift):** **REFUTED as measurable today** (confidence 2/10). Volume and instrumentation insufficient. Hypothesis remains possible but not actionable.

**Verdict (Claim 6 — ASO/review benefit):** **UNVERIFIED** (confidence 3/10). ASO copy does not mention live voice; early review count unknown. No evidence flip improves acquisition.

**Verdict (Claim 8 — iOS Pro gating):** **UNVERIFIED** (confidence 2/10). Must inspect iOS repo before flip.

---

## Angle 4 — QA & Rollback

### Go/no-go checklist

| Check | Status | Evidence |
|---|---|---|
| App live on App Store | PASS | 2026-06-19 build 16 |
| Backend route deployed | PASS | `Running-coach-` main |
| Throttle unit tests | PASS | 6/6 vitest |
| Route integration tests | FAIL | Missing |
| Physical device voice QA | **FAIL** | `dashboard/status.json` risk |
| Pro gating confirmed on iOS | **UNKNOWN** | iOS repo private |
| Rollback path | PASS | Flag → 503 |
| iOS graceful degrade on 503 | **UNKNOWN** | Needs iOS repo |
| ASO overclaim risk | PASS | Description does not promise live voice |

### Rollback procedure

1. Set `VOICE_COACH_ENABLED=false` in Vercel production env
2. Redeploy not required for env-only change on Vercel (immediate on next request)
3. Verify POST `/api/coach/voice-cue` returns 503
4. Monitor PostHog `voice_cue_served` drops to zero

**Verdict (Claim 7 — simulator sufficient):** **REFUTED** (confidence 8/10). Status and Practitioner lens require physical audio + cellular.

---

# PHASE 3 — Decision Memo

## Recommendation: **DEFER flip until physical voice QA passes** (conditional, not indefinite)

### Rationale

| Factor | Now | After QA pass |
|---|---|---|
| Cost risk | Low (capped ~$30/mo) | Same |
| Product risk | Medium (Pro leak if iOS ungated) | Low if gating confirmed |
| UX risk | **High** (untested on device) | Acceptable if latency pass |
| Retention upside | Not measurable | Still not measurable — do not flip *for* retention |
| Garmin train | Unaffected | Unaffected |

Flipping now optimizes for **speculative differentiation** at the cost of **verified trust**. The executive posture already aligned on defer (`EXECUTIVE-DASHBOARD.md`); Phase 2 grounding **confirms** that posture — it does not overturn it.

### Conditional flip criteria (all required)

1. Physical-device QA pass on build 16 (audio plays, no crash, cellular)
2. Latency p50 < 6s on 5+ cues (founder-measured)
3. iOS Pro gating confirmed OR founder explicitly accepts free voice temporarily
4. Founder explicit "yes" to Vercel production env change

### Smallest next work packet

**Title:** RunSmart iOS — Physical Voice QA (30 min)  
**Repo:** RunSmart iOS local  
**Steps:**

1. Read `docs/superpowers/plans/2026-06-01-sprint-11-ux-voice-coach.md` acceptance criteria
2. Set `VOICE_COACH_ENABLED=true` on Vercel **preview** or prod (founder approval)
3. Real iPhone, outdoor run, headphones, cellular — trigger ≥5 cues
4. Log pass/fail per: audio start, ducking, latency, 503/500 handling
5. If pass → founder approves prod flip; if fail → file iOS/web fix, keep flag off

**Do not:** Block Garmin Story 1; run QA in parallel.

### What NOT to do

- Do not flip for retention — data cannot support it
- Do not assume simulator coverage
- Do not implement paywall in same session as flip (EXD-009 still gates monetization)

---

## Facts / Assumptions / Open Questions

### Facts (sourced)

- Live app, flag off, voice code in build
- Public backend implementation audited from `nadavyigal/Running-coach-`
- Cost model and caps documented in code + `.env.example`
- Physical voice QA explicitly outstanding

### Assumptions

- iOS client calls `/api/coach/voice-cue` when user starts a run (per WP-2 packet; not verified in Swift)
- OpenAI `tts-1` pricing remains ~$15/1M characters (route comment)

### Open questions

1. Does iOS gate voice behind Pro today?
2. Does iOS degrade gracefully on 503?
3. What is measured p50/p95 latency on cellular?
4. Are client-side `voice_cue_*` PostHog events wired?

---

**Confidence:** **Medium-High** on defer recommendation; **Low** on retention and latency claims until device QA.

**Recommended next step:** Run the 30-minute physical voice QA work packet; re-evaluate flip same day if pass.

**Decision needed:** Founder approval to (a) run QA with flag on preview/prod, then (b) flip prod if pass.

---

## Changelog

- 2026-06-22: Initial STORM + deep research brief. Sources: public `Running-coach-` repo, Agentic OS status, executive monetization spec, onboarding review.
