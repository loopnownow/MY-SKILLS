#!/usr/bin/env python3
"""Build spec.html (single file, no external resources) from the spec and config.

Single source of truth:
  * rules, tables, comment example  <- Lab-STE-SPEC.md
  * thresholds, profiles, slots     <- config.yaml
  * latest change notes             <- CHANGELOG.md
Run from anywhere:  python tools/build_spec_html.py
Needs PyYAML:       pip install pyyaml
"""
import html
import re
from pathlib import Path

import yaml

# ---------------- CONFIG ----------------
ROOT = Path(__file__).resolve().parent.parent          # Lab-STE folder
SPEC = ROOT / "Lab-STE-SPEC.md"
CONFIG = ROOT / "config.yaml"
CHANGELOG = ROOT / "CHANGELOG.md"
OUT = ROOT / "spec.html"
PAGE_TITLE = "Lab-STE 可控语言规范"
# Rule groups shown as filter buttons: (key, label, id-prefix tuple)
GROUPS = [("all", "全部", ()), ("en", "英文 EN", ("EN-",)), ("zh", "中文 ZH", ("ZH-",)),
          ("cm", "批注 CM", ("CM-",)), ("ai", "去 AI", ("AI-",))]
# Fields shown on each rule card, in order.
FIELDS = ["语言 / 场景", "检测", "严重度", "正例", "反例", "豁免"]
# Short labels for the ordered process flow (step text, config key shown at right).
FLOW = [
    ("输入文本", "稿件 / 批注 / 大模型回复", ""),
    ("选定档案", "按场景取强度与启用规则", "profiles"),
    ("分段分句，剥离豁免块", "代码、引文、公式、数字+单位", "exemptions"),
    ("术语锁定", "课题表、默认模板、数值、引文标为“不动”", "paths.term_lock*"),
    ("STE 可读性检查", "EN-* / ZH-* / CM-01", "thresholds"),
    ("去 AI 扫描", "AI-L / AI-S / AI-D / AI-F", "thresholds.de_ai"),
    ("冲突裁决", "按固定顺序取舍", "conflict_order"),
    ("改写", "只改允许改的部分", ""),
]
# ---------------- END CONFIG ----------------

E = html.escape


# ---------- small markdown helpers ----------
def inline(s):
    """Escape, then render `code` and **bold**."""
    s = E(s.strip())
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)


def section(text, heading_regex):
    """Text of a '## ' section whose heading matches heading_regex."""
    m = re.search(rf"^##\s+{heading_regex}.*?$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def tables(block):
    """All markdown tables in a block -> list of (header, rows)."""
    out, cur = [], []
    for line in block.splitlines() + [""]:
        if line.strip().startswith("|"):
            cur.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif cur:
            if len(cur) >= 2:
                out.append((cur[0], [r for r in cur[2:]]))
            cur = []
    return out


def table_html(header, rows, cls=""):
    th = "".join(f"<th>{inline(h)}</th>" for h in header)
    body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="scroll"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def parse_rules(text):
    """Return list of dicts: id, title, fields{...}."""
    rules = []
    for m in re.finditer(r"^###\s+([A-Z]+-[A-Z]*\d+)\s+(.+?)$(.*?)(?=^#{2,3}\s|\Z)", text, re.S | re.M):
        rid, title, body = m.group(1), m.group(2).strip(), m.group(3)
        fields = {}
        for fm in re.finditer(r"^-\s+\*\*(.+?)[：:]\*\*\s*(.*?)\s*$", body, re.M):
            fields[fm.group(1).strip()] = fm.group(2).strip()
        if rid == "CM-01":                                # example/counter-example sit below the entry
            fields.setdefault("语言 / 场景", fields.get("语言 / 场景", "zh"))
        rules.append({"id": rid, "title": title, "fields": fields})
    return rules


def meta(text, key):
    m = re.search(rf"\*\*{key}[：:]\*\*\s*(.+?)\s*$", text, re.M)
    return m.group(1).strip() if m else ""


# ---------- SVG builders ----------
def svg_flow():
    w, bx, bw, bh, gap, y0 = 860, 190, 330, 52, 26, 16
    parts, y = [], y0
    n = len(FLOW)
    for i, (title, sub, key) in enumerate(FLOW):
        parts.append(f'<rect class="box" x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="8"/>')
        parts.append(f'<text class="t1" x="{bx + bw / 2}" y="{y + 22}" text-anchor="middle">{i + 1}. {E(title)}</text>')
        parts.append(f'<text class="t2" x="{bx + bw / 2}" y="{y + 40}" text-anchor="middle">{E(sub)}</text>')
        if key:
            parts.append(f'<text class="cfg" x="{bx + bw + 16}" y="{y + 32}">config: {E(key)}</text>')
        parts.append(f'<line class="ar" x1="{bx + bw / 2}" y1="{y + bh}" x2="{bx + bw / 2}" y2="{y + bh + gap}" marker-end="url(#a)"/>')
        y += bh + gap
    # decision diamond: semantic check
    cx, cy, dw, dh = bx + bw / 2, y + 48, 190, 48
    parts.append(f'<polygon class="dec" points="{cx},{cy - dh} {cx + dw},{cy} {cx},{cy + dh} {cx - dw},{cy}"/>')
    parts.append(f'<text class="t1" x="{cx}" y="{cy - 4}" text-anchor="middle">9. 复检：语义保持？</text>')
    parts.append(f'<text class="t2" x="{cx}" y="{cy + 14}" text-anchor="middle">数字、锁定术语、否定词集合不变</text>')
    # loop back to rewrite (step 8)
    rewrite_y = y0 + (n - 1) * (bh + gap) + bh / 2
    lx = cx - dw - 36
    parts.append(f'<path class="ar" d="M{cx - dw},{cy} H{lx} V{rewrite_y} H{bx}" marker-end="url(#a)" fill="none"/>')
    parts.append(f'<text class="no" x="{lx - 6}" y="{cy - 8}" text-anchor="end">否：回到改写</text>')
    parts.append(f'<text class="ok" x="{cx + 10}" y="{cy + dh + 22}">是</text>')
    parts.append(f'<line class="ar" x1="{cx}" y1="{cy + dh}" x2="{cx}" y2="{cy + dh + 30}" marker-end="url(#a)"/>')
    oy = cy + dh + 30
    parts.append(f'<rect class="box out" x="{bx}" y="{oy}" width="{bw}" height="{bh}" rx="8"/>')
    parts.append(f'<text class="t1" x="{cx}" y="{oy + 22}" text-anchor="middle">10. 输出 + 验证指标</text>')
    parts.append(f'<text class="t2" x="{cx}" y="{oy + 40}" text-anchor="middle">句长、术语一致率、命中数、误报率（§11）</text>')
    parts.append(f'<text class="cfg" x="{bx + bw + 16}" y="{oy + 32}">失败即视为冲突层 1–2 失败</text>')
    h = oy + bh + 16
    return svg_wrap(w, h, "".join(parts), "处理流程图")


def svg_conflict(order):
    labels = {"term_lock_and_numerics_and_citations": ("1", "术语锁定、数值、统计量、引文", "不动"),
              "factual_accuracy": ("2", "事实准确性", "不得改变含义、不得增删否定"),
              "ste_readability": ("3", "STE 可读性规则", "句长、语态、一词一义"),
              "de_ai": ("4", "去 AI 规则", "最后取舍")}
    w, y, parts = 860, 14, []
    for i, key in enumerate(order):
        num, name, note = labels.get(key, (str(i + 1), key, ""))
        bw = 560 - i * 70
        parts.append(f'<rect class="box lv{i}" x="40" y="{y}" width="{bw}" height="44" rx="8"/>')
        parts.append(f'<text class="t1" x="58" y="{y + 27}">{num}. {E(name)}</text>')
        parts.append(f'<text class="t2" x="{40 + bw + 14}" y="{y + 27}">{E(note)}</text>')
        y += 56
    parts.append(f'<text class="cfg" x="40" y="{y + 12}">优先级自上而下降低。config: conflict_order；名词重复豁免只对已登记术语生效（term_repeat_exemption）。</text>')
    return svg_wrap(w, y + 28, "".join(parts), "冲突优先级")


def svg_slots(slots, example):
    names = {"location": "位置", "problem": "问题", "basis": "依据", "fix": "修改建议", "severity": "严重度"}
    parts_txt = [p.strip() for p in example.replace("\n", "").split("。") if p.strip()]
    w, parts, x, cw = 860, [], 20, 160
    for i, s in enumerate(slots):
        parts.append(f'<polygon class="box sl{i}" points="{x},12 {x + cw - 14},12 {x + cw},40 {x + cw - 14},68 {x},68 {x + 14},40"/>')
        parts.append(f'<text class="t1" x="{x + cw / 2}" y="46" text-anchor="middle">{i + 1}. {E(names.get(s, s))}</text>')
        txt = parts_txt[i] if i < len(parts_txt) else ""
        parts.append(f'<foreignObject x="{x}" y="78" width="{cw - 10}" height="70"><div xmlns="http://www.w3.org/1999/xhtml" class="slot-ex">{E(txt)}</div></foreignObject>')
        x += cw + 8
    return svg_wrap(w, 150, "".join(parts), "批注五槽")


def svg_dict_flow():
    w = 860
    parts = []
    boxes = [(20, "单词", "box"), (200, "在课题锁定表？", "dec2"), (400, "在默认锁定模板？", "dec2"), (610, "在批准词典？", "dec2")]
    for x, t, c in boxes:
        parts.append(f'<rect class="{c}" x="{x}" y="20" width="160" height="48" rx="8"/>')
        parts.append(f'<text class="t1" x="{x + 80}" y="49" text-anchor="middle">{E(t)}</text>')
    for i, (a, b) in enumerate([(180, 200), (360, 400), (560, 610)]):  # i=0: word -> first test
        parts.append(f'<line class="ar" x1="{a}" y1="44" x2="{b - 2}" y2="44" marker-end="url(#a)"/>')
        if i > 0:                                  # first arrow has no condition
            parts.append(f'<text class="no" x="{(a + b) / 2}" y="36" text-anchor="middle">否</text>')
    parts.append('<text class="ok" x="280" y="98" text-anchor="middle">任一层命中＝已登录</text>')
    parts.append('<line class="ar" x1="690" y1="68" x2="690" y2="108" marker-end="url(#a)"/>')
    parts.append('<text class="no" x="700" y="92">否</text>')
    parts.append('<rect class="box warn" x="520" y="110" width="330" height="52" rx="8"/>')
    parts.append('<text class="t1" x="685" y="132" text-anchor="middle">EN-L01 命中（should_fix）</text>')
    parts.append('<text class="t2" x="685" y="150" text-anchor="middle">改成登录词，或登记进某一层锁定表</text>')
    parts.append('<text class="cfg" x="20" y="150">禁止用专业近义词堆砌覆盖率；批准词典增词需记 CHANGELOG。</text>')
    return svg_wrap(w, 176, "".join(parts), "词汇查找流程")


def svg_wrap(w, h, inner, label):
    defs = ('<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" class="ah"/></marker></defs>')
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(label)}" xmlns="http://www.w3.org/2000/svg">{defs}{inner}</svg>'


# ---------- page parts ----------
def rule_cards(rules):
    out = []
    for r in rules:
        grp = next((k for k, _, pre in GROUPS[1:] if r["id"].startswith(pre)), "other")
        rows = "".join(f"<dt>{E(k)}</dt><dd>{inline(r['fields'][k])}</dd>" for k in FIELDS if k in r["fields"])
        sev = r["fields"].get("严重度", "")
        badge = "must" if "must_fix" in sev else ("should" if "should_fix" in sev else "hint")
        out.append(f'<details class="rule" data-g="{grp}" data-text="{E((r["id"] + r["title"] + " ".join(r["fields"].values())).lower())}">'
                   f'<summary><span class="rid">{E(r["id"])}</span><span class="rt">{E(r["title"])}</span>'
                   f'<span class="bd {badge}">{badge}</span></summary><dl>{rows}</dl></details>')
    return "\n".join(out)


def thresholds_html(cfg):
    out = []
    names = {"en": "英文 en", "zh": "中文 zh", "de_ai": "去 AI de_ai"}
    for grp, items in cfg["thresholds"].items():
        rows = "".join(f"<tr><td><code>{E(k)}</code></td><td>{E(str(v))}</td></tr>" for k, v in items.items())
        out.append(f'<div class="card"><h4>{E(names.get(grp, grp))}</h4><div class="scroll"><table><thead><tr><th>键</th><th>值</th></tr></thead><tbody>{rows}</tbody></table></div></div>')
    return '<div class="grid3">' + "".join(out) + "</div>"


def profiles_html(cfg):
    rows = []
    lvl = {"high": "高", "mid": "中", "low": "低"}
    for name, p in cfg["profiles"].items():
        rules = " ".join(f"<code>{E(x)}</code>" for x in p.get("enable_rules", []))
        skip = " ".join(f"<code>{E(x)}</code>" for x in p.get("skip_rules", []))
        extra = f"<br><small>跳过：{skip}</small>" if skip else ""
        rows.append(f"<tr><td><code>{E(name)}</code></td><td>{'中文' if p['language'] == 'zh' else '英文'}</td>"
                    f"<td>{lvl.get(p['ste'], p['ste'])}</td><td>{lvl.get(p['de_ai'], p['de_ai'])}</td>"
                    f"<td class='rules'>{rules}{extra}</td><td>{E(p.get('notes', ''))}</td></tr>")
    head = "<tr><th>档案</th><th>语言</th><th>STE</th><th>去 AI</th><th>启用规则</th><th>备注</th></tr>"
    return f'<div class="scroll"><table><thead>{head}</thead><tbody>{"".join(rows)}</tbody></table></div>'


def changelog_latest(text):
    m = re.search(r"^##\s+(.+?)$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    if not m:
        return ""
    items = [i[2:].strip() for i in m.group(2).splitlines() if i.startswith("- ")]
    return f"<h4>{E(m.group(1))}</h4><ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"


CSS = """
:root{--bg:#fbfbfa;--fg:#1d2430;--mut:#5c6675;--line:#cfd5de;--box:#ffffff;--card:#ffffff;--acc:#2b6cb0;--ok:#2f855a;--no:#c05621;
--must:#c53030;--should:#b7791f;--hint:#2b6cb0;--lv0:#e6f0fb;--lv1:#eaf6ee;--lv2:#fdf3df;--lv3:#f3e8f7;--code:#eef1f5;--warn:#fff4e5}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14181f;--fg:#e4e8ee;--mut:#9aa5b5;--line:#364050;--box:#1c222c;--card:#1a1f28;--acc:#63a4e8;--ok:#58c08a;--no:#f0a066;
--must:#f07a7a;--should:#e6b457;--hint:#63a4e8;--lv0:#1d2b3d;--lv1:#1b2f26;--lv2:#352c18;--lv3:#2d2236;--code:#252c38;--warn:#3a2c16}}
:root[data-theme=dark]{--bg:#14181f;--fg:#e4e8ee;--mut:#9aa5b5;--line:#364050;--box:#1c222c;--card:#1a1f28;--acc:#63a4e8;--ok:#58c08a;--no:#f0a066;
--must:#f07a7a;--should:#e6b457;--hint:#63a4e8;--lv0:#1d2b3d;--lv1:#1b2f26;--lv2:#352c18;--lv3:#2d2236;--code:#252c38;--warn:#3a2c16}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.7 -apple-system,"PingFang SC","Microsoft YaHei","Noto Sans CJK SC","Segoe UI",sans-serif}
header{padding:28px 20px 12px;max-width:1040px;margin:0 auto}
h1{font-size:26px;margin:0 0 6px}h2{font-size:20px;margin:0 0 12px;padding-top:6px}h4{margin:0 0 8px}
.sub{color:var(--mut);font-size:13px}
nav{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);z-index:5}
nav div{max-width:1040px;margin:0 auto;padding:8px 20px;display:flex;gap:14px;flex-wrap:wrap;align-items:center}
nav a{color:var(--acc);text-decoration:none;font-size:13px}nav button{margin-left:auto}
main{max-width:1040px;margin:0 auto;padding:0 20px 60px}
section{margin:30px 0}
.note{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acc);padding:10px 14px;border-radius:6px}
.scroll{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13.5px;background:var(--card)}
th,td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
th{background:var(--code)}
code{background:var(--code);padding:1px 5px;border-radius:4px;font:12.5px ui-monospace,Menlo,Consolas,monospace}
.diagram{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;overflow-x:auto}
.diagram svg{width:100%;min-width:640px;height:auto;display:block}
.box{fill:var(--box);stroke:var(--line);stroke-width:1.4}.box.out{stroke:var(--ok)}.box.warn{fill:var(--warn);stroke:var(--no)}
.dec{fill:var(--warn);stroke:var(--no);stroke-width:1.4}.dec2{fill:var(--box);stroke:var(--acc);stroke-width:1.4}
.lv0{fill:var(--lv0)}.lv1{fill:var(--lv1)}.lv2{fill:var(--lv2)}.lv3{fill:var(--lv3)}
.sl0{fill:var(--lv0)}.sl1{fill:var(--lv1)}.sl2{fill:var(--lv2)}.sl3{fill:var(--lv3)}.sl4{fill:var(--warn)}
.sl0,.sl1,.sl2,.sl3,.sl4{stroke:var(--line);stroke-width:1.2}
.t1{fill:var(--fg);font-size:14px;font-weight:600}.t2{fill:var(--mut);font-size:12px}
.cfg{fill:var(--mut);font-size:12px;font-family:ui-monospace,Menlo,Consolas,monospace}
.ar{stroke:var(--mut);stroke-width:1.6;fill:none}.ah{fill:var(--mut)}.ok{fill:var(--ok);font-size:12.5px;font-weight:600}.no{fill:var(--no);font-size:12.5px;font-weight:600}
.slot-ex{font-size:12.5px;line-height:1.5;color:var(--fg);padding:2px 4px;word-break:break-all}
.bar{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 12px;align-items:center}
.bar button,nav button{border:1px solid var(--line);background:var(--card);color:var(--fg);padding:4px 12px;border-radius:999px;cursor:pointer;font-size:13px}
.bar button.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.bar input{flex:1;min-width:160px;padding:5px 10px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg)}
details.rule{background:var(--card);border:1px solid var(--line);border-radius:8px;margin:6px 0}
details.rule summary{cursor:pointer;padding:8px 12px;display:flex;gap:10px;align-items:center}
.rid{font:600 13px ui-monospace,Menlo,Consolas,monospace;color:var(--acc);min-width:84px}.rt{flex:1}
.bd{font-size:11.5px;padding:1px 8px;border-radius:999px;border:1px solid currentColor}
.bd.must{color:var(--must)}.bd.should{color:var(--should)}.bd.hint{color:var(--hint)}
details.rule dl{margin:0;padding:4px 14px 12px;display:grid;grid-template-columns:96px 1fr;gap:4px 12px}
details.rule dt{color:var(--mut);font-size:13px}details.rule dd{margin:0}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px}
td.rules code{display:inline-block;margin:1px 2px}small{color:var(--mut)}
footer{max-width:1040px;margin:0 auto;padding:0 20px 40px;color:var(--mut);font-size:12.5px}
@media print{nav,.bar{display:none}details.rule{break-inside:avoid}details.rule dl{display:grid}}
"""

JS = """
(function(){
  var btns=document.querySelectorAll('.bar button[data-g]'),cards=document.querySelectorAll('details.rule'),q=document.getElementById('q'),g='all';
  function run(){var t=(q.value||'').toLowerCase();cards.forEach(function(c){
    var ok=(g==='all'||c.dataset.g===g)&&(!t||c.dataset.text.indexOf(t)>-1);c.style.display=ok?'':'none';});}
  btns.forEach(function(b){b.addEventListener('click',function(){g=b.dataset.g;btns.forEach(function(x){x.classList.toggle('on',x===b)});run();});});
  q.addEventListener('input',run);
  document.getElementById('openall').addEventListener('click',function(){var any=[].some.call(cards,function(c){return c.open;});cards.forEach(function(c){c.open=!any;});});
  var root=document.documentElement,tb=document.getElementById('theme');
  tb.addEventListener('click',function(){var d=root.dataset.theme==='dark'||(!root.dataset.theme&&matchMedia('(prefers-color-scheme: dark)').matches);root.dataset.theme=d?'light':'dark';});
})();
"""


def main():
    spec = SPEC.read_text(encoding="utf-8")
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    log = CHANGELOG.read_text(encoding="utf-8")
    rules = parse_rules(spec)
    version, date = meta(spec, "版本"), meta(spec, "日期")
    if str(cfg.get("version")) != version:
        print(f"WARNING: spec version {version} != config version {cfg.get('version')}")

    # section 7 example (for the five-slot diagram)
    s7 = section(spec, r"7\.")
    ex = re.search(r"\*\*正例：\*\*\s*\n\s*>\s*(.+?)\n", s7)
    example = ex.group(1) if ex else ""
    s9 = section(spec, r"9\.")
    s11 = section(spec, r"11\.")
    s10 = section(spec, r"10\.")
    s10_tables = tables(s10)
    metrics = tables(s11)
    buttons = "".join(f'<button type="button" data-g="{k}"{" class=on" if k == "all" else ""}>{E(l)}</button>' for k, l, _ in GROUPS)

    page = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(PAGE_TITLE)} {E(version)}</title><style>{CSS}</style></head><body>
<header><h1>{E(PAGE_TITLE)}</h1>
<div class="sub">版本 {E(version)} · {E(date)} · 实验室内部规范 · 不是 ASD-STE100 译本或摘录 · 本页由 Lab-STE-SPEC.md 与 config.yaml 生成，请勿手改</div></header>
<nav><div><a href="#flow">流程</a><a href="#profiles">档案</a><a href="#rules">规则</a><a href="#conflict">冲突</a><a href="#comment">批注</a><a href="#dict">词典</a><a href="#thr">阈值</a><a href="#metrics">指标</a><a href="#log">变更</a>
<button id="theme" type="button">深色 / 浅色</button></div></nav>
<main>
<section><div class="note">Lab-STE 管“怎么写得可检测、可改、不改事实”。它不管统计是否做对、文献是否存在、伦理号是否真实。规则正文只写规则，数字全在 <code>config.yaml</code>。</div></section>
<section id="flow"><h2>1. 处理流程</h2><div class="diagram">{svg_flow()}</div></section>
<section id="profiles"><h2>2. 场景档案</h2>{profiles_html(cfg)}
<p class="sub">同一规则集，强度按档案变。本版先落地 <code>manuscript-methods-en</code> 与 <code>review-comment-zh</code>。</p></section>
<section id="rules"><h2>3. 规则速查（{len(rules)} 条）</h2>
<div class="bar">{buttons}<input id="q" type="search" placeholder="搜索规则 ID、关键词" aria-label="搜索规则"><button id="openall" type="button">全部展开 / 收起</button></div>
{rule_cards(rules)}</section>
<section id="conflict"><h2>4. 冲突优先级</h2><div class="diagram">{svg_conflict(cfg["conflict_order"])}</div></section>
<section id="comment"><h2>5. 批注五槽（CM-01）</h2><div class="diagram">{svg_slots(cfg["comment_schema"]["slots"], example)}</div>
<p class="sub">一条批注只写一个问题；建议必须可直接执行；Word 作者字段固定为 <code>{E(str(cfg["comment_schema"]["word_author_field"]))}</code>。</p></section>
<section id="dict"><h2>6. 词典与锁定表</h2>
{"".join(table_html(h, r) for h, r in s10_tables)}
<div class="diagram" style="margin-top:12px">{svg_dict_flow()}</div></section>
<section id="thr"><h2>7. 阈值（来自 config.yaml）</h2>{thresholds_html(cfg)}</section>
<section id="metrics"><h2>8. 验证指标</h2>{"".join(table_html(h, r) for h, r in metrics)}
<p class="sub">没有指标就不能改阈值。语义保持失败视为冲突层 1–2 失败，不得用 STE 或去 AI 分数开脱。</p></section>
<section id="log"><h2>9. 本版变更</h2><div class="card">{changelog_latest(log)}</div></section>
</main>
<footer>Lab-STE {E(version)} · 单文件，无外部资源，可离线查看与存档。</footer>
<script>{JS}</script></body></html>"""
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT} ({len(page) // 1024} KB, {len(rules)} rules)")


if __name__ == "__main__":
    main()
