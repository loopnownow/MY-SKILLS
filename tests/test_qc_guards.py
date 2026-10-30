"""QC guards added by CHG-20261029: retired lab tree, anchors, flow steps, punctuation wording.

Config
------
SCAN_SUFFIX : text suffixes scanned
SKIP_FILES  : historical ledgers allowed to name retired things
"""
from __future__ import annotations

import difflib
import re
import unittest

from tests.support import ROOT

SCAN_SUFFIX = (".md", ".yaml", ".py", ".json")
SKIP_FILES = {"VERSION.txt", "INTEGRATION_MAP.md", "legacy_aliases.yaml"}
FENCE = re.compile(r"^```.*?^```", re.S | re.M)


def live_files(suffixes=SCAN_SUFFIX):
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in suffixes or p.name in SKIP_FILES:
            continue
        if ".git" in p.parts or "tests" in p.relative_to(ROOT).parts[:1]:
            continue
        yield p


def slug(h: str) -> str:
    h = re.sub(r"[`*_]", "", h.strip().lower())
    return re.sub(r"[^\w\u4e00-\u9fff\- ]", "", h).replace(" ", "-")


class RetiredLabTree(unittest.TestCase):
    PAT = re.compile(r"\{doc_root\}[\\/]+(?:0[0-9]-[a-z-]+)[\\/]")

    def test_no_numbered_doc_root_subtree(self) -> None:
        bad = [f"{p.relative_to(ROOT)}: {m.group(0)}" for p in live_files()
               for m in self.PAT.finditer(p.read_text(encoding="utf-8", errors="ignore"))]
        self.assertEqual(bad, [], "retired {doc_root}\\0N-* tree still cited; use an alias or _library")


class MarkdownAnchors(unittest.TestCase):
    LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s#]*)#([^)\s]+)\)")

    def test_anchor_targets_exist(self) -> None:
        heads = {}
        def heads_of(path):
            if path not in heads:
                t = FENCE.sub("", path.read_text(encoding="utf-8", errors="ignore"))
                heads[path] = {slug(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.*)$", t, re.M)}
            return heads[path]
        bad = []
        for p in live_files((".md",)):
            t = FENCE.sub("", p.read_text(encoding="utf-8", errors="ignore"))
            for m in self.LINK.finditer(t):
                tgt = (p.parent / m.group(1)).resolve() if m.group(1) else p
                if m.group(1) and not tgt.is_file():
                    bad.append(
                        f"missing target: {p.relative_to(ROOT)} -> {m.group(1)}"
                    )
                    continue
                if tgt.is_file() and tgt.suffix == ".md" and slug(m.group(2)) not in heads_of(tgt):
                    bad.append(f"{p.relative_to(ROOT)} -> {m.group(1)}#{m.group(2)}")
        self.assertEqual(bad, [])


class FlowSteps(unittest.TestCase):
    ITEM = re.compile(r"^\s*\d+[.)]\s+(.*\S)\s*$")

    def test_no_adjacent_duplicate_numbered_steps(self) -> None:
        bad = []
        for p in live_files((".md",)):
            prev = None
            for n, line in enumerate(FENCE.sub("", p.read_text(encoding="utf-8", errors="ignore")).splitlines(), 1):
                m = self.ITEM.match(line)
                cur = re.sub(r"[`*_]", "", m.group(1)).lower() if m else None
                if cur and prev and len(cur) > 12 and difflib.SequenceMatcher(None, prev, cur).ratio() >= 0.9:
                    bad.append(f"{p.relative_to(ROOT)}:{n}")
                prev = cur
        self.assertEqual(bad, [])


class PunctuationWording(unittest.TestCase):
    RETIRED = ("More than 2 em dashes per 1000 words", "en dashes, and colons as routine",
               "Prefer sentences, commas, semicolons", "comma, semicolon, parentheses")

    def test_superseded_wording_absent(self) -> None:
        bad = [f"{p.relative_to(ROOT)}: {s}" for p in live_files((".md",))
               for s in self.RETIRED if s in p.read_text(encoding="utf-8", errors="ignore")]
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
