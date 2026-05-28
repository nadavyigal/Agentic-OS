---
type: experiment-card
id: <rs|rb>-<channel>-<nnn>
status: proposed
product: <RunSmart | ResumeBuilder>
channel: <channel>
created: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
---

# Experiment: <short name>

## Hypothesis

If we <do specific change>, then <metric> will <direction> by <magnitude> within <timebox>, because <underlying belief>.

## Target Audience

The specific segment affected.

## Asset Needed

The concrete artifact to produce.

## Success Metric

Canonical metric name from `metrics-schema.md`. Target value. Measurement window.

## Expected Result

Numeric or directional target with confidence range.

## Risk

What could go wrong, including downside to existing flow.

## Mitigation

How to bound the downside (kill switch, holdout group, partial rollout).

## Scoring

| Dimension | Score (1-5) |
|---|---|
| Impact | |
| Confidence | |
| Effort (subtracted) | |
| Speed | |
| Founder fit | |
| Strategic fit | |

Score = Impact + Confidence + Speed + FounderFit + StrategicFit − Effort = **<value>**

Decision threshold: do-now >= 15, later 10–14, reject < 10.

## Decision

`do-now` | `later` | `reject`

## Status

`proposed` | `approved` | `queued` | `running` | `paused` | `done-worked` | `done-failed` | `rejected`

## Start / End

Start: <YYYY-MM-DD>
End: <YYYY-MM-DD>

## Result (filled at end)

- Actual metric value:
- Compared to target:
- What changed:
- Lesson captured? <yes/no, link to lesson row>

## Notes

(Context, links, screenshots.)
