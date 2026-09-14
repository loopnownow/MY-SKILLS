---
name: grilling
description: >
  Interrogate a vague build/implementation request into an executable spec before
  starting. Trigger on grill-me, grill-with-docs, 盘问, 烤透需求, 需求盘问, or whenever
  a request to write code, build a tool/page/script, define a new skill, or design a
  pipeline is underspecified. Two modes: grill-me (ask directly, batched, one round);
  grill-with-docs (read existing repo/docs/web first, ask only what's left). Do not use
  for single-step tasks with one obvious implementation, for repeated questions already
  answered this task, or for literature/stats/writing/review (those own their interaction
  rules in 03/04/05/06).
---

# Grilling（需求烤透）

不能一句"做个登录页"就开工。任何构建/实现类请求（写代码、做工具、建页面、定义新技能、设计
pipeline）动手前，先把需求烤到**任何一个不知道背景的实现者拿着这份规格就能做，不用再问一句**
的程度。这是通用交互层，不是某个领域技能——具体领域（文献/统计/写作/审稿）已经在 03–06 里有
自己的提问规则，不套用这个。

## 两种模式

### grill-me — 直接问

列出你自己回答不了的每一个问题，编号，每题带你的推荐答案，**一轮问完，等答案**，不要一次问一题、
来回好几轮：

```
❓ Q1 — <标题>：<问题，可能带选项/多段说明>

➡️ <你的推荐答案>

---

❓ Q2 — <标题>：<问题>

➡️ <你的推荐答案>
```

只问真正需要用户决策的问题。一个问题的答案依赖另一个还没问的问题时，把它放进下一轮，不要在这一轮
里猜。

### grill-with-docs — 先查后问

提问前先做完这些事，把能查到的都查到，不占用户的提问轮次：

1. 读这个仓库里已有的类似实现（比如新技能吸收前先看 `01_skill-discovery-integration` 的
   capability evaluation 记录，或已有 sub-skill 的 `SKILL.md` 怎么写的）
2. 读用户之前给过的任何规格/文档/截图/已有文件
3. 需要时用网络搜索确认外部事实（框架版本、API 行为、平台限制、协议条款）

做完这些之后，剩下的才是真正需要用户拍板的问题——这时候切到 **grill-me** 的一轮提问格式问出来。
**能查到的事实自己去查，不要当成问题抛给用户。**

## 何时启动

- "做一个/写一个/建一个 X" 类请求，且 X 的行为、边界、失败处理、目标读者不止一种合理解读
- `01_skill-discovery-integration` 评估新技能是否吸收/挂载时
- `00_orchestrator` 的多节点任务派发（`SKILL.md` 里的 Plan card 是这个机制在派发场景下的
  具体应用，规则本体在这份文件，Plan card 不重复定义）

## 何时不启动

- 单一步骤、只有一种合理做法的任务（改一个错字、加一行 import）
- 同一任务里已经问过、用户已经回答过的问题——不重复问
- 文献/统计/写作/审稿类任务，走 03/04/05/06 各自的规则

## 完成标准

一轮问完、用户确认收到共同理解之后再动手。某个答案又牵出一个依赖它才能问的新问题时，开下一轮——
但大多数任务一轮就够；开到三轮以上说明前面某一轮问题问得不够全，不是任务本身天生复杂，回头检查
是不是漏了该 grill-with-docs 先查的东西。
