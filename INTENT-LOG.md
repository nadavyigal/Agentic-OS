<!-- Last Audit: 2026-06-30 — backfilled 28 entries from wiki-log + memory (2026-06-08 through 2026-06-30) -->
# Intent Log

> **Status: Promoted.** The experiment worked — the 4 seed entries surface durable themes
> (trust, verifiability, experiment-cheaply) that still describe how the OS is run today.
> Manual logging failed (0 entries between June 2 and June 30). This file was backfilled
> from the wiki-log and session memory on 2026-06-30.
>
> **Next step:** wire a lightweight auto-capture into the Stop hook so entries are written
> at session end, not retroactively. See the implementation plan at the bottom of this file.

## Why this exists

The rest of the OS records the **supply side**: decisions made (`DECISIONS.md`), status
(`PROJECT-STATUS.md`), what was built. None of it records the **demand side**: the recurring
asks, the framing, the standing priorities behind individual tasks. This log captures intent,
not transcripts. The signal is the pattern across requests, not any single prompt.

## How to use it (lightweight)

- One entry per meaningful request or session. Most recent first.
- Capture the *intent and why*, paraphrased. Do not paste raw prompts.
- Tag recurring themes so clusters become visible over time.
- Do not log fixes, bug resolutions, or implementation detail. Those live in the repos.

## Format

```
## YYYY-MM-DD - <short title>
**Request:** <paraphrased ask>
**Intent / why:** <the durable goal behind it>
**Themes:** <tag, tag>
```

---

## Entries

## 2026-07-09 - Weekly distribution review: log WP-31/WP-32 into the cycle
**Request:** Run the weekly distribution review per `PROMPTS/distribution-weekly.md`; specifically close the gap the CEO review flagged — WP-31 (Resumely Hebrew ASO) and WP-32 (Facebook-groups posting) were founder-approved and live but never logged into `distribution-os/experiment-log.md` or `weekly-growth-review.md`.
**Intent / why:** Wants the distribution cycle to reflect ground truth, not a 3-week-stale snapshot — the CEO review had explicitly called this a "distribution blind spot" undermining the OS's own trust story. Standing pattern: don't let founder-side actions (manual FB posts, approvals) go dark in the system just because no agent session logged them.
**Themes:** distribution-os, evidence-before-done, cross-session-continuity

---

## 2026-07-01 - Mode tagging system + close out OS-IMPROVEMENT-PLAN-2026-06-30
**Request:** Explore whether Boris Cherny's 5 role archetypes (Prototyper/Builder/Sweeper/Grower/Maintainer) should replace or fold into the executive-os (CEO/COO/CFO/Risk/Analysis) structure; once decided, add it; then review and close every remaining uncommitted or unfinished item in the Agentic OS repo, including the 2026-06-30 improvement plan and 3 older saved plans.
**Intent / why:** Wants the OS to help him move faster as a solo founder, not accrete ceremony — repeatedly pushed back on complexity ("isn't this just more documentation?") until the design earned its keep. Also wants nothing left half-done or silently stale across sessions/tools (Claude, Cursor) — the recurring theme of this whole session was finding and closing gaps between what looked done and what was actually verified.
**Decisions:** Mode is an orthogonal axis (what kind of work) layered onto existing work packets/backlog items as one field, not a replacement for CEO/COO/CFO/Risk (who decides) and not a new "Mode OS" department — added a Mode Contracts table to `AGENTS.md` instead. `distribution-os/` was initially proposed for folding/deletion, then kept as-is after actually reading it — it's real channel-scoring infrastructure, not a redundant shell (self-correction, not the founder's). WP-21 and WP-23 (PostHog LLM observability, ResumeBuilder + RunSmart) were found already merged (PR #98, PR #108) and closed with evidence instead of left as open Draft packets. OS-IMPROVEMENT-PLAN-2026-06-30 fully closed — all 5 problems (status-from-memory, manual-practices-die, evidence-before-done, asking-not-acting, compound-don't-accrete) plus WP-22 (INTENT-LOG auto-capture: Stop hook + `intent_cluster.py` + morning-brief hook health check). Two older saved plans (2026-05-20 setup overhaul, 2026-06-07 Obsidian integration) verified already fully implemented and checked off rather than re-run. Hebrew-first distribution playbook (still draft, unapproved) surfaced in `NEXT-MOVES.md` — a real founder decision it had no path to before.
**Verification:** Wrote the WP-22 completion plan via the writing-plans skill, handed to a Cursor session, then independently re-verified every claim against the repo (not the report) — diffed all 6 commits, reran both test suites (65 + 5 tests, all pass), confirmed the settings.json Stop hook and cli.py insertion points byte-for-byte. Caught one real bug in my own plan (a wrong expected-value assertion in the intent_cluster test fixture) that Cursor correctly fixed rather than forcing. One gap still open: a genuine live Claude Code Stop-hook fire (cwd at the Agentic OS root) hasn't happened from either me or Cursor yet — only simulated by manual invocation.
**Themes:** self-improvement, mode-system, org-design, evidence-before-commit, compound-don't-accrete, cross-tool-handoff, verification, scope-discipline

## 2026-06-30 - Analyse whether prompt intent capture has value in the OS
**Request:** Look at whether prompts to Claude have been captured and if there's value in analysing intent behind them; check if any infrastructure exists.
**Intent / why:** Wants to treat himself as a user of his own OS — understand his own AI usage patterns to improve how he works, not just what he builds.
**Themes:** meta, self-improvement, intent-capture, demand-side-memory

## 2026-06-27 - Close remaining Karpathy wiki gaps (living pages + cross-repo links)
**Request:** Verify Dataview rendering from prior PR; close the cross-repo wikilink leak and query operation pattern; skip raw-sources layer as low-value.
**Intent / why:** Quality of the knowledge layer matters for long-term reuse — broken links and stale hub pages silently degrade trust in everything the vault says.
**Themes:** wiki-quality, compounding, anti-accretion, trust

## 2026-06-27 - Evolve vault to Karpathy living-page pattern
**Request:** Re-read the Karpathy wiki gist and evolve the vault: compounding living pages that update in place, and an auto-generated index that can't drift.
**Intent / why:** The vault was accreting (adding dated notes) but not compounding (updating the canonical page). A living page stuck at a stale Current State is the same as not having one.
**Themes:** compounding, living-pages, wiki-quality, anti-accretion

## 2026-06-26 - Weekly plan + status correction
**Request:** Morning brief, then weekly progress summary; founder corrected the plan mid-session when he found it missed already-completed Garmin work and a merged Resumely PR.
**Intent / why:** Wants status derived from ground truth (git, PostHog), not from prose memory. Plan should reflect what is actually open, not what was open when the session started.
**Themes:** status-truth, weekly-rhythm, verifiability, planning

## 2026-06-24 - D7 activation readouts for both apps
**Request:** Run and store the D7 activation readout for RunSmart and Resumely; update OKR baselines in the OS; create an exec→CEO→action plan prompt.
**Intent / why:** Paywall and post-launch decisions must be data-grounded, not gut-feel. D7 is the first concrete signal of whether the product works for real users.
**Themes:** metrics, activation, evidence-before-commit, product-decisions

## 2026-06-24 - Garmin Gate-4 fixes + RunSmart iOS 1.0.4 submitted
**Request:** File the day's implementation session (HRV/wellness fixes, Body Battery root cause, Garmin Wellness entry point), sync Agentic OS, and confirm submission.
**Intent / why:** Garmin commercial partnership is the primary distribution moat for RunSmart. Every gate must be documented and closed cleanly, not just shipped and forgotten.
**Themes:** garmin-partnership, distribution, ship-clean, documentation

## 2026-06-26 - Secret-scan guardrails in both product repos
**Request:** Add pre-commit secret-scan hooks to RunSmart and ResumeBuilder; create a global git-guard for main-branch commits.
**Intent / why:** One leaked key destroys user trust and creates a legal liability. Automation is the only reliable prevention — a rule nobody reads is not a guardrail.
**Themes:** security, automation, trust, guardrails

## 2026-06-26 - Model routing policy across all products
**Request:** Pin subagent model assignments in RunSmart and ResumeBuilder; write a global routing policy in GLOBAL-TOOL-USAGE.md.
**Intent / why:** Uncontrolled model selection means unpredictable cost and quality. A written routing policy lets any session make consistent decisions without re-deriving them.
**Themes:** cost-control, consistency, policy-formation, model-routing

## 2026-06-26 - Token and cost observability
**Request:** Build a usage collection script (collect_usage.py) and understand where the ~$8.6k/30d is coming from.
**Intent / why:** Flying blind on AI cost is a founder risk. Cache-reads from long sessions are the dominant driver — need to see it to manage it.
**Themes:** cost-visibility, observability, anti-bloat

## 2026-06-26 - Trim global CLAUDE.md static context
**Request:** Trim the global CLAUDE.md — it had grown too large and was wasting context on every session.
**Intent / why:** Long context files eat tokens on every session and slow cold starts. The cost of a bloated instruction file is paid on every single prompt.
**Themes:** anti-bloat, context-efficiency, static-context-diet

## 2026-06-24 - Plan-generator eval harness for RunSmart
**Request:** Build an eval harness for the RunSmart plan-generator; run it against a baseline; fix enforcement gaps surfaced by the eval.
**Intent / why:** Shipping AI features without evals means you don't know if they regress. The eval harness is the only honest quality gate.
**Themes:** eval, quality-gate, evidence-before-commit, ai-quality

## 2026-06-24 - ResumeBuilder eval baseline
**Request:** Ship an eval harness for the resume optimizer; establish a 100%/0 critical baseline.
**Intent / why:** Same pattern as RunSmart — product has AI at its core but no quality measurement. An eval is the minimal honest step before any optimization claim.
**Themes:** eval, quality-gate, evidence-before-commit, ai-quality

## 2026-06-22 - Stanford STORM method adoption
**Request:** Verify the STORM research method, adopt it into the OS (Agentic OS runbook + vault prompt + Claude.ai Project), and create a plan for the next day.
**Intent / why:** Research currently takes hours because it's done ad-hoc. A reusable structured method with grounded citations compresses hours to minutes.
**Themes:** research-methods, tool-adoption, efficiency, anti-hallucination

## 2026-06-22 - Automate wiki maintenance (nightly sweep)
**Request:** Close index gaps surfaced by a nightly sweep dry run; wire up overnight triage automation.
**Intent / why:** Manual lint passes are always forgotten. Automation is the only thing that keeps the wiki from silently degrading between sessions.
**Themes:** automation, self-maintenance, anti-drift, ops

## 2026-06-21 - Study system prompt leaks for reusable agent-prompt patterns
**Request:** Read the asgeirtj/system_prompts_leaks repo for structure only; extract what's missing from the Agentic OS; ship the useful gaps.
**Intent / why:** Frontier AI labs have solved many agent-instruction problems already. Wants to learn from their structure without copying proprietary content.
**Themes:** research, agent-design, meta, steal-like-an-artist

## 2026-06-20 - Resolve ATS claim defensibility + skills security audit
**Request:** Close the open ATS claim risk (defensibility of the numeric Resumely Match Score in public copy); scan all installed skills for prompt injection; audit wiki for contradictions.
**Intent / why:** Two separate trust problems: product claims that could expose the business legally, and skills that could be hijacked if unvetted. Both need resolution before shipping.
**Themes:** legal-risk, security, trust, anti-drift

## 2026-06-20 - Positioning battlecards for RunSmart and Resumely
**Request:** Consolidate locked positioning and do-not-claim guardrails into a single drift-check artifact per product.
**Intent / why:** Positioning keeps drifting across notes, PRs, and copy — no canonical place to check before writing. A battlecard is the single source of truth for what can and cannot be claimed.
**Themes:** brand-clarity, single-source-of-truth, anti-drift

## 2026-06-19 - Both iOS apps shipped — update OS status
**Request:** Update vault hub pages and Agentic OS after RunSmart v1.0.3 and Resumely v1.1 both cleared Apple review.
**Intent / why:** Launch-and-ship phase is closed; the OS must reflect that before post-launch priorities are set. Stale "in review" status produces wrong decisions.
**Themes:** status-truth, milestone, post-launch

## 2026-06-18 - Smart connections + High Agency advisor check
**Request:** Implement 4 smart connections from the weekly review; get a High Agency POV on whether any are rumination vs. action.
**Intent / why:** Observations without actions are just noise. The HA advisor forces the "is this Level 0 or Level 1?" check before committing work to the backlog.
**Themes:** high-agency, anti-rumination, connection-making, decision-quality

## 2026-06-18 - Weekly Obsidian Review
**Request:** Run weekly review after CEO review; update hub pages that say "in review" when both apps are live.
**Intent / why:** Hub pages are what future sessions read first. If they're stale, every downstream decision starts from wrong information.
**Themes:** status-truth, weekly-rhythm, hub-freshness, trust

## 2026-06-17 - PostHog analytics QA + OS status-truth root cause
**Request:** Full PostHog QA on both live apps; diagnose why the OS still shows "in review" when apps are live; fix the launchd refresh that silently died.
**Intent / why:** Recurring pattern: OS claims diverge from reality within days of any manual update. Wants evidence-grounded status, not prose that nobody updates.
**Themes:** trust, verifiability, status-truth, automation

## 2026-06-16 - Resumely brand video after unexpected App Store approval
**Request:** Pivot mid-session from CEO strategy to brand video when Resumely got Apple approval during the session.
**Intent / why:** Launch window is short and arbitrary. The highest-ROI move in the first 48 hours post-approval is distribution, not strategy.
**Themes:** distribution, launch-window, velocity, bias-to-action

## 2026-06-15 - Garmin production roadmap ingested and tracked
**Request:** Synthesize the full Garmin production plan, commercial terms, and four production gates into the OS after a 6-hour implementation session.
**Intent / why:** Garmin is the primary distribution moat for RunSmart. Every gate and deadline must be documented in the OS — knowledge that lives only in session memory evaporates.
**Themes:** garmin-partnership, distribution, documentation, long-horizon

## 2026-06-12 - Full three-layer OS audit + broken learning loop fix
**Request:** Audit all three OS layers for truth and operational health; find why the self-improvement loop was dead.
**Intent / why:** The Stop hook was silently missing from settings.json, so lessons never got written. Wants the OS to actually learn from sessions, not just claim to.
**Themes:** trust, verifiability, self-improvement, automation, ops

## 2026-06-12 - CEO Review + weekly review
**Request:** Run weekly and CEO review after the OS audit; surface queued decisions and what is actually open vs. deferred.
**Intent / why:** Weekly review is the forcing function that prevents deferred decisions from silently becoming blockers. Without it, the backlog grows invisibly.
**Themes:** weekly-rhythm, decision-quality, ceo-lens, planning

## 2026-06-10 - Emergency App Store rejections (both apps, same day)
**Request:** Fix both apps' App Store rejections same day — Apple sign-in disabled on review device.
**Intent / why:** Review windows are short and arbitrary. Any day lost is potentially weeks. Bias toward same-day resolution over careful planning.
**Themes:** velocity, bias-to-action, ship-clean, app-store

## 2026-06-09 - High Agency framework + advisor infrastructure
**Request:** Adopt George Mack's High Agency framework; wire it into Claude.ai Projects, the decision template, and the weekly review template.
**Intent / why:** Recurring trap: studying and planning instead of doing. Wants a persistent advisor that asks "is this Level 0 or Level 1?" before any decision gets logged.
**Themes:** high-agency, meta, anti-rumination, decision-quality, advisor

## 2026-06-08 - Vault + wiki infrastructure bootstrap
**Request:** Bootstrap the Obsidian vault with the Karpathy LLM Wiki pattern; build the RunSmart domain wiki; create the Daily Operations Map.
**Intent / why:** The thinking layer was scattered across files with no index, no navigation, and no compounding. Wants a vault a Claude session can read cold and understand without context.
**Themes:** infrastructure, wiki-quality, navigation, cold-start, compounding

---

## 2026-06-02 - Make Agentic OS top-tier
**Request:** Move the OS from "good" to "top tier" by making it more truthful, current, and operational, not by adding more files. Start by upgrading the dashboard refresh to parse local project task files.
**Intent / why:** Distrust of curated narrative status; want state provably derived from source evidence with a confidence rating. Treat hand-written summaries as fallback, not proof.
**Themes:** trust, verifiability, anti-bloat, dashboards

## 2026-06-02 - Ship in reviewable checkpoints
**Request:** Create a PR for the parser work, then start Phase 1 (freshness/staleness).
**Intent / why:** Prefers shipping in clean, reviewable increments while keeping momentum; one phase at a time with verification before moving on.
**Themes:** velocity, reviewable-increments, one-story-at-a-time

## 2026-06-02 - Add a demand-side memory dimension
**Request:** Consider logging prompts/requests (plans and asks), not fixes, as another dimension of understanding. Unsure if it is worth it.
**Intent / why:** Sense that intent behind requests is currently invisible and might improve how agents anticipate and frame work. Wants to experiment cheaply and judge later.
**Themes:** meta, self-improvement, experiment-cheaply

## 2026-06-02 - Create the log non-invasively, audit later
**Request:** Proceed to Phase 2; create INTENT-LOG.md without impacting anything; revisit in 1-2 weeks to audit whether it makes sense and decide what to do with it.
**Intent / why:** Low-risk experimentation: add the surface, change nothing else, evaluate with real evidence before committing to or discarding it.
**Themes:** experiment-cheaply, reversible, evidence-before-commit

---

## Implementation Plan — Auto-capture (2026-06-30, executed 2026-07-01)

Manual logging failed completely (0 entries in 28 days). The fix is automation via the Stop hook.

### What to build

**Step 1 — Stop hook writes one intent entry per session.**
The Stop hook already fires when a Claude session ends. Add a prompt to it:
at session end, Claude writes a single INTENT-LOG entry (paraphrased request, intent/why, 2-3 theme tags) and prepends it to this file. No human action required.

**Step 2 — Monthly theme cluster.**
Once a month (can be part of the existing monthly lint pass), a script reads all entries, extracts theme tags, counts frequency, and appends a `## Theme Clusters — YYYY-MM` section to this file. This surfaces the pattern across requests without reading every entry.

**Step 3 — Morning brief reads top themes.**
The morning brief currently reads PROJECT-STATUS.md. Add a one-line pull from the most recent theme cluster: "Top themes this month: trust, verifiability, anti-bloat." This makes the demand-side pattern visible every day.

### Files to touch

| File | Change |
|---|---|
| `~/.claude/settings.json` | Add Stop hook that runs intent-capture prompt |
| `scripts/agentic_os/intent_cluster.py` | New — reads entries, counts theme tags, appends cluster |
| `PROMPTS/morning-brief.md` | Add one line: pull top themes from latest cluster |
| This file | Auto-appended by the hook |

### Sequence
1. Write `intent_cluster.py` (standalone, no dependencies)
2. Add Stop hook to settings.json (reuse the existing hook pattern)
3. Test: end a session and verify the entry appears
4. Add theme pull to morning-brief on next morning-brief session
