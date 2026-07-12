# Daily Operations — Agentic OS

One page for every work day. Executive OS, research, decisions, and long-running GTM/launch/monetization plans are **fully preserved** — this file only defines what you open **first**.

## Tier -1 — Gate (only for a raw, ungated request)

If what just came in is a raw ask — not already a Tier 0 daily action and not
already a scoped work packet with Goal/Task/Constraints/Validation — classify
it against `ORCHESTRATION-GATE.md` before doing anything else. That table
picks the Tier, the `Mode`, and the `Workflow pattern` in one lookup instead
of three separate manual decisions. Skip this step entirely once the request
is already a Tier 0 action or an Execution-mode packet.

## Tier 0 — Daily (60–90 seconds)

1. From the Agentic OS repo root, run:

   ```bash
   ./agentic-os morning
   ```

2. Open Portfolio HQ (localhost link from the command output).

3. Read only the first two sections:

   - **The one thing to do next** — choose one action. Each card says where to do
     it and includes a copy button when an agent prompt is useful.
   - **Active work packets** — copy one only if this section shows an active
     packet. It names the exact product repo where the packet should be pasted.
     If it says "No active work packet today," there is nothing to paste.

4. Trust rule: do not treat App Store review, submit readiness, or "ready to ship" claims as authoritative unless sync is clean and portfolio trust is **actionable**.

## Tier 1 — Execute (one move)

1. Copy **one** active work packet from the Command Center.
2. Open the exact **target product repo** printed on the packet card.
3. Paste the packet as the new task context.

Closed, research-complete, and ready-for-later packets remain in
`executive-os/work-packets/` as history. They do not appear in the daily Active
work packets section and should not be pasted into a product repo.

Agent reads in the product repo only: `AGENTS.md` / `CLAUDE.md`, `tasks/MEMORY.md`, `tasks/ERRORS.md`, and files named in the packet.

**Execution mode** (see `AGENTS.md`): if the packet has Goal, Task, Constraints, and Validation, implement without scope questions. Ask only on hard blockers (missing device, credentials, wrong repo).

## Tier 2 — Executive (on demand, unchanged capability)

Use when sequencing is unclear, you need a decision, or it is weekly review time. **Nothing below is removed or deprecated.**

| When | Open |
|------|------|
| What happens next / which repo | `PROMPTS/coo-operating-review.md` + `executive-os/COO-OS.md` |
| Weekly portfolio / tradeoffs | `PROMPTS/executive-weekly-review.md` + `executive-os/CEO-OS.md` |
| Finance / pricing / monetization shape | `PROMPTS/cfo-monthly-review.md` + `executive-os/CFO-OS.md` |
| Competitor / market research | `PROMPTS/analysis-research-sprint.md` + `executive-os/research/` |
| Vague major idea before scoping | `PROMPTS/context-extraction.md` + `executive-os/workflows/context-extraction.md` |
| New idea before it is a decision | `executive-os/NEXT-MOVES.md` |
| Log or resolve a strategic call | `executive-os/EXECUTIVE-DECISIONS.md` |
| Launch / channels / distribution | `distribution-os/` + project GTM plans (read in **weekly** review, not daily) |
| Manual executive snapshot | `executive-os/EXECUTIVE-DASHBOARD.md` (updated by weekly CEO review) |

**COO rule for long-running plans:** Plans (GTM, launch, monetization, distribution) are strategy sources. The COO extracts the **next milestone** into **one** work packet. If the dashboard shows **Needs next packet** for a plan, run the COO operating review — the plan is not abandoned.

## Weekly (not daily)

- `./agentic-os morning` output + Command Center plan index
- `PROMPTS/executive-weekly-review.md` — includes **plan progress** checklist (milestones, blockers, `needs_next_packet`)
- Full saved plans board: `dashboard/project-status.html` (Saved Plans section)

## Session end (30 seconds, in the product repo you touched)

Update `tasks/progress.md` using `TEMPLATES/progress-template.md` and `STATUS-SCHEMA.md`. Set **Last Updated** and **Last Validation** so the next morning refresh can reach High confidence.

## References

- Canonical agent rules: `AGENTS.md`
- Cursor adapter: `CURSOR.md`
- Status contract: `STATUS-SCHEMA.md`
- Executive layer map: `executive-os/README.md`
