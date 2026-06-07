# Weekly Obsidian Review Workflow

## Purpose

Create a human-readable weekly review note that summarizes what changed, what matters, what is blocked, and what should happen next.

## When To Run It

- At the end of a week.
- Before or after a Weekly CEO Review.
- When the dashboard has been refreshed and the founder wants a readable summary in Obsidian.

## Inputs

- `DASHBOARD.md`
- `PROJECT-STATUS.md`
- `executive-os/WEEKLY-CEO-LATEST.md`, if present and current.
- Relevant project task files only when fresh source evidence is needed.
- `docs/obsidian/templates/weekly-review-template.md`

## Steps

1. Read current Agentic OS status sources.
2. Create `exports/obsidian/weekly-reviews/YYYY-MM-DD-weekly-review.md`.
3. Summarize movement, blockers, decisions, lessons, next priorities, and risks.
4. Link major projects using wiki links such as `[[RunSmart]]` and `[[ResumeBuilder]]`.
5. Keep status evidence clear, especially when a project status is inferred.
6. Copy the finished note into `07-Weekly-Reviews/` in the Obsidian vault.

## Output File Location

`exports/obsidian/weekly-reviews/`

## Quality Checklist

- It is clear what actually changed this week.
- It separates facts from recommendations.
- It includes next-week priorities.
- It does not invent product status from memory.
- It is short enough to reread quickly.

## What Not To Include

- Raw build logs.
- Full task logs.
- Secrets, credentials, or customer data.
- Long pasted transcripts.
- Status that was not verified from current files.
