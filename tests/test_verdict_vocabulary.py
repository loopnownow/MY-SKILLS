"""One verdict vocabulary: NOT_APPLICABLE, not N/A / n/a / "not applicable" / SKIP.

`06_review/qc/assurance-verdicts.md` owns the six states. Drift into
prose variants made machine reads (and human greps) miss real verdicts, so the
variants are rejected here. Line-level exemptions cover the three legitimate
uses that are not verdicts.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BAD = re.compile(r"N/A|(?<![A-Za-z])n/a|(?i:not applicable)|(?<![A-Za-z])SKIP(?![A-Za-z])")
EXEMPT_LINE = (
    re.compile(r"#N/A"),        # Excel error code in a vendored pack
    re.compile(r"SKIP_[A-Z]"),  # configuration token, not a verdict
)
EXEMPT_PAIRS = (
    # Quoted manuscript sentence showing correct English usage.
    ("05_manuscript/personal/Aitor-format.md", "were not applicable"),
)


class VerdictVocabulary(unittest.TestCase):
    def test_no_variant_verdict_tokens(self) -> None:
        violations: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("tests/"):
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if not BAD.search(line):
                    continue
                if any(rx.search(line) for rx in EXEMPT_LINE):
                    continue
                if any(rel == f and snippet in line for f, snippet in EXEMPT_PAIRS):
                    continue
                violations.append(f"{rel}:{i}: {line.strip()[:110]}")
        self.assertEqual(
            violations,
            [],
            "use NOT_APPLICABLE (assurance-verdicts.md):\n" + "\n".join(violations[:40]),
        )


if __name__ == "__main__":
    unittest.main()
