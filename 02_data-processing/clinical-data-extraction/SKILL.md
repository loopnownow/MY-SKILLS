---
name: clinical-data-extraction
description: >
  Extract clinical data from txt/docx, labs, and pathology text already exported
  off the hospital machine. Use for 提取检验, 病理全文, 临床数据提取, 出院小结抽取.
  Dash/阴性 = Negative, not missing. Do not invent labs.
  HIS login clients stay on the hospital machine, never in git.
---

# 临床数据提取

个人数据提取补充，家园在 `02_data-processing/clinical-data-extraction/`（从 archive 迁入；脚本在 `scripts/`，深度 skill/pack/scripts/file）。

## 适用场景
- 从 .txt / .docx 提取患者信息（姓名、性别、年龄、门诊号）
- 提取检验指标（血常规、肝功能、肾功能、血糖血脂、肿瘤指标等）
- 出院小结、入院记录内容抽取
- 临床数据合并、去重、格式化

HIS / PACS 登录与查询客户端只在医院机器上运行，**不得进入本仓库**。本技能只处理已经导出到本地的文本/文档。

## 核心工作流

### 1. 文本/文档提取
```
[Step 1] 遍历目录下所有 .txt / .docx 文件
[Step 2] 用 LAB_DICT 关键词字典匹配指标
[Step 3] 提取患者基本信息与检验结果
[Step 4] 去除单位，列名使用英文全称+缩写+(单位)
[Step 5] 输出 CSV / Excel
```

### 2. HIS 客户端（不在 A）

HIS login automation must not live in A. Hospital-system clients stay on the hospital machine and are never committed to git. Do not add Selenium/HIS URLs, usernames, or passwords here. Feed this skill exported txt/docx/CSV only.

## 关键规则
1. **LAB_DICT 字典**：所有检验指标关键词集中管理，便于增删
2. **软编码**：路径、关键词、输出文件作为顶层配置
3. **单位处理**：单位从数据中去除，放入列名
4. **断点续传**：查询/提取中断后可从上次位置继续
5. **最大程度提取**：优先完整提取，遗漏信息向用户报告并让其决策
6. **去重合并**：相同患者数据合并，重复内容只录一次
7. **免疫组化**：从病理**全文**抽（`指标（结果）`）。结构化 `病理_ER` 等列若过工作区缺失阈值（见 `../0rad-workspace.md`），不要整列写入，改从全文解析。
8. **阴性不是缺失**：括号里的 `-` / `－` / `—` / `阴性` 编码为 `Negative`，不得当空值丢掉。
9. **标记名完整匹配**：`ER` 不得命中 `HER2`；在标记名前要求非字母（或词界）。`P16` 的斑驳/斑片单独记 `Mosaic`，不要并进 `Positive`。
10. 分类标签用英文（`Positive`/`Negative`），规则见 `../0rad-workspace.md`，此处不另写一套。

## 附带的脚本
- `scripts/extract_patient_data.py` — 患者信息与检验指标提取
- `scripts/extract_docx.py` — docx 文档批量提取
