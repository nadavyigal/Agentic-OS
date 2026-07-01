# WP-24 — Garmin: File Two Developer Portal Applications (Internal Test + Commercial)

**Created:** 2026-07-01
**Updated:** 2026-07-01 — Marc confirmed the answer to WP-24's original open question, and it's worse than the hypothetical: escalated from "which portal capability exists" to an active deactivation.
**Status:** URGENT — the current (sole) application is being deactivated by Garmin. Check live-user impact before anything else.
**Repos:** `/Users/nadavyigal/Documents/RunSmart` (web/backend), `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` (iOS)
**External system:** Garmin Developer Portal (`developerportal.garmin.com`) — browser-based, founder-authenticated
**Execute with:** Codex, in a session where the founder has the Garmin Developer Portal open and logged in in their own browser. Codex reads/writes the repos for supporting evidence and drives the field-by-field portal work; the founder performs the actual clicks/logins since this is founder-credentialed and external.
**Related:** [[project_wp24_garmin_fresh_production_app]] and [[project_runsmart_ios_live_version]] memory; iOS PR #69/#70 (merged), web PR #109/#110/#111 (merged); `docs/garmin-application/GARMIN-STATUS.md` is the living status doc.

---

## What changed — Marc's reply (2026-07-01, after our clarifying-questions email)

> Evaluation apps are not allowed to connect external users as per Terms. I will deactivate your app now. Please generate two new apps. One for internal testing and verification, one for commercial use after successful production review.

This is not a brand-guideline nuance — it's a Terms violation. RunSmart's single Developer Portal application has been **Evaluation tier** this whole time, and Evaluation tier does not permit connecting real (external) users at all. We've been running production traffic through it since the integration launched. Confirmed by direct code read: there has never been any environment separation — every Garmin route (`garmin-oauth-store.ts`, `garmin/connect/route.ts`, `api/devices/garmin/callback/route.ts`, `api/devices/garmin/diagnose/route.ts`) reads the same single `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` pair, with no code-level guard against an Evaluation-tier credential serving real end users. That gap is the actual root cause, not a screenshot or logo detail.

Marc is deactivating that application now. The credential-rotation risk flagged in the original version of this WP is no longer hypothetical.

---

## Immediate actions — do these before touching the Developer Portal

1. **Check current Garmin connection health right now.** Query `garmin_connections` in Supabase, or hit `/api/devices/garmin/diagnose` (needs an authed request), or check Vercel function logs for Garmin API errors. Determine: are the 7 previously-connected users (per `GARMIN-STATUS.md`, 2026-06-21 count — recheck current count) already failing to sync?
2. **Do not attempt to "fix" this by rotating credentials without a plan.** The old app is gone or going regardless of what we do — there is nothing to preserve by acting fast on the credential side.
3. **Founder decision needed:** should RunSmart proactively notify currently-connected users that Garmin sync is temporarily unavailable while a new commercial application goes through Garmin's review? Given the timeline below, this could be a multi-week gap, not an overnight one.
4. **Business reality to state plainly:** between now and the new commercial application's Production approval, **RunSmart has no way to sync real users' Garmin data.** The internal-testing app Marc is asking for explicitly cannot serve external users either (that's the whole point of the tier) — so there is no legitimate interim path. Plan the messaging and expectations around that gap now, not after building the two apps.

---

## Goal

File exactly what Marc asked for — two separate Developer Portal applications, not one reset application:

1. **Internal Testing / Verification application** — Evaluation tier, used only by the team for development, QA, and future Gate-4 screenshot capture. Never connects a real RunSmart end user.
2. **Commercial application** — filed for Production review, carrying the brand-compliance fixes already merged (iOS PR #69/#70), submitted with on-device evidence once ready. This is the only application that may ever serve real users, and only after Garmin approves it.

Plus a code-level fix so this cannot happen again: environment separation between the two credential sets, with production traffic hard-gated to the commercial app's credentials only.

---

## Steps

### Step 1 — File the Internal Testing / Verification application (fast, low-risk, do first)
1. Founder logs into `developerportal.garmin.com`.
2. Create a new application:
   - **Name:** `RunSmart - Internal Test` (or similar — avoid anything that could look production-facing to a future reviewer)
   - **Tier:** Evaluation
   - **Scope:** Health API + Activity API (import only), same as before — no Training/Courses API
   - **Users:** only the founder's own Garmin test account(s), explicitly never a real customer
3. Record the new `client_id`/`client_secret` — these go into a **non-production** environment only (local `.env`, Vercel Preview, or a dedicated staging env), never the production Vercel environment.
4. This is the application used going forward for Gate-4 screenshot capture, QA, and any dev-time Garmin testing.

### Step 2 — File the Commercial application (needs the evidence pipeline finished first)
1. Create a second new application:
   - **Name:** `RunSmart` (or the existing public-facing name) — this is the one intended for real users
   - **Tier:** request Production directly (or Evaluation-then-Production if the portal requires evaluation first — observe what the portal actually offers and report back, since we don't know its exact flow for a *new* application)
   - **Scope:** Health API + Activity API (import only) — do **not** request Training/Courses API (see `12-MARC-2026-06-22-REJECTION-REMEDIATION-PLAN.md` for why this caused an earlier unresolvable demand)
2. Do not submit this one for Production review until the on-device evidence below is done — submitting with stale/simulator evidence risks a 4th rejection.
3. Commercial terms (restate, already answered by Garmin 2026-06-15, don't re-litigate):

| Question | Answer |
|---|---|
| Q1 — Subscription use of Garmin data | YES |
| Q2 — AI coaching derived from Garmin data | YES |
| Q3 — License fees | NO fees |
| Q4 — Historical data window | 30 days max |
| Q5/Q6 — Attribution + "Works with Garmin Connect" wording | Deferred to brand guidelines — keep conservative wording |

4. Team/account section: only `nadav.yigal@runsmart-ai.com` on the account (company domain, no freemail), API Blog notifications enabled, no third-party integrators.

### Step 3 — Finish the on-device evidence pipeline (blocking dependency for Step 2's submission)
1. Merges already done: iOS PR #69 (Garmin Wellness rename + logo clipShape fix), PR #70 (version bump to 1.0.7/20).
2. Founder archives, uploads, and confirms `1.0.7 (20)` genuinely live on the App Store.
3. Recapture all 6 Gate-4 screenshots on a **real device** against that live build — not simulator, not a pre-fix build.
4. Re-verify each screenshot against `Garmin_Developer_API_Brand_Guidelines.pdf` and the Hashiri.AI/NeverDone reference examples.
5. Re-verify `garmin-connect-tile.jpg` (currently a 512×512 lossy JPEG) is the pristine official asset from `developer.garmin.com/brand-guidelines/connect/`, not a re-saved capture.
6. Attach this evidence to the **commercial** application's Production submission (Step 2), using the new internal-testing app's credentials to actually capture the screenshots (Step 1) so no real user data is involved.

### Step 4 — Code fix: hard-separate the two credential sets (do this regardless of portal timing)
This is the structural fix for the root cause, independent of the Garmin portal work:
1. Split `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` into environment-scoped variants — e.g. `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` remain the production (commercial-app) credentials, and add `GARMIN_TEST_CLIENT_ID`/`GARMIN_TEST_CLIENT_SECRET` for the internal-testing app, read only in non-production environments.
2. Add an explicit runtime guard (e.g. in `garmin-oauth-store.ts`) that refuses to start an OAuth flow using test credentials if `NODE_ENV === 'production'` / `VERCEL_ENV === 'production'` — this is the one-line safeguard that would have prevented today's escalation.
3. This does not need to wait for the portal work — it can be built and merged now, then wired to the real credentials once both applications exist.

### Step 5 — Update tracking docs
1. `docs/garmin-application/GARMIN-STATUS.md` — record both new applications' portal references, which credentials went where, and the deactivation timeline for the old app.
2. Both repos' `tasks/progress.md` — reflect that RunSmart's Garmin integration is down for real users pending the commercial app's Production approval.
3. Do not update production Vercel env vars until the commercial application's credentials exist and Step 4's code guard is merged.

---

## Constraints

- No submission to Garmin, and no message to Marc, without the founder confirming wording in the same session.
- Do not connect any real RunSmart user account to the internal-testing application, ever — that's the exact mistake being corrected.
- Do not resubmit the commercial application for Production review using simulator screenshots or a pre-fix build.
- Do not re-add Training/Courses API scope to either application.
- Do not rotate production `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` until Step 4's code guard is merged and the commercial application's credentials are confirmed.

---

## Acceptance criteria

- [ ] Current live-user impact checked and reported (are the 7 previously-connected users already failing?)
- [ ] Internal Testing / Verification application created (Evaluation tier), credentials stored in a non-production environment only
- [ ] Code guard merged: production can never authenticate using test/internal credentials
- [ ] On-device Gate-4 screenshots recaptured against `1.0.7 (20)` live build, re-verified against the brand PDF
- [ ] `garmin-connect-tile.jpg` confirmed pristine or replaced
- [ ] Commercial application created and submitted for Production review with current evidence, no Training API scope
- [ ] `GARMIN-STATUS.md` and both repos' `tasks/progress.md` updated with both applications' references and the user-impact timeline
- [ ] Founder has decided on user-facing messaging for the sync-outage gap

---

## Return format (for Codex to fill in)

- Live-user impact confirmed (yes/no, how many affected):
- Internal Testing application ID/reference:
- Commercial application ID/reference, submission status:
- Code guard PR link:
- Screenshot zip filename used for the commercial submission:
- Files changed:
- What was NOT done / blockers:
