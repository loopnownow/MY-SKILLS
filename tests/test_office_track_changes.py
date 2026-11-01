"""Office tooling: the tracked-changes validator must not pass a silent overwrite.

The lab rule (MY-RULES `My rule.md` 5.1, `06_review/advanced/word-edit.md`) is that
every `.docx` edit lands under Track Changes. The upstream Anthropic validator used to
return True as soon as it found no revisions under the requested author, which is
exactly the case a silent overwrite produces — so the guard never fired for the
author the lab actually uses ("A").
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import yaml

from tests.support import ROOT


def _resolve_office() -> Path | None:
    """The office package lives in MY-CODES (t1521u P3-D); resolve {code_stats} from lab-paths."""
    data = (
        yaml.safe_load(
            (ROOT / "00_orchestrator" / "references" / "lab-paths.yaml").read_text(
                encoding="utf-8"
            )
        )
        or {}
    )
    root = str((data.get("aliases") or {}).get("code_stats") or "")
    if not root:
        return None
    hit = Path(root) / "tools" / "office"
    return hit if hit.is_dir() else None


OFFICE = _resolve_office()
if OFFICE is None:
    raise unittest.SkipTest(
        "MY-CODES checkout with tools/office not found ({code_stats}); "
        "office validator contract skipped on a partial checkout"
    )

try:
    sys.path.insert(0, str(OFFICE))
    from validators import RedliningValidator  # noqa: E402

    HAVE_VALIDATOR = True
except ImportError:  # lxml / defusedxml not installed on this host
    HAVE_VALIDATOR = False

BASE_PARAGRAPH = "Baseline sentence."


def _document_xml(body: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body><w:p>{body}</w:p></w:body></w:document>"
    )


def _write_docx(path: Path, body: str) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types/>')
        zf.writestr("word/document.xml", _document_xml(body))


def _unpack(docx: Path) -> Path:
    out = Path(tempfile.mkdtemp())
    with zipfile.ZipFile(docx) as zf:
        zf.extractall(out)
    return out


@unittest.skipUnless(HAVE_VALIDATOR, "lxml/defusedxml not installed")
class RedliningValidatorGuardsTrackChanges(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.original = self.tmp / "original.docx"
        _write_docx(self.original, f"<w:r><w:t>{BASE_PARAGRAPH}</w:t></w:r>")

    def _validate(self, unpacked_dir: Path, author: str = "A") -> bool:
        # The validator prints a human-readable diff on failure; keep the suite quiet.
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return RedliningValidator(str(unpacked_dir), str(self.original), author=author).validate()

    def test_clean_document_passes(self) -> None:
        unpacked = _unpack(self.original)
        self.assertTrue(self._validate(unpacked))

    def test_silent_overwrite_fails(self) -> None:
        """The regression: no revisions by the author must not short-circuit to True."""
        unpacked = _unpack(self.original)
        (unpacked / "word" / "document.xml").write_text(
            _document_xml("<w:r><w:t>Silently overwritten.</w:t></w:r>"),
            encoding="utf-8",
        )
        self.assertFalse(self._validate(unpacked))

    def test_tracked_insertion_passes(self) -> None:
        """A properly tracked edit by the same author must still pass."""
        unpacked = _unpack(self.original)
        (unpacked / "word" / "document.xml").write_text(
            _document_xml(
                f"<w:r><w:t>{BASE_PARAGRAPH}</w:t></w:r>"
                '<w:ins w:id="1" w:author="A" w:date="2026-10-27T00:00:00Z">'
                "<w:r><w:t>Added under track changes.</w:t></w:r></w:ins>"
            ),
            encoding="utf-8",
        )
        self.assertTrue(self._validate(unpacked))
