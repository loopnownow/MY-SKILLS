"""E3: lightweight cross-repo contract (Rules / Skills / stats-analysis).

Runs inside MY-SKILLS pytest. Sibling checkouts are optional: when absent, the
related assertions skip so the suite stays portable. No new QC framework.
"""
from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
import tempfile
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
    "modules/provenance.py",
    "modules/tests/test_public_path_policy.py",
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
RETIRED_STATS_PATH = re.compile(
    r"_code[\\/]+04-analysis[\\/]+stats-analysis",
    re.I,
)


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


def _load_check_paths(rules: Path):
    path = rules / "check_paths.py"
    spec = importlib.util.spec_from_file_location("rules_check_paths", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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
                missing.append(f"required Rules file missing: {name}")
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
        for key in ("code_stats", "code_modules", "code_modules_master", "rules_git"):
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
        self.assertEqual(
            Path(str(aliases["code_modules_master"])).resolve(),
            modules.resolve(),
            "code_modules_master must equal code_modules",
        )
        init = (stats / "modules" / "__init__.py").read_text(encoding="utf-8")
        m = VERSION_MARK_RE.search(init)
        self.assertIsNotNone(m, "modules/__init__.py missing __version__")
        pyproject = (stats / "pyproject.toml").read_text(encoding="utf-8")
        vm = re.search(r"(?m)^version\s*=\s*[\"']([^\"']+)[\"']", pyproject)
        self.assertIsNotNone(vm, "pyproject.toml missing version")
        self.assertEqual(m.group(1), vm.group(1))

    def test_lab_mode_stats_provenance_public_path_contract(self) -> None:
        """N9: lab-paths + stats public-path / MODULES provenance stay aligned."""
        data = yaml.safe_load(LAB_PATHS.read_text(encoding="utf-8"))
        aliases = data["aliases"]
        # No live alias may still point at retired _code/04-analysis/stats-analysis.
        stale_alias = [
            f"{k}={v}"
            for k, v in aliases.items()
            if RETIRED_STATS_PATH.search(str(v))
        ]
        self.assertEqual(
            stale_alias,
            [],
            "lab-paths still points at retired stats path:\n" + "\n".join(stale_alias),
        )
        stats = _sibling("stats-analysis")
        if stats is None:
            self.skipTest("stats-analysis sibling / code_stats absent")
        prov = (stats / "modules" / "provenance.py").read_text(encoding="utf-8")
        self.assertIn("RAD_MODULES_STRICT", prov)
        self.assertIn("def enforce", prov)
        self.assertIn("Public path policy", prov)
        policy = (
            stats / "modules" / "tests" / "test_public_path_policy.py"
        ).read_text(encoding="utf-8")
        self.assertIn("DEFAULT_GROK_ROOT", policy)
        self.assertIn("Lab topology SSOT remains MY-SKILLS lab-paths.yaml", policy)
        readme = (stats / "README.md").read_text(encoding="utf-8")
        self.assertIn("Public-path policy", readme)
        self.assertIn("{code_stats}", readme)
        # Rules pointers must not contradict public stats path.
        rules = _sibling("MY-RULES")
        if rules is None:
            return
        for name in ("workspace-layout.md", "My rule.md", "skills.md", "README.md"):
            text = (rules / name).read_text(encoding="utf-8")
            for i, line in enumerate(text.splitlines(), 1):
                if not RETIRED_STATS_PATH.search(line):
                    continue
                if re.search(
                    r"retired|former|formerly|historical|legacy|archived|"
                    r"勿建|归档|历史|moved to|was\s",
                    line,
                    re.I,
                ):
                    continue
                self.fail(f"{name}:{i}: live retired stats path: {line.strip()[:120]}")

    def test_rules_check_paths_fail_loud(self) -> None:
        """N8: check_paths must not false-green when skills or required MD missing."""
        rules = _sibling("MY-RULES")
        if rules is None:
            self.skipTest("MY-RULES sibling / rules_git absent")
        cp = rules / "check_paths.py"
        self.assertTrue(cp.is_file())
        mod = _load_check_paths(rules)

        # Missing skills root -> non-zero (unless allow flag).
        env = {**os.environ, "SKILLS_ROOT": "", "MY_SKILLS": ""}
        # Point ROOT temporarily via subprocess with cwd=temp that has no sibling.
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            # Copy only check_paths into an empty fake rules root (no sibling skills).
            (tmp / "check_paths.py").write_text(cp.read_text(encoding="utf-8"), encoding="utf-8")
            # No required MD either - but missing skills should fail first.
            r = subprocess.run(
                [sys.executable, "-B", str(tmp / "check_paths.py"), "--check"],
                cwd=str(tmp),
                env={k: v for k, v in env.items() if k not in ("SKILLS_ROOT", "MY_SKILLS")},
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(
                r.returncode,
                0,
                f"missing skills must fail loud, got 0:\n{r.stdout}\n{r.stderr}",
            )
            r2 = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(tmp / "check_paths.py"),
                    "--check",
                    "--allow-missing-skills",
                ],
                cwd=str(tmp),
                env={k: v for k, v in env.items() if k not in ("SKILLS_ROOT", "MY_SKILLS")},
                capture_output=True,
                text=True,
            )
            self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)

        # Required MD missing while skills present -> fail.
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            fake_rules = tmp / "MY-RULES"
            fake_skills = tmp / "MY-SKILLS"
            fake_rules.mkdir()
            fake_skills.mkdir()
            (fake_rules / "check_paths.py").write_text(
                cp.read_text(encoding="utf-8"), encoding="utf-8"
            )
            # Only README present; skills.md / My rule.md missing.
            (fake_rules / "README.md").write_text("# stub\n", encoding="utf-8")
            r3 = subprocess.run(
                [sys.executable, "-B", str(fake_rules / "check_paths.py"), "--check"],
                cwd=str(fake_rules),
                env={**os.environ, "SKILLS_ROOT": str(fake_skills)},
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(
                r3.returncode,
                0,
                f"missing required MD must fail loud:\n{r3.stdout}\n{r3.stderr}",
            )
            self.assertIn("required Rules file missing", r3.stdout + r3.stderr)

        # Real layout must pass (green means real pass).
        r4 = subprocess.run(
            [sys.executable, "-B", str(cp), "--check"],
            cwd=str(rules),
            env={**os.environ, "SKILLS_ROOT": str(ROOT)},
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            r4.returncode,
            0,
            f"live Rules->Skills check must pass:\n{r4.stdout}\n{r4.stderr}",
        )

    def test_rules_md_path_scan_coverage(self) -> None:
        """N14: Rules check_paths scans MD for stale path claims; green = real pass."""
        rules = _sibling("MY-RULES")
        if rules is None:
            self.skipTest("MY-RULES sibling / rules_git absent")
        mod = _load_check_paths(rules)
        self.assertTrue(hasattr(mod, "check_stale_md_paths"))
        # Live tree should be clean.
        bad = mod.check_stale_md_paths()
        self.assertEqual(bad, [], "stale Rules MD paths:\n" + "\n".join(bad))
        # Inject a false-green guard: affirmative D:\\0Grok\\0del must be detected.
        sample = "落点 `D:\\0Grok\\0del\\_by-function` 即可。"
        hit = False
        for pat, _label, allow_if in mod.STALE_RULES:
            if pat.search(sample) and not allow_if.search(sample):
                hit = True
        self.assertTrue(hit, "stale scanner must catch affirmative D:\\0Grok\\0del")

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
