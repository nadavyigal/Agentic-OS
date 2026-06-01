# Global Taste & Craft

The judgment layer. Standards tell agents what is *allowed*; taste tells them what is *worth shipping*.

Taste protects products from generic AI output, overbuilt features, weak UX, messy architecture, and work that looks complete but does not improve the product. When a change passes every check and still feels wrong, this file is the reason you can name why and stop it.

This is a cross-agent standard. Claude Code, Codex, Cursor, and future agents all apply it. It is markdown-first and lightweight by design. It does not replace local project OS files, and the local repo remains the implementation source of truth.

## How To Use This

- **Taste Check** — a fast self-check the implementing agent runs before declaring work done. Inline, no separate agent. Covered as a gate step in `GLOBAL-WORKFLOWS.md`.
- **Taste Review** — a deeper pass using the `SKILLS/taste-reviewer.md` role, for UI, AI output, public-facing surfaces, or anything that will be hard to walk back.

Relationship to existing tools: gstack's `design-review`, `plan-design-review`, and `plan-ceo-review` are tool-specific taste passes that live outside this OS. This file is the agent- and project-neutral version they all point back to. Do not duplicate their content here.

## The Verdict Model

Every taste judgment resolves to one of three:

- **PASS** — ships. It improves the product, fits the product's voice, carries no slop, and is scoped to what was asked.
- **REVISE** — right direction, specific fixable issues. Name each issue and the bar it has to clear. Do not ship until cleared.
- **REJECT** — wrong direction. Generic, overbuilt, off-voice, or it does not move the product forward. Stop and rethink before writing more code. A REJECT is not a failure of effort; it prevents shipping polished work that should not exist.

When unsure between PASS and REVISE, choose REVISE. When unsure between REVISE and REJECT, ask the founder.

## The Five Dimensions

### 1. Product Taste
The bar: the change makes the product measurably better for its actual user, not just more featureful.

- REJECT triggers: a feature nobody asked for, added because it was easy; scope that crept past the request; complexity the user has to absorb for the builder's convenience.
- PASS bar: clear user goal, answers "who is this for and how do we know it worked," and removes friction rather than adding surface.

### 2. UX Taste
The bar: the interface supports the real workflow and respects the user's attention.

- REJECT triggers: a wall of data where one clear action belongs; dead-end states (no empty/loading/error handling); web layouts copied onto native; visual noise that hides the next step.
- PASS bar: clear hierarchy, one obvious next action, all states handled (empty, loading, error, success, permission), platform-native on mobile.

### 3. Engineering Taste
The bar: the solution is as simple as the problem allows and a future reader can follow it.

- REJECT triggers: a new abstraction where an existing pattern fits; clever code that needs a comment to be understood; duplicated logic; a fix that quietly touches unrelated files.
- PASS bar: matches surrounding code idiom, reuses existing patterns, scoped to the outcome, rollback notes for risky changes.

### 4. AI Output Taste
The bar: AI-generated user-facing text reads like the product's voice, not like a model.

- REJECT triggers: warmup phrases, em dashes, hype, hedging, generic positivity, "as an AI," filler that says nothing, confident claims with no basis.
- PASS bar: specific, in the product's voice, says only what is true and useful, editable and explainable by the user.

### 5. PR / QA Taste
The bar: the change is defensible on its own and the evidence proves it works.

- REJECT triggers: "done" with no evidence; tests or dashboards edited to look green; a PR that bundles unrelated changes; a summary that hides a known risk.
- PASS bar: evidence attached (tests, build, screenshots, manual notes), acceptance criteria met, regressions and edge cases checked, risks named honestly.

## Product Taste Profiles

Each product has a center of gravity. Taste means defending it.

### RunSmart — calm personal coach, not an analytics dashboard
- PASS: one clear next action, an encouraging human voice, respects recovery and the runner's state, surfaces the *insight* and hides the raw math.
- REJECT: a wall of charts and raw metrics, anxiety-inducing data dumps, generic fitness-app clichés, more numbers where one sentence of coaching belongs.

### Resumely — professional career assistant, not a gimmicky AI resume toy
- PASS: credible and professional tone, ATS-aware and practical, the user stays in control and can edit everything, output a hiring manager would respect.
- REJECT: emoji-stuffed "AI magic" buttons, hype and fake confidence scores, gimmicks over substance, output that reads machine-generated.
- Note: the founder's memory brands this product "Resumely"; the local repo is still named ResumeBuilder. Use the repo name in code paths, the brand name in product voice.

### AI Audit Toolkit — consultant-grade workflow audit, not generic automation hype
- PASS: findings tied to the client's *actual* workflow, prioritized by impact, defensible with evidence, reads like a consultant who did the work.
- REJECT: generic "automate everything with AI" hype, vague recommendations, no evidence, a template with the client's name pasted in.
- Note: not an active repo yet. Forward-looking profile; confirm scope when the project starts.

## When Taste And Speed Conflict
The founder values speed over ceremony. Taste is not ceremony. A REJECT that prevents shipping the wrong thing saves more time than it costs. But do not gold-plate a PASS: once it clears the bar, ship it.
