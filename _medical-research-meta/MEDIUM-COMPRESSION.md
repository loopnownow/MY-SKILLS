# Skills 中压方案 — 已执行说明与详细建议

**档位：** B 中压  
**目标：** 可发现 skill 从 ~80 → **7（顶层）**；知识仍在磁盘，按需加载。  
**已执行日期：** 随仓库状态  

---

## 一、已执行的改动

1. **全部嵌套 `SKILL.md` → `MODULE.md`**（约 72 个）  
   - Grok 只注册名为 `SKILL.md` 的包 → 子库不再进入 slash / 自动触发列表。  
2. **删除** `06_automation/bundles/ly-rules`（仅跳转壳）。  
3. **删除重复** `01_research/bundles/citation-management`（与 `ly-literature/bundles/citation-management` 重复）；地图改指 literature 内路径。  
4. **批量改路径引用** `.../SKILL.md` → `.../MODULE.md`（bundles/references 下）。  
5. **顶层 00–06** 补充 progressive disclosure 说明。

**保留可发现：**

| 目录 | name |
|------|------|
| `00_orchestrator` | medical-research-orchestrator |
| `01_research` | medical-research-design-and-evidence |
| `02_analysis` | medical-statistical-and-predictive-analysis |
| `03_imaging` | medical-imaging-and-radiomics |
| `04_writing` | medical-scientific-writing |
| `05_review` | medical-peer-review-and-quality-control |
| `06_automation` | medical-research-automation-and-coding |

验证：`grok inspect` 的 Skills 段应主要显示上述 7 个 user skill（bundled 系统 skill 仍在）。

---

## 二、架构原则（中压后）

```
~/.grok/skills/
  0N_xxx/SKILL.md          ← 唯一发现入口 + 能力地图 + 硬规则
  0N_xxx/bundles/*/MODULE.md  ← 专题细则（按需 read）
  0N_xxx/bundles/*/references|scripts
  0N_xxx/references/
```

| 层级 | 作用 | 是否被自动发现 |
|------|------|----------------|
| 顶层 SKILL.md | 路由、硬规则、能力表 | 是 |
| MODULE.md | 领域深度、库用法、清单 | 否（需显式打开） |
| references/ | 长文、表格、模板 | 否 |
| scripts/ | 可运行代码 | 否 |

Agent 工作流：

1. 由 description 命中 7 选 1（或 orchestrator）。  
2. 读顶层能力地图 → 打开对应 `MODULE.md`。  
3. 再向下打开 `references/` 或跑 `scripts/`。

---

## 三、各顶层 — 推荐加载顺序（详细）

### 00_orchestrator

- **何时用：** 跨文献/影像/统计/写作/审稿/批处理的端到端任务。  
- **不要用：** 单一明确任务（直接 01–06）。  
- **下游：** 只选最小集合；handoff 用 ARCHITECTURE 契约。

### 01_research

| 模式 | 先打开 | 再打开 |
|------|--------|--------|
| 日常查文献 / DOI / Zotero | `bundles/ly-literature/MODULE.md` | paper-lookup / citation-management / radiology-search 子 MODULE |
| 系统综述 / PRISMA | `literature-review/MODULE.md` | ly-literature 作执行后端 |
| PubMed 语法 / E-utilities | `pubmed-database/MODULE.md` | — |
| 课题设计 / 可行性 | `radiology-design/MODULE.md` | `references/radiology/study-design.md` |
| 前沿方向 | `radiology-frontier/MODULE.md` | frontier-patterns 参考文献 |

**建议（未做、可选下一步）：**

- `literature-review` + `pubmed-database` 可再降为 `ly-literature/references/` 附录（轻压 A 已部分重叠）。  
- deep-research 体积大：保持 MODULE，仅系统综述/深度调研时加载。

### 02_analysis

| 模式 | 先打开 | 再打开 |
|------|--------|--------|
| 影像组学/诊断统计默认 | `ly-stats-ml/MODULE.md` → `radiology-stats/MODULE.md` | diagnostic-accuracy, model-evaluation… |
| 写 sklearn/Cox 代码 | 对应 scikit-* / scikit-survival MODULE | — |
| 插补 | `data-impute/MODULE.md` | scripts；export 版 `export_u_impute.py` 仅作对照 |
| 实验室 R pipeline | `scripts/from_skills_export/statistical-modeling/NOTES.md` | pipeline.R / 0_config.R |

**硬规则保持在顶层：** 患者级划分、嵌套特征选择、主指标带 CI、禁止编造数字。

**建议：** 11 个库 MODULE 不必再合并文件；靠「默认 radiology-stats」减少打开次数即可。

### 03_imaging

| 模式 | 先打开 | 再打开 |
|------|--------|--------|
| 组学设计 IBSI | `radiology-radiomics/MODULE.md` | radiomics.md 参考 |
| 写/改 pipeline 代码 | `radiomics-pipeline-toolkit/MODULE.md` | `scripts/from_skills_export/` |
| DICOM/批处理 | `ly-imaging-ops/MODULE.md` | `scripts/from_skills_export/dicom-nifti|file-batch` |
| fMRI | `fMRI-preprocessing/MODULE.md` | MATLAB 脚本 |
| DL 研究设计 | `ly-dl-libs/MODULE.md` → radiology-deep-learning | Lightning/HF 仅实现时 |
| 标注 / 生境基因组 / 转化 / 中英读 | 各 radiology-* MODULE | — |

**建议（可选重压 C 项）：** annotation+radiomics+radiogenomics+translation+reader 合成一个 `imaging-methods/MODULE.md` 多 mode——**中压不必做**，除非仍觉得 03 地图过长。

### 04_writing

| 模式 | 先打开 | 再打开 |
|------|--------|--------|
| 李瀛 SCI 写作/润色 | `ly-sci-writing/MODULE.md` | sentence-templates, pipeline-stages |
| 段落级润色模板 | `ying-li-polisher/MODULE.md` | 与 sci-writing 二选一即可，优先 sci-writing |
| 去 AI 腔 | `stop-slop/MODULE.md` + sci-writing 禁词 | 需要检测报告时再开 ai-writing-detector |
| 期刊图 | `ly-figures/MODULE.md` → radiology-figure | — |
| 读片会 PPT | system `pptx`（`ly-slides` 已于 2026-08-15 迁入 `0del`） | — |

**建议（强烈、可下一迭代）：**

1. **写作单一真源：** 以 `ly-sci-writing` 为准；`ying-li-polisher` 降为 `references/polisher-sections.md`（减双入口）。  
2. **de-AI 合一：** stop-slop + ai-writing-detector → `references/de-ai/`，顶层写 5 条硬规则即可。  
3. 当前中压已去掉发现噪音；内容合并可另开一次「写作去重」任务。

### 05_review

| 模式 | 先打开 | 再打开 |
|------|--------|--------|
| 自己稿预审 | `ly-prereview/MODULE.md` | review_checklist_export, radiology pre-sub |
| 审别人 | ly-prereview path B + `peer-review/MODULE.md` 作结构参考 | — |
| 回审信 | `ly-response/MODULE.md` | — |

**建议：** peer-review 长文保留 MODULE；预审 dealbreaker 永远优先于语法。

### 06_automation

| 模式 | 先打开 | 再打开 |
|------|--------|--------|
| 写 lab 脚本 | `code-refactoring/MODULE.md` + soft_code_template.py | — |
| 出院小结/检验 | `clinical-data-extraction/MODULE.md` | scripts |
| 环境/CUDA | `tool-environment-setup/MODULE.md` | cuda_install.md |
| Word/PDF/Excel | docx / pdf / xlsx MODULE | 按扩展名 |
| 伦理表 | ethics-application-forms | 保模板不改结构 |
| 死磕 debug | pua（可选，非默认） | pua-loop |

**建议：** docx+pdf+xlsx+markitdown 可远期合成 `office-io/MODULE.md`；中压阶段保持分文件即可。

---

## 四、仍建议的后续压缩（未自动执行）

按收益排序：

| 优先级 | 项 | 收益 | 风险 |
|--------|-----|------|------|
| P1 | 写作：polisher+stop-slop+ai-detector 并入 sci-writing references | 减双标准、减 token | 需一次对照合并禁词表 |
| P2 | 文献：literature-review/pubmed 收进 ly-literature/references | 01 地图更短 | 系统综述模板要改路径 |
| P3 | 03：五个 radiology-* 合成 imaging-methods 多 mode | 地图更短 | 大文件难维护 |
| P4 | 06：office 四合一 | 略 | 触发描述变模糊 |
| P5 | 移出 pua 到 `~/.grok/skills-optional` 或 disabled | 减无关触发 | 调试习惯依赖时不便 |
| P6 | 删除 MODULE 内 YAML `name:`（可选） | 防止未来若扫描扩展 | 无功能必要 |

**不建议：**

- 合并 7 顶层；  
- 删除 radiology-stats / ly-sci-writing 等内容本体；  
- 为省磁盘删 scripts（体积小、实战价值高）。

---

## 五、使用约定（给 Agent / 给人）

1. **禁止**再为疾病、软件包、论文章节新建顶层 skill。  
2. 新知识优先：`references/*.md` 或现有 `MODULE.md` 增 mode。  
3. 只有反复「顶层描述塞不下、路由总错」时才考虑第 8 个顶层 skill。  
4. 改 MODULE 后无需清缓存；新会话 / `grok inspect` 即可看到 7 入口。  
5. 若某子能力必须 slash 直达：单独拷到顶层短 skill（极少用），不要恢复整树 SKILL.md。

---

## 六、回滚

- 备份 zip：`D:\MedicalResearch-Skills-v1.1.0-integrated.zip`（中压前一代）。  
- 或把所有 `MODULE.md` 批量改回 `SKILL.md`（会恢复高噪音发现）。

```text
# 回滚发现面（不推荐）
Get-ChildItem ~/.grok/skills -Recurse -Filter MODULE.md |
  Where-Object { $_.Directory.Name -notmatch '00_|01_|...' } |
  Rename-Item -NewName SKILL.md
```

更稳妥：从 zip 恢复整树。

---

## 七、验收清单

- [ ] `grok inspect` user skills ≈ 7（+ 系统 bundled）  
- [ ] 润色任务命中 `04_writing` 而非 ying-li-polisher  
- [ ] AUC/DeLong 命中 `02_analysis`  
- [ ] 软编码/dry-run 命中 `06_automation` → code-refactoring MODULE  
- [ ] 嵌套路径 `MODULE.md` 可被 read_file 打开  
- [ ] 无 `bundles/ly-rules`、无双份 citation-management 顶层包  

---

# End

## P1 writing merge DONE

- `ying-li-polisher` → `04_writing/bundles/ly-sci-writing/references/polisher-sections.md`
- `stop-slop` + `ai-writing-detector` → `.../references/de-ai/`
- Single writing source: `ly-sci-writing/MODULE.md`
- Removed bundles: ying-li-polisher, stop-slop, ai-writing-detector


## P2–P6 execution log

| Item | Decision | Result |
|------|----------|--------|
| P2 | 收进 references | literature-review → `ly-literature/references/systematic-literature-review/`; pubmed → `.../pubmed-database/` |
| P3 | imaging-methods 多 mode | 五个 radiology-* → `03_imaging/bundles/imaging-methods/modes/*` |
| P4 | 跳过 | office 四分包保持 |
| P5 | 移出技能树 | pua → `~/.grok/skills-optional/pua/`（2026-08-15 再迁到 `D:\0Grok\0RAD\0del\skills-optional_pua`） |
| P6 | 剥 frontmatter | 全部 `MODULE.md` 去掉 YAML name/description |

