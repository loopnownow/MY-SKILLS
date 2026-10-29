"""Ledger freshness and assurance vocabulary.

Merged from: `test_ledger_freshness.py`.
"""
from __future__ import annotations

import re
import unittest
import yaml

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

CHG_RE = re.compile(r"CHG-(\d{8})")
CHG_FULL = re.compile(r"CHG-\d{8}-[a-z0-9-]+")
VERSION_HEAD = re.compile(r"^(CHG-\d{8}-[a-z0-9-]+)", re.M)
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

        newest = CHG_FULL.findall((ROOT / "INTEGRATION_MAP.md").read_text(encoding="utf-8"))
        self.assertTrue(newest, "INTEGRATION_MAP.md has no CHG-YYYYMMDD-slug entry")
        self.assertEqual(
            change_id,
            newest[0],
            "registry change_id must equal the newest INTEGRATION_MAP entry",
        )
        head = VERSION_HEAD.search((ROOT / "VERSION.txt").read_text(encoding="utf-8"))
        self.assertIsNotNone(head, "VERSION.txt has no top CHG entry")
        self.assertEqual(
            change_id,
            head.group(1),
            "registry change_id must equal the top VERSION.txt entry",
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
