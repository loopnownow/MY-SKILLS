# 模式 3 — 回复审稿人

含原：G 正式 response + B.3 信函骨架。

## 3.1 何时用

- 已有 Reviewer #1/#2 意见，要 point-by-point 回复信  
- 修订说明 + 可贴修改句  

## 3.2 工作流

1. 给每条意见稳定 ID（R1-1, R1-2, R2-1…）  
2. 分类：方法 / 统计 / 写作 / 额外实验 / 不同意  
3. 映射动作：改稿位置 + 英文回复句；**禁止编造未做实验**  
4. 审计：每条 claimed change 可定位（`merged/radiology-response/response-audit-gate.md`）  
5. 动作映射表：`merged/radiology-response/action-mapping.md`  

## 3.3 信函骨架

```text
Dear Editors and Reviewers:
Thank you for considering our paper and for the valuable comments. We have carefully revised the manuscript accordingly.

Modifications for Reviewer #X:
#n [optional restatement of the comment]
Response: Thank you for the suggestion/inquiry. [What we changed]. [Key sentence or location: p.X / Methods / Table Y].
```

一条对一条；不同意时先认关切，再给数据/文献，并尽量仍改表述。

## 3.4 输出格式

```text
Mode: 3 回复审稿人

Letter (paste-ready)

Change log
| ID | Type | Action | Location | Status |

Missing experiments (cannot invent)
- ...

Next: `ly-sci-writing`润色修改段 / `ly-prereview`再预审（可选）
```

