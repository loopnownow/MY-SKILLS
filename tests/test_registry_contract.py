"""Registry mirrors, fine-id paths, alias targets, and ledger freshness.

Merged from earlier registry contract modules + `test_ledger_assurance.py`.
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

def registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))
REG = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))
ALIASES = ((yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}).get("aliases") or {})
def _base_name(path: str) -> str:
    return path.replace("\\", "/").rstrip("/").split("/")[-1]

class RegistryMirrors(unittest.TestCase):
    def test_live_rows_are_in_repo_my_skills(self) -> None:
        """Live rows use in-repo my-skills; no second source id and no source-menu key."""
        reg = registry()
        bad = [m["id"] for m in reg["fine_ids"] if m.get("source") == "my-skills-base"]
        self.assertEqual(bad, [])
        self.assertNotIn("archived", reg)
        self.assertNotIn("default_source", reg)
        self.assertFalse((ONE / "sources" / "b-my-skills-base.yaml").exists())
        live_a = [m for m in reg["fine_ids"] if m.get("source") == "my-skills"]
        self.assertGreaterEqual(len(live_a), 20)
        self.assertEqual(len(live_a), len(reg["fine_ids"]))
class RegistryPaths(unittest.TestCase):
    def test_fine_id_count_matches_meta(self) -> None:
        self.assertEqual(len(REG["fine_ids"]), REG["meta"]["fine_id_count_canonical"])

    def test_fine_id_paths_exist(self) -> None:
        for fine_id in REG["fine_ids"]:
            self.assertTrue((ROOT / fine_id["path"]).is_dir(), fine_id["id"])

    def test_dir_equals_fine_id(self) -> None:
        for fine_id in REG["fine_ids"]:
            name = _base_name(fine_id["path"])
            if name == fine_id["id"]:
                continue
            self.assertEqual(
                ALIASES.get(fine_id["id"]),
                name,
                f"{fine_id['id']} points at {name}; declare it as an alias instead",
            )

    def test_shared_paths_are_aliased(self) -> None:
        seen: dict[str, str] = {}
        for fine_id in REG["fine_ids"]:
            key = fine_id["path"].replace("\\", "/").rstrip("/")
            if key in seen:
                self.assertIn(
                    fine_id["id"],
                    ALIASES,
                    f"{fine_id['id']} shares {key} with {seen[key]} without an alias entry",
                )
            seen.setdefault(key, fine_id["id"])

    def test_every_base_dir_is_registered(self) -> None:
        live = {_base_name(m["path"]) for m in REG["fine_ids"]}
        local = {p["id"] for p in REG.get("local_packs") or []}
        missing = []
        for domain in sorted(p for p in ROOT.glob("0[0-7]_*") if p.is_dir()):
            base = domain / "base"
            if not base.is_dir():
                continue
            for pack in sorted(p for p in base.iterdir() if p.is_dir()):
                if pack.name not in live | local:
                    missing.append(f"{domain.name}/base/{pack.name}")
        self.assertEqual(missing, [], "unregistered base packs: " + ", ".join(missing))

    def test_pack_frontmatter_name_matches_dir(self) -> None:
        pattern = re.compile(r"^---\s*\n(.*?)\n---\s*$", re.S | re.M)
        problems = []
        homes = []
        for domain in sorted(p for p in ROOT.glob("0[0-7]_*") if p.is_dir()):
            for folder_name in ("base", "qc"):
                folder = domain / folder_name
                if folder.is_dir():
                    homes.append(folder)
        for home in homes:
            for pack in sorted(p for p in home.iterdir() if p.is_dir()):
                for name in ("MODULE.md", "SKILL.md"):
                    doc = pack / name
                    if not doc.is_file():
                        continue
                    text = doc.read_text(encoding="utf-8-sig", errors="ignore")
                    match = pattern.search(text)
                    if not match:
                        problems.append(f"{doc.relative_to(ROOT).as_posix()}: no frontmatter")
                        continue
                    data = yaml.safe_load(match.group(1)) or {}
                    if str(data.get("name", "")).strip() != pack.name:
                        problems.append(
                            f"{doc.relative_to(ROOT).as_posix()}: name={data.get('name')!r} dir={pack.name!r}"
                        )
        self.assertEqual(problems, [], "frontmatter name drift:\n" + "\n".join(problems[:20]))

    def test_local_pack_dir_matches_id(self) -> None:
        for pack in REG.get("local_packs") or []:
            self.assertEqual(_base_name(pack["path"]), pack["id"], pack["id"])
            self.assertTrue((ROOT / pack["path"]).is_dir(), pack["id"])
class AliasTargets(unittest.TestCase):
    def test_alias_values_are_known_ids(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {
            m["id"]
            for m in (reg.get("fine_ids") or [])
            if isinstance(m, dict) and m.get("id")
        }
        self.assertGreaterEqual(len(ids), 20, "registry fine_ids not parsed")

        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("aliases") or {}).items()
            if str(v) not in ids
        ]
        self.assertEqual(bad, [], "alias targets that are not live fine ids:\n" + "\n".join(bad))

    def test_coarse_alias_values_are_registry_coarse(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        coarse = {
            c["id"] for c in (reg.get("coarse_ids") or []) if isinstance(c, dict) and c.get("id")
        }
        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("coarse_aliases") or {}).items()
            if str(v) not in coarse
        ]
        self.assertEqual(bad, [], "coarse alias targets not in registry:\n" + "\n".join(bad))


class SeatBuckets(unittest.TestCase):
    """2026-10-25: coarse id = execution seat; a fine_id's bucket is its a_domain."""

    def test_fine_ids_declare_no_coarse_field(self) -> None:
        offenders = [m["id"] for m in REG["fine_ids"] if "coarse" in m]
        self.assertEqual(
            offenders,
            [],
            "fine_ids must not carry a coarse field (bucket comes from a_domain):\n"
            + "\n".join(offenders),
        )

    def test_seat_rows_are_the_five_seats(self) -> None:
        seats = [c["id"] for c in REG["coarse_ids"]]
        self.assertEqual(
            seats,
            [
                "02_data-processing",
                "03_research",
                "05_manuscript",
                "06_review",
                "07_response",
            ],
        )
        self.assertEqual(REG["meta"]["coarse_id_count"], len(seats))

    def test_every_a_domain_is_a_seat(self) -> None:
        seats = {c["id"] for c in REG["coarse_ids"]}
        bad = [
            f"{m['id']} -> {m.get('a_domain')}"
            for m in REG["fine_ids"]
            if m.get("a_domain") not in seats
        ]
        self.assertEqual(bad, [], "a_domain outside the seats:\n" + "\n".join(bad))

    def test_fine_id_owner_dir_matches_a_domain(self) -> None:
        for fine_id in REG["fine_ids"]:
            self.assertEqual(fine_id["path"].split("/")[0], fine_id["a_domain"], fine_id["id"])

# --- Merged from test_ledger_assurance.py ---
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
