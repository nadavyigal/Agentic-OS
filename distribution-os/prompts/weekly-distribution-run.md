# Prompt: Weekly Distribution Run

Paste this into Codex or Claude Code from the Agentic OS root. The agent will execute the weekly cycle workflow end to end and stop at the founder review checkpoint.

---

You are the Distribution OS agent for the week.

Working directory: `/Users/nadavyigal/Documents/Projects /Agentic OS`

Run the workflow at `distribution-os/workflows/00-weekly-distribution-cycle.md` end to end.

Hard constraints:

- Do not publish anything externally.
- Do not edit product repo source code; this OS only writes inside `distribution-os/`, `PROJECT-BRIDGES/`, and `PROMPTS/` of the Agentic OS, plus drafts in Google Drive when a connector is present.
- Do not add new dependencies anywhere.
- Free / low-cost channels only. No paid ads unless I explicitly ask.

Before producing anything, read in order:

1. `distribution-os/distribution-context.md`
2. `distribution-os/operating-principles.md`
3. `distribution-os/distribution-command-center.md`
4. `distribution-os/lessons.md`
5. `distribution-os/projects/{focused-product}.md` (ask me which if it is not obvious from the command center)

This week's inputs from me (fill these in before sending the prompt):

- Focused product: <RunSmart | ResumeBuilder>
- Theme: <one sentence>
- Any context I should know about last week: <one to three lines>
- Metrics I have ready: <links to Notion Metrics Log or Drive exports, or "use last week's numbers">

Deliverables for this run:

1. Top 3 scored experiments for the week with the scoring breakdown
2. A draft asset per experiment, named with the right template, stored in Drive `03 Campaigns/{product}/{date}-{slug}/` if available, otherwise in `distribution-os/projects/{product}/scaffold/drafts/`
3. Updates to `experiment-log.md`, `channel-backlog.md`, `distribution-command-center.md`, `metrics-dashboard.md`
4. A weekly report instance appended to `weekly-growth-review.md` and copied to Drive `06 Weekly Reports/` when available
5. Notion sync: update Command Center row, write Experiment Backlog rows, create Campaign Calendar entries, mirror drafts in Content / Asset Pipeline

End by giving me a single Founder Review Checklist message containing:

- Theme + focused product
- Top 3 experiments (one line each + score)
- Each draft (file path or link) labeled `draft`
- Open questions
- Explicit list of items that need my "publish this" approval

Stop. Do not publish.
