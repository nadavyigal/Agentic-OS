# Adoption Initiation Prompt

Paste the block below into a fresh Claude Code / Codex session **opened in the Agentic OS repo** to start executing the skill/tool adoption work. It enforces the operating rules so the agent does not bulk-install or skip the security gate.

---

```
You are working in the Agentic OS repo — my cross-project operating layer. It owns shared reusable skills; RunSmart and ResumeBuilder consume only project-specific workflows. The Builder OS vault is human-readable thinking only, not a production dependency.

Before doing anything:
1. Read docs/research/external-skills-and-tools-adoption-plan.md
2. Read docs/research/marketingskills-adoption-plan.md
3. Read OS-AMENDMENT-PLAN-2026-06-20.md
4. State the objective in one sentence.

Operating rules (these override defaults):
- Selective adoption only. Never install a full repo or plugin. Copy SKILL.md files only — no evals/, scripts/, or tools/.
- SECURITY GATE FIRST: no third-party skill enters .agents/ until SkillSpector scans it clean (no HIGH/CRITICAL). The marketingskills/ clone already in this repo has never been scanned — scan it before trusting it.
- One story at a time. Implement, verify, report evidence, then ask before the next story.
- Adapt every skill to my products. A skill that produces generic output (does not name RunSmart/ResumeBuilder specifics, Garmin, ATS, etc.) is not done.
- Fold everything into the amendment plan's slim shape: skills are invisible infra in .agents/skills/<domain>/; reviews are workflows in .agents/workflows/. Do not create new top-level silos. Do not raise the root file/dir count.
- No new dependencies, no production app changes, no Docker changes without my explicit "yes" in the current message.
- Pin versions; sync upstream on-demand only. No auto-refresh treadmills.

Start with Phase 1, Story 1 from the external-skills plan: build SkillSpector (Docker) and scan the existing marketingskills/ clone. Report the scan result and stop for my approval before importing any skill.
```

---

## Why this lives in Agentic OS and "runs from here"

- Agentic OS is the operating layer that owns shared reusable skills and workflows. The adoption work (SkillSpector gate, PM skills, engineering slice) installs into `.agents/` here and executes from here.
- The Builder OS vault is explicitly *not* a production dependency — it holds synthesis and decision narrative, not executable plans or skills.
- Project-specific skills (e.g. the `obsidian-vault` skill) live with their project, not here. That one lives in the Builder OS vault.

## Quick reference — what to run first

| Order | Action | Source doc |
|---|---|---|
| 1 | Build SkillSpector, scan `marketingskills/` | external-skills plan, Stories 1-2 |
| 2 | Write skill-security-scan + skill-adoption-review workflows | external-skills plan, Stories 3-4 |
| 3 | Adopt phuryn pm-execution core (create-prd, user-stories, pre-mortem, prioritization) | external-skills plan, Stories 5-7 |
| 4 | Pilot addyosmani web-performance-auditor on ResumeBuilder | external-skills plan, Story 9 |
| 5 | Marketing: write RunSmart/.agents/product-marketing.md | marketingskills plan, Story 2 |
