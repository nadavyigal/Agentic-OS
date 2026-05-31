#!/usr/bin/env python3
"""Codex PreToolUse policy for high-risk shell commands."""

from __future__ import annotations

import json
import re
import sys


def extract_command(payload: object) -> str:
    if not isinstance(payload, dict):
        return ""

    candidates = [
        payload.get("command"),
        payload.get("cmd"),
        payload.get("tool_input"),
        payload.get("input"),
        payload.get("arguments"),
    ]

    for candidate in candidates:
        if isinstance(candidate, str):
            return candidate
        if isinstance(candidate, dict):
            nested = extract_command(candidate)
            if nested:
                return nested
    return ""


def block_reason(command: str) -> str | None:
    checks: list[tuple[str, str]] = [
        (r"\brm\s+.*-[A-Za-z]*r[A-Za-z]*f|\brm\s+.*-[A-Za-z]*f[A-Za-z]*r", "rm -rf is blocked. Use explicit file deletion with user approval."),
        (r"\bgit\s+reset\s+--hard\b", "git reset --hard is blocked because it discards work."),
        (r"\bgit\s+push\b.*\s(--force|-f)(\s|$)", "Force push is blocked without explicit approval."),
        (r"\b(DROP\s+TABLE|TRUNCATE\s+TABLE|DROP\s+DATABASE|DROP\s+SCHEMA)\b", "Destructive SQL is blocked without explicit approval."),
        (r"\b(production|prod)\b.*\b(delete|drop|truncate|destroy|remove|wipe|purge|flush)\b", "Destructive production command is blocked."),
        (r"Authorization:\s*Bearer\s+['\"]?[A-Za-z0-9_\-\.]{12,}", "Inline bearer tokens are blocked. Use env vars or a secrets manager."),
        (r"\b(api[_-]?key|secret|token)=['\"]?[A-Za-z0-9_\-\.]{12,}", "Inline secrets are blocked. Use env vars or a secrets manager."),
    ]

    for pattern, reason in checks:
        if re.search(pattern, command, flags=re.IGNORECASE):
            return reason
    return None


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        payload = {"command": raw}

    command = extract_command(payload)
    if not command:
        return 0

    reason = block_reason(command)
    if reason:
        print(f"BLOCKED BY CODEX POLICY: {reason}", file=sys.stderr)
        print("Ask Nadav for explicit approval in the current task before proceeding.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
