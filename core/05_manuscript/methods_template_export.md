# 方法部分写作模板

用于撰写学术论文的 Methods 部分，确保完整、可复现。

**固定顺序与 title page 默认（真源）：** [`Aitor-format.md`](Aitor-format.md)。下面只保留可填空句，不要改顺序。

1. Ethics  
2. Study design and sample size  
3. Patients  
4. Inclusion and exclusion  
5. Diagnostic and treatment criteria  
6. Outcomes and endpoints  
7. Laboratory tests  
8. Imaging examinations  
9. Image processing（分割 / 预处理 / 配准 / habitat / 特征）  
10. Model building  
11. Statistical analysis（软件、正态、相关、模型评价、多重校正、*P*）

---

## 2.1 研究对象（Study Population）

本研究回顾性纳入 [时间范围] 于 [医院/中心] 接受 [检查/治疗] 的 [疾病] 患者。纳入标准：(1) ...；(2) ...。排除标准：(1) ...；(2) ...。最终纳入 [N] 例患者，其中 [组1] [n1] 例，[组2] [n2] 例。

## 2.2 图像采集（Image Acquisition）

所有图像使用 [设备型号] 采集。扫描参数：TR = [X] ms，TE = [X] ms，层厚 = [X] mm，矩阵 = [X]×[X]，FOV = [X] mm。

## 2.3 图像预处理（Image Preprocessing）

图像预处理使用 [软件及版本] 完成。流程包括：(1) [步骤1]；(2) [步骤2]；(3) [步骤3]。

## 2.4 影像组学特征提取（Radiomics Feature Extraction）

使用 [pyradiomics 版本] 从 [图像] 中提取影像组学特征，共 [N] 个特征，包括一阶统计、形状、纹理特征。ROI 由 [X] 名放射科医师 [方法] 勾画。

## 2.5 特征筛选与模型构建（Feature Selection and Model Construction）

特征筛选采用 LASSO 回归（glmnet 包，R 版本 [X]），通过 10 折交叉验证选择最优 lambda（lambda.min）。筛选后保留 [N] 个特征。radscore 通过线性回归拟合筛选特征得到。临床特征采用 [逻辑回归/LASSO] 筛选。

## 2.6 统计建模（Statistical Modeling）

- 基线特征比较：连续变量用 [t检验/Mann-Whitney U]，分类变量用 [卡方/Fisher]
- 模型性能：ROC 曲线、AUC、校准曲线、DCA
- 显著性水平：P < 0.05（双侧）
- 统计软件：R [版本]，Python [版本]

## 2.7 验证（Validation）

数据按 7:3 随机分为建模组（[n1] 例）与验证组（[n2] 例）。验证组使用建模组模型进行预测，不重新筛选特征。

---

## 写作要点
1. **可复现性**：所有软件、版本、参数必须明确
2. **完整性**：每个分析步骤都要描述
3. **统计细节**：检验方法、校正方法、显著性水平
4. **引用**：方法部分不引用文献；TRIPOD / IBSI / Riley 等如需引用，放在 Introduction 或 Discussion。全文其余约定见 `Aitor-format.md`。