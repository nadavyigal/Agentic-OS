# Experiment Schema

Canonical structure for every experiment row. Used by `experiment-log.md`, Notion Experiment Backlog, and `templates/experiment-card-template.md`.

## Required Fields

| Field | Type | Notes |
|---|---|---|
| `id` | Text | `{rs|rb}-{channel}-{nnn}` |
| `product` | Enum | RunSmart, ResumeBuilder |
| `channel` | Enum | One of the channels in `channel-backlog.md` |
| `hypothesis` | Text | One sentence, falsifiable |
| `target_audience` | Text | Who is affected |
| `asset_needed` | Text | The concrete artifact |
| `time_required` | Text | Days |
| `success_metric` | Enum | Canonical metric name from `metrics-schema.md` |
| `expected_result` | Text | Numeric or directional target |
| `risk` | Text | What could go wrong |
| `mitigation` | Text | How to limit downside |
| `impact` | Number 1–5 | |
| `confidence` | Number 1–5 | |
| `effort` | Number 1–5 | |
| `speed` | Number 1–5 | |
| `founder_fit` | Number 1–5 | |
| `strategic_fit` | Number 1–5 | |
| `score` | Number | Computed: I + C + S + FF + SF − E |
| `decision` | Enum | do-now, later, reject |
| `status` | Enum | proposed, approved, queued, running, paused, done-worked, done-failed, rejected |
| `start_date` | Date | |
| `end_date` | Date | |
| `result_summary` | Text | After end |
| `lesson_captured` | Boolean | After end |

## Status Lifecycle

```
proposed
  → approved (founder + score >= threshold)
    → queued (waiting for slot)
      → running (start_date set)
        → done-worked  (target hit)
        → done-failed  (target missed)
        → paused        (returns to queued or rejected)
  → rejected (score < threshold or founder kill)
```

## Hypothesis Format

`If we {do specific change}, then {metric} will {direction} by {magnitude} within {timebox}, because {underlying belief}.`

Bad: "Improve onboarding."
Good: "If we replace the second onboarding screen with a sample plan preview, then `runsmart.activation.first_plan_generated` will move from 42% to 55% within 14 days, because users currently bounce when asked for run preferences before seeing what the product produces."

## Single-Hypothesis Rule

One experiment tests one change. If multiple changes ship together, the experiment is bundled and the result is uninterpretable.

Exception: a campaign is allowed to bundle multiple coordinated assets toward one goal. Each individual asset can still be tracked as a sub-experiment under the campaign for measurement.

## Sample Size And Time Box

Use the worksheet from `marketingskills/skills/ab-testing/SKILL.md` for traffic-driven experiments. For low-traffic flows, default to:

- Minimum 14 days
- Minimum 30 conversions per variant for any A/B
- For directional decisions (no A/B), compare pre 4 weeks vs post 4 weeks

## Decision Thresholds

- Hit target: keep, expand
- Within 20% of target: iterate one element, run again
- Below 20% of target: kill or pivot. Document the lesson.

## Conflict With Lessons File

Before creating a new experiment, the agent checks `lessons.md` for failed approaches. If a similar approach is logged as failed, the experiment is rejected automatically with a reference to the lesson.
