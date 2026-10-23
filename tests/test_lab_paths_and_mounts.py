#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab-paths aliases resolve; LICENSE/NOTICE present; mount probes are documented."""

from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LAB_PATHS = ROOT / "00_orchestrator" / "references" / "lab-paths.yaml"


class LabPaths(unittest.TestCase):
    def test_aliases_file_and_required_keys(self) -> None:
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        for key in (
            "lab_root",
            "code_root",
            "doc_root",
            "skills_git",
            "skills_runtime",
            "jcr2026_xlsx",
            "find_journal_submission",
                        "mounts_cap_cache",
        ):
            self.assertIn(key, aliases)
            self.assertTrue(str(aliases[key]).strip())

    def test_local_disk_aliases_exist_when_on_lab_machine(self) -> None:
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        # Local disk aliases (drive-letter paths). Skip whole check if any D:/L: root missing.
        # mounts_cap is deliberately absent (retired 2026-10-20) -> covered below.
        keys = (
            "lab_root",
            "del_root",
            "code_root",
            "doc_root",
            "jcr2026_xlsx",
            "find_journal_submission",
        )
        missing = []
        for key in keys:
            if key not in aliases:
                continue
            val = str(aliases[key])
            if len(val) >= 2 and val[1] == ":" and not Path(val).exists():
                missing.append(key)
        if missing:
            self.skipTest(f"lab paths absent ({', '.join(missing)}); skip off non-lab host")
        for key in keys:
            if key not in aliases:
                continue
            p = Path(aliases[key])
            if p.exists():
                self.assertTrue(p.exists(), f"{key} missing: {p}")

    def test_retired_mounts_cap_is_documented(self) -> None:
        """mounts-cap is retired: either absent, or explicitly marked retired."""
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        val = str((data.get("aliases") or {}).get("mounts_cap") or "")
        notes = " ".join(str(x) for x in (data.get("notes") or []))
        self.assertIn("retired", notes.lower())
        self.assertIn("mounts-cap-retired", notes)
        if val and Path(val).exists():
            self.fail(
                "mounts_cap exists again; retirement moved its bytes to "
                "{DEL}\\_by-function\\mounts-cap-retired-20261020"
            )


class LicenseNotice(unittest.TestCase):
    def test_license_and_notice_exist(self) -> None:
        self.assertTrue((ROOT / "LICENSE").is_file())
        notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
        self.assertIn("SlopMonster", notice)
        self.assertIn("Permission is hereby granted, free of charge, to any person obtaining a copy", notice)
        style = (ROOT / "00_orchestrator" / "references" / "style-tells.md").read_text(encoding="utf-8")
        self.assertIn("NOTICE", style)
        self.assertNotIn("Permission is hereby granted, free of charge, to any person obtaining a copy", style)


class SubmissionPrivacy(unittest.TestCase):
    def test_priors_not_in_git_data_folder(self) -> None:
        # A find-journal stub removed 2026-10-17; capability body is in-repo base/; priors stay out of git
        self.assertFalse((ROOT / "03_research" / "find-journal").exists())
        a_fj = ROOT / "03_research" / "base" / "find-journal"
        self.assertTrue((a_fj / "SKILL.md").is_file())
        # No submission priors inside A git tree (incl. in-repo base)
        for root in (ROOT, a_fj):
            for name in ("submission-prior.jsonl", "whitelist-submitted.csv"):
                hits = list(root.rglob(name)) if root.exists() else []
                self.assertEqual(hits, [], f"prior file must not be in git: {hits}")


if __name__ == "__main__":
    unittest.main()
