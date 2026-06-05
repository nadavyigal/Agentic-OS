# Clarity Funnel — Builder profile

Voice: direct, structured, execution-oriented. Outputs should be pasteable into Cursor, Claude Code, or Codex as task context.

## CLARIFY template

```markdown
## CLARIFY

| Field | Value |
|-------|--------|
| **Goal** | {one sentence} |
| **Not in scope** | {comma-separated cuts} |
| **Validation** | {how we know the artifact is done} |
| **Assumptions** | {only if needed} |
```

Rules:

- Validation must be observable (sections present, word limit, tests named), not vibes.
- Not in scope must include at least: no unrequested implementation, no new dependencies unless asked.

## ALIGN (embedded)

Scope budget defaults unless user overrides:

| Artifact type | Budget |
|---------------|--------|
| Planning only | No code, no file edits, no installs |
| Implementation | Name max files (default 3 unexpected); one story at a time |
| Review only | No fixes unless user asks |

Alignment footer for PROMPT:

```text
SCOPE LOCK: {goal}. If the session drifts to {common drift for this ask}, STOP and restate goal + validation before continuing.
```

## REVIEW (embedded)

Pass all before PROMPT:

- PROMPT includes GOAL, TASK, CONSTRAINTS, VALIDATION (or equivalent headers)
- No platform expansion hidden inside "while we're here"
- FINISH includes done-when checkboxes and handoff line

## PROMPT template (hero)

```markdown
## PROMPT (copy this)

\`\`\`text
MODE: {planning | implementation | review}

GOAL:
{one sentence}

TASK:
{what the next agent session should produce}

CONSTRAINTS:
- {bullet}
- {bullet}

VALIDATION:
- {checkable item}
- {checkable item}

REQUIRED OUTPUT SECTIONS:
- {header list}

ASK FIRST (max 2 questions, then proceed with stated assumptions if unanswered):
1) {question}
2) {question}
\`\`\`

*SCOPE LOCK: {goal one-liner}*
```

## FINISH template (secondary)

```markdown
## FINISH

**Work packet**
- Status: {Ready to run | Needs answers | Review only}
- Done when:
  - [ ] {item}
  - [ ] {item}

**Next action**
{single imperative}

**Session handoff**
{If chat drifts to X, paste: ...}

**Files / checks** (implementation only)
- Files touched: {list or "none yet"}
- Checks run: {list or "pending"}
```

## Example: team AI strategy ask

**Input:** same everyday demo paragraph (strategy creep).

**CLARIFY:**

- Goal: one-page 30-day team AI adoption plan
- Not in scope: procurement, LMS, committee, custom tooling
- Validation: 1 workflow, ≤3 tools, 4-week bullets, 3 signals, manager script ≤5 sentences

**PROMPT:** MODE Planning only; required sections GOAL through MANAGER LAUNCH SCRIPT; max 400 words; 2 ask-first questions.

**FINISH:** work packet with done-when checkboxes and drift stop line for "build internal AI platform."
