"""Lab path aliases, fine-id board and raw-path hygiene.

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
            self.assertIn(key, aliases, f"lab-paths.yaml missing alias {key}")
            val = str(aliases[key])
            p = Path(val)
            self.assertTrue(p.is_absolute(), f"{key} must be an absolute path, got {val!r}")
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


ALIAS_TOKEN = re.compile(r"\{([a-z][a-z0-9_]+)\}")


def _alias_tokens() -> dict[str, set[str]]:
    """alias -> files that cite it as `{alias}`."""
    uses: dict[str, set[str]] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".mmd", ".py"}:
            continue
        if SKIP_DIRS & set(path.parts):
            continue
        if path.name == "lab-paths.yaml":
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in ALIAS_TOKEN.findall(text):
            uses.setdefault(token, set()).add(rel)
    return uses


class AliasMapIsTight(unittest.TestCase):
    """Every alias is cited somewhere, and every path-shaped {token} is defined.

    A dead alias is a path nobody uses; a dangling one is a path that resolves to
    nothing at read time. Both were found in the 2026-10-27 deep QC.
    """

    PATH_PREFIXES = ("code_", "doc_", "find_journal_", "jcr", "lab_", "raw_", "del_", "rules_", "skills_")
    # Retired names may still appear in dated history lines (VERSION.txt / INTEGRATION_MAP.md).
    HISTORY_ONLY = {"code_06_review", "doc_xml", "code_md_bank"}

    def test_no_dead_alias(self) -> None:
        aliases = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))["aliases"]
        uses = _alias_tokens()
        dead = sorted(name for name in aliases if name not in uses)
        self.assertEqual(
            dead,
            [],
            "aliases declared but never cited (delete them or cite them):\n"
            + "\n".join(f"  {name}: {aliases[name]}" for name in dead),
        )

    def test_no_dangling_alias(self) -> None:
        aliases = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))["aliases"]
        uses = _alias_tokens()
        dangling = sorted(
            token
            for token in uses
            if token.startswith(self.PATH_PREFIXES)
            and token not in aliases
            and token not in self.HISTORY_ONLY
        )
        self.assertEqual(
            dangling,
            [],
            "path-shaped {tokens} with no entry in lab-paths.yaml "
            "(cite an existing alias, or add the alias):\n"
            + "\n".join(f"  {{{t}}}: {sorted(uses[t])[:3]}" for t in dangling),
        )


LAB_MODULES_VERSION = re.compile(r"v?(\d+\.\d+\.\d+)")
# Skill prose that states the live lab-module version. The SSOT is
# stats-analysis modules/__init__.py; these files may only repeat that number.
VERSION_PROSE = (
    "02_data-processing/SKILL.md",
    "02_data-processing/advanced/analysis/pipeline.md",
    "02_data-processing/advanced/analysis/methods.md",
)


class LabModulesVersionProse(unittest.TestCase):
    """Skill prose must state the version the library actually declares.

    2026-10-27: the prose said 4.3.0 while `modules/__init__.py` said 4.3.1 and
    `pyproject.toml` said 0.1.0. Rather than hard-code the offending numbers (which
    would need editing at every release), this reads the version out of the
    stats-analysis tree when it is present and compares.
    """

    STATS_INIT = ROOT.parent / "stats-analysis" / "modules" / "__init__.py"

    def _library_version(self) -> str | None:
        if not self.STATS_INIT.is_file():
            return None
        match = re.search(
            r'__version__\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"',
            self.STATS_INIT.read_text(encoding="utf-8"),
        )
        return match.group(1) if match else None

    def test_prose_states_one_version(self) -> None:
        seen: dict[str, list[str]] = {}
        for rel in VERSION_PROSE:
            text = (ROOT / rel).read_text(encoding="utf-8")
            for line_no, line in enumerate(text.splitlines(), 1):
                for match in LAB_MODULES_VERSION.finditer(line):
                    if "Lab pipeline" in line or "lab modules" in line.lower() or "modules v" in line:
                        seen.setdefault(match.group(1), []).append(f"{rel}:{line_no}")
        self.assertLessEqual(
            len(seen),
            1,
            "skill prose states more than one lab-module version:\n"
            + "\n".join(f"  {v}: {sites}" for v, sites in seen.items()),
        )

    def test_prose_matches_library_when_repo_is_present(self) -> None:
        expected = self._library_version()
        if expected is None:
            self.skipTest("stats-analysis checkout not beside MY-SKILLS")
        for rel in VERSION_PROSE:
            for line_no, line in enumerate(
                (ROOT / rel).read_text(encoding="utf-8").splitlines(), 1
            ):
                for match in LAB_MODULES_VERSION.finditer(line):
                    if not (
                        "Lab pipeline" in line
                        or "lab modules" in line.lower()
                        or "modules v" in line
                    ):
                        continue
                    self.assertEqual(
                        match.group(1),
                        expected,
                        f"{rel}:{line_no} says {match.group(1)} but the library is {expected}",
                    )
