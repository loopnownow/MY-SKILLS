"""Bare ``*.md`` cites in backticks must resolve somewhere in the repo.

Deep-scan 2026-10-20: eight dead pointers (`sentence-templates.md`,
`stats-checklist.md`, `radiology-submission-map.md`, `manuscript-docx.md`,
`manuscript-style-classical.md`, `corpus-phrase-bank.md`, ...) survived 145 tests
because nothing checked filename-only cites.

Rules
- A backticked ``foo.md`` (no slash) must exist somewhere in the tree, or be
  listed as an external/upstream doc, or be a report artifact the user creates.
- Lines that already mark the name as former/merged/archived are skipped.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}

NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{2,58}\.md$")
TICK_RE = re.compile(r"`([^`]{2,90})`")
HIST_LINE = re.compile(
    r"archived|historical|legacy|former|formerly|merged|absorbed|retired|relocated|"
    r"pruned|not on disk|do not recreate|do not create|distill of|dated snapshot|"
    r"勿建|不另建|归档|已并入|历史",
    re.I,
)

# Documents that live on the lab disk (0doc), in an upstream skill, in MY-RULES,
# or in a dated snapshot note, not in this repo.
EXTERNAL = {
    "lab-palettes.md",  # {doc_root}\templates\lab-palettes.md
    "Lab-STE-SPEC.md",  # {doc_lab_ste}\Lab-STE-SPEC.md
    "acceptance-gate.md",  # ARIS shared-references (attribution only)
    "gate_mechanical.md",  # SNL-UCSB paper-writing skill (MIT, upstream)
    "citation-formats.md",  # retraction-watcher upstream docs
    "api-documentation.md",  # retraction-watcher upstream docs
    "experiment-integrity.md",  # ARIS experiment-audit distill note (attribution)
    "evidence-precheck.md",  # ARIS result-to-claim distill note (attribution)
    "evidence-request.md",  # A05 evidence-request template (lab, not vendored)
    "skills.md",  # MY-RULES skills.md
    "coding-principles.md",  # named only as a "do not create" ban
    "changelog.md",  # per-project ref/review artifact
    "CHANGELOG_*.md",  # glob form in docs; ignore if matched
    "manuscript-revision.md",  # per-project Word change ledger
    "EXECUTION.md",  # optional per-project wrap-up
    "workspace-layout.md",  # standing-delivery pointer name
    "structures.md",  # upstream/general-prose reference list
    "examples.md",  # upstream/general-prose reference list
    "literature-evidence-2023-2026.md",  # dated snapshot note (归档勿建)
    "INTEGRATION_MAP-20261007.md",  # monthly archive under {DEL}
    "INTEGRATION_MAP.archive.md",  # older archive under {DEL}
    "INTEGRATION_MAP-YYYYMMDD.md",  # archive naming pattern
    # 0doc / park / harvest (not vendored into MY-SKILLS)
    "INDEX-thesis.md",  # roles-park thesis quote index
    "themes.md",  # {doc_root}\_library\lit-corpus\themes.md
    "HARVEST-STANDARD.md",  # {doc_root}\skill-harvest\
    "harvest-projects-cut.md",  # skill-harvest companion
    "harvest-verified-links.md",  # skill-harvest companion
    # grant fulltext skeleton section headings (park originals, not in repo)
    "03-002-03-guojiazirankexuejijin-qingnianxiangmu.md",
    "03-003-03-fudandaxue-boshibaokao.md",
    "03-004-03-jinshanquweijianwei.md",
    "03-005-03-jinshanyiyuan-yanjiushengketi.md",
    "03-006-03-jinshanyiyuan-yanjiushengketi-2.md",
    "03-007-03-jinshanyiyuan-yanjiushengketi-3.md",
    "03-008-03-jinshanyiyuan-yuanjikeyanjijin.md",
}

# Report artifacts the running task writes; they are names, not repo files.
ARTIFACTS = {
    "RESUBMIT_REPORT.md",
    "PAPER_CLAIM_AUDIT.md",
    "CLAIMS_FROM_RESULTS.md",
    "figure-manifest.md",
    "journals-submitted.md",
    "house-format.md",
    "0rad-workspace.md",
}


def _iter_md():
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix == ".md" and not (SKIP_DIRS & set(p.parts)):
            yield p


class BareMdCites(unittest.TestCase):
    def test_bare_md_names_resolve(self) -> None:
        known = {p.name for p in ROOT.rglob("*") if p.is_file()}
        missing: list[str] = []
        for path in _iter_md():
            rel = path.relative_to(ROOT).as_posix()
            for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if HIST_LINE.search(line):
                    continue
                for m in TICK_RE.finditer(line):
                    tok = m.group(1).strip()
                    if not NAME_RE.match(tok) or "/" in tok:
                        continue
                    if tok in known or tok in EXTERNAL or tok in ARTIFACTS:
                        continue
                    missing.append(f"{rel}:{i}: `{tok}`")
        self.assertEqual(
            missing,
            [],
            "bare .md cites that resolve nowhere (add the file, fix the cite, or "
            "list it in EXTERNAL/ARTIFACTS):\n" + "\n".join(missing[:40]),
        )


if __name__ == "__main__":
    unittest.main()
