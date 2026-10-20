"""QC Batch5: backtick in-repo paths under live domains must exist (allowlisted debt OK)."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BT = re.compile(r"`([^`]+)`")

TOPS = (
    "00_orchestrator/",
    "01_skill-integration/",
    "02_data-processing/",
    "03_research/",
    "04_analysis/",
    "05_manuscript/",
    "06_review/",
    "07_response/",
    "tests/",
    "docs/",
)

# Known missing / relocated / archived path mentions still present in prose.
# Prefer shrinking this list over growing it.
ALLOW_MISSING = {
    "docs/",  # optional viz outputs; often regenerated locally
    # Explicit "do NOT create this parallel file" example in coding-qc.md.
    # Not a pointer; keep the token so the ban stays readable.
    "02_data-processing/code-qc.md",
}

SKIP_FILE_PREFIXES = (
    "VERSION.txt",
    "INTEGRATION_MAP.md",
)


class InlinePathsExist(unittest.TestCase):
    def test_backtick_repo_paths_exist_or_allowlisted(self) -> None:
        missing: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            if path.parts[0] == "tests":
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in SKIP_FILE_PREFIXES or rel.startswith(SKIP_FILE_PREFIXES):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for m in BT.finditer(text):
                tok = m.group(1).strip()
                if "/" not in tok and "\\" not in tok:
                    continue
                if tok.startswith(
                    ("http://", "https://", "D:", "L:", "C:", "{", "<", "#", "mailto:", "file:")
                ):
                    continue
                clean = tok.split()[0].rstrip(".,);:\"'")
                clean = clean.replace("\\", "/").split("#", 1)[0]
                if clean.startswith("./"):
                    clean = clean[2:]
                if not clean.startswith(TOPS):
                    continue
                if clean in ALLOW_MISSING:
                    continue
                if not (ROOT / clean).exists():
                    missing.append(f"{rel}: `{clean}`")
        self.assertEqual(
            missing,
            [],
            "inline paths missing (add to ALLOW_MISSING only with cause):\n"
            + "\n".join(missing[:50]),
        )




# Bare relative cites that historically bypassed the TOP-prefix checker.
FORBIDDEN_BARE_RELATIVE = (
    "qc/local-checks.md",
)

class BareRelativeCites(unittest.TestCase):
    def test_no_forbidden_bare_relative_cites(self) -> None:
        hits: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("tests/") or rel in SKIP_FILE_PREFIXES or rel.startswith(SKIP_FILE_PREFIXES):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for bare in FORBIDDEN_BARE_RELATIVE:
                needle = f"`{bare}`"
                if needle in text:
                    hits.append(f"{rel}: {needle}")
        self.assertEqual(hits, [], "forbidden bare relative cites:\n" + "\n".join(hits[:40]))

if __name__ == "__main__":
    unittest.main()
