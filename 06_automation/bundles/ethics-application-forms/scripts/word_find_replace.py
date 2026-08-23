# -*- coding: utf-8 -*-
"""Preserve-format find/replace for a single .doc/.docx via Word COM.

Usage:
  python word_find_replace.py <file> <old> <new>
  python word_find_replace.py <file> --map map.json

map.json: {"旧文本": "新文本", ...}
"""
from __future__ import annotations

import json
import os
import sys
import time


def kill_office():
    for name in ("WINWORD.EXE", "wps.exe", "wpscloudsvr.exe"):
        os.system(f"taskkill /F /IM {name} >nul 2>&1")
    time.sleep(1.5)


def replace_all(doc, old: str, new: str) -> bool:
    if not old:
        return False
    if len(old) > 250:
        print("WARN: FindText longer than ~250 may fail:", old[:40], file=sys.stderr)
    find = doc.Content.Find
    find.ClearFormatting()
    find.Replacement.ClearFormatting()
    # positional args required for reliable pywin32 behavior
    return bool(
        find.Execute(old, False, False, False, False, False, True, 1, False, new, 2)
    )


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    path = os.path.abspath(argv[1])
    if not os.path.isfile(path):
        print("File not found:", path, file=sys.stderr)
        return 1

    pairs: list[tuple[str, str]] = []
    if argv[2] == "--map":
        with open(argv[3], encoding="utf-8") as f:
            data = json.load(f)
        pairs = list(data.items())
    else:
        if len(argv) < 4:
            print("Need <old> <new>", file=sys.stderr)
            return 2
        pairs = [(argv[2], argv[3])]

    import pythoncom
    import win32com.client

    kill_office()
    pythoncom.CoInitialize()
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(path, ConfirmConversions=False)
        for old, new in pairs:
            ok = replace_all(doc, old, new)
            print(f"{'OK' if ok else 'NO'}\t{old[:40]!r} -> {new[:40]!r}")
        doc.Save()
        doc.Close()
    finally:
        try:
            word.Quit()
        except Exception:
            pass
        pythoncom.CoUninitialize()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
