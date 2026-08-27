# 机制

Use this file when the user has completed, or plans to complete, a radiomics or
medical imaging deep learning model and wants to explain its biological basis using
bulk transcriptomics, single-cell RNA-seq, spatial transcriptomics, genomics,
proteomics, metabolomics, pathology, immune microenvironment, or other multi-omics data.

## 核心原则

机制解析的目标不是给影像模型“补一个组学分析”，而是建立一条可解释、可验证的证据链：

```text
影像表型 / radiomics score / deep feature
-> 分子通路和基因模块
-> 细胞类型、免疫状态或空间生态位
-> 病理生物学过程
-> 临床终点或治疗反应
```

不要把相关性写成机制。最稳妥的表述通常是“提示/关联/支持某种生物学解释”，只有在有实验验证、独立队列验证或强因果设计时才使用更强结论。

## 需要先问清楚

```yaml
radiomics_model:
  features_or_radscore:
  endpoint:
  validation:
  selected_features:
  image_region: tumor / peritumor / habitat / whole organ
omics_data:
  bulk_rna:
  single_cell:
  spatial_transcriptomics:
  genomics_mutation_cnv_methylation:
  proteomics_metabolomics:
matching:
  paired_same_patients:
  n_paired:
  same_region_or_block:
  time_gap:
clinical_data:
  pathology:
  treatment:
  survival_or_response:
constraints:
  sample_size:
  batch:
  missingness:
  target_output:
```

关键判断：组学数据是否与影像来自同一患者、同一病灶、同一时间点、同一空间区域。未配对数据只能做外部解释或公共数据库验证，不能写成直接机制证据。

## 总体分析框架

1. **定义影像表型。** 使用 radiomics score、关键影像特征、影像 habitat、深度模型 embedding、attention 区域或高低风险分组。
2. **建立配对关系。** 以患者/病灶/区域为单位连接影像、组学、病理和临床终点。
3. **找分子关联。** 分析影像表型与基因、通路、免疫浸润、细胞类型、空间区域之间的关系。
4. **构建生物学解释。** 从缺氧、增殖、血管生成、炎症、免疫抑制、EMT、DNA 修复、代谢重编程、基质反应等方向解释。
5. **验证证据链。** 用外部队列、公共数据库、病理/IHC、多重免疫荧光、空间转录组、功能实验或敏感性分析验证。
6. **控制表述强度。** 分清相关、预测、解释、机制和因果。

## bulk RNA-seq 套路

适合：有配对 bulk 转录组，或有 TCGA/GEO/自建队列可做验证。

常用路径：

1. 按 radscore 或模型风险分为 high/low 组，或把 radscore 作为连续变量。
2. 做差异表达分析：DESeq2、edgeR、limma-voom。
3. 做通路富集：GSEA、GSVA/ssGSEA、GO、KEGG、Reactome、Hallmark。
4. 做基因模块：WGCNA 或相关网络，找与 radscore 相关的模块。
5. 做免疫微环境估计：ESTIMATE、CIBERSORT、xCell、MCP-counter、TIMER、quanTIseq、ssGSEA immune signatures。
6. 做临床连接：通路/模块与生存、疗效、病理分级、分子分型或免疫治疗应答关联。
7. 做外部验证：公共队列或独立队列验证 radscore 相关通路/基因模块是否稳定。

输出逻辑：

```text
高 radscore 组富集 [通路/基因集]，并伴随 [细胞成分/免疫状态] 改变；
这些分子特征与 [终点] 相关，提示影像模型可能捕捉到 [生物过程]。
```

风险：

- 样本量小导致差异基因不稳定。
- 多重检验未校正。
- bulk 结果不能区分细胞来源。
- 公共数据库和本队列平台/人群/处理流程不同。

## 单细胞转录组套路

适合：需要解释 bulk 通路来自哪些细胞，或想说明影像表型对应的免疫/肿瘤/基质细胞状态。

常用路径：

1. 质量控制、降维、聚类和注释：Seurat、Scanpy。
2. 注释主要细胞类型：肿瘤细胞、T/NK、B、髓系、成纤维细胞、内皮、上皮等。
3. 从 bulk 或 radiomics 关联基因构建 gene signature。
4. 在单细胞中打分：AddModuleScore、AUCell、UCell、ssGSEA-like scoring。
5. 定位 signature 主要表达在哪些细胞类型或细胞状态。
6. 比较高低风险相关 signature 的细胞比例、激活状态、耗竭状态、髓系免疫抑制、CAF 亚型、血管生成状态等。
7. 做细胞通讯：CellChat、CellPhoneDB、NicheNet、LIANA，连接影像表型相关 signature 与配体-受体轴。
8. 可选做拟时序/状态转变：Monocle、Slingshot、scVelo，用于解释侵袭、分化、耐药或免疫逃逸。

输出逻辑：

```text
radiomics 相关基因模块主要定位于 [细胞类型/状态]；
高风险影像表型与 [免疫抑制/缺氧/基质激活/增殖] 相关细胞状态一致；
细胞通讯分析提示 [配体-受体轴] 可能参与该影像表型对应的微环境改变。
```

风险：

- 单细胞数据未与影像患者配对时，只能做机制注释或外部支持。
- 细胞注释错误会影响后续解释。
- 细胞比例受采样和消化偏倚影响。

## 空间转录组套路

适合：想把影像区域、病理区域和空间分子生态位连起来，特别适合解释 habitat、瘤内异质性、瘤周区域、免疫排斥和空间结构。

常用路径：

1. 建立空间坐标：影像 ROI/病灶区域、病理切片、空间转录组 spot/细胞坐标。
2. 定义影像区域：高/低 radscore habitat、增强/坏死/水肿/瘤周区域、深度模型关注区域。
3. 做空间表达和区域差异：空间可变基因、区域差异基因、空间通路 score。
4. 做细胞组成反卷积：cell2location、RCTD、SPOTlight、Tangram、Seurat label transfer。
5. 做空间邻域和生态位：肿瘤-免疫-基质邻近关系、免疫排斥边界、血管/缺氧区域。
6. 做空间细胞通讯：将配体-受体轴限制在邻近细胞或区域内解释。
7. 把空间机制映射回影像：说明某类影像表型对应的空间结构和微环境状态。

输出逻辑：

```text
高风险影像区域在空间转录组中对应 [区域/生态位]；
该区域富集 [通路] 并聚集 [细胞类型]；
提示影像模型可能捕捉到 [空间异质性/免疫排斥/缺氧坏死/基质屏障]。
```

风险：

- 影像和空间切片不是同一区域时，只能做间接解释。
- 组织变形、切片方向和配准误差会影响结论。
- spot 分辨率限制细胞级解释。

## 基因组、甲基化、蛋白和代谢组

可选补充：

- **突变/CNV**：比较 radscore 与关键突变、拷贝数改变、突变负荷、分子分型。
- **甲基化**：解释表观遗传亚型、免疫状态或分化状态。
- **蛋白组/磷酸化组**：连接通路活性和信号轴，比 RNA 更接近功能状态。
- **代谢组**：解释缺氧、糖酵解、脂代谢、氧化应激等影像表型。
- **病理组学**：连接影像区域与组织结构、细胞密度、坏死、基质和免疫浸润。

## 推荐证据链模板

```text
1. 影像模型层：radscore/deep feature 可预测 [终点]，并在 [验证方式] 中稳定。
2. 分子层：高 radscore 与 [通路/模块] 显著相关。
3. 细胞层：该通路主要来源于 [细胞类型/细胞状态]。
4. 空间层：相关细胞/通路聚集在 [空间生态位/影像 habitat]。
5. 临床层：该机制轴与 [疗效/复发/生存/分型] 一致。
6. 验证层：在 [独立队列/公共数据库/IHC/空间转录组/功能实验] 得到支持。
```

## 写作表达

更稳妥：

- “该结果提示影像模型可能捕捉到与肿瘤免疫微环境相关的表型差异。”
- “多组学分析支持该影像表型与缺氧和基质重塑相关。”
- “单细胞分析进一步定位该信号主要来源于髓系细胞和 CAF 亚群。”

避免：

- “证明 radiomics 特征导致免疫逃逸。”
- “影像模型揭示了完整机制。”
- “单细胞验证了因果关系。”

## 输出格式

```text
机制解析定位
- 已有影像模型：
- 可用组学数据：
- 是否配对：
- 核心生物学问题：

推荐整合路线
1. bulk RNA：
2. 单细胞：
3. 空间转录组：
4. 其他组学：

关键分析表
| 目标 | 方法 | 输入 | 输出 | 风险 |

建议图表
- Figure 1:
- Figure 2:
- Figure 3:

可写进论文的逻辑
[用谨慎语言串联影像表型、多组学证据和临床终点]

需要补充
- [配对情况、样本量、平台、批次、验证队列等]
```

## 红线

- 不要把未配对公共数据库分析写成直接机制验证。
- 不要从相关性推出因果。
- 不要忽略批次效应、平台差异、样本量和多重检验。
- 不要把单细胞或空间转录组当作装饰性分析；必须服务于具体生物学问题。
- 不要编造基因、通路、细胞类型、配体-受体关系或验证实验。
