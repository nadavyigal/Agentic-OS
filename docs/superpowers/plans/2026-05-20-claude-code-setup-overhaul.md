# Claude Code Setup Overhaul — Implementation Plan

> **Status: verified already implemented, 2026-07-01.** All boxes below were retroactively checked after confirming every file in the File Map exists and is in active use (not re-executed). Verification evidence:
> - `~/.claude/MEMORY.md`, `ERRORS.md`, `LEARNINGS.md` — exist, populated (9.6KB / 4.1KB / 6.7KB).
> - `~/.claude/agents/investigator.md`, `code-reviewer.md` — exist.
> - `~/.claude/hooks/bash-firewall.sh` — exists, executable, tested live: blocks `rm -rf`, allows `ls -la`.
> - `~/.claude/settings.json` — valid JSON, `PreToolUse` has 2 hooks (`bash-firewall.sh` + a later addition, `git-guard.sh`), `Stop` has 1 hook.
> - `~/.claude/CLAUDE.md` — has Session Start Ritual, Never Do, Permanent Facts, and Session End sections matching this plan's Task 5 content near-verbatim.
> - RunSmart and ResumeBuilder `tasks/MEMORY.md` + `tasks/ERRORS.md` — exist, populated, alongside `tasks/lessons.md`.
>
> **One deviation from spec, not a gap:** Task 4's Stop hook was originally designed as two `type: prompt` hooks (one nudging an ERRORS.md entry, one nudging a MEMORY.md summary). The system that actually shipped uses one `type: command` hook (`update-progress.sh`) that stamps `tasks/progress.md` and emits a `systemMessage` reminder, plus a separate, much broader auto-memory system (`memory/*.md` + `MEMORY.md` index, described in the session harness's system prompt) superseding the flat `~/.claude/MEMORY.md` decision-log design. The intent — never lose session context — is served by a more capable mechanism than this plan specified. Not a regression; no action needed.

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a structurally enforced memory, learning, and workflow system so Claude never loses context between sessions, never re-proposes already-failed approaches, and follows a consistent prompt → plan → implement → test → QA workflow.

**Architecture:** Three layers — global memory files (`~/.claude/`) that persist across all projects, per-project memory files (`tasks/`) that capture project-specific history, and hooks in `settings.json` that enforce the system at the tool level rather than relying on instructions Claude could ignore.

**Tech Stack:** Bash (hook script), JSON (settings.json), Markdown (all memory/agent files), Claude Code CLI

---

## File Map

### Created (new files)
- `~/.claude/MEMORY.md` — global decision log
- `~/.claude/ERRORS.md` — global failed approaches log
- `~/.claude/LEARNINGS.md` — global positive patterns log
- `~/.claude/agents/investigator.md` — debug specialist subagent
- `~/.claude/agents/code-reviewer.md` — read-only review subagent
- `~/.claude/hooks/bash-firewall.sh` — PreToolUse safety hook
- `/Users/nadavyigal/Documents/RunSmart/tasks/MEMORY.md` — RunSmart decisions
- `/Users/nadavyigal/Documents/RunSmart/tasks/ERRORS.md` — RunSmart failed approaches
- `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/MEMORY.md`
- `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/ERRORS.md`

### Modified (existing files)
- `~/.claude/settings.json` — add hooks block
- `~/.claude/CLAUDE.md` — add 4 new blocks (Session Start upgrade, Never Do, Permanent Facts, Session End)

---

## Task 1: Create Global Memory Files

**Files:**
- Create: `~/.claude/MEMORY.md`
- Create: `~/.claude/ERRORS.md`
- Create: `~/.claude/LEARNINGS.md`

- [x] **Step 1: Create `~/.claude/MEMORY.md`**

```markdown
# Global Memory — Decision Log

Cross-project architectural and product decisions. Read this at the start of every session.
Never contradict a logged decision without flagging it first.

## Format
## YYYY-MM-DD — [Decision title]
**Decided:** [What was chosen]
**Why:** [The reasoning]
**Rejected:** [Alternatives considered and why ruled out]

---

## 2026-05-20 — Claude Code Setup Overhaul
**Decided:** Implement memory + hooks + subagents system per design spec
**Why:** Losing context between sessions and re-proposing failed approaches was costing hours per week
**Rejected:** Minimal patch (MEMORY.md only) — hooks are mandatory enforcement, not optional
```

- [x] **Step 2: Create `~/.claude/ERRORS.md`**

```markdown
# Global Errors — Failed Approaches Log

Approaches that were tried and failed across any project. Read this before proposing any fix.
Never propose an approach already logged here as failed.

## Format
## YYYY-MM-DD — [Task or issue description]
**Project:** [RunSmart / ResumeBuilder / Global]
**Tried:** [What was attempted and why it failed]
**Worked:** [The approach that finally succeeded — fill in when resolved]
**Next time:** [Key insight to carry forward]

---
```

- [x] **Step 3: Create `~/.claude/LEARNINGS.md`**

```markdown
# Global Learnings — Patterns That Work

Approaches, patterns, and shortcuts that have worked especially well. Read this at session start.
Prefer these patterns when similar situations arise.

## Format
## YYYY-MM-DD — [Pattern title]
**Pattern:** [What worked well]
**Context:** [When to apply it — what kind of task, what project]
**Evidence:** [Why we know it works]

---
```

- [x] **Step 4: Verify all three files exist**

```bash
ls -la ~/.claude/MEMORY.md ~/.claude/ERRORS.md ~/.claude/LEARNINGS.md
```

Expected output: all three files listed with size > 0.

---

## Task 2: Create Subagent Definitions

**Files:**
- Create: `~/.claude/agents/investigator.md`
- Create: `~/.claude/agents/code-reviewer.md`

- [x] **Step 1: Ensure agents directory exists**

```bash
mkdir -p ~/.claude/agents
ls ~/.claude/agents/
```

- [x] **Step 2: Create `~/.claude/agents/investigator.md`**

```markdown
---
name: investigator
description: Systematic debugger. Finds root causes before writing any code. Always checks ERRORS.md first.
model: claude-sonnet-4-6
tools: Read, Grep, Glob, Bash
---

You are a systematic debugger. Your only job is to find root causes — never to guess, never to patch symptoms.

## Before starting any investigation

1. Read `tasks/ERRORS.md` in the current project directory
2. Read `~/.claude/ERRORS.md`
3. State out loud: "I checked ERRORS.md. Here is what has already been tried: [list]"
4. If this exact failure pattern already has a "Worked" entry in ERRORS.md — implement that solution directly. Do not re-investigate.

## Investigation rules

- State your root cause hypothesis explicitly before writing any code
- Rule out at least 2 alternative causes before committing to a hypothesis
- Show your reasoning: "I ruled out X because [evidence]. I ruled out Y because [evidence]. The root cause is Z because [evidence]."
- Never propose a fix that already appears in ERRORS.md under "Tried" for this issue
- If you implement a fix and the issue persists, log it to `tasks/ERRORS.md` immediately — do not wait for session end

## When investigation is complete

Append the outcome to `tasks/ERRORS.md` in this format:

```
## [Today's date] — [Issue description]
**Project:** [project name]
**Tried:** [what was attempted in this session and why it didn't work, if anything failed]
**Worked:** [what finally resolved it]
**Next time:** [key insight — what to check first next time this type of issue appears]
```

## What you must never do

- Never write a fix before stating the root cause
- Never propose the same approach that already failed (ERRORS.md)
- Never mark an issue as resolved without running the verification step
- Never touch files outside the scope of the bug being investigated
```

- [x] **Step 3: Create `~/.claude/agents/code-reviewer.md`**

```markdown
---
name: code-reviewer
description: Read-only code reviewer. Checks scope, spec match, bugs, regressions, and security. Cannot edit files.
model: claude-sonnet-4-6
tools: Read, Grep, Glob
---

You are a read-only code reviewer. You cannot and will not edit any files. Your job is to find problems, not fix them.

## Review checklist — run every item for every review

1. **Scope:** Did the implementation touch files outside the stated task scope? List any out-of-scope changes.
2. **Spec match:** Does every acceptance criterion in the spec appear in the implementation? List any gaps.
3. **Bugs:** Are there missing null checks, unhandled error paths, or uncovered edge cases? List with file:line.
4. **Regressions:** Does anything changed here risk breaking an existing user flow? Identify which flows.
5. **Security:** Any hardcoded secrets, SQL injection surface, exposed stack traces, or missing auth checks?

## Output format

```
## Code Review — [Task name] — [Date]

### Scope
PASS / FAIL — [finding]

### Spec Match
PASS / FAIL — [finding, list missing criteria if FAIL]

### Bugs
PASS / FAIL — [finding, file:line if FAIL]

### Regressions
PASS / FAIL — [finding, which flows at risk if FAIL]

### Security
PASS / FAIL — [finding]

### Verdict
APPROVED / CHANGES REQUESTED

### Required changes before approval (if any)
- [specific change 1]
- [specific change 2]
```

## What you must never do

- Never suggest refactoring outside the current task scope
- Never suggest style improvements unrelated to correctness
- Never approve when any item is FAIL — always list required changes
- Never edit a file (you don't have the tool, but this is the rule regardless)
```

- [x] **Step 4: Verify both agent files exist**

```bash
ls -la ~/.claude/agents/
```

Expected: `investigator.md` and `code-reviewer.md` listed.

---

## Task 3: Create Bash Firewall Hook

**Files:**
- Create: `~/.claude/hooks/bash-firewall.sh`

- [x] **Step 1: Create hooks directory**

```bash
mkdir -p ~/.claude/hooks
```

- [x] **Step 2: Create `~/.claude/hooks/bash-firewall.sh`**

```bash
#!/bin/bash
# Claude Code PreToolUse hook — Bash firewall
# Reads tool call JSON from stdin, blocks dangerous commands
# Exit 0 = allow, Exit 1 = block (Claude sees the stderr message)

INPUT=$(cat)

# Extract the command field from the JSON tool call
COMMAND=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    # Handle both direct and nested tool_input formats
    cmd = data.get('tool_input', data).get('command', '')
    print(cmd)
except:
    print('')
" 2>/dev/null)

if [ -z "$COMMAND" ]; then
    exit 0
fi

BLOCKED=0
REASON=""

# rm -rf (recursive force delete)
if echo "$COMMAND" | grep -qE 'rm\s+(-[a-zA-Z]*f[a-zA-Z]*r[a-zA-Z]*|-[a-zA-Z]*r[a-zA-Z]*f[a-zA-Z]*)\s'; then
    BLOCKED=1
    REASON="rm -rf is blocked. Use rm with explicit file paths and get user confirmation first."
fi

# git push --force
if echo "$COMMAND" | grep -qE 'git\s+push\s+(--force|-f)(\s|$)'; then
    BLOCKED=1
    REASON="git push --force is blocked. Ask the user explicitly before force-pushing to any remote."
fi

# git reset --hard
if echo "$COMMAND" | grep -qE 'git\s+reset\s+--hard'; then
    BLOCKED=1
    REASON="git reset --hard is blocked. This discards uncommitted work. Ask the user explicitly."
fi

# Destructive SQL
if echo "$COMMAND" | grep -qiE '(DROP\s+TABLE|TRUNCATE\s+TABLE|DROP\s+DATABASE)'; then
    BLOCKED=1
    REASON="Destructive SQL (DROP TABLE / TRUNCATE / DROP DATABASE) is blocked. Ask the user explicitly."
fi

# Destructive command targeting production
if echo "$COMMAND" | grep -qi 'production' && echo "$COMMAND" | grep -qiE '(delete|drop|truncate|destroy|remove|wipe|purge|flush)'; then
    BLOCKED=1
    REASON="Destructive command referencing 'production' is blocked. Ask the user explicitly with full details."
fi

# Wipe node_modules or dist without asking
if echo "$COMMAND" | grep -qE 'rm\s+.*node_modules' || echo "$COMMAND" | grep -qE 'rm\s+.*\.next'; then
    BLOCKED=1
    REASON="Deleting node_modules or .next is blocked. Ask the user first — this affects build state."
fi

if [ $BLOCKED -eq 1 ]; then
    echo "BLOCKED BY BASH FIREWALL: $REASON" >&2
    echo "To proceed with this command, ask the user explicitly in the current message and get a 'yes'." >&2
    exit 1
fi

exit 0
```

- [x] **Step 3: Make the script executable**

```bash
chmod +x ~/.claude/hooks/bash-firewall.sh
```

- [x] **Step 4: Test the firewall locally**

```bash
# Should be blocked
echo '{"tool_input": {"command": "rm -rf /tmp/test"}}' | ~/.claude/hooks/bash-firewall.sh
echo "Exit code: $?"

# Should be allowed
echo '{"tool_input": {"command": "ls -la"}}' | ~/.claude/hooks/bash-firewall.sh
echo "Exit code: $?"
```

Expected:
- First command: prints `BLOCKED BY BASH FIREWALL: rm -rf is blocked...`, exit code 1
- Second command: no output, exit code 0

---

## Task 4: Update Global settings.json with Hooks

**Files:**
- Modify: `~/.claude/settings.json`

The existing settings.json has `permissions` and `enabledPlugins`. We are adding a `hooks` key alongside them. Do not remove or change any existing content.

- [x] **Step 1: Read the current settings.json to confirm current structure**

```bash
cat ~/.claude/settings.json
```

Confirm the file has `permissions` and `enabledPlugins` at the top level.

- [x] **Step 2: Add hooks to `~/.claude/settings.json`**

Add the `"hooks"` key to the existing JSON object. The complete updated file:

```json
{
  "permissions": {
    "allow": [
      "Read(//Users/nadavyigal/Documents/RunSmart/**)",
      "Read(//Users/nadavyigal/Documents/Projects/**)",
      "Read(//Users/nadavyigal/Documents/**)",
      "Bash(xargs cat *)",
      "Bash(npx cap *)",
      "Read(//Users/nadavyigal/**)",
      "Read(//Users/nadavyigal/.config/**)",
      "mcp__plugin_supabase_supabase__execute_sql",
      "Bash(vercel promote *)",
      "Skill(superpowers:brainstorming)",
      "Skill(superpowers:brainstorming:*)",
      "mcp__claude_ai_PostHog__exec",
      "Bash(xcodebuild -project '/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app/IOS RunSmart app.xcodeproj' -scheme 'IOS RunSmart app' -destination 'generic/platform=iOS Simulator' build)"
    ],
    "additionalDirectories": [
      "/Users/nadavyigal/Documents/RunSmart"
    ]
  },
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "context7@claude-plugins-official": true,
    "github@claude-plugins-official": true,
    "playwright@claude-plugins-official": true,
    "claude-md-management@claude-plugins-official": true,
    "supabase@claude-plugins-official": true,
    "vercel@claude-plugins-official": true
  },
  "extraKnownMarketplaces": {
    "claude-plugins-official": {
      "source": {
        "source": "github",
        "repo": "anthropics/claude-plugins-official"
      }
    }
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$HOME/.claude/hooks/bash-firewall.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Before this session ends: Did any approach fail more than once during this session? If yes, append it now to tasks/ERRORS.md (or ~/.claude/ERRORS.md if this was a cross-project session) using this format:\n\n## [Today's date] — [Issue description]\n**Project:** [project name]\n**Tried:** [what failed and why]\n**Worked:** [leave blank if unresolved]\n**Next time:** [key insight]\n\nOnly write to ERRORS.md if something genuinely failed. Skip this step if everything worked on the first or second attempt."
          },
          {
            "type": "prompt",
            "prompt": "Write a session summary now to tasks/MEMORY.md (or ~/.claude/MEMORY.md if cross-project). Use this format:\n\n## [Today's date] — [Brief session title]\n**Worked on:** [what we focused on]\n**Completed:** [what is finished and verified]\n**In progress:** [what was started but not finished]\n**Decisions:** [any architectural or product choices made this session]\n**Next session:** [exactly what to pick up first, with enough context to resume cold]\n\nKeep it under 200 words. This is a status update, not a recap."
          }
        ]
      }
    ]
  }
}
```

**Note:** The `curl` line with the Resend API key was removed from permissions — it contained a hardcoded API key. Do not add it back. If the Resend API is needed, use environment variables instead.

- [x] **Step 3: Validate the JSON is well-formed**

```bash
python3 -m json.tool ~/.claude/settings.json > /dev/null && echo "JSON valid" || echo "JSON INVALID — fix before continuing"
```

Expected: `JSON valid`

- [x] **Step 4: Verify hooks key is present**

```bash
python3 -c "import json; d=json.load(open('$HOME/.claude/settings.json')); print('hooks keys:', list(d.get('hooks', {}).keys()))"
```

Expected: `hooks keys: ['PreToolUse', 'Stop']`

---

## Task 5: Update Global CLAUDE.md

**Files:**
- Modify: `~/.claude/CLAUDE.md`

We are adding 4 blocks. The existing content stays intact. Changes:
1. Replace the Session Start Ritual section with an upgraded version
2. Add "Never Do" block after Global Work Rules
3. Add "Permanent Facts" block after Never Do
4. Add "Session End" block at the end of the file

- [x] **Step 1: Replace the Session Start Ritual section**

Find this exact block (lines 27–33 in the current file):
```markdown
## Session Start Ritual (Every Project, Every Time)

1. **Read** the project `CLAUDE.md` — it's auto-loaded, so this is already done
2. **Read** `docs/agent-os/project-context.md` if it exists — architecture decisions, scope, open questions
3. **Read** `tasks/lessons.md` if it exists — known bugs and their fix paths (do this before any triage)
4. **State** the objective in one sentence before planning anything
5. **Follow** `docs/agent-os/planning-protocol.md` for any task touching more than 2 files
```

Replace with:
```markdown
## Session Start Ritual (Every Project, Every Time)

Before doing anything each session — in this order:

1. **Read** `~/.claude/MEMORY.md` — never contradict a logged decision without flagging it first
2. **Read** `~/.claude/ERRORS.md` — never propose an approach already logged as failed
3. **Read** `~/.claude/LEARNINGS.md` — prefer patterns logged as working well
4. **Read** `tasks/MEMORY.md` if it exists — project-specific decisions and session history
5. **Read** `tasks/ERRORS.md` if it exists — project-specific failed approaches
6. **Read** `docs/agent-os/project-context.md` if it exists — architecture decisions, scope, open questions
7. **Read** `tasks/lessons.md` if it exists — known bugs and their fix paths
8. **State** the objective in one sentence before planning anything
9. **Follow** `docs/agent-os/planning-protocol.md` for any task touching more than 2 files
```

- [x] **Step 2: Add "Never Do" block after the Global Work Rules section**

After the closing of the Global Work Rules section, add:

```markdown
---

## Never Do

- Never open responses with: "Great question!", "Of course!", "Certainly!", "Absolutely!", "Sure!", "Happy to help", or any warmup phrase. Start directly with the answer.
- Never use em dashes (—).
- Never use these phrases: "dive into", "it's worth noting", "in today's world", "let's explore", "in conclusion".
- Never ask "would you like me to continue?" — just continue.
- Never give generic advice — be specific to the project and codebase.
- Never propose an approach that already appears in `ERRORS.md` as failed for this issue.
- Never declare a task done without evidence: lint pass, test pass, or explicit QA report.
- Never re-explain something already in MEMORY.md — reference it instead.
```

- [x] **Step 3: Add "Permanent Facts" block after Never Do**

```markdown
---

## Permanent Facts

These are always true. Flag any conflict before proceeding — do not work around them silently:

- Solo founder — no team to coordinate with. Speed and clarity matter more than ceremony.
- RunSmart is primary; ResumeBuilder is secondary.
- Mac-based (moved from Windows March 2026).
- Never suggest new npm dependencies without asking first.
- Never deploy or run migrations without explicit "yes" in the current message.
- Scope gate: if a fix expands to touch >3 unexpected files, stop and surface it before continuing.
- No secrets in code — no hardcoded API keys, URLs, or env-specific values ever.
- One story at a time — implement, verify (lint + tests), report evidence, then ask before next story.
```

- [x] **Step 4: Add "Session End" block at the end of the file**

```markdown
---

## Session End

When I say "session end", "wrapping up", "done for now", or "let's stop here":

1. Write a session summary to `tasks/MEMORY.md` (or `~/.claude/MEMORY.md` if cross-project):
   ```
   ## [Date] — [Brief session title]
   Worked on: [what we focused on]
   Completed: [what is finished and verified]
   In progress: [what was started but not done]
   Decisions: [key choices made]
   Next session: [what to pick up first, with enough context to resume cold]
   ```
2. If any approach failed more than once this session, append it to `tasks/ERRORS.md`.
3. If a pattern worked especially well, append it to `~/.claude/LEARNINGS.md`.
4. List: files changed, tests run, open questions, what was NOT done this session.
```

- [x] **Step 5: Verify the CLAUDE.md changes look correct**

```bash
grep -n "Never Do\|Permanent Facts\|Session End\|MEMORY.md\|ERRORS.md\|LEARNINGS.md" ~/.claude/CLAUDE.md
```

Expected: lines from all 4 new blocks appear in the output.

---

## Task 6: Create RunSmart Project Memory Files

**Files:**
- Create: `/Users/nadavyigal/Documents/RunSmart/tasks/MEMORY.md`
- Create: `/Users/nadavyigal/Documents/RunSmart/tasks/ERRORS.md`

- [x] **Step 1: Create RunSmart `tasks/MEMORY.md`**

```markdown
# RunSmart — Decision Log

Project-specific architectural and product decisions. Read at the start of every RunSmart session.

## Format
## YYYY-MM-DD — [Decision title]
**Decided:** [What was chosen]
**Why:** [The reasoning]
**Rejected:** [Alternatives considered and why ruled out]

---

## 2026-05-20 — Agentic OS Setup
**Decided:** Added MEMORY.md, ERRORS.md, hooks, and subagents to Claude Code setup
**Why:** To eliminate re-explaining context and re-proposing failed approaches between sessions
**Rejected:** Minimal patch — hooks provide structural enforcement that CLAUDE.md instructions alone cannot
```

- [x] **Step 2: Create RunSmart `tasks/ERRORS.md`**

```markdown
# RunSmart — Failed Approaches Log

Read this before proposing any fix in RunSmart. Never propose an approach already logged here.

## Format
## YYYY-MM-DD — [Issue description]
**Tried:** [What was attempted and why it failed]
**Worked:** [What finally resolved it — fill in when resolved]
**Next time:** [Key insight to carry forward]

---
```

- [x] **Step 3: Verify files exist in RunSmart**

```bash
ls -la "/Users/nadavyigal/Documents/RunSmart/tasks/"
```

Expected: `lessons.md`, `MEMORY.md`, and `ERRORS.md` all listed.

- [x] **Step 4: Commit to RunSmart repo**

```bash
cd "/Users/nadavyigal/Documents/RunSmart" && git add tasks/MEMORY.md tasks/ERRORS.md && git commit -m "chore: add session memory and error log files for Claude Code continuity"
```

---

## Task 7: Create ResumeBuilder Project Memory Files

**Files:**
- Create: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/MEMORY.md`
- Create: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/ERRORS.md`

- [x] **Step 1: Create ResumeBuilder `tasks/MEMORY.md`**

```markdown
# ResumeBuilder — Decision Log

Project-specific architectural and product decisions. Read at the start of every ResumeBuilder session.

## Format
## YYYY-MM-DD — [Decision title]
**Decided:** [What was chosen]
**Why:** [The reasoning]
**Rejected:** [Alternatives considered and why ruled out]

---

## 2026-05-20 — Agentic OS Setup
**Decided:** Added MEMORY.md and ERRORS.md to Claude Code setup for this project
**Why:** To eliminate re-explaining context and re-proposing failed approaches between sessions
**Rejected:** Minimal patch — structural enforcement requires the full system
```

- [x] **Step 2: Create ResumeBuilder `tasks/ERRORS.md`**

```markdown
# ResumeBuilder — Failed Approaches Log

Read this before proposing any fix in ResumeBuilder. Never propose an approach already logged here.

## Format
## YYYY-MM-DD — [Issue description]
**Tried:** [What was attempted and why it failed]
**Worked:** [What finally resolved it — fill in when resolved]
**Next time:** [Key insight to carry forward]

---
```

- [x] **Step 3: Verify files exist in ResumeBuilder**

```bash
ls -la "/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/"
```

Expected: `lessons.md`, `MEMORY.md`, and `ERRORS.md` all listed.

- [x] **Step 4: Commit to ResumeBuilder repo**

```bash
cd "/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-" && git add tasks/MEMORY.md tasks/ERRORS.md && git commit -m "chore: add session memory and error log files for Claude Code continuity"
```

---

## Task 8: End-to-End Verification

Verify the full system works together before declaring the plan complete.

- [x] **Step 1: Confirm all new files exist**

```bash
ls -la ~/.claude/MEMORY.md ~/.claude/ERRORS.md ~/.claude/LEARNINGS.md
ls -la ~/.claude/agents/investigator.md ~/.claude/agents/code-reviewer.md
ls -la ~/.claude/hooks/bash-firewall.sh
ls -la "/Users/nadavyigal/Documents/RunSmart/tasks/MEMORY.md"
ls -la "/Users/nadavyigal/Documents/RunSmart/tasks/ERRORS.md"
ls -la "/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/MEMORY.md"
ls -la "/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/ERRORS.md"
```

Expected: all 9 files listed with size > 0.

- [x] **Step 2: Confirm settings.json is valid and has hooks**

```bash
python3 -m json.tool ~/.claude/settings.json > /dev/null && echo "JSON valid"
python3 -c "import json; d=json.load(open('$HOME/.claude/settings.json')); hooks=d.get('hooks',{}); print('PreToolUse hooks:', len(hooks.get('PreToolUse',[]))); print('Stop hooks:', len(hooks.get('Stop',[])))"
```

Expected:
```
JSON valid
PreToolUse hooks: 1
Stop hooks: 1
```

- [x] **Step 3: Test the bash firewall blocks dangerous commands**

```bash
echo '{"tool_input": {"command": "rm -rf ~/Documents"}}' | ~/.claude/hooks/bash-firewall.sh
echo "Blocked rm -rf: exit $?"

echo '{"tool_input": {"command": "git push --force origin main"}}' | ~/.claude/hooks/bash-firewall.sh
echo "Blocked force push: exit $?"

echo '{"tool_input": {"command": "ls -la"}}' | ~/.claude/hooks/bash-firewall.sh
echo "Allowed ls: exit $?"
```

Expected:
```
BLOCKED BY BASH FIREWALL: rm -rf is blocked...
Blocked rm -rf: exit 1
BLOCKED BY BASH FIREWALL: git push --force is blocked...
Blocked force push: exit 1

Allowed ls: exit 0
```

- [x] **Step 4: Confirm CLAUDE.md has all new blocks**

```bash
grep -c "Never Do\|Permanent Facts\|Session End\|MEMORY.md\|ERRORS.md\|LEARNINGS.md" ~/.claude/CLAUDE.md
```

Expected: count of 6 or more (each term appears at least once).

- [x] **Step 5: Open a new Claude Code session in RunSmart and verify session start**

```bash
cd /Users/nadavyigal/Documents/RunSmart
# Open claude and send this first message:
# "What do you know about this project from memory?"
```

Expected behavior: Claude reads MEMORY.md, ERRORS.md, tasks/MEMORY.md, tasks/ERRORS.md, and summarizes what it found — including the 2026-05-20 setup entry — without being asked to read those files.

---

## What Success Looks Like

After this plan is complete:

| Behavior | Before | After |
|----------|--------|-------|
| Session start | Re-explain context every time | Claude reads MEMORY.md + ERRORS.md automatically |
| Bug that was tried before | Claude re-proposes same failed fix | Claude checks ERRORS.md, skips to what worked |
| Destructive shell command | Executes after permission prompt | Blocked at hook level with explanation |
| Session end | Context lost | Summary written to MEMORY.md automatically |
| New feature | Claude jumps to implementation | brainstorming → plan → story-by-story → QA |
| Code review | Manual or skipped | code-reviewer subagent with structured checklist |
| Debug session | Guess and patch | investigator subagent reads ERRORS.md first, finds root cause |
