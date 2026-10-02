#!/usr/bin/env python3
"""Targeted verification for check_repository.py.

Tests that:
1. The valid repository passes all checks.
2. A broken markdown link is detected.
3. Missing frontmatter metadata is detected.

Uses a temporary copy to inject faults without modifying the real repository.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CHECKER = "scripts/check_repository.py"


def run_checker(repo_dir):
    """Run check_repository.py in the given directory and return (returncode, output)."""
    result = subprocess.run(
        [sys.executable, CHECKER],
        cwd=repo_dir,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout + result.stderr


def test_valid_repo_passes():
    """The real repository should pass all checks."""
    code, output = run_checker(REPO_ROOT)
    assert code == 0, f"Valid repo failed checks:\n{output}"
    print("  PASS: Valid repository passes all checks.")


def test_broken_link_detected():
    """Injecting a broken link into a markdown file should be detected."""
    with tempfile.TemporaryDirectory() as tmp:
        clone = Path(tmp) / "repo"
        shutil.copytree(REPO_ROOT, clone)
        # Inject a broken link into projects/README.md
        target = clone / "projects" / "README.md"
        with open(target, "a") as f:
            f.write("\n[broken link](./nonexistent-file.md)\n")
        code, output = run_checker(clone)
        assert code != 0, f"Broken link was NOT detected:\n{output}"
        assert "nonexistent-file.md" in output, f"Error message missing link name:\n{output}"
        print("  PASS: Broken markdown link is detected.")


def test_missing_metadata_detected():
    """Removing required frontmatter from a programme README should be detected."""
    with tempfile.TemporaryDirectory() as tmp:
        clone = Path(tmp) / "repo"
        shutil.copytree(REPO_ROOT, clone)
        # Strip frontmatter from programmes/ral/README.md
        target = clone / "programmes" / "ral" / "README.md"
        with open(target, "w") as f:
            f.write("# RAL\n\nNo frontmatter here.\n")
        code, output = run_checker(clone)
        assert code != 0, f"Missing metadata was NOT detected:\n{output}"
        assert "Missing frontmatter" in output or "Missing required metadata" in output, (
            f"Error message missing metadata mention:\n{output}"
        )
        print("  PASS: Missing frontmatter metadata is detected.")


def main():
    print("Running targeted verification of check_repository.py...")
    tests = [test_valid_repo_passes, test_broken_link_detected, test_missing_metadata_detected]
    failures = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"  FAIL: {test.__name__}: {e}")
            failures += 1
    if failures:
        print(f"\n{failures}/{len(tests)} verification(s) failed.")
        sys.exit(1)
    else:
        print(f"\nAll {len(tests)} verifications passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
