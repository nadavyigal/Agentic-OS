# Frozen demo output — Builder profile

**Input:**

> Help me create a strategy for my team to start using AI better at work. We tried a few tools but people are confused and I want a clear plan.

---

## CLARIFY

| Field | Value |
|-------|--------|
| **Goal** | Ship a 30-day team AI adoption plan one page long, with one canonical workflow and tool rules. |
| **Not in scope** | Tool procurement, LMS, AI committee, custom integrations, company-wide transformation |
| **Validation** | Plan has: goal sentence, 1 workflow, ≤3 tools, 4-week bullets, 3 success signals, manager script ≤5 sentences |
| **Assumptions** | Mixed skill team; confusion is tool/overchoice, not hostility |

---

## PROMPT (copy this)

```text
MODE: Planning only. Do not propose building software or buying tools.

GOAL:
Produce a one-page 30-day team AI adoption plan with one canonical workflow.

TASK:
Write the plan document only. No implementation, no new tools, no policy program beyond 5 team rules.

CONSTRAINTS:
- Max 400 words unless user asks for detail
- Plain language
- No "digital transformation" framing
- Max 3 tools in tool map

VALIDATION:
- GOAL is exactly one sentence
- Exactly one CANONICAL WORKFLOW (5 steps max)
- WEEK-BY-WEEK covers W1–W4 only
- MANAGER LAUNCH SCRIPT is 5 sentences or fewer

REQUIRED OUTPUT SECTIONS:
- GOAL (1 sentence)
- DIAGNOSIS (3 bullets: why confusion happens)
- CANONICAL WORKFLOW (1 workflow, 5 steps max)
- TOOL MAP (table: task → tool → when not to use)
- 30-DAY ROLLOUT (W1–W4, 3 bullets/week max)
- TEAM RULES (5 bullets: privacy, verification, quality bar)
- SUCCESS SIGNALS (3 observable, week-4 check)
- MANAGER LAUNCH SCRIPT (5 sentences)

ASK FIRST (max 2 questions, then proceed with stated assumptions if unanswered):
1) Team size and roles (rough)?
2) Top 2 weekly tasks to target with AI?
```

*SCOPE LOCK: one-page 30-day team AI adoption plan. If the session drifts to "build an internal AI platform," STOP and restate goal + validation before continuing.*

---

## FINISH

**Work packet**
- Status: Ready to run in next chat after 2 clarifying answers
- Done when:
  - [ ] One-page plan exists
  - [ ] Exactly one workflow named
  - [ ] ≤3 tools in tool map
  - [ ] Manager script copied to team channel

**Next action**  
Paste PROMPT above into chat; answer 2 questions; save output against FINISH checklist.

**Session handoff**  
If chat drifts to "build an internal AI platform" or tool procurement, paste: *SCOPE LOCK: planning artifact only — one-page 30-day adoption plan.*

**Files / checks**
- Files touched: none (planning only)
- Checks run: pending (user saves plan doc)
