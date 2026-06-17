#!/bin/bash
# Launchd entrypoint. launchd cannot execute scripts under ~/Documents without TCC;
# install this to ~/.local/bin/agentic-os-launchd-wrapper.sh and point the plist here.
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
REPO="/Users/nadavyigal/Documents/Projects /Agentic OS"
LOG="/tmp/agentic-os-refresh.wrapper.log"

notify_fail() {
  local code="$1"
  osascript -e "display notification \"Refresh failed (exit $code). Run ./agentic-os doctor.\" with title \"Agentic OS\" subtitle \"Launchd refresh failed\" sound name \"Glass\"" 2>/dev/null || true
}

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') wrapper start ==="
  cd "$REPO"
  "$REPO/scripts/daily-refresh.sh"
} >> "$LOG" 2>&1 || {
  code=$?
  notify_fail "$code"
  exit "$code"
}
