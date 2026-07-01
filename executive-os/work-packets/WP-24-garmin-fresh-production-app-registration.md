# WP-24 — Garmin: File a Fresh Developer Portal Production Application

**Created:** 2026-07-01
**Status:** Not started — ready to execute
**Repos:** `/Users/nadavyigal/Documents/RunSmart` (web/backend), `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` (iOS)
**External system:** Garmin Developer Portal (`developerportal.garmin.com`) — browser-based, founder-authenticated
**Execute with:** Codex, in a session where the founder has the Garmin Developer Portal open and logged in in their own browser. Codex reads/writes the repos for supporting evidence and drives the field-by-field portal work; the founder performs the actual clicks/logins since this is founder-credentialed and external.
**Related:** [[project_runsmart_ios_live_version]] memory; iOS PR #69 (merged) and web PR #109 (merged) fixed the code-level brand violations that caused this; `docs/garmin-application/GARMIN-STATUS.md` is the living status doc for this whole saga.

---

## Read this before starting — the one risk that can cause an outage

RunSmart's backend authenticates with Garmin using a single pair of environment variables, confirmed live in `v0/lib/server/garmin-oauth-store.ts` and `v0/app/garmin/connect/route.ts`:

```
GARMIN_CLIENT_ID
GARMIN_CLIENT_SECRET
```

**If the Garmin Developer Portal only lets you register a brand-new application with its own new client ID/secret (rather than resetting the existing one back to a clean state), swapping those values in production will invalidate every currently-connected user's OAuth token.** GARMIN-STATUS.md records 7 actively-connected users as of 2026-06-21. Those users would silently stop syncing until they manually reconnect Garmin — this is a real, live-user-facing outage risk, not a hypothetical.

**First action in the portal, before filling in anything:** determine whether Garmin's UI supports either (a) resetting/starting over the *existing* application's Production request without regenerating credentials, or (b) only lets you spin up a fully separate app with new credentials. This determines the whole plan below. If it's (b), do not cut over `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` in Vercel production until there is an explicit plan for migrating or notifying the 7 connected users — check with the founder before touching those env vars.

---

## Context — why this WP exists

Garmin Connect Partner Services (Marc Lussi) has rejected RunSmart's Gate 4 (UX/brand compliance) evidence **three times**: 2026-06-22, 2026-06-26, and 2026-07-01 (same day the "fully fixed" 1.0.6(19) evidence was sent). The 2026-07-01 rejection was blunt: "Garmin Wellness" is not a recognized term in Garmin's brand guidelines, the logo is still not compliant, and Marc's exact words were "Please generate a production app to start all over."

Founder's read on "start all over" (confirmed 2026-07-01): **stop patching the same rejected Developer Portal application record and file a fresh Production application request**, rather than continuing to resubmit incremental fixes against a record Garmin has now rejected three times.

The underlying code violations that caused the last two rejections are already fixed and merged to `main` in both repos (2026-07-01):
- "Garmin Wellness" as an invented compound feature/product name — fully renamed to "Wellness Trends" across the iOS app (iOS PR #69).
- The official Garmin Connect tile being reshaped via `.clipShape(RoundedRectangle(...))` in two places — removed (iOS PR #69).
- Still open and unverified: whether `GarminConnectTile.imageset/garmin-connect-tile.jpg` (a 512×512 lossy JPEG) is the pristine official asset from Garmin's brand kit or a re-saved capture. Re-verify/re-download before attaching it as evidence to the new application.

---

## Goal

File a new (or cleanly reset) Garmin Developer Portal Production application request that:
1. Does not carry forward the two specific defects Marc flagged (naming, logo alteration) — both are already fixed in code as of this WP's creation.
2. Is submitted with brand-compliant, on-device-verified evidence, not simulator screenshots or evidence from a build predating the fixes.
3. Does not silently break the 7 users currently connected via the existing Garmin integration.

---

## Steps

### Step 0 — Reconnaissance (do this first, before any field entry)
1. Founder logs into `developerportal.garmin.com` in their browser.
2. Locate the existing RunSmart application record (the one with 3 rejections). Screenshot or describe its current status/tier.
3. Look for any portal option like "Start New Application," "Reset Request," "Withdraw and Resubmit," or similar — Garmin's actual UI capability here is unknown to us and needs to be observed directly, not assumed.
4. Report back: can the existing app's Production request be reset without new credentials, or does starting fresh mean a genuinely new app registration with new `client_id`/`client_secret`? This determines whether the credential-rotation risk above applies.

### Step 1 — Prepare the on-device evidence (blocking dependency, do not skip)
Do NOT proceed to submission until this is done:
1. Merge is already done (iOS PR #69, web PR #109 both merged to `main` 2026-07-01).
2. Bump the iOS app version/build, archive, upload to App Store Connect, confirm genuinely live (founder-only Xcode step, no git-visible commit — check the live App Store listing, not just a commit message).
3. Recapture all 6 Gate-4 screenshots on a **real device** against that live build.
4. Re-verify each screenshot against `Garmin_Developer_API_Brand_Guidelines.pdf` and the Hashiri.AI/NeverDone reference examples Garmin previously sent — don't assume the code fix alone is sufficient without a visual re-check.
5. Re-verify `garmin-connect-tile.jpg` is the pristine asset from `developer.garmin.com/brand-guidelines/connect/`, not a re-saved capture — re-download if there's any doubt.

### Step 2 — Re-declare application scope (learn from the Training API mistake)
The previous rejected application had the Training/Courses API enabled in the portal even though RunSmart is import-only and never used it — this created an unresolvable "produce a transfer screenshot" demand in an earlier rejection round (documented in `12-MARC-2026-06-22-REJECTION-REMEDIATION-PLAN.md`, later parked per the 2026-06-25 decision). When filling in the new application's requested scopes, only request:
- Health API (wellness/stress/HRV/sleep — import only)
- Activity API (import only)
- Do **not** request Training/Courses API this time.

### Step 3 — Re-enter commercial terms (already answered once, don't re-litigate)
Garmin already answered these on 2026-06-15 — restate the same answers, don't ask again:
| Question | Garmin's answer |
|---|---|
| Q1 — Subscription use of Garmin data | YES |
| Q2 — AI coaching derived from Garmin data | YES |
| Q3 — License fees | NO fees |
| Q4 — Historical data window | 30 days max |
| Q5/Q6 — Attribution + "Works with Garmin Connect" wording | Deferred to brand guidelines — keep conservative wording |

### Step 4 — Team/account section
Already compliant, restate: only `nadav.yigal@runsmart-ai.com` on the account (company domain, no freemail), API Blog notifications enabled, no third-party integrators.

### Step 5 — Attach evidence and submit
1. Privacy policy anchor: `https://runsmart-ai.com/privacy#garmin-connect-data` (already live, Gate 1 previously passed).
2. Technical/Gate 2 evidence: PUSH webhook async 200 response, User Deregistration + User Permission endpoints, most recent Partner Verification / Data Generator run.
3. Attach the on-device screenshot zip from Step 1 (name it with today's date, do not reuse the 2026-07-01 zip that was part of the rejected submission).
4. Submit.

### Step 6 — Update tracking docs
1. `docs/garmin-application/GARMIN-STATUS.md` — record the new application's portal reference/ID (or confirm it's the same app just reset), submission date, and evidence zip filename.
2. RunSmart iOS `tasks/progress.md` and RunSmart web equivalent — reflect the new submission state.
3. If the credential-rotation risk from the top of this WP materialized (new `client_id`/`client_secret`), do NOT update Vercel production env vars as part of this WP — that is a separate, explicitly-approved step given the live-user impact.

---

## Constraints

- No message is sent to Marc/Garmin, and no submission is finalized, without the founder confirming the exact wording and evidence in the same session — this is an external, semi-irreversible action (a 4th rejection would further damage the partner relationship).
- Do not rotate `GARMIN_CLIENT_ID`/`GARMIN_CLIENT_SECRET` in production without a separate, explicit founder go-ahead and a plan for the 7 currently-connected users.
- Do not resubmit using simulator screenshots or a pre-fix build — the whole point of this WP is evidence that is actually correct this time.
- Do not re-add Training/Courses API scope.

---

## Acceptance criteria

- [ ] Reconnaissance done: confirmed whether this is a true new app (new credentials) or a reset of the existing record
- [ ] On-device screenshots recaptured against a live build containing the iOS PR #69 fixes, re-verified against the brand PDF
- [ ] `garmin-connect-tile.jpg` confirmed to be the pristine official asset (or replaced with a freshly downloaded one)
- [ ] New/reset Production application submitted with: correct scope (no Training API), restated commercial terms, current evidence
- [ ] `GARMIN-STATUS.md` and both repos' `tasks/progress.md` updated with the new submission state
- [ ] No production env var change made without a separate explicit founder approval

---

## Return format (for Codex to fill in)

- Portal capability found (new app vs. reset existing): 
- New application ID/reference (if applicable):
- Credential-rotation risk realized (yes/no), and if yes, what was done about the 7 connected users:
- Screenshot zip filename used for this submission:
- Submission confirmation reference:
- Files changed:
- What was NOT done / blockers:
