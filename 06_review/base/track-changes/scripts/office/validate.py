"""
Validate a .docx for tracked changes.

Usage:
    python validate.py <path> --original <original.docx> [--author A] [--auto-repair]

`<path>` is either an unpacked directory or a packed .docx. With `--original` the
redlining check runs: every text difference between the two must be wrapped in a
`w:ins` / `w:del` revision, so a silent overwrite fails. Without `--original` only
the structural checks run (well-formed XML, namespaces, unique IDs, relationship
targets, whitespace preservation, comment markers).

PPTX/XLSX support was removed 2026-10-27 — the lab only redlines Word.

Auto-repair fixes:
- paraId/durableId values that exceed OOXML limits
- Missing xml:space="preserve" on w:t elements with whitespace
"""

import argparse
import sys
import tempfile
import zipfile
from pathlib import Path

from validators import DOCXSchemaValidator, RedliningValidator


def main():
    parser = argparse.ArgumentParser(description="Validate Office document XML files")
    parser.add_argument(
        "path",
        help="Path to unpacked directory or packed .docx",
    )
    parser.add_argument(
        "--original",
        required=False,
        default=None,
        help="Pre-edit original .docx. Without it the redlining check is skipped.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--auto-repair",
        action="store_true",
        help="Automatically repair common issues (hex IDs, whitespace preservation)",
    )
    parser.add_argument(
        "--author",
        default="A",
        help="Author name whose revisions are expected (default: A, the lab author field)",
    )
    args = parser.parse_args()

    path = Path(args.path)
    assert path.exists(), f"Error: {path} does not exist"

    original_file = None
    if args.original:
        original_file = Path(args.original)
        assert original_file.is_file(), f"Error: {original_file} is not a file"
        assert original_file.suffix.lower() == ".docx", (
            f"Error: {original_file} must be a .docx file"
        )

    file_extension = (original_file or path).suffix.lower()
    assert file_extension == ".docx", (
        f"Error: only .docx is supported; got {file_extension or 'no extension'} from {path}"
    )

    if path.is_file() and path.suffix.lower() == ".docx":
        temp_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(path, "r") as zf:
            zf.extractall(temp_dir)
        unpacked_dir = Path(temp_dir)
    else:
        assert path.is_dir(), f"Error: {path} is not a directory or Office file"
        unpacked_dir = path

    match file_extension:
        case ".docx":
            validators = [
                DOCXSchemaValidator(unpacked_dir, original_file, verbose=args.verbose),
            ]
            if original_file:
                validators.append(
                    RedliningValidator(unpacked_dir, original_file, verbose=args.verbose, author=args.author)
                )
        case _:
            print(f"Error: Validation not supported for file type {file_extension}")
            sys.exit(1)

    if args.auto_repair:
        total_repairs = sum(v.repair() for v in validators)
        if total_repairs:
            print(f"Auto-repaired {total_repairs} issue(s)")

    success = all(v.validate() for v in validators)

    if success:
        print("All validations PASSED!")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
