# How to write a method upgrade into the justification — Voice B (your own)

**Put the method upgrade into the justification narrative — do not start a parallel essay, and do not dump it only in the innovation box.**
Reviewing someone else's NSFC → `grant-review.md` (Voice A). Whether the topic is new enough / journal landscape → other files in this bundle; this chapter only answers how the upgraded method nests into the proposal justification.

Placeholders: `[Title]` `[疾病]` `[表型]` `[技术]` `[n]` `[PI]` `[假说]`. Do not write unpublished patient tables, ethics scans, phones, or full pathway text.

## Upgrade chain (method words — not pretending old work is new)

When writing justification, pick words by the **current** method generation. Do not write backwards: early drafts must not claim unfinished techniques as completed basis.

| Generation | Method words (tech gap in justification → this study) | How to use in justification |
|---|---|---|
| Baseline spectroscopy | 1H-MRS / in vivo + ex vivo MRS | As an existing readout; name the gap: low sensitivity/specificity, **cannot quantify [molecule]** |
| Upgrade 1 | Hyperpolarized 13C-MRS / metabolic-flux tracing (substrate → product) | Against the prior gap: quantify [molecule], trace [A]→[B] |
| Upgrade 2 | Multimodal imaging + interpretable ML | Against subjective scales / single-modality limits: integrate heterogeneous data and predict phenotype; gold standard still pathology or scales |

The chain belongs in the **justification body** (tech-gap paragraph under a mechanism-node heading). The innovation box only gets one sentence on “what method replaced that gap” — do not rewrite the review there.

## How to write it into justification (nest it; no new chapter)

1. **Subsection titles are mechanism nodes**, not method names. Methods are evidence, not chapter titles.
2. After “mainstream theory and its gap” or right after prior work, nail the tech gap in a short paragraph:
   - `[技术]敏感性、特异性低，且无法对[分子]进行定量。`
   - `目前通常采用[量表]协助诊断，缺乏客观评估手段，容易受到主观因素影响。`
3. “What this study will do” continues from the gap: noninvasive `[升级技术]` ± animal/cell validation — not a sudden unrelated new platform.
4. Align the two innovation columns with justification:
   - Method column = countermeasure to the named gap (1H-MRS cannot quantify → hyperpolarized 13C; subjective scales → radiomics / interpretable ML).
   - Idea column = mechanism one step forward — not “we used MRI.”

## Drop-in justification closers (placeholders)

```
如果能探寻[代谢节点]，示踪[A]到[B]的过程，有望早期发现[表型]，并进一步揭示发病机制。
我们拟使用无创的[升级技术]，检测[对象]的[读出]。通过比较[因素]与[表型]的相关性，并使用[对照模型]加以验证。
```

From 2022, abstracts can nail one sentence each (NSFC fields are short — these two earn their space; full bank in `grant-writing.md`):

```
技术上拟创新性使用[技术]对[分子/表型]进行定量。
理论上创新性提出[分子]通过[通路]导致[细胞事件]，最终导致[表型]。
```

## Key scientific questions (after the method upgrade)

Question form fits general/cross schemes:

- `如何实现多模态异质数据的智能整合与精准预测？传统统计方法难以同时处理包含[临床/代谢/炎症/影像]的高维异质数据。本研究拟基于机器学习算法，构建具可解释性的跨模态预测模型。`
- `[疾病]相关[表型]的病理核心机制是什么？目前尚不清楚多系统异常如何协同作用。本研究拟通过整合[组学A]、[组学B]与[影像]数据，揭示[轴]的动态互作机制。`

Statement form fits early/youth: `使用在体和离体[技术]阐明[表型]干预前后的特征性代谢谱及其变化规律。`

## Division of labor vs other frontier files

- `03_research/personal/radiology-frontier.md` + live `design-study` / `lit-search`: whether the direction is new, whether data can support it, what journals require for validation.
- **This file:** once the path is MRS → hyperpolarized 13C / flux → multimodal+ML, **which paragraph of the justification gets which sentence**.
- Do not put Voice A critique (「创新性有限」) or English journal “Please clarify” into the justification.
