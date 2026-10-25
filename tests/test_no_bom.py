"""No UTF-8 BOM in repository text files (2026-10-20).

A BOM is invisible in most editors but breaks naive `startswith("---")`
frontmatter readers and makes greps miss the first line.
"""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOM = b"\xef\xbb\xbf"
SUFFIXES = {".md", ".yaml", ".yml", ".txt", ".tsv", ".py", ".mmd", ".sh", ".ini"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}


class NoBom(unittest.TestCase):
    def test_no_bom_in_text_files(self) -> None:
        offenders = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in SUFFIXES:
                continue
            if set(path.parts) & SKIP_DIRS:
                continue
            with path.open("rb") as handle:
                if handle.read(3) == BOM:
                    offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [], "BOM found:\n" + "\n".join(offenders[:20]))


if __name__ == "__main__":
    unittest.main()
