# Prompt: Daily Agentic OS Routine (Full Cycle)

Copy everything inside the fenced block below into Cursor (Agentic OS repo root as working directory).

Trigger phrases:
- "run the daily Agentic OS routine"
- "daily agentic os routine"
- "full morning cycle"

---

```txt
You are running the daily Agentic OS routine in Cursor. Execute in this exact sequence. Do not skip the refresh step — every later stage depends on fresh data. Do not perform any destructive git action (deleting a branch, removing a worktree, discarding uncommitted changes) without explicitly listing it and getting a yes first — this includes within STEP 0.5 and STEP 6 below.

Working directory: `/Users/nadavyigal/Documents/Projects /Agentic OS`

Repo paths (from PROJECT-PATHS.md):
- RunSmart iOS: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
- Resumely iOS: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- RunSmart Web: `/Users/nadavyigal/Documents/RunSmart`
- ResumeBuilder AI (Web): `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- Agentic OS: `/Users/nadavyigal/Documents/Projects /Agentic OS`

---

## STEP 0 — Refresh ground truth (mandatory first step)

Run `./agentic-os refresh` from the Agentic OS root.

Do NOT read PROJECT-STATUS.md or dashboard/status.json until this completes.

If refresh fails, stop and report the error before doing anything else.

### Baseline context (confirm against refreshed output; flag if changed)

Trust the live refresh output over this snapshot if they disagree:

- **RunSmart iOS:** v1.0.3 build 16 is LIVE on the App Store (go-live **2026-06-19**, founder-confirmed). Active work is Garmin readiness / production enablement — NOT a resubmission. PostHog early volume (~16 users/7d) is expected for early post-launch — not a traction signal.
- **Resumely iOS:** v1.1 build 5 is LIVE on the App Store (founder-confirmed **2026-06-21**). D7 readout ~7 days after go-live (~2026-06-28).
- **RunSmart Web — Garmin production enablement:** worker-RPC grant lockdown migration (`20260621000000_restrict_garmin_worker_rpc_grants.sql`) written; awaiting founder approval to apply (`supabase login` + `db push` or SQL Editor). Webhook async-200 + deregistration handling verified in code. Gate 1 (privacy policy) live in code; Gates 2–4 are manual Garmin-portal/email tasks. Garmin Production approval is external (~2–4 weeks after submission).
- **ResumeBuilder AI (Web) — ATS scoring:** LinkedIn guest-scrape fix merged via **PR #77** (2026-06-20). JD heading classifier in **PR #81** may be open. Do not treat LinkedIn fix as fully verified until datacenter preview check passes OR production re-optimize confirms score lift. Story 2 (metrics_presence) closed as not-a-bug per progress.md.

---

## STEP 0.5 — Resolve RunSmart iOS status contradiction (if flagged)

Only run this step if refresh reports a contradiction for RunSmart iOS.

Known false-positive pattern (verify before editing): `declared_prelaunch()` in `scripts/agentic_os/cli.py` matches the substring `"resubmission"` inside phrases like **"not a resubmission"** or **"not another App Store submission"**. If the declared status already says LIVE with a dated go-live, fix the phase wording — do not overwrite with generic "LIVE" that loses Garmin context.

If a real contradiction remains:

1. Confirm the App Store go-live date for v1.0.3 build 16 (App Store Connect timeline, git/session evidence, or ask founder). Expected: **2026-06-19**.
2. Update `tasks/progress.md` in RunSmart iOS:
   - Status line must include explicit go-live date — never undated "live".
   - Note PostHog as **"early post-launch, low volume (~N users/7d)"** — do not imply broad traction.
   - Current Phase must NOT contain prelaunch trigger tokens (`resubmission`, `in review`, etc.) unless actually prelaunch.
3. Re-run `./agentic-os verify` after the edit.
4. Re-run `./agentic-os refresh` and confirm `PROJECT-STATUS.md` → `## Contradictions vs Ground Truth` → **None**.
5. If contradiction persists, report exactly what's still mismatched (declared state vs PostHog vs App Store env) — do not force a cosmetic fix.

---

## STEP 1 — Morning brief

Run `./agentic-os morning` (runs refresh + verify + serve). If verify fails on html/json sync, re-run `./agentic-os verify` once after refresh settles.

Then read from refreshed output (not memory):
- `PROJECT-STATUS.md` (Status Table, Action Board, Contradictions)
- `DASHBOARD.md` (Executive Summary, Project Health, Stranded Work summary)
- `dashboard/status.json` (`portfolioTrust`, `planExecution`, `executiveLoop`, `contradictions`)

Surface in output:
1. **What shipped** since last routine (with dates/evidence)
2. **What's in flight** per project
3. **Drift vs baseline** (Garmin migration state, ATS/LinkedIn verification state, any stale pre-launch distribution copy)
4. **Recommended next focus** (single primary bottleneck)

Fallback if `./agentic-os morning` fails: use `PROMPTS/morning-brief.md` reading protocol against the post-refresh files above.

---

## STEP 2 — Weekly review (only if due)

Check `distribution-os/weekly-growth-review.md` for the newest entry date.

- If **no entry exists for the current calendar week** (week starting Monday): run both:
  - `executive-os/workflows/weekly-ceo-review.md`
  - `distribution-os/prompts/weekly-distribution-run.md` + `distribution-os/workflows/00-weekly-distribution-cycle.md`
  - Append a new entry to `distribution-os/weekly-growth-review.md` (newest first)
  - Use **post-launch growth** framing — both iOS apps are live; no pre-launch positioning
- If an entry already exists this week: **skip** and state the date of the last entry and why skipped.

Note: `07-Weekly-Reviews/` vault folder may not exist locally — `weekly-growth-review.md` is the source of truth.

---

## STEP 3 — COO operating review

Run `executive-os/workflows/coo-operating-review.md` using `PROMPTS/coo-operating-review.md`.

Pull state from STEP 0/0.5 refreshed data only — not from memory.

Read:
- `DASHBOARD.md`, `PROJECT-STATUS.md`
- `dashboard/status.json` (`planExecution`, `executiveLoop`, `osRegistry.outcomeLoops`)
- `executive-os/COO-OS.md`
- Each product repo's `tasks/progress.md`

**Update** `executive-os/COO-LATEST-REVIEW.md` with today's date and full output:
1. Operating summary
2. Loop needing attention (or none)
3. Plans needing packets (`needs_next_packet` rows)
4. Current bottleneck + unblock owner
5. Execution sequence (first/second/third, tagged)
6. CEO / CFO / Analysis / Risk escalation (Yes/No + exact question if Yes)
7. One work packet (or reason for none)
8. What not to touch

---

## STEP 4 — Executive overview

Run `PROMPTS/executive-weekly-review.md` against:
- `executive-os/EXECUTIVE-DASHBOARD.md`
- `executive-os/EXECUTIVE-METRICS.md`
- `executive-os/EXECUTIVE-DECISIONS.md`

Reconcile against COO review from STEP 3:
- If COO and executive views disagree on bottleneck or priority, **flag the disagreement explicitly** — do not silently pick one.
- Update `executive-os/EXECUTIVE-DASHBOARD.md` (Top 3, Decision Board, Risk Board, Weekly Review, Next Actions) to match refreshed portfolio state.
- Append new decisions to `EXECUTIVE-DECISIONS.md` only if a genuinely new decision emerged.
- Do not invent metrics — use `unknown — need: <source>`.

---

## STEP 5 — Distribution

Run `distribution-os/prompts/daily-distribution-check.md`.

Read:
- `distribution-os/distribution-command-center.md`
- `distribution-os/experiment-log.md` (active rows only)

Produce (<200 words):
1. Running experiments — status, any meaningful movement
2. Stuck / waiting on founder
3. Kill candidates (if any)
4. One thing to ship or approve today

**Post-launch rules:**
- Both iOS apps are live — no "awaiting App Store approval" or pre-launch CTAs
- rb-dir-001 (directories) is unblocked if App Store URL exists
- rs-aso-001/002 are post-launch ASO iteration, not pre-submission

If weekly cadence (STEP 2 ran): also note top experiments from the weekly distribution run.

Flag if `distribution-command-center.md` still shows pre-launch week/theme — recommend update.

---

## STEP 6 — Stranded Work cleanup (proposals only until yes)

Pull the Stranded Work list from the **just-refreshed** `PROJECT-STATUS.md` — not from memory.

For **every** entry, verify live git state before proposing action:

```bash
# Per repo — adapt paths
git -C "<repo>" status -sb
git -C "<repo>" branch --merged main
git -C "<repo>" log --merges --oneline -15
git -C "<repo>" log main..<branch> --oneline   # unmerged commits?
git -C "<repo>" worktree list
git -C "<repo>" diff --stat                     # uncommitted summary
```

### Known stale patterns (always re-verify)

- `fix/garmin-ios-branch-fixes` on RunSmart Web — likely **already merged PR #93** (`ed397de`); do not open redundant PR
- `claude/dedup-imported-skill-packs` — likely **superseded by PR #95**; delete, don't PR
- `fix/linkedin-guest-scrape` on ResumeBuilder Web — likely **merged PR #77**; delete local branch after verification
- Empty worktrees at commit `0000000` with 0 commits vs main — safe to remove after confirm
- Resumely iOS: **pull main first** if behind origin before any other work

### Action rules (wait for explicit yes before executing)

For each remaining item, propose ONE of:
- **Push + open PR** — branch has real unmerged commits not on main
- **Delete local branch** — merged or superseded (state which PR proves it)
- **Remove worktree** — branch landed or worktree empty (confirm first)
- **Commit** — show `git diff --stat` summary; intentional uncommitted work
- **Discard** — show diff summary; accidental/duplicate files only
- **Leave pending** — needs founder input

Never run `git checkout .`, `git clean -f`, `git worktree remove`, or `git branch -D` without explicit yes per item or batch.

Never push to `main` without explicit yes.

---

## OUTPUT — Consolidated summary (required)

End with a single consolidated summary containing:

### What ran
- List each step (0, 0.5, 1–6) with outcome and proof (command output snippet or file section)

### What was skipped and why
- e.g. STEP 2 skipped because weekly entry exists for 2026-06-21

### Contradiction resolution (STEP 0.5)
- Cleared / still open / false-positive — with verify output quote

### Stranded work table
| Repo | Item | Verification | Proposed action | Resolution |
|------|------|--------------|-----------------|------------|
(one row per item — pushed+PR'd / deleted / committed / left pending your approval)

### Top 1–3 actions for today
- Ordered by COO bottleneck logic

### Proof rule
Do not declare anything "done" without citing command output or refreshed file evidence.

---

## Safety constraints (entire run)

- No App Store submissions, billing changes, production deploys, emails, or external sends unless founder explicitly asks mid-run
- No Supabase `db push` or production DB mutations unless founder explicitly approves mid-run
- No git destructive operations without explicit yes
- No inventing metrics or status — cite `tasks/progress.md`, git, or refresh output
- Commit Agentic OS routine outputs (COO review, dashboard updates, weekly entry) when files were edited — only if founder asks to commit
```

---

## Notes for the operator

- **Daily default** remains `./agentic-os morning` + Command Center (`DAILY.md` Tier 0). Use this full prompt for the complete weekly-aligned cycle or after time away.
- **After this routine:** run `./agentic-os refresh` once more if you edited any product `tasks/progress.md` files, so dashboard sync stays clean.
- **Garmin migration manual path:** `RunSmart/v0` → `supabase login` → `supabase link --project-ref biilxiuhufkextvwqdob` → `npx supabase db push`, or paste SQL from `v0/supabase/migrations/20260621000000_restrict_garmin_worker_rpc_grants.sql` into Supabase SQL Editor.
