# Resumely — consolidated session (2026-07-20)

Spans two repos:
- iOS: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- Web: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`

## Context you can trust

1.4.3 (13) is **LIVE** (released 2026-07-19T21:47:02Z, store-verified). Release C shipped, WP-46 is closed. It carries the Story 13 auth-retry fix, the partial activation-cliff fix (tappable "Sign in to Optimize" + diagnosis persistence), and the `optimization_id` fix — saved-résumé reuse had never worked in production for any user before this build.

WP-48 (#112, merged) read the post-release cohort and returned a clean negative: **0 of the required 20 clean uploaders**, 9 hours after release, at a measured 4.7 clean file-selectors/week. Maturity projects to **~2026-08-18**.

Ignore any dashboard text saying "Stories 7 and 8 are actively being built" — that is stale; Stories 11-13 shipped.

## Do these in order

**1. Unblock Web PR #117 (WP-49 anonymous carryover).** It is held, not rejected. The WP-39-style `42703`/`PGRST204` guard covers only the `ats-check` **insert**; the three **read** paths request the six new columns with no fallback:
- `src/app/[locale]/auth/callback/route.ts`
- `src/app/api/public/convert-session/route.ts` GET and POST (`SCORE_COLUMNS`)

The migration is not applied to production. Merging and deploying first makes those selects return `42703`, `anonScore` comes back null, and the `.update()` setting `user_id`/`converted_at` never runs — so session conversion, which works today, silently stops.

Fix: apply the same `isUndefinedColumnError` fallback to all three reads (retry with the original narrow column list, skip materialization). Add a regression test proving conversion still sets `user_id`/`converted_at` when the new columns are absent. This makes deploy order irrelevant and also covers the schema-cache reload window. **Do NOT apply the migration** — that needs explicit founder approval.

Also add a Privacy Policy line (EN + HE) covering short-term anonymous résumé retention. The landing copy was already corrected; the policy page was not.

**2. Fix the measurement denominator before the window matures (iOS).** From `docs/qa/reports/wp48-post-1.4.3-cohort-read-2026-07-20.md`:
- **Defect A:** the predeclared 12.5% baseline is not reproducible on 1.4.3. It was computed on legacy `resume_uploaded`, whose call site Story 10 removed. Its successor `resume_upload_succeeded` is emitted at `TailorViewModel.swift:172`, **after** the sign-in guard at `:146` — unreachable for guests by construction. Measured: 1 of 10 clean file-selectors ever emitted it.
- **Defect B:** the canonical Story 10 HogQL uses `resume_upload_succeeded` as its `uploaded_people` step, so the upload step can never exceed the sign-in step and every downstream rate excludes all guests.

Redesignate the denominator to a pre-auth event (`resume_file_selected`) and **recompute the baseline on that same definition** so the win rule is reproducible. Update the canonical HogQL. Do this now — reading first and fixing later would compare an auth-gated numerator against a guest-inclusive baseline and declare a win that is pure denominator substitution.

**3. Scope S2 instrumentation for 1.4.4:** `score_screen_signin_tapped`, file-picker outcome events, `job_source` property.

**4. Triage stale open PRs.** iOS: #100 (1.4.2 measurement baseline), #96 (FTUX audit artifacts), #86 (Fit-First thresholds). Web: #112 (expert apply finalize error handling), #100 (grandfather free users). Decide each.

**5. Close the two deferred follow-ups** if there is room: Hebrew/RTL PDF, and the Story 8 Home→Fit direct tap-through. Neither is a release blocker.

## Constraints

- **Do NOT read the activation cohort.** It is not mature until ~2026-08-18. If asked for a number, state the maturity date instead of reading early.
- Do NOT apply the `20260720000000_anonymous_carryover_artifacts` migration to production.
- No schema change beyond that migration without surfacing it first. No new npm dependencies without asking.
- If a fix expands past 3 unexpected files, stop and surface it.

## Validation

- Web: `npx tsc --noEmit` clean, `npx eslint` no new errors on touched files, targeted tests. If `node_modules` is broken use `npm ci`, never `npm install` (ERRORS.md 2026-06-12).
- iOS: full suite on iOS 26.5 (the 26.3.1 runtime has a pre-existing XCTest crash unrelated to any change).
- Any HogQL committed must be content-free and reproducible, with the exact cohort cutoff stated.

## Known traps (from ERRORS.md)

- Exclusion rules protect against inflated numbers, not deleted signal. List what each excluded person did; individually re-examine anyone carrying an ERROR event.
- Reconcile against Portfolio HQ before publishing. If they disagree, resolve the disagreement rather than assuming the fresh read wins.

## Completion gate

Update `tasks/progress.md`, `tasks/todo.md`, `tasks/session-log.md` in whichever repo you touched. Push and report push state. Report what was NOT done.
