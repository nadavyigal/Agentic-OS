# Webwright Integration Evaluation

**Decision: PILOT in Agentic OS. Not deployed to any server.**

## What It Is

Microsoft Webwright (MIT, 5.2K stars, Microsoft Research) is a terminal-native browser agent framework. You give it a natural-language task; it writes and runs a Playwright script. Generated scripts are saved as durable artifacts.

## Why It Fits the Agentic OS

Repeatable browser tasks (QA regression, competitor research, landing page audits) currently require manual effort or hand-written Playwright. Webwright turns natural-language descriptions into re-runnable scripts, making browser automation accessible to Codex/Claude workflows.

## Integration Architecture

Local only. Lives in `scripts/webwright/` inside the Agentic OS repo. Separate venv at `tools/webwright-env/`. Scripts invoked manually or via Codex/Claude tasks. Outputs are local and gitignored.

## Available Scripts

| Script | Purpose |
|--------|---------|
| `qa-resumebuilder-flow.py` | Upload → optimize → export regression |
| `research-resume-competitors.py` | Pricing + feature scrape |
| `qa-runsmart-flow.py` | (placeholder, Phase 4) |
| `landing-page-audit.py` | (placeholder, Phase 4) |
| `pricing-page-check.py` | (placeholder, Phase 4) |

## Setup

```bash
bash scripts/webwright/setup.sh
```

## Safety Rules

- `STAGING_ONLY=true` by default — scripts exit if URL looks like production
- `--dry-run` flag on every script — always run first on new scripts
- `outputs/` is gitignored
- No credentials in scripts — `.env` only
- Research scripts: public pages only, no authentication, 3-second delay between pages

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| Accidental prod action | STAGING_ONLY guard + --dry-run |
| Credential leakage | .env only, never committed |
| ToS violations on competitor sites | Public pages only, no auth, delays |
| Screenshot capturing PII | outputs/ gitignored, never shared |

## Maintenance

Webwright is at 5.2K stars vs MarkItDown's 147K. It's a Microsoft Research project, active as of May 2026. If it becomes unmaintained, scripts can be rewritten as raw Playwright — same Playwright dependency, just without the natural-language layer.
