"""CHG-20260926-008: every repo YAML file must parse with yaml.safe_load."""
from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
# mounts-cap pack dirs and STATE.yaml are gitignored local caches, not repo files.
MOUNTS_CAP_TRACKED = {"INDEX.yaml"}
SKIP_PARTS = {".git", "__pycache__", "node_modules"}


def repo_yaml_files() -> list[Path]:
    if (ROOT / ".git").exists():
        out = subprocess.check_output(
            ["git", "-c", "core.quotepath=false", "ls-files", "--", "*.yaml", "*.yml"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        )
        rels = [line for line in out.splitlines() if line]
        return [ROOT / r for r in rels]
    files = []
    for p in list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.yml")):
        rel = p.relative_to(ROOT)
        if SKIP_PARTS & set(rel.parts):
            continue
        if rel.parts[0] == "mounts-cap" and (len(rel.parts) > 2 or rel.name not in MOUNTS_CAP_TRACKED):
            continue
        files.append(p)
    return files


class YamlValid(unittest.TestCase):
    def test_all_repo_yaml_parses(self) -> None:
        files = repo_yaml_files()
        self.assertGreaterEqual(len(files), 10, msg=str(files))
        bad = []
        for p in files:
            try:
                yaml.safe_load(p.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                bad.append(f"{p.relative_to(ROOT)}: {exc}")
        self.assertEqual(bad, [], msg="\n".join(bad))

    def test_presets_are_included(self) -> None:
        names = {p.name for p in repo_yaml_files()}
        for n in ("review-hybrid.yaml", "evidence-deep-L2.yaml", "manuscript-final-W2.yaml", "external-review-R1.yaml"):
            self.assertIn(n, names)


if __name__ == "__main__":
    unittest.main()
