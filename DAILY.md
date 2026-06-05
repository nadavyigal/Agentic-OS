# Daily Operations — Agentic OS

One page for every work day. Executive OS, research, decisions, and long-running GTM/launch/monetization plans are **fully preserved** — this file only defines what you open **first**.

## Tier 0 — Daily (60–90 seconds)

1. From the Agentic OS repo root, run:

   ```bash
   ./agentic-os morning
   ```

2. Open the Command Center (localhost link from the command output).

3. Read in order:

   - **Sync / trust** pill — if "Needs sync" or trust is not actionable, fix git sync or re-run morning before trusting status.
   - **Do this next** — derived from product repo `tasks/progress.md` (or derived task files).
   - **Work packets (Active)** — in the operating loop; these are what you execute today.
   - **Strategic plans (index)** — titles and status only (`active`, `needs_next_packet`, `research_only`). Do **not** open full plan files in Tier 0.

4. Trust rule: do not treat App Store review, submit readiness, or "ready to ship" claims as authoritative unless sync is clean and portfolio trust is **actionable**.

## Tier 1 — Execute (one move)

1. Copy **one** active work packet from the Command Center (or the recommended project prompt).
2. Open the **target product repo** (not Agentic OS) in Claude Code, Cursor, or Codex.
3. Paste the packet as the session context.

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
