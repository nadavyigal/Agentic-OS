# Clarity Funnel

Guided AI work skill for everyday users and power builders. Clarifies goals, improves prompts, keeps chats aligned, reviews answers, and turns messy conversations into usable outcomes.

**Hero moment:** copy-ready **PROMPT**. **Secondary:** **FINISH** checklist or work packet. **CLARIFY** is always first. **ALIGN** and **REVIEW** are embedded guardrails.

## Quick start

1. Copy this folder to a skills directory (see below).
2. Paste a messy chat, plan, or vague ask.
3. Invoke **clarity-funnel** (or use the one-shot opener on the landing page).
4. Copy **PROMPT** into your next AI chat; use **FINISH** to close the loop.

## Demo input

```text
Help me create a strategy for my team to start using AI better at work. We tried a few tools but people are confused and I want a clear plan.
```

Same input for **everyday** and **builder** profiles; outputs differ in tone and structure.

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
  templates/          # frozen demo outputs (optional)
```

## QR landing page

Open locally:

```bash
open clarity-funnel/landing/index.html
```

For hackathon/demo: host `landing/` on GitHub Pages or Vercel and point a QR code at that URL. Profile toggle: Everyday vs Builder on the same page.

## Pipeline

```text
CLARIFY → ALIGN (silent) → REVIEW (silent) → PROMPT → FINISH
```

## Profiles

| Profile | Read |
|---------|------|
| Everyday | `profiles/everyday.md` |
| Builder | `profiles/builder.md` |

Default to everyday unless the user mentions agents, Cursor, scope, or work packets.

## Relation to office-hours

[gstack office-hours](https://github.com) diagnoses *whether* to build (startup/design doc). Clarity Funnel runs across the chat lifecycle: clarify, prompt, align, review, finish. QR-installable, host-agnostic.

## Hackathon scope

Shipped in this folder:

- SKILL.md + two profiles
- Static landing + copy buttons
- One-shot opener for hosts without skill install

Deferred: live drift monitor, MCP, analytics, profile marketplace.

## Demo templates

See `templates/README.md`. Use when you need reliable hackathon output without a live model run.
