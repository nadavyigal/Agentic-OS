# Global Self-Improvement

The global OS should learn from repeated issues without becoming noisy.

## Self-Learning Loop

After cross-project mistakes, repeated issues, bad planning, bad assumptions, or user corrections:

1. Add a lesson to `LESSONS.md`.
2. Convert the lesson into a short reusable rule.
3. If the lesson applies to a specific project, also update that project's local `tasks/lessons.md`.
4. If the lesson changes a workflow, update the relevant global workflow or prompt.
5. Do not add noisy lessons. Only save lessons that are likely to matter again.

## What Counts As A Lesson

Save a lesson when it is:

- Repeated.
- Expensive.
- Easy to forget.
- Relevant across projects.
- Likely to improve future agent behavior.

Do not save:

- One-off preferences.
- Temporary bugs.
- Obvious reminders.
- Project details that belong only in a local project OS.

## Lesson Format

Use `TEMPLATES/lesson-template.md`.

Keep each lesson short:

- Context
- Mistake or issue
- Reusable rule
- Applies to
- Follow-up updates made

## Automation Gate

Before shipping any new recurring practice, ask: "Will this survive if nobody thinks about it for 30 days?"

- If **yes** (it's wired into a hook, cron, or daily ritual): ship it.
- If **no** (it requires human memory or discipline): add automation on day 1, or don't ship the practice at all.

A practice that requires human memory is not a practice. Evidence: INTENT-LOG (0 entries in 28 days), Stop hook (silently vanished), launchd refresh (exited 126 with no alert), learning loop (dead for 3+ weeks). All failed for the same reason.

## Executive Lessons Loop (Layer 8)

Executive-level lessons (CEO, CFO/Monetization, or Analysis) live in
`executive-os/EXECUTIVE-LESSONS.md`, not in `LESSONS.md`. Save only reusable
executive lessons that improve future strategy, finance, or research behavior; skip
noisy details.

If an executive lesson also affects local product execution, update the relevant
project's local `tasks/lessons.md` as well. If it changes an executive rule or
workflow, update the relevant file in `executive-os/`.

