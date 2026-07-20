# Agentic OS — consolidated session (2026-07-20)

Repo: `/Users/nadavyigal/Documents/Projects /Agentic OS` — work on `main`, not in a worktree.

## Context

Portfolio HQ trust reads **"Refresh required"**, and the only remaining cause is 2 open worktrees. Both were verified on 2026-07-20 to have **zero unique commits** and to be ancestors of `main`, so removing the worktrees loses nothing.

Today's session exposed a structural weakness worth fixing, not just the symptoms of it.

## Do these in order

**1. Clear the trust blocker without deleting branches.** The founder explicitly declined branch deletion on 2026-07-20, so do **not** run `./agentic-os clean --apply` (it plans branch deletes across four repos). Instead remove only the finished worktrees:

```
git worktree remove ".claude/worktrees/ios-apps-status-update-7f220b"
git worktree remove ".claude/worktrees/resumely-ftux-release-b-c-b5e864"
```

Each has one dirty file (`tasks/progress.md`) so `--force` may be needed — inspect the diff first and preserve anything real. Every branch stays intact. Then commit the loose preview scaffolding (`.claude/launch.json`, `.claude/serve-portfolio-hq.py`, `.claude/serve-portfolio-hq.sh`), run `./agentic-os morning`, and confirm trust reads **actionable**.

**2. Audit the remaining Launch Pad cards.** `dashboard/portfolio-hq-manual.json` had 47 stale-claim matches on 2026-07-20; roughly 20 present-tense ones were corrected across `tracks`, `clocks`, `activationHeadline`, `knownUnknown`, `weekPriorities` and `suggestedSessions`. The 4 `founderCommand` cards are current. **The other ~13 Launch Pad cards were never individually verified** — check each against live git and store state, and rewrite or delete what has gone false.

**3. Fix the root cause, not just the rot.** `portfolio-hq-manual.json` is hand-maintained input that `./agentic-os refresh` never writes, so it decays silently while the page renders `asOf` as today — a current-looking date stamp over stale content, which is worse than an obviously old page. Options: stamp each manual block with its own last-verified date and surface anything older than N days as a visible warning; or cross-check a few machine-verifiable claims (live App Store version, merged PR numbers) against real sources during refresh and flag contradictions. Pick one and implement it.

**4. Document the PostHog project trap.** On 2026-07-20 the MCP reported project 171597 "Running coach" as active, but the first several queries returned ResumeBuilder data and an empty result that nearly got reported as a RunSmart analytics outage. Explicitly calling `switch-project` fixed it. Verified mapping: **RunSmart = 171597**, **Resumely = 270848**, and RunSmart's project contains zero Resumely events (checked over 60 days). Add to `LESSONS.md`: always `switch-project` explicitly and confirm with an event-name query before trusting any PostHog read.

**5. Verify the morning process changes hold.** The `morning-brief` skill was updated to run `./agentic-os morning` (not `refresh`, which skips verify and never opens Portfolio HQ), to check whether yesterday's EOD block was filled, and to verify live versions against Apple's lookup API. `AGENTS.md` was repointed off the retired `~/.claude/MEMORY.md`. Run one morning brief and confirm each step actually fires.

## Constraints

- Work on `main`. Do not create worktrees or feature branches for OS work.
- Do NOT delete any branch.
- Do not invent status. Every claim needs a dated source; git and the store beat prose files.
- Do not introduce new dependencies, MCP servers, or process layers.

## Validation

`./agentic-os test` (72+ tests), `./agentic-os verify`, `git diff --check`. Confirm Portfolio HQ trust level and that the page renders.

## Completion gate

Commit to `main`, push, and confirm 0 unpushed. Add an `INTENT-LOG.md` entry. Update `LESSONS.md` if a durable lesson came out of it.
