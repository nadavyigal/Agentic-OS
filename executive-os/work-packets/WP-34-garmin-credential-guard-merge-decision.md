# Work Packet WP-34 - Garmin Credential Guard: Merge or Explicitly Park

- Status: Closed — explicitly parked (2026-07-05, EXD-019)
- Created: 2026-07-05
- Source: Weekly review 2026-07-05 — flagged twice now (2026-07-02 STORM analysis, 2026-07-05 weekly review) as finished code sitting stranded, unmerged
- Mode: Builder (mechanical merge) + founder confirmation that maintenance-mode still wants it
- Workflow pattern: single story
- Outcome loop: Garmin maintenance track (EXD-015 — no new Developer Portal apps, no relaunch push, but "keep the 5 currently-synced users working" is explicitly still in scope)
- Related: WP-24 through WP-28 (Garmin relaunch sequence, paused per EXD-015); `Garmin-Integration` vault living page

## Why this packet exists

The credential-guard fix is done code, not a research gap — commit `baa19aa` on branch `codex/wp24-garmin-credential-guard` in the RunSmart iOS repo is complete and stranded local-only (no origin branch), confirmed by a live git read on 2026-07-02 and still true as of 2026-07-05. Under EXD-015's maintenance-only framing, finished work protecting the 5 currently-synced users' credentials should not sit idle just because the surrounding relaunch push is paused.

## Project

RunSmart iOS: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Task

1. Check out `codex/wp24-garmin-credential-guard`, diff `baa19aa` against current `main` to confirm it still applies cleanly (branch may have drifted since 2026-07-02).
2. If clean: push the branch to origin, open a PR, run the repo's normal test suite, merge.
3. If drifted: rebase, re-verify the fix still does what WP-24/25 intended (gates new Garmin connections / guards credentials), then proceed as above.
4. If founder decides maintenance-mode means *not* touching Garmin code at all right now: close this packet as explicitly parked (not silently dropped) with a one-line reason and a review date.

## Constraints

- Maintenance-mode per EXD-015: this merge should not become a wedge for restarting the paused relaunch work (new portal apps, Production resubmission). Scope is exactly this one stranded fix.
- No new Garmin scope added while merging — mechanical integration only.
- No new dependencies. No secrets in code.

## Acceptance

- Either: commit is live on `main` (or the repo's release branch) and the PR is linked here, or: packet is closed as "explicitly parked" with a reason and review date — but not left silently stranded a third time.

## Validation

- Repo's existing test suite passes post-merge.
- `Garmin-Integration` vault living page and RunSmart's `tasks/progress.md` updated to reflect the merge (or the explicit-park decision).

## Progress

- 2026-07-05: Packet created from weekly review — this is the second time the stranded commit has been flagged without action. Not started.
- 2026-07-05: Founder asked to check status. Verification in RunSmart iOS repo found current `main` clean at `8b9dfee` (`origin/main`), with Garmin-related branches present but no `codex/wp24-garmin-credential-guard` branch, no local commit `baa19aa`, and no branch containing that commit. `tasks/progress.md` currently points to WP-27 Garmin Gate-4 evidence cleanup / Garmin Data Trust Audit, not a completed credential-guard merge. Treat this packet as not completed until the missing branch/commit is recovered from another clone/worktree or the decision is explicitly parked.
- 2026-07-05: Exhaustive recovery attempt run in the RunSmart iOS repo — `git cat-file -t baa19aa` (invalid object), `git branch -a` / `git log --all` / `git reflog` (no match), `git fsck --unreachable` (no matching commit), `git stash list` (no match), `git fetch origin` + `git ls-remote` (no remote branch), local backup bundle `runsmart-local-branches-backup-20260520-144014.bundle` (18 heads, none credential/wp24), other machine clones (no match). Logged in RunSmart iOS `tasks/ERRORS.md`. Confirmed genuinely unrecoverable, not just unmerged.
- 2026-07-05: Founder decision: park, do not reimplement. Recorded as EXD-019 in `EXECUTIVE-DECISIONS.md`. Packet closed — the credential-guard hardening does not exist and is deliberately not being rebuilt this week; the 5 currently-synced Garmin users are unaffected since this only gates *new* connection attempts. Revisit at the 2026-08-01 EXD-015 reread.
- 2026-07-08: Closure re-verified — no change since EXD-019. RunSmart iOS repo: `git cat-file -t baa19aa` still invalid; no `codex/wp24-garmin-credential-guard` branch local or remote; `tasks/ERRORS.md` incident log present. No PR, no merge, no reimplementation. Note: RunSmart iOS `tasks/progress.md` still says "founder decision required" (predates EXD-019) — stale downstream doc, not a reopen of this packet. Revisit date unchanged: **2026-08-01** with EXD-015 reread. (Separate scope: RunSmart **Web** credential guard from WP-25 is merged and live; this packet tracked only the lost iOS/web-local commit `baa19aa`.)
