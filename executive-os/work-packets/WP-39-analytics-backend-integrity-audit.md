# WP-39 — Analytics + Backend Integrity Audit (RunSmart + Resumely)

- **Status:** OPEN — S1 CLOSED (merged PR #111, `b7db662`, 2026-07-09). S2-S10 open. Phase 1 Supabase validation done; PostHog validation still blocked on tooling.
- **Opened:** 2026-07-09
- **Source:** External PostHog + Supabase audit report (founder-supplied, 2026-07-09). Treated as **hypotheses to validate**, not ground truth — per the report's own instruction.
- **Apps:** RunSmart (Running coach, PostHog 171597, Supabase `dxqglotcyirxzyqaxqln`) · Resumely (ResumeBuilder AI, PostHog 270848, Supabase `brtdyamysfmctrhuankn`)
- **Priority context:** Resumely is primary (activation-target product); RunSmart Garmin is parked/maintenance per the 2026-07-02 reset. That reweights the PR order below vs the raw report.

## Guardrails (non-negotiable, from the report + global rules)
- No raw user data, emails, tokens, resume contents, Garmin tokens, or secrets in any output/event/log.
- Aggregate counts and safe metadata only.
- No destructive migrations, no row deletes, no production data mutation, no secret rotation without explicit "yes".
- Every DB migration prepared + risk-explained before applying.
- Small PR-sized changes. Every issue carries PostHog + Supabase + code evidence.

## Evidence status legend
`CONFIRMED` (validated this session) · `HYPOTHESIS` (from report, needs Phase-1 validation) · `CONTRADICTED`.

---

## Phase 1 — Supabase validation results (2026-07-09)

Ran read-only aggregate SQL against both production databases (`dxqglotcyirxzyqaxqln`, `brtdyamysfmctrhuankn`) plus `get_advisors(security)` on both. **No PostHog-side query tool was available in this session** (only a render-UI widget requiring an `exec` tool not exposed here) — the PostHog half of every hypothesis below is still unvalidated; Supabase side is done.

**Headline: the report's Supabase numbers are highly accurate.** Every claimed count either matched exactly or was within a few units (explained by rolling-14-day-window drift between when the report ran and when this validation ran — both are moving windows, not a real discrepancy). Two things the report got meaningfully wrong, and two root causes it missed entirely:

### Corrected: S4 expert-workflow diagnosis (was HYPOTHESIS, now CONFIRMED + reframed)
Report said "26 runs exist, all stuck, 0 applied." Reality: **124 runs exist all-time** (26 is just the last-14-day cohort). All-time status: 105 `needs_user_input`, 19 `completed`. 10 runs (all-time) have a non-null `applied_at` — the apply mechanism has worked before.
**The real finding is sharper and worse:** `max(applied_at)` across the entire table is **2026-03-10**. Zero applies in exactly four months, across ~110 runs created since then (weekly creation continued steadily: 18, 5, 10, 22, 11, 14, 26 runs/week through late June). Meanwhile the structurally similar `optimization_review_runs` table (separate apply flow, same product) shows **12 of 16 applied in the last 14 days alone (75%)** — that flow is healthy.
**Revised root cause hypothesis:** this smells like a dead/orphaned code path, not a discoverability problem. Something around 2026-03-10 likely replaced or disconnected the expert-workflow apply action while `optimization_review_runs`' apply flow kept working. **Recommended first step for S4 is now: grep the codebase for where `expert_workflow_runs.applied_at` gets written, and confirm whether an "Apply" action for expert-workflow output still exists and is reachable in the current UI** — before writing new instrumentation, since if the button is gone or dead, better UI copy won't fix it. `expert_workflow_artifacts` (334 rows: cover letter variants 99, quantified bullets 90, screening answers 60, summary options 55, ATS reports 29) confirms the workflow does generate real output per run — it's specifically the finalize/apply step that stopped landing.

### Confirmed root cause the report missed: S6 Garmin — `App not Approved`
`garmin_connections.error_state` contains, for multiple connections starting **2026-07-02**: `"invalid_client-app_not_approved: App not Approved"`. This is a direct root cause for the reauth_required cascade (**9/9 connections, 100%, are `reauth_required`; 0 are `connected`**) and lines up with `garmin_activities.max(created_at) = 2026-06-30` (ingestion silently stopped 9 days before this validation ran). A secondary, independent bug also present: several `garmin_import_jobs.last_error` rows read `"Garmin connection N is missing profile_id"` — a data-integrity gap unrelated to the app-approval issue. Also worth noting for context (not urgency): of 16,403 total import jobs, 16,240 are `status=failed`, but a sample of `last_error` shows some of those are intentional dead-letters (`"[DEAD: wellness dataset, not a real activity]"`, `"Dead-lettered: phantom provider_user_id with no active connection"`) rather than real breakage — the failure count is inflated by correctly-rejected non-activity payloads mixed in with genuine failures.
**This is decision-relevant for EXD-015.** The park decision assumed an open-ended "5-user feature not worth attention" framing. What's actually broken is narrower and possibly bounded: a Garmin Developer Portal app re-approval (ties to the existing `WP-24` "file new Garmin Developer Portal app" thread) plus one data-integrity fix (`profile_id` backfill). Flagging for the founder to weigh — not deciding it here; EXD-019's 2026-08-01 review date stands unless the founder wants to pull it forward given this specific, scoped root cause.

### Confirmed exact matches (Supabase side)
RunSmart: auth users 0 new/14d, profiles 0 new/14d, plans 0 new/14d, workouts 0 new/14d, runs 3 new/14d (0 completed), Garmin activity-files pending 2/14d, analytics_events 3 distinct users/14d with only `page_viewed`/`pwa_install_prompt_shown` firing, aha moments 0/14d, ai_insights 0 ever. Resumely: auth users 5 new/14d, resumes 20/14d, job_descriptions 23/14d, optimizations 12/14d (all completed), optimization_review_runs 16 created/12 applied/14d, saved_resumes 7/14d (7 total — brand-new feature), anonymous_ats_scores 28 new/14d + 1 converted/14d, `public.events` 0 rows **ever** (stronger than the report's "0 in period"), storage.objects in `applications` bucket 6/14d (72 total all-time).

### S10 — concrete advisor findings (was HYPOTHESIS, now CONFIRMED with specifics)
Both projects: leaked-password protection disabled; several functions with mutable `search_path`. Resumely also: Postgres `17.4.1.075` has security patches available; pgvector extension installed in `public` schema (should move); several `SECURITY DEFINER` functions **executable by the `anon` role**, including the exact categories the report flagged — **`consume_credit`, `grant_apple_credits`** (credit RPCs) and **`generate_file_path`** (file-path RPC). Anon-executable doesn't automatically mean exploitable (the function body may still check `auth.uid()` internally), but these three are the highest-priority to manually read before Gate A reopens (EXD-018), since they touch money/credits and file paths. RunSmart's RLS findings are mostly benign-by-design (RLS enabled + zero policies on `app_secrets`, `garmin_tokens`, `user_memory_snapshots` is a correct default-deny posture for service-role-only tables, not a bug) but it also has anon-executable SECURITY DEFINER functions worth a read: `finalize_onboarding` (accepts arbitrary `jsonb` profile payload), `link_beta_signup_to_profile`.

### Still unvalidated (needs a different tool/session)
Every PostHog-side number in the report (S2 environment pollution, S3 export events, S5 anon-ATS PostHog linkage, S7 activation funnel, S8 screen names) — no PostHog query tool was reachable from this session. Recommend validating via the founder's own PostHog dashboard, or a session where the PostHog MCP's `exec` tool is actually available.

---

## S1 — [P0, Resumely] Auth-URL token/PII leak into PostHog — CLOSED (merged `b7db662`, 2026-07-09)
**Issue:** Auth callback URLs (with `access_token`/`refresh_token`/`code`/`email`) are captured into PostHog as `$current_url`.
**Evidence (code, validated 2026-07-09):**
- `src/components/providers/posthog-provider.tsx:51-53` — `posthog.capture('$pageview', { $current_url: window.location.href })` sends the full href, hash included, unsanitized.
- `src/lib/posthog.ts:19-36` — `posthog.init` has **no** `sanitize_properties` / `before_send` hook. posthog-js attaches `$current_url` to *every* event by default, so exposure is not limited to pageviews.
**Root cause:** No URL sanitization layer between the browser location and PostHog capture.
**Fix:** Add `sanitize_properties` (or `before_send`) in `initPostHog` that, for auth routes, keeps only `pathname` and strips `access_token, refresh_token, expires_at, expires_in, token_type, type, email, code, state, provider_token, provider_refresh_token` from both query and hash. Strip `window.location.hash` before the manual pageview capture.
**Files:** `src/lib/posthog.ts`, `src/components/providers/posthog-provider.tsx`.
**Events:** none added; sanitize existing.
**DB:** none.
**Acceptance:** regression test proving no sensitive param reaches `posthog.capture` for a simulated `/auth/callback#access_token=...` URL.
**Verification (PostHog):** query last-30d events where `$current_url` matches `access_token|refresh_token|code=|email=`; expect 0 after fix; capture the pre-fix count as the incident baseline. **Note:** PostHog may already hold leaked tokens in historical events — flag whether a retroactive scrub/property-deletion is warranted (do not auto-run).
**Risk:** privacy incident if left; regression risk low (additive sanitizer).

## S2 — [P1, both] Environment separation (prod vs preview vs local)
**HYPOTHESIS:** production PostHog is polluted by localhost + Vercel preview; sessions unreliable (`$session_id` missing on many events); founder/QA traffic inflates counts (known issue — see PostHog founder-exclusion memory).
**Validate:** breakdown of events by `$host` / `properties.environment` last 14d; % events missing `$session_id`.
**Fix:** register super-props `environment` (production|preview|development|local), `app_surface` (web|ios|backend), `build_channel`; gate/annotate non-prod; consider a separate PostHog key for preview. Ensure dashboards filter internal + `filterTestAccounts=true`.
**Files:** `src/lib/posthog.ts`, provider, and CI env wiring. **DB:** none.
**Acceptance:** prod dashboards exclude localhost/preview; session_id present on new events.

## S3 — [P2, Resumely] Export / saved-output conversion funnel reconciliation
**HYPOTHESIS:** exports under-tracked — 7 `saved_resumes` + 6 application storage objects but only 2 `export_success` users; `saved_resumes` vs `applications` vs `storage.objects` are distinct concepts conflated in analytics.
**Validate:** PostHog `export_started/success/failed` users vs Supabase `saved_resumes`, `applications`, `storage.objects` counts (14d). Build the source-of-truth reconciliation row per funnel step.
**Fix/instrument:** `export_cta_seen, export_started, export_success, export_failed, export_blocked(+reason), saved_resume_created, application_package_created, download_started/success/failed`.
**Files:** Resumely web export flow + analytics wrapper. **DB:** none.
**Acceptance:** PostHog export funnel reconciles (±) to Supabase rows.

## S4 — [P3, Resumely] Expert-workflow stuck state
**HYPOTHESIS:** 26 `expert_workflow_runs` all `needs_user_input`, 0 applied — UI missing a clear apply step, or PostHog completion events are misleading vs backend truth.
**Validate:** Supabase `expert_workflow_runs` status histogram; compare to PostHog expert completion events; read the workflow UI apply path in code.
**Fix:** align event naming to backend truth; if user input is required, make the UI state explicit (missing input, why, one primary CTA, abandonment tracking). Events: `expert_workflow_started/needs_user_input/user_input_submitted/completed/apply_clicked/applied/apply_failed`.
**Acceptance:** each backend state has a matching event; apply path is reachable and instrumented.

## S5 — [P4, Resumely] Anonymous ATS → signup conversion
**HYPOTHESIS:** 28 anonymous ATS scores, only 1 converted; unclear where/when signup is shown and whether anon results survive signup.
**Validate:** where `anonymous_ats_scores` are created (code + table); PostHog `fit_check_*` linkage; signup-prompt placement.
**Fix/instrument:** `anonymous_ats_started/completed/result_viewed/signup_prompt_seen/signup_clicked/signup_completed/converted/conversion_failed`.
**Acceptance:** anon→signup funnel measurable end to end.

## S6 — [P0-for-RunSmart, but product is parked] Garmin backend health + failure surfacing
**HYPOTHESIS (RunSmart):** all Garmin connections `reauth_required` (9), 37 webhook events failed, 1 import job failed, 2 activity files pending, activities stopped after 2026-06-30; backend failures invisible in PostHog.
**Validate:** Supabase (`dxqglotcyirxzyqaxqln`) counts for `garmin_connections.status`, `garmin_webhook_events` by status, `garmin_import_jobs`, `garmin_activity_files`, `last_successful_sync_at`; Supabase logs/advisors for the failure cause.
**Fix:** server-side events (`garmin_webhook_received/queued/failed`, `garmin_import_job_created/failed/completed`, `garmin_connection_reauth_required`, `garmin_activity_imported/import_failed`, `garmin_activity_file_pending/parsed`) with safe metadata only (`environment, app_name, source, status, failure_reason, job_type, event_type, has_auth_user_id, has_profile_id, created_at_day` — no tokens, no raw payload, no unhashed Garmin ID).
**Sequencing note:** Garmin is parked per EXD-019 (revisit 2026-08-01). **Instrumentation** (visibility) is cheap and worth doing; **backend repair** stays gated behind the un-park decision. Do not reopen Garmin repair work without founder sign-off.

## S7 — [P1, RunSmart] Activation funnel: install/open → 0 backend activation
**HYPOTHESIS:** PostHog shows installs/opens + 1 `onboarding_started` but Supabase shows 0 new auth users / profiles / plans / workouts; `run_started` 0 but `run_completed` 1; 3 DB runs, 0 completed via `completed_at`; 0 aha moments, 0 AI insights.
**Caveat:** RunSmart 14d volume is tiny (16 users) and heavily internal — validate against founder/simulator exclusion (PostHog founder-exclusion memory) before concluding the funnel is "broken" vs "just unused."
**Validate + instrument:** the full onboarding→profile→plan→workout→run funnel events (`onboarding_started/step_completed/completed, profile_created, plan_generation_started/generated/failed, workouts_created, first_workout_viewed, run_started, run_completed, run_completion_saved/save_failed, post_run_report_viewed, next_workout_viewed`).

## S8 — [P2, RunSmart] Useful screen names
**HYPOTHESIS:** `$screen` = generic SwiftUI class names (`UIHostingController<...>`), useless for analysis.
**Fix:** explicit product screen names (Onboarding*, GarminConnect, HealthKitConnect, Today, Plan, Run, Report, Profile, Coach, PostRunReport).

## S9 — [P3, both] Internal/dev/test filtering + cross-app event standard
Standard properties on every event: `app_name, environment, app_surface, platform, app_version, build_number, build_channel, is_internal, is_testflight, is_simulator, user_type, auth_state, source_screen, flow_name, flow_step, success, failure_reason`. Never: emails, names, resume text, raw JDs, health data (unminimized), unhashed Garmin IDs, tokens, auth URLs, raw webhook payloads, raw LLM prompts with user content.

## S10 — [P4/P5, both] Supabase security advisor pass (before payments scale)
**HYPOTHESIS:** advisor warnings on `SECURITY DEFINER` functions, credit RPCs, file-path RPCs, rate-limit + anon-ATS insert policies, mutable `search_path`, leaked-password protection, Postgres patch level.
**Do:** run `get_advisors` (security + performance) on both projects; produce a **migration plan** with risk per item. Do NOT apply RLS/security migrations blindly (lockout risk).

## D4 — CLOSED (migration applied 2026-07-09)
Cursor's code read (2026-07-09) found `consume_credit` and `grant_apple_credits` had zero internal caller-identity checks — `p_user_id` was a bare caller-supplied parameter. Verified live against production via `information_schema.role_routine_grants`: **`anon` had active `EXECUTE` on both, right now**, not hypothetically. This meant any holder of the public anon key could drain any user's credit balance via `consume_credit`, or mint unlimited free credits via `grant_apple_credits` (bypassing Apple purchase verification entirely, which only happened in the calling API route, never inside the function). Applied `REVOKE EXECUTE ... FROM PUBLIC, anon` on both functions via migration `revoke_anon_execute_credit_functions`; verified post-migration grants show only `authenticated`/`postgres`/`service_role` remain. Legitimate app usage is unaffected — both functions are only called from authenticated server-side API routes per Cursor's call-site trace. `generate_file_path` left untouched (assessed low-risk: no DB writes, storage RLS still gates uploads) per founder choice.

## S4 — CLOSED: confirmed live regression, migration applied (2026-07-09)
Live smoke test (production, QA account `nadav.yigal+fable-qa-jul03@gmail.com`) confirmed **Outcome B — the scenario-(a) "just UX abandonment" verdict was wrong.** Apply returns HTTP 200 `{success: true}` and partially updates `optimizations.ats_score_optimized`, but `expert_workflow_runs.applied_at`/`apply_mode`/`status` never finalize. Supabase REST logs showed the decisive evidence: `PATCH expert_workflow_runs` → **400**, silently swallowed by the API, which returns `success: true` anyway.
**Root cause: production schema drift, not a UX problem.** `applyExpertWorkflowRun()` (`orchestrator.ts` ~L788-801) writes an `applied_assets_json` column that migration `20260303000000_expert_workflow_assets_and_new_types.sql` adds — but that migration was **never applied to production** (prod `schema_migrations` had `20260301000000`/`20260302000000` only). The 2026-03-09 "hardening" commit (`a8d97a6`) started writing that column against a schema that never got it, so every apply PATCH has 400'd since ~2026-03-10 — matching the 60%-to-0% cliff exactly.
**Fix applied:** ran migration `expert_workflow_assets_and_new_types` against `brtdyamysfmctrhuankn` (2026-07-09) — pure additive schema, columns + CHECK constraints, no destructive ops, founder-approved before applying. Verified `applied_assets_json` column now exists.
**Still open (P1, follow-up code fix, not yet packaged):** the API's silent error-swallowing itself is a separate bug — `applyExpertWorkflowRun()`'s finalize UPDATE doesn't check `{ error }`, so any future PATCH failure will again report `success: true` falsely. Needs a small fix (return 500 on write failure) before this class of bug can recur silently. Recommended as the next Cursor/Codex session on this repo.
**Not yet reconfirmed end-to-end:** the original test run (`4102da8d-0bde-4692-a133-321f396e3f20`) still shows `applied_at` NULL since it failed before the migration landed — a fresh Apply click (or a new test run) is needed to get a clean Outcome-A confirmation post-fix.

---

## PR sequence (reweighted: Resumely-primary)
1. **S1** — Resumely auth-URL sanitization (P0 privacy, confirmed) — do first, standalone, with regression test.
2. **S2** — Resumely environment separation (unblocks trustworthy funnels).
3. **S3** — Resumely export funnel instrumentation.
4. **S4** — Resumely expert-workflow repair.
5. **S5** — Resumely anonymous-ATS conversion.
6. **S6 (instrumentation only)** — RunSmart Garmin health visibility; repair stays gated.
7. **S7 + S8** — RunSmart activation instrumentation + screen names.
8. **S9** — cross-app event standard + dashboards.
9. **S10** — Supabase security hardening plan (both apps).

## Phase 1 (next execution step — needs founder go)
Validate every `HYPOTHESIS` above with live PostHog + Supabase queries (read-only), producing the cross-source evidence table (Product · Funnel step · PostHog · Supabase · Code · Diagnosis · Priority · Match quality). This touches two production databases (read-only) and both PostHog projects — flagged under the scope gate for explicit go-ahead.

## Open decisions for founder
- **D1:** Retroactive scrub of already-leaked tokens in PostHog history (S1) — do it, or accept + rotate-forward? (Privacy call.)
- **D2 — DECIDED 2026-07-09 (EXD-021, supersedes EXD-020):** Issue: Garmin's Developer Portal OAuth app is de-approved by Garmin itself since 2026-07-02, causing all 9 currently-connected users to sit in `reauth_required`. First pass (EXD-020) asked "hold the calendar park or unpark the fix" and the founder initially reconfirmed a full park — then corrected it same-day: the real gate isn't a date, it's the founder's Israeli עוסק מורשה business registration (in progress, tied to EXD-017), which Garmin's commercial tier requires. **Final decision:** three tracks — Garmin app process/communication continues as a low-priority background thread (WP-26/27 rescoped accordingly); the actual commercial filing stays blocked until the business registration completes (no fixed date); RunSmart's engineering focus redirects to HealthKit (already built, universal on iOS, currently near-zero usage) + non-wearable users, not Garmin. See EXD-021.
- **D3:** Separate PostHog project/key for preview/dev (S2) vs super-prop filtering only.
- **D4 (new):** Read `consume_credit`, `grant_apple_credits`, `generate_file_path` function bodies (Resumely) for actual anon-callable risk before Gate A reopens — quick code review, not a migration; do this regardless of D1-D3 timing.
- **D5 (new):** S4's revised scope (find the dead/orphaned apply path vs write new instrumentation) changes the work from a UX pass to a code-archaeology pass — confirm this reprioritization before someone starts building new "clearer CTA" UI for a button that may not exist.
