# Portfolio Activation Playbook v2

- Status: Current operating doctrine and roadmap
- Effective: 2026-07-12 through the 2026-08-01 EXD-015 review
- Allocation: Resumely 70% / RunSmart 30%
- Owner: Founder, routed through the existing CEO/COO, work-packet, and experiment-log system
- Governing decisions: EXD-009, EXD-013, EXD-015, EXD-016, EXD-018, EXD-021
- Supersedes for current action: `executive-os/reviews/2026-07-11-activation-strategy-synthesis.md`

This document is the canonical activation doctrine for RunSmart and Resumely and the dated roadmap for the current activation window. Historical reviews remain evidence snapshots; they are not rewritten when later data changes the action.

## 1. Operating definition

Activation is not onboarding completion or output generation. It is the point at which a new user has received a relevant result, recognized enough value to act on it, and completed the first outcome that makes returning rational.

Use five stages:

`Intent → Setup → First value → Verified value → Repeat value`

- **Intent:** the user states the job they need completed.
- **Setup:** the minimum inputs needed to produce a credible result.
- **First value:** the product produces the first job-relevant result.
- **Verified value:** the user acts in a way that indicates the result was understood or trusted.
- **Repeat value:** the user completes the outcome or begins the next value cycle.

One primary activation outcome governs each product. Earlier events are leading diagnostics, not competing definitions.

## 2. Portfolio allocation and gates

- Resumely receives 70% of activation effort through 2026-08-01.
- RunSmart receives 30%, limited to closing already-started WP-40 release evidence and measuring shipped activation paths.
- Ship no new RunSmart activation feature until a clean cohort or a reproducible technical defect identifies the next bottleneck.
- Keep monetization, paywalls, paid acquisition, Garmin expansion, and RunSmart Hebrew-first distribution closed under the existing decisions.
- Do not add iCloud Documents capability for WP-44 S1. That story is dropped from the active path unless the founder separately approves the capability change.
- Run one product experiment per app at most. Do not create a second activation backlog outside the existing experiment log and work packets.

## 3. Canonical metric contract

| Stage | RunSmart | Resumely |
|---|---|---|
| Intent / setup | onboarding started and completed | upload CTA → input supplied → job added |
| First value | `plan_generated` | `free_ats_completed` or first job-specific diagnosis |
| Verified value | `first_run_cta_tapped` with `start_now` or `remind_me` | `optimization_completed` → `optimized_viewed` |
| Primary activation | `run_completed` within 7 days of first physical App Store install | `export_success` within 7 days of first seen |
| Repeat value | second planned workout or week-one adherence | another job/resume cycle or return within 14 days |

Portfolio targets:

- RunSmart: at least 30% D7 install → `run_completed`.
- Resumely: at least 20% D7 first-seen → `export_success` by the 2026-08-01 EXD-015 review.
- First-session activation and time to first value remain leading diagnostics.

### Evidence contract

- Exclude founder, QA, bot, emulator, TestFlight, and sideloaded traffic before using the word “real.”
- Construct ordered same-person funnels. Independent event totals are not a funnel.
- Require at least 10 eligible users at the examined step before making a funnel-only product recommendation.
- Below 10, allow a change only when the same issue appears in at least 3 of 5 relevant-user observations or a technical failure is reproducible.
- Run final cohort queries twice, reconcile person sets and arithmetic, and record timezone, window, version/build, query timestamp, and exclusions.
- Never send resume text, job text, health data, routes, emails, or full identifiers to analytics or committed evidence.

## 4. AI trust pattern

Every new activation story must satisfy the TRUST checklist without adding a product tour:

- **Transparent inputs:** show the user-visible facts used.
- **Reasoned output:** provide a concise rationale, not chain-of-thought.
- **User control:** allow correction, rejection, editing, or safe retry where the product supports it.
- **Safe uncertainty:** label missing data and estimates honestly.
- **Tight feedback:** ask a specific, local question beside the result.

The product should show transformation, not generic AI celebration. RunSmart explains why the first week fits the runner. Resumely shows the job requirement, existing evidence, proposed change, and why it matters without inventing experience or metrics.

## 5. Submitted playbook compared with live Agentic OS

| Recommendation | Current state | Operating decision |
|---|---|---|
| Define first, verified, and repeat value | Partially represented across metrics and reviews | Adopt the single contract in this document |
| Instrument first-run commitment | Shipped in RunSmart 1.0.7 (21) through WP-20/WP-15 | Measure; do not rebuild |
| Move HealthKit into the first-run path | WP-40 S1+S2 merged; S3/S4 evidence in release closeout | Finish handoff, then wait for a clean cohort |
| Improve web entry funnel | All six WP-43 Tier A changes merged in PR #115 | Measure `ats_checker_hero_cta_clicked` → `ats_checker_submitted` |
| Open iOS picker on a populated folder | WP-44 S1 blocked because the app has no iCloud Documents capability | Drop from active path |
| Add paste-resume input | No dedicated canonical text-upload contract; existing agent endpoint is the wrong path | Evidence-gated behind 2026-07-18 and 3-of-5 observation rule |
| Fix export | Web observability merged; D7 Resumely cohort has 0 optimizations and 0 exports | Wait for 5 clean completers or a reproducible failure |
| Add a weighted activation score | No retention comparison and insufficient activated users | Defer |
| Redesign onboarding broadly | Existing focused fixes are shipped; cohorts remain small | Reject until evidence shows structural failure |
| Run many A/B tests | Traffic is too low | Use observed sessions, sequential release, and directional cohorts |
| Expand GTM | Activation remains 0% in both current D7 cohorts | Keep paid/high-volume gates closed |

## 6. Current truth as of 2026-07-12

- RunSmart: 13 clean mature installs → 1 onboarding → 1 plan → 0 run starts/completions within D7.
- Resumely: 73 clean mature first-seen people → 9 uploads → 0 optimizations/exports within D7.
- WP-20 first-run CTA/reminder is already shipped.
- WP-40 S1+S2 is merged. S3 physical-device evidence, the S4 re-read, and the 1.0.8 (22) archive record are preserved in RunSmart commit `d9ce8fa`; the clean external cohort remains empty.
- WP-43 is merged and ready for measurement.
- WP-44 S1 is blocked and dropped. S2 is gated; S3 stays later.
- The manual claim of one founder-excluded cumulative iOS export conflicts with the saved clean July 6 evidence showing zero. Treat cumulative export as **under review** until a reproducible query resolves it. The current D7 export result is unambiguously 0/73.

## 7. Dated roadmap

### 2026-07-12 through 2026-07-17: establish current truth

1. Confirm App Store Connect processing for the founder-archived RunSmart 1.0.8 (22), then run the documented TestFlight smoke when the build is available. No agent-triggered release action.
2. Measure the shipped RunSmart path:
   `install → onboarding_completed → plan_generated → first_run_cta_viewed → first_run_cta_tapped → first_run_reminder_scheduled or run_started → run_completed`.
3. Observe five right-fit Resumely first sessions. Record whether the person has a usable resume file on the phone, where they hesitate, whether they understand the diagnosis, and whether they reach a usable export.
4. Observe three phone-only beginner/returning RunSmart sessions. Focus on listing expectation, onboarding start, plan comprehension, and first-run commitment.
5. Review existing ASO drafts only. Publishing remains a founder approval gate.

### Observation protocol

Use the same capture for every session:

| Field | Record |
|---|---|
| Participant fit | Why this person matches the target user |
| Starting job | What they expected the app to do |
| Input availability | Resume file location or recent-run information available |
| First value | First moment they described as useful |
| Trust friction | What made them uncertain or looked generic/wrong |
| Next action | What they believed they should do next |
| Outcome | Export/run commitment/run completion reached or not |
| Repeated issue tag | Stable short label used across sessions |

Do not store personal resume, job, health, or account data in Agentic OS. Save only redacted observations and aggregate repeated issue counts.

### 2026-07-18: minimum Resumely gate

Re-run WP-41 with the established exclusion and ordered-funnel method.

- With at least 10 picker openers, select the largest absolute loss.
- With fewer than 10, do not infer a bottleneck from percentages.
- If at least 3 of 5 observed users lacked a usable local file, activate WP-44 S2.
- If users supplied files but failed later, target the observed downstream step instead.
- If at least 5 clean users complete optimization, inspect `optimized_viewed`, export intent, failure, and success. Change export only for a reproducible defect or a repeated 3-of-5 comprehension issue.

### Conditional WP-44 S2 interface

If the gate opens, extend the existing authenticated `/api/upload-resume` multipart contract:

- Accept exactly one of `resume` or `resumeText`; reject both or neither.
- Reuse the current parsing, `raw_text` persistence, optimization, privacy, and response path, including `resumeId`.
- Use the iOS client’s existing fields-only multipart helper.
- Do not route this traffic through `/api/agent/run`.
- Emit `resume_paste_started`, `resume_paste_submitted`, and `resume_paste_failed`, plus a safe `input_method` property on shared downstream events.
- Never attach the pasted content to analytics.
- Add no migration unless the implementation audit proves existing `raw_text` storage cannot support the same lifecycle.

### 2026-07-19 through 2026-07-24: one Resumely experiment

Ship exactly one evidence-selected intervention:

1. Paste-text input, if local-file absence is confirmed.
2. Post-optimization routing/value comprehension, if optimization completes but the result is not viewed.
3. Export CTA/reliability, if the result is viewed but no usable file is obtained.

RunSmart receives no new experiment unless a clean cohort identifies a reproducible blocker.

### 2026-07-25 through 2026-08-01: definitive reads and portfolio decision

- Run the 14-day Resumely 1.4.1 read on 2026-07-25.
- Re-run RunSmart WP-42 after at least one clean post-WP-40 disclosure viewer; require 10 before changing the HealthKit path.
- Compare activated and non-activated retention only when both groups exist.
- On 2026-08-01, run one CEO/COO review: continue Resumely, shift attention to RunSmart, revisit existing gates, or stop an unsuccessful lane.

## 8. Validation contract

Agentic OS changes:

- Parser unit tests.
- Portfolio HQ trust/privacy tests.
- `./agentic-os refresh`.
- `./agentic-os verify`.
- `git diff --check`.

RunSmart release/measurement:

- Focused first-run CTA/reminder tests.
- Relevant HealthKit tests and build.
- Simulator smoke and existing physical-device evidence.
- No App Store action without explicit current approval.

Conditional Resumely paste path:

- API tests: file-only, text-only, both rejected, neither rejected, authentication, redaction, and unchanged response shape.
- iOS tests: submission, failure recovery, analytics redaction, and file-upload regression.
- Build and physical-device smoke.

Completion means Portfolio HQ shows one primary activation definition per app, explicit sample sizes, at most one current experiment per app, and the next evidence gate.
