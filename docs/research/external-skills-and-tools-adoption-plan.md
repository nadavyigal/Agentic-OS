# External Skills & Tools Adoption Plan

**Date:** 2026-06-20
**Scope:** 5 repos evaluated against 4 contexts — Builder OS (vault), Agentic OS, RunSmart, ResumeBuilder.
**Status:** Research only. Nothing installed, copied, or scanned yet. Decisions pending approval.

---

## 1. Executive Recommendation

**Adopt two things now, one Builder-OS skill, a thin slice of a third, and defer the rest.**

The dominant fact across all five repos: **you already own engineering skills three times over** (superpowers, gstack, your own `.agents` agents) and you already cloned a 377-file marketing pack with **zero security vetting**. So the real gaps are not more skills. They are:

1. **A security gate (NVIDIA/SkillSpector)** — adopt **first**. You are actively importing third-party skill packs; research cited in its README finds 26.1% of skills contain vulnerabilities and 5.2% show likely malicious intent. You have imported one large pack already and are evaluating four more. This is the single most important adoption, and its first job is to retroactively scan the marketingskills clone.
2. **A product-management layer (phuryn/pm-skills, `pm-execution` + `pm-product-discovery` only)** — adopt **selectively**. You have engineering and marketing skills but no structured PRD / user-story / pre-mortem / prioritization layer that sits *before* Codex writes code. That is a true gap.
3. **Builder OS fit (mattpocock `obsidian-vault`)** — one skill that directly serves your vault.
4. **A thin slice of addyosmani/agent-skills** — only the web-performance / observability / frontend pieces that your existing packs lack. Not the bulk; it overlaps heavily with superpowers and gstack.

**Defer apple/container.** Your stack (Next.js + hosted Supabase + Vercel + Capacitor/Swift) is serverless/hosted and does not depend on local Linux containers. The tool is v0.x with 349 open issues. Replacing a working setup now is risk with no payoff. Revisit only if you move to local Supabase or containerized CI.

**The meta-deliverable** is the reusable external-skill adoption workflow (Section 11) with SkillSpector as its security gate — so the *next* repo you find gets vetted automatically instead of cloned blind.

---

## 2. Summary of Evaluated Repos

| Repo | What it is | Stars | License | Lang | Last push | Maturity signal | Verdict |
|---|---|---|---|---|---|---|---|
| mattpocock/skills | Personal eng/productivity skills from his `.claude` | 137k | MIT | Shell | 2026-06-18 | Active, mature | **Adapt 1 (obsidian-vault) + inspiration** |
| apple/container | Native Linux containers on Apple Silicon | 39k | Apache-2.0 | Swift | 2026-06-18 | v0.x, 349 issues | **Later / defer** |
| NVIDIA/SkillSpector | Security scanner for agent skills | 8.4k | Apache-2.0 | Python | 2026-06-16 | Active, focused | **Adopt now (gate)** |
| addyosmani/agent-skills | Production-grade eng skills (CC plugin) | 64k | MIT | Shell | 2026-06-19 | Very active | **Adapt slice (4 skills)** |
| phuryn/pm-skills | 100+ PM skills/commands across 8 categories | 20k | MIT | — | 2026-06-06 | Active | **Adopt slice (pm-execution + discovery)** |

---

## 3. Current Local Agentic OS Context (Step 1 findings)

| Looked for | Result |
|---|---|
| AGENTS.md, CLAUDE.md, README.md | PRESENT (root) |
| `.agents/` | PRESENT — canonical cross-agent skill home |
| `.agent-os/` (from proposed paths) | **MISSING** — proposed `.agent-os/...` paths do not exist; use `.agents/` |
| `docs/` | PRESENT (integrations, obsidian, agentic-os, superpowers); `docs/research/` created this session |
| PROJECT-BRIDGES/ | PRESENT — runsmart-/resumebuilder- web/ios/distribution bridges |
| SKILLS/ + skills/ | BOTH present (a duplication smell) |
| marketingskills/ | PRESENT — 377-file clone, **never security-scanned** |
| distribution-os/ | PRESENT — marketing consumption silo (flagged in amendment plan) |
| CODEX.md, tasks/lessons.md | missing |
| Existing skill libraries (global) | superpowers + gstack (180+ skills) already loaded |

**Implication:** Adoption must reconcile with `OS-AMENDMENT-PLAN-2026-06-20.md` (one home per data type; generated/written/invisible). New skills are INVISIBLE infra → `.agents/skills/<domain>/`. New review workflows → `.agents/workflows/`. Do not create new top-level silos.

---

## 4. Repo-by-Repo Analysis

### 4.1 mattpocock/skills
Skills in `engineering/` (codebase-design, diagnosing-bugs, domain-modeling, implement, improve-codebase-architecture, prototype, resolving-merge-conflicts, **tdd**, **to-prd**, to-issues, triage, grill-with-docs), `productivity/` (grill-me, grilling, handoff, teach, writing-great-skills), `personal/` (edit-article, **obsidian-vault**), `misc/` (git-guardrails, setup-pre-commit).
- **Overlap:** High. tdd, diagnosing-bugs, domain-modeling, to-prd, implement all duplicate superpowers/gstack equivalents you already run. Adopting them invites conflicting instructions.
- **Genuinely additive:** `personal/obsidian-vault` → directly serves **Builder OS**. `productivity/writing-great-skills` → useful reference when you author your own skills. `handoff`/`teach` → minor.
- **Verdict:** Adopt `obsidian-vault` (Builder OS). Use the rest as inspiration only. Do **not** bulk-install — it would triple-stack your TDD/debug skills.

### 4.2 apple/container
Native Linux containers via lightweight VMs on Apple Silicon (Swift, Apache-2.0).
- **Relevance to your stack:** Low. RunSmart and ResumeBuilder are Next.js + hosted Supabase + Vercel (web) and Capacitor/Swift (iOS). None of that requires local Linux containers in daily dev. Agentic OS is markdown + a Python CLI.
- **Commercial/practical:** v0.x, 349 open issues, fast churn. Complements (not replaces) Docker for Apple-silicon Linux workloads; not yet a stable Docker Desktop replacement.
- **Verdict:** **Later.** No current workflow needs it. Revisit only if you adopt local Supabase containers or containerized CI. Do not replace a working Docker/serverless setup now (explicit risk).

### 4.3 NVIDIA/SkillSpector
Python 3.12 security scanner. 64 vulnerability patterns / 16 categories: prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, output handling, system-prompt leakage, memory poisoning, tool misuse, rogue agent, trigger abuse, dangerous code (AST), taint tracking, YARA, MCP least-privilege, MCP tool poisoning. Static + optional LLM stage. Scans repos/URLs/zips/dirs/files. Outputs terminal/JSON/Markdown/SARIF. 0-100 risk score. **Runs via Docker (no Python pollution of your machine).**
- **Fit:** This is the keystone of safe skill adoption. It answers "is this skill safe to install?" before you clone. It is a **local dev / CI tool**, not a skill that goes in agent context — so zero token cost.
- **First job:** retroactively scan the already-imported `marketingskills/` (377 files) and any pack from this report before it touches `.agents/`.
- **Verdict:** **Adopt now**, Docker mode, `--no-llm` for fast local scans (add LLM stage with your Anthropic key for deep scans of anything that scores risky).

### 4.4 addyosmani/agent-skills
20 skills (api-and-interface-design, browser-testing-with-devtools, ci-cd-and-automation, code-review-and-quality, code-simplification, context-engineering, debugging-and-error-recovery, deprecation-and-migration, documentation-and-adrs, doubt-driven-development, frontend-ui-engineering, git-workflow-and-versioning, idea-refine, incremental-implementation, interview-me, observability-and-instrumentation, performance-optimization, planning-and-task-breakdown, security-and-hardening, shipping-and-launch) + commands (build/plan/review/ship/spec/test/webperf) + agents (code-reviewer, security-auditor, test-engineer, web-performance-auditor). Multi-agent (Claude/Gemini/Cursor/Windsurf/opencode). Installable as a Claude Code plugin.
- **Overlap:** Very high. planning, code-review, debugging, tdd-equivalents, ship/spec/test commands all duplicate superpowers + gstack (`/review`, `/qa`, `/ship`, `/spec`, `/careful`, `/impeccable`) and your own agents (code-reviewer, investigator).
- **Genuinely additive:** `frontend-ui-engineering`, `performance-optimization`, `observability-and-instrumentation`, and the `web-performance-auditor` agent — useful for RunSmart/ResumeBuilder web Core Web Vitals and ResumeBuilder SEO. `browser-testing-with-devtools` partly overlaps Playwright MCP you already have.
- **Verdict:** **Adapt a slice (≤4 skills).** Do **not** install the plugin — it would import 20 skills + 8 commands + 4 agents and collide with two existing libraries (conflicting-instructions risk).

### 4.5 phuryn/pm-skills
8 categories. Highest-value cluster `pm-execution` (create-prd, user-stories, job-stories, prioritization-frameworks, pre-mortem, outcome-roadmap, strategy-red-team, release-notes, retro, sprint-plan, stakeholder-map, test-scenarios) and `pm-product-discovery` (analyze-feature-requests, opportunity-solution-tree, identify-assumptions, interview-script, prioritize-assumptions). Other categories: pm-go-to-market, pm-market-research, pm-marketing-growth, pm-product-strategy, pm-data-analytics, pm-ai-shipping.
- **Fit:** Fills your real gap — a structured planning/requirements layer *before* code. PRD → user-stories → pre-mortem → prioritization maps exactly onto your planning-protocol + one-story-at-a-time rule.
- **Overlap:** `pm-go-to-market` / `pm-market-research` / `pm-marketing-growth` duplicate the marketingskills pack (positioning, ICP, competitor, growth-loops, value-prop). **Ignore those** to avoid a second marketing layer.
- **Solo-founder filter:** skip sprint-plan / stakeholder-map (team ceremony you don't need).
- **Verdict:** **Adopt `pm-execution` core + `pm-product-discovery` core (~8 skills).** Ignore the GTM/market/marketing categories (marketingskills owns those).

---

## 5. Agentic OS Fit

| Repo | Adopt? | Lives globally | Default or optional |
|---|---|---|---|
| SkillSpector | Yes (now) | Local CLI (Docker), invoked by adoption workflow | **Default gate** before any skill import |
| phuryn pm-skills | Yes (slice) | `.agents/skills/product-management/` | Optional, invoked on planning |
| addyosmani | Slice (≤4) | `.agents/skills/engineering/` | Optional, on demand |
| mattpocock | obsidian-vault → Builder OS | not Agentic OS | Optional |
| apple/container | No (later) | — | — |

- **Invocation:** skills self-trigger on their `description` phrases; PM skills invoked when you say "write a PRD / user stories / pre-mortem." Reviews run as named workflows under `.agents/workflows/`.
- **Avoid bloating:** copy `SKILL.md` only, no examples/scripts/evals; cap PM additions at ~8 and engineering at ~4; never install a full plugin (pulls commands+agents you don't need). Pin versions; sync on-demand only (no refresh treadmill — per amendment plan).

## 6. RunSmart Fit

- **Product planning:** phuryn `create-prd`, `user-stories`/`job-stories`, `prioritization-frameworks` for feature scoping; `pre-mortem` + `strategy-red-team` for **Garmin production release readiness** (high-stakes, irreversible — pre-mortem is ideal here).
- **Engineering quality:** addyosmani `performance-optimization` + `observability-and-instrumentation` for the web app; existing superpowers/gstack already cover TDD/review.
- **Mobile/iOS:** none of these packs add iOS value; your `ios-expert` skill + ios-build-triager agent already cover it.
- **Analytics/demo/Garmin:** phuryn discovery skills can structure Garmin messaging hypotheses; demo video is covered by marketingskills `video`.
- **Workflows to create (later, not now):** `product-requirements-review`, `pre-mortem-release-readiness`.

## 7. ResumeBuilder Fit

- **Product planning:** phuryn `create-prd`, `user-stories`, `prioritization-frameworks` for ATS-checker and feature work.
- **SEO / web quality:** addyosmani `web-performance-auditor` agent + `performance-optimization` → Core Web Vitals directly feed Resumely's SEO growth thesis (pairs with marketingskills `seo-audit`/`programmatic-seo`).
- **PDF generation reliability:** none of these packs address it specifically; treat as an engineering story under existing TDD/debug skills + addyosmani `debugging-and-error-recovery` (only if not already covered).
- **Paywall/conversion/ASO:** owned by marketingskills (prior report), not these repos.
- **Workflows to create (later):** `seo-perf-review`, `product-requirements-review`.

---

## 8. Adopt / Adapt / Ignore Tables

### mattpocock/skills
| Asset | Decision | Belongs | Why | Value | Complexity | Risk/validation |
|---|---|---|---|---|---|---|
| obsidian-vault | Adopt | Builder OS | Directly serves the vault | Med-High | Low | Verify it fits your vault structure, not generic |
| writing-great-skills | Adapt | Agentic OS | Reference when authoring skills | Low-Med | Low | — |
| engineering/* (tdd, implement, to-prd, diagnosing-bugs…) | Ignore | — | Triplicates superpowers/gstack | Low | — | Conflicting instructions |
| productivity/* (grill, teach, handoff) | Later | — | Minor; revisit per-need | Low | Low | — |

### apple/container
| Asset | Decision | Belongs | Why | Value | Complexity | Risk/validation |
|---|---|---|---|---|---|---|
| container runtime | Later | Local Dev Tool | Stack is hosted/serverless; no current need | Low now | High | v0.x churn; don't replace Docker early |

### NVIDIA/SkillSpector
| Asset | Decision | Belongs | Why | Value | Complexity | Risk/validation |
|---|---|---|---|---|---|---|
| SkillSpector scanner (Docker) | Adopt | Agentic OS / Local Dev Tool | Security gate for skill imports | **Very high** | Low-Med | Verify Docker build runs; scan marketingskills first |
| LLM deep-scan stage | Adapt | Same | Deeper scan for risky-scored packs | Med | Med | Uses your Anthropic key (cost) |

### addyosmani/agent-skills
| Asset | Decision | Belongs | Why | Value | Complexity | Risk/validation |
|---|---|---|---|---|---|---|
| web-performance-auditor (agent) | Adopt | Shared (RunSmart/RB) | Core Web Vitals / SEO perf | High | Low | — |
| performance-optimization | Adapt | Shared | Web perf | Med-High | Low | Overlap w/ gstack |
| observability-and-instrumentation | Adapt | Shared | Eventing/monitoring | Med | Low | — |
| frontend-ui-engineering | Adapt | Shared | UI quality | Med | Low | Overlap w/ frontend-design |
| 16 other skills + commands + agents | Ignore | — | Triplicate existing libraries | Low | — | Conflicting instructions / bloat |

### phuryn/pm-skills
| Asset | Decision | Belongs | Why | Value | Complexity | Risk/validation |
|---|---|---|---|---|---|---|
| create-prd | Adopt | Agentic OS | Pre-code requirements gap | High | Low | Adapt to solo-founder, no team ceremony |
| user-stories / job-stories | Adopt | Agentic OS | Story-writing layer | High | Low | — |
| pre-mortem | Adopt | Agentic OS | Release readiness (Garmin) | High | Low | — |
| prioritization-frameworks | Adopt | Agentic OS | Scoping | Med-High | Low | — |
| strategy-red-team | Adapt | Agentic OS | Challenge PRDs/strategy | Med | Low | — |
| outcome-roadmap | Adapt | Agentic OS | Roadmap framing | Med | Low | — |
| product-discovery core | Adapt | Agentic OS | Feature-request triage | Med | Low | — |
| pm-go-to-market / market-research / marketing-growth | Ignore | — | Duplicates marketingskills | Low | — | Second marketing layer |
| sprint-plan / stakeholder-map | Ignore | — | Team ceremony; you're solo | Low | — | — |

---

## 9. Combined Adoption Priority Table

| # | Repo | Asset | Action | Why now | Owner area | First step |
|---|---|---|---|---|---|---|
| 1 | SkillSpector | Scanner (Docker) | Adopt | You import packs unscanned today | Agentic OS / Local | Build Docker image, scan `marketingskills/` |
| 2 | phuryn | create-prd | Adopt | Pre-code gap, used constantly | Agentic OS | Copy SKILL.md to `.agents/skills/product-management/` |
| 3 | phuryn | user-stories / job-stories | Adopt | Story layer for one-story rule | Agentic OS | Same |
| 4 | phuryn | pre-mortem | Adopt | Garmin release readiness | RunSmart | Same |
| 5 | phuryn | prioritization-frameworks | Adopt | Scoping both apps | Agentic OS | Same |
| 6 | mattpocock | obsidian-vault | Adopt | Serves Builder OS vault | Builder OS | Copy + adapt to vault layout |
| 7 | addyosmani | web-performance-auditor | Adopt | RB SEO / Core Web Vitals | Shared | Copy agent def |
| 8 | phuryn | strategy-red-team | Adapt | Challenge plans (pairs w/ advisor) | Agentic OS | Copy SKILL.md |
| 9 | addyosmani | observability-and-instrumentation | Adapt | Eventing for both apps | Shared | Copy SKILL.md |
| 10 | phuryn | outcome-roadmap | Adapt | Roadmap framing | Agentic OS | Copy SKILL.md |

Everything else: Ignore or Later.

---

## 10. Recommended Folder Structure (adapted to actual local layout)

Your proposed `.agent-os/` paths do not exist; use the real `.agents/` standard, folded into the amendment plan's slim shape.

```
Agentic OS/
  .agents/
    skills/
      product-management/      # phuryn slice (~8 SKILL.md only)
        create-prd/SKILL.md
        user-stories/SKILL.md
        job-stories/SKILL.md
        pre-mortem/SKILL.md
        prioritization-frameworks/SKILL.md
        strategy-red-team/SKILL.md
        outcome-roadmap/SKILL.md
        product-discovery/SKILL.md
      engineering/             # addyosmani slice (≤4 SKILL.md)
        web-performance/SKILL.md
        observability/SKILL.md
        performance-optimization/SKILL.md
        frontend-ui/SKILL.md
      security/
        README.md              # how to run SkillSpector (points to Docker)
    workflows/
      skill-adoption-review.md
      skill-security-scan.md
      product-requirements-review.md
      pre-mortem-release-readiness.md
  tools/
    skillspector/              # cloned scanner (Docker), NOT in agent context
  docs/research/external-skills-and-tools-adoption-plan.md   # this report

Builder OS vault/
  09-Templates/ or skill location for obsidian-vault skill

# apple/container: not added. Documented as "Later" only.
```

---

## 11. Reusable External-Skill Adoption Workflow

Use this every time you find a new GitHub skill repo. SkillSpector is the security gate at step 5.

1. **Repo discovery** — capture URL, stars, license, last-push, open-issues, language. Reject archived/unmaintained.
2. **Local context check** — does it overlap superpowers / gstack / marketingskills / existing `.agents`? If >50% overlap, default to Ignore.
3. **Repo inspection** — read README, AGENTS.md, folder structure, 2-3 representative SKILL.md, install method, tool/dependency assumptions.
4. **Skill value mapping** — map each candidate skill to Builder OS / Agentic OS / RunSmart / ResumeBuilder / Local-Dev. Discard unmapped.
5. **Security/risk scan (SkillSpector gate)** — `docker run --rm -v "$PWD:/scan" skillspector scan ./repo --no-llm`. Any HIGH/CRITICAL (prompt injection, data exfiltration, excessive agency, supply chain) → **block**. Risky-but-unclear → re-run with LLM stage.
6. **Token-bloat review** — count SKILL.md size + references that load into context. Copy SKILL.md only; leave evals/scripts/tools behind. Cap per-domain skill count.
7. **Adopt / Adapt / Ignore / Later decision** — record in a decision table with why + owner area.
8. **Pilot workflow** — run the candidate skill on ONE real task in its target project. Compare output to current baseline.
9. **Validation criteria** — output is product-specific (names your product/constraints unprompted), no security flags, no instruction conflicts, measurable improvement over baseline.
10. **Approval gate** — nothing enters `.agents/` until: SkillSpector clean + pilot passed + you explicitly approve. Then pin version; sync on-demand only.

## 12. Phased Implementation Plan

- **Phase 0 — Research & scoring (this report).** Done: 5 repos inspected, overlap mapped, value ranked.
- **Phase 1 — Safety & adoption workflow.** Build SkillSpector (Docker). Scan the existing `marketingskills/` clone. Write `skill-adoption-review.md` + `skill-security-scan.md`. Define the approval rule (Section 11, step 10).
- **Phase 2 — Engineering slice.** Pilot addyosmani web-performance-auditor on ResumeBuilder; adapt ≤4 skills. Skip everything overlapping superpowers/gstack.
- **Phase 3 — Product-management layer.** Adopt phuryn `pm-execution` core + `pm-product-discovery` core into `.agents/skills/product-management/`. Wire `create-prd`/`user-stories`/`pre-mortem` into the planning-protocol.
- **Phase 4 — Local dev environment.** Document apple/container as "Later." No pilot now. Re-evaluate if/when local Supabase or containerized CI appears. Do not touch Docker.
- **Phase 5 — Project pilots.** RunSmart: pre-mortem the Garmin release; create-prd for next feature. ResumeBuilder: web-perf audit + create-prd for ATS checker. Measure: did output quality beat baseline? Keep only what passes.

## 13. Risk Review

| # | Risk | Root cause | Impact | Mitigation | Validation test | Decision gate |
|---|---|---|---|---|---|---|
| 1 | Token bloat | Copying full repos | Slow, costly, noisy agents | SKILL.md-only; per-domain caps | Context load unchanged | Don't proceed if it grows |
| 2 | Conflicting instructions across packs | superpowers + gstack + matt + addyosmani all define TDD/review | Agent picks wrong/contradictory guidance | Adopt only NON-overlapping skills | Ask for a review → one skill fires | >50% overlap → Ignore |
| 3 | Generic advice | No product context | Useless output | Pair with per-app product-marketing.md + product-context | Output cites real product specifics | Reject unanchored advice |
| 4 | Security issues in third-party skills | Implicit trust, no vetting | Malicious/unsafe skills in your OS | SkillSpector gate before import | Scan returns no HIGH/CRITICAL | No import without clean scan |
| 5 | Hidden prompt injection / unsafe tool use | Skills carry hidden instructions | Data exfiltration, excessive agency | SkillSpector static + LLM stage | Injection/exfiltration patterns = 0 | Block on any HIGH finding |
| 6 | Adopting too much before measuring | Enthusiasm | Bloat, low ROI | Pilot + baseline compare per skill | Measurable improvement | No keep without pilot pass |
| 7 | Agentic OS harder to use | More skills/silos | You skip it (again) | Fold into amendment plan; cap counts | Root file/dir count flat | Violates amendment → stop |
| 8 | Apple container compatibility issues | v0.x, 349 issues | Broken local dev | Don't adopt now | n/a | Later only |
| 9 | Replacing working Docker too early | Novelty | Lost productivity | Keep current setup | n/a | Defer |
| 10 | Unclear ownership global vs project | Skills in two places | Drift, duplication | Global = invisible infra in `.agents/`; project = written context only | One home per skill | Per amendment rule |

## 14. First 10 Implementation Stories

1. **Build SkillSpector (Docker).** `git clone` to `tools/skillspector`, `make docker-build`. *(Verify: image builds, `--help` runs.)*
2. **Scan the existing marketingskills clone.** `docker run --rm -v "$PWD:/scan" skillspector scan ./marketingskills --no-llm`. *(Verify: review report; triage any HIGH/CRITICAL.)*
3. **Write `skill-security-scan.md` workflow.** Codify the scan command + thresholds. *(Verify: re-runnable on any repo.)*
4. **Write `skill-adoption-review.md` workflow.** The 10-step Section-11 process incl. approval gate. *(Verify: walks a new repo end-to-end.)*
5. **Adopt phuryn `create-prd`.** SkillSpector-scan, then copy SKILL.md to `.agents/skills/product-management/`. *(Verify: scan clean; produces a PRD on a real RunSmart feature.)*
6. **Adopt phuryn `user-stories` + `pre-mortem`.** Same gate. *(Verify: pre-mortem run on the Garmin release surfaces a real risk.)*
7. **Adopt phuryn `prioritization-frameworks`.** Same gate. *(Verify: prioritizes a real backlog slice.)*
8. **Adopt mattpocock `obsidian-vault` into Builder OS.** Scan, adapt to vault structure. *(Verify: fits your actual folder map, not generic.)*
9. **Pilot addyosmani `web-performance-auditor` on ResumeBuilder.** Scan, run as agent on the live site. *(Verify: returns RB-specific Core Web Vitals findings.)*
10. **Document apple/container as "Later."** One-paragraph note + revisit trigger. *(Verify: decision recorded; nothing installed.)*

## 15. Recommended First Action

**Build SkillSpector and scan the marketingskills clone you already imported (Stories 1-2).** It is the highest-value, lowest-risk move: it stands up the safety gate every future adoption depends on, and its first run retroactively de-risks the 377 unvetted files already sitting in your OS. Until that scan is clean, treat marketingskills as untrusted.

---

*Nothing executed. No repo installed, no skill copied, no scan run, no app/Docker/production files modified. All adoption awaits explicit approval.*
