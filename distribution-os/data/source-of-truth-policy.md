# Source Of Truth Policy

Different facts live in different places. When two places disagree, this policy decides who wins.

## The Layers

| Layer | Holds | Owner |
|---|---|---|
| Project repo (`runsmart` / `resumebuilder`) | Product facts, positioning, channels, project lessons | Product agent inside the repo |
| `distribution-os/` (this folder) | Cross-product strategy, workflows, prompts, templates, scoring | Distribution OS agent |
| `marketingskills/` | Marketing skill instructions | Upstream repo; pulled as-is |
| Google Drive | Documents, drafts, source material, exports, weekly reports | Founder + agent (writes drafts) |
| Notion | Planning and live status | Founder + agent (syncs status) |
| `~/.claude/` global files | User-level rules, memory, errors, learnings | Founder |

## Conflict Resolution

| Fact | Winner |
|---|---|
| Product positioning, audience definition | Project repo |
| Channel strategy per product | Project repo `.agent-os/distribution/channels.md` if present, otherwise `distribution-os/projects/{product}.md` |
| Cross-product workflows and prompts | `distribution-os/` |
| Marketing skill definitions | `marketingskills/` (do not fork inline) |
| Document drafts and exports | Drive |
| Live status of an experiment, campaign, asset | Notion |
| Hypothesis text and scoring | `experiment-log.md` (versioned source) |
| Lessons | The most specific scope wins; promote upward when generalized |
| Founder preferences | `~/.claude/CLAUDE.md` and `~/.claude/MEMORY.md` |

## What Agents Must Do

When starting a task that depends on a fact:

1. Read the lowest-numbered authoritative layer first
2. If two layers disagree, surface the conflict before acting
3. Update the authoritative layer; do not let a downstream copy silently drift
4. Reflect the change in any mirror copies

## What Agents Must Not Do

- Treat Drive or Notion as authoritative for product facts
- Treat `distribution-os/` as authoritative for what a product does
- Treat workflows here as immutable; they evolve via the lessons / monthly-strategy-review cycle
- Edit `marketingskills/` files inline (the repo is upstream)

## Mirror Files

Some files need to live in two places for the agent ecosystem to work:

- Product positioning → mirrored to `.agents/product-marketing.md` inside the project repo (so marketingskills can find it)
- Lessons promoted globally → mirrored to `~/.claude/LEARNINGS.md`
- Errors promoted globally → mirrored to `~/.claude/ERRORS.md`
- Decisions promoted globally → mirrored to `DECISIONS.md` at Agentic OS root

When a mirror exists, the authoritative side is named at the top of the file (`# Source: <path>`).

## Audit Tip

If a metric or fact ever feels wrong, run this loop:

1. Locate the fact in this policy
2. Pull the value from the authoritative source
3. If a downstream copy differs, update it
4. Add a lesson if the drift cost real time
