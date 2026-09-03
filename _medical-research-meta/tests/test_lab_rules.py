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
        table = read("05_manuscript", "personal", "forbidden-phrases.md").lower()
        hits = []
        for word in (
            "delve",
            "landscape",
            "pivotal",
            "robust",
            "comprehensive",
            "interestingly",
            "leverage",
            "groundbreaking",
        ):
            if word in self.SAMPLE.lower():
                self.assertIn(word, table, f"{word} must be listed in forbidden-phrases")
                hits.append(word)
        self.assertGreaterEqual(len(hits), 6)

    def test_de_ai_is_personal_not_a_mount(self) -> None:
        five = read("05_manuscript", "SKILL.md")
        self.assertNotIn("05-de-ai", five)
        self.assertIn("05-write-manuscript", five)
        self.assertFalse((SKILLS / "05_manuscript" / "de-ai").exists())
        self.assertTrue((SKILLS / "05_manuscript" / "personal" / "forbidden-phrases.md").is_file())


class Aitor(unittest.TestCase):
    def test_methods_have_no_citations(self) -> None:
        text = read("05_manuscript", "personal", "Aitor-format.md")
        self.assertIn("Methods: no citations", text)

    def test_table1_is_training_vs_test(self) -> None:
        text = read("05_manuscript", "personal", "Aitor-format.md")
        self.assertRegex(text, r"Table 1\s*=\s*training vs test")


class ValMode(unittest.TestCase):
    def test_test_set_does_not_reselect_features(self) -> None:
        text = read("04_analysis", "personal", "0rad-pipeline-rules.md")
        self.assertIn("VAL_MODE", text)
        self.assertRegex(text, r"[Rr]e-select features on the test set")
        self.assertIn("no new screening", text)
        self.assertIn("不重筛", text)


class Routing(unittest.TestCase):
    def test_01_is_discovery_not_excel(self) -> None:
        readme = (SKILLS / "README.md").read_text(encoding="utf-8")
        self.assertIn("01_skill-discovery-integration", readme)
        self.assertIn("Discover / evaluate / mount", readme)
        self.assertNotIn("01_automation", readme)
        zero = read("00_orchestrator", "SKILL.md")
        self.assertIn("01_skill-discovery-integration", zero)
        self.assertIn("Excel / 批处理 / 0RAD", zero)
        # Excel routes to 02, not 01
        self.assertRegex(zero, r"Excel / 批处理 / 0RAD 文件夹 → `02_data-processing`")

    def test_figures_route_to_04(self) -> None:
        zero = read("00_orchestrator", "SKILL.md")
        self.assertIn("出图", zero)
        five = read("05_manuscript", "SKILL.md")
        self.assertIn("04_analysis", five)
        self.assertIn("04-fig-plot", five)
        self.assertIn("04-fig-flow", five)
        self.assertNotIn("bundles/figure-engine", five)

    def test_session_mount_pick(self) -> None:
        one = read("01_skill-discovery-integration", "SKILL.md")
        zero = read("00_orchestrator", "SKILL.md")
        reg = read("01_skill-discovery-integration", "registry.yaml")
        self.assertIn("Session mount pick", one)
        self.assertIn("ask-each-run", reg)
        self.assertIn("session mount pick", zero.lower())
        five = read("05_manuscript", "SKILL.md")
        self.assertIn("This-run pick", five)

    def test_literature_to_03_response_to_06(self) -> None:
        zero = read("00_orchestrator", "SKILL.md")
        self.assertIn("Literature enters 03 only", zero)
        self.assertIn("reviewer response only here", zero)


if __name__ == "__main__":
    unittest.main()
