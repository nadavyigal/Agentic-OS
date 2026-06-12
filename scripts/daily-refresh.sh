#!/bin/bash
# Daily automated dashboard refresh, run by launchd
# (~/Library/LaunchAgents/com.nadav.agentic-os-refresh.plist, 07:00 daily).
# Refreshes the dashboard, commits ONLY the generated files, pushes main.
# Founder-approved automation (2026-06-12 OS audit, decision 1).

set -uo pipefail

REPO="/Users/nadavyigal/Documents/Projects /Agentic OS"
LOG="$REPO/logs/daily-refresh.log"
GENERATED=(dashboard PROJECT-STATUS.md DASHBOARD.md executive-os/EXECUTIVE-DASHBOARD.md)

mkdir -p "$REPO/logs"
{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') daily refresh ==="
  cd "$REPO" || exit 1

  ./agentic-os refresh || { echo "refresh FAILED"; exit 1; }

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
    osascript -e "display notification \"$STRANDED item(s) at risk — open DASHBOARD.md\" with title \"Agentic OS\" subtitle \"Stranded Work\" sound name \"Glass\"" 2>/dev/null || true
    echo "stranded-work notification sent ($STRANDED items)"
  fi

  echo "done"
} >> "$LOG" 2>&1
