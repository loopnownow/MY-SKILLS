# -*- coding: utf-8 -*-
"""Lab SCI Figure 1 — patient/analysis flowchart.

Project entry:
    python -m modules.stats.figure_strobe_flow --json spec.json --out output/PNG/Figure1_flow.png

White ground, black ink only. No Inclusion criteria box.
Development/Validation connect down to the analysis row.
"""
from __future__ import annotations

import argparse
import json
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


def _font():
    for name in ("Arial", "Calibri", "DejaVu Sans", "Helvetica"):
        try:
            path = font_manager.findfont(name, fallback_to_default=False)
            if path and "DejaVuSans.ttf" not in path or name == "DejaVu Sans":
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


def _numbered(title: str, items: list, width: int = 32) -> str:
    lines = [title]
    for i, item in enumerate(items[:6], 1):
        lines.append(_wrap(f"{i}. {item}", width))
    return "\n".join(lines)


class Canvas:
    def __init__(self, width=10.4):
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

    def v_arrow(self, b1, b2):
        self.add_arrow(b1[0] + b1[2] / 2, b1[1] + b1[3], b2[0] + b2[2] / 2, b2[1])

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


def draw_strobe_flow(spec: dict, out_path) -> Path:
    """Draw spec to PNG. Ignores any inclusion field."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    spec = dict(spec or {})
    spec.pop("inclusion", None)
    spec.pop("met_inclusion", None)

    screened = (spec.get("screened") or "").strip()
    exclusion = [str(x).strip() for x in (spec.get("exclusion") or []) if str(x).strip()]
    analyzed = (spec.get("analyzed") or "").strip()
    splits = spec.get("splits") or []
    pipeline = [str(x).strip() for x in (spec.get("pipeline") or []) if str(x).strip()]
    if not analyzed and not screened:
        raise ValueError("spec needs at least screened or analyzed text")

    split_raw = [
        (s.get("label") if isinstance(s, dict) else str(s)).strip() for s in splits[:3]
    ]
    pipe_raw = [str(t).strip() for t in pipeline[:4] if str(t).strip()]
    scr_txt, w_scr, h_scr = _fit(screened, 46) if screened else ("", 0.0, 0.0)
    ana_txt, w_ana, h_ana = _fit(analyzed, 46) if analyzed else ("", 0.0, 0.0)
    exc_txt = _numbered("Exclusion criteria:", exclusion, width=36) if exclusion else ""
    w_exc, h_exc = _box_wh(exc_txt, FS_SMALL, pad_x=0.28, max_w=4.8) if exc_txt else (0.0, 0.0)
    split_fitted = [_fit(t, 28) for t in split_raw]
    pipe_fitted = [_fit(t, 24) for t in pipe_raw]
    split_span = (
        sum(w for _, w, _ in split_fitted) + 0.18 * max(0, len(split_fitted) - 1)
        if split_fitted else 0.0
    )

    c = Canvas()
    spine_x = 2.95
    y = 0.18
    last = None

    def place_center(txt, w, h, y0, **kw):
        return c.add_box(spine_x - w / 2, y0, w, h, txt, **kw)

    if scr_txt:
        last = place_center(scr_txt, w_scr, h_scr, y)
        y = y + h_scr

    if ana_txt:
        if last and exc_txt:
            stem = max(0.58, h_exc + 0.16)
            ana_y = y + stem
            x_exc = max(last[0] + last[2], spine_x + split_span / 2) + 0.40
            b_exc = c.add_box(
                x_exc, y + (stem - h_exc) / 2, w_exc, h_exc, exc_txt,
                align="left", fs=FS_SMALL,
            )
            join_y = b_exc[1] + b_exc[3] / 2
            c.add_line(spine_x, y, spine_x, ana_y)
            c.add_arrow(spine_x, join_y, b_exc[0], join_y)
        elif last:
            ana_y = y + 0.48
            c.add_arrow(spine_x, y, spine_x, ana_y)
        else:
            ana_y = y
        b_ana = place_center(ana_txt, w_ana, h_ana, ana_y)
        if (not last) and exc_txt:
            x_exc = max(b_ana[0] + b_ana[2], spine_x + split_span / 2) + 0.40
            b_exc = c.add_box(
                x_exc, ana_y + max(0.0, (h_ana - h_exc) / 2), w_exc, h_exc,
                exc_txt, align="left", fs=FS_SMALL,
            )
            c.add_arrow(
                b_ana[0] + b_ana[2], b_ana[1] + b_ana[3] / 2,
                b_exc[0], b_exc[1] + b_exc[3] / 2,
            )
        last = b_ana
        y = ana_y + h_ana
    elif last and exc_txt:
        x_exc = last[0] + last[2] + 0.42
        b_exc = c.add_box(x_exc, y + 0.16, w_exc, h_exc, exc_txt, align="left", fs=FS_SMALL)
        c.add_arrow(last[0] + last[2], last[1] + last[3] / 2, b_exc[0], b_exc[1] + b_exc[3] / 2)
        y = max(y, b_exc[1] + b_exc[3])

    split_boxes = []
    if split_fitted and last:
        sg = 0.18
        widths = [w for _, w, _ in split_fitted]
        heights = [h for _, _, h in split_fitted]
        h = max(heights)
        total = sum(widths) + sg * (len(widths) - 1)
        x0 = spine_x - total / 2
        fork_top = y + 0.40
        x_cursor = x0
        for t, w, _h0 in split_fitted:
            sb = c.add_box(x_cursor, fork_top, w, h, t)
            split_boxes.append(sb)
            c.add_arrow(spine_x, last[1] + last[3], x_cursor + w / 2, fork_top)
            x_cursor += w + sg
        last = (x0, fork_top, total, h)
        y = fork_top + h

    if pipe_fitted:
        pg = 0.22
        widths = [w for _, w, _ in pipe_fitted]
        heights = [h for _, _, h in pipe_fitted]
        h = max(heights)
        total = sum(widths) + pg * (len(widths) - 1)
        x0 = max(0.28, (10.2 - total) / 2)
        pipe_y = y + 0.48
        pboxes = []
        x_cursor = x0
        for t, w, _h0 in pipe_fitted:
            pboxes.append(c.add_box(x_cursor, pipe_y, w, h, t))
            x_cursor += w + pg
        target = pboxes[0]
        if split_boxes:
            bar_y = split_boxes[0][1] + split_boxes[0][3] + 0.16
            xs = [sb[0] + sb[2] / 2 for sb in split_boxes]
            for xx in xs:
                c.add_line(xx, split_boxes[0][1] + split_boxes[0][3], xx, bar_y)
            if len(xs) > 1:
                c.add_line(min(xs), bar_y, max(xs), bar_y)
            mid_x = (min(xs) + max(xs)) / 2 if len(xs) > 1 else xs[0]
            hit_x = mid_x if target[0] <= mid_x <= target[0] + target[2] else target[0] + target[2] / 2
            c.add_arrow(mid_x, bar_y, hit_x, pipe_y)
        elif last:
            c.v_arrow(last, target)
        for a, b in zip(pboxes, pboxes[1:]):
            c.add_arrow(a[0] + a[2], a[1] + a[3] / 2, b[0], b[1] + b[3] / 2)

    c.render(out_path)
    return out_path


def default_legend(spec: dict | None = None) -> str:
    spec = spec or {}
    bits = ["Figure 1. Patient enrollment and analysis flowchart."]
    analyzed = (spec.get("analyzed") or "").strip()
    if analyzed:
        bits.append(analyzed.rstrip(".") + ".")
    if spec.get("splits"):
        bits.append("The internal split is the allocation reported in Methods.")
    bits.append("The lower row summarizes imaging, processing, and modelling.")
    bits.append("Per-criterion exclusion counts are shown only when written in the text.")
    bits.append("The figure does not depict an external test cohort.")
    return " ".join(bits)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Draw SCI Figure 1 enrollment/analysis flowchart")
    ap.add_argument("--json", required=True, help="Path to spec JSON")
    ap.add_argument("--out", required=True, help="Output PNG (use PNG/Figure1_flow.png)")
    args = ap.parse_args(argv)
    spec = json.loads(Path(args.json).read_text(encoding="utf-8"))
    if isinstance(spec, dict) and "spec" in spec and "analyzed" not in spec:
        spec = spec["spec"]
    print(draw_strobe_flow(spec, args.out))


if __name__ == "__main__":
    main()
