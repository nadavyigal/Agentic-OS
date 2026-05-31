# Global Agentic OS Visual Dashboard

This is a lightweight static dashboard suite for the Global Agentic OS. It does not replace `../DASHBOARD.md`; it is a visual companion generated from `../PROJECT-STATUS.md`. Three pages share one dark design and a common top nav:

- **Command Center** (`command-center.html`): plan the next move, run a workflow, or talk to any OS.
- **Orchestration Map** (`orchestration.html`): the layered system map, Layers 0 to 9.
- **Project Status** (`index.html`): project cards, action board, decision board, QA board.

## Open Locally

Open any of the three pages in a browser, or serve the folder for the live `status.json` path:

```bash
cd dashboard && python3 -m http.server 8787 --bind 127.0.0.1
```

No backend, database, authentication, paid service, or build step is required. When
served by a static file server, `index.html` loads `status.json`; opened via `file://`
it uses the embedded JSON fallback.

## Files

- `index.html`: Project Status dashboard. Dark theme via `styles.css`; reads `status.json`.
- `command-center.html`: OS Command Center (see below). Self-contained dark theme.
- `orchestration.html`: layered Orchestration Map (Layers 0 to 9) with embedded status JSON.
- `styles.css`: dark theme for `index.html` (palette shared with the other two pages).
- `status.json`: easy-to-edit dashboard data copied from `PROJECT-STATUS.md`.
- `README.md`: this usage note.

## OS Command Center

`command-center.html` is the centralized launcher. It is fully static and respects
the guardrails below: no backend, no API keys, no chat box. Every card has a one-click
"Copy prompt" button that puts a context-loaded prompt on the clipboard to paste into
Claude Code or Cursor, plus deep links into the relevant docs. A live filter box
searches all cards. It has four kinds of group:

- **Planner** — fuses the Action Board and Decision Board into one-click prompts:
  generate the next sprint, resolve open decisions, or draft the next feature plan.
- **OS roster** — CEO, CFO, Analysis, Director, Distribution, Growth, and the delivery
  agents (Architect, PM, QA, Release Manager, UI/UX).
- **Runs / Workflows** — runnable workflows (morning brief, weekly exec review, weekly
  distribution, QA review, risk review, update lessons, PR summary).
- **Memory & Learning** — recall context, log session end, review lessons and decisions.

To add or improve a card, edit the embedded `<script id="cc-data">` JSON block: append
to a group's `items` array (set `name`, `tone`, `status`, `purpose`, `starter`,
`links`), or add a whole new group with its own `tag`, `title`, and `items`. Use
`{date}` in a `starter` to auto-fill the generated date. Tones: `violet`, `cyan`,
`green`, `amber`, `pink`, `accent`. Statuses: `ready`, `active`, `needsdata`.

## Update Status

When status changes, update `status.json`, then mirror it into the embedded
`<script id="status-data">` block in `index.html` so `file://` opening stays current.
Sync command (run from `dashboard/`):

```bash
python3 - <<'PY'
import re, json
s=open("status.json",encoding="utf-8").read(); json.loads(s)
h=open("index.html",encoding="utf-8").read()
h=re.sub(r'(<script id="status-data" type="application/json">\n).*?(\n    </script>)',
         lambda m: m.group(1)+s.rstrip("\n")+m.group(2), h, count=1, flags=re.S)
open("index.html","w",encoding="utf-8").write(h); print("synced")
PY
```

## Scope Guardrails

- Keep the Markdown dashboard.
- Keep this static and manual-update-friendly.
- Do not add a database.
- Do not add authentication.
- Do not add paid services.
- Do not add a build step.
