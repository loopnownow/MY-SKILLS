# -*- coding: utf-8 -*-
"""Published STROBE Figure 1 — patient selection flowchart.

Gold standard: 2023 BJR POLE Fig.1 (type A). Not the 0RAD auto figure.

    python draw_strobe_flow.py --json spec.json --out Figure1_flow.png

White ground, black square boxes, Arial. Vertical spine.
Right inclusion with arrow IN to the spine; right exclusion with arrow OUT
and each reason (n=k). Bottom Training Cohort / Validation Cohort.
No pipeline / analysis row. Never label a split "Development set".

n-audit (fail-closed): exit nonzero if screened − Σ exclusion n ≠ analyzed
or Σ split n ≠ analyzed. Do not invent n. Historical figures that fail
arithmetic may pass --no-audit.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.textpath import TextPath

EDGE = "#000000"
FACE = "#FFFFFF"
LW = 1.05
FS = 8.3
FS_SMALL = 8.0

DEFAULT_SPLIT_LABELS = ("Training Cohort", "Validation Cohort")
DEFAULT_LEGEND = "Figure 1. Flowchart of patient selection and study design."

_N_EQ = re.compile(r"\bn\s*=\s*(\d+)\b", re.I)
_LEADING_COUNT = re.compile(
    r"^\s*(\d+)\s+(?:patients?|subjects?|cases?|women|men)\b", re.I
)


class AuditError(ValueError):
    """n-audit failed; CLI exits nonzero."""


def _font():
    for name in ("Arial", "Calibri", "Helvetica", "DejaVu Sans"):
        try:
            path = font_manager.findfont(name, fallback_to_default=False)
            if not path:
                continue
            if name != "DejaVu Sans" and "DejaVuSans" in path.replace("\\", "/"):
                continue
            return name
        except Exception:
            continue
    return "DejaVu Sans"


FONT = _font()


def _wrap(text: str, width: int) -> str:
    text = " ".join((text or "").split())
    return textwrap.fill(text, width=width, break_long_words=False)


def _line_w(line: str, fs: float) -> float:
    fp = FontProperties(family=FONT, size=fs)
    tp = TextPath((0, 0), line or " ", size=fs, prop=fp)
    return max(0.06, tp.get_extents().width / 72.0)


def _box_wh(text: str, fs: float = FS, pad_x: float = 0.36, pad_y: float = 0.12,
            min_w: float = 1.45, max_w: float = 6.2) -> tuple[float, float]:
    lines = (text or " ").split("\n")
    w = min(max_w, max(min_w, max(_line_w(ln, fs) for ln in lines) + pad_x))
    h = max(0.36, 2 * pad_y + (fs / 72.0) * 1.42 * len(lines))
    return w, h


def _fit(text: str, max_chars: int, fs: float = FS) -> tuple[str, float, float]:
    t = _wrap(text, max_chars) if text else ""
    w, h = _box_wh(t, fs)
    return t, w, h


def parse_n(value) -> int | None:
    """Parse a count. Prefer n=N, then a leading '<N> patients' phrase. Never invent."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, dict):
        if value.get("n") not in (None, ""):
            return parse_n(value.get("n"))
        for key in ("text", "label", "reason", "screened", "analyzed"):
            if key in value:
                found = parse_n(value.get(key))
                if found is not None:
                    return found
        return None
    text = str(value).strip()
    if not text:
        return None
    match = _N_EQ.search(text)
    if match:
        return int(match.group(1))
    match = _LEADING_COUNT.match(text)
    if match:
        return int(match.group(1))
    return None


def _exclusion_items(raw) -> list[tuple[str, int | None]]:
    items = []
    for entry in raw or []:
        if isinstance(entry, dict):
            reason = str(entry.get("reason") or entry.get("text") or "").strip()
            n = parse_n(entry.get("n"))
            if n is None:
                n = parse_n(reason)
            if n is not None and not _N_EQ.search(reason):
                reason = f"{reason} (n={n})" if reason else f"(n={n})"
            items.append((reason, n))
        else:
            text = str(entry).strip()
            items.append((text, parse_n(text)))
    return [(t, n) for t, n in items if t]


def _numbered(title: str, lines: list[str], width: int = 36) -> str:
    out = [title]
    for i, line in enumerate(lines, 1):
        out.append(_wrap(f"{i}. {line}", width))
    return "\n".join(out)


def _normalize_split_label(raw: str, index: int, n_splits: int) -> str:
    label = (raw or "").strip()
    if "development" in label.lower():
        label = "Training Cohort"
    if not label:
        if n_splits == 2 and index < 2:
            return DEFAULT_SPLIT_LABELS[index]
        return f"Cohort {index + 1}"
    return label


def _split_items(raw) -> list[tuple[str, int | None]]:
    entries = list(raw or [])
    n_splits = len(entries)
    items = []
    for i, entry in enumerate(entries):
        if isinstance(entry, dict):
            label = _normalize_split_label(str(entry.get("label") or ""), i, n_splits)
            n = parse_n(entry.get("n"))
            if n is None:
                n = parse_n(entry)
        else:
            text = str(entry).strip()
            n = parse_n(text)
            label = _normalize_split_label(text, i, n_splits)
            if n is not None:
                label = _N_EQ.sub("", label).strip(" ,;:-")
                label = _normalize_split_label(label, i, n_splits)
        display = label
        if n is not None and not _N_EQ.search(display):
            display = f"{display}\n(n={n})"
        items.append((display, n))
    return items


def audit_n(spec: dict) -> None:
    """Fail-closed n-audit. Raises AuditError; does not invent n."""
    screened_n = parse_n(spec.get("screened"))
    analyzed_n = parse_n(spec.get("analyzed"))
    exclusions = _exclusion_items(spec.get("exclusion"))
    splits = _split_items(spec.get("splits"))

    problems = []
    if spec.get("screened") and screened_n is None:
        problems.append("cannot parse n from screened")
    if spec.get("analyzed") and analyzed_n is None:
        problems.append("cannot parse n from analyzed")

    missing_exc = [i + 1 for i, (_, n) in enumerate(exclusions) if n is None]
    if missing_exc:
        problems.append(
            "cannot parse n from exclusion item(s) " + ", ".join(map(str, missing_exc))
        )
    missing_split = [i + 1 for i, (_, n) in enumerate(splits) if n is None]
    if missing_split:
        problems.append(
            "cannot parse n from split item(s) " + ", ".join(map(str, missing_split))
        )

    if problems:
        raise AuditError("n-audit failed: " + "; ".join(problems) + ". Do not invent n.")

    if screened_n is not None and analyzed_n is not None:
        excl_sum = sum(n for _, n in exclusions if n is not None)
        remainder = screened_n - excl_sum
        if remainder != analyzed_n:
            raise AuditError(
                f"n-audit failed: screened ({screened_n}) − Σ exclusion n "
                f"({excl_sum}) = {remainder}, not analyzed ({analyzed_n}). "
                "Do not invent n."
            )

    if splits and analyzed_n is not None:
        split_sum = sum(n for _, n in splits if n is not None)
        if split_sum != analyzed_n:
            raise AuditError(
                f"n-audit failed: Σ splits n ({split_sum}) != analyzed ({analyzed_n}). "
                "Do not invent n."
            )


class Canvas:
    def __init__(self, width=11.0):
        self.width = width
        self.boxes = []
        self.arrows = []
        self.lines = []

    def add_box(self, x, y, w, h, text, weight="normal", align="center", lw=LW, fs=FS):
        self.boxes.append((x, y, w, h, text, weight, align, lw, fs))
        return (x, y, w, h)

    def add_arrow(self, x1, y1, x2, y2):
        self.arrows.append((x1, y1, x2, y2))

    def add_line(self, x1, y1, x2, y2):
        self.lines.append((x1, y1, x2, y2))

    def render(self, out_path: Path):
        if not self.boxes:
            raise ValueError("no boxes to draw")
        max_y = max(y + h for _, y, _, h, *_ in self.boxes) + 0.22
        fig_h = max(5.0, max_y + 0.12)
        fig, ax = plt.subplots(figsize=(self.width, fig_h), dpi=300)
        fig.subplots_adjust(0, 0, 1, 1)
        ax.set_position([0, 0, 1, 1])
        ax.set_xlim(0, self.width)
        ax.set_ylim(fig_h, 0)
        ax.set_aspect("auto")
        ax.axis("off")
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")
        for x, y, w, h, text, weight, align, lw, fs in self.boxes:
            ax.add_patch(
                FancyBboxPatch(
                    (x, y), w, h, boxstyle="square,pad=0",
                    linewidth=lw, edgecolor=EDGE, facecolor=FACE, joinstyle="miter",
                )
            )
            ax.text(
                x + (0.14 if align == "left" else w / 2),
                y + h / 2,
                text,
                ha="left" if align == "left" else "center",
                va="center",
                fontsize=fs,
                fontweight=weight,
                fontfamily=FONT,
                color=EDGE,
                linespacing=1.28,
            )
        for x1, y1, x2, y2 in self.lines:
            ax.add_patch(
                FancyArrowPatch(
                    (x1, y1), (x2, y2), arrowstyle="-", mutation_scale=1,
                    linewidth=1.05, color=EDGE, shrinkA=0, shrinkB=0,
                )
            )
        for x1, y1, x2, y2 in self.arrows:
            ax.add_patch(
                FancyArrowPatch(
                    (x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=11,
                    linewidth=1.05, color=EDGE, shrinkA=0.6, shrinkB=0.6,
                )
            )
        fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white", pad_inches=0.10)
        plt.close(fig)


def draw_strobe_flow(spec: dict, out_path, audit: bool = True) -> Path:
    """Draw a type-A published STROBE patient-selection flowchart."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    spec = dict(spec or {})

    pipeline = spec.get("pipeline")
    if pipeline:
        raise ValueError(
            "spec.pipeline is a type-C methods row and must not be drawn by "
            "draw_strobe_flow; see references/methods-pipeline.md"
        )

    if audit:
        audit_n(spec)

    screened = (spec.get("screened") or "").strip()
    inclusion = [str(x).strip() for x in (spec.get("inclusion") or []) if str(x).strip()]
    excl_items = _exclusion_items(spec.get("exclusion"))
    exclusion_lines = [text for text, _ in excl_items]
    analyzed = (spec.get("analyzed") or "").strip()
    split_items = _split_items(spec.get("splits"))

    if not analyzed and not screened:
        raise ValueError("spec needs at least screened or analyzed text")

    scr_txt, w_scr, h_scr = _fit(screened, 46) if screened else ("", 0.0, 0.0)
    ana_txt, w_ana, h_ana = _fit(analyzed, 46) if analyzed else ("", 0.0, 0.0)
    inc_txt = _numbered("Inclusion criteria:", inclusion, width=36) if inclusion else ""
    exc_txt = _numbered("Exclusion criteria:", exclusion_lines, width=36) if exclusion_lines else ""
    w_inc, h_inc = _box_wh(inc_txt, FS_SMALL, pad_x=0.28, max_w=4.8) if inc_txt else (0.0, 0.0)
    w_exc, h_exc = _box_wh(exc_txt, FS_SMALL, pad_x=0.28, max_w=4.8) if exc_txt else (0.0, 0.0)
    split_fitted = [_fit(t, 28) for t, _ in split_items]

    side_w = max(w_inc, w_exc)
    spine_x = 3.15
    canvas_w = max(11.0, spine_x + 0.55 + side_w + 0.35)
    x_side = spine_x + 0.55
    c = Canvas(width=canvas_w)

    y = 0.18
    last = None

    def place_center(txt, w, h, y0, **kw):
        return c.add_box(spine_x - w / 2, y0, w, h, txt, **kw)

    if scr_txt:
        last = place_center(scr_txt, w_scr, h_scr, y)
        y = y + h_scr

    stem_need = 0.0
    if inc_txt:
        stem_need += h_inc
    if exc_txt:
        stem_need += h_exc
    if inc_txt and exc_txt:
        stem_need += 0.22
    if inc_txt or exc_txt:
        stem_need = max(0.70, stem_need + 0.28)

    if ana_txt:
        if last and (inc_txt or exc_txt):
            ana_y = y + stem_need
            c.add_line(spine_x, y, spine_x, ana_y)
            cursor = y + 0.14
            if inc_txt:
                b_inc = c.add_box(
                    x_side, cursor, w_inc, h_inc, inc_txt, align="left", fs=FS_SMALL,
                )
                join_y = b_inc[1] + b_inc[3] / 2
                # Arrow IN: head on the spine.
                c.add_arrow(b_inc[0], join_y, spine_x, join_y)
                cursor = b_inc[1] + b_inc[3] + 0.22
            if exc_txt:
                b_exc = c.add_box(
                    x_side, cursor, w_exc, h_exc, exc_txt, align="left", fs=FS_SMALL,
                )
                join_y = b_exc[1] + b_exc[3] / 2
                # Arrow OUT: head on the exclusion box.
                c.add_arrow(spine_x, join_y, b_exc[0], join_y)
        elif last:
            ana_y = y + 0.48
            c.add_arrow(spine_x, y, spine_x, ana_y)
        else:
            ana_y = y
            if inc_txt or exc_txt:
                cursor = ana_y
                if inc_txt:
                    b_inc = c.add_box(
                        x_side, cursor, w_inc, h_inc, inc_txt, align="left", fs=FS_SMALL,
                    )
                    join_y = b_inc[1] + min(h_ana, b_inc[3]) / 2
                    c.add_arrow(b_inc[0], join_y, spine_x + w_ana / 2, ana_y + h_ana / 2)
                    cursor = b_inc[1] + b_inc[3] + 0.22
                if exc_txt:
                    b_exc = c.add_box(
                        x_side, cursor, w_exc, h_exc, exc_txt, align="left", fs=FS_SMALL,
                    )
                    c.add_arrow(
                        spine_x + w_ana / 2, ana_y + h_ana / 2,
                        b_exc[0], b_exc[1] + b_exc[3] / 2,
                    )
        last = place_center(ana_txt, w_ana, h_ana, ana_y)
        y = ana_y + h_ana
    elif last and (inc_txt or exc_txt):
        cursor = y + 0.16
        if inc_txt:
            b_inc = c.add_box(x_side, cursor, w_inc, h_inc, inc_txt, align="left", fs=FS_SMALL)
            c.add_arrow(b_inc[0], b_inc[1] + b_inc[3] / 2, last[0] + last[2], last[1] + last[3] / 2)
            cursor = b_inc[1] + b_inc[3] + 0.22
        if exc_txt:
            b_exc = c.add_box(x_side, cursor, w_exc, h_exc, exc_txt, align="left", fs=FS_SMALL)
            c.add_arrow(last[0] + last[2], last[1] + last[3] / 2, b_exc[0], b_exc[1] + b_exc[3] / 2)
            y = max(y, b_exc[1] + b_exc[3])

    if split_fitted and last:
        sg = 0.22
        widths = [w for _, w, _ in split_fitted]
        heights = [h for _, _, h in split_fitted]
        h = max(heights)
        total = sum(widths) + sg * (len(widths) - 1)
        x0 = spine_x - total / 2
        fork_top = y + 0.46
        x_cursor = x0
        for t, w, _h0 in split_fitted:
            c.add_box(x_cursor, fork_top, w, h, t)
            c.add_arrow(spine_x, last[1] + last[3], x_cursor + w / 2, fork_top)
            x_cursor += w + sg

    c.render(out_path)
    return out_path


def default_legend(spec: dict | None = None) -> str:
    del spec
    return DEFAULT_LEGEND


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Draw published STROBE Figure 1 (patient selection; no pipeline row)"
    )
    ap.add_argument("--json", required=True, help="Path to spec JSON")
    ap.add_argument("--out", required=True, help="Output PNG")
    ap.add_argument(
        "--no-audit",
        action="store_true",
        help="Skip n-audit. Only for documented historical figures whose printed n do not add up.",
    )
    args = ap.parse_args(argv)
    spec = json.loads(Path(args.json).read_text(encoding="utf-8"))
    if isinstance(spec, dict) and "spec" in spec and "analyzed" not in spec:
        spec = spec["spec"]
    try:
        print(draw_strobe_flow(spec, args.out, audit=not args.no_audit))
    except AuditError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
