# Channel Prioritization Workflow

Run during the monthly strategy review (`workflows/12-monthly-strategy-review.md`) or whenever a channel is suspect. Not weekly.

## Goal

Update `channel-backlog.md` so each channel has a current score, tier, and clear next step.

## Inputs

- `distribution-os/channel-backlog.md`
- Last 4 weekly reports
- `experiment-log.md` rows linked to each channel
- `lessons.md`

## Steps

### 1. Pull recent evidence per channel

For each channel in the backlog (per product):

- Count experiments run in the last 90 days
- Count wins / losses
- Estimate average effort hours
- Note any qualitative lesson logged

### 2. Re-score

Use the dimensions in `channel-backlog.md`:

```
ChannelScore = Reach + Conviction + LeverageOverTime + FounderFit + StrategicFit - OngoingEffort
```

Lock current scores side by side with prior scores. Highlight any movement >= 2.

### 3. Re-tier

- A: at least one channel must remain A per product. Move out if score < 15 for two consecutive months.
- B: trigger-based. If the trigger fired but no experiment ran, demote to C.
- C: park. If a C channel has not moved in 6 months, kill.

### 4. Decide next step per A channel

For each A channel, name the next experiment or maintenance task. If neither exists, demote the channel.

### 5. Apply the kill list

For each channel below threshold or stagnant:

- Move to bottom of `channel-backlog.md` under "Killed"
- Add one-line reason and date
- Cancel any queued experiments tied to it

### 6. Output

- Updated `channel-backlog.md`
- A monthly channel summary appended to `weekly-growth-review.md` under that week's report
- Updated Notion: Command Center channel statuses + Experiment Backlog rejections
