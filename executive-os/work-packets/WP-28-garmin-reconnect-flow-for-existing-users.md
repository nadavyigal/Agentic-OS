# Work Packet WP-28 - Garmin: Reconnect Flow for the Existing 7 Connected Users

- Status: **PAUSED 2026-07-03** — under the 2026-07-02 priority-reset (Resumely primary, RunSmart Garmin maintenance-only through ~2026-08-01), this packet's premise (build a reconnect flow ahead of commercial-app approval) doesn't apply while the commercial app isn't being filed. Maintenance mode is "fix breakage only, do not expand scope" — a new reconnect flow is scope expansion, not a fix, so this stays unbuilt. Revisit alongside WP-26 Steps 3-4 at the day-30 checkpoint. See [[project_resumely_primary_runsmart_maintenance]] memory.
- Created: 2026-07-02
- Source: Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md` (PR #13, merged) — the "blind spot no lens addressed" finding: none of the STORM lenses, and neither the founder's plan nor the ChatGPT advisory draft, planned the reconnect migration for existing users
- Mode: Grower
- Workflow pattern: normal
- Input trust: trusted internal — Supabase aggregate reads already establish the baseline user count
- Outcome loop: RunSmart Garmin production approval
- Related: WP-25 (connection gate must exist first), WP-26 (this becomes required once the commercial app is approved)
- Success signal: on the day the commercial Garmin application is approved, every previously-connected user can re-establish sync in-app without a support ticket, and RunSmart can report a reconnect rate — the specific metric this packet must move

## Owner Role

RunSmart Web operator — execute with Codex or Cursor Composer 2.5, same as WP-25 (repo already has `.codex`, `AGENTS.md`, `.cursor/rules`, `.cursor/skills`). If a native iOS surface turns out to be needed (Task step 1), that slice moves to the iOS repo and inherits WP-27's caveat: Codex works there via `AGENTS.md`, but there is no `.cursor/` config for Composer yet.

## Project

RunSmart Web (+ RunSmart iOS if the reconnect entry point needs a native surface)

Path: `/Users/nadavyigal/Documents/RunSmart`

## Goal

Build the reconnect flow now, while there is no time pressure, so it is not a scramble on Garmin approval day. Every metric this packet touches must cite what it moves, per the Grower mode contract: the target is reconnect rate among the 7 (or however many by then) previously-connected users, measured within a defined window after the commercial app goes live.

## Context

Garmin's 2026-07-01 deactivation orphans every existing Garmin OAuth token once the old Evaluation application is fully torn down. As of the 2026-07-01T16:12Z Supabase aggregate check, 9 `garmin_connections` rows existed: 7 `connected`, 2 already `reauth_required`. Those users' historical data stays in RunSmart (nothing is deleted), but sync stops until they reconnect through whatever new flow exists — and today, no such flow exists. This was gate T6 in the old (now-historical) `Garmin-Production-Roadmap` and was never built even before the deactivation escalation. The STORM analysis flagged this as the item most likely to become the actual critical path on approval day if left unplanned, since every other lens was focused on getting the application approved, not on what happens the moment it is.

## Read First

- Builder OS vault `02-Products/RunSmart/2026-07-02-garmin-deactivation-storm.md`
- `docs/garmin-application/GARMIN-STATUS.md` (T6 in the historical gate table)
- Whatever component currently renders Garmin connection state to the user (Profile / Connected tab area) — same surface WP-25's temporary-unavailable message will use
- Current `garmin_connections` schema in Supabase

## Task

1. **Design the reconnect UX.** A user whose `garmin_connections` row has gone stale (token invalidated by the old app's teardown) should see a clear, non-alarming prompt in-app: their Garmin data and history are safe, sync is paused, and a "Reconnect Garmin" action starts a fresh OAuth flow against the new commercial application's credentials. This reuses WP-25's connection gate surface — same place, different message, once the commercial app is live.
2. **Instrument it.** Add a PostHog event (e.g. `garmin_reconnect_prompted`, `garmin_reconnect_completed`) so reconnect rate is measurable, per this packet's Mode contract. Exclude the founder's own account per [[project_posthog_founder_account_exclusion]] memory.
3. **Build the notification trigger.** Decide and implement how affected users learn a reconnect is needed: an in-app banner is the minimum; an email to the known-affected user set (identifiable from the current `garmin_connections` table) is the founder's call — flag it, don't decide it unilaterally.
4. **Do not activate this flow's credentials path until WP-26's commercial application is approved and its `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` are live in production.** Build and test it now against the Internal Test application's credentials (from WP-26) in a non-production environment; the cutover to real credentials is a one-line config change gated on Garmin's approval, not a rebuild.
5. Update `docs/garmin-application/GARMIN-STATUS.md` with the reconnect flow's status and the affected-user count at time of writing.

## Constraints

- No production credential changes in this packet — build and test against non-production/Internal Test credentials only.
- No unrelated Profile/Connected-tab changes bundled in.
- Founder must approve the notification approach (in-app only vs. also email) before it ships — do not assume.
- Lint + tests pass before done.

## Validation

- Reconnect flow tested end-to-end against Internal Test credentials in a non-production environment.
- PostHog events fire correctly and are excluded from the founder's own account.
- `docs/garmin-application/GARMIN-STATUS.md` updated.

## Completion Gate

Report:

- Reconnect UX description and where it lives in the app.
- PostHog events added, and confirmation they were tested with founder-account exclusion applied.
- Notification approach used, and founder approval status for it.
- Confirmation this flow is ready to flip to production credentials the moment WP-26's commercial application is approved.
- What was NOT done.
