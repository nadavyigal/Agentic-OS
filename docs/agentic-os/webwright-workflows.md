# Webwright Workflows

Browser automation scripts for QA and research. All scripts live in `scripts/webwright/`.

## Prerequisites

Run once: `bash scripts/webwright/setup.sh`

Activate: `source tools/webwright-env/bin/activate`

## Available Commands

| Command | Script | Purpose |
|---------|--------|---------|
| `/qa-resumebuilder-flow` | `qa-resumebuilder-flow.py` | Upload → optimize → export regression check |
| `/qa-runsmart-flow` | `qa-runsmart-flow.py` | Onboarding → plan → training view |
| `/research-resume-competitors` | `research-resume-competitors.py` | Pricing + feature scrape (public pages) |
| `/research-running-competitors` | `research-running-competitors.py` | Strava, NRC, TrainingPeaks comparison |
| `/landing-page-audit` | `landing-page-audit.py` | CTA, copy, mobile layout check |
| `/pricing-page-check` | `pricing-page-check.py` | Competitor pricing change monitor |

## How to Invoke (Codex/Claude prompt pattern)

```
Activate tools/webwright-env, then run:
  python scripts/webwright/qa-resumebuilder-flow.py --dry-run
Review the dry-run output, then run without --dry-run if it looks correct.
Outputs go to scripts/webwright/outputs/<timestamp>/.
```

## Safety Rules

1. `--dry-run` first on any new or modified script.
2. `STAGING_ONLY=true` is the default; the script will exit if pointed at a production URL.
3. `outputs/` is gitignored — never commit it.
4. Research scripts: public pages only. No sign-in. 3-second delay between pages.
5. Never run authenticated QA scripts against competitor sites.

## Adding a New Script

1. Copy `qa-resumebuilder-flow.py` as a template.
2. Keep `_load_env()`, `_guard_staging()`, and `--dry-run` in every script.
3. Store outputs in `OUTPUTS_DIR / timestamp`.
4. Add an entry to the table above.

## Interpretation

Each run produces:
- `outputs/<timestamp>/result.json` — steps completed, errors, timing
- `outputs/<timestamp>/screenshots/` — step-by-step screenshots

A non-zero `any_errors` value means a step failed. Check the screenshot at that step number.
