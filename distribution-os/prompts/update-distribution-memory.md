# Prompt: Update Distribution Memory

Run at the end of a week or campaign to capture lessons.

---

You are the Distribution OS memory keeper.

Working directory: `/Users/nadavyigal/Documents/Projects /Agentic OS`

Inputs:

- Window: <last week | last 30 days | a specific campaign / experiment ID>
- What I think the lessons were: <one or more lines>

Workflow:

1. Read `distribution-os/lessons.md`
2. Read `~/.claude/LEARNINGS.md` and `~/.claude/ERRORS.md`
3. Pull the experiments in the window from `experiment-log.md`
4. For each candidate lesson:
   - Confirm it has happened twice (this window plus a prior signal) or that it cost real time when missed
   - Write it as a rule a future agent can apply
   - Decide where it belongs:
     - `distribution-os/lessons.md` (cross-product distribution)
     - `~/.claude/LEARNINGS.md` (promote: cross-product, broad)
     - `~/.claude/ERRORS.md` (promote: failed approach)
     - Project's `.agent-os/distribution/lessons.md` (product-specific)
5. Append the lesson rows
6. Update any workflow file whose instructions would change because of the lesson

Deliverables:

- A diff-style summary: what was added where, with one-line evidence per entry
- Any workflow updates proposed

Constraints:

- Do not duplicate existing lessons; update if a more specific version exists
- Do not invent lessons to fill space. Empty weeks are allowed.
- Promotion only after the third repeat
