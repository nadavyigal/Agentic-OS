# Work Packet

- Status: Ready
- Mode: Grower
- Source: dashboard/status.json — "WP-29 S5 anonymous-session carryover is next"
- Workflow pattern: normal
- Input trust: trusted
- Success signal: an anonymous ATS check survives signup and appears in the new account's dashboard
- Model route: Claude Opus

## Owner Role
Full-stack engineer

## Project
ResumeBuilder AI (Web) — `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`

## Goal
Carry anonymous ATS-check results through signup into the new account, closing WP-29 S5.

## Context
WP-43 Tier A shipped the free ATS Checker entry funnel (PR #115, 2026-07-11): hero CTA, styled dropzone, live checklist, URL-path nudge, LinkedIn thin-scrape warning, mobile login reposition. Those changes get an anonymous user to *complete a check*. S5 is the step that stops that work leaking: right now the result does not follow the user through signup, so the funnel's payoff is discarded at the account boundary.

Web is the top-of-funnel for the iOS app, so this compounds with the Resumely iOS activation work in WP-48.

## Read First
- AGENTS.md, CLAUDE.md
- tasks/progress.md (2026-07-11 WP-43 entry)
- tasks/work-pack-wp-43-free-ats-checker-entry-activation.md
- tasks/lessons.md

## Task
Carry the anonymous check result (score, parsed resume reference, job description) through the signup flow into the authenticated dashboard. Decide and document the persistence mechanism (server-side anonymous session vs signed client token) before implementing.

## Constraints
- No schema change without surfacing it first.
- No new npm dependencies without asking.
- Do not run migrations or deploy without explicit approval in the current message.
- If the fix expands past 3 unexpected files, stop and surface it.

## Validation
`npx tsc --noEmit` clean; `npx eslint` on touched files with no new errors; targeted test covering anonymous-check → signup → dashboard carryover. Per `~/.claude/ERRORS.md` 2026-06-12: if node_modules is broken, use `npm ci`, never `npm install`.

## Completion Gate
Update tasks/todo.md, tasks/progress.md, tasks/session-log.md.

## Final Output
What changed, files changed, commands run, validation evidence, remaining risks, next recommended action.
