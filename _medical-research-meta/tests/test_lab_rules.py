"""P2: no-LLM fixtures. Skill files must encode the locked lab rules."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[2] / "core"


def read(*parts: str) -> str:
    return (SKILLS.joinpath(*parts)).read_text(encoding="utf-8")


class TestSelection(unittest.TestCase):
    def test_skewed_two_independent_continuous_is_mann_whitney(self) -> None:
        text = read(
            "04_analysis",
            "bundles",
            "statistical-analysis",
            "references",
            "test_selection_guide.md",
        )
        # Two Independent Groups → continuous non-normal → Mann-Whitney
        block = re.search(
            r"Two Independent Groups(.*?)(?:Two Paired|### 2\.)",
            text,
            re.S,
        )
        self.assertIsNotNone(block)
        chunk = block.group(1)
        self.assertIn("non-normal", chunk.lower())
        self.assertRegex(chunk, r"Mann-Whitney U")


class DeAI(unittest.TestCase):
    SAMPLE = (
        "This paper delves into the landscape of radiomics. "
        "The pivotal and robust model is comprehensive. "
        "Interestingly, we leverage a groundbreaking approach."
    )

    def test_sample_hits_forbidden_table(self) -> None:
        table = read(
            "05_manuscript",
            "bundles",
            "manuscript-core",
            "references",
            "de-ai",
            "forbidden-phrases.md",
        ).lower()
        hits = []
        for word in ("delve", "landscape", "pivotal", "robust", "comprehensive", "interestingly", "leverage", "groundbreaking"):
            if word in self.SAMPLE.lower():
                self.assertIn(word, table, f"{word} must be listed in forbidden-phrases")
                hits.append(word)
        self.assertGreaterEqual(len(hits), 6)


class Aitor(unittest.TestCase):
    def test_methods_have_no_citations(self) -> None:
        text = read(
            "05_manuscript",
            "bundles",
            "manuscript-core",
            "references",
            "Aitor-format.md",
        )
        self.assertIn("Methods: no citations", text)

    def test_table1_is_training_vs_test(self) -> None:
        text = read(
            "05_manuscript",
            "bundles",
            "manuscript-core",
            "references",
            "Aitor-format.md",
        )
        self.assertRegex(text, r"Table 1\s*=\s*training vs test")


class ValMode(unittest.TestCase):
    def test_test_set_does_not_reselect_features(self) -> None:
        text = read("04_analysis", "references", "0rad-pipeline-rules.md")
        self.assertIn("VAL_MODE", text)
        self.assertRegex(text, r"[Rr]e-select features on the test set")
        self.assertIn("no new screening", text)
        self.assertIn("不重筛", text)


if __name__ == "__main__":
    unittest.main()
