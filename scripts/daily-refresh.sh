#!/bin/bash
# Daily automated dashboard refresh, run by launchd
# (~/Library/LaunchAgents/com.nadav.agentic-os-refresh.plist, 07:00 daily).
# Refreshes the dashboard, commits ONLY the generated files, pushes main.
# Founder-approved automation (2026-06-12 OS audit, decision 1).

set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="/Users/nadavyigal/Documents/Projects /Agentic OS"
LOG="$REPO/logs/daily-refresh.log"
ENV_FILE="$HOME/.config/agentic-os.env"
GENERATED=(dashboard PROJECT-STATUS.md DASHBOARD.md executive-os/EXECUTIVE-DASHBOARD.md)

if [ -f "$ENV_FILE" ]; then
  # shellcheck disable=SC1090
  source "$ENV_FILE"
fi

mkdir -p "$REPO/logs"
notify() {
  local title="$1"
  local subtitle="$2"
  local body="$3"
  osascript -e "display notification \"$body\" with title \"$title\" subtitle \"$subtitle\" sound name \"Glass\"" 2>/dev/null || true
}

on_failure() {
  local code="$?"
  notify "Agentic OS" "Daily refresh failed" "Exit $code. Open logs/daily-refresh.log and run ./agentic-os doctor."
  echo "FAILED (exit $code)"
  exit "$code"
}
trap on_failure ERR

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') daily refresh ==="
  cd "$REPO" || exit 1

  ./agentic-os refresh

  if ! git diff --quiet -- "${GENERATED[@]}"; then
    # Path-scoped commit: never sweeps in unrelated working-tree changes.
    git commit -m "Auto-refresh dashboard ($(date '+%Y-%m-%d'))" -- "${GENERATED[@]}"
  else
    echo "no dashboard changes"
  fi

  if [ "$(git rev-parse --abbrev-ref HEAD)" = "main" ] && [ -n "$(git log --oneline @{u}.. 2>/dev/null)" ]; then
    git push origin main && echo "pushed" || echo "push FAILED (will retry tomorrow)"
  fi

  # Notify on stranded work so items don't silently accumulate.
  STRANDED=$(python3 -c "
import json, sys
try:
    d = json.load(open('dashboard/status.json'))
    print(len(d.get('strandedWork', {}).get('items', [])))
except Exception:
    print(0)
" 2>/dev/null)
  if [ "${STRANDED:-0}" -gt 0 ]; then
    notify "Agentic OS" "Stranded Work" "$STRANDED item(s) at risk — open DASHBOARD.md"
    echo "stranded-work notification sent ($STRANDED items)"
  fi

  echo "health check"
  ./agentic-os doctor || notify "Agentic OS" "Refresh stale or contradicted" "Run ./agentic-os doctor for details."

  echo "done"
} >> "$LOG" 2>&1
