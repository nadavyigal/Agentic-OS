# Prompt: Exec Review

Use on demand for a single project. CEO + distribution lens. Strategic, not operational. Different from `morning-brief` (which is daily, cross-project, execution-focused).

Trigger phrases:
- "give me an exec review on <project>"
- "exec review <project>"

```txt
You are doing a single-project Exec Review. CEO + distribution lens.
This is NOT a status update — see morning-brief for that.

First read:
1. PROJECT-BRIDGES/<project>.md (strategic position, north-star, current bet)
2. The project's local tasks/session-log.md — last 10 entries (pattern, not snapshot)
3. The project's local tasks/lessons.md (what we've learned)
4. The project's local docs/agent-os/project-context.md if it exists
5. Recent commits in the project repo: git log --since="14 days ago" --oneline

Do NOT include execution-level content. No "next story", no "what you left off",
no commit-by-commit recap. Stay strategic.

Produce exactly these 4 sections, in order:

## 1. North-Star Check
- What is the north-star metric for this project?
- Is it moving? Direction? Over what window?
- Why is it moving (or not) — cause, not correlation
- If unknown: say so and name the data source that would answer it

## 2. Shipped vs Matters
- What shipped in the last 14 days
- Of those, which actually serve the north-star
- Gap: where effort and impact diverged
- One sentence: busy or productive?

## 3. Distribution Reality
- Who is actually seeing the product (channel + volume estimate)
- What's working, what isn't
- Distribution hypothesis being tested right now — or none
- Biggest unverified assumption about distribution

## 4. Next Bet
A single bet for the next 2-4 weeks. Specific enough to become a story:
- Hypothesis: if we ship X, then Y will move
- What to ship (concrete enough that plan-feature could pick it up)
- How we'll know it worked (metric + threshold)
- Kill criteria: what would make us stop

Then save the full review to:
PROJECT-BRIDGES/exec-reviews/YYYY-MM-DD-<project-slug>.md

Print one line confirming the path.

Rules:
- One project per run.
- Be honest. If the north-star isn't moving, say so. If distribution isn't real yet, say so.
- Cite evidence: commits, lessons, session-log entries. No vibes-only claims.
- Do not invent metrics. If a number isn't available, mark it "unknown — need: <source>".
- Do not propose execution-level next steps. Next Bet outputs hypothesis + ship target + success metric.
- This is the strategic war room. The Next Bet is meant to be carried back into the product repo and turned into a plan via plan-feature.
```

