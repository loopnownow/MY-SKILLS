"""2026-10-30: 03 fine-id true absorb (-3) + lit-fulltext LIVE."""
from __future__ import annotations

import re
import unittest
import yaml

from tests.support import ONE, ROOT

ABSORBED_DIRS = (
    "03_research/base/retraction-watcher",
    "03_research/base/write-protocol",
    "03_research/base/grant-builder",
)
DEAD_IDS = ("retraction-watcher", "write-protocol", "grant-builder")
WHITELIST = {
    "tests/test_03_fineid_absorb_20261030.py",
    "00_orchestrator/legacy_aliases.yaml",
    "00_orchestrator/registry.yaml",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "03_research/base/README.md",
    "03_research/base/verify-refs/LICENSE_NOTE.txt",
    "03_research/base/verify-refs/references/retraction-audit.md",
    "03_research/base/fill-protocol/MODULE.md",
    "03_research/base/lit-fulltext/LICENSE_NOTE.txt",
    "03_research/base/lit-fulltext/MODULE.md",
    "03_research/base/lit-fulltext/scripts/fetch.py",
    "NOTICE",
}


def _registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))


def _aliases() -> dict:
    return (
        yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
    ).get("aliases") or {}


class AbsorbContract(unittest.TestCase):
    def test_alias_keys_not_live(self) -> None:
        live = {m["id"] for m in _registry()["fine_ids"]}
        overlap = set(_aliases()) & live
        self.assertEqual(overlap, set())

    def test_alias_targets_live(self) -> None:
        live = {m["id"] for m in _registry()["fine_ids"]}
        bad = [f"{k}->{v}" for k, v in _aliases().items() if v not in live]
        self.assertEqual(bad, [])

    def test_absorbed_dirs_gone(self) -> None:
        for rel in ABSORBED_DIRS:
            self.assertFalse((ROOT / rel).exists(), rel)

    def test_no_live_refs_to_dead_ids(self) -> None:
        skip_suffix = {".pyc", ".png", ".jpg", ".pdf", ".docx"}
        violations: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in WHITELIST or rel.startswith("tests/") or ".git/" in rel:
                continue
            if path.suffix.lower() in skip_suffix:
                continue
            if "__pycache__" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            for dead in DEAD_IDS:
                if not re.search(rf"\b{re.escape(dead)}\b", text):
                    continue
                violations.append(f"{rel}: {dead}")
        self.assertEqual(violations, [], "\n".join(violations[:50]))

    def test_fine_id_count(self) -> None:
        reg = _registry()
        self.assertEqual(len(reg["fine_ids"]), reg["meta"]["fine_id_count_canonical"])

    def test_lit_fulltext_live(self) -> None:
        reg = _registry()
        row = next(m for m in reg["fine_ids"] if m["id"] == "lit-fulltext")
        self.assertEqual(row["path"].rstrip("/"), "03_research/base/lit-fulltext")
        self.assertTrue((ROOT / "03_research/base/lit-fulltext/MODULE.md").is_file())
        self.assertTrue((ROOT / "03_research/base/lit-fulltext/scripts/fetch.py").is_file())
        self.assertGreater((ROOT / "03_research/base/lit-fulltext/scripts/fetch.py").stat().st_size, 0)
        self.assertNotIn("fetch_oa.py", (ROOT / "03_research/base/lit-fulltext/MODULE.md").read_text(encoding="utf-8"))
        self.assertNotIn("03-lit-fulltext", _aliases())


if __name__ == "__main__":
    unittest.main()
