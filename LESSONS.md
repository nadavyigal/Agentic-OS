# Global Lessons

Save only lessons that are likely to matter again across projects.

## Lesson Index

Distilled 2026-06-12 from per-repo `tasks/lessons.md` files (full detail in `~/.claude/LEARNINGS.md` and `~/.claude/ERRORS.md` for Claude sessions; per-repo lessons files remain canonical for project-specific rules).

- **Supabase: `.maybeSingle()` over `.single()`** — `.single()` 406s on zero/multiple rows; hit independently in RunSmart Web and ResumeBuilder Web.
- **Apple App Review playbook** — visible UI must name the Apple API (HealthKit); never collect name/email after Sign in with Apple; reviewer sign-in failures → check Supabase `provider_disabled` first. (RunSmart builds 9 + 11 rejections, Resumely 2026-06-10.)
- **Custom Info.plist keys** — INFOPLIST_KEY_* silently drops custom keys; use a PlistBuddy Run Script with the generated Info.plist as inputPath and a stamp file as outputPath. (Resumely iOS, 2026-06-03/09.)
- **Supabase RLS migrations** — inspect `pg_class.relkind` first; views need `security_invoker`, not table RLS; prune older permissive policies after adding owner-scoped ones. (RunSmart iOS Garmin migration, 2026-06-12.)
- **iOS ↔ Next.js API contract** — destructure both camelCase and snake_case on shared routes; iOS Codable defaults to snake_case and fails silently with 400s. (Resumely Submit Package, 2026-06-09.)
- **Mobile OAuth** — app-scheme callback (`runsmart://`) + poll server connection state; a successful Safari redirect is not app-side success. (Garmin, 2026-06-11.)
- **node_modules repair** — "Cannot find module" inside node_modules means lockfile drift: `npm ci`, not `npm install`. (RunSmart Web, 2026-06-12.)
- **Live git beats prose dashboards** — rebuild status from parsed truth each refresh; never trust narrative carried across refreshes. (status accretion bug, 2026-06-11.)
- **Never depend on a ritual nobody triggers** — attach improvement-loop checks to rituals that demonstrably run daily, not to phrases or hooks that can silently vanish. (Dead learning loop found 2026-06-12.)
- **Never state product status from memory** — always verify from a live source (git tag, PostHog, `./agentic-os refresh` output) and cite it inline. If no live source is available, say so. (8 sessions of drift found 2026-06-30.)
- **Instructions are not questions** — "create X", "spec Y", "add Z" are instructions; execute them. Only ask when two different interpretations would produce meaningfully different outputs. (Recurring pattern found 2026-06-30.)
- **Manual practices die in 30 days** — any recurring practice introduced without automation fails silently. Wire it into a hook, cron, or daily ritual on day 1. (INTENT-LOG: 0 entries in 28 days, 2026-06-30.)
- **Compound, don't accrete** — before creating a new file, check if a living page for the subject exists. If yes, update it; use the new content as the dated evidence note. Hub pages stale by more than 7 days degrade trust in the whole OS. (Recurring wiki drift 2026-06-30.)
- **Done requires evidence, not completion** — "the feature works" is not evidence. Lint pass, test output, or a PostHog event confirmed in the dashboard is evidence. Log the evidence in the INTENT-LOG entry or the session summary. (Evidence-before-commit theme, 6 of 28 backfilled sessions, 2026-06-30.)

## Lesson Template

Use `TEMPLATES/lesson-template.md` when adding a new lesson.

