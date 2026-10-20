"""QC Batch5: live B-pack path residue must stay in historical / allowlisted files only."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Explicit B label, force_b key, or prose remote name MY-SKILLS-base (not source id checks).
B_PAT = re.compile(r"(?:\bB\s+0[0-7]-[a-z0-9-]+/?\b|\bforce_b\b|\bMY-SKILLS-base\b)")

ALLOW_FILES = {
    "01_skill-integration/registry.yaml",
    "01_skill-integration/legacy_aliases.yaml",
    "01_skill-integration/MOUNTED_SKILLS.md",
    "01_skill-integration/references/id-rules.md",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
}

ALLOW_LINE = re.compile(
    r"archived|historical|legacy|old_path|was\s+B|formerly|0del|"
    r"not restored|do not sync|\.grok/skills|assertNotIn|retired",
    re.I,
)


class NoBPackResidue(unittest.TestCase):
    def test_no_live_b_pack_residue(self) -> None:
        violations: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".txt"}:
                continue
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES or rel.startswith(("_", "tests/")):
                continue
            if rel.endswith("test_no_b_pack_residue.py"):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), 1):
                if not B_PAT.search(line):
                    continue
                if ALLOW_LINE.search(line):
                    continue
                violations.append(f"{rel}:{i}: {line.strip()[:120]}")
        self.assertEqual(
            violations,
            [],
            "B-pack residue outside allowlist:\n" + "\n".join(violations[:40]),
        )


if __name__ == "__main__":
    unittest.main()
