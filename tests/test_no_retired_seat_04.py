"""04_analysis retired into 02_data-processing (2026-10-25): no stale pointers.

Live docs must not cite the retired seat folder, its old gate id, or the old
mermaid node ids. Historical ledgers (`INTEGRATION_MAP.md`, `VERSION.txt`) and
the retired-id alias map keep the old names on purpose.

How to run: python -m unittest tests.test_no_retired_seat_04
"""
from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Files that may name the retired seat (history / retired-id SSOT).
ALLOW_FILES = {
    "INTEGRATION_MAP.md",
    "VERSION.txt",
    "01_skill-integration/legacy_aliases.yaml",
}

# Tests carry the old names as assertion fixtures; they fail loudly on their own.
SKIP_PREFIXES = ("tests/",)

SUFFIXES = {".md", ".yaml", ".yml", ".txt", ".py", ".mmd", ".json", ".ini", ".mermaid"}

PATTERNS = (
    ("folder", re.compile(r"04_analysis")),
    ("gate", re.compile(r"G-04(?![0-9])")),
    ("node", re.compile(r"Need04|\bP04\b|GF04|GA04")),
)

# Combined seat forms that would read as a duplicate after the merge.
DUP_FORM = re.compile(r"02\s*[/+→]\s*02|02\s+02")


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout
    return [line for line in out.splitlines() if line.strip()]


class NoRetiredSeat04(unittest.TestCase):
    def test_folder_is_gone(self) -> None:
        self.assertFalse((ROOT / "04_analysis").exists(), "04_analysis retired into 02_data-processing")
        self.assertTrue((ROOT / "02_data-processing" / "SKILL.md").is_file())
        for pack in ("analyze-stats", "plot-figures", "draw-flowchart", "calc-sample-size"):
            self.assertTrue((ROOT / "02_data-processing" / "base" / pack).is_dir(), pack)
            self.assertTrue(
                (ROOT / "02_data-processing" / "personal" / "analysis" / "route.md").is_file()
            )

    def test_no_stale_references(self) -> None:
        violations: list[str] = []
        for rel in tracked_files():
            if rel in ALLOW_FILES or rel.startswith(SKIP_PREFIXES):
                continue
            if Path(rel).suffix.lower() not in SUFFIXES:
                continue
            path = ROOT / rel
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for label, pattern in PATTERNS:
                for m in pattern.finditer(text):
                    line_no = text.count("\n", 0, m.start()) + 1
                    violations.append(f"{rel}:{line_no}: {label} {m.group(0)}")
        self.assertEqual(violations, [], "stale 04 seat references:\n" + "\n".join(violations[:40]))

    def test_no_duplicate_seat_forms(self) -> None:
        violations: list[str] = []
        for rel in tracked_files():
            if rel.startswith(SKIP_PREFIXES) or Path(rel).suffix.lower() not in SUFFIXES:
                continue
            path = ROOT / rel
            if not path.is_file():
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if DUP_FORM.search(line):
                    violations.append(f"{rel}:{i}: {line.strip()[:100]}")
        self.assertEqual(violations, [], "duplicate 02 seat forms:\n" + "\n".join(violations[:40]))


if __name__ == "__main__":
    unittest.main()
