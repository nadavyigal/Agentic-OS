# Status Schema

The contract the dashboard refresh parser (`scripts/agentic_os/cli.py`) reads from each
project's local task files. A project that follows this schema in `tasks/progress.md` can
reach **High** source confidence; without it, status is derived and caps at **Medium**.

This is the standard referenced by the Dashboard Trust Rule in `DECISIONS.md`.

## Preference order

1. **`tasks/progress.md`** - if present, it is the preferred status source. Use the keyed
   `Key: Value` format below.
2. **Derived** - if `progress.md` is absent, status is derived from `tasks/todo.md` +
   the latest `tasks/session-log.md` entry + `tasks/MEMORY.md`.
3. **None** - if no task files exist, the project is Low (narrative only) or Unknown.

## `tasks/progress.md` keys

One `Key: Value` per line, at the top of the file. Recognized keys (case-insensitive):

| Key | Maps to | Notes |
| --- | --- | --- |
| `Status` | status | e.g. `In Progress`, `Active`, `Pre-release`. |
| `Current Phase` | currentPhase | The headline state shown in the status table. |
| `Active Story` | activeStory | What is being worked on now. |
| `Last Completed Story` | lastCompletedStory | Most recent finished story. |
| `Next Recommended Story` | nextRecommendedStory | Drives the "Next Action" column. |
| `Blockers` | blockers | Semicolon-separated list. `—` / `none` = empty. |
| `Risks` | risks | Semicolon-separated list. |
| `Last Validation` | lastValidation | Evidence sentence. See vocabulary below. |
| `Last Updated` | lastUpdated | `YYYY-MM-DD`. Feeds freshness. |
| `Latest QA Report` | qaNeeded | Path or `—`. |
| `Estimated Completion` | estimatedCompletion | Free text or percent. |

Lines starting with `#`, `|`, `-`, `>`, or `*` are ignored, so tables and bullets below the
keyed block do not interfere. Only the first occurrence of each key is used. A value of
`-`, `—`, `none`, `n/a`, `tbd`, `pending`, or empty is treated as no value.

## Validation evidence vocabulary

Source confidence is **High** only when `Last Validation` (or, for derived projects, the
latest session-log `### Validation` block) contains positive evidence and no negation.

- **Positive signals:** `pass` / `passed` / `passing`, `succeeded`, `success`, `green`,
  `verified`, `build succeeded`, `tests passed`, `✓`, `✅`.
- **Negations that block High:** `not validated/run/done/tested/verified`, `no validation`,
  `untested`, `unverified`, `unclear`, `validation pending`, `pending verify`.

Write the real evidence: what was built/tested, the result, and the date. Example:
`Full xcodebuild test passed 53 XCTest + 5 Swift Testing on 2026-06-01.`

## Confidence levels

| Level | Meaning |
| --- | --- |
| High | Task file parsed and validation evidence found. |
| Medium | Task file parsed but validation unclear. |
| Low | No task files; existing dashboard narrative only. |
| Unknown | No reliable source (missing path or no task files and no narrative). |

## Freshness and downgrade

Freshness is the age of the newest of `Last Updated` and the last git commit date:

| Label | Age |
| --- | --- |
| Fresh | <= 2 days |
| Needs Review | 3-7 days |
| Stale | > 7 days |
| Unknown | no date found |

**Stale evidence downgrades confidence one level** (High -> Medium -> Low -> Unknown): an
inactive repo cannot keep a confident status.

## Minimum to reach High

A project reaches High when its `tasks/progress.md` has a `Current Phase`, a
`Next Recommended Story`, a `Last Validation` line with positive evidence, and a recent
`Last Updated` (within 7 days, kept current by ongoing commits). Use
`TEMPLATES/progress-template.md` as the starting point.
