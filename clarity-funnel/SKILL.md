---
name: clarity-funnel
description: >-
  Guided AI work skill that turns messy chats and vague plans into clear goals,
  copy-ready prompts, aligned sessions, and finished outcomes. Use when the user
  pastes a drifting chat, bloated plan, vague idea, or asks to clarify goals,
  improve prompts, keep AI on track, review an AI answer, or get a usable result
  from planning or building with AI. Supports everyday and builder profiles.
disable-model-invocation: true
---

# Clarity Funnel

Clarity Funnel controls natural expansion in AI conversations. It turns vague ideas, bloated plans, and drifting chats into focused goals, smaller scopes, clear prompts, prioritized actions, and finished outputs.

**Not office-hours.** Office-hours diagnoses whether to build a startup. Clarity Funnel gets the user what they meant out of **this** chat.

## When to use

- Messy paste: vague ask, strategy creep, tool confusion, plan bloat, scope drift
- User wants: clearer goal, better prompt, aligned session, answer review, usable outcome
- Before a long agent session (builder) or before the next ChatGPT turn (everyday)

## Profile selection

Ask once if unclear:

| Profile | For |
|---------|-----|
| **everyday** | Non-technical users, managers, anyone chatting or planning with AI |
| **builder** | Power users, agent sessions, long plans, work packets |

Read the active profile before emitting output:

- `profiles/everyday.md`
- `profiles/builder.md`

Default to **everyday** unless the user mentions agents, Cursor, scope gates, work packets, or multi-file implementation.

## Pipeline (mandatory order)

Do not skip steps. Do not emit PROMPT until CLARIFY and internal checks pass.

```
1. CLARIFY   (visible to user — always first)
2. ALIGN     (embedded guardrail — enforce silently)
3. REVIEW    (embedded guardrail — enforce silently)
4. PROMPT    (hero output — copy-ready for next chat turn)
5. FINISH    (secondary output — checklist, summary, artifact)
```

### Step 1 — CLARIFY (visible)

Per active profile:

1. Restate **what they actually want** in one sentence.
2. List **what this is not** (cut list, 3 bullets max).
3. If ambiguous, offer **2–3 focus options** (A/B/C) with a sensible default if they do not pick.

Stop and wait only if the input is empty or unintelligible.

### Step 2 — ALIGN (embedded, silent)

Before PROMPT, verify internally:

- Output stays tied to the one-sentence goal from CLARIFY.
- Scope fits the profile (everyday: one next chat; builder: stated constraints).
- No platform vision, tool shopping, or transformation language unless explicitly requested.

If fail: compress CLARIFY and re-run checks. Do not emit PROMPT yet.

**Builder only:** Apply scope budget from profile (planning artifact only unless user asked to implement).

### Step 3 — REVIEW (embedded, silent)

Before PROMPT, verify internally:

| Check | Question |
|-------|----------|
| Answers the ask? | Does the planned PROMPT address the clarified goal? |
| Small enough? | One chat turn or one bounded artifact, not a program? |
| One next step? | Can the user act Monday without reading a deck? |

If fail: narrow CLARIFY and re-run. Do not emit PROMPT yet.

### Step 4 — PROMPT (hero)

Emit a **single copy block** the user pastes into their next AI chat.

Requirements:

- Self-contained (no "use the skill above").
- Plain language for everyday; structured headers and constraints for builder.
- Include **alignment footer** (one line): stay focused on [goal]; if reply drifts, paste this line.
- Everyday: max 2 clarifying questions before delivering the main ask.
- Builder: GOAL, TASK, CONSTRAINTS, VALIDATION pattern where applicable.

Label clearly: `## PROMPT (copy this)`

### Step 5 — FINISH (secondary)

Emit a short **done package**:

- **Everyday:** at-a-glance summary, checkbox list (3–5 items), optional one-paragraph session summary to save.
- **Builder:** work packet tail (done when, next action, session handoff, drift stop line).

Label clearly: `## FINISH`

## Hard rules

1. **Compress, don't educate.** No lectures on prompting or agent architecture unless asked.
2. **Never emit PROMPT before CLARIFY** is one sentence and ALIGN/REVIEW pass.
3. **Do not expand scope** in PROMPT beyond CLARIFY without flagging tradeoff.
4. **Do not invent** team size, tools, or facts; state assumptions in PROMPT when missing.
5. If user pastes an AI reply for review, run REVIEW visibly (short checklist) then offer a **follow-up PROMPT** only.

## Demo reference input

Use for rehearsals and landing page examples:

> Help me create a strategy for my team to start using AI better at work. We tried a few tools but people are confused and I want a clear plan.

Expected shape: 30-day adoption plan, one workflow, tool rules, manager script (everyday); work packet + constrained planning PROMPT (builder).

## Demo templates

Frozen outputs for rehearsals: `templates/everyday-team-ai-strategy.md`, `templates/builder-team-ai-strategy.md`.

## Install

See `README.md` in this folder. QR landing: `landing/index.html`.
