# Orchestration Gate

The first step for any **raw, ungated request** — before `DAILY.md` Tier 0/1/2 gets
picked by hand, before a `Mode` gets chosen, before a `Workflow pattern` gets
picked from `GLOBAL-WORKFLOWS.md`. This file exists because that routing was
previously done entirely in the founder's head: read `DAILY.md`, guess a Tier,
guess a Mode, guess a pattern. This table makes that first classification
step explicit and fast — a lookup, not a new process layer.

## When To Use This

Run this gate only when the incoming ask is **not already** one of:

- A scoped work packet with Goal / Task / Constraints / Validation → skip
  straight to **Execution mode** in `AGENTS.md`.
- A daily Command Center action → skip straight to `DAILY.md` Tier 0.

Everything else — a raw prompt, a new idea, a "can you look into X," a
sketch, a question with no clear box to put it in — goes through this table
first.

## The Table

| Signal in the request | Tier (`DAILY.md`) | Mode (`AGENTS.md` Mode Contracts) | Workflow pattern (`GLOBAL-WORKFLOWS.md`) | Route to |
|---|---|---|---|---|
| "What should I do next / what's the status" | Tier 0 | n/a | normal | Command Center (`./agentic-os morning`) |
| A single scoped bug or feature in a known product repo | Tier 1 | Builder | normal | Product repo, Execution mode |
| "Quick test / prototype / see if this works" | Tier 1 | Prototyper | normal | Product repo |
| "Clean up / delete / simplify," no new functionality | Tier 1 | Sweeper | normal | Product repo |
| Tied to a metric, funnel step, or channel score | Tier 1 | Grower | normal | `distribution-os/` or product repo |
| Touches auth, billing, production data, or a migration | Tier 1–2 | Maintainer | adversarial-review | `RISK-OS.md` first, then product repo |
| Debugging with an unknown number of passes needed | Tier 1 | Builder | loop-until-done | Product agent / QA |
| Independent research angles (competitor, market, GitHub, pricing) | Tier 2 | n/a | fan-out-research | Analysis OS |
| "Poke holes in this / is this safe / sanity-check this" | Tier 2 | n/a | adversarial-review | Risk OS / QA / Taste |
| Need options before a direction is chosen | Tier 2 | n/a | generate-filter | Analysis OS / CEO OS |
| Comparing named alternatives (UI, naming, copy, positioning) | Tier 2 | n/a | tournament | CEO OS / Taste |
| Untrusted external content (scraped page, email, client doc, ticket) | Tier 2 | n/a | quarantine | Analysis OS / Risk OS |
| Sequencing, priorities, pricing, "what's next across the portfolio" | Tier 2 | n/a | normal | `COO-OS.md` / `CEO-OS.md` |
| Vague major idea, not yet scoped | Tier 2 | n/a | normal | `PROMPTS/context-extraction.md` |

If nothing matches cleanly, default to **Tier 1, Mode Builder, pattern
normal** — the same default `AGENTS.md` already uses when a work packet omits
a `Mode` field. Do not block on an ambiguous case; classify with the closest
row and flag the ambiguity in the output line below.

## Output Format

State the classification in one line before acting, so the choice is visible
and reviewable — not just made silently:

```
GATE: Tier <0|1|2> · Mode <name|n/a> · Pattern <name> · Route <file or OS>
```

## What This Is Not

- Not a new approval step — it does not add a human checkpoint beyond what
  `AGENTS.md` "Stop And Ask Before" already requires.
- Not automation — no script runs this; it is a decision table an agent (or
  the founder) applies at the top of a session, the same way the `Advanced
  Workflow Modes` table in `GLOBAL-WORKFLOWS.md` already gets applied by hand.
  This file exists to make that one lookup happen *first*, consistently,
  instead of being skipped because `DAILY.md` was never opened.
- Not a replacement for `DAILY.md`, `AGENTS.md`, or `GLOBAL-WORKFLOWS.md` —
  it only decides which of those three tables to consult, and with what
  inputs.
