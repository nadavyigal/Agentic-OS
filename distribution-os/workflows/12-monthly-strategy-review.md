# Monthly Strategy Review Workflow

Run on the first weekly cycle of each month. Replaces the standard weekly cycle that week.

## Goal

Step back from execution. Decide what to keep, what to kill, what to start.

## Inputs

- Last 4 weekly reports
- `channel-backlog.md`
- `experiment-log.md`
- `lessons.md`
- Metrics dashboard with monthly summary

## Steps

### 1. Read last month

Pull the last 4 weekly reports. Note:

- Wins (>= 2 lessons captured as working)
- Losses (>= 2 lessons captured as failed)
- Drift (weeks where the focused product wasn't really focused)
- Bottleneck movement (did the funnel weak point change?)

### 2. Re-score channels

Run `workflows/03-channel-prioritization.md`. Update `channel-backlog.md`.

### 3. Re-pick A channels

For each product, decide:

- Which A channels stay
- Which become B
- Which get demoted to C or killed
- Any new channels to admit

### 4. Decide the next month's focus pattern

Default: 3 weeks RunSmart focus + 1 week ResumeBuilder focus, or 2-2, or 4-0 if one product needs concentrated work. Document the choice in `distribution-command-center.md`.

### 5. Pick monthly themes

For the focused product(s), pick 1 theme per week (not 4 themes simultaneously).

### 6. Update operating principles only if needed

If a principle has been violated repeatedly with good reason, update it. Otherwise leave them alone — they only work if they outlast disagreement.

### 7. Capture promoted lessons

Lessons that have repeated >= 3 times across products move to `~/.claude/LEARNINGS.md`. Failed approaches that repeated move to `~/.claude/ERRORS.md`.

### 8. Output

- Monthly review entry at top of `weekly-growth-review.md`
- Updated `channel-backlog.md` and `distribution-command-center.md`
- New month plan in Notion Command Center
- Updated `~/.claude/LEARNINGS.md` and `~/.claude/ERRORS.md` if applicable

### 9. Anti-patterns

- Picking the same focused channel for 8 weeks straight without a clear reason
- Changing strategy weekly
- Promoting a channel after one good week
- Killing a channel after one bad week
- Adding more channels because something feels stagnant — usually the answer is fewer
