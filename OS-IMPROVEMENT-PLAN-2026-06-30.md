# OS Improvement Plan — 2026-06-30

Derived from backfilling 28 sessions into INTENT-LOG.md (2026-06-08 through 2026-06-30).
The signal is the recurring themes across sessions, not any single incident.

---

## What the patterns say

After reading 28 sessions, five themes recur so often they are structural problems, not one-offs.

| Theme | Count | What it means |
|---|---|---|
| trust / verifiability / status-truth | 8 entries | Claude keeps stating status from memory; OS state diverges from reality |
| automation vs manual | 7 entries | Every manual practice dies silently; only automated things survive |
| evidence-before-commit | 6 entries | "Done" is declared without proof; QA and evals come after, not before |
| ask instead of act | 5 entries | Claude converts clear instructions into questions |
| compounding vs accreting | 4 entries | New files are created instead of updating the canonical living page |

---

## Problem 1: Status from memory

**Pattern:** Claude states "RunSmart is at v1.0.3" or "both apps are in review" without verifying.
The OS says one thing; git, PostHog, and App Store say another. This happened in at least 8 sessions.

**Root cause:** No hard rule forcing a live source check before any status claim.

**Changes:**

1. Add to `LESSONS.md`:
   > **Never state product status from memory.** Always verify from a live source (git tag, PostHog, Agentic OS refresh output). State the source and date inline: "As of git tag v1.0.4 pushed 2026-06-24, RunSmart iOS is at..." If no live source is available, say so explicitly.

2. Add to `~/.claude/ERRORS.md`:
   > **2026-06-30 — Stating status from memory across multiple sessions**
   > Tried: reading status from progress.md, vault hub notes, or recalling from prior session context.
   > Worked: running `git describe --tags` or `./agentic-os refresh` and citing the output.
   > Next time: status claim = live source check first, always.

3. Add to `GLOBAL-SELF-IMPROVEMENT.md`: a "Status Truth" rule — before any status is stated, the agent must cite a live source, not a file that was last updated by a human.

---

## Problem 2: Manual practices die silently

**Pattern:** The Stop hook disappeared. The launchd refresh exited 126 silently. The INTENT-LOG
went 28 days without an entry. Every manual ritual failed. Every automated thing survived.

**Root cause:** New practices are introduced without deciding upfront whether they need automation.
The default is "someone will remember to do it" — this always fails.

**Changes:**

1. Add to `GLOBAL-SELF-IMPROVEMENT.md`:
   > **Automation gate:** When introducing any new recurring practice, ask before shipping it:
   > "Will this survive if nobody thinks about it for 30 days?" If no: wire it into a hook,
   > cron, or existing daily ritual on day 1. A practice that requires human memory is not a practice.

2. The INTENT-LOG itself: auto-capture via Stop hook is WP-22 (see bottom of this file).

3. Add a hook health check to the morning brief: if `~/.claude/settings.json` Stop hook is absent
   or `lastExit` on `com.nadav.agentic-os-refresh` is non-zero, surface it before any other briefing.

---

## Problem 3: Done declared without evidence

**Pattern:** Sessions end with "done" before lint passes, tests run, or the PR is open.
The eval harnesses, D7 readouts, and PostHog QA all came after decisions had already been made
based on unverified claims.

**Root cause:** The verification rule exists in `~/.claude/CLAUDE.md` but is not enforced at
session end — the Stop hook does not check for it.

**Changes:**

1. Stop hook prompt (when implemented) should include: "Before writing the INTENT-LOG entry,
   state: files changed, lint status, test status, PR open or branch+commit count. If any are
   unknown, say unknown — do not omit."

2. Add to `LESSONS.md`:
   > **Done requires evidence, not completion.** "The feature works" is not evidence. Lint pass,
   > test output, or a PostHog event confirmed in the dashboard is evidence. Log the evidence
   > in the INTENT-LOG entry or the session summary.

3. Update `GLOBAL-QA-RULES.md` to add: for any AI-facing feature, a PostHog event confirmed
   in the dashboard (or a test asserting it fires) is required before closing the story.

---

## Problem 4: Asking instead of acting

**Pattern:** Clear instructions converted into questions. "Spec this out" → "Want me to spec
this out?" "Create a plan" → "Should I create a plan?" This added friction and frustrated the
founder in at least 5 sessions.

**Root cause:** No clear rule distinguishing when to ask vs. when to act. The conservative
default is to ask; the correct default for instructions is to act.

**Changes:**

1. Add to `~/.claude/CLAUDE.md` (Global Work Rules):
   > **Instruction vs question:** If the user's message contains a verb + object ("create X",
   > "spec out Y", "add Z", "fix W"), execute it. Do not convert it into a question. Reserve
   > questions for genuine ambiguity where two different interpretations would produce
   > meaningfully different outputs.

2. Add to `~/.claude/ERRORS.md`:
   > **2026-06-30 — Converting instructions into questions**
   > Tried: "Want me to create the plan?" after the user said "create a plan to implement fully."
   > Worked: Just creating the plan.
   > Next time: A sentence with a verb ("create", "implement", "spec", "add") is an instruction.
   > Execute, do not ask.

---

## Problem 5: Accreting instead of compounding

**Pattern:** Sessions create new dated notes instead of updating the living page. Hub notes
go stale within days. The wiki-index drifts from reality. Decisions get written into dated
notes but not propagated to DECISIONS.md.

**Root cause:** The default action is "create a new note for this session" — it requires no
judgment. Updating an existing page requires finding it, reading it, and deciding what to
change. The lazy path is always accretion.

**Changes:**

1. Already partially fixed: vault CLAUDE.md has a living-pages rule (added 2026-06-27).
   Generalize it to all repos: add to `GLOBAL-SELF-IMPROVEMENT.md`:
   > **Compound, don't accrete.** Before creating a new file, ask: does a living page for this
   > subject already exist? If yes, update it and use the new content as evidence in the dated
   > note. Never let a hub note go more than 7 days without reflecting reality.

2. Add to `GLOBAL-WORKFLOWS.md` under Post-Session checklist:
   - Did any living page's `Current State` block become stale? If yes, update it now.
   - Did any decision get written to a dated note but not to `DECISIONS.md`? If yes, mirror it.

---

## What Nadav should do differently (minimal list)

Most of the above is agent-side. One founder-side change that would have prevented the most pain:

> **When a practice is introduced, immediately ask: "Is this automated?"**
> If the answer is no, and it's expected to run more than once, require automation before
> accepting it. The INTENT-LOG, the Stop hook, the launchd job, and the learning loop all
> failed for the same reason: they were introduced as manual practices.

---

## Immediate action queue (execute in order)

| # | Action | File | Session |
|---|---|---|---|
| 1 | Add "never state status from memory" to LESSONS.md | `LESSONS.md` | Now |
| 2 | Add "instruction vs question" rule to global CLAUDE.md | `~/.claude/CLAUDE.md` | Now |
| 3 | Add "asking instead of acting" to ERRORS.md | `~/.claude/ERRORS.md` | Now |
| 4 | Add automation gate to GLOBAL-SELF-IMPROVEMENT.md | `GLOBAL-SELF-IMPROVEMENT.md` | Now |
| 5 | Build Stop hook INTENT-LOG auto-capture | `~/.claude/settings.json` + script | WP-22 (next session) |
| 6 | Add hook health check to morning brief | `PROMPTS/morning-brief.md` | WP-22 |
| 7 | Implement PostHog LLM observability in ResumeBuilder | ResumeBuilder repo | WP-21 (Codex session) |

---

## WP-22 — Intent capture automation (placeholder)

To be specced when WP-21 is done. Scope:
- Stop hook writes one INTENT-LOG entry per session (paraphrased request, intent/why, 2-3 theme tags)
- `scripts/agentic_os/intent_cluster.py` — counts theme tags monthly, appends cluster section
- Morning brief pulls top 3 themes from latest cluster
- Hook health check added to morning brief startup
