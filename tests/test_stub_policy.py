"""Stub policy: pointer-only markdown must have a live consumer.

A "stub" is a leftover shell: a `.md` whose body is only a move/pointer cue
(`pointer stub`, `thin pointer`, `Body moved`, `moved to`, `已移至`). It is
transient, not a contract: either a live consumer still reads that exact path
(declared in ALLOW with a reason), or the file is deleted.

Entry names (SKILL.md / README.md / MODULE.md / INDEX.md) are navigation files,
not stubs, and are exempt by name.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ENTRY_NAMES = {"SKILL.md", "README.md", "MODULE.md", "INDEX.md"}

# Pointer-only files deliberately kept because a live consumer reads this exact
# path as its entry point. Key = repo-relative POSIX path, value = reason.
ALLOW = {
    "05_manuscript/base/vocab/L2/preferred.md":
        "base-layer L2 entry; 05_manuscript/SKILL.md and advanced/route.md read it as the base index",
}

CUE = re.compile(r"pointer stub|pointer shell|moved to|已移至|已迁移|Body moved|thin pointer", re.I)


def pointer_only(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    lines = [ln for ln in body.splitlines()
             if ln.strip() and not ln.lstrip().startswith("#")]
    return len(lines) <= 5 and bool(CUE.search(body))


class TestStubPolicy(unittest.TestCase):
    def test_no_pointer_only_stubs_without_consumer(self) -> None:
        hits = []
        for p in ROOT.rglob("*.md"):
            if ".git" in p.parts or p.name in ENTRY_NAMES:
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel in ALLOW:
                continue
            if pointer_only(p):
                hits.append(rel)
        self.assertEqual(
            hits, [],
            "pointer-only stubs without a live consumer: "
            f"{hits}; delete them, or add a reason to ALLOW in this file",
        )

    def test_allow_entries_have_reason(self) -> None:
        for rel, reason in ALLOW.items():
            self.assertTrue(reason.strip(), f"{rel}: ALLOW needs a reason")


if __name__ == "__main__":
    unittest.main()
