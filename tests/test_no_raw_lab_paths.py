"""Live skill bodies must cite lab paths through {alias}, not raw drive letters.

`lab-paths.yaml` is the only place that may write `D:\\0Grok` / `D:\\0del` /
`D:\\00db`. Historical / archive lines (dates, 0del move notes) may keep them.

Deep-scan 2026-10-20 converted the last live bodies (gates.md, claim-number-align,
forensic-consistency, console-ui, find-journal data README, 03 handoff,
workspace subproject headings, project-ref layout/template).
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "tests"}

RAW_RE = re.compile(r"[A-Za-z]:\\{1,2}(0Grok|0del|00db|00used)\b")
HIST_LINE = re.compile(
    r"archived|historical|legacy|former|formerly|pruned|relocated|absorbed|retired|"
    r"勿建|do not recreate|归档|archive|archived|历史|historical|moved to",
    re.I,
)
ALLOW_FILES = {
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "NOTICE",
    "00_orchestrator/references/lab-paths.yaml",
}


class NoRawLabPaths(unittest.TestCase):
    def test_bodies_use_aliases(self) -> None:
        bad: list[str] = []
        for p in ROOT.rglob("*"):
            if not p.is_file() or p.suffix not in {".md", ".yaml", ".yml"}:
                continue
            if SKIP_DIRS & set(p.parts):
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES:
                continue
            for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if HIST_LINE.search(line):
                    continue
                if RAW_RE.search(line):
                    bad.append(f"{rel}:{i}: {line.strip()[:100]}")
        self.assertEqual(
            bad,
            [],
            "raw lab drive paths in live bodies (use {doc_root} / {DEL} / {raw_root} / "
            "{code_modules} / {skills_git} / {lab_root}):\n" + "\n".join(bad[:40]),
        )


if __name__ == "__main__":
    unittest.main()
