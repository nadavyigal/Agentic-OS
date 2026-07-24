# WP-45 — Resumely Direct Optimize + Trustworthy Score Calibration

- **Status:** In Progress — **amended v2 on 2026-07-24** after the Meirav moderated user session and a full scorer-integrity audit
- **Created:** 2026-07-12 · **Amended:** 2026-07-24
- **Mode:** Grower
- **Workflow pattern:** normal, one story at a time; scorer integrity before score UI; cross-vendor review for the scorer change
- **Input trust:** trusted local code, privacy-safe PostHog aggregates, privacy-safe Supabase aggregates, founder direction 2026-07-12, moderated user session 2026-07-24
- **Projects:** Resumely iOS and ResumeBuilder Web/backend
- **Source:** 2026-07-12 founder direction and score investigation; 2026-07-24 Meirav session + scorer audit; supersedes the pre-optimization iOS gate in WP-12/WP-13
- **Related decisions:** 2026-06-20 branded Match Score; 2026-06-23 Fit-First thresholds; 2026-07-02 20% activation target; 2026-07-12 remove the pre-optimization Fit gate
- **Metric / funnel step:** founder-excluded `job_added -> analysis_cta_tapped -> optimization_started -> optimization_completed -> export_success`
- **Memory update:** iOS and web `tasks/progress.md`, `tasks/session-log.md`, and `tasks/lessons.md` only if a reusable correction is learned
- **Success signal:** see [Revised success signals](#revised-success-signals) — the v1 signals were funnel-only and cannot be evaluated at current traffic

---

## v2 amendment log (2026-07-24)

The v1 packet was correct that the score is untrustworthy and that the pre-optimization gate must go. It was wrong about **why** the score is untrustworthy, and it deferred every scoring fix behind an iOS routing change.

The 2026-07-24 audit found that the score is not merely *miscalibrated*. **Three of eight scoring components are structurally broken**, the before/after pair is measured on two different representations of the resume, and the band thresholds were set for a scoring regime that stopped existing on 2026-06-18. Calibration (v1 Story 4) applied on top of this would have re-banded a broken scale and locked the defects in as "calibrated".

| Change | v1 | v2 |
|---|---|---|
| Primary thesis | Fit is an ATS composite wearing a fit label | Fit is an ATS composite wearing a fit label **and** the composite itself has a ~65-point hard ceiling caused by three dead components |
| First code story | S1 iOS gate removal | **S1 scorer integrity** — the iOS routing change cannot fix a number that is wrong at source |
| Before/after pair | not addressed | **S2** — the 42→44 that the user saw is a measurement artifact, now its own story |
| One number across surfaces | implicit | **S3** — explicit; three code paths currently produce three different numbers for one resume/job pair |
| Bands | "select from benchmark in S4" | unchanged intent, but S5 now must prove Strong is *reachable* before bands ship |
| Flow simplification | only "remove FitCheckView" | **S7** — the full `fit → optimize → uplift → experts → design → share` spine, per founder feedback 2026-07-24 |
| Success gate | PostHog funnel thresholds | **Deterministic benchmark gates are primary**; PostHog is a lagging confirm, because the clean cohort is 2 people |
| Historical scores | not addressed | **S8** — pre-2026-06-18 rows are from an incomparable regime and must not be compared or averaged with current ones |

Story numbering changed. Mapping: v1 S0 → v2 S0 (unchanged, already implemented); v1 S1 → v2 S6; v1 S2 → v2 S4; v1 S3 → v2 S3; v1 S4 → v2 S5; v1 S5 → v2 S8; v1 S6 → v2 S10. New in v2: S1, S2, S7, S9.

---

## Evidence

### The user session (2026-07-24, Meirav, moderated, founder present)

1. Fit screen showed **45**. Below the `skip` threshold of 50, so the app told her to consider skipping the job before she had experienced any value.
2. After optimizing, the result screen showed **42 before → 44 after**. Three different numbers for what she reasonably read as one thing, and a +2 payoff for the app's core action.
3. The path from job to shareable PDF ran `fit → optimize → uplift → experts → design → share`, which she navigated but did not experience as one flow.

Founder read: (2) is the drop point. Users must see the number move up as they progress, or the product's central promise is visibly not working.

### Measured score distributions (privacy-safe aggregates, pulled 2026-07-24)

**Free/anonymous checker** — Supabase `anonymous_ats_scores`, 60 days, n=67:

| mean | median | min | max | below 50 | at or above 75 |
|---|---|---|---|---|---|
| 34.5 | 36 | 11 | **51** | 51 (76%) | **0** |

**Authenticated optimizations** — Supabase `optimizations`, 60 days, n=59:

| mean before | mean after | mean delta | median after | max after | went down | flat | up 1–4 | up 10+ |
|---|---|---|---|---|---|---|---|---|
| 32.2 | 41.6 | +9.4 | 40 | **62** | 6 | 2 | 16 | 25 |

**24 of 59 optimizations (41%) ended at +4 or worse.** Meirav's +2 is not an outlier, it is the modal bad outcome. Nobody in 60 days has seen a post-optimization score above 62, and nobody on the free checker has seen above 51.

**Regime shift** — the same table by month:

| month | n | mean before | mean after | mean delta | max after |
|---|---|---|---|---|---|
| 2026-07 | 14 | 32.8 | 44.5 | +11.7 | 61 |
| 2026-06 | 41 | 29.6 | 38.8 | +9.2 | 61 |
| 2026-05 | 25 | 56.6 | 60.7 | +4.1 | 67 |
| 2026-02 | 18 | 56.8 | 61.0 | +4.2 | 74 |
| 2025-11 | 110 | 61.6 | 68.7 | +7.1 | 100 |

The scale dropped roughly 20 points between May and June 2026. The cause is a cluster of *correct* fixes landed 2026-06-18 → 2026-06-26 in the web repo: `d5168aa` word-bound keyword extraction (#80), `073aecc` requirement atomization (#82), `5879b6b` junk-phrase filter (#85), `47abf12` strip fabricated metrics. Each removed a source of inflation. None was followed by a recalibration, so the top third of the scale silently became unreachable.

**Component means** — `optimizations`, 60 days, n=59, before → after:

| component | weight | before | after | reading |
|---|---|---|---|---|
| keyword_exact | 22% | 21.7 | 39.1 | works, moves |
| semantic_relevance | 16% | 54.1 | 71.1 | works, moves |
| title_alignment | 10% | 23.0 | 38.3 | works, moves |
| section_completeness | 8% | 66.5 | 99.7 | works, moves |
| **keyword_phrase** | **12%** | **0.6** | **4.2** | **dead** |
| **metrics_presence** | **10%** | **6.2** | **7.2** | **dead, and triggers a permanent penalty** |
| **format_parseability** | **14%** | **87.8** | **87.8** | **frozen — identical on all 59 rows** |
| **recency_fit** | **8%** | **50.0** | **12.7** | **inverted — measurement artifact** |

**Bands vs reality** — `FitVerdict.swift:19-28` sets `strong ≥ 75`, `stretch 50-74`, `skip < 50`. Observed maxima are 51 (free) and 62 (optimized). PostHog confirms: across all non-tester `fit_check_completed` events in 60 days, the only verdicts ever emitted are `stretch` and `skip`. **No user has ever seen `strong`.** Meirav's 45 → `skip`.

### Named defects

**D1 — `keyword_phrase` (12% of weight) is a dead component.**
`analyzers/keyword-phrase.ts` scores verbatim 3–6-word n-gram overlap between the JD and the resume. Real resumes essentially never reproduce a JD's exact phrasing, so the component returns near-zero for everyone (means 0.6 / 4.2 / 1.3). It contributes ~0.5 of its 12 available points while still consuming 12% of the denominator. Cost to every user: ~11.5 points.

**D2 — `metrics_presence` (10%) is dead and carries a permanent penalty.**
Means are 6.2 before and 7.2 after, both under the `< 10` trigger for `no_metrics_penalty: 5` in `config/thresholds.ts`. So the −5 penalty applies to essentially every scoring run, before *and* after, and cancels out of the delta while depressing both numbers. `47abf12 stripFabricatedMetrics` — correctly — prevents the optimizer from inventing metrics, which means this component cannot be earned by optimizing. Combined cost: ~14 points.

**D3 — `format_parseability` (14%) is frozen across the before/after pair.**
`core.ts:49` builds one `format_report` in `prepareInput` and `core.ts:62-73` passes that same object into both the original and the optimized analyzer run. The optimized resume is scored on the original's format report. Confirmed empirically: 87.8 → 87.8, identical on all 59 rows. 14% of the score can never move, no matter what the optimizer does.

**D4 — `recency_fit` (8%) is measured asymmetrically.**
`analyzers/recency-fit.ts:24` returns a fixed `50` with confidence 0.6 when no structured experience array is present. The **original** is scored from raw text (no array → constant 50); the **optimized** is scored from `resumeJsonToText()` output built from structured JSON (real dates → real score, mean 12.7). This subtracts a systematic ~3.0 points from every reported delta, purely as an artifact of how the two sides are represented. This is the single clearest mechanism behind "the number barely moved".

**D5 — three surfaces, three numbers.** The fit screen calls `/api/public/ats-check`, which builds its input with `DEFAULT_FORMAT_REPORT` and the `jobData` resolver. The optimize path calls `scoreOptimization`, which builds `generateFormatReport(resumeOriginalText)` (`integration.ts:172`) and may use `jobExtractedJson` instead. Same resume, same job, different format report and different JD extraction, therefore different score. **This is Meirav's 45 vs 42.**

**D6 — bands are calibrated for a regime that ended on 2026-06-18.** `strong ≥ 75` against an observed ceiling of 51/62 means 76% of free-checker users are told `skip` before the product has done anything for them.

**Ceiling estimate.** Holding D1–D4 at their observed values and assuming a *perfect* job match (keyword_exact, semantic, title, sections all 100): `0.22(100) + 0.12(4.2) + 0.16(100) + 0.10(100) + 0.10(7.2) + 0.08(100) + 0.14(87.8) + 0.08(12.7) ≈ 70.5`, then −5 for the metrics penalty ≈ **65.5**. A flawless candidate cannot reach `strong`. This is an estimate from observed component means, not a proof — S1 must verify it with a synthetic perfect-match fixture before and after the fixes.

### What this means

The v1 constraint "do not inflate scores to improve conversion" stays, and D1–D4 do not violate it. Repairing a component that returns zero regardless of input is not inflation; it is removing a systematic deflation that the product never intended and never validated. The distinction matters for the cross-vendor reviewer: **the test is whether a change makes the score more responsive to real evidence, not whether the number goes up.**

---

## Product decision and amended journey

### Remove

- The authenticated Home/Tailor presentation of `FitCheckView` after Analyze.
- The repeated "Using Job Link" confirmation card and optional job-description field when the job was already supplied.
- The second "Check Fit" CTA.
- The pre-optimization red `skip`/`Weak Fit` gate and "Browse Other Jobs" exit.
- The expectation that `fit_check_optimize_tapped` remains part of the new activation path.

### New authenticated iOS journey

```text
Resume + job supplied
-> Analyze & Optimize (one intent, one CTA)
-> validate existing inputs and job-extraction quality
-> start optimization directly
-> show honest loading states backed by real work
-> Result: what changed, one score, top remaining gaps
-> export PDF
   (Design and Expert reachable from the result, not as gates on the way to it)
```

If a URL cannot be read reliably, stay on the original input surface and show one actionable recovery: "We couldn't read the full job from this link. Paste the job description to continue." Preserve the resume, URL, and any pasted text. Do not open a second Fit screen and do not return a guessed score.

### Score placement

- **Before S1–S5 land:** do not show a numeric pre-optimization score or band in the authenticated activation path. Show progress, then specific gaps and what changed after optimization completes.
- **After S5:** show one job-fit number as contextual starting guidance inside the result, never as permission to optimize.
- The user must never see a score go **down** as a result of using the product. If the honest post-optimization number is lower than the honest pre-optimization number for the same evidence, that is a bug in the scorer or the optimizer, not a result to display. S2 makes this an enforced invariant, not a hope.
- Keep the broader Resumely Match/ATS-readiness score after optimization, clearly labeled and separate from job-only fit.

## Score contract

The backend `fit` object becomes a real, versioned contract rather than a label wrapped around `ats_score`:

```jsonc
{
  "fit": {
    "available": true,
    "score": 67,
    "band": "stretch",
    "confidence": "high",
    "scoreVersion": "fit_v2",
    "jobInputSource": "url",
    "extractionQuality": "high",
    "requirementCount": 8,
    "topGaps": [],
    "missingKeywords": []
  }
}
```

Rules:

1. Fit uses only job-dependent evidence: semantic alignment, credible requirement coverage, and title/seniority alignment. It must not include format, generic section completeness, quantified-metrics presence, or recency hygiene.
2. Exact weights and band thresholds are not guessed in code. They are selected from the benchmark in S5.
3. `available=false` when extraction quality is insufficient. In that state the response carries a recovery reason, no score, and no band.
4. Requirement extraction rejects headings/navigation fragments and preserves meaningful phrases. A generic stop list alone is insufficient; the quality gate must consider phrase shape, source section, minimum credible requirement count, and extraction provenance.
5. The existing `score.overall` remains backward-compatible for the public web checker during migration, but iOS must not silently substitute it for missing `fit.score` after `fit_v2` launches.
6. **Every component in any displayed composite must be able to change in response to the evidence it claims to measure.** A component that returns a constant is either fixed or removed from the weighting — it is never left in the denominator.
7. No resume text, job-description text, URLs, emails, or identifiers are added to analytics.

---

## Stories

| Story | Repo | Mode | Outcome |
|---|---|---|---|
| S0 — Measurement contract and baseline | iOS + PostHog | Grower | **Done 2026-07-12** — clean before/after funnel, no UX change |
| **S1 — Scorer integrity: repair the dead components** | Web/backend | Builder | **Done 2026-07-24 (PR #119)** — the composite can reach its own top band |
| **S2 — Symmetric before/after and the no-regression invariant** | Web/backend | Builder | The pair is measured the same way; the number cannot go down |
| **S3 — One canonical score per (resume, job)** | Web/backend | Builder | Fit screen and optimize screen agree |
| S4 — Extraction-quality gate | Web/backend | Builder | Junk requirements cannot produce a confident score |
| S5 — Calibration benchmark, weights, and bands | Web/backend | Maintainer | Bands reflect labeled evidence on a repaired scale |
| S6 — Remove the redundant iOS gate | iOS | Sweeper/Grower | One CTA starts optimization directly |
| **S7 — Collapse the post-optimization flow** | iOS | Grower | One spine from job to PDF; Design/Expert become side-doors |
| S8 — Diagnosis/Review guidance copy | iOS | Grower | Guidance motivates action, including in the no-lift state |
| S9 — Historical score regime handling | Web/backend | Maintainer | Old scores are not silently compared to new ones |
| S10 — Release, readout, and cleanup | iOS + PostHog | Maintainer | Verify lift and remove dead Fit-first code |

**Ordering rationale.** S1→S3 are backend-only and ship independently of any app release, so they can land while the iOS work is still in review. S6/S7 are the visible change and should not ship before S5 decides what number, if any, the app is allowed to display. If time forces a split, **S1 + S2 alone are worth shipping** — they fix what Meirav actually saw.

### S0 — Measurement contract and baseline

**Implemented 2026-07-12:** Resumely iOS branch `codex/wp45-s0-measurement-contract`, commit `d53d091`. Authenticated Home and Tailor intent points emit `analysis_cta_tapped` with the stable envelope and `flow_version=fit_gate_v1`; existing Fit events carry flow/score version and the completion event carries a bounded score bucket. Privacy-safe 60-day baseline saved at `docs/qa/reports/wp45-s0-measurement-baseline-2026-07-12.md`. Focused analytics tests 13/13, Debug simulator build succeeded, `git diff --check` passed.

**2026-07-24 status check.** `analysis_cta_tapped` exists on `main` (`Core/Analytics/AnalyticsService.swift:138`), and PostHog shows **11 events across 2 people since 2026-07-19** — the branch `codex/wp45-s0-measurement-contract` is still on `origin` and unmerged into a released build. S0's instrumentation is therefore *authored* but not *earning data*. Reconcile that branch before S6, and do not treat the S0 baseline as a usable denominator (see [Cohort reality](#cohort-reality)).

Envelope fields (verify, do not re-add if present): `flow_version`, `score_version`, `job_input_source`, `extraction_quality`, `requirement_count_bucket`, `score_bucket`, `is_internal_tester`, `app`, `marketing_version`, `build_number`.

### S1 — Scorer integrity: repair the dead components

**Implemented 2026-07-24.** ResumeBuilder web branch `claude/wp45-s1-scorer-integrity`, commits `f8966e5` + `ccbc4d5`, [PR #119](https://github.com/nadavyigal/new-ResumeBuilder-ai-/pull/119). All four defects addressed: keyword_phrase withdrawn from the weighting (weights rescaled old/0.88), the no-metrics penalty removed as double-counting, per-side format reports in both orchestrators, and a conservative text extractor for the original side's work history passed as a dedicated `recency_json` so it reaches only the recency analyzer.

Gate results: G1 an excellent candidate without quantified metrics scored 72 and now scores 87, so Strong is reachable; G2 every weighted component varies by >= 5 points across fixtures and keyword_phrase is out of the denominator. 30 deterministic tests, 6 verified failing on the pre-fix source. Full suite unchanged at 17 pre-existing suite failures, passing 171 -> 201; eslint clean; 0 new tsc errors; `next build` passes on a clean checkout.

An adversarial review caught two own-goals in the first commit that would have widened the delta dishonestly — the derived stub reaching four analyzers that branch on `resume_json` (collapsing original-side section_completeness from ~100 to 25), and integration.ts comparing two different format functions (a manufactured ~+2.4 points per run). Both fixed in `ccbc4d5` with regression gates verified to fail against the first commit. **Lesson for S2-S5: verify that a scorer change does not move the ORIGINAL side, not just that the composite went up.**

Still open from this story: `core.ts`/`index.ts` remain duplicate orchestrators; `SubScoreBreakdown.tsx` shows keyword_phrase as a live bar; free-checker scores rise ~11-13 points so the >= 75 verdict may start firing before S5 calibrates the bands.

**This is the story that fixes what the user saw.** Address D1–D4. Each fix is independently testable and independently revertable.

1. **`keyword_phrase` (D1).** Verbatim n-gram overlap is the wrong measure. Either (a) replace exact-match with normalized/stemmed fuzzy phrase matching that credits paraphrase, or (b) if no formulation scores meaningfully above zero on the benchmark, **remove it from the weighting entirely** and redistribute its 12% to `keyword_exact` and `semantic_relevance`. Option (b) is acceptable and may be correct — a component that measures nothing should not be 12% of a user-facing number.
2. **`metrics_presence` (D2).** Decide explicitly: either the optimizer may surface metrics *already present in the source resume* (never fabricate — `stripFabricatedMetrics` stays), making the component earnable; or the component drops out of the composite and the `no_metrics_penalty` is removed with it. Do not keep a 10% component plus a −5 penalty that no user can ever escape.
3. **`format_parseability` (D3).** Compute a separate format report for the optimized side. `core.ts:62-73` must pass a format report derived from the resume being scored, not one shared across both runs.
4. **`recency_fit` (D4).** Score both sides from comparable representations. Either parse structured experience out of the original text before scoring, or apply the same `no experience data` fallback to both sides. The `50` constant must never face a real parsed value on the other side of the same comparison.

**Verification, required, before and after:**

- A synthetic **perfect-match fixture** (resume that fully satisfies a JD) scores **≥ 85** after the fixes. Record its score before the fixes to confirm the ~65 ceiling estimate.
- A synthetic **clear-mismatch fixture** still scores low. The fixes must not compress the scale upward for everyone.
- Every component in the final weighting varies by ≥ 10 points across the fixture set. A component that is constant across all fixtures fails this story.
- Re-scoring the 60-day sample offline shows the composite's max moving above 75 for at least the pairs a human labels Strong.

**Acceptance:** targeted tests fail before and pass after; component-variance report committed; before/after distribution on the fixture set documented; cross-vendor reviewer confirms each change increases evidence-responsiveness rather than adding uplift. Lint, type-check for touched files, and production build pass.

### S2 — Symmetric before/after and the no-regression invariant

The displayed pair must be an apples-to-apples comparison, and the pipeline must never hand back a result worse than where the user started.

1. **Symmetric representation.** The original and the optimized resume must be scored from the same kind of representation. Today one is raw text and the other is `resumeJsonToText()` output, which alone explains a multi-point systematic bias (D4, and any residue of D3). Either parse the original into the same structured shape before scoring, or score both from text produced by the same function.
2. **The invariant.** `optimize-pipeline.ts:250-304` selects between pass 1 and pass 2 by comparing them **to each other**, never to the original. Add an explicit floor: if the winning candidate's optimized score is not meaningfully above `ats_score_original`, that is a pipeline failure, not a result to display. Required behavior on failure — do not silently show a −3 or +2:
   - run the additional pass the current logic already allows;
   - if still below floor, return the honest state: show what changed and the specific remaining gaps, and suppress the numeric pair rather than displaying a non-improvement;
   - emit a privacy-safe `optimization_no_lift` signal with the component that failed to move, so this is measurable instead of anecdotal.
3. **Floor value** is selected in S5 from the benchmark, not guessed here. Until then, use a config constant with a conservative default and no hardcoded uplift.

**Acceptance:** a fixture whose optimization genuinely fails produces the honest no-lift state, not a small positive delta; a fixture that genuinely improves produces a delta driven by components that actually changed; the 6 "went down" and 2 "flat" cases from the 60-day sample are re-run offline and none of them displays a downward number. No artificial minimum score, no flat uplift, no clamping the delta positive.

### S3 — One canonical score per (resume, job)

Meirav saw 45 and 42 for the same resume and the same job because two code paths build different scorer inputs (D5).

- Single scoring entry point used by `/api/public/ats-check`, `scoreOptimization`, and any future surface, with **identical** format-report and JD-extraction construction.
- The score for a `(resume_hash, job_hash, score_version)` triple is computed once and reused across surfaces for the life of that session; `score-cache.ts` already exists and should be the mechanism.
- If two surfaces must legitimately show different concepts (job-only fit vs overall readiness), they must be **labeled as different things**, carry different names in the UI, and never both be called "your score".

**Acceptance:** a contract test asserts the fit surface and the optimize surface return the same number (±1) for the same resume/job pair; the divergent `DEFAULT_FORMAT_REPORT` / `generateFormatReport` split is gone or explicitly justified in code with a test pinning the intended difference.

### S4 — Extraction-quality gate

Strengthen the shared job resolver used by `/api/public/ats-check` and optimization preparation:

- filter structural headings and fragments such as "about", "role objective", and malformed "key responsibilities build";
- retain valid short requirements such as SQL, AWS, or CRM through allowlisted shape rules rather than a blunt word-count filter;
- score extraction quality from source provenance, usable text length, credible requirement count, junk ratio, and title availability;
- fail closed when URL extraction is thin or polluted: return a typed recovery response requesting pasted JD;
- preserve the existing LinkedIn guest-endpoint strategy and do not fall back to a thin authwall snippet.

TDD fixtures must include technical, non-technical, Hebrew, LinkedIn URL, pasted JD, sparse-but-valid, and polluted-heading examples. No production scrape or database migration is part of this story.

**Acceptance:** targeted tests fail before and pass after; no known valid short skill is removed; polluted fixtures return `fit.available=false` or a clean requirement set; lint, type-check, and production build pass.

### S5 — Calibration benchmark, weights, and bands

Create a privacy-safe benchmark of 30–50 synthetic or consented resume/job pairs spanning technical, commercial, operational, junior, senior, career-switch, English, and Hebrew cases. No production resume or JD content is copied into the repo.

For each pair, record independent human labels for Strong / Stretch / Weak plus the decisive reasons. Use the set to choose component weights, the S2 lift floor, and band thresholds. Required gates:

- no artificial flat uplift or hardcoded minimum score;
- **Strong must be reachable and actually reached** by pairs a human labels Strong — this is the gate v1 could not have passed, and it is not satisfiable before S1;
- false-Weak rate below 10% for pairs labeled Strong or Stretch;
- monotonicity: adding truthful relevant evidence cannot lower fit;
- irrelevant format/metric changes cannot move fit;
- polluted or thin extraction yields unavailable/low confidence, not Weak;
- calibration and holdout results reported separately.

If the repaired scale still cannot produce Strong for clearly-Strong pairs, **the bands move, not the evidence** — and that decision is documented as a deliberate recalibration with its date, so a future reader does not repeat the 2026-06-18 mistake of changing the scale without changing the bands.

**Acceptance:** deterministic benchmark runner, documented calibration and holdout results, reviewer approval. Only then enable numeric `fit_v2` and its bands.

### S6 — Remove the redundant iOS gate

In both live entry points, Home and Tailor:

1. Preserve the already-entered resume, pasted JD, and job URL.
2. On Analyze, call the existing upload/preparation helper once, then proceed directly to the existing optimize function.
3. Do not present `FitCheckView` (`HomeTabView.swift:176`, `TailorView.swift:164`), run a separate blocking public-ATS request, or require `onOptimize` from a verdict sheet.
4. Keep duplicate-tap protection, current cancellation behavior, and actionable connection errors.
5. Use the existing diagnosis/review destination after optimization; do not add a new destination.
6. Change the visible CTA to "Analyze & Optimize" only if user testing shows "Analyze" does not already set the correct expectation. Keep EN/HE copy concise and RTL-safe.
7. Reconcile the unmerged `codex/wp45-s0-measurement-contract` branch first — do not rebuild its instrumentation.

Tests must prove: one tap produces at most one upload/preparation and one optimize request; the job link or paste supplied earlier reaches optimize unchanged; no Fit sheet is presented; success reaches the result destination; unreadable-job recovery preserves all prior input; direct optimize does not consume more credits than the current optimize call.

**Acceptance:** focused view-model/routing tests, Debug build, EN/HE localization export, real simulator/device smoke from Home and Tailor.

### S7 — Collapse the post-optimization flow

Founder feedback 2026-07-24: the path should feel like one flow, not six destinations. Today the authenticated user crosses `Home/Tailor → Fit sheet → Optimize → Diagnosis → Optimized tab → Design tab → Expert tab → Preview/Export`, and the tab bar (`ResumlyTabBar.swift:5-10`) presents Design and Expert as **peers of** the core journey rather than as follow-ons from it.

Target spine — one linear path, everything else demoted to an optional side-door from the result:

```text
Add resume + job  →  Analyze & Optimize  →  Result (what changed · one score · top gaps)  →  Export PDF
                                                    ↘ Change design      (optional)
                                                    ↘ Deeper review      (optional)
```

Required work:

1. **Measure first.** Instrument and record the current tap count and screen count from `job_added` to `export_success`. This story's success is a reduction against a recorded number, not a feeling.
2. Make Export the primary action on the result screen. It is currently reachable but not the obvious next step.
3. Demote Design and Expert from primary tabs to named actions on the result screen. Both keep their full functionality; neither sits between the user and their PDF.
4. Do not delete Expert or Design surfaces or their analytics. `submit_package_saved` shows 30 people in 60 days — the Expert path has real usage and this story must not break it.
5. Keep EN/HE parity, RTL, Dynamic Type, reduced motion.

**Open decision for the founder — do not resolve this in an execution session.** Restructuring the tab bar from 5 tabs to 3 is a larger change than the rest of this packet and touches navigation state, deep links (`App/DeepLinkRouter.swift`), and every tab's entry analytics. Two options:

- **(a) Result-screen promotion only** — leave the 5 tabs, make Export primary on the result, add the two side-door actions. Small, low-risk, reversible, ships with S6.
- **(b) Tab-bar restructure** — Home / My Resumes / Me, with Design and Expert reachable only from a result. Delivers the "one flow" feeling properly, costs a separate release and its own QA pass.

Recommendation: **(a) now, (b) as its own packet** once S1–S5 have made the result screen worth arriving at. A cleaner path to a number the user does not trust does not fix activation.

**Acceptance:** recorded before/after tap-and-screen count; screenshots and accessibility snapshots for EN/HE, RTL, Dynamic Type, reduced motion; simulator smoke confirms the user cannot become trapped after optimization and can reach export without visiting Design or Expert.

### S8 — Diagnosis/Review guidance copy

After optimization has started or completed, present guidance as a starting point and action plan:

- high-confidence calibrated fit: concise starting alignment, top gaps, and what the optimization changed;
- low/unavailable confidence: no number or band, only verified gaps and a prompt to improve the JD input if needed;
- no-lift state from S2: what changed, what still blocks, and the next concrete action — never a downward or trivially positive number;
- low score copy: supportive and specific, e.g. "This resume starts with several gaps for this role. We prepared targeted improvements for review.";
- remove `skip`/"Weak Fit" as a red pre-action verdict and remove "Browse Other Jobs" from the primary optimization journey;
- keep the primary next action aligned with review/apply/export, not abandonment;
- retain the Resumely Match Score disclosure and never imply an employer/vendor ATS score.

### S9 — Historical score regime handling

Scores written before 2026-06-18 are from a materially different scale (mean after ≈ 60–69 vs ≈ 39–45 now), and S1's repairs will introduce a third regime.

- Stamp every stored score with its `score_version`. Rows lacking one are pre-`fit_v2` and must be treated as unlabeled.
- Any UI, report, or dashboard that trends or averages scores must filter to a single version, or state the boundary.
- Decide explicitly whether to backfill/rescore historical rows or to freeze them as historical-only. **Rescoring touches production data and requires separate founder approval in the execution session** — it is out of scope here without that approval.
- Add the 2026-06-18 boundary and the S1 boundary to `tasks/lessons.md` in the web repo, so the next person who tightens matching remembers to recheck the bands.

### S10 — Release, readout, and dead-code cleanup

Ship behind the existing build/release process, not a production toggle that does not exist. Mark founder/QA traffic. After the first release cohort reaches the cohort gate below, compare against S0.

If the direct path is healthy, delete unreachable `FitCheckView` entry UI and obsolete routing/analytics branches rather than retaining a dark parallel journey. Keep only service/model pieces still used by the web checker or diagnosis. Update `.agents/product-marketing.md` so "Fit-First" describes background analysis and actionable guidance, not a mandatory extra screen.

**Rollback trigger:** if `optimization_started -> optimization_completed` drops more than 10% relative, duplicate optimize requests/credits occur, or unreadable-job errors increase materially, revert the routing change while keeping S0 instrumentation and the scorer fixes.

---

## Revised success signals

v1's signals were all PostHog funnel ratios. They cannot be evaluated (see below), and more importantly they would not have caught what the user actually experienced. Split into gates that are checkable now and signals that arrive later.

### Primary — deterministic, checkable at merge time

| Gate | Target | Today |
|---|---|---|
| G1 Perfect-match fixture reaches the top band | ≥ 85 | ~65 estimated ceiling |
| G2 Every weighted component varies across fixtures | ≥ 10 pt range each | 3 of 8 are effectively constant |
| G3 Same resume+job scores the same on both surfaces | within ±1 | 45 vs 42 observed |
| G4 Optimizations ending at ≤ +4 | < 10% | **41%** (24/59) |
| G5 Optimizations displaying a downward number | **0** | 6 of 59 |
| G6 Users shown a discouraging verdict before any value | **0** | 76% of free-checker users |
| G7 Taps from job supplied to exported PDF | reduced vs recorded baseline | not yet recorded |

### Secondary — PostHog, lagging confirm only

- at least 80% `analysis_cta_tapped -> optimization_started`;
- at least 20% relative improvement in `job_added -> optimization_started`;
- no regression in `optimization_started -> optimization_completed`, export success, crash/error rate, or duplicate credit consumption;
- movement toward the 20% founder-excluded launch-to-export activation target.

### Cohort reality

PostHog cannot referee this work at current volume. Over 60 days, filtering to non-internal-tester iOS traffic: `fit_check_completed` 2 people, `optimization_started` 2 people, `export_success` 2 people, `analysis_cta_tapped` 2 people. The `is_internal_tester=True` bucket resolves to 32–33 distinct "people" because simulator and QA runs each mint a new anonymous distinct_id — so raw person counts on that segment are not user counts and must not be quoted as such.

Consequences, binding on the execution session:

1. **Do not block a correct scorer fix waiting for a PostHog readout.** G1–G6 are the merge gates.
2. v1's S6 gate ("20 clean `analysis_cta_tapped` users or 14 days, whichever is later") will not be met on the current trajectory. Keep it as the *readout* trigger, not as a ship gate, and state the observed n in the readout whatever it is.
3. Run at least two more moderated sessions in the Meirav format after S1–S3 land. At n=2 organic users, a moderated session is a higher-quality signal than the funnel, and it is available this week.

### Open investigation (small, not blocking)

15 distinct non-tester people recorded `fit_check_completed` with a score of exactly **51**, and 17 recorded exactly **68**. Identical scores across many distinct people suggests a cached, fixture, or default value rather than real per-user scoring. Worth 30 minutes before S5 calibration, since it may mean part of the "real user score" evidence is not real.

---

## Files and surfaces likely involved

### Web/backend (S1–S5, S9)

- `src/lib/ats/core.ts` — shared `format_report` across both analyzer runs (D3)
- `src/lib/ats/integration.ts` — `scoreOptimization`, `resumeJsonToText`, format-report construction (D4, D5)
- `src/lib/ats/analyzers/keyword-phrase.ts` (D1), `metrics-presence.ts` (D2), `recency-fit.ts` (D4)
- `src/lib/ats/config/weights.ts`, `src/lib/ats/config/thresholds.ts` (D2, S5)
- `src/lib/ats/scorers/penalties.ts` (D2)
- `src/lib/ai-optimizer/optimize-pipeline.ts` — pass-selection floor (S2)
- `src/app/api/public/ats-check/route.ts`, `src/lib/ats/public-ats-check-response.ts` (D5, S3)
- `src/lib/ats/job-data-resolver.ts` and requirement extraction helpers (S4)
- `src/lib/ats/score-cache.ts` (S3)
- focused API, extraction, scorer, and calibration tests
- `tasks/progress.md`, `tasks/lessons.md`

### iOS (S6–S8)

- `Features/V2/Home/HomeTabView.swift:176`, `Features/Tailor/TailorView.swift:164`
- `Features/V2/Fit/` and `Core/API/FitCheckService.swift`
- `Core/API/Models/FitVerdict.swift:19-28` — band thresholds
- `Features/V2/Diagnosis/`, `Features/V2/Improve/`, `Features/V2/Preview/`
- `Core/DesignSystem/Components/ResumlyTabBar.swift` (S7 option b only)
- `App/DeepLinkRouter.swift` (S7 option b only)
- `Core/Analytics/AnalyticsService.swift` and contract tests
- `Resources/Localizable.xcstrings`
- `.agents/product-marketing.md`, `tasks/progress.md`, `tasks/session-log.md`

The executor must confirm exact call sites before editing. If any story expands beyond three unexpected files, stop and surface the revised scope.

---

## Constraints

- One story at a time. Do not bundle scorer repair with iOS routing.
- No new dependency, Supabase migration, production deploy, App Store submission, paid action, or production flag change without explicit founder approval in that execution session. **Rescoring historical rows counts as production data change.**
- Do not inflate scores to improve conversion. Repairing a component that cannot respond to evidence is not inflation; adding uplift, minimum scores, or positive-clamped deltas is. Every S1/S2 change must be defensible as increasing evidence-responsiveness.
- The user must never be shown their score going down as a result of using the product. Suppress, explain, and fix — do not clamp.
- No raw resumes, job descriptions, URLs, emails, or identifiers in analytics, fixtures, logs, or reports.
- Preserve the public web checker contract until its consumers are migrated and verified.
- Keep EN/HE parity and RTL behavior.
- Keep the score branded as Resumely's estimate, never an external ATS result.
- Existing user changes in dirty worktrees remain untouched. Both product repos currently have uncommitted files and stray `" 2.ts"` duplicates — do not sweep them as part of this packet.

## Validation matrix

| Layer | Required validation |
|---|---|
| Scorer integrity | perfect-match and clear-mismatch fixtures; per-component variance report; no constant component in the weighting |
| Before/after | symmetric-representation test; no-lift invariant test; replay of the 6 down / 2 flat cases |
| Cross-surface | same resume+job returns the same score from fit and optimize paths |
| Extraction | polluted/thin/valid/short-skill/LinkedIn/paste/HE fixtures |
| Calibration | benchmark + holdout + monotonicity + component-isolation; Strong demonstrably reachable |
| API | additive/backward-compatible response contract; unavailable recovery |
| iOS routing | Home + Tailor, one tap/one request, input preserved, no Fit sheet |
| iOS UI | EN/HE, RTL, Dynamic Type, reduced motion, score/no-score/no-lift states |
| Flow | recorded tap-and-screen count before and after S7 |
| Build | targeted tests, full relevant suite, Debug simulator build, Release build before ship |
| Analytics | internal smoke rows plus founder/QA/bot-excluded cohort query, with observed n stated |
| Product | direct path reaches result and export without a discouraging gate |

## Completion gate

- Product-repo progress/session files updated per local AGENTS.md.
- Every story has evidence, not a code-only claim.
- G1–G7 recorded with before and after values.
- PostHog readout links the exact cohort/window and exclusion rules, and states the observed n honestly even when it is small.
- Product-marketing context reflects the amended background-fit journey.
- Old WP-12/WP-13 artifacts remain historical; this packet and the 2026-07-12 + 2026-07-24 decisions are the active direction.

## Final output for each story

- What changed and why
- Files changed
- Tests/builds/smokes run with results
- Metric or gate affected and how it was measured
- Remaining risks and rollback condition
- What was not done
- Git branch, PR, merge, and push state
