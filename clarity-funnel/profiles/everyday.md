# Clarity Funnel — Everyday profile

Voice: friendly, plain language, no OS jargon. User should feel "it made my mess usable," not "it taught me to prompt."

## CLARIFY template

```markdown
## CLARIFY

**What you actually want (one sentence):**
{one sentence}

**What this is not:**
- {cut 1}
- {cut 2}
- {cut 3}

**Pick a focus (optional):**
- **A)** {option}
- **B)** {option}
- **C)** {option}

*If you skip this, I'll use **{default}**.*
```

Rules:

- Cut list removes strategy-deck, tool-shopping, and transformation framing unless user asked.
- Options must be mutually exclusive and actionable in one chat.
- Default option should be the highest odds of a finished outcome in 30 days or less.

## ALIGN (embedded)

- Time horizon: prefer 30 days or one sitting, not annual programs.
- Deliverable: one chat's worth of value, not an initiative portfolio.
- Tone: no vendor pitch, no "AI council," no LMS.

Alignment footer for PROMPT:

```text
Stay focused on: {goal one-liner}. If the reply adds extra tools, committees, or long training programs, say: "Narrow to the one workflow and 30-day plan we defined."
```

## REVIEW (embedded)

Pass all before PROMPT:

- Answers the user's words, not a generic AI strategy article
- Fits one paste into ChatGPT/Claude/Gemini
- Produces something they can use this week (checklist, script, outline, plan)

## PROMPT template (hero)

```markdown
## PROMPT (copy this)

\`\`\`text
You are helping me with a practical, specific request.

Context:
{2–4 bullets from CLARIFY}

Deliver in this exact structure:
1. {section}
2. {section}
3. {section}
...

Constraints:
- Plain language, no jargon
- No vendor pitch
- {profile-specific constraints}

Before you write the full answer, ask me ONLY these questions (max 2):
1) {question}
2) {question}
\`\`\`

*Stay focused on: {goal one-liner}*
```

## FINISH template (secondary)

```markdown
## FINISH

**At a glance**
- {bullet}
- {bullet}
- {bullet}

**Checklist**
- [ ] {action}
- [ ] {action}
- [ ] {action}

**Summary to save**
{one paragraph: what we clarified, what prompt to use next, what done looks like}
```

## Example: team AI strategy ask

**Input:**

> Help me create a strategy for my team to start using AI better at work. We tried a few tools but people are confused and I want a clear plan.

**CLARIFY output shape:**

- Goal: 30-day plan for consistent AI use on real work, without tool chaos
- Not: company-wide transformation, tool comparison essay, training slides
- Options: A) one shared workflow, B) tool rules, C) manager rollout (default A)

**PROMPT sections:** goal sentence, confusion diagnosis, one workflow, tool table (max 3), week-by-week (4 weeks), team rules (5), success signals (3), manager script (5 sentences).

**FINISH:** week-at-a-glance + post-in-channel checklist + session summary.
