# Work Packet WP-26 - Garmin: File Internal Test + Commercial Portal Applications

- Status: **RESCOPED 2026-07-09 (EXD-021)** — no longer gated on the 2026-08-01 calendar date. Step 2's core deliverable (Internal Test app filed, approved, connect flow verified) stands as done. **Step 3 (commercial application filing/submission) is a low-priority background thread that may continue now (prep, evidence, communication) but the actual submission stays blocked on the founder's עוסק מורשה business registration completing** (Garmin's commercial tier requires a registered business; that registration is in progress, tied to EXD-017, no fixed date). Step 2's remaining sub-item (Data Generator + Partner Verification runs) can also resume as background work. This is not RunSmart's product-engineering priority — that's HealthKit + non-wearable users per EXD-021 — but the Garmin thread is no longer frozen. See EXD-021.
- Created: 2026-07-02
- Source: Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md` (PR #13, merged), steps 3+5+7 of the synthesis action plan; supersedes WP-24
- Mode: Maintainer
- Workflow pattern: normal
- Input trust: founder-authenticated external system (Garmin Developer Portal) — every field value must be confirmed with the founder before submission, nothing external goes out without explicit sign-off in the session
- Outcome loop: RunSmart Garmin production approval
- Related: WP-24 (superseded by this packet — see WP-24's Status line pointer), WP-25 (must land first), WP-27 (evidence dependency), [[project_wp24_garmin_fresh_production_app]] memory
- Success signal: two Developer Portal applications exist (Internal Test, Commercial), the commercial one has been submitted for Production review exactly once with a complete evidence package, and no further "what is this / start over" replies have come back from Garmin

## Owner Role

Release Manager + RunSmart Web operator. Execute with Codex or Cursor Composer 2.5, in a session where the founder has `developerportal.garmin.com` open and logged in in their own browser — this is founder-credentialed and external, and neither tool can drive a live OAuth-gated browser session itself. The agent drives field-by-field content, evidence prep, and drafts the resubmission text; the founder performs the actual portal clicks/logins/submission and reads back what the portal shows when this packet asks "observe what the portal actually presents." This is the one packet in the Garmin track that cannot be fully agent-driven regardless of tool choice.

## Project

RunSmart Web (supporting evidence, credentials) + Garmin Developer Portal (external, browser-based)

Path: `/Users/nadavyigal/Documents/RunSmart`

## Goal

File exactly what Marc Lussi asked for on 2026-07-01: two separate Developer Portal applications, not a reset of the old one. Submit the commercial application for Production review **once**, complete, with every item numbered against Garmin's own requirements list — not another partial, iterative reply.

## Context

Garmin deactivated RunSmart's single Evaluation-tier application on 2026-07-01 because it was serving real (external) users, which Evaluation tier's Terms prohibit outright. This is not a continuation of the three prior Gate-4 brand rejections — it is a different, higher-severity finding that makes the old app unusable regardless of how compliant its screenshots become. Garmin requires two new applications: one for internal testing/verification only, one for commercial/production use after passing review.

The STORM analysis (vault `2026-07-02-garmin-deactivation-storm.md`) found, across five independent lenses, one consistent recommendation: this thread's problem was never really the brand assets, it was treating a deterministic compliance process as a negotiable conversation — three same-day, partial replies in nine days read as thrashing, not diligence. The fix is not speed, it is completeness: one full, numbered, boring resubmission after everything is actually ready.

Founder already confirmed the two-app plan to Marc by email on 2026-07-02 (10:31). The reply is sent; the work is filing the apps and preparing the resubmission correctly this time.

## Read First

- Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md` (full five-lens analysis + ordered plan)
- Builder OS vault `02-Products/RunSmart/Domain/Garmin-Integration.md` (Current State block)
- `docs/garmin-application/GARMIN-STATUS.md`
- Garmin email chain, 2026-07-01 and 2026-07-02 (founder has this; ticket 213165)
- `docs/garmin-application/21-GARMIN-REPLY-DRAFT-2026-07-01-3RD-REJECTION.md` and any later draft for tone/precedent
- WP-25 (must be merged before Step 1 below — the connection gate should already be live so no new user connects mid-filing)

## Task

1. **Confirm WP-25 landed.** Do not proceed to portal work until the connection gate and credential guard from WP-25 are merged — filing new apps while new users can still hit the dead old app makes the outage worse, not better.
2. **File the Internal Testing / Verification application.**
   - Name: `RunSmart - Internal Test` (avoid anything that reads production-facing to a future reviewer).
   - Tier: Evaluation.
   - Scope: Health API + Activity API (import only). No Training/Courses API.
   - Users: founder's own Garmin test account(s) only — never a real RunSmart customer.
   - Record `client_id`/`client_secret`; store only in a non-production environment (local `.env`, Vercel Preview, or dedicated staging), matching `GARMIN_TEST_CLIENT_ID`/`GARMIN_TEST_CLIENT_SECRET` from WP-25.
   - Use this application for Gate-4 screenshot capture (WP-27) and for running Garmin's Data Generator + Partner Verification tools, including the still-open **USER_DEREG** coverage item — this can finally be demonstrated deliberately on a test account instead of waiting for an organic real-user disconnect.
3. **Do NOT file the commercial application yet if WP-27's evidence isn't ready.** Only proceed to commercial filing once WP-27 reports the live build confirmed and real-device screenshots captured.
4. **File the Commercial application** (once WP-27 is done):
   - Name: `RunSmart` (public-facing name).
   - Tier: request Production directly if the portal offers it for a new application; otherwise Evaluation-then-Production. Observe what the portal actually presents and report back — this flow for a brand-new application (vs. an upgrade of an existing one) is unconfirmed.
   - Scope: Health API + Activity API (import only). Explicitly do NOT request Training/Courses API — this caused an earlier unresolvable demand for a screenshot RunSmart cannot produce (import-only product, workout-push parked per 2026-06-25 decision).
   - Commercial terms: already answered by Garmin 2026-06-15 — do not re-ask. Subscription use YES, AI coaching from Garmin data YES, no license fees, 30-day historical data max.
   - Account: `nadav.yigal@runsmart-ai.com` only (company domain, no freemail), API Blog notifications enabled, no third-party integrators.
5. **Assemble the resubmission package**, numbered against Garmin's own four-gate requirements list verbatim (Legal / Technical / Account / UX+Brand — see the 2026-06-22 requirements email in the thread), using WP-27's real-device evidence. Draft the reply for founder review before sending — no email goes to Marc without explicit sign-off in the session.
6. **Submit once.** After the founder confirms the draft, submit the commercial application for Production review and send the single consolidated reply. Do not send a follow-up until Garmin responds.
7. Update `docs/garmin-application/GARMIN-STATUS.md`, both repos' `tasks/progress.md`, and the Builder OS vault `Garmin-Integration.md` Current State block with both applications' portal references and the submission date.

## Constraints

- No Garmin Developer Portal action, and no email to Marc, without the founder confirming in the current session.
- Never connect a real RunSmart user account to the internal-testing application.
- Do not resubmit for Production review using simulator screenshots or a build that isn't the one actually live on the App Store.
- Do not re-add Training/Courses API scope to either application.
- Do not rotate production `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` until the commercial application's credentials exist and are ready to receive traffic (that cutover is its own step after approval, not part of this packet).
- One consolidated resubmission, not another round of partial replies — this is the whole point of the packet.

## Validation

- Internal Test application exists in the portal; credentials confirmed present only in non-production env.
- Data Generator + Partner Verification run against the Internal Test app, including a deliberate USER_DEREG event, with results captured for the evidence package.
- Commercial application exists; scope matches exactly Health + Activity import, no Training API.
- Resubmission reply reviewed and approved by the founder before sending.

## Completion Gate

Report:

- Internal Test application portal reference and confirmation credentials are non-production only.
- Data Generator / Partner Verification results, including USER_DEREG coverage.
- Commercial application portal reference and exact scope requested.
- Whether the resubmission was sent (date, and confirm founder approved it first) or is still pending WP-27.
- `GARMIN-STATUS.md` and vault `Garmin-Integration.md` update confirmation.
- What was NOT done.

## Garmin-side confirmation (2026-07-02, received while paused — no action taken)

Two things arrived from Garmin after this packet paused; recorded here as evidence, not as a resumption of Steps 3-4.

- **Marc Lussi, 2026-07-02 10:11 GMT+2:** "You do not have a production app so we cannot speak of 'a new'. Please generate your first production app to re-initiate the production review process." Confirms in Garmin's own terms what root-cause analysis already established: the deactivated app was never Production tier, only Evaluation — there is no existing production app to reset, only a first one to eventually file. This is Garmin's process restating itself, not a deadline or a question; per the priority-reset decision, filing that first production app is exactly the paused Step-4 work and stays parked. No reply sent.
- **Automated Garmin Developer Portal notification:** the Internal Test application (Connect Developer - Evaluation) is **approved**, scoped to exactly `ACTIVITY, HEALTH` — matches what was filed, confirms no Training/Women's Health API slipped through. No action needed; credentials were already retrieved and stored per the 2026-07-02 filing.

## Progress (2026-07-02)

Step 2 executed directly (browser-driven, founder-confirmed each step) rather than handed to Codex/Composer, since the portal is founder-authenticated and OAuth-gated end to end.

**Internal Test application filed and approved.**
- Name `RunSmart - Internal Test`, tier Connect Developer - Evaluation, scope Health API + Activity API only (Women's Health and Training API explicitly excluded). Portal reference: `https://developerportal.garmin.com/teams/runsmart_ai/apps/runsmart_internal_test`.
- Confirmed via the portal UI: **Authorization: OAuth 2.0** — resolves the earlier concern that the old dead app showed "OAuth 1.0" while the shipped code uses PKCE. The new-app creation form has no OAuth-version selector at all; new apps default to the current program's OAuth 2.0, so there was never an actual mismatch to fix.
- **Caught and fixed a bad form default**: "Do you plan to sell activity data provided by Garmin to any third parties?" defaulted to "Yes" on page load. Corrected to "No" before submission. Worth watching for again on the Commercial app filing (Step 4) — likely the same default.
- **Redirect URL corrected after initial filing.** First registered `https://www.runsmart-ai.com/garmin/callback` (matching the old app and the code's production fallback), then discovered WP-25's own credential guard makes that unusable for testing: `assertProductionIsNotUsingTestCredentials()` fires on any production runtime (`VERCEL_ENV === 'production'`), so the production domain can never be pointed at test credentials, deliberately, by the code we just shipped. Updated the registered redirect to `http://localhost:3000/garmin/callback` so local dev can actually exercise the flow. **Note for whoever runs WP-27's real-device screenshot capture: this redirect will need to change again** to a phone-reachable URL (staging subdomain or tunnel) — localhost won't work from an iPhone.
- Credentials (Client ID/Secret) issued, confirmed present in the portal. Deliberately not read or relayed through any agent tooling — founder stored them directly into Vercel (`running-coach` project, Preview + Development scope, Production excluded) via the dashboard.

**Local connect-flow structurally verified working**, using ephemeral placeholder credentials passed only to the process (never written to `.env.local`, no real secret touched by tooling):
- `POST /api/devices/garmin/connect` with the same payload shape the real frontend sends (`device-connection-screen.tsx:162`, which explicitly sends `redirectUri: \`${window.location.origin}/garmin/callback\``) returned `success: true` with a well-formed Garmin OAuth 2.0 PKCE authorization URL: correct `client_id` (test mode, confirmed via `resolveGarminOAuthClientId()` picking `internal-test`), `redirect_uri` exactly matching the portal registration, valid `code_challenge`/`code_challenge_method=S256`, signed state.
- Along the way, found (and explained, not a bug) that a bare API call without an explicit `redirectUri` falls back to a `GARMIN_OAUTH_REDIRECT_URI` env var already present in `.env.local`, which points at the production domain — only matters for direct API testing (curl/Postman), not the real browser UI, which always sends `redirectUri` explicitly.
- Not yet done, needs the founder's real credentials and an actual click-through: completing the full OAuth handshake against Garmin's live server (this local test verified everything up to but not including Garmin's own acceptance of the request).

**Still open within Step 2:** Data Generator + Partner Verification tool runs against the Internal Test app, including a deliberate USER_DEREG event -- not started.

**Not started:** Step 3/4 (commercial application filing) -- correctly blocked on WP-27.
