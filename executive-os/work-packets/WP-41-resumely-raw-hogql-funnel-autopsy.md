# WP-41 — Resumely Raw HogQL Funnel Autopsy

- **Status:** Active — run on or after 2026-07-18; definitive read preferred on 2026-07-25
- **Mode:** Grower
- **Workflow pattern:** normal
- **Input trust:** trusted local context + read-only production analytics
- **Project:** Resumely iOS, `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- **PostHog:** project `270848` (`ResumeBuilder AI`)
- **Metric / funnel step:** 1.4.1 first-session activation, from upload CTA exposure through export; primary diagnostic is picker-open → file-selected conversion
- **Success signal:** one exact, reproducible clean-cohort table names the single largest absolute real-user loss, with entrants, drop-offs, conversion rates, sample size, and raw-person evidence.

## Goal

Pull the actual Resumely iOS PostHog event stream for the clean App Store 1.4.1 cohort, reconstruct the ordered activation funnel person by person, and quantify the one step where the most non-founder, non-QA, non-bot users vanish.

## Read First

1. Repo `AGENTS.md`, `tasks/progress.md`, `tasks/lessons.md`, and `tasks/ERRORS.md` if present.
2. `tasks/progress.md` entry **“PostHog picker→file-selected funnel re-read — DEFERRED (2026-07-11)”**.
3. Agentic OS `executive-os/reviews/2026-07-05-activation-reread.md`, especially its same-day event-name correction.
4. Agentic OS `executive-os/work-packets/WP-37-resumely-activation-followups.md`, Verify story.
5. PostHog project `270848` schema/event definitions. Use the connected PostHog app and its current HogQL documentation rather than guessing syntax.

## Task

### 1. Prove the cohort definition before calculating the funnel

Query a small raw sample first and confirm exact property names, types, timezone, and event availability. Then use this cohort:

- App: `properties.app = 'resumely_ios'`.
- Marketing version: `properties.marketing_version = '1.4.1'` (handle string typing explicitly).
- Window: `2026-07-11T00:00:00` in the PostHog project timezone through query execution time. State the project timezone and exact UTC bounds in the report.
- Production only: exclude rows where `is_internal_tester = true`, robust to boolean/string/null representation.
- Exclude known founder/QA/bot person-id prefixes: `067544b5`, `761e5b1b`, `a6441489`, `712cf425`.
- Keep `$lib = 'resumely-ios-urlsession'` as a validation column. If filtering by it would remove otherwise valid `app=resumely_ios` 1.4.1 production events, show the discrepancy and use the app/version cohort as canonical.
- Check whether the PostHog cohort **Founder + QA exclusion** (`394227`) matches the explicit exclusions. Do not silently substitute it because earlier evidence says email is not reliably present on events.

Before proceeding, print a cohort audit: raw distinct people, people removed by each exclusion reason, clean distinct people, and overlap between exclusion reasons. A person excluded once stays excluded from every step.

### 2. Pull the raw event stream

Run HogQL over `events` for every clean person and return at least:

- `person_id` / canonical distinct person identifier used for counting
- `distinct_id`
- `event`
- `timestamp`
- `uuid`
- `$session_id` when present
- `app`, `marketing_version`, `build_number`, `is_internal_tester`, `$lib`
- safe reconciliation IDs when present (`anonymous_session_id`, `resume_id`, `job_description_id`, `optimization_id`, `review_id`)

Events in scope:

`app_launched`, `guest_mode_started`, `resume_upload_cta_seen`, `resume_upload_cta_tapped`, `resume_file_picker_opened`, `resume_file_picker_cancelled`, `resume_file_selected`, `resume_upload_started`, `resume_upload_succeeded`, `resume_uploaded`, `job_added`, `optimization_started`, `optimization_completed`, `optimized_viewed`, `export_cta_seen`, `export_pdf_tapped`, `export_started`, `export_success`, `export_failed`, `submit_package_saved`.

Order by person and timestamp. Save the exact HogQL and a privacy-safe raw extract or aggregate evidence under `docs/qa/reports/`; do not store emails, resume content, job text, tokens, or full person identifiers in git. Hash/redact identifiers in saved evidence while keeping stable joins.

### 3. Reconstruct one ordered clean-cohort funnel

Build an ordered, same-person funnel using first qualifying occurrence after the prior step. Do not use independent per-event distinct counts as if they were a funnel.

Canonical steps:

1. `app_launched`
2. `resume_upload_cta_seen`
3. `resume_upload_cta_tapped`
4. `resume_file_picker_opened`
5. `resume_file_selected`
6. upload complete, canonical cross-version event `resume_uploaded`; use `resume_upload_succeeded` only as the 1.4.1 diagnostic and reconcile the two
7. `job_added`
8. `optimization_started`
9. `optimization_completed`
10. `optimized_viewed`
11. `export_cta_seen`
12. `export_pdf_tapped`
13. `export_success`

Use a 1-hour conversion window for `resume_file_picker_opened → resume_file_selected`, matching the deferred read. For the full first-session funnel, use `$session_id` where coverage is reliable; otherwise use a documented 24-hour window from each person's first `app_launched`. Report session-ID coverage and do not mix window definitions silently.

Treat `resume_file_picker_cancelled` and `export_failed` as side exits, not sequential success steps. Quantify them against the eligible upstream population.

### 4. Produce the exact drop-off table and name one bottleneck

The report table must include:

| Step | Eligible entrants | Reached step | Lost at step | Step conversion | Cumulative conversion | Side-exit count |
|---|---:|---:|---:|---:|---:|---:|

Define `Lost at step = eligible entrants - reached step`. Rank steps by **absolute clean-person loss**. Name exactly one largest-loss step. For that step report:

- `N` eligible real users
- `N` reached the next step
- `N` vanished
- `%` step conversion and `%` drop-off
- the top raw event-path patterns among those lost
- whether the result is decision-grade or only directional

Tie-breaker: if absolute losses tie, choose the lower conversion rate; if still tied, choose the earlier step and disclose the tie.

Also publish the narrower picker diagnostic beside the full table: opened, selected within 1h, cancelled, neither selected nor cancelled. Compare 1.4.1 conversion to the documented 60-day baseline `13 → 6` (46%) only when definitions truly match.

### 5. Interpret without overclaiming

- If picker openers are `< 10`, quantify the result but label it underpowered and defer product changes; still name the observed largest loss.
- If there are zero clean people, report **no readable cohort**, not 0% conversion.
- If event ordering is logically impossible, stop interpretation, show the conflicting raw paths, and resolve identity/event taxonomy before naming a product bottleneck.
- Do not repeat the 2026-07-05 mistake: `resume_uploaded` is the historical upload denominator; `resume_upload_succeeded` is newer granular instrumentation.

## Deliverables

1. `docs/qa/reports/resumely-1.4.1-raw-hogql-funnel-autopsy-YYYY-MM-DD.md` containing scope, timezone, exact HogQL, exclusion audit, clean funnel table, ranked losses, the single bottleneck, caveats, and PostHog links.
2. A privacy-safe CSV or Markdown appendix of per-person ordered paths, if small enough to review; otherwise aggregate path groups plus query instructions.
3. Update `tasks/progress.md` with the quantified result and next action. Update `tasks/lessons.md` only for a genuinely reusable new analytics lesson.

## Constraints

- Read-only PostHog work. Do not create/update dashboards, cohorts, or insights unless the founder explicitly asks.
- No app code, UX, instrumentation, backend, deploy, App Store, or dependency changes.
- Never print or commit `AGENTIC_OS_POSTHOG_API_KEY` or any token.
- Do not claim “real users” until the exclusion audit is complete.
- Do not collapse anonymous and identified IDs without proving the `$create_alias` / `$identify` join from raw events.

## Validation

- Re-run the final HogQL once and confirm the same counts at a stated query timestamp.
- Independently reconcile each funnel-step count against grouped clean `person_id` sets from the raw extract.
- Verify no excluded prefix appears in the final person set.
- Verify `Lost at step` arithmetic and percentages programmatically or with a second query.
- Run `git diff --check`, inspect the report and progress diff, then commit and push on a product-repo branch per that repo's session-end rules.

## Final Output

Lead with one sentence in this form: **“The largest clean-cohort loss is X → Y: A of B real users vanished (C% drop-off; D reached Y), queried through TIMESTAMP.”** Then list files changed, query/check evidence, caveats, open questions, and what was not done.
