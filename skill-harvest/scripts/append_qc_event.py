#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append one harvest QC event line (optional governance log; not a gate)."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "skill-harvest" / "data" / "roi-ledger.csv"
EVENTS = ROOT / "skill-harvest" / "data" / "qc-events"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gate", required=True, help="e.g. G-04 / G-FACT")
    p.add_argument("--result", required=True, choices=("pass", "fail", "unknown", "recovered"))
    p.add_argument("--skill", default="", help="responsible skill id or layer")
    p.add_argument("--note", default="")
    args = p.parse_args()

    EVENTS.mkdir(parents=True, exist_ok=True)
    day = date.today().isoformat()
    event_path = EVENTS / f"{day}.csv"
    new_file = not event_path.exists()
    with event_path.open("a", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        if new_file:
            w.writerow(["date", "gate", "result", "skill", "note"])
        w.writerow([day, args.gate, args.result, args.skill, args.note])

    # Optional ROI stub row (empty benefit until user measures).
    if LEDGER.exists() and args.result in {"fail", "recovered"}:
        with LEDGER.open("a", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([day, args.skill or "unknown", "qc", "", args.result, args.note, "", "", "", "", ""])

    print(event_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
