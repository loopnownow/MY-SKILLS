"""The external renderer is gone (2026-10-20); it must not creep back in.

A retired reference is tolerated only when the line says so (deleted / removed /
former / archived), which keeps the retirement record readable.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HIST = re.compile(r"deleted|removed|former|archived|retired|no external renderer", re.I)
ALLOW_FILES = {"INTEGRATION_MAP.md"}  # monthly integration archive
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}


class NoExternalRendererReference(unittest.TestCase):
    def test_no_live_archify_reference(self) -> None:
        hits: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ".py", ".mmd"}:
                continue
            if set(path.parts) & SKIP_DIRS:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES or rel.startswith("tests/"):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), 1):
                if "archify" not in line.lower():
                    continue
                if HIST.search(line):
                    continue
                hits.append(f"{rel}:{i}: {line.strip()[:110]}")
        self.assertEqual(hits, [], "live external-renderer references:\n" + "\n".join(hits[:20]))


if __name__ == "__main__":
    unittest.main()
