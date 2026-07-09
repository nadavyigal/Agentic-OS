# WP-39 — Analytics + Backend Integrity Audit (RunSmart + Resumely)

- **Status:** OPEN — investigation packet, validation-first
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

## S1 — [P0, Resumely] Auth-URL token/PII leak into PostHog — CONFIRMED
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
- **D2:** Garmin instrumentation now vs fully parked until 2026-08-01 (S6).
- **D3:** Separate PostHog project/key for preview/dev (S2) vs super-prop filtering only.
