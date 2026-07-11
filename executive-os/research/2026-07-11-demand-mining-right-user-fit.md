# Research Brief: Right-User Demand Mining for Fit (RunSmart + Resumely)

- Date: 2026-07-11 (upgraded same day — Grok live-web pass)
- Researcher / agent: Cursor/Grok (Analysis OS)
- Question (and why it matters now): Where do the actual target users for RunSmart and Resumely gather, and what exact language do they use — so ASO copy and acquisition targeting attract users who fit the product instead of diluting activation with wrong-fit installs. This attacks RunSmart’s **~94.7% install→onboarding drop** from the “wrong traffic” angle funnel UX work cannot reach. Companion to `2026-07-11-competitor-activation-teardown.md`.
- Tools available: web search / fetch — **yes**. Direct `reddit.com` and `x.com` remain **network-blocked** in this environment (confirmed 2026-07-11 via WebFetch + curl JSON). Primary community text obtained from **HealthUnlocked**, **TeamBlind**, peer-reviewed papers, and press that cites Reddit/TikTok/Threads with named outlets (WSJ). Secondary aggregators kept only when labeled.

## Methodology Note

| Attempt | Result |
|---|---|
| `reddit.com` / `old.reddit.com` / Reddit JSON API | Blocked (“network policy” / login wall) |
| PullPush / Arctic Shift archives | 404 / 502 / bad params — no usable posts |
| `x.com` direct | Not obtained — gap |
| HealthUnlocked C25K forum | **Primary posts retrieved** |
| TeamBlind resume threads | **Primary posts retrieved** |
| Peer-reviewed studies (IJERPH 2023, BJSM 2025) | **Primary papers retrieved** |
| Press citing Reddit/TikTok/WSJ (Women’s Running, The5KRunner) | Secondary with attributable claims |

Earlier draft of this file (Claude, same day) correctly flagged weaker evidence. This upgrade **replaces paraphrased Reddit quotes with primary forum text where available**, **corrects the 10% rule to the BJSM single-session definition**, and **does not invent X quotes**. Remaining Reddit/X gaps stay labeled gaps.

---

## 1. Facts

### RunSmart — where right-fit users gather

1. **Named gathering places (beginner / returning / injury-aware):** r/running, r/C25K, r/Runna (named in press as injury-debate venue), HealthUnlocked Couch to 5K (~137k members), RunningAhead / Runners Forum / LetsRun (directory-level), TikTok/Threads (cited as cautionary-tale venues for AI plan aggression). [S1][S5][S6][S7]
2. **IJERPH 2023 (Relph et al.):** only **27.3% completed** a 9-week Couch-to-5K programme (n=110 UK beginners). Drop-out themes from interviews: MSK injury, negative emotions tied to non-completion, and **programme design / progression**. Previous injury predicted non-completion (OR 7.56). [S2]
3. **BJSM 2025 (Frandsen et al., Garmin-Runsafe, n=5,205):** overuse injury rate rises when a **single session** exceeds **10% of the longest run in the past 30 days** (small spike HRR 1.64; large spike >100% HRR 2.28). Week-to-week and classic ACWR spikes were **not** the predictive signal — the single “monster run” was. [S3]
4. **Primary HealthUnlocked language (C25K community):** users repeatedly title posts *“Harder than I thought”*; Week 7 called out as the first week **with no walk breaks** — “mentally that’s a challenge”; peers advise repeat weeks, rest, strength work; one recovering poster: physio advice is “about getting stronger to stop it recurring.” [S4]
5. **Primary / dated user-review language (None to Run page, cites App Store-style reviews):** “I tried couch to 5k plans but it was **too hard**” (2025-11-19); “other couch to 5K apps… starting with alternating **1 min run–1 min walks… not attainable**” (2025-06-11); “**Couch to 5 k made me feel like a failure**”; “always ended up **getting injured**”; “**more aggressive** couch to 5K plans”; “I can’t run for a minute straight.” [S5]
6. **Press + clinician echo of social channels (not primary Reddit text):** Women’s Running (2026-06-29) reports a “steady stream of cautionary tales on **TikTok and Reddit**” about Runna (stress fractures, shin splints, burnout); cites **Wall Street Journal** PTs seeing multiple injured Runna users per week; notes Runna rolled out **less aggressive** beginner plans in Jan 2026 and a **‘Not Feeling 100%’** adapt feature. The5KRunner (2026-02-21) same WSJ claim + notes anecdotes on TikTok/Reddit/Threads are “real, but unproven” vs peer review. [S6][S7]
7. **Wrong-fit vs right-fit signal:** race-goal / aggressive-plan users are already served (and sometimes injured) by Runna-class apps; the underserved voice in primary beginner forums is **load fear + walk-run dignity + “don’t make me feel like a failure.”** Runna already ships Post-Injury / Return to Running / Not Feeling 100% — differentiation must be sharper than “we also do returning runners.” [S6][S8]

### Resumely — where right-fit users gather

8. **Named gathering places:** r/resumes, r/jobs, r/careerguidance, r/GetEmployed, r/cscareerquestions, r/recruiting, r/linkedin (directory + aggregator consensus); **TeamBlind** (tech professionals — primary threads retrieved). [S9][S10]
9. **Primary Blind language on ChatGPT resumes:** “Every time I’ve attempted this it’s been **really obvious it was written by ChatGPT**”; another: ChatGPT “Doesn’t listen… use less **flowery prose**”; opposing camp claims better response rates if you still human-edit. [S10]
10. **Blind recruiter-style formatting language (compiled Blind guide):** “Your resume isn’t an art project—it’s a document that needs to be quickly scannable and **ATS-friendly**”; reject tables/columns/icons; plain-text round-trip test. [S11]
11. **Secondary (still unverified against original Reddit posts):** aggregator quotes of r/resumes-type complaints — “It just added **buzzwords** and made my resume sound like everyone else’s”; tools that “look free but charge **$20+/month** for basic exports”; Resume Worded scoring called **“gameable.”** Kept as Medium reliability only. [S9]
12. Positive tool names in the same secondary roundup: Teal, Kickresume, Rezi, Jobscan — aligns with competitor teardown free-export patterns. [S9]

### Internal funnel anchor (not new measurement)

13. RunSmart mature organic: install→onboarding collapse (~94.7% drop); plan→run wall. Resumely: optimize→export wall (0 clean exports). Source: `executive-os/reviews/2026-07-05-activation-reread.md`. Wrong-fit traffic is a **hypothesis** for the onboarding drop, not a proven causal split.

---

## 2. Sources

| # | Source | Type | Reliability | Date |
|---|---|---|---|---|
| S1 | Feedspot / distribution scaffolds — running forum directories | Secondary | Medium | 2026-07-11 |
| S2 | Relph et al., *Int. J. Environ. Res. Public Health* 2023, 20, 6682 (PMC10487403 / DOI 10.3390/ijerph20176682) | Primary research | High | 2023-08 |
| S3 | Frandsen et al., *Br J Sports Med* 2025;59:1203 (PubMed 40623829) | Primary research | High | 2025 |
| S4 | HealthUnlocked — Couch to 5K post “Harder than I thought” + replies | Community primary | High for language; Low for prevalence | accessed 2026-07-11 (thread ~3y old; pattern still live in related “harder than I thought” titles) |
| S5 | None to Run — “Couch to 5K Alternative… (2026)” with dated user quotes | Vendor page hosting user quotes | Medium–High (quotes dated; vendor selection bias) | accessed 2026-07-11 |
| S6 | Women’s Running — “Should you let ChatGPT plan your training?” | Secondary press | Medium–High | 2026-06-29 |
| S7 | The5KRunner — “Is Your Runna AI Marathon Training Plan Pushing You Towards Injury?” | Secondary | Medium–High | 2026-02-21 |
| S8 | Runna — Post-Injury plan marketing / feature claims | Vendor | High for “what they claim” | accessed 2026-07-11 |
| S9 | Resume Optimizer Pro — “Best AI Resume Builder Reddit (2026)” | Secondary aggregator | Medium (quotes not re-verified on Reddit) | accessed 2026-07-11 |
| S10 | TeamBlind — “Using ChatGPT to optimize resume?” | Community primary | High for language | 2023-07-21 (older; pattern still cited in 2025–26 guides) |
| S11 | TeamBlind — Software Engineer / PM resume guides compiling Blind advice | Secondary of primary | Medium–High | 2025 |

**Still not obtained:** direct Reddit thread bodies; any native X/Twitter posts; Hebrew job-seeker forums for Resumely.

---

## 3. Assumptions

- HealthUnlocked + App Store review language is a usable proxy for r/C25K vocabulary while Reddit stays blocked.
- “Wrong-fit” for RunSmart ≈ users seeking aggressive race-block / PB-max plans who will bounce when the product leads with readiness/safety; “right-fit” ≈ beginners, returning-from-break, injury-anxious, walk-run-friendly.
- Blind (tech) language generalizes partially to Resumely’s broader job-seeker audience — not to all Hebrew/IL users.
- Folding study stats into ASO does not require App Store legal review beyond ordinary substantiation (founder should still verify claim wording).

---

## 4. Insights

1. **Wrong-traffic angle is real and named in user language.** Right-fit runners say *too hard / too aggressive / felt like a failure / getting injured / can’t run a minute / need walk breaks*. ASO that promises “crush your marathon PB” pulls the opposite cohort into a readiness-first product — then onboarding looks “broken” when they leave.
2. **Study hooks are stronger than vibes — and must be worded precisely.** Lead with “only ~27% finish a 9-week C25K in Relph 2023” and “single-run spikes >10% vs your longest run in 30 days raise overuse risk (Frandsen 2025)” — **not** a vague “10% weekly rule,” which the BJSM paper did not support as the key predictor.
3. **Social proof of the category problem already exists without Reddit scrape:** WSJ + Women’s Running + The5KRunner document TikTok/Reddit injury narratives around aggressive AI plans. RunSmart can position as the plan that **backs off**, not the plan that brags hardest.
4. **Runna occupies “returning runner” brand space.** Compete on *daily readiness / conversational coaching / never make you feel like a failure*, not on owning “post-injury” as a label.
5. **Resumely right-fit language is anti-generic-AI and anti-bait-free.** Blind: “obviously ChatGPT,” “flowery prose.” Secondary Reddit: buzzwords, gameable scores, $20+/mo export traps. Match Score must stay diagnostic, not gameable; export must stay usable (ties to teardown).

---

## Language bank (copy-ready — cite before shipping)

### RunSmart — attract (right-fit)

| Phrase cluster | Source type |
|---|---|
| “too hard” / “too aggressive” / “way too intense” | S5 primary-ish user reviews |
| “made me feel like a failure” | S5 |
| “can’t run for a minute straight” / “not attainable” | S5 |
| “Harder than I thought” / Week 7 “no walk breaks” | S4 primary forum |
| “getting injured” / shin splints / stress fracture (category fear) | S5 S6 S7 |
| “Not Feeling 100%” (competitor feature name — paraphrase, don’t trademark-claim) | S6 |
| “consistency, not performance” / conversational pace | S5 + coaching consensus |

### RunSmart — ASO proof lines (substantiated)

- “In a UK beginner study, only 27.3% finished a 9-week Couch-to-5K programme.” — S2
- “Injury risk jumps when one run is >10% longer than your longest run in the last 30 days (5,205-runner BJSM study).” — S3

### RunSmart — repel (wrong-fit, optional negative keyword / copy avoidance)

- Lead promises of maximal race aggression, “never miss a workout,” elite PB framing without readiness escape hatches.

### Resumely — attract

| Phrase cluster | Source type |
|---|---|
| “really obvious it was written by ChatGPT” | S10 primary Blind |
| “flowery prose” / less AI polish | S10 |
| “ATS-friendly” / “not an art project” | S11 |
| “buzzwords… sound like everyone else’s” | S9 secondary |
| “look free but charge $20+/month” / export lock | S9 secondary + teardown |
| “gameable” score (what to *not* be) | S9 secondary |

---

## 5. Opportunities

### Opportunity Card: RunSmart ASO right-fit rewrite

- **Opportunity name:** ASO / subtitle / first 3 lines rewrite using failure/injury/walk-run language + Relph/Frandsen proof
- **Product:** RunSmart iOS
- **User problem:** Wrong-fit installs inflate the 94.7% onboarding drop
- **Evidence:** Facts 2–7; Language bank
- **Target user:** Beginner / returning / injury-anxious runners searching C25K alternatives
- **Business value:** Improves activation denominator quality without new product features
- **Implementation complexity:** Low
- **Data / API dependencies:** App Store Connect copy; optional PostHog acquisition→onboarding by keyword later
- **Revenue potential:** Indirect
- **Strategic fit:** EXD-013 activation; WP-9 ASO lineage
- **Risks:** Over-claiming clinical outcomes; must keep study wording accurate
- **Confidence:** High

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 4 | 4 | 2 | 2 | 5 | 2 |

**Recommended next step:** Draft one App Store description variant for founder review (WP-9 style), citing S2/S3.

### Opportunity Card: Onboarding fit gate (lightweight)

- **Opportunity name:** First-screen intent split — “Start gently / returning from break” vs “Train for a race”
- **Product:** RunSmart iOS
- **User problem:** Race-intent users enter a readiness-first path and bounce
- **Evidence:** Facts 6–7; Insight 1
- **Target user:** All new installs
- **Business value:** Routes wrong-fit to honest expectations or shorter path; measures segment mix
- **Implementation complexity:** Medium
- **Data / API dependencies:** New onboarding property + funnel split
- **Revenue potential:** Indirect
- **Strategic fit:** Attacks wrong-traffic angle of 94.7% drop
- **Risks:** Extra screen can hurt completion — keep to one tap
- **Confidence:** Medium

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 4 | 3 | 3 | 2 | 5 | 3 |

**Recommended next step:** Packet after ASO copy ships; one-question gate only.

### Opportunity Card: Resumely anti-generic / anti-gameable messaging

- **Opportunity name:** Store + in-app copy: “sounds like you, not ChatGPT” + Match Score is diagnostic not gameable
- **Product:** Resumely iOS / Web
- **User problem:** Category distrust of AI polish and fake scores
- **Evidence:** Facts 9–11
- **Target user:** Job seekers burned by AI buzzword resumes
- **Business value:** Attracts users who will complete optimize→export for a *usable* file
- **Implementation complexity:** Low
- **Revenue potential:** Indirect
- **Strategic fit:** Pairs with first-free-PDF teardown recommendation
- **Risks:** Over-promising uniqueness of AI output
- **Confidence:** Medium–High

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 3 | 4 | 2 | 2 | 4 | 2 |

**Recommended next step:** Fold 2 phrases into next ASO / WP-32 community post draft.

### Opportunity Card: Community distribution targets

- **Opportunity name:** Observe-only presence plan for HealthUnlocked C25K + Blind + named subreddits (when Reddit access available)
- **Product:** Both (RunSmart priority)
- **User problem:** No organic listening loop in the rooms where right-fit language is minted
- **Evidence:** Facts 1, 4, 8
- **Implementation complexity:** Low (listening) / Medium (posting — needs founder yes)
- **Strategic fit:** WP-32 style; distribution-os observe-only rules
- **Confidence:** Medium

| Impact | Confidence | Effort (lower=better) | Revenue potential | Strategic fit | Risk (lower=better) |
|---|---|---|---|---|---|
| 3 | 3 | 2 | 2 | 4 | 2 |

**Recommended next step:** Add HealthUnlocked C25K to RunSmart distribution watchlist; no posts without founder approval.

---

## 6. Risks

- Treating secondary Reddit paraphrases as primary (mitigated: labeled).
- Claiming “Runna injures runners” as proven — press says anecdotes unproven; position on *user fear of load*, not competitor malpractice.
- ASO medical overclaim vs study nuance (Frandsen ≠ weekly 10% rule).
- Intent gate adds friction if poorly designed.

---

## 7. Recommendations

1. **Ship a RunSmart ASO variant** using Language bank + Relph 27.3% + Frandsen single-session 10% wording (Opportunity 1).
2. **Keep Resumely Match Score diagnostic** and pair anti-ChatGPT-generic messaging with first free PDF (teardown).
3. **Do not** open paid acquisition until right-fit copy is live and EXD-013 still holds.
4. **Park** “scrape X” until network access exists; do not invent tweets.

---

## 8. Open Questions

- Share of RunSmart’s 94.7% drop that is wrong-fit vs UX friction — **unknown — need: intent question + cohort split**.
- Live r/C25K / r/Runna thread sampling once Reddit unblocks — **unknown**.
- Native X language for IL/Hebrew runners and job seekers — **unknown**.
- Whether HealthUnlocked allows brand participation without spam flags — **unknown — need: founder policy**.

---

## 9. Decision Needed

**Approve one RunSmart App Store description draft** that leads with beginner/returning/failure-to-finish language and cites Relph + Frandsen accurately — then A/B or replace current copy.

---

**Confidence:** Medium — primary studies + primary HealthUnlocked/Blind language + attributable press; Reddit/X still blocked so social prevalence is not fully re-verified.
**Recommended next step:** Draft the RunSmart ASO variant (copy only, no ship) for founder review; update WP-9 or open a thin Grower packet if approved.

---

## Evidence Table (material claims)

| Claim | Source | Type | Reliability | Date | Summary | Contradictions | Confidence | Implication |
|---|---|---|---|---|---|---|---|---|
| C25K completion 27.3%; drop themes include injury + design | S2 | Primary | High | 2023 | Relph et al. n=110 | Small sample / UK | High | Core ASO proof |
| Single-run >10% vs longest in 30d raises overuse injury | S3 | Primary | High | 2025 | Frandsen n=5205 | Not weekly 10% rule | High | Correct prior brief imprecision |
| Beginners say “too hard / failure / injured / can’t run 1 min” | S4 S5 | Primary / vendor quotes | Med–High | 2020–2025 | Consistent across years | Vendor selection bias on S5 | High | Right-fit language bank |
| TikTok/Reddit cautionary tales + WSJ PTs on Runna load | S6 S7 | Press | Med–High | 2026 | Named channels; anecdotes ≠ RCT | No peer-reviewed Runna injury rate | Medium | Category fear is public |
| Blind: “obvious ChatGPT” resume prose | S10 | Primary | High | 2023 | Direct replies | Older thread | Medium–High | Resumely anti-generic hook |
| Reddit buzzword / gameable / $20 export quotes | S9 | Secondary | Medium | 2026 | Aggregator | Not re-fetched on Reddit | Medium | Keep labeled secondary |
| Direct Reddit/X bodies this session | — | — | — | 2026-07-11 | Blocked | — | — | Gap remains |

---

## Updates logged

- Brief upgraded in place: `executive-os/research/2026-07-11-demand-mining-right-user-fit.md`
- Scaffold + EXECUTIVE-DASHBOARD notes refreshed with grounded findings (same day)
- No EXECUTIVE-DECISIONS change until founder approves ASO draft
