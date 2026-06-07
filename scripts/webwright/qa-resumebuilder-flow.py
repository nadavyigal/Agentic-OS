"""
QA script: ResumeBuilder upload → optimize → export flow.
Tests the core product path against a local or staging instance.

Usage:
  python qa-resumebuilder-flow.py [--dry-run]

Output:
  outputs/<timestamp>/result.json
  outputs/<timestamp>/screenshots/

Environment (.env):
  ANTHROPIC_API_KEY=...
  STAGING_URL_RESUMEBUILDER=http://localhost:3000   (default)
  STAGING_ONLY=true                                  (default)
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).parent
OUTPUTS_DIR = SCRIPT_DIR / "outputs"
FIXTURE_RESUME = SCRIPT_DIR / "test-fixtures" / "sample-resume.pdf"

# Explicit allowlist of safe hostnames for staging
SAFE_HOSTNAMES = {"localhost", "127.0.0.1", "0.0.0.0"}


def _load_env() -> None:
    env_file = SCRIPT_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, raw_value = line.partition("=")
            # Strip inline comments (e.g. key=value  # comment)
            value = raw_value.split(" #")[0].split("\t#")[0].strip()
            os.environ.setdefault(key.strip(), value)


def _guard_staging(base_url: str) -> None:
    """
    Refuse to run against production URLs when STAGING_ONLY=true (default).
    Uses urlparse to inspect the hostname — not a substring match.
    Safe hostnames: localhost, 127.0.0.1, or any host containing 'staging'.
    """
    staging_only = os.environ.get("STAGING_ONLY", "true").lower()
    if staging_only != "true":
        return

    hostname = urlparse(base_url).hostname or ""
    is_safe = (
        hostname in SAFE_HOSTNAMES
        or "staging" in hostname
        or hostname.startswith("192.168.")
    )
    if not is_safe:
        print(
            f"ERROR: STAGING_ONLY=true but URL hostname looks like production: {hostname!r}\n"
            f"Full URL: {base_url}\n"
            "Set STAGING_ONLY=false in .env to allow this."
        )
        sys.exit(1)


def build_task(base_url: str, fixture_path: str) -> str:
    return f"""
You are testing the ResumeBuilder web application. Complete these steps and report results.

Base URL: {base_url}
Resume fixture: {fixture_path}

Steps:
1. Navigate to {base_url}
2. Find the resume upload form or the main CTA button.
3. Upload the resume file at: {fixture_path}
4. In the job description field, enter:
   "Senior Software Engineer at Acme Corp. Requirements: 5+ years Python, React, AWS.
   Strong communication skills. Bachelor's in Computer Science or equivalent."
5. Submit the form and wait for the optimization to complete (look for a 'Review',
   'Download', or 'Export' button — up to 60 seconds).
6. Click the export or download PDF button.
7. Confirm the download dialog or file download starts.

After each major step, take a screenshot named step-N.png.

Return a JSON object with:
- steps_completed: number of steps completed (1-7)
- any_errors: list of error messages encountered (empty list if none)
- timing_seconds: total time taken
- notes: any observations about the UI or flow
"""


def run(dry_run: bool = False) -> None:
    _load_env()

    base_url = os.environ.get("STAGING_URL_RESUMEBUILDER", "http://localhost:3000")
    _guard_staging(base_url)

    fixture_path = str(FIXTURE_RESUME)
    if not FIXTURE_RESUME.exists():
        print(
            f"WARNING: Fixture not found at {fixture_path}\n"
            "Create test-fixtures/sample-resume.pdf before running without --dry-run."
        )
        if not dry_run:
            sys.exit(1)

    task = build_task(base_url, fixture_path)

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

    print(f"Running QA against {base_url} ...")
    print(f"Output: {output_dir}/")

    agent = Agent(model=os.environ.get("WEBWRIGHT_MODEL", "claude-sonnet-4-6"))
    result = agent.run(task, start_url=base_url, workspace=str(output_dir))

    result_file = output_dir / "result.json"
    try:
        with open(result_file, "w") as f:
            json.dump(result, f, indent=2)
    except TypeError:
        with open(result_file, "w") as f:
            json.dump({"raw": str(result)}, f, indent=2)

    print(f"Done. Results saved to {result_file}")

    if isinstance(result, dict) and result.get("any_errors"):
        print(f"ERRORS: {result['any_errors']}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ResumeBuilder QA automation")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the task without executing",
    )
    args = parser.parse_args()
    run(dry_run=args.dry_run)
