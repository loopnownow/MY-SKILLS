"""E3: lightweight cross-repo contract (Rules / Skills / stats-analysis).

Runs inside MY-SKILLS pytest. Sibling checkouts are optional: when absent, the
related assertions skip so the suite stays portable. No new QC framework.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

from tests.support import ONE, ROOT

LAB_PATHS = ONE / "references" / "lab-paths.yaml"
LEGACY = ONE / "legacy_aliases.yaml"
REGISTRY = ONE / "registry.yaml"

REQUIRED_STATS_REL = (
    "modules",
    "modules/__init__.py",
    "pyproject.toml",
    "README.md",
)

RULES_SKILL_PATH_RE = re.compile(
    r"(?:\{SKILLS\}|\{skills_git\}|\{skills_runtime\}|MY-SKILLS)"
    r"[\\/]+"
    r"([A-Za-z0-9_.\\/-]+\.(?:md|yaml|yml|txt|mmd))",
)

VERSION_MARK_RE = re.compile(r"__version__\s*=\s*[\"']([^\"']+)[\"']")
SEAT_RE = re.compile(r"`((?:00|02|03|05|06|07)_[a-z0-9-]+)`")


def _sibling(name: str) -> Path | None:
    data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
    aliases = data.get("aliases") or {}
    key = {
        "MY-RULES": "rules_git",
        "stats-analysis": "code_stats",
        "MY-SKILLS": "skills_git",
    }.get(name)
    if key and key in aliases:
        p = Path(str(aliases[key]))
        if p.is_dir():
            return p
    cand = ROOT.parent / name
    if cand.is_dir():
        return cand
    return None


class CrossRepoContract(unittest.TestCase):
    def test_rules_skills_cited_paths_exist(self) -> None:
        """Rules docs that cite concrete Skills files / seats must resolve."""
        rules = _sibling("MY-RULES")
        if rules is None:
            self.skipTest("MY-RULES sibling / rules_git absent")
        missing: list[str] = []
        for name in ("skills.md", "My rule.md", "README.md"):
            path = rules / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for m in RULES_SKILL_PATH_RE.finditer(text):
                rel = m.group(1).replace("\\", "/")
                target = ROOT / rel
                if not target.exists():
                    missing.append(f"{name}: {rel}")
            if name in ("skills.md", "My rule.md"):
                for m in SEAT_RE.finditer(text):
                    seat = m.group(1)
                    if not (ROOT / seat).is_dir():
                        missing.append(f"{name}: seat {seat}")
        self.assertEqual(
            missing,
            [],
            "Rules->Skills broken cites:\n" + "\n".join(missing),
        )

    def test_code_stats_layout_matches_stats_analysis(self) -> None:
        """lab-paths {code_stats}/{code_modules} must match stats-analysis layout."""
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        for key in ("code_stats", "code_modules"):
            self.assertIn(key, aliases)
        stats = Path(str(aliases["code_stats"]))
        modules = Path(str(aliases["code_modules"]))
        if not stats.is_dir():
            self.skipTest(f"code_stats absent: {stats}")
        for rel in REQUIRED_STATS_REL:
            self.assertTrue((stats / rel).exists(), f"code_stats missing {rel}")
        self.assertEqual(
            modules.resolve(),
            (stats / "modules").resolve(),
            "code_modules must be code_stats/modules",
        )
        init = (stats / "modules" / "__init__.py").read_text(encoding="utf-8")
        m = VERSION_MARK_RE.search(init)
        self.assertIsNotNone(m, "modules/__init__.py missing __version__")
        pyproject = (stats / "pyproject.toml").read_text(encoding="utf-8")
        vm = re.search(r"(?m)^version\s*=\s*[\"']([^\"']+)[\"']", pyproject)
        self.assertIsNotNone(vm, "pyproject.toml missing version")
        self.assertEqual(m.group(1), vm.group(1))

    def test_retired_ids_not_live_in_registry(self) -> None:
        """legacy_aliases keys must not appear as LIVE registry fine ids."""
        la = yaml.safe_load(LEGACY.read_text(encoding="utf-8")) or {}
        retired = set((la.get("aliases") or {}).keys())
        reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
        live = {row["id"] for row in reg.get("fine_ids") or []}
        overlap = sorted(retired & live)
        self.assertEqual(overlap, [], f"retired ids still LIVE: {overlap}")

    def test_skills_version_marker_present(self) -> None:
        ver = ROOT / "VERSION.txt"
        self.assertTrue(ver.is_file())
        text = ver.read_text(encoding="utf-8").strip()
        self.assertTrue(text, "VERSION.txt empty")
        self.assertRegex(text, r"CHG-|20\d{6}")


if __name__ == "__main__":
    unittest.main()