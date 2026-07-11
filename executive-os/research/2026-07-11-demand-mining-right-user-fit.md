# Research Brief: Right-User Demand Mining for Fit (RunSmart + Resumely)

- Date: 2026-07-11
- Researcher / agent: Claude (web search — no live X/Reddit access; see Methodology Note)
- Question (and why it matters now): Where do the actual target users for RunSmart and Resumely gather, and what exact language do they use — so ASO copy and acquisition targeting attract users who fit the product instead of diluting activation with wrong-fit installs. Companion to `2026-07-11-competitor-activation-teardown.md` (proven onboarding patterns); this brief is about audience precision, not funnel UX.
- Tools available: web search / fetch only — **could not fetch reddit.com or x.com directly** (blocked); worked from secondary aggregators, review sites, and one peer-reviewed study that cite/quote primary community discussion.

## Methodology Note (read before trusting this brief)

This is a materially weaker evidence base than the 2026-07-11 competitor teardown, which had live Reddit/X access. Direct fetches to `reddit.com` failed in this session. Every quote below is a **secondary aggregator's quote of a primary post**, not a Claude-verified original. Where a search returned no real links, that attempt is reported as a gap, not filled in with a fabricated finding — several initial queries returned "No links found" and are omitted from Facts below rather than reported as null results with invented content.

---

## 1. Facts

### RunSmart — where beginner/returning runners gather and how they talk

1. Named communities where beginner and injury-returning runners congregate: **r/running** (largest, ~2M-follower scale per aggregator), **r/C25K**, **RunningAhead Forums** (explicitly newcomer-welcoming, injury-prevention focus), **Runners Forum** (dedicated "Beginners" and "Injury & Health" subforums), **LetsRun Forum**. [S1]
2. A 2023 peer-reviewed study (*International Journal of Environmental Research and Public Health*) found only **27.3% of participants completed** a 9-week Couch to 5K program — secondary sources round this to "73% of users don't finish it." Cited driver: "the plan gets harder faster than their bodies adapt." [S2]
3. A study following 5,200+ runners found injuries cluster when "a single run suddenly jumped more than about 10% beyond the longest run in the past month" — a specific, quotable mechanism for "too much too soon." [S2]
4. Secondary-sourced Reddit sentiment: Nike Run Club's "Get Started" plan is criticized because it "asks for a 20-minute continuous run on day one — unrealistic for true beginners"; Runna's "New to Running" plan is called "too aggressive" and "too challenging for a true beginner" by multiple Reddit posts (per aggregator, not independently verified). [S2]
5. The vocabulary beginners actually search/ask for, per the same aggregator's framing of what beginners need: "short intervals," "slow, time-based progressions," "regular walk breaks," "simple strength work," "supportive coaching," "consistency, not performance" — this reads as close to native user language (framed as answers to what beginners are asking for) rather than marketing copy. [S2]
6. Runna already ships a named **"Post-Injury Plan"** with "Plan Realignment" (auto-adjusts schedule after missed sessions) and "Training Preferences" (intensity/volume/long-run tuning) — i.e., "returning runner" is not white-space; a direct competitor already has a shipped, named feature here. [S3]
7. Standard return-to-running guidance repeated across sources (not RunSmart-specific): ease in with walking first, don't increase weekly volume/speed by more than 10%, consider a physio/medical check for specific injuries, use cross-training (swim/cycle/row/elliptical) to maintain fitness without impact. [S3]

### Resumely — where job seekers gather and how they talk

8. Named communities: **r/resumes, r/jobs, r/careerguidance, r/GetEmployed, r/cscareerquestions, r/recruiting, r/linkedin**. [S4]
9. Quoted complaint on AI resume output (secondary-sourced from r/resumes-type threads): *"It just added buzzwords and made my resume sound like everyone else's."* Also: ChatGPT-drafted resumes read as "too polished" or "obviously AI-written," and recruiters on r/recruiting report recognizing ChatGPT phrasing patterns. [S4]
10. Billing-trap language, closely mirroring the competitor teardown's Resume.io/Rezi findings: *"Tools that look free but charge $20+/month for basic exports"*; users "despise bait-and-switch free tools that lock the download behind a paywall"; a stated preference for "one-time payments over monthly recurring fees" ("subscription fatigue"). [S4]
11. ATS-scoring skepticism: Resume Worded's scoring is described by users as **"gameable"** (reports of inflating scores with irrelevant keywords) — this is a direct, specific risk to Resumely's own "Match Score" positioning if it is ever perceived the same way; the defensibility work already done (renaming to "Resumely Match Score," adding the "not affiliated with any ATS vendor" explainer) is the right shape of fix for this exact complaint pattern. [S4]
12. Template/formatting complaint: multi-column, icon-heavy, color-scheme-heavy templates are called out by name as "ATS systems can't parse" — validates keeping Resumely's optimizer output format-conservative. [S4]
13. Tools named with positive sentiment in the same discussions: Teal, Kickresume, Rezi, Jobscan. Mixed/negative: ChatGPT (for resume writing specifically), Resume Worded, Enhancv. [S4]

---

## 2. Sources

| # | Source | Type | Reliability | Date |
|---|---|---|---|---|
| S1 | Feedspot — "Top 20 Running Forums in 2026" | Secondary aggregator | Medium | accessed 2026-07-11 |
| S2 | None to Run — "The Best Beginner Running Apps for 2026" (cites 2023 IJERPH study + 5,200-runner injury study + Reddit sentiment) | Secondary, cites a peer-reviewed study | Medium-High (primary stat), Low-Medium (Reddit paraphrase, unverified) | accessed 2026-07-11 |
| S3 | Runna Support / runna.com — "Top Tips for Returning to Running After a Break," "Post-Injury Training Plans" | Vendor/primary (Runna's own claims about its feature set) | High for "what Runna claims to ship"; not independently verified in-product | accessed 2026-07-11 |
| S4 | Resume Optimizer Pro — "Best Resume Builder Reddit (2026)" | Secondary aggregator, quotes r/resumes-type threads | Medium (quotes are aggregator-curated, not independently verified against original Reddit posts) | accessed 2026-07-11 |

**Not obtained (queries attempted, no usable result — reported as a gap, not filled in):** direct Reddit thread text for r/running / r/C25K beginner injury complaints; direct Reddit thread text for "ATS killed my application" style resume complaints; any X (Twitter) discussion for either app category; TikTok/Discord/Facebook-group presence for either audience.

---

## 3. What this changes for RunSmart and Resumely

**RunSmart — the wrong-fit-traffic angle on the 94.7% onboarding drop:**
- The category's own numbers (73% C25K non-completion, driven by plans outrunning the body) are RunSmart's strongest, most quotable ASO proof point: "most beginner running apps lose 3 in 4 people because the plan gets harder faster than your body does." This is a stat, not a vibe claim.
- The 10%-weekly-jump injury threshold is a concrete, technical hook for copy and possibly a literal safety guardrail to state explicitly in marketing ("we never increase your week by more than 10%").
- Direct competitors (Runna, NRC) are already criticized by name in the exact language "too aggressive for a true beginner" — RunSmart's ASO can target that specific dissatisfied segment without inventing a new positioning.
- Caution: Runna already has a named, shipped "Post-Injury Plan" + "Plan Realignment" feature. "Returning runner" is a real, served segment already — RunSmart's differentiation there needs to be sharper than "we also support returning runners," since a direct competitor claims this ground.

**Resumely — audience precision + a live defensibility risk:**
- The named subreddits (r/resumes, r/jobs, r/careerguidance, r/GetEmployed, r/cscareerquestions, r/recruiting, r/linkedin) are concrete targets for organic/community distribution work, not a guess.
- The "gameable ATS score" complaint (aimed at a named competitor, Resume Worded) is a direct warning shot for Resumely's own Match Score: if it is ever perceived as gameable rather than diagnostic, it inherits this exact community skepticism. The defensibility work already shipped (2026-06-20 positioning fix, "Resumely Match Score" + explainer) is pointed the right direction; this finding is evidence to keep enforcing that line, not a new action item.
- Billing-trap fatigue is now confirmed from two independent angles (this brief's resume-community quotes + the competitor teardown's Resume.io/Rezi findings) — reinforces that Resumely's pricing model should lead with simplicity/transparency in messaging, whatever the eventual paid-tier shape turns out to be.

## 4. Recommended next step

Not a new work packet on its own — this is audience/positioning input for whoever next touches RunSmart ASO copy or Resumely community distribution (WP-32-style community distribution work). The one concrete, low-risk action: fold the "73% of beginners quit because the plan outpaces the body" stat and the 10%-rule into RunSmart's App Store description / ASO copy test, since it is sourced to a real study rather than invented.

## Updates logged

- Research brief filed: `executive-os/research/2026-07-11-demand-mining-right-user-fit.md`
- No EXECUTIVE-DECISIONS change — informational input, not a decision request
- Companion to `2026-07-11-competitor-activation-teardown.md` (Grok-style example pair, item 2 of 2)
