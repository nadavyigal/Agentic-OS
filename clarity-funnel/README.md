# Clarity Funnel

Session companion for AI chats. Helps everyday users feel the conversation is **staying on track** and getting **clearer over time** — not one-shot plans or copy-paste prompts.

## What it does

| Moment | Behavior |
|--------|----------|
| **Start** | Lock a north star + show funnel stage |
| **During** | Light certainty nudges every few replies |
| **Anytime** | `check` / `funnel` for a full funnel check |
| **End** | `wrap` recap |

Commands are for testing. The latched session also nudges automatically so it feels intuitive without memorizing keywords.

## Quick start

1. Copy this folder to a skills directory (see below).
2. Paste a messy ask or say you're unsure the chat is helping.
3. Invoke **clarity-funnel** (or say `funnel` / `check`).
4. Keep chatting; say `check` when uncertain, `wrap` when done.

## Demo script (3 acts)

**Input:**

```text
Help me create a strategy for my team to start using AI better at work. We tried a few tools but people are confused and I want a clear plan.
```

1. **START** — north star + funnel stage (no full plan)
2. Chat 2–3 turns → **CHECK** (clearer / fuzzy / on track)
3. **WRAP** — what's clear + one real-world next step

Frozen walkthrough: `templates/everyday-team-ai-strategy.md`

## Install by host

| Host | Path |
|------|------|
| Cursor (personal) | `~/.cursor/skills/clarity-funnel/` |
| Cursor (project) | `.cursor/skills/clarity-funnel/` in repo root |
| Claude Code | `~/.claude/skills/clarity-funnel/` |

Required files:

```text
clarity-funnel/
  SKILL.md
  profiles/everyday.md
  profiles/builder.md
  templates/          # frozen demo walkthrough (optional)
```

## QR landing page

```bash
open clarity-funnel/landing/index.html
```

Host `landing/` for hackathon QR. Tabs: Everyday vs Builder.

## Profiles

| Profile | Read |
|---------|------|
| Everyday | `profiles/everyday.md` |
| Builder | `profiles/builder.md` |

Default everyday unless user mentions agents, Cursor, scope, or work packets.

## Relation to office-hours

Office-hours diagnoses *whether* to build. Clarity Funnel orients *this chat* while it evolves.

## Hackathon scope

- SKILL.md + two profiles
- Static landing + copy buttons
- One-shot opener for hosts without skill install

Deferred: analytics, MCP, profile marketplace.
