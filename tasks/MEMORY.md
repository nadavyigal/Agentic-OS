# Agentic OS Memory

Repo-local decisions and session history for `/Users/nadavyigal/Documents/Projects /Agentic OS`.

Use this file for durable Agentic OS learnings that are likely to matter again. Keep entries concise and auditable. Do not store secrets, credentials, customer data, or one-off preferences.

## 2026-06-04 - ROOT CAUSE of "lost information": worktree fragmentation + OS registry fix
CRITICAL LESSON: The founder's COO OS (executive-os/COO-OS.md, agents/coo-agent.md, workflows/coo-operating-review.md, BUSINESS-GTM-PLAN-V0.md, work-packets/WP-1, PROMPTS/coo-operating-review.md, + edits to EXECUTIVE-DECISIONS/RHYTHM/README) was created in worktree `clever-shannon-04b041` and NEVER committed/merged. My dashboard work was uncommitted in `elastic-babbage-020866`. There are 12 worktrees, all branched off the same commit, none merged. The dashboard reads the MAIN repo, which had neither. THIS is why information "kept disappearing": parallel uncommitted worktrees + a dashboard that only surfaced hand-wired things.
Fixes shipped (in elastic-babbage-020866):
- Consolidated the COO OS from clever-shannon into this worktree (copied all 7 new files + 3 modified docs). Nothing lost.
- OS REGISTRY (`build_os_registry()` in cli.py): auto-discovers executive-os/*-OS.md (CEO/COO/CFO/Analysis), executive-os/agents/*, executive-os/work-packets/* (with status), SKILLS/*, distribution-os, and the ./agentic-os commands. Written to status.json `osRegistry`. Anything created under these folders now surfaces automatically — the structural fix so nothing is invisible again. Confirmed: COO OS, COO Agent, WP-1 (Active) all surface.
- Command Center HTML rewritten SIMPLE: brief + one command + Commands (all 5, what each does) + The OS (registry incl COO) + Projects. Removed tabs, action board, saved-plans board, agent queue, project prompts. Plain short copy.
- data-flow.html = a real orchestration DIAGRAM (Sources -> Engine -> What you see) with LIVE counts; a red 0 = that source is not being surfaced (so GTM/COO gaps are visible at a glance).
- command-center.html mirrored to index.html. 28 tests pass, verify passed, screenshot-confirmed render (only harmless favicon 404).
OPERATING RULE (do not repeat the mistake): Do NOT scatter work across per-session worktrees and leave it uncommitted. Work on one branch, commit, and MERGE TO MAIN at session end. Before starting, check other worktrees (`git worktree list`) for unmerged founder work and consolidate. The dashboard trusts the repo on disk — uncommitted parallel worktrees = lost information.
Open: This branch is NOT merged to main yet. The 11 other worktrees may hold more unmerged work — needs a consolidation/cleanup pass. Recommend: merge elastic-babbage-020866 to main, then prune stale worktrees.

## 2026-06-04 - ONE trustworthy morning process: derived brief + all saved plans surfaced
Worked on: Two rounds. (1) Root-caused why `./agentic-os morning` served stale data ("build 6 in review" after build 8 shipped) and lost context (GTM invisible). (2) Per founder: collapse the two processes (`./agentic-os morning` + a separate "write the morning brief" agent step) into ONE, surface EVERY saved plan, keep HTML + localhost in the one flow.
Root cause: `morning` = refresh + verify + serve, NO synthesis step. Refresh regenerated evidence (taskParse, projectHealth) but never rewrote the narrative the founder reads (summary.overallStatus/bestNextAction, priorityBoard, per-project status). Those were hand-written and rotted; drift was flagged, never reconciled. And `collect_evidence` only scanned tasks/* + a few docs/*, so plans (GTM, specs) could never surface.
Final design (single process, no agent overlay):
- `build_derived_summary()` rebuilds headline + priority board from parsed repo truth EVERY run. overallStatus: the two apps get "Name — phase: nextAction" inline, support repos get phase only. bestNextAction ranks the apps and prefers the non-"monitor" action. No synthesizedOn gate, no synthesisMode, no two modes — those fields are retired on every refresh. The dashboard is literally the repos, re-derived.
- High-confidence per-project cards overwrite displayed currentPhase/activeStory/nextRecommendedStory/lastCompletedStory/lastValidation from parsed tasks/progress.md. Drift went 8 → 0.
- `collect_plans()` + `build_saved_plans()`: scans docs/superpowers/plans, docs/plans, docs/superpowers/specs, docs/specs, and `*plan*` files under .agent-os/distribution (distribution scaffold reference docs like audience/channels are excluded). Per project: newest first, 6 shown + GTM always kept + total count. New "Saved Plans & Requests" panel on the Plan tab. 30 real plans surfaced across 5 projects (RunSmart iOS 17, etc.).
- `parse_gtm()` surfaces GTM positioning/status/date on each project card + priority board. command-center.html made a true mirror of index.html (was a divergent older copy).
- `./agentic-os morning` is the ONE command: refresh → surface plans → derive brief → update HTML → verify → serve localhost. README + PROMPTS/morning-brief.md rewritten to the one-process model (no stamp step).
- 28 hermetic tests pass (added TestGtm, TestPlans, TestDerivedSummary). verify passed. git diff --check clean.
Files hand-edited: scripts/agentic_os/cli.py, scripts/agentic_os/test_cli.py, dashboard/index.html, dashboard/command-center.html, dashboard/README.md, dashboard/status.json, PROMPTS/morning-brief.md, tasks/MEMORY.md. (DASHBOARD.md, PROJECT-STATUS.md, executive-os/EXECUTIVE-DASHBOARD.md, project-status.html, orchestration.html regenerated by refresh.)
Decisions: One process, one source of truth = parsed repos, re-derived each run (founder delegated the call). Mechanical-but-true beats rich-but-stale; depth lives in the cards + Saved Plans board, headline is the true index. Distribution scaffold files are NOT plans (only *plan* there).
Open: Work is on worktree branch claude/elastic-babbage-020866, NOT merged to main. Needs PR.
Next session: Real product state — RunSmart iOS build 8 in Apple review (build 6 rejected 2.1a); Resumely iOS pre-submission, founder device smoke on iPhone 13 is the gate. To get status anytime: run `./agentic-os morning` (that is the whole process).

## 2026-06-01 - Cross-project closeout, morning brief, status refresh
Worked on: End-of-day cross-project closeout across RunSmart, Resumely, web support repos, Agentic OS, and Executive OS.
Completed: Ran the morning-brief evidence protocol from local files and git. Refreshed `PROJECT-STATUS.md`, `DASHBOARD.md`, `dashboard/status.json`, `dashboard/index.html` fallback JSON, `dashboard/orchestration.html`, `executive-os/EXECUTIVE-DASHBOARD.md`, `executive-os/EXECUTIVE-DECISIONS.md`, and `executive-os/EXECUTIVE-METRICS.md`. Updated EXD-004 to Decided because Resumely PostHog was integrated before first App Store submission.
In progress: Resumely iOS still needs authenticated real-device smoke, PostHog/export coverage confirmation, and ASC upload/submit. RunSmart iOS is in Apple review context and should keep v1.0 artifacts frozen. RunSmart Web and ResumeBuilder Web both need dirty-tree triage before further implementation.
Decisions: Treat Resumely smoke + submit as the next highest-leverage portfolio action. Do not start broad RunSmart 1.0.1 implementation until v1.0 review outcome is known. Continue using local project files and git as status evidence; no external dashboards were queried.
Next session: Start with Resumely iOS device smoke from `tasks/session-log.md`, then upload/submit if it passes. If RunSmart receives Apple feedback first, handle that before 1.0.1 work.

## 2026-05-31 (eve) - Dashboard suite: unify design, status refresh, Planner + Runs + Memory
Worked on: Second pass on the dashboard suite per founder feedback (5 points).
Completed: (1) Status refresh from product-repo git: RunSmart iOS submitted to review + E7 Garmin HRV/readiness trends shipped + 1.0.1 fast-follow UX spec drafted; Resumely iOS PostHog integrated (PR #35 into #36) + PR#36 UX transformation + PII guard. Updated status.json, index.html embedded copy, orchestration.html. (2) Unified design: rewrote styles.css to the dark theme; all three pages share one top nav (.osnav). (3) Added Layer 9 "Memory & Learning" to the orchestration map. (4) Command Center Planner group (generate sprint / resolve decisions / draft feature) fusing action + decision boards. (5) Command Center Runs group (morning-brief, exec-review, distribution, qa, risk, lessons, pr-summary).
Verified: 4 JSON blocks parse; 65/65 Command Center deep links exist; git diff --check clean; all 3 pages screenshotted on localhost:8787 (only console error is a harmless favicon 404).
Decisions: Work directly in the main checkout (not the worktree) since localhost serves from main and the founder's flow is commit→merge→push→serve-from-main. Planner/Runs/Memory are plain `groups` in cc-data (no new render code). To keep index.html file:// fallback current, mirror status.json via the sync snippet in dashboard/README.md.
Next session: If RunSmart 1.0.1 scope locks or Resumely submits, refresh status.json + re-sync index.html. Add Runs/OS cards as the system grows.

## 2026-05-31 - OS Command Center + Orchestration Map refresh
Worked on: Centralized dashboard to talk to each OS directly, plus refreshing the Orchestration Map after iOS + Agentic OS progress.
Completed: Built `dashboard/command-center.html` (new) — a static launcher with one card per OS (CEO, CFO, Analysis, Director, Distribution, Growth, Architect, PM, QA, Release Manager, UI/UX). Each card has a status dot, a "Copy conversation starter" button (clipboard, with file:// fallback) that pastes a context-loaded prompt into Claude Code/Cursor, deep links into that OS's docs/prompts, and a live keyword filter. Refreshed `dashboard/orchestration.html` (stamp 2026-05-31; RunSmart PostHog/activation events now wired+firing; rs-analytics-001 done; EXD-002/003 resolved + Q2/Q3 OKRs drafted). Cross-linked all three dashboards (index + status.json nav now include Command Center + Orchestration Map). Documented the new file in `dashboard/README.md`.
Verified: All 4 embedded/JSON blocks parse; all 34 deep-link targets exist on disk; `git diff --check` clean. No live browser screenshot (no server; reuses orchestration.html's proven CSS).
Decisions: Interaction model = "launcher + deep links" (user choice). Live embedded chat rejected — would break dashboard guardrails (no backend, no API key in code, no paid service). To add an OS: append to a group's `items` array in the `cc-data` JSON block; `{date}` auto-fills the generated date.
Next session: If new OSes/agents are added under SKILLS/ or executive-os/, add matching cards. Consider a `gen` note in README for keeping the Command Center status dots in sync with status.json.

## 2026-05-31 - Codex, Cursor, Claude Code Alignment
Worked on: Aligning repo-local agent routing so Codex, Cursor, and Claude Code share `AGENTS.md` as the source of truth while keeping tool-specific adapters lean.
Completed: Added Codex guardrails, repo-local memory/error files, Cursor routing updates, Claude `@AGENTS.md` import while preserving Claude-specific repo context, executive-os local instructions, and alignment docs.
In progress: Manual cleanup remains outside this repo: rotate the exposed Resend token and remove the matching allowlist entry from `~/.claude/settings.json`.
Decisions: Do not modify files under `~/.claude/` from Codex. The known Resend token cleanup is a manual Claude/global-config task.
Next session: Re-check alignment files before changing agent behavior again.
