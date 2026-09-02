# `manuscript-core` — SCI 写作 · 章节润色 · 去 AI · 李瀛语言风格

含原：A 润色 · C 预测模型全文 · D 期刊体例 · L 去 AI · I 引用/清单（写作时）· K 伦理段落 · B.8 实验纲要 · E 通用学术大纲。

## 1.1 何时用

- 起草或重写 Title / Abstract / Intro / Methods / Results / Discussion / Conclusion  
- 润色已有段落；去 AI 腔  
- 影像组学 / habitat / 列线图 / TRIPOD 双集**全文**  
- Radiology Summary/Key Results 或 Nature 家族体例  
- Methods 伦理句、Refs/DOI、CLAIM·TRIPOD 写作自检  
- **实验/机制方案英文纲要**（未完成实验勿写死阳性）  
- **通用学术大纲 / plan / outline**（非影像或跨学科，浓缩自原 E）  

## 1.2 工作流

1. 判定子任务：`polish` | `draft-section` | `full-C` | `venue-D` | `experiment-outline` | `academic-outline`  
2. 确认目标期刊族（Radiology / Nature / Eur Radiol / 其他）→ 格式层  
3. 语气层始终：李瀛全局硬规则（主 SKILL）  
4. **英文 SCI 全文**先打开 `Aitor-format.md`（版式、title page、Methods 顺序、字数/文献配额），再打开下表  
5. 输出统一信封（主 SKILL）  

| 子任务 | 打开 |
|--------|------|
| 润色句/节 | `sentence-templates.md`, `stats-checklist.md`, `merged/radiology-polishing/*` |
| 预测模型全文 | `pipeline-stages.md`, `section-templates.md`, `citation-and-language.md`, `radiomics-reporting.md` |
| Radiology/Nature 骨架 | `merged/radiology-writing/*` |
| 伦理段落 | `merged/radiology-ethics/approval-consent.md` |
| 引用/清单写作自检 | `merged/radiology-citation/*`, `merged/radiology-reporting/guideline-router.md` |
| 口吻校准 | `exemplars.md`（论文相关段） |
| 实验纲要 | 见 §1.9 |
| 通用学术大纲 | `mode-academic-pipeline.md`（plan / outline-only 等） |

## 1.3 润色（原 A）要点

- 节结构：全文以 `Aitor-format.md` 为准；句级润色仍用 `polisher-sections.md`  
- 统计：`stats-checklist.md`；不改正文数字  
- 输出：Polished 全文 + Key changes  
- 期刊 house style：`merged/radiology-polishing/*`  

## 1.4 预测模型全文（原 C，全文默认）

版式与章节顺序：`Aitor-format.md`。  
预测模型叠加：P0 Plan → 双集 Results → LASSO+RadScore → DOI+QC → DOCX（`pipeline-stages.md`）。  

硬约束：开发集拟合 / 验证只评估；患者级划分；主模型 nomogram 双集 AUC/NRI/IDI/DCA；LASSO 表+RadScore；禁破折号；区间用 *to*；Vancouver+DOI。  

## 1.5 期刊体例起草（原 D）

Radiology：structured abstract + Summary statement + Key Results≤3/≤75w。  
Nature 族：见 `nature-family-shape.md`。  
先一句话论证 → topic-sentence chain → 成文。  

## 1.6 去 AI（原 L）

扫并替换：delve, landscape, pivotal, robust, comprehensive, leverage, seamless, throat-clearing, 统一段长, 滥用 em dash。  
改短句、学科词、数字贴断言。  

## 1.7 伦理段落（原 K）

回顾性默认 waiver、批件号留空、title page 伦理句：`Aitor-format.md`。  
更细的同意模型表：`merged/radiology-ethics/approval-consent.md`。  
**填表** → `ethics-application-forms`，不在此改模板。  

## 1.8 引用与清单（原 I，写作时）

- 主张–文献核验；无 DOI 不进表  
- 写 Methods/Results 时对照 guideline-router（CLAIM/TRIPOD+AI/CLEAR…）标缺失  
- **不编造**合规或文献  

预审阶段会用同一套资料再跑审计（`06_review` / `manuscript-quality`）。  

## 1.9 实验/机制方案英文纲要（原 B.8）

```text
1. Introduction (disease → gap → mechanism → prior → aim)
2. Research content and expected result
3. Objectives (To determine whether…)
4. Key issues (model trade-offs)
```

预期用 *might be found / intended to investigate*；**未做实验不写死阳性结果**。

## 1.10 通用学术大纲（原 E）

非影像或用户明确要「大纲/逐步规划」时：  

- 打开 `mode-academic-pipeline.md`  
- 优先 `plan` 或 `outline-only`；全文起草仍服从本 skill 全局铁律（不编造、数字贴断言）  
- 影像预测模型全文仍优先 §1.4（原 C），不用通用 E 替代  

