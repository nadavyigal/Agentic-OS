# Decision Log Workflow

## Purpose

Capture decisions in Obsidian-readable form while keeping durable cross-project architectural decisions in Agentic OS `DECISIONS.md`.

## When To Run It

- When a founder, product, architecture, workflow, pricing, or strategy decision is made.
- When a decision is proposed and should be revisited later.
- When a decision from Agentic OS needs a human-readable Obsidian note.

## Inputs

- The source decision or conversation summary.
- `DECISIONS.md` for durable cross-project decisions.
- Product repo decision files, if product-specific.
- `docs/obsidian/templates/decision-template.md`

## Steps

1. Decide whether the decision is durable enough for Agentic OS `DECISIONS.md`.
2. If yes, update `DECISIONS.md` through the normal Agentic OS process.
3. Create an Obsidian export note in `exports/obsidian/decisions/`.
4. Use the title format `Decision: {{title}}`.
5. Record the decision, why now, context, options, recommendation, risks, mitigations, next actions, and links.
6. Copy the note into `05-Decisions/` or the relevant product `Decisions/` folder in Obsidian.

## Output File Location

`exports/obsidian/decisions/`

## Quality Checklist

- The decision is stated plainly.
- The reason and tradeoff are visible.
- The owner and status are clear.
- Links point back to source files when possible.
- Durable architectural decisions are not stranded only in Obsidian.

## What Not To Include

- Secrets or credentials.
- Private customer details.
- Speculative decisions presented as final.
- Product status that was not verified.
- Raw transcripts when a summary is enough.
