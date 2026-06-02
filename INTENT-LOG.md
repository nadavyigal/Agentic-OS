# Intent Log

> **Experimental. Not wired into anything.** This file is a standalone, demand-side log of
> requests and intent. Nothing reads it, no pipeline depends on it, and it changes no behavior.
> It exists to test whether capturing *what is asked for and why* (not the fixes or
> resolutions) adds a useful dimension of understanding.
>
> **Audit on or after 2026-06-16** (roughly two weeks in): re-read it and decide one of:
> keep as-is, promote into the memory system / a real workflow, or delete it.

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
