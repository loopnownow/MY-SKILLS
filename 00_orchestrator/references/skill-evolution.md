# Skill evolution (propose only)

Applies to skills 00–07. Never edit live skill bodies directly; post-merge deploy sync is the only write path (Rules `skills.md` §1b).

**Harvest 任务流程**（本文件 §「Harvest 任务流程」）由 **00_orchestrator** 管理；收集口径 SSOT 见 `_corpus/skill-harvest/HARVEST-STANDARD.md`（收集标准）。**不**新增顶层 evolution skill / evolution agent / 第 5 知识库。

## Evidence

- Default evidence level **E4** = the same class of user correction repeated. A single event never evolves a skill.
- Priority: user edits the deliverable 高于 explicit correction 高于 named issue 高于 observation 高于 self-review.

## Keep or skip

- Keep only if ALL: repeated or locked; used in a future project; methodology / naming / layout / validation / hygiene (not n / AUC / ethics IDs); no other SSOT.
- Skip: one-off path; SSOT duplicate; vendor production script; long human profile (pointer only); taste; single-project numbers or IDs.
- Absorb external packs into an existing layer. Do not open a new top level for a disease, organ, package, section, statistical test, metric, or modality. One authority home per topic.

## Budget and outcome

- Budget: at most 1 core behaviour change, at most 3 new rules, no duplicates, no unapproved boundary expansion.
- Each proposal answers: what recurrence it prevents; how effectiveness will be known.
- Outcome: keep / revise / rollback / merge·simplify / archive / delete (delete needs explicit approval).
- Rollback restores a recorded git point; do not stack a second evolution on a regression.

---

## Harvest 任务流程（00 管理）

Owner（2026-10-24）：harvest 同样更新任务流程，由 skill-00 管理，并做成收集标准。

**层级（保持，不另开树）**

| 层 | 含义 | 物理落点 |
|---|---|---|
| Rules (R) | 跨技能硬契约 | MY-RULES |
| Skills (S) | 00–07 技能正文 / personal | MY-SKILLS |
| Registry (Reg) | fine-ID / mount 登记 | `01_skill-integration/registry.yaml` 等 |
| Capabilities (Cap) | 可挂载能力包 | MY-SKILLS `NN_slug/base/` + registry（**无**单独 capabilities 克隆） |
| Corpus | 语料 / harvest 草稿 | `D:\0Grok\0doc\_corpus\skill-harvest\`（SSOT）；`D:\0del` = 工作副本 |

**硬门**

- **Extract ≠ promote**：抽取只写 corpus / candidate；**「进skills」** 才允许改 runtime。
- Corpus 更新 ≠ runtime 更新；runtime 只经 MY-SKILLS PR → merge → `git pull` 活克隆（Rules `skills.md` §1b）。
- **无评分系统**；候选只记最小字段。

### 步骤

```text
1 证据摄入 (intake)
      │  格式 = 收集标准 HARVEST-STANDARD（细ID 三桶 + 候选字段）
      ▼
2 证据类型 (type)
      │  用户纠正 | 失败返工 | 成功案例 | AI假设
      ▼
3 归属 (ownership)
      │  R / S / Reg / Cap / Corpus
      ▼
4 候选记录 (candidate)
      │  最小字段；落 corpus，不改 live
      ▼
5 人工批准 (human gate)
      │  城城说「进skills」（或等价显式批准）
      ▼
6 范围变更 (scoped change)
      │  按归属改一处；遵守预算；按风险分级
      ▼
7 回归四问 (regression)
      │  全过才可合入
      ▼
8 晋升或回滚 (promote / rollback)
```

### 1–2 证据摄入与类型

| 证据类型 | 默认处置 | 自动改 runtime？ |
|---|---|---|
| 用户纠正 | 候选 → 待「进skills」 | 否 |
| 失败返工 | 候选 → 待「进skills」 | 否 |
| 成功案例 | **默认进 Corpus**（可再候选晋升） | 否 |
| AI假设 | 只记候选 / 备注；**永不**自动改 runtime | 否 |

摄入格式指针：收集标准 `HARVEST-STANDARD.md`（细ID：**语料库要素 / 过程 / 注意事项**；另附候选字段，不替换三桶）。

### 3–4 归属与候选最小字段

候选记录（corpus 侧）至少含：

| 字段 | 说明 |
|---|---|
| 证据类型 | 用户纠正 / 失败返工 / 成功案例 / AI假设 |
| 归属 | R / S / Reg / Cap / Corpus |
| 强度 | 低 / 中 / 高（定性；非打分） |
| 处置 | 记 corpus / 待批准 / 已晋升 / 拒绝 / 回滚 |
| 摘要 | 一句话；可附 fine-ID / 路径指针 |

可选：`source`、`date`、`fine_id`、`risk_tier`。不要分数、不要排行榜。

### 5–6 批准与范围变更 · 风险分级

| 风险分级 | 例子 | 门 |
|---|---|---|
| content | corpus 草稿、personal `corpus-*.md` 增补 | 「进skills」+ 预算 |
| merge | 改已有 skill 正文 / 合入 PR | 清单 + 用户同意 merge |
| registry/ID | registry、fine-ID、mount 映射 | 显式批准；禁止 silently 改 ID |
| Rules | MY-RULES | 最高门；propose-only，显式批准 |

Cap 变更 = 改 `base/` 与/或 registry，**不**新建 capabilities 仓。

### 7 回归四问

合入前必须书面回答（可写在 PR 说明）：

1. **防复发**：挡住的是哪类重复失败 / 纠正？
2. **可观测**：合并后怎样知道有效（一次失败复现或检查点即可）？
3. **SSOT**：是否重复或抢别层权威？权威家是否唯一？
4. **预算与边界**：是否 ≤1 核心行为变更、≤3 新规则、无未批边界扩张？

任一项否 → 不晋升；可回退为「只记 corpus」或修订候选。

### 8 晋升 / 回滚

- 晋升：按归属开/更新 PR → 完整变更清单 → merge → 活克隆 `git pull`。
- 回滚：回到已记录 git 点；**禁止**在回归上叠第二次 evolution。
- delete：须显式批准（见上「Budget and outcome」）。

### 指针

- 收集标准（SSOT）：`D:\0Grok\0doc\_corpus\skill-harvest\HARVEST-STANDARD.md`
- 细ID 薄指针：`01_skill-integration/references/text-harvest-by-fine-id.md`
- Rules 门：`MY-RULES/skills.md` §3（propose-only；任务流正文在本文件）
