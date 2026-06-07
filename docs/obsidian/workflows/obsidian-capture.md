# Obsidian Capture Workflow

## Purpose

Capture useful Agentic OS knowledge as Obsidian-friendly Markdown without making Obsidian a source of truth or production dependency.

## When To Run It

- After a meaningful planning session.
- After a founder strategy conversation.
- After a decision, review, research pass, or reusable prompt is created.
- When a Codex, Claude, or ChatGPT session produces durable knowledge worth reading later.

## Inputs

- The session summary or artifact being captured.
- Relevant Agentic OS source files.
- Relevant product repo source files, if the note is product-specific.
- The matching template from `docs/obsidian/templates/`.

## Steps

1. Identify the note type: decision, weekly review, research, product note, prompt, lesson, or session summary.
2. Choose the matching template.
3. Create a Markdown file under the matching `exports/obsidian/` subfolder.
4. Use the naming pattern `YYYY-MM-DD-topic-name.md`.
5. Summarize the useful knowledge, preserving links to source files where helpful.
6. Remove secrets, raw logs, sensitive client details, and production data.
7. Manually copy the note into the Obsidian vault.

## Output File Location

Use one of:

- `exports/obsidian/decisions/`
- `exports/obsidian/weekly-reviews/`
- `exports/obsidian/research/`
- `exports/obsidian/prompts/`
- `exports/obsidian/product-notes/`
- `exports/obsidian/lessons-learned/`

## Quality Checklist

- The note is useful to a human reader.
- The note says where the information came from.
- The note uses plain Markdown.
- The note uses simple tags only when useful.
- The note links related topics with wiki links where helpful.
- The note does not claim current product status without fresh source evidence.

## What Not To Include

- API keys, credentials, secrets, or tokens.
- Raw private resumes or sensitive client details unless intentionally protected.
- Full raw logs.
- Build artifacts.
- Large generated files.
- Production data.
- Anything that belongs only in GitHub, Supabase, Vercel, app storage, or CI.
