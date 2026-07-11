# WP-42 — RunSmart HealthKit Raw HogQL Funnel Autopsy

- **Status:** Active — run when the first post-WP-40 production cohort exists
- **Mode:** Grower
- **Workflow pattern:** normal
- **Input trust:** trusted local context + read-only production analytics
- **Project:** RunSmart iOS, `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
- **PostHog:** project `171597` (`Running coach`)
- **Metric / funnel step:** WP-40 Apple Health disclosure → connect → first successful sync
- **Success signal:** one exact, reproducible clean-cohort table names the single largest absolute real-user loss in the new HealthKit path, with counts, conversion rates, raw-event paths, and a defensible post-ship cohort anchor.

## Goal

Pull the actual RunSmart PostHog event stream for the first production cohort exposed to WP-40, exclude founder and QA traffic before counting, reconstruct the ordered Apple Health connect-to-sync journey person by person, and quantify the one step where the most real users vanish.

## Read First

1. Repo `AGENTS.md`, `tasks/progress.md`, `tasks/todo.md`, `tasks/session-log.md`, `tasks/ERRORS.md`, and `tasks/lessons.md` if present.
2. Agentic OS `executive-os/work-packets/WP-40-runsmart-healthkit-activation.md`, especially S1, S2, and S4.
3. `IOS RunSmart app/Services/Analytics/AnalyticsEvents.swift` definitions for `healthkit_disclosure_viewed`, `healthkit_connect_tapped`, and `healthkit_sync_completed`.
4. The shipped WP-40 implementation and release/version evidence in the product repo. Do not assume the Agentic OS packet's stale “not started” status is current.
5. PostHog project `171597` schema/event definitions. Use the connected PostHog app and current HogQL documentation rather than guessing syntax.

## Task

### 1. Establish the first valid WP-40 production cohort

Do not choose a date or app version from memory. Derive and document all of these from live raw events plus repo release evidence:

- exact production marketing version/build that first contains merged WP-40 S1/S2
- first timestamp that version emitted `healthkit_disclosure_viewed` in production
- PostHog project timezone and exact UTC query bounds
- canonical iOS app/library properties that separate RunSmart native production traffic from web, backend, simulator, or old-build rows
- exact founder/QA/test-account signals available on events/persons

Query a narrow raw sample first. Use the WP-40 production version's first live timestamp as cohort start and query through execution time. If that build is not live or there are zero clean disclosure viewers, return **no readable first cohort yet** with the earliest re-read condition. Do not manufacture a 0% funnel.

### 2. Build and audit the exclusion set once

Start with PostHog's `filterTestAccounts=true` semantics as required by WP-40 S4, but make the exclusion reproducible in HogQL:

- inspect the project's current test-account filters and person properties
- locate known founder/QA identifiers from existing RunSmart analytics reports and raw `$identify` / alias events
- exclude simulator/debug/internal builds using verified properties, not assumed names
- list each exclusion reason, people removed, overlaps, and the final clean-person count

Do not rely only on current person properties if person-on-events values differ at ingestion time. Do not hardcode a new founder ID into project docs until it is evidenced and redacted. A person excluded once stays excluded from every step.

### 3. Pull the raw HealthKit event stream

Run HogQL over `events` for every person in the cohort and return at least:

- canonical `person_id`, `distinct_id`, `event`, `timestamp`, and `uuid`
- `$session_id` when present
- marketing version, build, platform/app/library, internal/test flags, and relevant HealthKit event properties
- safe outcome/error/status fields attached to disclosure, connect, and sync events

Events in scope:

- `healthkit_disclosure_viewed`
- `healthkit_connect_tapped`
- `healthkit_sync_completed`
- any existing HealthKit permission-denied, skipped, sync-started, sync-failed, or imported-run events discovered in the schema
- `app_launched` and `onboarding_completed` only as cohort/context anchors if their exact names are verified

Order by person and timestamp. Save the exact HogQL and privacy-safe raw evidence under `docs/qa/reports/`. Never commit health data, email, tokens, full identifiers, route data, workout details, or other sensitive properties. Hash/redact identifiers while preserving stable joins.

### 4. Reconstruct the ordered clean funnel

Use first qualifying event after the prior step for the same clean person. Do not present independent event totals as a funnel.

Primary WP-40 funnel:

1. `healthkit_disclosure_viewed`
2. `healthkit_connect_tapped`
3. `healthkit_sync_completed`

If a verified `healthkit_connect_succeeded` or `healthkit_sync_started` event exists, insert it as a diagnostic step and keep the three canonical WP-40 events visible. Quantify explicit skip/deny/failure events as side exits.

Use the same `$session_id` when coverage is reliable. Otherwise use a documented 24-hour conversion window from disclosure, plus a sensitivity check at 1 hour. Report session-ID coverage. A sync preceding disclosure/connect does not count as conversion for this funnel; show it as a pre-existing-user path.

### 5. Produce the exact drop-off table and name one bottleneck

The report table must include:

| Step | Eligible entrants | Reached step | Lost at step | Step conversion | Cumulative conversion | Side-exit count |
|---|---:|---:|---:|---:|---:|---:|

Define `Lost at step = eligible entrants - reached step`. Rank steps by **absolute clean-person loss** and name exactly one largest-loss step. For that step report:

- `N` eligible real users
- `N` reached the next step
- `N` vanished
- `%` conversion and `%` drop-off
- observed raw path groups for the lost users, including explicit skip/deny/failure versus silent disappearance
- whether the cohort is decision-grade or only directional

Tie-breaker: if absolute losses tie, choose the lower conversion rate; if still tied, choose the earlier step and disclose the tie.

Also show exposure context: clean users on the WP-40 build, clean disclosure viewers, and the share of eligible users who ever saw the disclosure. If a verified onboarding anchor exists, report onboarding → disclosure separately so the analysis can distinguish discoverability from permission/sync friction.

### 6. Interpret without overclaiming

- If disclosure viewers are `< 10`, quantify and name the observed loss but label it underpowered; do not recommend a product change solely from it.
- If raw paths show instrumentation gaps or impossible ordering, stop product interpretation and identify the measurement defect.
- Separate permission denial from silent abandonment when events allow it. If denial is uninstrumented, state that unknown rather than infer it.
- Do not broaden into HealthKit accuracy, wellness-value UI, Garmin, background sync, or new instrumentation implementation. This packet diagnoses the observed cohort only.

## Deliverables

1. `docs/qa/reports/runsmart-wp40-healthkit-raw-hogql-funnel-autopsy-YYYY-MM-DD.md` containing release anchor, timezone, exact HogQL, exclusion audit, clean funnel table, ranked losses, the single bottleneck, caveats, and PostHog links.
2. A privacy-safe CSV or Markdown appendix of ordered per-person paths, if reviewable; otherwise aggregate path groups plus reproduction instructions.
3. Update `tasks/progress.md` with the quantified first-cohort result and next action. Update `tasks/lessons.md` only for a genuinely reusable new analytics lesson.

## Constraints

- Read-only PostHog work. Do not create/update dashboards, cohorts, insights, or test-account filters without explicit founder approval.
- No app code, HealthKit permissions, instrumentation, backend, release, deploy, App Store, dependency, or Garmin changes.
- Never print or commit API keys or tokens.
- Do not claim “real users” until the explicit exclusion audit matches or explains PostHog's test-account filtering.
- HealthKit event payloads may be sensitive. Select only the minimum safe properties needed for funnel reconstruction.

## Validation

- Re-run the final HogQL once and confirm the same counts at a stated timestamp.
- Independently reconcile funnel counts against grouped clean `person_id` sets from the raw extract.
- Verify no excluded person appears in the final set.
- Verify release/version filtering excludes pre-WP-40 events.
- Verify arithmetic and percentages programmatically or with a second query.
- Run `git diff --check`, inspect the report and progress diff, then commit and push on a product-repo branch per that repo's session-end rules.

## Final Output

Lead with one sentence in this form: **“The largest clean WP-40 cohort loss is X → Y: A of B real users vanished (C% drop-off; D reached Y), queried through TIMESTAMP.”** Then list files changed, query/check evidence, caveats, open questions, and what was not done.
