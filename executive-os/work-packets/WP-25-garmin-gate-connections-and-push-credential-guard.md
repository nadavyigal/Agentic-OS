# Work Packet WP-25 - Garmin: Gate Off New Connections + Push/Merge the Credential Guard

- Status: Open
- Created: 2026-07-02
- Source: Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md` (PR #13, merged), steps 1-2 of the synthesis action plan
- Mode: Maintainer
- Workflow pattern: normal
- Input trust: trusted — direct git read of the RunSmart repo confirmed the guard commit's existence and its stranded state
- Outcome loop: RunSmart Garmin production approval
- Related: WP-24 (superseded — see its Status line), [[project_wp24_garmin_fresh_production_app]] memory, `docs/garmin-application/GARMIN-STATUS.md`
- Success signal: production cannot start a Garmin OAuth flow with test/Evaluation credentials, and no new user can begin a Garmin connect flow until the commercial app is approved

## Owner Role

RunSmart Web operator (Codex or Claude Code, code-only — no portal/browser action in this packet)

## Project

RunSmart Web

Path: `/Users/nadavyigal/Documents/RunSmart` (app code in `v0/`)

## Goal

Stop the bleeding on the two things that are pure code and do not require the Garmin Developer Portal: (1) new users can no longer start a Garmin connect flow while there is no legitimate application to connect them to, and (2) the credential-separation guard that fixes the root cause of the whole deactivation sits merged in intent but unmerged in git — land it for real.

## Context

On 2026-07-01 Garmin deactivated RunSmart's sole Developer Portal application because it was Evaluation tier serving external (real) users, a Terms violation. Root cause, confirmed by code read: `v0/lib/server/garmin-oauth-store.ts` and the connect/callback routes have always read a single `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` pair with no environment separation. A fix was already built and committed locally (`baa19aa`, "Guard Garmin production credentials," branch `codex/wp24-garmin-credential-guard`) but verified 2026-07-02 to have **no origin branch** — it never left the local machine that authored it. Separately, nothing in the app currently stops a brand-new user from tapping "Connect Garmin" today, which would be a fresh Terms violation against a now-deactivated app.

Full analysis: Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md`. Current status: RunSmart web `tasks/progress.md` (2026-07-01 entry) and `docs/garmin-application/GARMIN-STATUS.md`.

## Read First

- `docs/garmin-application/GARMIN-STATUS.md`
- `tasks/progress.md` (RunSmart web, Garmin section)
- `v0/lib/server/garmin-oauth-store.ts`
- `v0/lib/server/garmin-credentials.ts` (new file on `codex/wp24-garmin-credential-guard`)
- `v0/app/garmin/connect/route.ts` and `v0/app/api/devices/garmin/connect/route.ts`
- Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md` and `02-Products/RunSmart/Domain/Garmin-Integration.md`

## Task

1. **Push and land the credential guard.** Checkout `codex/wp24-garmin-credential-guard` locally (commit `baa19aa`, 11 files changed: `garmin-credentials.ts`/`.test.ts` new, `garmin-oauth-store.ts`, both connect/callback routes + tests, `.env.example`). Diff it against current `main` — 5+ Garmin PRs have merged to `main` since this branch was cut (`#109`-`#113`), so check for conflicts before pushing. Rebase onto current `main` if needed, resolve conflicts, push, open a PR, get it merged.
2. **Add the connection gate.** In the Garmin connect entry point(s) (`v0/app/garmin/connect/route.ts`, `v0/app/api/devices/garmin/connect/route.ts`, and whatever UI component renders the "Connect Garmin" CTA), add a feature flag (e.g. `GARMIN_CONNECT_ENABLED`, default `false` in production) that blocks new connection attempts and returns/shows: "Garmin sync is temporarily unavailable while we complete Garmin production approval. Existing activity data remains in RunSmart. We'll notify you when reconnection is available." Already-connected users' existing data and sync must be unaffected by this flag — it only blocks new connection attempts.
3. **Verify env wiring.** Confirm `GARMIN_TEST_CLIENT_ID`/`GARMIN_TEST_CLIENT_SECRET` (from the guard branch) are documented in `.env.example` but are NOT set in production Vercel env vars yet — there is no Internal Test portal application to point them at until WP-26 creates one. Production continues to use existing `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` for already-connected users' ongoing sync only (do not rotate these yet).
4. Update `docs/garmin-application/GARMIN-STATUS.md` and `tasks/progress.md` with what shipped.

## Constraints

- No Garmin Developer Portal action in this packet — that is WP-26.
- Do not rotate `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` in production. Existing connected users must keep syncing until the commercial app exists.
- Do not touch Training/Courses API scope (parked, out of scope, see [[project_runsmart_ios_live_version]] memory).
- No unrelated file changes — this is credential-guard + connection-gate only.
- Lint + tests must pass before declaring done, per repo convention.

## Validation

- `npm run type-check` and targeted `npx eslint` pass on all changed files (repo's established Garmin validation pattern — see `tasks/progress.md` 2026-07-01 entry for the exact commands used last time).
- New/updated tests for `garmin-credentials.ts` and the connect/callback route guards pass.
- Manual check: hitting the connect route/UI as a fresh (unconnected) user shows the temporary-unavailable message and does not start an OAuth flow.
- Manual/Supabase check: an already-connected user's next scheduled sync still succeeds (no regression to existing sync paths).

## Completion Gate

Report:

- PR link and merge commit for the credential guard.
- PR link and merge commit for the connection gate.
- Confirmation that production env vars were NOT touched.
- Files changed, tests run, and their results.
- What was NOT done (expected: portal application creation, screenshot recapture, reconnect flow — all separate WPs).
