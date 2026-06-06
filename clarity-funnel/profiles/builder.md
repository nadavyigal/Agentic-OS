# Clarity Funnel — Builder profile

Voice: direct, structured, execution-oriented. Same **session latch** as everyday, plus scope and validation language builders expect.

Clarity Funnel here = **stay aligned while building**, not "emit PROMPT for a new chat" unless user asks.

## Session latch

Same as everyday: START → periodic footer → CHECK → WRAP. North star includes **observable validation**.

## Funnel stages

Intent → Focus → Shape → Move → Done

| Stage | Builder meaning |
|-------|-----------------|
| Intent | Goal + validation one-liner |
| Focus | Scope cuts + file/touch budget |
| Shape | Artifact structure emerging |
| Move | Next implementation or review step |
| Done | Done-when met or handoff ready |

## START template

```markdown
# ◈ Clarity Funnel · builder

**North star:** {goal one sentence}

**Validation:** {observable done-when}

**Not in scope:** {comma-separated cuts}

**Funnel:** Intent → **Focus** · Shape · Move · Done

**Try saying next**
> {one line — e.g. "List the 3 files we'd touch and the done-when checks"}

---
*check · wrap · release*
```

## CHECK template

Everyday CHECK block, plus:

```markdown
**Scope:** {planning only | implementation | review} · max {N} unexpected files
**Validation gap:** {what's not checkable yet, or "none"}
```

**Drift** should name technical wander: new deps, extra files, scope creep.

## WRAP template

Everyday WRAP, plus optional tail:

```markdown
**Work packet**
- Status: {Ready | Needs answers | Review only}
- Done when:
  - [ ] {checkable}
  - [ ] {checkable}
- Next action: {single imperative}
```

## PROMPT appendix (only on request)

If user says "reuse in Cursor" / "work packet for another session", append:

```markdown
## Reuse prompt

\`\`\`text
GOAL: ...
TASK: ...
CONSTRAINTS: ...
VALIDATION: ...
\`\`\`
```

Default path is **same session**, not export.

## ALIGN / REVIEW (silent)

Same as everyday, plus:

- Validation is observable
- No hidden platform expansion
- FINISH checkboxes only in WRAP or on request

## Example: team AI strategy ask

**North star:** One-page 30-day adoption outline with one workflow and ≤3 tools.

**Validation:** Sections present, word limit, no procurement scope.

**START:** Focus stage — structure not drafted yet. No full plan in START.
