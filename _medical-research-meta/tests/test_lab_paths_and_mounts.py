#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lab-paths aliases resolve; LICENSE/NOTICE present; mount/B probes are documented."""

from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
LAB_PATHS = ROOT / "00_orchestrator" / "references" / "lab-paths.yaml"


class LabPaths(unittest.TestCase):
    def test_aliases_file_and_required_keys(self) -> None:
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        for key in (
            "lab_root",
            "script_root",
            "doc_root",
            "skills_git",
            "skills_runtime",
            "jcr2026_xlsx",
            "find_journal_submission",
            "b_capabilities_repo",
            "mounts_cap_cache",
        ):
            self.assertIn(key, aliases)
            self.assertTrue(str(aliases[key]).strip())

    def test_local_disk_aliases_exist_when_on_lab_machine(self) -> None:
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        keys = ("script_root", "doc_root", "jcr2026_xlsx", "find_journal_submission")
        missing = [key for key in keys if not Path(aliases[key]).exists()]
        if missing:
            self.skipTest(f"lab paths absent ({', '.join(missing)}); skip off non-lab host")
        for key in keys:
            p = Path(aliases[key])
            self.assertTrue(p.exists(), f"{key} missing: {p}")


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
        data = ROOT / "03_research" / "find-journal" / "data" / "2026"
        self.assertFalse((data / "submission-prior.jsonl").exists())
        self.assertFalse((data / "whitelist-submitted.csv").exists())
        self.assertTrue((data / "SUBMISSION_PRIVACY.md").is_file())


if __name__ == "__main__":
    unittest.main()
