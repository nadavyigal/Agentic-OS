# morning-brief

## When to Use

**Daily default:** run `./agentic-os morning` and read the Command Center (`DAILY.md` Tier 0). That is the morning brief for normal work days.

The long reading protocol is only for:

- Command Center unavailable.
- Localhost unavailable.
- Founder explicitly asks for a deep cross-project narrative.
- Weekly CEO review preparation.

Do not use the long protocol for normal daily work.

## How to Invoke

1. **Daily:** `./agentic-os morning` from the Agentic OS repo (see `DAILY.md`).
2. **Deep brief:** Use the reading protocol below only when one of the fallback conditions above is true.

---

## Reading Protocol

Fallback only: read all of the following in parallel before generating output. If a file does not exist, note it and skip, do not error.

For every project below, also collect live git state (run with `git -C "<path>"`):
- `status --short --branch` (current branch + uncommitted work)
- `log --oneline @{u}.. 2>/dev/null` (unpushed commits; ignore errors if no upstream)

And check the modification date of every task file read (`stat -f '%Sm' -t '%Y-%m-%d'`). A task file older than the latest commit is background context only, cited with its date, never current status.

### RunSmart Web
Path: `/Users/nadavyigal/Documents/RunSmart`
- `git log --oneline --since="96 hours ago"` (run from this path)
- `tasks/MEMORY.md` (last 2 entries)
- `tasks/todo.md`
- `docs/agent-os/project-context.md`
- Most recent 2 files from `docs/plans/` (list by filename/date, read latest 2)

### RunSmart iOS
Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
- `git log --oneline --since="96 hours ago"` (run from this path)
- `tasks/MEMORY.md` (last 2 entries)
- `tasks/todo.md`
- `tasks/session-log.md` (last 2 entries)
- Most recent 2 files from `docs/superpowers/plans/` (list by filename/date, read latest 2)
- Latest `docs/product-strategy-*.md` file

### ResumeBuilder AI
Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- `git log --oneline --since="96 hours ago"` (run from this path)
- `tasks/MEMORY.md` (last 2 entries)
- `docs/agent-os/project-context.md`
- All `docs/plan.*.md` files (they are small; read all)
- `docs/gtm/canonical-90-day-plan.md`

### ResumeBuilder iOS
Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- `git log --oneline --since="96 hours ago"` (run from this path)
- `tasks/MEMORY.md` (last 2 entries)
- `tasks/todo.md`
- `tasks/progress.md`
- `tasks/session-log.md` (last 2 entries)
- `docs/specs/README.md` (active specs index)
- `docs/product/product-vision.md`
- `docs/product/current-product-state.md`

### Agentic OS (cross-project context)
Path: `/Users/nadavyigal/Documents/Projects /Agentic OS`
- `DASHBOARD.md`
- `dashboard/status.json`
- `BACKLOG.md` (Now + Next sections only)

---

## Output Format

Produce the following 6 sections in order. Synthesize — do not paste file contents verbatim. Direct, specific, no filler. Total should be readable in under 3 minutes.

---

### Morning Brief — [TODAY'S DATE]

One-line overall status across projects. Which need immediate attention, which are in-flight, and which are idle.

---

### Product Snapshot

For each project — the "why we're building this" context, refreshed from strategy/vision files:
- **Goal:** [one-sentence product vision or current phase goal]
- **Current epic/theme:** [what feature or milestone is the focus right now]
- **Roadmap position:** [how far into the plan — early / mid / close to shipping]
- **What's not started yet:** [planned work that hasn't been touched]

Keep each project to 4 bullet points. If a product-strategy or vision file doesn't exist, infer from project-context.md.

---

### What You Left Off

For each project with activity in the last 96 hours:
- **Last commit:** [timestamp + message]
- **Mid-flight:** [what was in progress per memory + session-log + todo]
- **Session closed properly:** yes / no (if no: describe what was likely still open)

For projects with no recent activity: "[Project]: No recent activity."

---

### Active Plans & Open Stories

For each project — what plans exist and where they stand:
- **Active plan:** [filename + one-line goal]
- **Open stories:** [list of unchecked [ ] stories from the plan]
- **Completed stories:** [count of done stories, not full list]
- **Plan age:** [date of plan file — flag if older than 30 days with no recent commits]
- **Next story to implement:** [the specific next unchecked item]

If no plan files exist for a project, note it and use todo.md instead.

---

### Stranded Work

From `dashboard/status.json` `strandedWork.items` (rebuilt every refresh from git). These are commits, branches, and worktrees at risk of being lost between Claude Code, Codex, and Cursor sessions. Lead with default-branch issues and unpushed commits, then local-only branches, then worktrees. Summarize cleanup-only items (merged branches safe to delete) in one line. If empty, say "Nothing stranded."

---

### Blockers & Decisions Needed

Only include real blockers and pending decisions (not hypothetical risks).

Format:
- [Project] — **Blocked:** [what it is + what unblocks it]
- [Project] — **Decision needed:** [the choice + what info exists to make it]

If nothing is blocked: state that clearly.

---

### Today's Recommendation

For each project, top 2-3 specific next actions (name the file, story, or command — not vague):
1. [Specific action]
2. [Specific action]
3. [Optional third if clearly next]

**Strategic recommendation:** Based on the product snapshot and what's in flight, where should time go today and why? One paragraph, specific. Example: "RunSmart iOS is closest to shipping (sprint 10 closeout is one archive away). ResumeBuilder iOS plans are complete but need smoke QA before the PR unblocks the backend work. Recommend: finish RunSmart iOS archive this morning, then switch to ResumeBuilder iOS smoke test."

---

## One process

There is one process for the morning brief: run `./agentic-os morning`. It refreshes evidence from every repo, surfaces every saved plan (including GTM), rebuilds the headline + priority board from parsed `tasks/progress.md` truth, updates the dashboard HTML, verifies, and serves localhost. Do NOT hand-write a separate narrative into `dashboard/status.json` — the script re-derives it every run, so any hand-edit is overwritten by design. If asked for a morning brief, run `./agentic-os morning` and read the result back from the dashboard; never write status from memory.

The text-only reading protocol below is for when you need a spoken brief without the dashboard (e.g. no localhost). It uses the same source files the script parses.

## Brief Rules

- Evidence priority, highest first: live git > session-log/todo/progress (date-checked) > refreshed dashboard files > tasks/MEMORY.md (background only).
- Drift rule: dashboard prose fields (`status`, `activeStory` in status.json) can carry stale narrative across refreshes. If dashboard text contradicts live git evidence (e.g. names an older build or version than the commits show), trust git and report the contradiction in a "Drift detected" section.
- End the brief with a "Data freshness" line per project: newest evidence source + its date.
- Never paste file contents verbatim. Synthesize.
- If a file doesn't exist: say so in one word and skip.
- If git shows no commits in 96 hours: "No recent commits."
- If `status.json` or `DASHBOARD.md` is older than 7 days: flag as stale.
- Be specific: reference plan filenames, story names, or commit messages when citing evidence.
- Direct tone — one sentence per point. No warmup phrases.
- If a project has zero activity and zero plans, summarize it in one line.
- Product Snapshot should reflect the latest product-strategy or vision file, not stale project-context if a newer file exists.
