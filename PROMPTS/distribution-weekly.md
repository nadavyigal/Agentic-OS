# Distribution Weekly Prompt

Thin pointer into the Distribution OS. Paste this into Codex or Claude Code from the Agentic OS root to run a full weekly distribution cycle.

## Use

```
Read and execute: distribution-os/prompts/weekly-distribution-run.md
```

That prompt is self-contained. It sets context, runs `distribution-os/workflows/00-weekly-distribution-cycle.md`, and stops at the founder review checkpoint.

## Pre-Flight Checklist

Before pasting, decide:

- Focused product for the week (RunSmart or ResumeBuilder)
- Theme (one sentence)
- What you want me to know about last week (one to three lines)
- Whether your metrics are fresh in Notion / Drive, or I should reuse last week's snapshot

Drop those into the prompt's "inputs from me" block, then run.

## Constraints The Agent Will Apply

- No publishing externally
- Free / low-cost channels first
- No new dependencies
- No edits to product repo source code

## Where Output Lands

- Drafts: Drive `03 Campaigns/{product}/` or `04 Content Assets/...`
- Logs: `distribution-os/experiment-log.md`, `distribution-os/distribution-command-center.md`, `distribution-os/weekly-growth-review.md`
- Notion: Command Center, Experiment Backlog, Campaign Calendar, Content / Asset Pipeline (when connector present)

## When To Run

Weekly. Same day each week (Monday default).
