# WP-45 — Resumely Direct Optimize + Trustworthy Score Calibration

- **Status:** Ready
- **Created:** 2026-07-12
- **Mode:** Grower
- **Workflow pattern:** normal, one story at a time; web contract before score UI; cross-vendor review for the scorer change
- **Input trust:** trusted local code, privacy-safe PostHog aggregates, privacy-safe Supabase aggregates, and founder direction on 2026-07-12
- **Projects:** Resumely iOS and ResumeBuilder Web/backend
- **Source:** 2026-07-12 founder direction and score investigation; supersedes the pre-optimization iOS gate in WP-12/WP-13
- **Related decisions:** 2026-06-20 branded Match Score; 2026-06-23 Fit-First thresholds; 2026-07-02 20% activation target; 2026-07-12 remove the pre-optimization Fit gate
- **Metric / funnel step:** founder-excluded `job_added -> analysis_cta_tapped -> optimization_started -> optimization_completed -> export_success`
- **Memory update:** iOS and web `tasks/progress.md`, `tasks/session-log.md`, and `tasks/lessons.md` only if a reusable correction is learned
- **Success signal:** the redundant iOS step is gone; at least 80% of clean `analysis_cta_tapped` users reach `optimization_started`; `job_added -> optimization_started` improves at least 20% relative to the pre-release baseline; no low-confidence result is shown as a hard score; launch-to-export continues toward the existing 20% target

## Owner Role

Product Manager for story sequencing; Director/Scrum/TDD executor inside each product repo; independent cross-vendor reviewer for the scoring contract and calibration suite.

## Why this packet exists

The current authenticated iOS journey asks for the same intent twice:

```text
Resume + job already supplied
-> Analyze
-> FitCheckView repeats the job link and offers another description field
-> Check Fit
-> low Strong/Stretch/Weak verdict
-> Optimize for This Job
-> actual optimization
```

The second screen made sense in the original Fit-First triage concept, where the product wanted users to decide whether a role was worth pursuing before spending an optimization credit. It no longer fits the observed activation goal. The user has already chosen the role, supplied its data, and asked the app to analyze it. The screen adds duplicate input, a second CTA, another network dependency, and an emotionally negative exit before the user experiences the core value.

The score itself is also not ready to carry that decision. The 2026-07-12 audit found:

- PostHog: 17 iOS `fit_check_completed` events in 60 days, all marked internal tester. Scores were 68 x12, 66 x3, 25 x1, and 27 x1. There is no organic iOS score cohort.
- Supabase `anonymous_ats_scores`, same shared engine: 47 rows in 60 days, mean 36.3, median 39, 31 below 50, 0 at or above 75, maximum 51. This is mostly anonymous web activity, not unique iOS users, but it proves the engine's scale is compressed below its own Strong threshold.
- The screenshot's stored 25 had semantic relevance 68 and section completeness 75, but keyword 25, title 21, metrics 0, and phrase match 0. Its weighted base of about 38 lost another 13 points through penalties.
- The displayed “fit” number is `score.overall = ats_score`; its weights include format, metrics, section completeness, and recency. That is a general resume-readiness composite, not a job-only fit measure.
- The screenshot's missing-keyword list included fragments such as “about,” “role objective,” and “key responsibilities build,” demonstrating extraction pollution in a user-visible result.

## Product decision and amended journey

### Remove

- The authenticated Home/Tailor presentation of `FitCheckView` after Analyze.
- The repeated “Using Job Link” confirmation card and optional job-description field when the job was already supplied.
- The second “Check Fit” CTA.
- The pre-optimization red `Weak Fit` gate and “Browse Other Jobs” exit.
- The expectation that `fit_check_optimize_tapped` remains part of the new activation path.

### New authenticated iOS journey

```text
Resume + job supplied
-> Analyze & Optimize (one intent, one CTA)
-> validate existing inputs and job-extraction quality
-> start optimization directly
-> show honest loading states backed by real work
-> Diagnosis / Optimization Review
   -> starting alignment, confidence, gaps, and targeted improvements
   -> continue to review, apply edits, and export
```

If a URL cannot be read reliably, stay on the original input surface and show one actionable recovery: “We couldn't read the full job from this link. Paste the job description to continue.” Preserve the resume, URL, and any pasted text. Do not open a second Fit screen and do not return a guessed score.

### Score placement

- **Before calibration:** do not show a numeric pre-optimization score or Strong/Stretch/Weak band in the authenticated activation path. Show progress and, after optimization completes, specific gaps/opportunities.
- **After calibration:** show the job-only fit as contextual starting guidance inside Diagnosis/Review, never as permission to optimize. Low fit can be honest, but the primary action remains improving the resume the user asked to optimize.
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
2. Exact weights and band thresholds are not guessed in code. They are selected from the benchmark in Story 4.
3. `available=false` when extraction quality is insufficient. In that state the response carries a recovery reason, no score, and no band.
4. Requirement extraction rejects headings/navigation fragments and preserves meaningful phrases. A generic stop list alone is insufficient; the quality gate must consider phrase shape, source section, minimum credible requirement count, and extraction provenance.
5. The existing `score.overall` remains backward-compatible for the public web checker during migration, but iOS must not silently substitute it for missing `fit.score` after `fit_v2` launches.
6. No resume text, job-description text, URLs, emails, or identifiers are added to analytics.

## Stories

| Story | Repo | Mode | Model route | Outcome |
|---|---|---|---|---|
| S0 — Measurement contract and baseline | iOS + PostHog | Grower | GPT-5.6 Sol or Claude Fable 5 | Establish a clean before/after funnel without changing UX |
| S1 — Remove the redundant iOS gate | iOS | Sweeper/Grower | GPT-5.6 Sol; cross-vendor review | One CTA starts optimization directly |
| S2 — Extraction-quality gate | Web/backend | Builder | Claude Fable 5 or GPT-5.6 Sol | Junk requirements cannot produce a confident score |
| S3 — Dedicated versioned fit contract | Web/backend | Builder | GPT-5.6 Sol; cross-vendor review | Fit and ATS readiness are separate concepts |
| S4 — Calibration benchmark and bands | Web/backend | Maintainer | GPT-5.6 Sol + independent reviewer | Bands reflect labeled evidence, not arbitrary uplift |
| S5 — Diagnosis/result UX | iOS | Grower | GPT-5.6 Sol | Guidance motivates action after optimization starts |
| S6 — Release, readout, and cleanup | iOS + PostHog | Maintainer | Claude Fable 5 or GPT-5.6 Sol | Verify activation lift and remove dead Fit-first code |

### S0 — Measurement contract and baseline

Add or verify these privacy-safe fields on the existing iOS analytics envelope before changing the flow:

- `flow_version`: `fit_gate_v1` or `direct_optimize_v2`
- `score_version`
- `job_input_source`: paste or URL
- `extraction_quality`: high, medium, low, unavailable
- `requirement_count_bucket`: 0, 1-2, 3-5, 6+
- `score_bucket`; use a numeric PostHog property for raw score if the transport can support typed values safely
- `is_internal_tester`, `app`, `marketing_version`, and `build_number` on every relevant event

Add `analysis_cta_tapped` at the single user intent point. Keep existing `fit_check_started` / `fit_check_completed` during migration with `flow_version`; deprecate `fit_check_optimize_tapped` for `direct_optimize_v2`. Do not rename historical events in place.

Capture a founder/QA/bot-excluded baseline for:

- `job_added -> analysis_cta_tapped`
- `analysis_cta_tapped -> optimization_started`
- `optimization_started -> optimization_completed`
- `optimization_completed -> optimized_viewed -> export_success`
- median time from `analysis_cta_tapped` to `optimization_started` and `optimization_completed`

Acceptance: event contract tests pass; a marked internal simulator/device smoke produces one correctly attributed row per event; the baseline query and timestamp are saved without PII.

### S1 — Remove the redundant iOS gate

In both live entry points, Home and Tailor:

1. Preserve the already-entered resume, pasted JD, and job URL.
2. On Analyze, call the existing upload/preparation helper once, then proceed directly to the existing optimize function.
3. Do not present `FitCheckView`, run a separate blocking public-ATS request, or require `onOptimize` from a verdict sheet.
4. Keep duplicate-tap protection, current cancellation behavior, and actionable connection errors.
5. Use the existing diagnosis/review destination after optimization; do not add a new destination.
6. Change the visible CTA to “Analyze & Optimize” only if user testing shows “Analyze” does not already set the correct expectation. Keep EN/HE copy concise and RTL-safe.

Tests must prove:

- one tap produces at most one upload/preparation and one optimize request;
- the job link or paste supplied earlier reaches optimize unchanged;
- no Fit sheet is presented;
- success reaches Diagnosis/Review;
- unreadable job recovery preserves all prior input;
- direct optimize does not consume more credits than the current optimize call.

Acceptance: focused view-model/routing tests, Debug build, EN/HE localization export, and real simulator/device smoke from Home and Tailor.

### S2 — Add the extraction-quality gate

Strengthen the shared job resolver used by `/api/public/ats-check` and optimization preparation:

- filter structural headings and fragments such as “about,” “role objective,” and malformed “key responsibilities build”;
- retain valid short requirements such as SQL, AWS, or CRM through allowlisted shape rules rather than a blunt word-count filter;
- score extraction quality from source provenance, usable text length, credible requirement count, junk ratio, and title availability;
- fail closed when URL extraction is thin or polluted: return a typed recovery response requesting pasted JD;
- preserve the existing LinkedIn guest-endpoint strategy and do not fall back to a thin authwall snippet.

TDD fixtures must include technical, non-technical, Hebrew, LinkedIn URL, pasted JD, sparse-but-valid, and polluted-heading examples. No production scrape or database migration is part of this story.

Acceptance: targeted tests fail before the change and pass after; no known valid short skill is removed; polluted fixtures return `fit.available=false` or a clean requirement set; lint, type-check for touched files, and production build pass.

### S3 — Implement the dedicated `fit_v2` contract

Create a separate job-fit calculation from the existing general ATS/readiness composite:

- inputs: semantic alignment, cleaned requirement coverage, title/seniority alignment, and extraction confidence;
- excluded: format, metrics presence, generic sections, and recency hygiene;
- output: `available`, score, band, confidence, version, extraction metadata, top gaps, and missing keywords;
- backward compatibility: keep existing response fields and public web behavior until its UI is migrated;
- iOS decoding: when `scoreVersion == fit_v2`, never replace `fit.score` with `score.overall`.

Do not select final weights or bands in this story. Implement the components and a configurable calibration table, then keep numeric/band display disabled until S4 passes.

Acceptance: contract tests cover snake/camel decoding, unavailable results, boundary safety, backwards compatibility, and separation from ATS/readiness components. Changing format or metric count alone must not change `fit_v2` for the same resume/job evidence.

### S4 — Calibrate with labeled evidence

Create a privacy-safe benchmark of 30-50 synthetic or consented resume/job pairs spanning technical, commercial, operational, junior, senior, career-switch, English, and Hebrew cases. No production resume or JD content is copied into the repo.

For each pair, record independent human labels for Strong, Stretch, or Weak plus the decisive reasons. Use the set to choose component weights and band thresholds. Required gates:

- no artificial flat uplift or hardcoded minimum score;
- Strong must be reachable for clearly aligned pairs;
- false-Weak rate below 10% for pairs labeled Strong or Stretch;
- monotonicity: adding truthful relevant evidence cannot lower fit;
- irrelevant format/metric changes cannot move fit;
- polluted or thin extraction yields unavailable/low confidence, not Weak;
- calibration and holdout results are reported separately.

Acceptance: deterministic benchmark runner, documented results, holdout results, and reviewer approval. Only then enable numeric `fit_v2` and its bands.

### S5 — Move guidance into Diagnosis/Review

After optimization has started or completed, present guidance as a starting point and action plan:

- high-confidence calibrated fit: concise starting alignment, top gaps, and what the optimization changed;
- low/unavailable confidence: no number or band, only verified gaps and a prompt to improve the JD input if needed;
- low score copy: supportive and specific, for example “This resume starts with several gaps for this role. We prepared targeted improvements for review.”;
- remove “Weak Fit” as a red pre-action verdict and remove “Browse Other Jobs” from the primary optimization journey;
- keep the primary next action aligned with review/apply/export, not abandonment;
- retain the Resumely Match Score disclosure and never imply an employer/vendor ATS score.

Acceptance: screenshots and accessibility snapshots for EN/HE, RTL, Dynamic Type, reduced motion, and score/no-score states; simulator smoke confirms the user cannot become trapped after optimization.

### S6 — Release, readout, and dead-code cleanup

Ship behind the existing build/release process, not a production toggle that does not exist. Mark founder/QA traffic. After the first release cohort reaches at least 20 clean `analysis_cta_tapped` users or 14 days, whichever is later, compare against S0:

- primary: at least 80% `analysis_cta_tapped -> optimization_started`;
- lift: at least 20% relative improvement in `job_added -> optimization_started`;
- guardrails: no regression in `optimization_started -> optimization_completed`, export success, crash/error rate, or duplicate credit consumption;
- north star: movement toward 20% founder-excluded launch-to-export activation.

If the direct path is healthy, delete unreachable `FitCheckView` entry UI and obsolete routing/analytics branches rather than retaining a dark parallel journey. Keep only service/model pieces still used by the web checker or diagnosis. Update product-marketing context so “Fit-First” describes background analysis and actionable guidance, not a mandatory extra screen.

Rollback trigger: if `optimization_started -> optimization_completed` drops more than 10% relative, duplicate optimize requests/credits occur, or unreadable-job errors increase materially, revert the routing change while keeping S0 instrumentation and the extraction fixes.

## Files and surfaces likely involved

### iOS

- `Features/V2/Home/HomeTabView.swift`
- `Features/Tailor/TailorView.swift`
- `Features/V2/Fit/` and `Core/API/FitCheckService.swift`
- Diagnosis/Optimization Review view and view model identified by call-site search
- `Core/Analytics/AnalyticsService.swift` and contract tests
- `Resources/Localizable.xcstrings`
- `.agents/product-marketing.md`, `tasks/progress.md`, `tasks/session-log.md`

### Web/backend

- `src/app/api/public/ats-check/route.ts`
- `src/lib/ats/public-ats-check-response.ts`
- `src/lib/ats/job-data-resolver.ts` and requirement extraction helpers
- dedicated fit scorer/config under `src/lib/ats/`
- focused API, extraction, scorer, and calibration tests
- `tasks/progress.md` and `tasks/lessons.md` if warranted

The executor must confirm exact call sites before editing. If any story expands beyond three unexpected files, stop and surface the revised scope.

## Constraints

- One story at a time. Do not bundle scorer calibration with iOS routing.
- No new dependency, Supabase migration, production deploy, App Store submission, paid action, or production flag change without explicit founder approval in that execution session.
- Do not inflate scores to improve conversion. Improve semantic validity, calibration, confidence handling, and placement.
- No raw resumes, job descriptions, URLs, emails, or identifiers in analytics, fixtures, logs, or reports.
- Preserve the public web checker contract until its consumers are migrated and verified.
- Keep EN/HE parity and RTL behavior.
- Keep the score branded as Resumely's estimate, never an external ATS result.
- Existing user changes in dirty worktrees remain untouched.

## Validation matrix

| Layer | Required validation |
|---|---|
| Extraction | polluted/thin/valid/short-skill/LinkedIn/paste/HE fixtures |
| Scoring | benchmark + holdout + monotonicity + component-isolation tests |
| API | additive/backward-compatible response contract; unavailable recovery |
| iOS routing | Home + Tailor, one tap/one request, input preserved, no Fit sheet |
| iOS UI | EN/HE, RTL, Dynamic Type, reduced motion, score/no-score states |
| Build | targeted tests, full relevant suite, Debug simulator build, Release build before ship |
| Analytics | internal smoke rows plus founder/QA/bot-excluded cohort query |
| Product | direct path reaches Diagnosis/Review and export without a discouraging gate |

## Completion gate

- Product-repo progress/session files updated per local AGENTS.md.
- Every story has evidence, not a code-only claim.
- PostHog readout links the exact cohort/window and exclusion rules.
- Product-marketing context reflects the amended background-fit journey.
- Old WP-12/WP-13 artifacts remain historical; this packet and the 2026-07-12 decision are the active direction.

## Final output for each story

- What changed and why
- Files changed
- Tests/builds/smokes run with results
- Metric or funnel step affected and how it will be measured
- Remaining risks and rollback condition
- What was not done
- Git branch, PR, merge, and push state
