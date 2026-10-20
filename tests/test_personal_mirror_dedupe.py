"""A-side pages must not mirror a base pack verbatim (dedupe 2026-10-20).

`03_research/personal/radiology-design.md` duplicated 69% of
`03_research/base/design-study/MODULE.md`; it now points at the pack and keeps
only A-specific sections. Add further pairs to MIRRORS as they are cleaned.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIRRORS = (
    ("03_research/base/design-study/MODULE.md", "03_research/personal/radiology-design.md"),
)
MIN_CHARS = 200


def _paragraphs(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    out = set()
    for para in re.split(r"\n\s*\n", text):
        norm = re.sub(r"\s+", " ", para).strip()
        if len(norm) >= MIN_CHARS:
            out.add(norm)
    return out


    def test_no_cross_file_long_paragraph(self) -> None:
        seen: dict[str, str] = {}
        hits: list[str] = []
        skip = {".git", "__pycache__", ".pytest_cache", "mounts-cap", "fixtures"}
        for path in ROOT.rglob("*.md"):
            if set(path.parts) & skip:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel == "INTEGRATION_MAP.md":
                continue
            for para in re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig", errors="ignore")):
                norm = re.sub(r"\s+", " ", para).strip()
                if len(norm) < MIN_CHARS:
                    continue
                if norm in seen and seen[norm] != rel:
                    hits.append(f"{rel} duplicates {seen[norm]}: {norm[:70]}")
                seen.setdefault(norm, rel)
        self.assertEqual(hits, [], "shared long paragraphs:\n" + "\n".join(hits[:10]))


class PersonalMirrorDedupe(unittest.TestCase):
    def test_mirror_pairs_share_no_long_paragraph(self) -> None:
        problems = []
        for base_rel, personal_rel in MIRRORS:
            shared = _paragraphs(ROOT / base_rel) & _paragraphs(ROOT / personal_rel)
            for text in sorted(shared):
                problems.append(f"{personal_rel} duplicates {base_rel}: {text[:90]}")
        self.assertEqual(problems, [], "verbatim mirror:\n" + "\n".join(problems[:10]))


if __name__ == "__main__":
    unittest.main()
