# Decision: Sample Obsidian Export Flow

Date: 2026-06-07
Project: Agentic OS
Status: Sample
Owner: Nadav

## Decision

Use `exports/obsidian/` as a manual staging area for Obsidian-friendly Markdown notes.

## Why Now

Agentic OS needs a human-readable knowledge layer that does not become a production dependency.

## Context

Product repos remain the implementation source of truth. Agentic OS remains the orchestration layer. Obsidian becomes the local-first founder knowledge base.

## Options Considered

- Manual export staging.
- Automatic sync.
- Keeping all knowledge only in repo docs.

## Recommendation

Start with manual export staging. Add automation only after the manual workflow proves useful.

## Risks

- Notes may drift from source-of-truth files.
- Sensitive data could be copied by mistake.

## Mitigations

- Keep notes clearly linked to source files.
- Run a safety review before copying notes into Obsidian.

## Next Actions

- Create the Obsidian vault manually.
- Copy useful sample notes into the vault.

## Links

- [[Agentic OS]]
- [[Decision Log]]
