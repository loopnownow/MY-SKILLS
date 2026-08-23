---
name: paper-writing-review
description: 学术论文写作与审稿。触发词：审稿、评阅、检查报告、Manuscript、论文修改、方法部分、修订、Checklist、投稿、review、peer review。
---

# 学术论文写作与审稿

## 适用场景
- 论文审阅与检查报告生成
- 方法部分（Methods）写作
- 论文修订（tracked changes）
- 投稿格式检查（Checklist）
- 实验流程描述

## 核心工作流

### 1. 论文审阅
```
[Step 1] 读取文稿（Manuscript.docx/pdf）
[Step 2] 对照原始数据核验结果
[Step 3] 检查统计方法、图表、参考文献
[Step 4] 生成详细检查报告（问题+修改建议）
```

### 2. 方法部分写作
```
[Step 1] 阅读实验代码（R/Python/MATLAB）
[Step 2] 掌握数据处理流程
[Step 3] 参考目标期刊格式
[Step 4] 撰写详细方法部分（含参数、统计细节）
```

### 3. 论文修订
- 使用修订方式（tracked changes）修改
- 根据最新结果更新方法/结果
- 补充 CI、统计细节

## 关键规则
1. **对照原始数据**：审稿必须核对数据与结果的一致性
2. **详细报告**：指出具体问题、位置、修改建议
3. **方法完整性**：方法部分需包含所有参数与统计细节，可复现
4. **投稿合规**：遵循目标期刊的格式要求（如 Checklist）
5. **不确定就问**：写作/修订中不明确之处向用户确认

## 附带的模板
- `scripts/review_checklist.md` — 论文审阅检查清单
- `scripts/methods_template.md` — 方法部分写作模板