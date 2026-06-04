# Global Agentic OS Visual Dashboard

This is a lightweight static dashboard suite for the Global Agentic OS. It does not replace `../DASHBOARD.md`; it is a visual companion generated from `../PROJECT-STATUS.md`. Three pages share one dark design and a common top nav:

- **Command Center** (`index.html` / `command-center.html`): plan the next move, run a workflow, copy project prompts, or talk to any OS.
- **Orchestration Map** (`orchestration.html`): the layered system map, Layers 0 to 9.
- **Project Status** (`project-status.html`): project cards, action board, decision board, QA board.
- **Executive** (`executive.html`): portfolio overview, focus, risk, dirty repos, blocked projects, and per-project prompts.
- **Decisions** (`decisions.html`): open portfolio decisions and recommendations.
- **Metrics** (`metrics.html`): honest metric status, QA evidence, and missing data state.
- **Data Flow** (`data-flow.html`): how local files and git evidence become dashboard data and copy-ready prompts.

## One Command

Run the morning command from the repo root to refresh local evidence, sync generated dashboard files, verify JSON/links, serve the dashboard, and open the Command Center:

```bash
./agentic-os morning
```

Available commands:

- `./agentic-os morning`: refresh, verify, serve `dashboard/`, and open `index.html`.
- `./agentic-os refresh`: refresh files only, no server.
- `./agentic-os serve`: serve the current dashboard only.
- `./agentic-os verify`: parse dashboard JSON, check embedded fallbacks, verify local links, and run `git diff --check`.

No backend, database, authentication, paid service, or build step is required. When served by the local static file server, pages load `status.json`; opened via `file://`, they use embedded JSON fallbacks.

## One process, one source of truth

There is exactly one process: `./agentic-os morning`. It refreshes evidence, surfaces every saved plan, rebuilds the brief, updates the HTML, verifies, and serves the dashboard on localhost. There is no separate "write the brief" step.

Everything a human reads first — `summary.overallStatus`, `summary.bestNextAction`, the priority board, the per-project cards — is **rebuilt from parsed repo truth on every run**:

- The headline and priority board are derived from each repo's `tasks/progress.md` (or `tasks/todo.md` + latest `tasks/session-log.md` when progress.md is absent). The two shippable apps get their next step inline; support repos show their phase.
- High-confidence per-project cards are overwritten from parsed truth, so a card can never show prose its repo disproves.
- **Saved Plans & Requests**: every plan/spec/GTM you saved (scanned from `docs/superpowers/plans`, `docs/plans`, `docs/superpowers/specs`, `docs/specs`, and the `*plan*` files under `.agent-os/distribution`) is listed per project, newest first, with GTM always kept in view and a total count so nothing looks hidden.

Because the brief is re-derived from the repos every run, stale hand-written prose is structurally impossible — the failure where the dashboard showed "build 6 in review" after build 8 shipped cannot recur. The dashboard's "Live from repos" tag shows the refresh time and how many plans were surfaced.

## Files

- `index.html`: Command Center home page. Self-contained dark theme; reads `status.json` and uses `cc-data` fallback.
- `command-center.html`: compatibility alias for the Command Center.
- `project-status.html`: Project Status dashboard. Dark theme via `styles.css`; reads `status.json`.
- `orchestration.html`: layered Orchestration Map (Layers 0 to 9) with embedded status JSON.
- `executive.html`: Executive overview page backed by `status.json`.
- `decisions.html`: Decision board page backed by `status.json`.
- `metrics.html`: Metrics and QA page backed by `status.json`.
- `data-flow.html`: Data-flow explanation page backed by `status.json`.
- `styles.css`: dark theme for `index.html` (palette shared with the other two pages).
- `status.json`: easy-to-edit dashboard data copied from `PROJECT-STATUS.md`.
- `README.md`: this usage note.

## OS Command Center

`index.html` is the first screen for the local OS. It is fully static and respects the guardrails below: no backend, no API keys, no chat box. The dominant answer is "what should I do next?", backed by Today’s Focus, blockers, one-command status, project health, and copy-ready delegation cards.

The main sections are:

- **Daily Run Result**: last OS command, check state, recommended repo prompt, and the last project prompt copied in this browser.
- **Plan**: priority board and next planning moves.
- **Monitor**: project health, blockers, dirty flags, stale flags, and next action per project.
- **Delegate**: compact agent cards with role, when to use, suggested task, evidence, and collapsed prompt preview.
- **Progress**: one copy-ready next prompt per project repo, including Agentic OS.
- **Run**: command cards for morning, refresh, verify, serve, and review prompts.
- **Learn**: links into memory, lessons, decisions, and session-end updates.

The Command Center reads `status.json` on localhost and falls back to the embedded `<script id="cc-data">` JSON block when opened directly.

## Update Status

When status changes, run `./agentic-os refresh` from the repo root. The refresh layer updates `status.json`, the embedded Project Status fallback, generated markdown status files, Executive OS status, and the Command Center fallback.

## Scope Guardrails

- Keep the Markdown dashboard.
- Keep this static and manual-update-friendly.
- Do not add a database.
- Do not add authentication.
- Do not add paid services.
- Do not add a build step.
