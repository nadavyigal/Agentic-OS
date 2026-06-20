# RunSmart — ASO Listing Audit (rs-aso-003)

**Date:** 2026-06-20
**Skill used:** `.agents/skills/marketing/aso/SKILL.md`
**App:** RunSmart: AI Run Coaching — [id6768297840](https://apps.apple.com/il/app/runsmart-ai-run-coaching/id6768297840) (bundle `com.runsmart.lite`, dev Nadav Yigal)
**Live version audited:** 1.0.3 (updated 2026-06-19, ~1 day before audit)
**Tier:** Challenger (brand-new app, zero ratings yet, needs keyword + conversion work). Scored strictly.
**Sources:** live App Store page (WebFetch) + version-controlled fastlane metadata + 5 in-repo screenshots per device.

---

## 0. Critical context findings

1. **Repo metadata is stale vs what's published.** `fastlane/metadata/en-US/name.txt` = `RunSmart`, but the live title is `RunSmart: AI Run Coaching`. The repo also shows en-US only, while the store lists English **and** Hebrew. Conclusion: App Store Connect, not the repo, is the live source of truth — the fastlane files were not kept in sync after submission. **Action: re-sync fastlane metadata from ASC so the repo reflects reality.**
2. **Brand-token collision.** An established same-named app, "RunSmart" by RunSmart Online LLC ([id1507476659](https://apps.apple.com/us/app/runsmart/id1507476659), runsmart.online), owns the bare term "RunSmart." Your fuller published name "RunSmart: AI Run Coaching" differentiates and adds keywords, which is the right move — but a plain-brand search still favors the incumbent. Out-keyword them on "AI run coaching / adaptive plan" rather than fighting for "RunSmart" alone.
3. **Zero ratings (insufficient to display).** v1.0.3 has no shown rating. For a Challenger app this is the single biggest conversion blocker — no social proof. A first-reviews push is priority #1, ahead of any keyword tweak.

---

## 1. Score card (provisional — listing is days old)

| # | Dimension | Weight | Score | Note |
|---|---|---|---|---|
| 1 | Title & Subtitle | 20% | 6.5/10 | Title strong (`RunSmart: AI Run Coaching`); subtitle wastes itself duplicating title words |
| 2 | Description | 15% | 7/10 | Clear daily-answer hook, honest, names Garmin/Apple Health; not search-indexed on Apple (conversion only) |
| 3 | Visual Assets | 25% | 5/10 | 5 well-ordered screens, premium dark aesthetic — but no caption headlines, no preview video |
| 4 | Ratings & Reviews | 20% | 2/10 | No ratings yet — expected for a new app, but blocks conversion; first-reviews push needed |
| 5 | Metadata & Freshness | 10% | 6/10 | Updated 1 day ago (fresh), Health & Fitness, English+Hebrew live; keyword field needs review in ASC |
| 6 | Conversion Signals | 10% | 4/10 | Free (good for installs) but zero social proof |

**Weighted provisional grade: C (~5.2/10).** Re-score once first ratings land and ASC keyword field is confirmed.

---

## 2. Top 3 quick wins (<1 hr each, App Store Connect metadata only — no app code)

1. **Rewrite the subtitle so it stops duplicating the title.**
   Apple indexes each word once; your title already owns `Run` and `Coaching`, so the current subtitle "Run coaching that fits today" largely wastes its 30 chars re-indexing words you already rank for.
   - From: `Run coaching that fits today` (29/30)
   - To: `Adaptive plans for every runner` (31 — trim) → `Adaptive plans, beginner to 10K` (31 — trim) → **`Adaptive plans, daily readiness`** (30/30)
   - Why: captures net-new indexed terms (`adaptive`, `plans`, `readiness`) instead of repeating `run`/`coaching`.

2. **Review and refill the keyword field in App Store Connect** (the repo `keywords.txt` is likely stale too).
   - Avoid any word already in title/subtitle (`runsmart`, `ai`, `run`, `coaching`, `adaptive`, `plans`, `readiness`) — repeating them wastes bytes.
   - Target high-intent gaps from RunSmart's own tracked themes: `marathon,beginner,5k,10k,interval,training,garmin,strava,recovery,gps,couch to 5k`.

3. **Add a first-reviews prompt.** Trigger `SKStoreReviewController` after a positive moment (first run logged, or first week-1 plan completed; max 3 prompts/365 days). Zero ratings is the conversion ceiling right now — getting to even 5-10 four/five-star ratings will move installs more than any copy change.

---

## 3. Detailed findings

- **Visual assets (biggest fixable lever, 25%):** The 5 screenshots (today → plan → run → report → profile) are well-ordered and show a premium dark UI, but they are **raw app screens with no caption headlines**. First 3 frames are what 90% of searchers see, and Apple has indexed caption text since June 2025. Add a one-line benefit headline per frame:
  - Frame 1 (Today): "Know what to run, every morning"
  - Frame 2 (Plan): "A plan that adapts when life does"
  - Frame 3 (Run): "GPS tracking + a plain-language debrief"
  - Frame 4 (Report): "See your effort, not just your pace"
  - Frame 5 (Profile): "Garmin & Apple Health, made useful"
  Also **no preview video** — a 15-30s silent screen capture is worth ~+20-40% conversion.
- **Title:** `RunSmart: AI Run Coaching` (25/30) is good — brand + two high-value keywords, and it differentiates from the same-named incumbent. Leave it.
- **Description:** Strong and honest; not indexed on Apple, so do not keyword-stuff it. Leave it.
- **Hebrew:** Already live — good (matches no specific RunSmart Hebrew thesis, but free reach in the IL store where this listing is served). Ensure the **Hebrew** subtitle/keywords/screenshots are separately optimized; this audit covered en-US only.
- **Freshness/category:** Updated 1 day ago (good signal). Primary category Health & Fitness is correct; confirm a secondary category (Sports) is set in ASC — WebFetch couldn't see one.
- **Release notes:** v1.0.3 "Stability improvements and performance optimizations" is generic; acceptable for a patch, but a one-line user-facing highlight converts slightly better when you next ship a feature.

---

## 4. What still couldn't be assessed

- **Live keyword field** (hidden; not exposed by WebFetch) — confirm in App Store Connect.
- **Promotional text** — WebFetch returned "not found"; confirm whether one is set.
- **Keyword rankings / search volume** — needs a paid ASO tool (AppTweak, Sensor Tower).
- **As-published screenshots/captions** — assessed the in-repo assets; confirm they match what's live.

---

## 5. Priority action plan (impact × effort)

1. First-reviews prompt (SKStoreReviewController) — unblocks the zero-ratings conversion ceiling. *Needs a small app change + your approval.*
2. Subtitle + keyword-field rewrite (quick wins 1-2) — ASC metadata only, <1 hr.
3. Caption headlines on the 5 screenshots — design effort, high conversion lift.
4. Re-sync fastlane metadata from ASC so the repo stops drifting from live.
5. Short preview video — medium effort.
6. Separate Hebrew-locale ASO pass.

*No app code was changed by this audit. Items 1 and 3 require app/asset work and your approval before execution.*
