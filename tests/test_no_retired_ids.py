"""QC Batch5: archived fine-ids must not reappear as live routing targets.

Retired set = registry.yaml archived ids (+ legacy_aliases keys that are not
still-on-disk path-unit directory names). Historical mention lines are allowed.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "01_skill-integration"

# Line-level historical / archival context (Chinese + English).
HIST_LINE = re.compile(
    r"archived|historical|legacy|absorb|absorbed|formerly|old_path|"
    r"status_note|covers former|round\s*[123]|勿建|归档|was\s+B|retired|"
    r"not on disk|do not recreate|do not mount|not a live",
    re.I,
)

# Files that may freely list retired ids (SSOT / mirrors / changelogs).
ALLOW_FILES = {
    "01_skill-integration/registry.yaml",
    "01_skill-integration/legacy_aliases.yaml",
    "01_skill-integration/MOUNTED_SKILLS.md",
    "01_skill-integration/references/id-rules.md",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "02_data-processing/base/README.md",  # 归档勿建 list
    "03_research/base/README.md",  # 归档勿建 list
    "04_analysis/base/README.md",  # path-unit table may echo alias keys
}

# Path-unit directory names that coincide with alias keys (not retired fine ids).
PATH_UNIT_ALIAS_KEYS = {
    "02-tables",
    "02-imaging-qc",
    "02-imaging-io",
    "02-radiomics-habitat",
    "04-fig-flow",
    "04-fig-plot",
    "04-stats-models",
    "04-model-eval",
    "fig-plot",
    "make-figures",
}


def _retired_ids() -> set[str]:
    reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))
    archived = {a["id"] for a in (reg.get("archived") or []) if a.get("id")}
    la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8"))
    alias_keys = set((la.get("aliases") or {}).keys())
    # Keep path-style / still-on-disk unit names out of the retired scan set.
    alias_keys -= PATH_UNIT_ALIAS_KEYS
    return archived | alias_keys


def _scan_paths() -> list[Path]:
    out: list[Path] = []
    for pat in (
        "*_*/SKILL.md",
        "*_*/personal/route.md",
        "*_*/base/**/MODULE.md",
        "00_orchestrator/workflows/*.md",
        "00_orchestrator/gates.md",
        "00_orchestrator/runtime-flow.mmd",
        "ARCHITECTURE.md",
        "README.md",
        "01_skill-integration/references/presets/*.yaml",
    ):
        out.extend(ROOT.glob(pat))
    return sorted({p.resolve() for p in out if p.is_file()})


# MODULE.md files carry upstream attribution and trigger words that legitimately
# echo retired source names. Only the routing section is a control-plane target.
HANDOFF_HEAD = re.compile(
    r"^#{1,6}\s*(handoffs?\b|routes?\b|next steps?\b|open when\b)", re.I
)


def _routing_lines(path: Path, text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    in_section = False
    for i, line in enumerate(text.splitlines(), 1):
        if re.match(r"^#{1,6}\s", line):
            in_section = bool(HANDOFF_HEAD.match(line))
            continue
        if in_section:
            rows.append((i, line))
    return rows


class NoRetiredIds(unittest.TestCase):
    def test_control_plane_has_no_live_retired_ids(self) -> None:
        retired = _retired_ids()
        self.assertGreaterEqual(len(retired), 30)
        violations: list[str] = []
        for path in _scan_paths():
            rel = path.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES:
                continue
            text = path.read_text(encoding="utf-8")
            if rel.endswith("MODULE.md"):
                rows = _routing_lines(path, text)
            else:
                rows = list(enumerate(text.splitlines(), 1))
            for i, line in rows:
                if HIST_LINE.search(line):
                    continue
                for rid in retired:
                    if re.search(
                        r"(?<![A-Za-z0-9_./-])" + re.escape(rid) + r"(?![A-Za-z0-9_-])",
                        line,
                    ):
                        violations.append(f"{rel}:{i}: {rid} :: {line.strip()[:100]}")
        self.assertEqual(violations, [], "live retired-id mentions:\n" + "\n".join(violations[:40]))

    def test_preset_include_lists_exclude_archived_ids(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))
        archived = {a["id"] for a in (reg.get("archived") or []) if a.get("id")}
        preset_dir = ONE / "references" / "presets"
        bad: list[str] = []
        for path in sorted(preset_dir.glob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            # Collect list-like include fields only (not free-text notes).
            chunks: list[object] = []
            for key in (
                "must_include",
                "fine_ids",
                "force_fine_ids",
                "include",
                "mounts",
                "skills",
                "ids",
            ):
                if key in data:
                    chunks.append(data[key])
            # nested common shapes
            for section in data.values():
                if isinstance(section, dict):
                    for key in ("must_include", "fine_ids", "force_fine_ids", "ids"):
                        if key in section:
                            chunks.append(section[key])

            def walk(obj: object) -> None:
                if isinstance(obj, str):
                    tok = obj.split("#", 1)[0].strip()
                    if tok in archived:
                        bad.append(f"{path.name}: active include `{tok}`")
                elif isinstance(obj, list):
                    for x in obj:
                        walk(x)
                elif isinstance(obj, dict):
                    for x in obj.values():
                        walk(x)

            for c in chunks:
                walk(c)
        self.assertEqual(bad, [], "presets still include archived ids:\n" + "\n".join(bad))


if __name__ == "__main__":
    unittest.main()
