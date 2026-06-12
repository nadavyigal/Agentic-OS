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

## Lesson Template

Use `TEMPLATES/lesson-template.md` when adding a new lesson.

