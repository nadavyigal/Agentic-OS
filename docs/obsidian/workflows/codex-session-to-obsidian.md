# Codex Session To Obsidian Workflow

## Purpose

Capture important Codex sessions as concise notes for founder memory, without replacing git history, pull requests, or Agentic OS task memory.

## When To Run It

- After Codex plans or implements a meaningful unit of work.
- After a session produces a reusable workflow lesson.
- After a high-risk review or architecture discussion.
- When the founder wants a readable summary in Obsidian.

## Inputs

- Codex final summary.
- `git status`, `git diff --stat`, and commit hash when available.
- Relevant task memory or plan files.
- `docs/obsidian/templates/codex-session-summary-template.md`

## Steps

1. Create `exports/obsidian/product-notes/YYYY-MM-DD-codex-session-summary.md` or another more specific export path.
2. Summarize what Codex was asked to do.
3. Record what Codex changed, planned, verified, or could not complete.
4. List files touched or proposed at a high level.
5. Record decisions, risks, follow-up actions, and lessons.
6. Exclude raw logs and sensitive data.
7. Copy the note into the relevant Obsidian product, Agentic OS, or weekly review folder.

## Output File Location

Usually `exports/obsidian/product-notes/`. Use `exports/obsidian/lessons-learned/` when the main value is a durable lesson.

## Quality Checklist

- The note is readable without the full chat.
- It identifies the repo and session goal.
- It includes verification evidence if work was implemented.
- It names open risks.
- It does not duplicate a full PR summary or raw terminal output.

## What Not To Include

- Secrets or credentials.
- Raw command logs.
- Full diffs.
- Private customer data.
- Unsupported claims that work is done without verification.
