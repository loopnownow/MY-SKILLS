# -*- coding: utf-8 -*-
"""Expanded STROBE Figure 1 — pre-split cohorts, optional downsample, then analyzed.

Type A' of draw-flowchart. Same house style as ``draw_strobe_flow`` (white ground,
black square boxes, Arial, arrows on a spine) but the cohort arithmetic is one level
deeper:

    screened -> [pre-split arm 1] -> (downsample) -> [final cohort 1] -+
              -> [pre-split arm 2] ----------------> [final cohort 2] -+-> analyzed

    python draw_strobe_flow_expanded.py --json spec.json --out Figure1_flow.pdf

Group constants (texts, n) live in the project's own ``ref/*.json``; this script
carries none. Spec keys: see ``references/expanded-strobe.md``.

n-audit is fail-closed (exit nonzero, no guessing):
  * arm.n != arm.pp + arm.non_pp
  * arm.n - downsample.n != cohort.n            (arms that carry a downsample)
  * cohort.n != cohort.pp + cohort.non_pp
  * screened n != sum of arm n
  * sum of cohort n != analyzed n
  * sum of cohort pp / non_pp != sum of arm pp / non_pp   (when given)

``--no-audit`` is only for documented historical figures whose printed n do not add up.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from draw_strobe_flow import (
    AuditError,
    Canvas,
    FS,
    _box_wh,
    _fit,
    _numbered,
    _wrap,
    parse_n,
)

# -- CONFIG -------------------------------------------------------------------
LAYOUT_KEY = "expanded-split-downsample"
DEFAULT_ANALYZED_LABEL = "Analyzed"
COL_GAP = 0.34
FORK_DROP = 0.46
STEM_MIN = 0.70
POS_NAME_FALLBACK = "positive"
TEXT_WIDTH = 30


# -- spec parsing -------------------------------------------------------------
def _arms(raw) -> list[dict]:
    if isinstance(raw, dict):
        items = []
        for key, val in raw.items():
            entry = dict(val or {})
            entry.setdefault("label", key.replace("_", " ").title())
            items.append(entry)
        return items
    return [dict(entry or {}) for entry in (raw or [])]


def _num(entry: dict, key: str) -> int | None:
    for field in (key, f"{key}_n"):
        if field in entry:
            got = parse_n(entry.get(field))
            if got is not None:
                return got
    return None


def _downsample_map(raw, arms: list[dict]) -> dict[int, dict]:
    entries = raw if isinstance(raw, list) else ([raw] if raw else [])
    out: dict[int, dict] = {}
    for entry in entries:
        entry = dict(entry or {})
        target = entry.get("arm")
        index = 0
        if isinstance(target, int) and not isinstance(target, bool):
            index = target
        elif isinstance(target, str):
            labels = [str(a.get("label") or "") for a in arms]
            index = labels.index(target) if target in labels else 0
        if not 0 <= index < len(arms):
            raise ValueError(f"downsample.arm {target!r} out of range")
        klass = str(entry.get("class") or "non_pp")
        if klass not in ("pp", "non_pp"):
            raise ValueError(
                f"downsample.class {klass!r} must be 'pp' or 'non_pp' (default non_pp)"
            )
        entry["class"] = klass
        out[index] = entry
    return out


def _resolve(spec: dict) -> dict:
    layout = spec.get("layout")
    if layout and layout != LAYOUT_KEY:
        raise ValueError(
            f"spec.layout={layout!r} is not {LAYOUT_KEY!r}; use draw_strobe_flow for type A"
        )
    if spec.get("pipeline"):
        raise ValueError(
            "spec.pipeline is a type-C methods row and must not be drawn here; "
            "see references/methods-pipeline.md"
        )

    arms = _arms(spec.get("presplit") or spec.get("arms"))
    if not arms:
        raise ValueError("spec needs at least one pre-split arm (presplit/arms)")
    for arm in arms:
        arm["_n"] = _num(arm, "n")
        arm["_pp"] = _num(arm, "pp")
        arm["_non"] = _num(arm, "non_pp")

    cohorts = _arms(spec.get("splits") or spec.get("cohorts"))
    if not cohorts:
        raise ValueError("spec needs final cohorts (splits/cohorts)")
    if len(cohorts) != len(arms):
        raise ValueError(
            f"{len(arms)} pre-split arm(s) vs {len(cohorts)} final cohort(s); "
            "pairing is by index — fix the spec"
        )
    for cohort in cohorts:
        cohort["_n"] = _num(cohort, "n")
        cohort["_pp"] = _num(cohort, "pp")
        cohort["_non"] = _num(cohort, "non_pp")

    return {
        "screened": (spec.get("screened") or "").strip(),
        "screened_n": parse_n(spec.get("screened")),
        "inclusion": [
            str(x).strip() for x in (spec.get("inclusion") or []) if str(x).strip()
        ],
        "arms": arms,
        "cohorts": cohorts,
        "downsample": _downsample_map(spec.get("downsample"), arms),
        "analyzed": (spec.get("analyzed") or "").strip(),
        "analyzed_n": parse_n(spec.get("analyzed")),
        "pos_name": (spec.get("pos_name") or POS_NAME_FALLBACK).strip(),
        "font_size": float(spec.get("font_size") or FS),
    }


# -- n-audit ------------------------------------------------------------------
def audit(spec: dict) -> None:
    """Fail-closed arithmetic check across screened -> arms -> downsample -> cohorts."""
    arms = spec["arms"]
    cohorts = spec["cohorts"]
    downs = spec["downsample"]
    problems: list[str] = []

    for i, arm in enumerate(arms, 1):
        label = arm.get("label") or f"arm {i}"
        if arm["_n"] is None:
            problems.append(f"{label}: cannot parse n")
            continue
        if arm["_pp"] is not None and arm["_non"] is not None:
            if arm["_n"] != arm["_pp"] + arm["_non"]:
                problems.append(
                    f"{label}: n ({arm['_n']}) != pp ({arm['_pp']}) "
                    f"+ non_pp ({arm['_non']})"
                )

        down = downs.get(i - 1)
        cohort = cohorts[i - 1]
        if cohort["_n"] is None:
            problems.append(f"{label}: final cohort n unparseable")
            continue
        if down is not None:
            dropped = parse_n(down.get("n"))
            if dropped is None:
                problems.append(f"{label}: cannot parse downsample n")
            elif arm["_n"] - dropped != cohort["_n"]:
                problems.append(
                    f"{label}: arm n ({arm['_n']}) - downsample n ({dropped}) "
                    f"= {arm['_n'] - dropped}, not cohort n ({cohort['_n']})"
                )
        elif arm["_n"] != cohort["_n"]:
            problems.append(
                f"{label}: arm n ({arm['_n']}) != cohort n ({cohort['_n']}) "
                "with no downsample"
            )

    for i, cohort in enumerate(cohorts, 1):
        label = cohort.get("label") or f"cohort {i}"
        if cohort["_n"] is None:
            continue
        if cohort["_pp"] is not None and cohort["_non"] is not None:
            if cohort["_n"] != cohort["_pp"] + cohort["_non"]:
                problems.append(
                    f"{label}: n ({cohort['_n']}) != pp ({cohort['_pp']}) "
                    f"+ non_pp ({cohort['_non']})"
                )

    arm_ns = [a["_n"] for a in arms]
    if spec["screened_n"] is not None and None not in arm_ns:
        arm_total = sum(arm_ns)
        if spec["screened_n"] != arm_total:
            problems.append(
                f"screened n ({spec['screened_n']}) != sum of pre-split arm n ({arm_total})"
            )

    cohort_ns = [c["_n"] for c in cohorts]
    if spec["analyzed_n"] is not None and None not in cohort_ns:
        cohort_total = sum(cohort_ns)
        if cohort_total != spec["analyzed_n"]:
            problems.append(
                f"sum of final cohort n ({cohort_total}) != analyzed n "
                f"({spec['analyzed_n']})"
            )

    pos_arms = [a["_pp"] for a in arms]
    pos_cohorts = [c["_pp"] for c in cohorts]
    if None not in pos_arms and None not in pos_cohorts:
        dropped_pos = sum(
            parse_n(d.get("n")) or 0
            for d in downs.values()
            if str(d.get("class") or "non_pp") == "pp"
        )
        if sum(pos_cohorts) != sum(pos_arms) - dropped_pos:
            problems.append(
                f"sum of cohort pp ({sum(pos_cohorts)}) != sum of arm pp "
                f"({sum(pos_arms)}) - downsampled pp ({dropped_pos})"
            )
    neg_arms = [a["_non"] for a in arms]
    neg_cohorts = [c["_non"] for c in cohorts]
    if None not in neg_arms and None not in neg_cohorts:
        dropped_neg = sum(
            parse_n(d.get("n")) or 0
            for d in downs.values()
            if str(d.get("class") or "non_pp") != "pp"
        )
        if sum(neg_cohorts) != sum(neg_arms) - dropped_neg:
            problems.append(
                f"sum of cohort non_pp ({sum(neg_cohorts)}) != sum of arm non_pp "
                f"({sum(neg_arms)}) - downsampled non_pp ({dropped_neg})"
            )

    if problems:
        raise AuditError("n-audit failed — do not invent n:\n  " + "\n  ".join(problems))


# -- text builders ------------------------------------------------------------
def _arm_text(arm: dict, pos_name: str) -> str:
    if arm.get("text"):
        return str(arm["text"]).strip()
    lines = [f"{arm.get('label') or 'Cohort'} (n = {arm['_n']})"]
    if arm["_pp"] is not None and arm["_non"] is not None:
        lines.append(f"{arm['_pp']} labeled {pos_name};")
        lines.append(f"{arm['_non']} without")
    note = str(arm.get("note") or "").strip()
    if note:
        lines.append(note)
    return "\n".join(lines)


def _cohort_text(cohort: dict, pos_name: str) -> str:
    if cohort.get("text"):
        return str(cohort["text"]).strip()
    lines = [f"{cohort.get('label') or 'Cohort'} (n = {cohort['_n']})"]
    if cohort["_pp"] is not None and cohort["_non"] is not None:
        lines.append(f"{cohort['_pp']} labeled {pos_name};")
        lines.append(f"{cohort['_non']} without")
    return "\n".join(lines)


def _downsample_text(down: dict) -> str:
    if down.get("text"):
        return str(down["text"]).strip()
    reason = str(down.get("reason") or "Downsampled for class imbalance").strip()
    return f"{reason}\n(n = {parse_n(down.get('n'))})"


# -- draw ---------------------------------------------------------------------
def draw_expanded_strobe(spec: dict, out_path, audit_n: bool = True) -> Path:
    """Draw a type-A' expanded STROBE patient-selection flowchart."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    resolved = _resolve(dict(spec or {}))
    if audit_n:
        audit(resolved)

    fs = resolved["font_size"]
    fs_side = max(1.0, fs - 0.3)
    pos_name = resolved["pos_name"]
    arms = resolved["arms"]
    cohorts = resolved["cohorts"]
    downs = resolved["downsample"]

    arm_txt = [_wrap(_arm_text(a, pos_name), TEXT_WIDTH) for a in arms]
    coh_txt = [_wrap(_cohort_text(c, pos_name), TEXT_WIDTH) for c in cohorts]
    ds_raw = [downs.get(i) for i in range(len(arms))]
    ds_txt = [_wrap(_downsample_text(d), TEXT_WIDTH) if d is not None else "" for d in ds_raw]

    arm_wh = [_box_wh(t, fs, max_w=3.6) for t in arm_txt]
    coh_wh = [_box_wh(t, fs, max_w=3.6) for t in coh_txt]
    ds_wh = [_box_wh(t, fs, max_w=3.6) if t else (0.0, 0.0) for t in ds_txt]

    col_w = [
        max(arm_wh[i][0], coh_wh[i][0], ds_wh[i][0]) for i in range(len(arms))
    ]
    col_total = sum(col_w) + COL_GAP * (len(arms) - 1)
    col_left = [0.0]
    for w in col_w[:-1]:
        col_left.append(col_left[-1] + w + COL_GAP)

    inc_txt = (
        _numbered("Inclusion criteria:", resolved["inclusion"], width=36)
        if resolved["inclusion"]
        else ""
    )
    w_inc, h_inc = (
        _box_wh(inc_txt, fs_side, pad_x=0.28, max_w=4.8) if inc_txt else (0.0, 0.0)
    )

    spine_x = max(3.15, col_total / 2 + 0.40)
    canvas_w = max(11.0, spine_x + 0.55 + w_inc + 0.35)
    offset_x = spine_x - col_total / 2

    if resolved["screened"]:
        screened_txt, w_scr, h_scr = _fit(resolved["screened"], 46, fs)
    else:
        screened_txt, w_scr, h_scr = "", 0.0, 0.0
    analyzed_txt, w_ana, h_ana = _fit(
        resolved["analyzed"] or DEFAULT_ANALYZED_LABEL, 46, fs
    )

    c = Canvas(width=canvas_w)
    y = 0.18
    if screened_txt:
        c.add_box(spine_x - w_scr / 2, y, w_scr, h_scr, screened_txt, fs=fs)
        y += h_scr

    stem_end = y + max(STEM_MIN, (h_inc + 0.28) if inc_txt else STEM_MIN)
    c.add_line(spine_x, y, spine_x, stem_end)
    if inc_txt:
        b_inc = c.add_box(
            spine_x + 0.55, y + 0.14, w_inc, h_inc, inc_txt, align="left", fs=fs_side
        )
        join_y = b_inc[1] + b_inc[3] / 2
        c.add_arrow(b_inc[0], join_y, spine_x, join_y)

    arm_y = stem_end + 0.16
    arm_h = max(h for _, h in arm_wh)
    for i in range(len(arms)):
        x = offset_x + col_left[i]
        cx = x + col_w[i] / 2
        c.add_box(x, arm_y, col_w[i], arm_h, arm_txt[i], fs=fs)
        c.add_arrow(spine_x, stem_end, cx, arm_y)

    cursor = arm_y + arm_h
    ds_bottom = list(range(len(arms)))
    for i in range(len(arms)):
        x = offset_x + col_left[i]
        cx = x + col_w[i] / 2
        if ds_txt[i]:
            ds_y = cursor + 0.26
            c.add_arrow(cx, cursor, cx, ds_y)
            c.add_box(x, ds_y, col_w[i], ds_wh[i][1], ds_txt[i], fs=fs)
            ds_bottom[i] = ds_y + ds_wh[i][1]
        else:
            ds_bottom[i] = cursor
    cursor = max(ds_bottom)

    coh_y = cursor + 0.30
    coh_h = max(h for _, h in coh_wh)
    for i in range(len(cohorts)):
        x = offset_x + col_left[i]
        cx = x + col_w[i] / 2
        c.add_box(x, coh_y, col_w[i], coh_h, coh_txt[i], fs=fs)
        c.add_arrow(cx, ds_bottom[i], cx, coh_y)

    fork_y = coh_y + coh_h + FORK_DROP
    cx_list = [offset_x + col_left[i] + col_w[i] / 2 for i in range(len(cohorts))]
    for cx in cx_list:
        c.add_line(cx, coh_y + coh_h, cx, fork_y)
    if len(cx_list) > 1:
        c.add_line(min(cx_list), fork_y, max(cx_list), fork_y)
    ana_y = fork_y + 0.28
    c.add_arrow(spine_x, fork_y, spine_x, ana_y)
    c.add_box(spine_x - w_ana / 2, ana_y, w_ana, h_ana, analyzed_txt, fs=fs)

    c.render(out_path)
    return out_path


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Draw an expanded STROBE Figure 1 (pre-split arms + optional downsample)"
    )
    ap.add_argument("--json", required=True, help="Path to spec JSON")
    ap.add_argument("--out", required=True, help="Output PDF (preferred) or PNG")
    ap.add_argument(
        "--no-audit",
        action="store_true",
        help="Skip n-audit. Only for documented historical figures whose printed n "
        "do not add up.",
    )
    args = ap.parse_args(argv)
    spec = json.loads(Path(args.json).read_text(encoding="utf-8"))
    if isinstance(spec, dict) and "spec" in spec and "presplit" not in spec:
        spec = spec["spec"]
    try:
        print(draw_expanded_strobe(spec, args.out, audit_n=not args.no_audit))
    except AuditError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
