"""Registry mirrors, fine-id paths, alias targets, and ledger freshness.

Merged from earlier registry contract modules + `test_ledger_assurance.py`.
"""
from __future__ import annotations

import re
import subprocess
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
            self.assertEqual(
                _base_name(fine_id["path"]),
                fine_id["id"],
                f"{fine_id['id']} path must end with the fine id (no alias table)",
            )

    def test_live_paths_are_unique(self) -> None:
        seen: dict[str, str] = {}
        for fine_id in REG["fine_ids"]:
            key = fine_id["path"].replace("\\", "/").rstrip("/")
            self.assertNotIn(
                key,
                seen,
                f"{fine_id['id']} shares {key} with {seen.get(key)}",
            )
            seen[key] = fine_id["id"]

    def test_every_base_dir_is_registered(self) -> None:
        live = {_base_name(m["path"]) for m in REG["fine_ids"]}
        local = {p["id"] for p in REG.get("local_packs") or []}
        registered = {
            m["path"].replace("\\", "/").rstrip("/")
            for m in REG["fine_ids"]
        }
        registered |= {
            p["path"].replace("\\", "/").rstrip("/")
            for p in REG.get("local_packs") or []
        }
        frontmatter = re.compile(r"^---\s*\n(.*?)\n---\s*$", re.S | re.M)
        missing = []
        for domain in sorted(p for p in ROOT.glob("0[0-7]_*") if p.is_dir()):
            base = domain / "base"
            if not base.is_dir():
                continue
            for skill in sorted(base.rglob("SKILL.md")):
                pack = skill.parent
                rel = pack.relative_to(ROOT).as_posix()
                if rel in registered or pack.name in live | local:
                    continue
                text = skill.read_text(encoding="utf-8-sig", errors="ignore")
                match = frontmatter.search(text)
                data = (yaml.safe_load(match.group(1)) if match else None) or {}
                if isinstance(data, dict) and data.get("routable") is False:
                    continue
                missing.append(rel)
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
                    if data.get("routable") is False and not str(data.get("name", "")).strip():
                        continue
                    if str(data.get("name", "")).strip() != pack.name:
                        problems.append(
                            f"{doc.relative_to(ROOT).as_posix()}: name={data.get('name')!r} dir={pack.name!r}"
                        )
        self.assertEqual(problems, [], "frontmatter name drift:\n" + "\n".join(problems[:20]))

    def test_local_pack_dir_matches_id(self) -> None:
        for pack in REG.get("local_packs") or []:
            self.assertEqual(_base_name(pack["path"]), pack["id"], pack["id"])
            self.assertTrue((ROOT / pack["path"]).is_dir(), pack["id"])
class NoAliasTable(unittest.TestCase):
    def test_legacy_aliases_file_is_gone(self) -> None:
        self.assertFalse((ONE / "legacy_aliases.yaml").exists())
        self.assertFalse((ROOT / "INTEGRATION_MAP.md").exists())


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

# --- Changelog / version (replaces ledger freshness) ---
TICKET_RE = re.compile(r"\bt((?:\d{4}u|\d{8}[a-z]))\b")


def _registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}


class ChangelogAndVersion(unittest.TestCase):
    def test_version_txt_is_one_line(self) -> None:
        text = (ROOT / "VERSION.txt").read_text(encoding="utf-8")
        lines = [ln for ln in text.splitlines() if ln.strip()]
        self.assertEqual(len(lines), 1, "VERSION.txt must be a single version line")
        self.assertRegex(lines[0].strip(), r"^\d+\.\d+(\.\d+)?$")
        self.assertNotIn("CHG-", text)

    def test_registry_version_matches_version_txt(self) -> None:
        meta = _registry().get("meta") or {}
        ver = (ROOT / "VERSION.txt").read_text(encoding="utf-8").strip()
        self.assertEqual(str(meta.get("version") or "").strip(), ver)
        self.assertNotIn("change_id", meta)

    def test_changelog_exists_newest_first(self) -> None:
        path = ROOT / "CHANGELOG.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        self.assertIn("t2307u", text)
        dates = re.findall(r"^-\s+(20\d{2}-\d{2}-\d{2})", text, re.M)
        self.assertTrue(dates, "CHANGELOG.md has no dated entries")
        self.assertEqual(dates, sorted(dates, reverse=True), "CHANGELOG.md is not newest-first")

    def test_legacy_ledgers_are_gone(self) -> None:
        self.assertFalse((ROOT / "INTEGRATION_MAP.md").exists())
        self.assertFalse((ONE / "legacy_aliases.yaml").exists())

    def test_head_commit_ticket_ids_reach_changelog(self) -> None:
        try:
            head = subprocess.run(
                ["git", "log", "-1", "--format=%B"],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )
        except (OSError, subprocess.SubprocessError):
            self.skipTest("git unavailable")
        if head.returncode != 0:
            self.skipTest("git log unavailable")
        ticket_ids = sorted({m.group(1) for m in TICKET_RE.finditer(head.stdout)})
        self.assertTrue(
            ticket_ids, "no ticket id (tNNNNu or round tYYYYMMDDx) in HEAD commit message"
        )
        ledger = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        missing = [f"t{ticket}" for ticket in ticket_ids if f"t{ticket}" not in ledger]
        self.assertEqual(missing, [], "HEAD ticket ids missing from CHANGELOG.md: " + ", ".join(missing))


class RetiredBodies(unittest.TestCase):
    """Non-routable bodies stay out of the fine-id routing table."""

    def test_retired_bodies_are_not_routable(self) -> None:
        from tests.retired_ids import RETIRED_BODIES, RETIRED_FINE_IDS
        live = {m["id"] for m in REG["fine_ids"]}
        for name, rel in RETIRED_BODIES.items():
            self.assertNotIn(name, live, f"{name} is both live and a retired body")
            self.assertNotIn(name, RETIRED_FINE_IDS, f"{name} must not be a retired fine-id alias")
            self.assertTrue((ROOT / str(rel)).is_dir(), f"{name} body path missing: {rel}")
