"""The change ledger must cover the registry's current change_id.

Guards against landing content changes without a VERSION / INTEGRATION_MAP row
(the 2026-10-20 renames first shipped with `change_id: CHG-20261007-001`).
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "01_skill-integration"
CHG_RE = re.compile(r"CHG-(\d{8})")


def _registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}


class LedgerFreshness(unittest.TestCase):
    def test_registry_change_id_reaches_both_ledgers(self) -> None:
        meta = _registry().get("meta") or {}
        change_id = str(meta.get("change_id") or "")
        self.assertTrue(CHG_RE.search(change_id), f"bad change_id: {change_id!r}")

        for name in ("VERSION.txt", "INTEGRATION_MAP.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(
                change_id,
                text,
                f"{name} has no entry for registry change_id {change_id}",
            )

    def test_version_top_is_not_older_than_registry(self) -> None:
        meta = _registry().get("meta") or {}
        reg_date = CHG_RE.search(str(meta.get("change_id") or "")).group(1)
        version = (ROOT / "VERSION.txt").read_text(encoding="utf-8")
        dates = CHG_RE.findall(version)
        self.assertTrue(dates, "VERSION.txt has no CHG-YYYYMMDD block")
        self.assertGreaterEqual(
            max(dates),
            reg_date,
            "VERSION.txt is older than the registry change_id",
        )


if __name__ == "__main__":
    unittest.main()
