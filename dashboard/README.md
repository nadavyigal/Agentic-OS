# Global Agentic OS Visual Dashboard

This is a lightweight static dashboard for the Global Agentic OS. It does not replace `../DASHBOARD.md`; it is a visual companion generated from `../PROJECT-STATUS.md`.

## Open Locally

Open `dashboard/index.html` in a browser. No backend, database, authentication, paid service, or build step is required.

## Update Status

Use `../PROJECT-STATUS.md` as the source of truth. Update `dashboard/status.json` manually from that file, then mirror the same JSON into the embedded `<script id="status-data">` block in `dashboard/index.html` if you want direct `file://` opening to show the latest data.

When served by any static file server, `index.html` will try to load `status.json` first. When opened directly from the filesystem, it uses the embedded JSON fallback so the dashboard still opens cleanly.

## Files

- `index.html`: static dashboard UI and renderer.
- `styles.css`: visual styling, status colors, cards, boards, and responsive layout.
- `status.json`: easy-to-edit dashboard data copied from `PROJECT-STATUS.md`.
- `README.md`: this usage note.

## Scope Guardrails

- Keep the Markdown dashboard.
- Keep this static and manual-update-friendly.
- Do not add a database.
- Do not add authentication.
- Do not add paid services.
- Do not add a build step.
