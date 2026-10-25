"""Registry, mirrors and alias-target contract.

Merged from: `test_registry_mirrors.py`, `test_registry_paths.py`, `test_alias_targets_exist.py`.
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
        bad = [m["id"] for m in reg["mounts"] if m.get("source") == "my-skills-base"]
        self.assertEqual(bad, [])
        self.assertNotIn("archived", reg)
        self.assertNotIn("default_source", reg)
        self.assertFalse((ONE / "sources" / "b-my-skills-base.yaml").exists())
        live_a = [m for m in reg["mounts"] if m.get("source") == "my-skills"]
        self.assertGreaterEqual(len(live_a), 20)
        self.assertEqual(len(live_a), len(reg["mounts"]))
class RegistryPaths(unittest.TestCase):
    def test_mount_count_matches_meta(self) -> None:
        self.assertEqual(len(REG["mounts"]), REG["meta"]["fine_id_count_canonical"])

    def test_mount_paths_exist(self) -> None:
        for mount in REG["mounts"]:
            self.assertTrue((ROOT / mount["path"]).is_dir(), mount["id"])

    def test_dir_equals_fine_id(self) -> None:
        for mount in REG["mounts"]:
            name = _base_name(mount["path"])
            if name == mount["id"]:
                continue
            self.assertEqual(
                ALIASES.get(mount["id"]),
                name,
                f"{mount['id']} points at {name}; declare it as an alias instead",
            )

    def test_shared_paths_are_aliased(self) -> None:
        seen: dict[str, str] = {}
        for mount in REG["mounts"]:
            key = mount["path"].replace("\\", "/").rstrip("/")
            if key in seen:
                self.assertIn(
                    mount["id"],
                    ALIASES,
                    f"{mount['id']} shares {key} with {seen[key]} without an alias entry",
                )
            seen.setdefault(key, mount["id"])

    def test_every_base_dir_is_registered(self) -> None:
        mounted = {_base_name(m["path"]) for m in REG["mounts"]}
        local = {p["id"] for p in REG.get("local_packs") or []}
        missing = []
        for domain in sorted(p for p in ROOT.glob("0[0-7]_*") if p.is_dir()):
            base = domain / "base"
            if not base.is_dir():
                continue
            for pack in sorted(p for p in base.iterdir() if p.is_dir()):
                if pack.name not in mounted | local:
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
            for m in (reg.get("mounts") or [])
            if isinstance(m, dict) and m.get("id")
        }
        self.assertGreaterEqual(len(ids), 20, "registry mounts not parsed")

        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("aliases") or {}).items()
            if str(v) not in ids
        ]
        self.assertEqual(bad, [], "alias targets that are not live mount ids:\n" + "\n".join(bad))

    def test_coarse_alias_values_are_registry_coarse(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        coarse = {
            m.get("coarse") for m in (reg.get("mounts") or []) if isinstance(m, dict)
        }
        coarse.discard(None)
        for c in reg.get("coarse_ids") or []:
            if isinstance(c, dict) and c.get("id"):
                coarse.add(c["id"])
        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("coarse_aliases") or {}).items()
            if str(v) not in coarse
        ]
        self.assertEqual(bad, [], "coarse alias targets not in registry:\n" + "\n".join(bad))
