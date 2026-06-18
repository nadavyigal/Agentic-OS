---
title: "Work Packet: Arm the Status Guard + Reconcile to Live"
date: 2026-06-17
type: work-packet
project: Agentic OS (+ RunSmart iOS, Resumely iOS progress.md)
status: closed
priority: 1
closed_date: 2026-06-18
closed_note: PostHog guard armed and verified — 0 contradictions, 60/60 tests pass. launchd exit 126 (TCC/Full Disk Access) tracked separately.
tags: [agentic-os, status, trust, posthog, ground-truth, reconcile]
---

# Work Packet — Arm the Status Guard + Reconcile to Live

> Run in: `/Users/nadavyigal/Documents/Projects /Agentic OS` (config + verification);
> two one-line edits in RunSmart iOS and Resumely iOS `tasks/progress.md`.
> This FINISHES the status-truth job: the guard exists but is switched off, and the
> dashboard still shows both live apps as "in review".

- Status: Active
- Source: Live verification 2026-06-17 (doctor PASS, status.json groundTruth, PostHog QA)
- Workflow pattern: normal
- Input trust: trusted
- Success signal: With the key armed, `./agentic-os refresh` first FLAGS both apps as hard contradictions (proving the guard works); after reconciling the two status lines, contradictions clear for the right reason and portfolioTrust returns to trustworthy. A future "live vs in-review" drift would be caught automatically.

## Owner Role
Director / Orchestrator (OS engineering)

## Verified Evidence (do not re-litigate)
- doctor PASS; launchd lastExit=0, RunAtLoad=true; mechanical refresh is fixed.
- groundTruth.posthog rows = available:false, source:"missing_key" for BOTH apps. unavailable[] lists "PostHog key not configured" + "App Store state missing". So contradictions:[] is a FALSE all-clear.
- PostHog live (2d): RunSmart (171597) 6 users, last 2026-06-17 12:16; Resumely (270848) 11 users, last 12:31. Both LIVE.
- Declared status still pre-launch: RunSmart iOS progress.md "build 15 ... resubmission prep"; Resumely iOS "In App Store review (build 4)".
- Code: contradiction fires when `declared_prelaunch(state) AND live_users > 0` (hard severity, forces trust down). Env names: AGENTIC_OS_POSTHOG_API_KEY, AGENTIC_OS_APPSTORE_STATES (JSON), AGENTIC_OS_GROUND_TRUTH_OVERRIDES (JSON, for offline tests). Project ids: runsmart-ios=171597, resumebuilder-ios=270848.

## Tasks (in order)
1. Create a READ-ONLY PostHog personal API key (scopes: query/insight read; access to projects 171597 + 270848). Do NOT reuse a write key.
2. Store it so the launchd refresh can see it WITHOUT committing it:
   - Add `EnvironmentVariables` to the plist OR source a gitignored env file (e.g. `~/.config/agentic-os.env`) at the top of `scripts/daily-refresh.sh`. Confirm the path is gitignored. NEVER commit the key.
   - Also set `AGENTIC_OS_APPSTORE_STATES='{"runsmart-ios":"live","resumebuilder-ios":"live"}'` the same way.
3. PROVE the guard fires (before reconciling): run `./agentic-os refresh`, then inspect dashboard/status.json groundTruth.contradictions. EXPECT 2 hard contradictions ("declared in-review but PostHog shows N live users/7d") and portfolioTrust dropping. If it does not fire, debug fetch_posthog_live_users (auth, project id, 7d window) before continuing.
4. Reconcile the status lines (the fix that never happened):
   - RunSmart iOS `tasks/progress.md`: set `Status:` and `Current Phase:` to live on the App Store (cite live PostHog users + date). Commit + push.
   - Resumely iOS `tasks/progress.md`: same. Commit + push.
5. Re-run `./agentic-os refresh`. EXPECT contradictions[] now empty for the RIGHT reason (declared live matches PostHog live) and portfolioTrust no longer flags a status contradiction.
6. Regression-protect: add a `test_cli.py` case using AGENTIC_OS_GROUND_TRUTH_OVERRIDES (live users + declared "in review") asserting a hard contradiction is emitted and trust is forced down. So the guard is provable offline, in CI, forever.

## Constraints
- No secrets in code or git. Key lives only in a gitignored env / plist EnvironmentVariables.
- Read-only key only. No write scopes.
- No new dependencies (stdlib urllib already used).
- Reconcile only the two status lines; do not rewrite the rest of progress.md or touch product source.
- Scope gate: config + 2 status-line edits + 1 test. If it grows beyond that, stop and surface.

## Validation
- Step 3: status.json shows 2 hard contradictions BEFORE reconcile (screenshot/paste the contradictions[] block).
- Step 5: status.json contradictions[] empty AFTER reconcile; doctor still PASS.
- Step 6: new test passes with override fixture (no network needed).
- git status --short --branch + git log @{u}.. in each repo touched before done.

## Final Output
- Where the key is stored (path, confirmed gitignored) -- value NOT included
- Before/after contradictions[] blocks (proof the guard fires then clears)
- progress.md reconciled in both iOS repos (commits pushed)
- New offline contradiction test passing
- Remaining risks + next packet (App Store Connect API for fully automated release-state)
