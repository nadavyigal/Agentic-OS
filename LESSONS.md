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
- **File-sync conflict copies are vault rot, not tool artifacts** — macOS/iCloud sync drops `<name> 2.md` duplicates beside real notes; any tool that scans the vault (brain map generator, linters) must skip `<base> N.md` shadows or they become phantom nodes and fake link hubs. Verify a "generator/re-save artifact" premise against the filesystem before excluding a file from lint: the Brain Map's `[[CLAUDE 2]]` links traced to real sync-duplicate files, not to Excalidraw. (Brain map investigation, 2026-07-13.)
- **PostHog: confirm the project before trusting any read** — the MCP reports an "active project" that is not necessarily the one it queries. On 2026-07-20 it reported project 171597 "Running coach" as active while the first several queries returned ResumeBuilder data, and an empty result was nearly reported as a RunSmart analytics outage. Always call `switch-project` explicitly, then confirm with an event-name query that the returned data belongs to the product you think you are reading. Verified mapping (re-confirmed via `projects-get` 2026-07-20): **RunSmart = 171597 "Running coach"**, **Resumely = 270848 "ResumeBuilder AI"**, plus an unrelated third project **327190 "Michal's page"** in the same org. RunSmart's project contains zero Resumely events over 60 days, so cross-contamination in a result set means you are reading the wrong project, not a data problem. (Near-miss false outage report, 2026-07-20.)
- **A hand-maintained layer under a machine-refreshed timestamp rots invisibly** — `dashboard/portfolio-hq-manual.json` is never written by `./agentic-os refresh`, yet the page rendered `asOf` as today, so stale claims wore a current date. A current-looking stamp over stale content is worse than an obviously old page, because it defeats the reader's own staleness instinct. Fix: every manual block carries its own `verified` date, and the refresh flags any block older than 7 days as a cross-layer issue that downgrades trust. Any hand-maintained input rendered next to auto-refreshed data needs its own independent freshness stamp. (47 stale-claim matches found, 2026-07-20.)
- **Done requires evidence, not completion** — "the feature works" is not evidence. Lint pass, test output, or a PostHog event confirmed in the dashboard is evidence. Log the evidence in the INTENT-LOG entry or the session summary. (Evidence-before-commit theme, 6 of 28 backfilled sessions, 2026-06-30.)

## Lesson Template

Use `TEMPLATES/lesson-template.md` when adding a new lesson.

