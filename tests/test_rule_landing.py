# -*- coding: utf-8 -*-
"""Assert Rules-landing content moved into MY-SKILLS (2026-10-18 slim)."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def t(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class RuleLanding(unittest.TestCase):
    def test_new_references_exist_and_linked(self) -> None:
        hm = ROOT / "00_orchestrator/references/handoff-monitor.md"
        se = ROOT / "00_orchestrator/references/skill-evolution.md"
        self.assertTrue(hm.is_file(), "handoff-monitor.md missing")
        self.assertTrue(se.is_file(), "skill-evolution.md missing")
        skill = t("00_orchestrator/SKILL.md")
        self.assertIn("handoff-monitor.md", skill)
        self.assertIn("skill-evolution.md", skill)

    def test_standing_delivery_drop_points(self) -> None:
        sd = t("00_orchestrator/references/standing-delivery.md")
        for needle in ("subproject root", "derivatives", "Asia/Shanghai"):
            self.assertIn(needle, sd, f"standing-delivery missing {needle}")
        # 0result retired as standard deliverable folder (2026-10-24)
        self.assertIn("no", sd.lower())
        self.assertTrue(
            ("do **not** create `0result" in sd) or ("do not create `0result" in sd) or ("no** live `0result" in sd) or ("no live `0result" in sd.lower()) or ("**no** `0result" in sd),
            "standing-delivery should scrub/forbid live 0result as deliverable seat",
        )

    def test_manuscript_local_qc_bans(self) -> None:
        ml = t("05_manuscript/qc/manuscript-local-qc.md")
        for needle in ("cannot_invent", "Do not invent", "[Figure N near here]", "layout_priority"):
            self.assertIn(needle, ml, f"manuscript-local-qc missing {needle}")

    def test_response_hard_rules(self) -> None:
        rp = t("07_response/personal/response.md")
        for needle in ("Please", "past tense", "ACCEPT-"):
            self.assertIn(needle, rp, f"response.md missing {needle}")

    def test_workspace_layout_points_at_rules(self) -> None:
        self.assertFalse((ROOT / "02_data-processing/personal/workspace.md").is_file())
        skill = t("02_data-processing/SKILL.md")
        self.assertIn("{RULES}/workspace-layout.md", skill)
        self.assertNotIn("personal/workspace.md", skill)
        sd = t("00_orchestrator/references/standing-delivery.md")
        self.assertIn("{RULES}/workspace-layout.md", sd)
        self.assertNotIn("`{WORK_A}", sd)
        self.assertNotIn("`{WORK_B}", sd)
        self.assertNotIn("## A-class", sd)
        self.assertNotIn("## B-class", sd)

    def test_ownership_dispatch(self) -> None:
        oc = t("00_orchestrator/references/ownership-contract.md")
        self.assertIn("## Dispatch", oc)
        self.assertIn("one executor", oc.lower() + " " + oc)  # English phrase may be Chinese
        # Chinese one-executor sentence from plan
        self.assertTrue(
            ("one executor" in oc.lower()) or ("一个任务只交一个执行方" in oc),
            "ownership-contract missing one-executor rule",
        )


if __name__ == "__main__":
    unittest.main()
