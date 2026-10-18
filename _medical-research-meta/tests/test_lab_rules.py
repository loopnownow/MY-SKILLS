"""P2: no-LLM fixtures. Skill files must encode the locked lab rules."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[2]


def read(*parts: str) -> str:
    return (SKILLS.joinpath(*parts)).read_text(encoding="utf-8")


class DeAI(unittest.TestCase):
    SAMPLE = (
        "This paper delves into the landscape of radiomics. "
        "The pivotal and robust model is comprehensive. "
        "Interestingly, we leverage a groundbreaking approach."
    )

    def test_sample_hits_forbidden_table(self) -> None:
        table = read("05_manuscript", "personal", "vocab", "L1", "ban-phrases.md").lower()
        hits = []
        for word in (
            "delve", "landscape", "pivotal", "robust", "comprehensive",
            "interestingly", "leverage", "groundbreaking",
        ):
            if word in self.SAMPLE.lower():
                self.assertIn(word, table, f"{word} must be listed in ban-phrases")
                hits.append(word)
        self.assertGreaterEqual(len(hits), 6)

    def test_compared_and_attenuated_wording(self) -> None:
        banned = read("05_manuscript", "personal", "vocab", "L1", "ban-phrases.md")
        patterns = read("05_manuscript", "personal", "vocab", "L1", "patterns.md")
        lang = read("05_manuscript", "personal", "process", "citation-and-language.md")
        for text in (banned, patterns, lang):
            self.assertIn("attenuated", text)
            self.assertIn("Compared", text)
            self.assertIn("relative CBF", text)
            self.assertIn("relCBF", text)
        self.assertIn("reduced", banned)
        self.assertIn("decreased", banned)
        self.assertIn("attenuation correction", banned)
        self.assertIn("comparison word", banned)

    def test_de_ai_is_personal_not_a_mount(self) -> None:
        five = read("05_manuscript", "SKILL.md")
        self.assertNotIn("05-de-ai", five)
        self.assertIn("write-paper", five)
        self.assertNotIn("05-write-manuscript", five)
        self.assertFalse((SKILLS / "05_manuscript" / "de-ai").exists())
        self.assertTrue(
            (SKILLS / "05_manuscript" / "personal" / "vocab" / "L1" / "ban-phrases.md").is_file()
        )


class Aitor(unittest.TestCase):
    def test_methods_have_no_citations(self) -> None:
        text = read("05_manuscript", "personal", "Aitor-format.md")
        self.assertIn("Methods: no citations", text)

    def test_table1_is_training_vs_test(self) -> None:
        text = read("05_manuscript", "personal", "Aitor-format.md")
        self.assertRegex(text, r"Table 1\s*=\s*training vs test")


class ValMode(unittest.TestCase):
    def test_test_set_does_not_reselect_features(self) -> None:
        text = read("04_analysis", "personal", "pipeline.md")
        self.assertIn("VAL_MODE", text)
        self.assertRegex(text, r"[Rr]e-select features on the test set")
        self.assertIn("no new screening", text)
        self.assertIn("\u4e0d\u91cd\u7b5b", text)


class Routing(unittest.TestCase):
    def test_01_is_discovery_not_excel(self) -> None:
        readme = (SKILLS / "README.md").read_text(encoding="utf-8")
        self.assertIn("01_skill-integration", readme)
        self.assertIn("Mount / index / hybrid recipes", readme)
        self.assertNotIn("01_automation", readme)
        zero = read("00_orchestrator", "SKILL.md")
        self.assertIn("01_skill-integration", zero)
        fast = read("00_orchestrator", "references", "fast-routing.md")
        self.assertIn("Excel / \u6279\u5904\u7406 / 0RAD", fast)
        self.assertRegex(
            fast,
            r"Excel / \u6279\u5904\u7406 / 0RAD \u6587\u4ef6\u5939 \u2192 `02_data-processing`",
        )

    def test_figures_route_to_04(self) -> None:
        fast = read("00_orchestrator", "references", "fast-routing.md")
        self.assertIn("\u51fa\u56fe", fast)
        five = read("05_manuscript", "SKILL.md")
        self.assertIn("04_analysis", five)
        self.assertIn("plot-figures", five)
        self.assertIn("draw-flowchart", five)
        self.assertNotIn("04-fig-flow", five)
        self.assertNotIn("bundles/figure-engine", five)

    def test_session_mount_pick(self) -> None:
        one = read("01_skill-integration", "SKILL.md")
        zero = read("00_orchestrator", "SKILL.md")
        reg = read("01_skill-integration", "registry.yaml")
        pick = read("01_skill-integration", "references", "session-pick.md")
        self.assertIn("Session mount pick", pick)
        self.assertIn("session-pick.md", one)
        self.assertIn("ask-each-run", reg)
        self.assertIn("session mount pick", zero.lower())
        five = read("05_manuscript", "SKILL.md")
        self.assertIn("This-run pick", five)

    def test_literature_to_03_response_to_07(self) -> None:
        zero = read("00_orchestrator", "SKILL.md")
        self.assertIn("Literature enters 03 only", zero)
        self.assertIn("Reviewer response enters 07 only", zero)
        fast = read("00_orchestrator", "references", "fast-routing.md")
        self.assertIn("回复审稿人", fast)
        self.assertIn("07_response", fast)
        self.assertIn("- **回复审稿人** → `07_response`", fast)
        self.assertNotIn("预审 / 审稿 / **回复审稿人** → `06_review`", fast)
        self.assertIn("- 预审 / 审稿 → `06_review`", fast)
        gates = read("00_orchestrator", "gates.md")
        self.assertIn("after Lee pre-review or re-review only", gates)
        self.assertNotIn("after pre-review or reviewer response", gates)
        self.assertIn("A07 / `07_response`", gates)


class LabSte(unittest.TestCase):
    def test_pointer_and_no_vendor(self) -> None:
        lab = read("05_manuscript", "personal", "vocab", "L3", "lab-ste.md")
        self.assertIn("{doc_lab_ste}", lab)
        self.assertIn("Do not", lab)
        self.assertIn("vendor", lab.lower())
        self.assertIn("conventional_passive", lab)
        self.assertIn("Compared", lab)
        self.assertIn("attenuated", lab)
        five = read("05_manuscript", "SKILL.md")
        self.assertIn("personal/vocab/L3/lab-ste.md", five)
        self.assertFalse((SKILLS / "05_manuscript" / "personal" / "approved-en.tsv").exists())
        self.assertFalse((SKILLS / "lab-ste").exists())
        self.assertTrue(
            (SKILLS / "05_manuscript" / "personal" / "vocab" / "L2" / "approved-en.tsv").is_file()
        )


if __name__ == "__main__":
    unittest.main()
