#!/usr/bin/env python3
"""Detect patient-level leakage across train/validation/test splits."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check whether patient IDs appear in multiple splits.")
    parser.add_argument("csv_path", help="CSV file containing patient and split columns.")
    parser.add_argument("--patient-col", default="patient_id", help="Patient ID column name.")
    parser.add_argument("--split-col", default="split", help="Split column name.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    path = Path(args.csv_path)
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8-sig")))
    if not rows:
        print("No rows found.", file=sys.stderr)
        return 2
    missing = [c for c in [args.patient_col, args.split_col] if c not in rows[0]]
    if missing:
        print(f"Missing column(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    patient_splits: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        patient = str(row.get(args.patient_col, "")).strip()
        split = str(row.get(args.split_col, "")).strip().lower()
        if patient and split:
            patient_splits[patient].add(split)

    leaked = {p: sorted(s) for p, s in patient_splits.items() if len(s) > 1}
    print("# Split Leakage Check")
    print("")
    print(f"- Rows: {len(rows)}")
    print(f"- Patients: {len(patient_splits)}")
    print(f"- Patients in multiple splits: {len(leaked)}")
    print("")
    if leaked:
        print("| Patient | Splits |")
        print("|---|---|")
        for patient, splits in sorted(leaked.items()):
            print(f"| {patient} | {', '.join(splits)} |")
        return 1
    print("No patient-level split leakage detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
