"""Ledger freshness and assurance vocabulary.

Merged from: `test_ledger_freshness.py`.
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
