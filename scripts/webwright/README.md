# Webwright Browser Automation Scripts

Local Agentic OS capability for QA automation and competitor research using Microsoft Webwright.

## Prerequisites

- Python 3.10+
- Docker Desktop (running)
- Anthropic API key

## Setup (run once)

```bash
cd /path/to/Agentic\ OS
bash scripts/webwright/setup.sh
```

This creates `tools/webwright-env/` with Webwright and Playwright installed.

## Environment

```bash
cp scripts/webwright/.env.example scripts/webwright/.env
# Edit .env: add ANTHROPIC_API_KEY and staging URLs
```

## Running a script

Always activate the venv first:

```bash
source tools/webwright-env/bin/activate
cd scripts/webwright
```

**Dry run first — always:**
```bash
python qa-resumebuilder-flow.py --dry-run
```

**Execute against staging:**
```bash
python qa-resumebuilder-flow.py
```

Outputs land in `outputs/YYYY-MM-DD_HH-MM/` (gitignored).

## Available Scripts

| Script | Purpose |
|--------|---------|
| `qa-resumebuilder-flow.py` | Upload → optimize → export regression QA |
| `qa-runsmart-flow.py` | Onboarding → plan → training view regression QA |
| `research-resume-competitors.py` | Scrape pricing + features of top resume tools |
| `research-running-competitors.py` | Strava, NRC, TrainingPeaks feature comparison |
| `landing-page-audit.py` | CTA, copy, mobile layout check |
| `pricing-page-check.py` | Competitor pricing change monitor |

## Safety Rules

1. Always `--dry-run` before first real execution of any script.
2. `STAGING_ONLY=true` is the default — scripts refuse to run against prod URLs.
3. Never commit the `outputs/` directory.
4. Never store credentials in scripts — `.env` only.
5. Never run authenticated scripts against competitor sites.
6. Public pages only for research scripts.

## Interpreting Output

Each run creates `outputs/<timestamp>/result.json` plus screenshots.
`result.json` contains: `steps_completed`, `any_errors`, `timing_seconds`.
A non-zero `any_errors` value means the flow failed; check the screenshot at that step.
