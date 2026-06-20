# marketingskills Adoption Plan

**Date:** 2026-06-20
**Repo evaluated:** https://github.com/coreyhaines31/marketingskills (MIT, 34.2k stars, last pushed 2026-06-17)
**Status:** Research only — nothing installed, pruned, or wired. Decision pending.

---

## 1. Executive Recommendation

**Adopt — selectively, and as a *pruning* exercise, not an installation.**

You have already over-adopted this repo. The full 377-file clone lives at `marketingskills/` (synced 2026-05-26, now ~3 weeks stale), and a hand-built consumption layer already exists in `distribution-os/projects/{runsmart,resumebuilder}/scaffold/`. So the work is **not** "add more." It is: keep ~12 relevant skills + one per-project context file each, drop the rest, and fold the result into the slim structure from `OS-AMENDMENT-PLAN-2026-06-20.md`.

Why adopt at all: the skills are genuinely high quality, MIT-licensed, self-contained (`SKILL.md` + on-demand `references/`), and the categories map almost 1:1 to your real needs (ASO, onboarding, paywalls, pricing, programmatic SEO, analytics, churn). Both apps are live on the App Store *right now* (RunSmart v1.0.3, Resumely v1.1), so ASO and onboarding skills are immediately actionable.

Why selective: the repo also ships **51 Node CLI tools + Composio integrations** (API keys, external deps) and `evals/` test infra you will never run. Adopting those is pure dependency and token bloat. And the repo's reference-link marketing (Corey's funnel) means some `references/` files carry promotional noise.

**The single highest-leverage move is not a skill at all — it is writing a real `product-marketing.md` for each app.** Every other skill reads it first. Without it, every output is generic. You already have 80% of the raw material in the `distribution-os` scaffolds.

---

## 2. Repo Summary

- **What it is:** A collection of marketing Agent Skills (CRO, copywriting, SEO, analytics, growth) following the [agentskills.io](https://agentskills.io) spec. Works with Claude Code, Codex, Cursor, Windsurf. Also a Claude Code plugin marketplace.
- **Structure:** 43 skills under `skills/<name>/`, each = `SKILL.md` (frontmatter: `name`, `description` with trigger phrases, `version`) + optional `references/*.md` (loaded on demand) + `evals/evals.json` (test cases).
- **Install model:** Copy skills into `.agents/skills/` (cross-agent standard) — exactly the directory you already have. Foundation context lives at `.agents/product-marketing.md`.
- **Architecture (load-bearing):** `product-marketing` is the root. Every other skill reads `.agents/product-marketing.md` first for product/audience/positioning before acting. Skills cross-reference each other in 7 clusters: SEO/Content, CRO, Content/Copy, Paid/Measurement, Growth/Retention, Sales/GTM, Strategy.
- **Tools:** `tools/clis/` (51 zero-dep Node tools), `tools/composio/` + `tools/integrations/` (third-party API layer). Optional; not required to use the skills.
- **Dependencies/assumptions:** Skills assume a single product context. ASO/SEO skills assume ability to fetch live listing/page data. Tool layer assumes API keys (GA4, GTM, Composio, etc.).
- **Risk from over-adopting:** 43 skills with overlapping trigger phrases → agent confusion and skill-selection noise; generic output without product context; tool layer pulls unavailable dependencies.

---

## 3. Local Agentic OS Fit

**Step-1 inventory (what was found vs missing):**

| Looked for | Result |
|---|---|
| AGENTS.md, CLAUDE.md, README.md | PRESENT (root) |
| `.agents/` | PRESENT — canonical skill home, matches repo spec |
| `.agent-os/` (from your proposed paths) | **MISSING** — your step-5 paths don't match reality; use `.agents/` instead |
| `marketingskills/` | PRESENT — full clone, 43 skills, 377 files, ~3 weeks stale |
| `distribution-os/` | PRESENT — already a consumption layer with per-project scaffolds |
| `PROJECT-BRIDGES/` | PRESENT — `runsmart-distribution.md`, `resumebuilder-distribution.md`, +ios/web bridges |
| `SKILLS/`, `skills/` | PRESENT (two of them — itself a duplication smell) |
| `docs/research/` | MISSING — created for this report |
| `CODEX.md`, `tasks/lessons.md` | missing |

**Fit verdict:** Strong fit *in slim form*, poor fit *as-is*. The repo's `.agents/skills/` + `.agents/product-marketing.md` model is exactly the "INVISIBLE infra + WRITTEN context" split from your amendment plan. But the current full clone + `distribution-os` scaffold + two `skills/` dirs is the accretion that plan is trying to remove. **Adoption must reconcile with the amendment, not add a parallel silo.**

- **What lives globally (Agentic OS):** the curated skill subset (infra) + per-project `product-marketing.md` (written context).
- **Folder:** `.agents/skills/marketing/` (subset of SKILL.md only), per-project context in each repo's `.agents/product-marketing.md`.
- **Invocation:** skills self-trigger on their description phrases; you invoke via `/`-style or natural language ("audit my App Store listing"). Reviews run as named workflows.
- **Avoiding bloat:** copy `SKILL.md` only (not `evals/`, not most `references/`, never `tools/`). Cap the global set at ~12 skills. Pin to a version; do not chase upstream weekly.

---

## 4. RunSmart Fit

Both apps are live, so this is actionable immediately. RunSmart's near-term gate (D7 retention 2026-06-24) makes **activation/onboarding** the priority, not acquisition.

| Priority | Skill | Use for RunSmart |
|---|---|---|
| 1 | `product-marketing` | Build `RunSmart/.agents/product-marketing.md` from existing `distribution-os/.../runsmart/scaffold/product-positioning.md` + `audience.md` + `messaging.md` |
| 2 | `onboarding` | First-run → first-plan → first-run-logged activation; directly serves the D7 gate |
| 3 | `aso` | RunSmart v1.0.3 listing audit (keywords, screenshots, conversion) |
| 4 | `paywalls` + `pricing` | Paywall placement and trial/price test |
| 5 | `analytics` | Activation + retention event design (PostHog) — pairs with `growth-analytics` skill you already have |
| 6 | `video` / `ad-creative` | Demo clips, App Store preview video |
| 7 | `churn-prevention` | Once retention data exists (not yet — too few users) |

**Recommended workflows (later, not now):** `aso-review`, `onboarding-review`, `activation-analytics-checklist`. Garmin messaging = a section in `product-marketing.md`, not a new skill.

---

## 5. ResumeBuilder (Resumely) Fit

Resumely's growth thesis is SEO/programmatic, a different shape from RunSmart.

| Priority | Skill | Use for ResumeBuilder |
|---|---|---|
| 1 | `product-marketing` | Build `ResumeBuilder/.agents/product-marketing.md` from `distribution-os/.../resumebuilder` scaffold |
| 2 | `programmatic-seo` + `site-architecture` | ATS-checker / role-specific / competitor landing pages at scale |
| 3 | `seo-audit` + `ai-seo` | Audit existing pages; AI-search visibility |
| 4 | `competitor-profiling` + `competitors` | Competitor comparison pages |
| 5 | `paywalls` + `pricing` | Conversion + price/packaging |
| 6 | `onboarding` + `signup` | Upload-resume → first-optimization activation |
| 7 | `emails` | Lifecycle / re-engagement (after funnel basics work) |
| 8 | `aso` | Resumely v1.1 listing (secondary — web SEO is the main channel) |

**Recommended workflows (later):** `seo-growth-review`, `programmatic-seo-plan`, `paywall-pricing-review`. **Validation gate:** programmatic SEO is the single biggest quality risk — see Risk 5.

---

## 6. Adopt / Adapt / Ignore Table

Scoped to the ~15 relevant skills (not all 43 — listing all 43 would itself be bloat).

| Skill / asset | Decision | Belongs | Why | Value | Complexity | Risk / validation |
|---|---|---|---|---|---|---|
| `product-marketing` | **Adapt** | Shared → per-project | Foundation all skills read; must be product-specific | Very high | Low | Must reflect real positioning, not aspirational; verify with 2-3 user quotes |
| `aso` | Adopt | Shared | Both apps live on App Store now | High | Low | Needs live listing fetch |
| `onboarding` | Adopt | Shared | RunSmart D7 gate; RB activation | High | Low | Don't redesign onboarding from generic advice without funnel data |
| `paywalls` | Adopt | Shared | Both monetize | High | Low | Validate against real conversion data before changing |
| `pricing` | Adapt | Shared | Both monetize; needs product economics | Med-High | Med | Over-optimizing pre-scale (Risk 7) |
| `programmatic-seo` | Adopt | ResumeBuilder | RB growth thesis | High | High | Low-quality page flood (Risk 5) — gate hard |
| `seo-audit` | Adopt | ResumeBuilder | Audit existing pages | Med-High | Low | — |
| `ai-seo` | Adapt | ResumeBuilder | AI-search visibility | Med | Low | Fast-moving area; treat as directional |
| `site-architecture` | Adopt | ResumeBuilder | Supports programmatic SEO | Med | Med | — |
| `competitor-profiling` / `competitors` | Adapt | Shared | Comparison pages both apps | Med | Low | Keep one, not both (overlap) |
| `analytics` | Adapt | Shared | Event design; pair with existing `growth-analytics` | High | Med | Plans without implementation (Risk 8) |
| `video` / `ad-creative` | Later | RunSmart | Demo clips when capacity allows | Med | Med | Production cost |
| `churn-prevention` | Later | Shared | Needs retention data you don't have yet | Med | Low | Premature now |
| `emails` / `sms` | Later | Shared | Lifecycle after funnel basics | Med | Med | Needs ESP + volume |
| `evals/` (all skills) | Ignore | — | Test infra you won't run | None | — | Pure bloat |
| `tools/` (51 CLIs + Composio) | Ignore | — | API keys + deps; unavailable-tools risk | Low now | High | Revisit only if a specific tool is needed |
| Remaining ~28 skills | Ignore | — | Not aligned to current focus | Low | — | Re-evaluate per-need, not in bulk |

---

## 7. Recommended Folder Structure (adapted to actual local layout)

Your proposed `.agent-os/` paths do not exist locally. Use the real `.agents/` standard (which the repo itself targets) and fold into the amendment plan's slim shape:

```
Agentic OS/
  .agents/
    skills/
      marketing/                 # curated SKILL.md subset ONLY (~12), no evals/tools
        product-marketing/SKILL.md
        aso/SKILL.md
        onboarding/SKILL.md
        paywalls/SKILL.md
        pricing/SKILL.md
        analytics/SKILL.md
        programmatic-seo/SKILL.md
        seo-audit/SKILL.md
        site-architecture/SKILL.md
        competitor-profiling/SKILL.md
        ...
  marketingskills/               # ARCHIVE the full clone (source of truth for re-sync only)
  docs/research/marketingskills-adoption-plan.md   # this report

RunSmart/.agents/product-marketing.md             # written, project-specific
ResumeBuilder/.agents/product-marketing.md        # written, project-specific

# Review workflows live with the other OS workflows (per amendment plan), e.g.:
Agentic OS/.agents/workflows/aso-review.md
Agentic OS/.agents/workflows/onboarding-review.md
Agentic OS/.agents/workflows/seo-growth-review.md
Agentic OS/.agents/workflows/paywall-pricing-review.md
```

Reconcile, don't duplicate: the `distribution-os` per-project scaffolds become the *source content* for each `product-marketing.md`, then `distribution-os` is archived per the amendment plan. Do not run marketing skills, the scaffold, AND distribution-os as three parallel systems.

---

## 8. Phased Implementation Plan

**Phase 0 — Selection (this report).** Done. Shortlist = the 12 Adopt/Adapt skills above. Boundary = SKILL.md only, no evals/tools, ~12 cap.

**Phase 1 — Foundation (highest leverage).**
- Pin the version: record current local skill versions; decide upstream-sync cadence = on-demand only (never auto).
- Curate `.agents/skills/marketing/` — copy the 12 SKILL.md files, leave evals/tools behind.
- Write `RunSmart/.agents/product-marketing.md` and `ResumeBuilder/.agents/product-marketing.md`, assembled from the existing `distribution-os` scaffolds + 2-3 real user quotes each.
- Archive the full `marketingskills/` clone (keep as re-sync source, not active context).

**Phase 2 — RunSmart.** `aso-review` on the live v1.0.3 listing → `onboarding-review` targeting the D7 gate → activation analytics checklist (PostHog). Video/ad-creative deferred.

**Phase 3 — ResumeBuilder.** `seo-audit` of current pages → `programmatic-seo-plan` (gated: 10 hand-quality pages before any scale) → `paywall-pricing-review` → lifecycle emails last.

**Phase 4 — Operating workflow.** Turn the per-app reviews into reusable workflows under `.agents/workflows/`. Add a risk-review gate and a "requires approval before implementation" rule for anything that touches production app code, pricing, or publishes pages.

---

## 9. Risk Review

| # | Risk | Root cause | Impact | Mitigation | Validation test | Decision gate |
|---|---|---|---|---|---|---|
| 1 | Token bloat | Full 377-file clone + tools in context | Slow, costly, noisy agents | SKILL.md subset only; archive clone | Context load measured before/after | Don't proceed if context grows |
| 2 | Generic marketing output | No real `product-marketing.md` | Useless advice, wasted runs | Write per-app context first (Phase 1) | Output names RunSmart/Garmin/ATS specifics unprompted | No skill use before context exists |
| 3 | Agent confusion | 43 overlapping trigger phrases | Wrong skill fires | Cap at 12; remove near-duplicates (competitors vs competitor-profiling) | Ask for ASO → `aso` fires, not 3 skills | >12 only with a reason |
| 4 | Copying workflows that ignore product reality | Skills are generic templates | Plans that don't fit your funnel | Treat skills as frameworks, adapt to data | Each recommendation cites a real metric/constraint | Reject advice with no product anchor |
| 5 | Low-quality programmatic SEO | Scale-first | Google penalty, brand damage | 10 hand-quality pages before scale; unique value per page | Pages pass a human "would I link this?" check | No bulk publish without gate pass |
| 6 | Analytics plan without implementation | Skill outputs a plan, no code | Dashboards that never populate | Pair `analytics` with `growth-analytics`; implementation is a separate approved story | Events fire in PostHog | Plan not "done" until events verified |
| 7 | Over-optimizing pre-scale | Eager tuning | Wasted effort at low N | Defer pricing/churn until enough users | Min user/traffic threshold per skill | Below threshold → skill = Later |
| 8 | Adopting skills needing unavailable tools | `tools/` assume API keys/Composio | Broken runs, dead ends | Ignore tool layer; revisit per-need | Skill runs with no external tool | No tool adoption without a named need |
| 9 | Re-bloating the OS | Adding a parallel marketing silo | Undoes the amendment plan | Fold into `.agents/`; archive distribution-os + clone | Root file/dir count does not rise | Violates amendment → stop |
| 10 | Stale skills / sync treadmill | Chasing upstream | The refresh-treadmill you just killed | Pin version; sync on-demand only | Zero scheduled sync jobs | No auto-sync |

---

## 10. First 5 Implementation Stories

1. **Curate the marketing skill subset.** Copy the 12 shortlisted `SKILL.md` files into `.agents/skills/marketing/`; leave `evals/`, `references/` (load on demand), and `tools/` behind. Archive the full clone. *(Verify: context load does not increase; 12 skills present.)*
2. **Write `RunSmart/.agents/product-marketing.md`.** Assemble from `distribution-os` runsmart scaffold + 2-3 real user quotes. *(Verify: a cold agent describes RunSmart accurately from it alone.)*
3. **Write `ResumeBuilder/.agents/product-marketing.md`.** Same, from the resumebuilder scaffold. *(Verify: same test.)*
4. **Run `aso-review` on RunSmart v1.0.3.** Live listing audit → prioritized action list (no app changes). *(Verify: output is RunSmart-specific, cites the live listing.)*
5. **Run `onboarding-review` for the D7 gate.** Map first-run → activation; identify the one highest-impact fix before 2026-06-24. *(Verify: recommendation ties to a measurable activation step.)*

---

## 11. Recommended First Action

**Write `RunSmart/.agents/product-marketing.md` (Story 2) before touching any skill.** It is the foundation every other skill depends on, the raw material already exists in your `distribution-os` scaffold, and RunSmart's D7 gate on 2026-06-24 makes RunSmart context the most time-sensitive. Skipping it guarantees generic output from everything downstream.

---

*Nothing in this report has been executed. No skills copied, no files pruned, no app or distribution-os files modified. Adoption awaits explicit approval.*
