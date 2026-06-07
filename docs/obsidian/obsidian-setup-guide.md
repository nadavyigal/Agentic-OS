# Obsidian Setup Guide

Obsidian is the human-facing knowledge layer for Agentic OS. It is for founder memory, product thinking, strategy, research, decisions, prompts, reviews, and session summaries.

GitHub repos remain the source of truth for product code and implementation docs. Agentic OS remains the execution and orchestration layer. Obsidian is not required for builds, CI, runtime behavior, deployments, credentials, or app data.

## Install Obsidian

1. Go to https://obsidian.md/.
2. Download the desktop app for macOS.
3. Install it locally.
4. Open Obsidian and choose `Create new vault`.
5. Suggested vault name: `Nadav Builder OS`.
6. Suggested local location: `~/Documents/Nadav-Builder-OS`.
7. If you prefer another local folder, choose one that is easy to find and not inside a product repo.

Do not install plugins, configure sync, or connect external services during the first setup pass.

## Initial Settings

Start simple:

- Use plain Markdown files.
- Keep the vault local-first.
- Avoid community plugins at the beginning.
- Enable backlinks if they are not already visible.
- Use the core graph view when you want to see relationships.
- Use Canvas for system maps and product maps.
- Do not set up complex sync unless there is a clear need.
- Treat Obsidian as a knowledge base, not a secure vault.

## Vault Structure

Create this folder structure inside the Obsidian vault:

```txt
00-Inbox/
01-Agentic-OS/
  Maps/
  Workflows/
  System-Notes/
02-Products/
  RunSmart/
    Strategy/
    Roadmap/
    Decisions/
    Research/
    Prompts/
  ResumeBuilder/
    Strategy/
    Roadmap/
    Decisions/
    Research/
    Prompts/
  AI-Audit-Toolkit/
    Strategy/
    Roadmap/
    Decisions/
    Research/
    Client-Work/
    Prompts/
03-Research/
  AI-Tools/
  Competitors/
  Market-Trends/
  GitHub-Repos/
04-Prompts/
  Codex/
  Claude/
  ChatGPT/
  Reusable/
05-Decisions/
06-Clients/
07-Weekly-Reviews/
08-Lessons-Learned/
09-Templates/
10-Archive/
```

## First Notes

Create these starter notes. Keep them short on day one. The goal is a useful map, not a finished encyclopedia.

### Home.md

Suggested location: vault root.

```md
# Nadav Builder OS

This vault is the human-readable knowledge layer for my products, Agentic OS, research, decisions, prompts, and weekly reviews.

## Start here

- [[Agentic OS Map]]
- [[Current Priorities]]
- [[Product Portfolio]]
- [[Decision Log]]
- [[Prompt Library]]
- [[Research Inbox]]
- [[Weekly Review]]
- [[Lessons Learned]]

## Current focus

- RunSmart
- ResumeBuilder / Resumely
- Agentic OS
- AI Audit Toolkit
```

### Agentic OS Map.md

Suggested location: `01-Agentic-OS/Maps/`.

```md
# Agentic OS Map

## Role

Agentic OS coordinates cross-project planning, standards, prompts, workflows, dashboards, and reusable agent behavior.

## Core layers

- [[Global Agentic OS]]
- [[RunSmart]]
- [[ResumeBuilder]]
- [[AI Audit Toolkit]]
- [[CEO OS]]
- [[CFO OS]]
- [[Analysis OS]]
- [[Codex]]
- [[Claude]]
- [[ChatGPT]]
- [[GitHub]]
- [[Obsidian]]

## Source of truth

- Product implementation lives in GitHub repos.
- Orchestration lives in Agentic OS.
- Human-readable thinking lives in Obsidian.
```

### Current Priorities.md

Suggested location: vault root or `01-Agentic-OS/System-Notes/`.

```md
# Current Priorities

Date:

## This week

1.
2.
3.

## Product focus

- [[RunSmart]]:
- [[ResumeBuilder]]:
- [[AI Audit Toolkit]]:

## Decisions needed

-

## Risks to watch

-
```

### Weekly Review.md

Suggested location: `07-Weekly-Reviews/`.

```md
# Weekly Review

Week of:

## Summary

## What moved forward

## What is blocked

## Key decisions

## Lessons learned

## Next week priorities

## Risks to watch

## Links
```

### Decision Log.md

Suggested location: `05-Decisions/`.

```md
# Decision Log

Use this note as the human-readable index. Durable cross-project architectural decisions still belong in Agentic OS `DECISIONS.md`.

## Accepted

-

## Proposed

-

## Revisit

-
```

### Prompt Library.md

Suggested location: `04-Prompts/`.

```md
# Prompt Library

## Codex

-

## Claude

-

## ChatGPT

-

## Reusable

-
```

### Product Portfolio.md

Suggested location: `02-Products/`.

```md
# Product Portfolio

## Active products

- [[RunSmart]]
- [[ResumeBuilder]]
- [[AI Audit Toolkit]]

## Operating systems

- [[Agentic OS]]
- [[CEO OS]]
- [[CFO OS]]
- [[Analysis OS]]

## Notes

Use Agentic OS and product repos for source-of-truth status. Use this note for human-readable orientation.
```

### Research Inbox.md

Suggested location: `03-Research/`.

```md
# Research Inbox

Capture research quickly here, then promote useful notes into project or topic folders.

## Inbox

-

## To synthesize

-

## Archived or rejected

-
```

### Lessons Learned.md

Suggested location: `08-Lessons-Learned/`.

```md
# Lessons Learned

Use this for human-readable lessons. Repeated, expensive, or easy-to-forget operating lessons should also be recorded in the relevant Agentic OS lesson file.

## Product

-

## Agent workflow

-

## Founder workflow

-
```

## First Canvas

Create an Obsidian Canvas named:

```txt
Agentic OS Map.canvas
```

Suggested location: `01-Agentic-OS/Maps/`.

Create one node for each item:

- Global Agentic OS
- RunSmart
- ResumeBuilder
- AI Audit Toolkit
- CFO OS
- CEO OS
- Analysis OS
- Codex
- Claude
- ChatGPT
- GitHub
- MarkItDown
- Webwright
- Hermes Agent
- Obsidian

Suggested connections:

```txt
Global Agentic OS -> RunSmart
Global Agentic OS -> ResumeBuilder
Global Agentic OS -> AI Audit Toolkit
Global Agentic OS -> CFO OS
Global Agentic OS -> CEO OS
Global Agentic OS -> Analysis OS
Global Agentic OS -> Codex
Global Agentic OS -> Claude
Global Agentic OS -> ChatGPT
Codex -> GitHub
Claude -> GitHub
ChatGPT -> Obsidian
Agentic OS -> Obsidian
MarkItDown -> Research
Webwright -> Research
Hermes Agent -> Automation candidates
```

Use the Canvas as a map of relationships, not as a source of truth.

## Agentic OS Export Flow

Agentic OS exports Obsidian-friendly Markdown into `exports/obsidian/`. These files are staging files that can be manually copied into the Obsidian vault.

Export:

- Decisions
- Weekly reviews
- Product strategy notes
- Research summaries
- Competitor notes
- Prompt templates
- Lessons learned
- Codex session summaries
- Claude session summaries
- AI Audit Toolkit client notes, when intentionally summarized
- Roadmap updates
- Risk reviews

Do not export:

- API keys, credentials, secrets, or tokens
- Raw private resumes or sensitive client details unless intentionally protected
- Full raw logs
- Build artifacts
- Large generated files
- Production data
- Anything that belongs only in GitHub, Supabase, Vercel, app storage, or CI

## Naming And Linking

Use this file naming pattern:

```txt
YYYY-MM-DD-topic-name.md
```

Examples:

```txt
2026-06-07-markitdown-webwright-decision.md
2026-06-07-runsmart-weekly-review.md
2026-06-07-resumebuilder-upload-pipeline-note.md
```

Use simple tags:

```txt
#agentic-os
#runsmart
#resumebuilder
#audit-toolkit
#decision
#research
#prompt
#weekly-review
#lesson
#risk
```

Use Obsidian wiki links where helpful:

```txt
[[RunSmart]]
[[ResumeBuilder]]
[[AI Audit Toolkit]]
[[Agentic OS]]
[[Decision Log]]
[[Prompt Library]]
```

## Obsidian Safety Rules

- Do not store API keys.
- Do not store customer secrets.
- Do not store raw private resumes unless intentionally needed and protected.
- Do not store sensitive client details in general research notes.
- Prefer summaries over raw logs.
- Keep production credentials outside Obsidian.
- Be careful with sync providers.
- Treat Obsidian as a knowledge base, not a secure vault.

## Adoption Phases

### Phase 0: Manual Setup

- Install Obsidian.
- Create the `Nadav Builder OS` vault.
- Create folders.
- Create the first `Home.md` note.
- Create `Agentic OS Map.canvas` manually.

### Phase 1: Repo Documentation

- Add this setup guide.
- Add Obsidian templates.
- Add Agentic OS workflow docs.
- Add the `exports/obsidian/` staging structure.

### Phase 2: Manual Export Workflow

- After important Codex sessions, create a session summary Markdown file.
- After decisions, create a decision note.
- After research, create a research note.
- Manually copy useful notes into Obsidian.

### Phase 3: Semi-Automated Export

- Optional future script that creates notes from templates.
- Optional command to generate weekly review notes.
- Optional command to summarize lessons learned.

### Phase 4: Advanced Integration

- Consider a Git-backed Obsidian vault.
- Consider Obsidian Sync or another sync method.
- Consider controlled automation.
- Consider connecting Hermes Agent or another sidecar later.
