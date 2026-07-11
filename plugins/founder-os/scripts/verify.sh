#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$repo_root"
python3 -m unittest scripts.portfolio_hq.test_refresh_portfolio_hq
./agentic-os verify
npm --prefix sites/portfolio-hq test
npm --prefix sites/portfolio-hq run lint
