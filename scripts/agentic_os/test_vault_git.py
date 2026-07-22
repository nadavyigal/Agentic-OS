#!/usr/bin/env python3
"""Tests for the vault staleness guard.

Builds real throwaway git repos in a temp dir rather than mocking subprocess,
because the thing under test IS the git plumbing. `fetch=False` throughout so
the tests never touch a network.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vault_git  # noqa: E402


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def commit(repo: Path, name: str) -> None:
    (repo / name).write_text(name)
    git(repo, "add", "-A")
    git(repo, "commit", "-m", name)


class VaultGitTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        self.remote = root / "remote.git"
        self.local = root / "vault"

        subprocess.run(
            ["git", "init", "--bare", "-b", "main", str(self.remote)],
            check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "clone", str(self.remote), str(self.local)],
            check=True, capture_output=True,
        )
        git(self.local, "config", "user.email", "t@t.test")
        git(self.local, "config", "user.name", "T")
        commit(self.local, "seed.md")
        git(self.local, "push", "-u", "origin", "main")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _advance_remote(self, n: int = 1) -> None:
        """Add n commits upstream without the local checkout knowing."""
        with tempfile.TemporaryDirectory() as other:
            clone = Path(other) / "c"
            subprocess.run(
                ["git", "clone", str(self.remote), str(clone)],
                check=True, capture_output=True,
            )
            git(clone, "config", "user.email", "t@t.test")
            git(clone, "config", "user.name", "T")
            for i in range(n):
                commit(clone, f"upstream-{i}.md")
            git(clone, "push", "origin", "main")
        # Make origin/main visible locally without changing HEAD.
        git(self.local, "fetch", "origin")

    # --- states ---------------------------------------------------------

    def test_current_is_allowed(self) -> None:
        s = vault_git.vault_status(self.local, fetch=False)
        self.assertEqual(s["state"], "current")
        self.assertTrue(vault_git.require_fresh_vault(self.local, "t", fetch=False))

    def test_behind_is_blocked(self) -> None:
        self._advance_remote(3)
        s = vault_git.vault_status(self.local, fetch=False)
        self.assertEqual(s["state"], "behind")
        self.assertEqual(s["behind"], 3)
        self.assertFalse(vault_git.require_fresh_vault(self.local, "t", fetch=False))

    def test_diverged_is_blocked(self) -> None:
        self._advance_remote(1)
        commit(self.local, "local-only.md")
        s = vault_git.vault_status(self.local, fetch=False)
        self.assertEqual(s["state"], "diverged")
        self.assertEqual((s["ahead"], s["behind"]), (1, 1))
        self.assertFalse(vault_git.require_fresh_vault(self.local, "t", fetch=False))

    def test_ahead_is_allowed_with_warning(self) -> None:
        commit(self.local, "local-only.md")
        s = vault_git.vault_status(self.local, fetch=False)
        self.assertEqual(s["state"], "ahead")
        self.assertTrue(vault_git.require_fresh_vault(self.local, "t", fetch=False))

    # --- fail-open paths ------------------------------------------------

    def test_not_a_repo_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as plain:
            s = vault_git.vault_status(Path(plain), fetch=False)
            self.assertEqual(s["state"], "not-a-repo")
            self.assertTrue(vault_git.require_fresh_vault(Path(plain), "t", fetch=False))

    def test_missing_directory_is_allowed(self) -> None:
        missing = Path(self._tmp.name) / "nope"
        self.assertEqual(vault_git.vault_status(missing, fetch=False)["state"], "not-a-repo")
        self.assertTrue(vault_git.require_fresh_vault(missing, "t", fetch=False))

    def test_no_upstream_is_allowed(self) -> None:
        git(self.local, "checkout", "-q", "-b", "detached-work")
        s = vault_git.vault_status(self.local, fetch=False)
        self.assertEqual(s["state"], "no-upstream")
        self.assertTrue(vault_git.require_fresh_vault(self.local, "t", fetch=False))

    def test_guard_never_raises(self) -> None:
        """Even on nonsense input the guard must return a bool, not explode."""
        self.assertIsInstance(
            vault_git.require_fresh_vault(Path("/dev/null/not/a/path"), "t", fetch=False),
            bool,
        )

    def test_guard_never_raises_on_malformed_status(self) -> None:
        """The 'never raises' promise must cover messaging, not just the lookup."""
        original = vault_git.vault_status
        try:
            vault_git.vault_status = lambda *a, **k: {}  # missing every key
            self.assertTrue(vault_git.require_fresh_vault(self.local, "t", fetch=False))
        finally:
            vault_git.vault_status = original

    # --- failed fetch must not masquerade as verified freshness -------------

    def _break_remote(self) -> None:
        """Make `git fetch` fail while the cached origin/* refs survive."""
        self.remote.rename(self.remote.with_name("remote-gone.git"))

    def test_failed_fetch_downgrades_current_to_unknown(self) -> None:
        """A network blip must not let a stale cache read as 'current'."""
        self._break_remote()
        s = vault_git.vault_status(self.local, fetch=True)
        self.assertFalse(s["fetched"])
        self.assertEqual(s["state"], "unknown")
        # Still allowed (fail open), but the caller now warns instead of trusting.
        self.assertTrue(vault_git.require_fresh_vault(self.local, "t", fetch=True))

    def test_failed_fetch_downgrades_ahead_to_unknown(self) -> None:
        commit(self.local, "local-only.md")
        self._break_remote()
        s = vault_git.vault_status(self.local, fetch=True)
        self.assertFalse(s["fetched"])
        self.assertEqual(s["state"], "unknown")

    def test_failed_fetch_still_blocks_when_cache_says_behind(self) -> None:
        """Stale-but-bad data is still worth blocking on."""
        self._advance_remote(2)  # local now knows it is behind via cached refs
        self._break_remote()
        s = vault_git.vault_status(self.local, fetch=True)
        self.assertFalse(s["fetched"])
        self.assertEqual(s["state"], "behind")
        self.assertFalse(vault_git.require_fresh_vault(self.local, "t", fetch=True))

    def test_successful_fetch_keeps_current(self) -> None:
        """The downgrade must not fire when the fetch actually worked."""
        s = vault_git.vault_status(self.local, fetch=True)
        self.assertTrue(s["fetched"])
        self.assertEqual(s["state"], "current")

    # --- message quality ------------------------------------------------

    def test_block_message_is_actionable(self) -> None:
        self._advance_remote(7)
        s = vault_git.vault_status(self.local, fetch=False)
        msg = vault_git.staleness_block_message(self.local, s, "daily note")
        self.assertIn("REFUSED", msg)
        self.assertIn("7 commits behind", msg)
        self.assertIn("git pull --ff-only", msg)
        self.assertIn("git diff origin/main", msg)
        self.assertTrue(msg.lstrip().startswith("⛔"), "CLI passthrough keys off the ⛔ prefix")

    def test_singular_commit_wording(self) -> None:
        self._advance_remote(1)
        s = vault_git.vault_status(self.local, fetch=False)
        msg = vault_git.staleness_block_message(self.local, s, "daily note")
        self.assertIn("1 commit behind", msg)
        self.assertNotIn("1 commits behind", msg)


if __name__ == "__main__":
    unittest.main()
