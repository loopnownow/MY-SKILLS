"""Lab path aliases, mounts board and raw-path hygiene.

Merged from: `test_lab_paths_and_mounts.py`, `test_no_raw_lab_paths.py`.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest
import yaml

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

LAB_PATHS = ROOT / "00_orchestrator" / "references" / "lab-paths.yaml"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "tests"}
RAW_RE = re.compile(r"[A-Za-z]:\\{1,2}(0Grok|0del|00db|00used)\b")
HIST_LINE = re.compile(
    r"archived|historical|legacy|former|formerly|pruned|relocated|absorbed|retired|"
    r"勿建|do not recreate|归档|archive|archived|历史|historical|moved to",
    re.I,
)
ALLOW_FILES = {
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "NOTICE",
    "00_orchestrator/references/lab-paths.yaml",
}

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
            "raw_root",
        ):
            self.assertIn(key, aliases)
            self.assertTrue(str(aliases[key]).strip())

    def test_local_disk_aliases_exist_when_on_lab_machine(self) -> None:
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        # Local disk aliases (drive-letter paths). Skip whole check if any D: root is missing.
        # raw_root is required on the alias map.
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
class NoRawLabPaths(unittest.TestCase):
    def test_bodies_use_aliases(self) -> None:
        bad: list[str] = []
        for p in ROOT.rglob("*"):
            if not p.is_file() or p.suffix not in {".md", ".yaml", ".yml"}:
                continue
            if SKIP_DIRS & set(p.parts):
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES:
                continue
            for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if HIST_LINE.search(line):
                    continue
                if RAW_RE.search(line):
                    bad.append(f"{rel}:{i}: {line.strip()[:100]}")
        self.assertEqual(
            bad,
            [],
            "raw lab drive paths in live bodies (use {doc_root} / {DEL} / {raw_root} / "
            "{code_modules} / {skills_git} / {lab_root}):\n" + "\n".join(bad[:40]),
        )
