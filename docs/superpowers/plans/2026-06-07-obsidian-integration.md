# 2026-06-07 Obsidian Integration Plan

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
