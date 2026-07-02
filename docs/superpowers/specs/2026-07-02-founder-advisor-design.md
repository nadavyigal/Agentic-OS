# Founder Advisor — Design

- **Date:** 2026-07-02
- **Status:** Approved design; implementation plan pending
- **Owner:** Nadav (solo founder)
- **Related:** `ORCHESTRATION-GATE.md`, `DAILY.md`, `GLOBAL-WORKFLOWS.md`, `AGENTS.md` (Mode Contracts), vault advisors (Storm, High-Agency, Red Team)

## Problem

Every session, a raw prompt gets routed by hand: the founder mentally decides
whether it needs *thinking* (advisors), *classifying* into the OS (Tier / Mode /
Pattern), or *executing* (which work packet, workflow, decision, or plan to
progress). This is the undefined "→ someone" arrow in the founder's original OS
sketch. `ORCHESTRATION-GATE.md` filled part of it (classification of actionable
work). It does not cover the thinking layer, and it does not read live OS state to
say what to *progress* next.

The Founder Advisor is the fully-specified front door: one entry point that
classifies a raw prompt and hands back a ready-to-fire next step.

## Goal

A single command — `/founder <prompt>` — that:

1. Classifies the prompt into exactly one of two paths: **Think** or **Act**.
2. States why in one sentence.
3. Ends with a copy-ready launch block so starting the next step is one action.

**Recommend-only.** It never invokes an advisor, opens a file, or runs a workflow
itself. It produces a verdict plus a paste-ready block. Initiation is the
founder's next action. This keeps it identical across Claude Code, Codex, and
Cursor.

## Non-Goals

- No auto-execution of any path (explicitly rejected in design).
- No new taxonomy: it composes existing tables (`ORCHESTRATION-GATE.md` Tiers/
  Modes/Patterns, vault advisors, `GLOBAL-WORKFLOWS.md`). It invents nothing.
- Not building the Red Team advisor prompt (was unbuilt at design time; built
  separately in vault PR #14, 2026-07-02, and now referenced as real — see
  Open Items).
- Not a replacement for `DAILY.md`, `ORCHESTRATION-GATE.md`, or the advisors — it
  is the layer above them that decides which one the prompt needs.

## Architecture

The Founder Advisor is a classifier / dispatcher, not a pipeline. Most prompts
need one path; it picks that one.

```
/founder <prompt>
        │
        ▼
   [ classify ]
     │      │
  Think     Act
     │      │
     │      └─ run through ORCHESTRATION-GATE.md → Tier · Mode · Pattern · Route
     │         then read live OS state → what to run / progress
     │         then emit paste-ready block
     │
     └─ pick advisor (Storm / High-Agency / Red Team)
        then emit paste-ready advisor prompt
```

### Home & distribution

- **Canonical file:** `Agentic OS/FOUNDER-ADVISOR.md` — git-versioned, the single
  source of truth. Root level, consistent with `ORCHESTRATION-GATE.md`.
- **Global trigger:** `~/.claude/commands/founder.md` is a **symlink** to the
  canonical file, so `/founder <prompt>` works in every Claude Code session, any
  repo, while the real file stays in git. This resolves the availability-vs-
  durability tension (`~/.claude` is not a git repo).
- **Codex / Cursor:** the canonical file's body is tool-agnostic prose. Paste it
  as task/chat context and append the prompt. No Claude-Code-specific syntax in
  the body.

## Components

### 1. Classifier

Decides Think vs Act from signals in the prompt.

**→ Think** when the prompt is:
- A question seeking a view ("should I…", "is it worth…", "what do I think…",
  "which is better…").
- A fuzzy or large idea with no clear first action.
- A decision between options.
- A request for critique, challenge, or a strategic POV.
- Something recurring or already circled before (rumination signal).

**→ Act** when the prompt:
- Names or implies concrete work to do.
- Asks "what should I do / progress next."
- References a product, repo, feature, bug, work packet, plan, decision, or
  workflow to move.
- Is anything not clearly a Think prompt. **Act is the default when unclear**,
  because the gate underneath Act has its own safe default (Tier 1 · Builder ·
  normal).

### 2. Think path

Selects one advisor and emits a paste-ready prompt with the founder's question
already framed.

Advisor selection:
- **Storm** — needs breadth / multiple perspectives / research synthesis. Source:
  vault `04-Prompts/Claude/storm-project-system-prompt.md` +
  `storm-multi-perspective-research.md`.
- **High-Agency Advisor** — needs a bias-to-action / anti-rumination challenge
  ("is this Level 0 or Level 1?"). Source: the vault's `/advisor` command
  (project-scoped to the Nadav Builder OS vault repo) and vault
  `04-Prompts/Claude/high-agency-advisor.md`.
- **Red Team** — needs adversarial stress-testing of a plan/launch/pitch/
  feature/hire/decision before committing to it. Built 2026-07-02 (vault PR
  #14): the vault's `/red-team` command (project-scoped, same pattern as
  `/advisor`) and vault `04-Prompts/Claude/cia-red-team-stress-test.md` — 4
  phases (Key Assumptions Check, Pre-Mortem, Hostile Competitor, 1-Star
  Review) adapted from the CIA Tradecraft Primer.

Output contract:

```
VERDICT: Think — <one-sentence why>
Advisor: <Storm | High-Agency | Red Team>

<paste-ready advisor prompt, with the framed question inlined>
```

### 3. Act path (state-aware)

Procedure when Act is chosen:

1. Run the prompt through `ORCHESTRATION-GATE.md` → produce
   `GATE: Tier <n> · Mode <name> · Pattern <name> · Route <file>`.
2. Read **only the state relevant to the classification** (do not read
   everything every time):
   - `executive-os/EXECUTIVE-DECISIONS.md` — any open decision this prompt
     touches or would progress.
   - Active plans / saved plans board — any plan whose next milestone this
     advances.
   - `executive-os/work-packets/` — a matching or next work packet.
   - `GLOBAL-WORKFLOWS.md` — the workflow / pattern to apply.
   - `DAILY.md` — the Tier.
3. Synthesize: what to run, and what in-flight work to progress.
4. Emit the paste-ready block: exact repo + command or work packet.

Output contract:

```
VERDICT: Act — <one-sentence why>
GATE: Tier <n> · Mode <name> · Pattern <name> · Route <file>
Progress: <open decision / plan milestone / WP this advances, or "none in flight">

<paste-ready block: exact repo path + command or work-packet text>
```

## Ambiguity & Failure Handling

- **Both paths fit** → recommend the first relevant path (usually Think, since
  thinking precedes doing), and name the likely next path in one line. Honors
  "one path at a time."
- **Low confidence** → say so explicitly and show the top-2 paths, each with its
  own block, so the founder picks.
- **Default when unclear** → Act (its gate has a safe default).
- **Cannot read a state file** (wrong repo, missing access) → degrade
  gracefully: still give the classification and a generic route, and state which
  state files could not be read. Never fabricate decision/plan/WP status.

## Testing / Validation

Since this is a prose command (not code), validation is by worked examples. The
spec is correct if, for each example prompt below, the advisor produces the
expected path and a block that is genuinely one-action-to-start:

1. "Should I keep building the Garmin reconnect flow or park it?" → **Think**
   (decision) → High-Agency advisor block.
2. "Give me five angles on the Resumely pricing page." → **Think** (breadth) →
   Storm block.
3. "Fix the voice-cue endpoint dirty tree in RunSmart web." → **Act** → gate
   line (Tier 1 · Builder · normal) + RunSmart web repo + paste-ready packet.
4. "What should I progress this week?" → **Act** → reads decisions/plans/WPs →
   recommends the next milestone + paste-ready packet.
5. "Poke holes in my plan to file two Garmin portal apps." → **Think** (Red Team)
   → recommend Red Team, paste-ready `/red-team` prompt.
6. A vague one-liner with no clear signal → **Act** (default) → gate default
   (Tier 1 · Builder · normal) + note low confidence.

## Open Items (out of scope for this spec)

- ~~Build the Red Team advisor prompt as a real file~~ — done, vault PR #14
  (2026-07-02): `.claude/commands/red-team.md` + vault
  `04-Prompts/Claude/cia-red-team-stress-test.md`. Built independently of
  this spec's timeline; Founder Advisor updated to reference it as real.
- Decide whether `/founder` should later gain an opt-in act-on-confirm mode
  (explicitly deferred; recommend-only for now).
