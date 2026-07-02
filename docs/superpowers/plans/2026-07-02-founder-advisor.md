# Founder Advisor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `/founder <prompt>`, a single front door that classifies a raw prompt into Think or Act and hands back a copy-ready next step, recommend-only.

**Architecture:** One prose file, `Agentic OS/FOUNDER-ADVISOR.md`, is the canonical, git-versioned source. It is symlinked to `~/.claude/commands/founder.md` so `/founder <prompt>` works in every Claude Code session. There is no code and no automated test runner — this is a Claude Code custom command (a markdown file whose body becomes the model's system prompt when invoked, with `ARGUMENTS: <what the user typed>` appended by the harness, matching the existing precedent at `.claude/commands/advisor.md`). Validation is by tracing the six worked examples from the spec against the file's content by hand.

**Tech Stack:** Markdown only. macOS `ln -s` for the symlink. Git for versioning.

## Global Constraints

- Recommend-only: the file must never instruct the model to invoke an advisor, open a file, or run a workflow on the founder's behalf — only to output a verdict and a paste-ready block. (Design decision, confirmed in spec.)
- No new taxonomy: content must reuse existing names and files verbatim — `ORCHESTRATION-GATE.md` Tiers/Modes/Patterns, `DAILY.md`, `GLOBAL-WORKFLOWS.md`, and the three vault advisor files. Do not invent new categories.
- Red Team has no file yet. The command must recommend it when appropriate but explicitly state it is unbuilt and fall back to the `adversarial-review` pattern. Do not create a Red Team file as part of this plan (tracked as a separate open item in the spec).
- Canonical file lives in the Agentic OS repo (git), not `~/.claude/` directly, per the spec's resolution of the availability-vs-durability tension.
- Commit to `main` in the Agentic OS repo directly (repo convention: no worktrees/branches for OS work — see `AGENTS.md` "Single Source Of Truth"). Push before ending the session.

---

### Task 1: Write the canonical Founder Advisor command file

**Files:**
- Create: `Agentic OS/FOUNDER-ADVISOR.md`

**Interfaces:**
- Consumes: nothing (this is the top-level entry file).
- Produces: the file's exact content is consumed verbatim by Task 3 (the symlink) and by Task 2 (manual validation trace). No other task depends on internal structure beyond the two verdict shapes (`VERDICT: Think — ...` / `VERDICT: Act — ...`) defined below.

- [ ] **Step 1: Write the file**

Create `Agentic OS/FOUNDER-ADVISOR.md` with exactly this content:

```markdown
# Founder Advisor

You are the founder's single front door for a raw prompt. Read the prompt
given to you as ARGUMENTS below and produce exactly ONE of two verdicts:
**Think** or **Act** (or both, only in the low-confidence case described
below). You never act on the prompt yourself — you only classify and hand
back a copy-ready next step. The founder takes the next action, not you.

## How To Classify

Route to **Think** when the prompt is:
- A question seeking a view ("should I…", "is it worth…", "what do I
  think…", "which is better…")
- A fuzzy or large idea with no clear first action
- A decision between named options
- A request for critique, challenge, or a strategic point of view
- Something that has come up before without a decision being made (a
  rumination signal)

Route to **Act** when the prompt:
- Names or implies concrete work to do
- Asks "what should I do / progress next"
- References a specific product, repo, feature, bug, work packet, plan,
  decision, or workflow
- Does not clearly match the Think signals above — **Act is the default
  when unclear**, because the Act path's own gate
  (`ORCHESTRATION-GATE.md`) has a safe default (Tier 1 · Builder ·
  normal).

If both sets of signals are present, pick **Think** (thinking precedes
doing) and name Act as the likely next step in one line at the end of your
output.

If your confidence in either verdict is genuinely low, say so explicitly
and produce both the Think block and the Act block, so the founder can
pick.

## Think Path

Pick exactly one advisor:

- **Storm** — the prompt needs breadth, multiple perspectives, or research
  synthesis. Source: vault `04-Prompts/Claude/storm-project-system-prompt.md`
  and `04-Prompts/Claude/storm-multi-perspective-research.md`.
- **High-Agency Advisor** — the prompt needs a bias-to-action or
  anti-rumination challenge ("is this Level 0 or Level 1?"). Source: the
  vault's `/advisor` command (project-scoped to the Nadav Builder OS vault
  repo) and vault `04-Prompts/Claude/high-agency-advisor.md`.
- **Red Team** — the prompt needs adversarial challenge ("poke holes in
  this," "what could go wrong," "is this safe to ship"). **This advisor is
  not built yet — no file exists anywhere, vault or Agentic OS.** Recommend
  it anyway when it is the right fit, say plainly that it is unbuilt, and
  fall back to the `adversarial-review` pattern in `GLOBAL-WORKFLOWS.md`
  (owner: Risk OS / QA / Taste, depending on context).

Output exactly this shape:

```
VERDICT: Think — <one sentence: why this is a thinking prompt, not an action>
Advisor: <Storm | High-Agency Advisor | Red Team (unbuilt — falls back to adversarial-review)>

<the paste-ready prompt for that advisor, with the founder's actual
question already filled in — reworded into that advisor's format, not a
placeholder>
```

## Act Path

Follow this procedure in order:

1. Classify the prompt against `ORCHESTRATION-GATE.md` and produce its
   Tier, Mode, and Workflow pattern.
2. Read only the state relevant to that classification — do not read every
   file every time:
   - `executive-os/EXECUTIVE-DECISIONS.md` — is there an open decision
     this prompt touches or would move forward?
   - The saved plans board / active plans — is there a plan whose next
     milestone this prompt advances?
   - `executive-os/work-packets/` — is there a matching or logically-next
     work packet?
   - `GLOBAL-WORKFLOWS.md` — which workflow or pattern applies?
   - `DAILY.md` — confirm the Tier.
3. State what to run, and what in-flight work (if any) this progresses.
4. Produce the paste-ready block: the exact repo path plus the exact
   command, or the full text of the work packet to paste.

Output exactly this shape:

```
VERDICT: Act — <one sentence: why this is actionable, not a thinking prompt>
GATE: Tier <n> · Mode <name> · Pattern <name> · Route <file>
Progress: <the open decision / plan milestone / work packet this advances, or "none in flight — new work">

<the paste-ready block: exact repo path, then the exact command or full
work-packet text to paste into that repo's session>
```

If a state file cannot be read (wrong repo open, file missing, no access),
do not guess its contents. State plainly which file could not be read,
still give the Tier/Mode/Pattern classification, and give a generic route
instead of a specific decision/plan/WP.

## Rules

- Recommend only. Never invoke an advisor, open a file, or run a
  workflow — the founder does that after reading your output.
- Never fabricate the status of a decision, plan, or work packet. If you
  have not read the file, say so.
- One verdict, unless confidence is genuinely low — then show both, each
  with its own complete block.
- This file is the front door to `ORCHESTRATION-GATE.md`, `DAILY.md`,
  `GLOBAL-WORKFLOWS.md`, and the vault advisors. It does not replace any
  of them and does not duplicate their tables — it only decides which one
  the prompt needs.

```

Do not add an `ARGUMENTS:` line at the end of the file. The precedent file
`.claude/commands/advisor.md` has no such line, and the harness appends
`ARGUMENTS: <what the founder typed>` automatically after this file's
content when `/founder <prompt>` is invoked — the file only needs to say,
in its own opening line, that it should read the prompt given to it.

- [ ] **Step 2: Verify the file was written correctly**

Run: `cat "Agentic OS/FOUNDER-ADVISOR.md" | head -5`
Expected output starts with:
```
# Founder Advisor

You are the founder's single front door for a raw prompt. Read the prompt
```

- [ ] **Step 3: Commit**

```bash
cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
git add FOUNDER-ADVISOR.md
git commit -m "feat: add Founder Advisor front-door command

Think/Act classifier per docs/superpowers/specs/2026-07-02-founder-advisor-design.md.
Recommend-only; routes to vault advisors or ORCHESTRATION-GATE.md + live OS state."
```

---

### Task 2: Validate the file against the six worked examples

**Files:**
- Read only: `Agentic OS/FOUNDER-ADVISOR.md` (from Task 1)
- Read only: `docs/superpowers/specs/2026-07-02-founder-advisor-design.md` (source of the six examples)

**Interfaces:**
- Consumes: the exact file content from Task 1, Step 1.
- Produces: nothing new is written to disk. This task either confirms Task 1's content is correct, or sends you back to Task 1 to edit it. This is the "test" for a prose file — there is no automated runner.

There is no code to execute here. Instead, for each of the six examples
below, read `FOUNDER-ADVISOR.md`'s classification rules and manually
determine what verdict a model following those rules would produce.
Compare against the expected result. If any example would misclassify,
edit the "How To Classify" bullets in `FOUNDER-ADVISOR.md` (Task 1, Step 1)
until all six pass, then re-run this task.

- [ ] **Step 1: Trace example 1**

Prompt: "Should I keep building the Garmin reconnect flow or park it?"
Expected: `VERDICT: Think` (matches "a decision between named options") →
Advisor: High-Agency Advisor (matches "bias-to-action / anti-rumination
challenge" — this is exactly the kind of stuck decision the High-Agency
Advisor exists for).
Confirm: does the "Route to Think" bullet list contain a bullet this
prompt clearly matches? (Yes — "A decision between named options.")

- [ ] **Step 2: Trace example 2**

Prompt: "Give me five angles on the Resumely pricing page."
Expected: `VERDICT: Think` → Advisor: Storm (matches "needs breadth,
multiple perspectives").
Confirm: does "Route to Think" clearly cover this, and does "Storm" clearly
cover "five angles"? (Yes — Storm's line says "breadth, multiple
perspectives, or research synthesis.")

- [ ] **Step 3: Trace example 3**

Prompt: "Fix the voice-cue endpoint dirty tree in RunSmart web."
Expected: `VERDICT: Act` → `GATE: Tier 1 · Mode Builder · Pattern normal`
→ Route: RunSmart web repo.
Confirm: does "Route to Act" clearly cover this ("References a specific
product, repo, feature, bug")? (Yes.) Confirm the Act path's step 1
correctly hands this off to `ORCHESTRATION-GATE.md` for the Tier/Mode/
Pattern rather than the Founder Advisor file guessing them itself. (Yes —
step 1 says "Classify the prompt against ORCHESTRATION-GATE.md.")

- [ ] **Step 4: Trace example 4**

Prompt: "What should I progress this week?"
Expected: `VERDICT: Act` → reads `EXECUTIVE-DECISIONS.md`, plans board,
`work-packets/` → recommends the next milestone.
Confirm: does the Act path's step 2 list cover reading exactly these
three sources plus `GLOBAL-WORKFLOWS.md` and `DAILY.md`? (Yes.) Confirm
step 3 ("state what to run, and what in-flight work this progresses")
matches "Progress:" line in the output shape. (Yes.)

- [ ] **Step 5: Trace example 5**

Prompt: "Poke holes in my plan to file two Garmin portal apps."
Expected: `VERDICT: Think` → Advisor: Red Team (unbuilt, falls back to
adversarial-review).
Confirm: does "Route to Think" cover "request for critique, challenge"?
(Yes.) Confirm the Red Team bullet explicitly states it is unbuilt and
names the adversarial-review fallback. (Yes, verify the exact sentence is
present in Task 1's file.)

- [ ] **Step 6: Trace example 6**

Prompt: a vague one-liner with no clear signal, e.g. "look into this."
Expected: `VERDICT: Act` (default) → `GATE: Tier 1 · Mode Builder ·
Pattern normal`, low confidence noted.
Confirm: does the classify section's last Act bullet explicitly say "Act
is the default when unclear"? (Yes.) Confirm the "Rules" section's
low-confidence handling would surface here (the model should note low
confidence per the top-level instruction "If your confidence in either
verdict is genuinely low, say so explicitly and produce both").

- [ ] **Step 7: Record the result**

If all six traces confirm the expected verdict, no file changes are
needed — proceed to Task 3. If any trace fails, edit
`Agentic OS/FOUNDER-ADVISOR.md`'s classification bullets now, re-run
Steps 1-6 for the failing example only, and commit the fix:

```bash
cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
git add FOUNDER-ADVISOR.md
git commit -m "fix: correct Founder Advisor classification for example <N>"
```

---

### Task 3: Wire up the global `/founder` command

**Files:**
- Create (symlink): `~/.claude/commands/founder.md` → `Agentic OS/FOUNDER-ADVISOR.md`

**Interfaces:**
- Consumes: the committed file from Task 1 (must exist on disk at its
  absolute path before the symlink is created).
- Produces: a working `/founder <prompt>` command in every Claude Code
  session. No later task depends on this beyond the acceptance check below.

- [ ] **Step 1: Create the commands directory if it does not exist**

Run: `mkdir -p ~/.claude/commands`
Expected: no output, exits 0.

- [ ] **Step 2: Create the symlink**

Run:
```bash
ln -sf "/Users/nadavyigal/Documents/Projects /Agentic OS/FOUNDER-ADVISOR.md" ~/.claude/commands/founder.md
```
Expected: no output, exits 0.

- [ ] **Step 3: Verify the symlink resolves correctly**

Run: `ls -la ~/.claude/commands/founder.md && diff ~/.claude/commands/founder.md "/Users/nadavyigal/Documents/Projects /Agentic OS/FOUNDER-ADVISOR.md"`
Expected: `ls` shows it as a symlink (`l` permission bit, `->` pointing at
the Agentic OS path); `diff` produces no output (files are identical
because it's a symlink, not a copy).

- [ ] **Step 4: Verify content is not committed twice**

Run: `cd "/Users/nadavyigal/Documents/Projects /Agentic OS" && git status --short`
Expected: `FOUNDER-ADVISOR.md` does not appear (already committed in Task
1); no new files listed related to this task, since `~/.claude/commands/`
is outside this repo and outside any repo that needs to track it.

No commit in this task — the symlink is local machine state, not
repo-tracked content. If this founder's other machines need the same
command, this step must be repeated there (documented as a limitation, not
solved by this plan — out of scope per the spec).

---

### Task 4: Push and confirm end-to-end

**Files:** none created or modified; verification only.

**Interfaces:** none — this task only confirms Tasks 1-3 are complete and
pushed.

- [ ] **Step 1: Push the Agentic OS commits**

```bash
cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
git push origin main
```
Expected: push succeeds, shows the new commit hash(es) from Task 1 (and
Task 2 if a fix commit was needed) landing on `origin/main`.

- [ ] **Step 2: Confirm clean state for this plan's files specifically**

Run: `cd "/Users/nadavyigal/Documents/Projects /Agentic OS" && git log --oneline -3 -- FOUNDER-ADVISOR.md`
Expected: shows at least one commit touching `FOUNDER-ADVISOR.md` (from
Task 1, and Task 2 if applicable), confirming it is committed and pushed
(check with `git status --short --branch` that `main` is not ahead of
`origin/main`).

- [ ] **Step 3: Manual end-to-end smoke check**

Open a new Claude Code session in any repo and type:
`/founder Should I keep building the Garmin reconnect flow or park it?`
Expected: the command loads (no "command not found" error), and the
response contains `VERDICT: Think` and `Advisor: High-Agency Advisor`,
matching Task 2's traced example 1. This is the final acceptance check for
the whole plan — if this does not produce the expected verdict shape, the
plan is not complete regardless of what Tasks 1-3 report.
