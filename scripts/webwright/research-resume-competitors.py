"""
Research script: Resume builder competitor pricing and feature comparison.
Scrapes public pages only — no authentication, no sign-in flows.

Usage:
  python research-resume-competitors.py [--dry-run]

Output:
  outputs/<timestamp>/competitor-research.json
  outputs/<timestamp>/screenshots/
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUTS_DIR = SCRIPT_DIR / "outputs"

COMPETITORS = [
    "https://resume.io",
    "https://www.kickresume.com",
    "https://enhancv.com",
    "https://www.resumegenius.com",
    "https://zety.com",
]


def _load_env() -> None:
    env_file = SCRIPT_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


def build_task(competitors: list[str]) -> str:
    urls = "\n".join(f"  - {u}" for u in competitors)
    return f"""
Research resume builder competitors. Visit each of these public pages and extract pricing
and feature information:

{urls}

For each site:
1. Navigate to their pricing page (usually /pricing or linked from the homepage).
2. Extract: free tier availability, paid plan prices (monthly + annual), key features listed.
3. Navigate to their homepage and note the main value proposition (headline/subheadline).
4. Take a screenshot of the pricing page.
5. Note any AI-specific features they advertise.

After visiting all sites, return a JSON object:
{{
  "scraped_at": "<ISO timestamp>",
  "competitors": [
    {{
      "url": "<url>",
      "pricing_page_url": "<pricing url if found>",
      "free_tier": true/false,
      "free_tier_limits": "<description or null>",
      "cheapest_paid_monthly": "<price string or null>",
      "annual_discount": "<percent or null>",
      "ai_features": ["<feature>"],
      "value_proposition": "<main headline>",
      "notes": "<anything notable>"
    }}
  ]
}}

Important: only access public pages. Do not sign up or log in to any site.
Add a 3-second delay between page navigations to avoid rate limiting.
"""


def run(dry_run: bool = False) -> None:
    _load_env()

    task = build_task(COMPETITORS)

    if dry_run:
        print("DRY RUN — would execute the following task:\n")
        print(task)
        return

    try:
        from webwright import Agent
    except ImportError:
        print("ERROR: webwright not installed. Run: bash scripts/webwright/setup.sh")
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_dir = OUTPUTS_DIR / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Researching {len(COMPETITORS)} competitors ...")
    print(f"Output: {output_dir}/")

    agent = Agent(model=os.environ.get("WEBWRIGHT_MODEL", "claude-sonnet-4-6"))
    result = agent.run(task, start_url=COMPETITORS[0], workspace=str(output_dir))

    result_file = output_dir / "competitor-research.json"
    with open(result_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Done. Results saved to {result_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Competitor research automation")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run(dry_run=args.dry_run)
