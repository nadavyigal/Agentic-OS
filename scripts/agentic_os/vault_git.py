#!/usr/bin/env python3
"""Refuse to write into a Builder OS vault checkout that is behind its remote.

Why this exists (2026-07-22): the vault's local checkout drifts behind
`origin/main` because PRs merge on GitHub but nobody pulls locally, while
`./agentic-os refresh` keeps writing a fresh daily note into `11-Journal/`
every morning regardless. That combination is not merely untidy, it is
actively dangerous:

  - The founder reads a vault missing whatever merged upstream. On 2026-07-22
    the checkout was 7 commits behind and the July 13-19 daily notes were
    simply absent from the vault being read.
  - Worse, files show up as ` M` in `git status` while being *older* than
    `origin/main`. `wiki-log.md`, `wiki-index.md` and `RunSmart.md` were all
    in that state. Committing them - the obvious reading of "commit the
    outstanding changes" - would have deleted the 07-19 activation-cliff
    autopsy, the 07-21 weekly review and the EXD-022/EXD-023 entries.

A morning ritual that writes into a stale checkout manufactures that exact
conflict every day it runs. So the vault writers now check first.

Design rules:
  - **Fail open on the unknowable, fail closed on the known-bad.** No network,
    no git, no upstream configured => proceed (the founder should not lose the
    habit rail because a coffee-shop wifi is down). Definitely behind or
    definitely diverged => refuse and say exactly how to fix it.
  - **Never raise.** A guard that crashes the morning refresh is worse than the
    staleness it prevents.
  - Stdlib only, consistent with the rest of scripts/agentic_os/.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

FETCH_TIMEOUT = 12
GIT_TIMEOUT = 10


def _git(vault: Path, *args: str, timeout: int = GIT_TIMEOUT) -> tuple[int, str]:
    """Run a git command against the vault. Returns (returncode, stdout)."""
    try:
        result = subprocess.run(
            ["git", "-C", str(vault), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return 1, ""
    return result.returncode, result.stdout.strip()


def vault_status(vault: Path, fetch: bool = True) -> dict:
    """Describe the vault checkout relative to its upstream branch.

    Returns a dict with:
      state    -- one of: not-a-repo, no-upstream, unknown, behind,
                  diverged, ahead, current
      ahead    -- commits the local branch has that upstream does not
      behind   -- commits upstream has that the local branch does not
      branch   -- local branch name (best effort)
      upstream -- upstream ref name (best effort)
      fetched  -- whether the remote was successfully contacted
    """
    out: dict = {
        "state": "unknown",
        "ahead": 0,
        "behind": 0,
        "branch": "",
        "upstream": "",
        "fetched": False,
    }

    if not vault.is_dir():
        out["state"] = "not-a-repo"
        return out

    rc, _ = _git(vault, "rev-parse", "--git-dir")
    if rc != 0:
        out["state"] = "not-a-repo"
        return out

    _, branch = _git(vault, "rev-parse", "--abbrev-ref", "HEAD")
    out["branch"] = branch

    rc, upstream = _git(vault, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    if rc != 0 or not upstream:
        # No tracking branch configured: nothing to be stale against.
        out["state"] = "no-upstream"
        return out
    out["upstream"] = upstream

    if fetch:
        rc, _ = _git(vault, "fetch", "--quiet", "origin", timeout=FETCH_TIMEOUT)
        out["fetched"] = rc == 0

    rc, counts = _git(vault, "rev-list", "--left-right", "--count", f"HEAD...{upstream}")
    if rc != 0 or not counts:
        out["state"] = "unknown"
        return out

    parts = counts.split()
    if len(parts) != 2:
        out["state"] = "unknown"
        return out
    try:
        out["ahead"], out["behind"] = int(parts[0]), int(parts[1])
    except ValueError:
        out["state"] = "unknown"
        return out

    if out["behind"] and out["ahead"]:
        out["state"] = "diverged"
    elif out["behind"]:
        out["state"] = "behind"
    elif out["ahead"]:
        out["state"] = "ahead"
    else:
        out["state"] = "current"

    # A failed fetch means rev-list compared against whatever origin/* ref was
    # cached by the last successful fetch, so "current"/"ahead" is unverified
    # rather than safe. Downgrade to unknown so the "freshness unverified"
    # warning fires instead of silent false confidence — otherwise a transient
    # network blip reproduces the exact failure this module exists to prevent.
    # "behind"/"diverged" are left alone: blocking on stale-but-bad data is
    # still the safe call.
    if fetch and not out["fetched"] and out["state"] in ("current", "ahead"):
        out["state"] = "unknown"
    return out


def staleness_block_message(vault: Path, status: dict, label: str) -> str:
    """The loud, actionable refusal. Written to be read at 7am, half awake."""
    n = status["behind"]
    plural = "commit" if n == 1 else "commits"
    lines = [
        f"⛔ {label}: REFUSED — the vault checkout is {n} {plural} behind {status['upstream']}.",
        "",
        "   Writing into a stale checkout is how the 2026-07-22 near-miss happened:",
        "   files show as modified while being OLDER than upstream, so committing",
        "   them deletes merged work. Nothing was written.",
        "",
        "   Fix (from the vault):",
        f"     cd {str(vault)!r} && git status --short",
        "     # anything modified there is probably STALE, not new — check with:",
        "     #   git diff origin/main -- <file>",
        "     git pull --ff-only",
        "",
        "   Then re-run this command.",
    ]
    if status["state"] == "diverged":
        lines[0] = (
            f"⛔ {label}: REFUSED — the vault checkout has diverged from "
            f"{status['upstream']} ({status['ahead']} ahead, {n} behind)."
        )
        lines[-3] = "     git pull --rebase   # or reconcile by hand; do NOT force"
    return "\n".join(lines)


def require_fresh_vault(vault: Path, label: str, fetch: bool = True) -> bool:
    """True if it is safe to write into the vault. Prints why when it is not.

    Callers should `return 1` (or otherwise abort) on False, having written
    nothing. Never raises.
    """
    # The whole body is guarded, not just the status lookup: the "never raises"
    # promise above has to be enforced rather than incidental.
    try:
        status = vault_status(vault, fetch=fetch)

        state = status["state"]

        if state in ("behind", "diverged"):
            print(staleness_block_message(vault, status, label))
            return False

        if state == "ahead":
            n = status["ahead"]
            plural = "commit" if n == 1 else "commits"
            print(
                f"⚠️ {label}: vault has {n} unpushed {plural} on {status['branch']}. "
                "Proceeding, but push before they strand."
            )
            return True

        if state == "unknown" and not status["fetched"]:
            print(f"⚠️ {label}: could not reach the vault remote; freshness unverified. Proceeding.")
            return True

        return True
    except Exception:  # noqa: BLE001 - a guard must never break the ritual
        return True
