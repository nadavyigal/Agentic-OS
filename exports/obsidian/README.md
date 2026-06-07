# Obsidian Export Staging

This folder is a manual staging area for Obsidian-friendly Markdown.

Files here can be copied into the Obsidian vault `Nadav Builder OS`. This folder is not a sync folder, not a production dependency, and not a secure storage location.

## Folders

- `decisions/` for decision notes.
- `weekly-reviews/` for weekly review notes.
- `research/` for research summaries.
- `prompts/` for reusable prompt notes.
- `product-notes/` for product strategy, roadmap, session, and planning notes.
- `lessons-learned/` for reusable lessons.
- `sample-notes/` for sample-only examples.

## Naming

Use:

```txt
YYYY-MM-DD-topic-name.md
```

Examples:

```txt
2026-06-07-runsmart-weekly-review.md
2026-06-07-resumebuilder-upload-pipeline-note.md
2026-06-07-agentic-os-obsidian-decision.md
```

## Manual Copy Flow

1. Create the export note in the relevant folder.
2. Run a quick safety review.
3. Copy the note into the matching Obsidian vault folder.
4. Keep source-of-truth implementation docs in the relevant GitHub repo.

## Safety Review

Do not export:

- API keys, credentials, secrets, or tokens.
- Raw private resumes or sensitive client details unless intentionally protected.
- Full raw logs.
- Build artifacts.
- Large generated files.
- Production data.
- Anything that belongs only in GitHub, Supabase, Vercel, app storage, or CI.
