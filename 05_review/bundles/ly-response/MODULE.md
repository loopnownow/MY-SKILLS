# ly-response — 回复审稿人

**职责：** 正式 point-by-point 回复信 + 可定位改动说明。

详规：[`references/mode-3-response.md`](references/mode-3-response.md)  
映射/审计：`merged/radiology-response/*`

**铁律：** 一条对一条；**禁止编造未做实验**；claimed change 必须可定位。

---

## 工作流

1. 给每条意见稳定 ID（R1-1, R2-1…）  
2. 分类：方法 / 统计 / 写作 / 额外实验 / 不同意  
3. 映射：改稿位置 + 英文回复句  
4. 审计：`response-audit-gate.md`  
5. 输出可粘贴信函 + change log  

## 信函骨架

```text
Dear Editors and Reviewers:
Thank you for considering our paper and for the valuable comments. We have carefully revised the manuscript accordingly.

Modifications for Reviewer #X:
#n [optional restatement]
Response: Thank you for the suggestion/inquiry. [What changed]. [Location: p.X / Methods / Table Y].
```

不同意时：先认关切 → 数据/文献 → 尽量仍改表述。

## 输出信封

```text
Skill: ly-response

Letter (paste-ready)
...

Change log
| ID | Type | Action | Location | Status |

Cannot invent (missing experiments)
- ...

Next: ly-sci-writing 润色修改段
```

---

## 触发语

`/ly-response` · 回复审稿人 · response letter · point-by-point · Reviewer  

---

# End of skill
