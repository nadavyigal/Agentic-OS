#!/bin/bash
# Webwright local environment setup
# Run once from the Agentic OS root: bash scripts/webwright/setup.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV_DIR="$REPO_ROOT/tools/webwright-env"

echo "Setting up Webwright environment..."
echo "Venv: $VENV_DIR"

python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

pip install --quiet --upgrade pip
pip install webwright playwright

playwright install chromium

echo ""
echo "Webwright ready."
echo "Activate with: source tools/webwright-env/bin/activate"
echo "Run a script:  python scripts/webwright/qa-resumebuilder-flow.py --dry-run"
