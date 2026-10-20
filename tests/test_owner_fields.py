"""QC Batch5: owner: fields under base/** must point at in-repo paths."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER_RE = re.compile(r"^owner:\s*[\"']?([^\"'\n]+)[\"']?\s*$", re.M)

# owner values that are intentionally external / not path checks
ALLOW_OWNER_VALUES: set[str] = set()


class OwnerFields(unittest.TestCase):
    def test_base_owner_fields_resolve(self) -> None:
        missing: list[str] = []
        seen = 0
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.name not in ("SKILL.md", "MODULE.md"):
                continue
            if "base" not in path.parts:
                continue
            if any(p.startswith(".") for p in path.parts):
                continue
            text = path.read_text(encoding="utf-8")
            for m in OWNER_RE.finditer(text):
                seen += 1
                owner = m.group(1).strip().strip("\"'")
                if owner in ALLOW_OWNER_VALUES:
                    continue
                # owners are repo-relative posix paths
                target = ROOT / owner
                if not target.exists():
                    rel = path.relative_to(ROOT).as_posix()
                    missing.append(f"{rel}: owner={owner}")
        self.assertGreaterEqual(seen, 20, "expected many owner: fields under base/")
        self.assertEqual(missing, [], "owner paths missing:\n" + "\n".join(missing))


if __name__ == "__main__":
    unittest.main()
