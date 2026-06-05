---
name: clarity-funnel
description: >-
  Guided AI work skill that turns messy chats and vague plans into clear goals,
  usable deliverables, aligned sessions, and finished outcomes in one session.
  Use when the user pastes a drifting chat, bloated plan, vague idea, or asks
  to clarify goals, improve prompts, keep AI on track, review an AI answer, or
  get a usable result from planning or building with AI. Supports everyday and
  builder profiles.
disable-model-invocation: true
---

# Clarity Funnel

Clarity Funnel controls natural expansion in AI conversations. It turns vague ideas, bloated plans, and drifting chats into focused goals, smaller scopes, clear outputs, prioritized actions, and finished results — **in the same chat**.

**Not office-hours.** Office-hours diagnoses whether to build a startup. Clarity Funnel gets the user what they meant out of **this** chat.

## When to use

- Messy paste: vague ask, strategy creep, tool confusion, plan bloat, scope drift
- User wants: clearer goal, better structure, aligned session, answer review, usable outcome
- Demo or everyday: one paste should yield a complete, designed-looking answer

## Profile selection

| Profile | For | Session |
|---------|-----|---------|
| **everyday** | Managers, non-technical users, any AI chat | **Single session** — deliver full plan in one reply |
| **builder** | Agents, Cursor, long plans, work packets | Single session deliverable + work packet tail |

Read before emitting: `profiles/everyday.md` or `profiles/builder.md`.

Default **everyday** unless user mentions agents, files, scope gates, or work packets.

Infer profile from query when possible; honor explicit "everyday" or "builder" if stated.

## Pipeline

### Everyday (default) — Clarity Card, not plan mode

```
1. SHRINK    (You said / You meant / We cut — always visible)
2. ALIGN     (silent)
3. REVIEW    (silent — if it sounds like a strategy deck, compress 50%)
4. DELIVER   (hero — short "Your answer", ~120 words unless expand)
5. TODAY     (one checkbox)
6. OFFER     (one line: reply expand / focus B / corrections)
```

**Do not** emit 8-section plans, week-by-week tables, or "rollout" language by default.

**Do not** tell the user to paste a prompt into a new chat.

If facts are missing: one-line assumptions under **We cut**, deliver anyway.

User says **expand** → add week-by-week bullets + rules (still no consultant template).

### Builder

```
1. CLARIFY   (goal table)
2. ALIGN + REVIEW (silent)
3. DELIVER   (artifact or plan doc)
4. FINISH    (work packet: done-when, next action, scope lock)
```

Optional `## Reuse prompt` appendix only when user asks to reuse in another tool.

## Hard rules

1. **Compress, don't educate.**
2. **Single session for everyday.** Hero = DELIVER, not a copy-prompt for later.
3. **Clarity Card layout.** You said / You meant / We cut / Your answer / Today. Bullets over wide tables. Not plan mode.
4. **Do not expand scope** beyond CLARIFY without naming the tradeoff.
5. Label assumptions; do not invent specifics silently.
6. If user pastes an AI reply for review: short REVIEW checklist, then revised DELIVER in same thread.

## Demo reference input

> Help me create a strategy for my team to start using AI better at work. We tried a few tools but people are confused and I want a clear plan.

Expected: one message with clarified goal table + full 30-day plan + checklist. No second chat.

## Demo templates

Frozen outputs: `templates/everyday-team-ai-strategy.md`, `templates/builder-team-ai-strategy.md`.

## Install

See `README.md`. QR landing: `landing/index.html`.
