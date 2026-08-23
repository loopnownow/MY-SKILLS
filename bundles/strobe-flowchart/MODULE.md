# strobe-flowchart — SCI 入组/分析流程图

**Owner:** `04_writing` / `ly-figures`. 实验室英文 SCI 全文 **Figure 1** 的唯一画法。  
版式入口仍是 `ly-sci-writing/references/Aitor-format.md`（何时插入、图注左对齐）。本模块只负责 **怎么画、用哪些 n**。

触发：流程图 · STROBE · CONSORT 入组 · 患者筛选图 · Figure 1 flow · 入组图 · enrollment flowchart

不要用 `scientific-schematics` 的 AI 生成来画入组图。

## 视觉模板（0ref）

对照实验室已有图，不要另起风格：

| 来源 | 用什么 |
|------|--------|
| `fyh_CAC/output/0ref/SR_Manuscript.docx` Figure 1 | 白底直角框、黑线、主轴自上而下；排除标准在右、箭头向右分出；底部分训练/验证。**不要画纳入标准框** |
| `fyh_CAC/output/0ref/毕业论文（方雨函）R2.docx` 图Ⅰ-1 | 入组之后再分分析支路（分割/特征 vs 阅片或建模） |
| `ly_SCH_HE/output/0ref/QIANG-肾性脑病Manuscript-有痕.docx` Figure 1 | 入组 + 分析工作流可画在同一张；排除项可带已写出的 n |

默认采用 **SR_Manuscript 框线 + 图Ⅰ-1 的分析支路**：上半 STROBE 入组，下半 imaging → processing → model/stats。

硬样式：白底、黑色 1 pt 直角框、黑色箭头、无阴影、无圆角、无彩色填充。图内无衬线字体（Arial / DejaVu Sans），终图最小约 8 pt。导出 PNG 300 dpi，宽约 16–17 cm。

## 连线（硬规则）

```
[screened]
    |
    |-----> [Exclusion criteria]
    v
[analyzed n]
   / \
[Development]  [Validation]
   \ /
    +---- bar (no arrowhead)
    v
[imaging] -> [processing] -> [model / stats]
```

- **不画 Inclusion criteria 框**，也不画“met inclusion”中间框。
- Development / Validation（或 training / test）**必须**向下接到分析行：两框先落到一条无箭头横杆，再从中点竖直落入第一格分析框。禁止两框悬空。
- 排除框只在右侧，箭头从主轴水平分出。
- 没有 screened *n* 就不要画 screened；没有划分 *n* 就不要画分叉。

## 数字铁律

- 只写正文/表里已经出现的 *n*、排除条文、划分方式。**不画 Inclusion criteria。**
- 筛出总人数 = 已写的 screened − analyzed 时，可以写一笔合计，**不要**按条编造排除人数。
- 没写 screened 就不要画 screened 框，从 analyzed 起笔。
- 没写 train/test 就不要画分叉。
- ADNI / 公开队列：用该队列自己的来源与日期，不要套金山窗口或机型。

## 脚本

项目内（首选）：

```bash
python -m modules.stats.figure_strobe_flow --json spec.json --out output/<endpoint>/PNG/Figure1_flow.png
```

文件：各项目 `modules/stats/figure_strobe_flow.py`（与 `0RAD/0scripts/manuscript/figure_strobe_flow.py` 同文）。  
SCI 全文 **Figure 1 必须是这张流程图**；ROC/列线图从 Figure 2 起编。

技能内副本：`scripts/figure_strobe_flow.py`（`draw_strobe_flow.py` 同文，兼容旧调用）。

`spec.json` 字段：

```json
{
  "screened": "Retrospective review of 375 cases of CAC between 1 August 2024 and 1 August 2026",
  "exclusion": ["Lesion diameter < 1 cm", "Nondiagnostic images"],
  "analyzed": "310 patients included in this study",
  "splits": [
    {"label": "Development set (n = 216)"},
    {"label": "Validation set (n = 94)"}
  ],
  "pipeline": [
    "Multiparametric MRI",
    "Habitat mapping and radiomics extraction",
    "LASSO RadScore, nomogram, and statistical analysis"
  ]
]
```

空字段省略。不要传 `inclusion`。排除最多 6 条；过长句在脚本里折行，不要改数字。

## 插入文稿

1. 作为 **Figure 1**；其后主图 +1。不要改 `Figure S*`。
2. Results 第一段加：`The study flowchart is shown in Figure 1.`
3. 图注左对齐、写清筛选/分析 *n*、划分、分析步骤，并写明未导出的逐条排除人数或外部验证。
4. 图注模板：`Figure 1. Patient enrollment and analysis flowchart. …`

## 不要做

- 不要画 Inclusion criteria / met-inclusion 框
- 不要让 Development / Validation 悬空、不连分析行
- 不要为了“好看”补 screened / 逐条排除 n
- 不要把 ROC/列线图画进这张图
- 不要把伦理号、功效/α 写进框图
