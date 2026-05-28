# Prompt: Risk Review

Use on demand after a plan exists, before any implementation. Trigger phrase: "run a risk review on the plan".

```txt
You are doing a Risk-Gated Review of a plan that already exists. Do not write code.

First read:
1. The plan, spec, or story being reviewed
2. AGENTS.md and CLAUDE.md for this repo
3. tasks/lessons.md and tasks/ERRORS.md for known traps
4. Any files the plan claims to touch — verify they exist and behave as the plan assumes

Review the plan like a skeptical senior engineer and risk manager.

Produce exactly these 5 sections, in order:

## 1. Goal Fit
- User goal in one sentence
- What "done" looks like from the user's view
- Anything in the plan that doesn't support the goal
- Anything missing required to achieve the goal

## 2. Assumptions
Flat list. Tag each: confirmed | needs-verification | risky.
For needs-verification or risky items, name the exact file, API, schema, env var, or flow to inspect.

## 3. Risk Register
Single table with columns:
Risk | Likelihood (L/M/H) | Impact (L/M/H) | Root cause | Mitigation | Verification
Cover these categories where relevant: product, technical, data, integration, UX, scope, regression, testing, deployment, agent-execution.

## 4. Smallest Safe Slice
- First PR scope: what ships
- What it explicitly does NOT do
- User-visible value
- How it's tested
- Regression risk

## 5. Recommendation
One of: proceed | proceed-with-mitigations | split-before-implementing | stop-and-investigate
One paragraph justifying the choice.

Then save the full review to:
tasks/risk-reviews/YYYY-MM-DD-<feature-slug>.md

Print one line confirming the path.

Rules:
- Do not invent files, APIs, or architecture. If unknown, mark as needs-verification.
- Do not propose approaches already in tasks/ERRORS.md.
- Be skeptical. A plan with zero risks was not reviewed.
```

