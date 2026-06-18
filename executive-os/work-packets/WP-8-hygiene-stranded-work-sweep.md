---
title: "Work Packet: Hygiene + Stranded-Work Sweep"
date: 2026-06-17
type: work-packet
project: RunSmart iOS, Resumely iOS (+ Agentic OS stranded board)
status: active
priority: 2
tags: [hygiene, stranded-work, worktrees, git, trust]
---

# Work Packet — Hygiene + Stranded-Work Sweep

> Run in each affected product repo (RunSmart iOS, Resumely iOS), then re-check the
> Agentic OS dashboard. Goal: clear the hygiene warnings that are holding portfolioTrust
> at "refresh_required" so the dashboard reads trustworthy/clean.

- Status: Active
- Source: dashboard/status.json portfolioTrust + strandedWork on 2026-06-17
- Workflow pattern: normal
- Input trust: trusted
- Success signal: portfolioTrust level returns to trustworthy (no hygiene warnings); stranded-work count -> 0 or each remaining item explicitly justified; extra worktrees resolved (merged/PR'd or removed).

## Owner Role
Release Manager / QA

## Verified Evidence (do not re-litigate)
- portfolioTrust.level = "refresh_required"; reasons include "5 uncommitted change(s)".
- hygieneWarnings: "Uncommitted files in product repos: RunSmart iOS, Resumely iOS." and "Extra product worktrees retained for review: RunSmart iOS (2), Resumely iOS (5)."
- daily-refresh notification: "stranded-work notification sent (17 items)".
- Both repos are actively used (live apps + recent Codex work), so dirty state is real, not noise.

## Repos to Sweep

### RunSmart iOS
Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
- 21 uncommitted files in primary working tree
- 2 extra worktrees:
  - `claude/tender-thompson-60f370`
  - `claude/youthful-moore-9d85c7`

### Resumely iOS
Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- 40 uncommitted files in primary working tree
- 5 extra worktrees:
  - `codex/post-live-d7-readout`
  - `codex/resumely-release-qa`
  - `claude/focused-raman-18ce50`
  - `version-2` (mapped at relaxed-northcutt-cb6240)
  - `claude/reverent-buck-a366b2`
- 3 unmerged branches: `claude/relaxed-northcutt-cb6240`, `feat/localization-updates`, `monitization`
- main is 2 commits behind origin (pull needed first)

## Tasks (in order)
1. List stranded items: read dashboard/status.json strandedWork.items (17). For each, classify: (a) commit & push, (b) discard, (c) keep with a one-line reason. Do not bulk-delete.
2. RunSmart iOS repo: `git status --short --branch` per worktree. Commit + push real work; discard throwaway; for the 2 extra worktrees decide merge/PR or `git worktree remove`. No force-delete of unmerged work.
3. Resumely iOS repo: same for its 5 extra worktrees. This is the bigger source of drift -- be deliberate; PR anything with real commits before removing.
4. Re-run `./agentic-os refresh` (or morning) and confirm hygieneWarnings cleared and portfolioTrust improved.

## Constraints
- Never delete a worktree/branch with unmerged commits without PR'ing or explicitly confirming it's throwaway.
- Do not merge `version-2` or `monitization` branches (founder rule).
- No product source changes in this packet -- hygiene only.
- Scope gate: if a "dirty file" turns out to be real unfinished feature work, stop and surface it as its own packet rather than committing blindly.

## Validation
- Each repo: `git status --short --branch` clean (or remaining items justified) + pushed.
- `./agentic-os doctor` PASS and portfolioTrust no longer lists uncommitted/worktree warnings.

## Final Output
- Stranded items: resolved / kept (with reasons)
- Worktrees: per-repo disposition (merged, PR'd, removed)
- Commits pushed per repo (branch, count)
- Final portfolioTrust level
- Remaining risks
