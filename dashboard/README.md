# Global Agentic OS Visual Dashboard

This is a lightweight static dashboard for the Global Agentic OS. It does not replace `../DASHBOARD.md`; it is a visual companion generated from `../PROJECT-STATUS.md`.

## Open Locally

Open `dashboard/index.html` in a browser. No backend, database, authentication, paid service, or build step is required.

## Update Status

Use `../PROJECT-STATUS.md` as the source of truth. Update `dashboard/status.json` manually from that file, then mirror the same JSON into the embedded `<script id="status-data">` block in `dashboard/index.html` if you want direct `file://` opening to show the latest data.

When served by any static file server, `index.html` will try to load `status.json` first. When opened directly from the filesystem, it uses the embedded JSON fallback so the dashboard still opens cleanly.

## Files

- `index.html`: static project-status dashboard UI and renderer.
- `command-center.html`: OS Command Center. One card per OS (CEO, CFO, Analysis, Director, Distribution, Growth, and the delivery agents). Each card has a live status, a one-click "Copy conversation starter" button that puts a context-loaded prompt on the clipboard to paste into Claude Code or Cursor, and deep links into that OS's docs and prompt files. Includes a live filter box.
- `orchestration.html`: layered Orchestration Map (Layers 0-8) with embedded status JSON.
- `styles.css`: visual styling, status colors, cards, boards, and responsive layout (used by `index.html`).
- `status.json`: easy-to-edit dashboard data copied from `PROJECT-STATUS.md`.
- `README.md`: this usage note.

## OS Command Center

`command-center.html` is the centralized launcher for talking to each OS directly.
It is fully static and respects the guardrails below: no backend, no API keys, no
chat box. To start a conversation, click "Copy conversation starter" on an OS card
and paste it into Claude Code or Cursor — the prompt pre-loads that OS's docs and
working rules. Edit the cards in the embedded `<script id="cc-data">` JSON block; add
a new OS by appending to a group's `items` array (set `name`, `tone`, `status`,
`purpose`, `starter`, and `links`). Use `{date}` in a starter to auto-fill the
generated date.

## Scope Guardrails

- Keep the Markdown dashboard.
- Keep this static and manual-update-friendly.
- Do not add a database.
- Do not add authentication.
- Do not add paid services.
- Do not add a build step.
