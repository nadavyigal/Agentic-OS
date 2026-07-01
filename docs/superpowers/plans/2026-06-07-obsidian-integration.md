# 2026-06-07 Obsidian Integration Plan

> **Status: verified already implemented, 2026-07-01.** All 4 acceptance criteria confirmed: `docs/obsidian/obsidian-setup-guide.md` exists, `docs/obsidian/templates/` has 7 templates, `docs/obsidian/workflows/` has 6 workflows (1,111 lines total across all three). The `Nadav Builder OS` vault named in this plan's Acceptance Criteria was created and has since grown its own more elaborate workflow set (`01-Agentic-OS/Workflows/` inside the vault itself) — this repo's `docs/obsidian/` is the seed spec, the vault is the living result. No action needed; not superseded, not a duplicate.

## Summary

Add Obsidian as the local-first human knowledge layer for Agentic OS. This is documentation and workflow setup only. Obsidian is not installed by agents, not synced automatically, and not used by product builds, CI, deployments, or runtime behavior.

## Implementation

- Create `docs/obsidian/obsidian-setup-guide.md` with manual setup instructions, vault structure, first notes, Canvas guidance, export rules, naming conventions, and safety rules.
- Add Obsidian-compatible templates under `docs/obsidian/templates/`.
- Add capture workflows under `docs/obsidian/workflows/` rather than creating a new `.agent-os/` layer.
- Add `exports/obsidian/` as a manual Markdown staging area with sample notes.

## Acceptance Criteria

- The setup guide tells Nadav how to install Obsidian and create the `Nadav Builder OS` vault manually.
- Every requested template exists.
- Every workflow includes purpose, when to run, inputs, steps, output location, quality checklist, and what not to include.
- Export staging folders exist and make clear they are not sync or secure storage.
- Sample notes contain sample-only content.

## Safety Rules

- Do not include secrets, API keys, credentials, tokens, private customer data, raw resumes, raw logs, build artifacts, or production data.
- Do not modify production app repos or behavior.
- Do not create sync config, scripts, dependencies, plugins, or external service connections in v1.

## Validation

- Run `git diff --check`.
- Confirm the requested files exist.
- Run `./agentic-os morning` if safe so the saved plan can surface through the existing dashboard flow.
