# OS Optimization Review — 2026-07-03 (Demo 2)

Full-system audit by Claude (Fable 5): global Claude layer (~/.claude), Agentic OS repo, Builder OS vault, all four product repos, automation, and cost telemetry. Every claim below is from a live measurement taken 2026-07-03, not from memory or dashboards.

## Headline

**The OS spends more on itself than on the products it serves.** Last 30 days: $8,589 across 197 sessions, of which Agentic OS ($3,180) + Builder OS vault ($2,987) = **72%**, versus ResumeBuilder ($1,664) + RunSmart ($716) = 28%. The founder's one goal is Resumely activation; the token budget says the priority is the meta-layer. Cache reads are ~half the total bill (5.59B cache-read tokens ≈ $4.3k), driven by long sessions carrying a huge static surface.

## What's healthy (verified)

- Global hooks intact: PreToolUse (git-guard) + Stop both present in settings.json (the 2026-06-12 "hooks silently vanished" failure has not recurred).
- `./agentic-os refresh` runs clean end-to-end, queries PostHog ground truth, reports no drift/stale-evidence warnings.
- Learning files alive: ERRORS.md and LEARNINGS.md last updated 2026-06-30.
- RunSmart iOS and Resumely iOS progress.md exactly match their last commit dates.
- Model routing policy + repo scaffolding exist (GLOBAL-TOOL-USAGE.md, RunSmart PR #106, ResumeBuilder PR #94).
- Auto-memory (24 files) is current and actively used.

## Findings and recommendations (priority order)

### P0-1 · Spend inversion: meta-work eats 72% of the budget
30d by project: Agentic OS $3,180/38 sessions, Vault $2,987/75 sessions (avg $40/session for "thinking layer" work), ResumeBuilder $1,664, RunSmart $716.
**Fix:** add a product-vs-meta split line to the morning brief from `dashboard/usage.json` (data already exists, byProject). Set a working target: ≥60% of weekly tokens on product repos while the activation push is on. Treat a week where the vault outspends ResumeBuilder as a drift warning, same class as a stale dashboard.

### P0-2 · Cache-read burn ≈ 50% of total cost
5,589,620,529 cache-read tokens/30d (Opus 2.18B ≈ $3.3k, Sonnet 3.41B ≈ $1.0k). Root cause, corrected after investigation: it is **not** the always-injected skill-catalog list (that's just names + one-liners, cheap). It's that each skill's *full* instructions load into context on invocation and then persist for the rest of the session, getting cache-read on every subsequent turn — a heavy skill invoked early in a long session compounds badly. gstack analytics show **8 invocations ever, 5 distinct skills used** (qa, qa-only, office-hours, plan-eng-review, investigate) out of 66 installed.
**Fix (founder-approved 2026-07-03, three levers):**
1. **Skill routing, not skill deletion:** gstack is one monolithic install ("one repo, one install, entire AI engineering workflow") — not per-skill toggleable, and deleting individual `SKILL.md` folders risks breakage on the next `gstack-upgrade`. Founder decision: keep the full 66-skill catalog installed and reachable, but make the 5 actually-used skills the *default* proactive working set; the rest are invoke-by-explicit-name only (same pattern as `/red-team` or a STORM analysis — full power on request, not on autopilot). Implemented in `~/.claude/CLAUDE.md` Skills section, 2026-07-03.
2. **Productivity connector suite:** 7 unauthenticated MCP servers (Asana, Atlassian, ClickUp, Linear, Monday, Notion, Slack) are confirmed **not** in this machine's `settings.json` `enabledPlugins` — they're enabled at the claude.ai account/connector level, outside file-edit reach. Founder action needed: disconnect unused connectors via claude.ai connector settings if they're not wanted.
3. **Session hygiene:** the routing policy's cost note already says it: shorter, scoped sessions for mechanical work. 75 vault sessions in 30d suggests long-lived catch-all sessions. After invoking a heavy skill (qa-only, plan-eng-review), prefer closing and reopening for the next unrelated task rather than carrying its full payload into hours of unrelated work.

### P0-3 · Opus routing exists on paper, not in behavior
Opus: 73% of cost from 23% of sessions (46 sessions, avg $136). The tier table (GLOBAL-TOOL-USAGE.md) reserves Opus for architecture/hard debugging, but sessions default to whatever model the window opened with.
**Fix:** make Sonnet the explicit default for Agentic OS and vault sessions (status sync, filing, planning against existing patterns). Open Opus/Fable sessions deliberately for the WP-29-class work. A one-line addition to each repo CLAUDE.md ("default session model: sonnet unless the task is P0 debugging/architecture") plus habit.

### P1-4 · The 07:00 auto-refresh has been failing silently every day
`com.nadav.agentic-os-refresh` shows launchd status **126**; the wrapper script exists and is executable, stderr log is empty — the classic macOS TCC denial (launchd bash cannot read ~/Documents). Known since June (memory: "intentionally manual for now"), but the job is still loaded and failing daily.
**Fix (founder pick one):** (a) delete the LaunchAgent and rely on the morning-brief refresh (it already refreshes first — the job is redundant), or (b) fix properly by granting Full Disk Access to a dedicated helper (not bare /bin/bash) or moving the refresh into a Claude scheduled task. Recommendation: (a) — a permanently failing daily job is noise that trains you to ignore failures.

### P1-5 · The global decision-memory file is dead but still in the ritual
`~/.claude/MEMORY.md` last real entry 2026-05-31 (33 days). Decisions now actually land in three other stores: auto-memory (24 files, current), Agentic OS DECISIONS.md, and vault decision notes. The session-start ritual still mandates reading the dead file first, every session, in every project.
**Fix:** replace ~/.claude/MEMORY.md's body with a pointer ("decisions live in auto-memory + Agentic OS DECISIONS.md") and trim the ritual step. One less stale read per session, and no more risk of an agent trusting a month-old "current" decision.

### P1-6 · Stranded-work leaks found despite the janitor existing
Found today: Resumely iOS commit `c3e6645` sat unpushed on main for 4 days (pushed during this audit); ResumeBuilder web `tasks/progress.md` 9 days older than its last commit (rule 12 violated, refresh reported "drift warnings: none" — detector miss, likely because recent commits are on the codex/wp29 branch); RunSmart main carrying untracked Garmin screenshot junk including a Finder " 2/" duplicate (the exact pattern logged in LEARNINGS 2026-06-18); **29 worktrees** accumulated in the vault repo (23 clean+merged ones removed during this audit; 6 remain, of which 2 are dirty and need a look: cool-sanderson 1 file, focused-raman 3 files).
**Fix:** extend `agentic-os clean` to include worktree cleanup (clean + merged-to-origin/main ⇒ remove, backup-first for the rest); make the drift detector compare progress.md date against last commit across ALL branches; add the RunSmart `docs/garmin-application` artifacts to .gitignore or archive them.

### P2-7 · Vault link rot: 96 phantom wikilink targets
Lint pass ran 2026-06-27 but 96 distinct phantom targets exist, several load-bearing: `[[posthog-founder-account-exclusion]]` (5 refs including the ResumeBuilder living page — the note did not exist anywhere; created during this audit), `[[deep-research]]` (9 refs), `[[Weekly Plan Creation Workflow]]` (6). Path-qualified links like `[[05-Decisions/Decision Log]]` never resolve (vault convention is title-only).
**Fix:** run a full lint-wiki pass; create stubs for the top-referenced phantoms; add the phantom-link count to the weekly review checklist so it trends down instead of accumulating.

### P2-8 · Near-duplicate skill families invite mis-invocation
Three separate "review" skills (gstack /review, built-in /review, plan-*-review family), qa vs qa-only vs verify vs ios-qa, two design-review variants. With PROACTIVE=true, the model picks one; which one it picks varies.
**Fix:** covered mostly by the P0-2 skill diet; after the diet, add explicit routing lines to CLAUDE.md skill-routing section for the survivors.

## Actions already taken during this audit (all reversible, backup-first)

1. Pushed the stranded Resumely iOS commit `c3e6645` to origin (main clean now).
2. Removed 23 clean, fully-merged vault worktrees + their branches (29 → 6); the 2 dirty ones left for founder review.
3. Created the missing `posthog-founder-account-exclusion` vault note (resolves 5 phantom refs).
4. Refreshed dashboards as a side effect of the audit (`./agentic-os refresh`, usage.json regenerated).

## Founder decisions — resolved 2026-07-03

1. **P1-4 (launchd):** DELETE — done. `com.nadav.agentic-os-refresh` unloaded and its plist removed; morning-brief refresh already covers this.
2. **P0-2 (skill/plugin diet):** APPROVED with a modification — keep gstack's full 66-skill catalog installed and reachable by explicit name (not per-skill toggleable without breakage risk); make the 5 actually-used skills the default proactive working set via `~/.claude/CLAUDE.md` routing guidance. Productivity connector suite (7 unauthenticated MCP servers) confirmed to live at the claude.ai account level, not this repo — founder to disconnect via claude.ai connector settings if desired.
3. **P1-5 (MEMORY.md):** APPROVED — done. `~/.claude/MEMORY.md` body replaced with a pointer to auto-memory + `DECISIONS.md`; historical entries kept below the pointer for reference. `CLAUDE.md` session-start ritual step 1 updated to match.
4. **Dirty vault worktrees:** LEAVE AS IS — founder call, no action taken on `cool-sanderson-0092f0` or `focused-raman-e4f264`.

## Measurement to watch

After applying P0 items, the 30d numbers to re-check (same script: `scripts/usage/collect_usage.py`): total spend, cache-read share, Opus share, product-vs-meta split. Expected effect: 30-40% total cost reduction with zero capability loss, mostly from cache-read shrinkage and Opus session discipline.

---
*Provenance note: this file was first written into the repo working tree mid-audit and was wiped by a concurrent session's cleanup before commit; rewritten identically from the session context on an isolated worktree. Filed via PR from branch `os-review-2026-07-03`.*
