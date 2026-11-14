# Lab-STE（实验室可控语言）

给人读的规范 + 可配置词表。不是 ASD-STE100 原文，也不进 skill Gate。当前版本 0.2.1。

| 文件 | 说明 |
|---|---|
| [Lab-STE-SPEC.md](Lab-STE-SPEC.md) | 规则正文 v0.2.1 |
| [spec.html](spec.html) | 规范的单文件网页版：流程图、规则表、阈值表（由规范与配置生成） |
| [config.yaml](config.yaml) | 阈值、场景档案、批注体例（全部带注释） |
| [approved-en.tsv](approved-en.tsv) | 英文批准词典，949 词元 / 1091 条目（通用词，无专业英语） |
| [approved-en.lemmas.txt](approved-en.lemmas.txt) | 词元清单 |
| [term-lock-default.tsv](term-lock-default.tsv) | 领域通用词默认锁定模板 |
| [lexicons/](lexicons/) | 去 AI / 名词化 / 模糊词 / 四字格 |
| [tools/check_spec_examples.py](tools/check_spec_examples.py) | 核对规范英文正例是否都在词典或锁定表内 |
| [tools/build_spec_html.py](tools/build_spec_html.py) | 由规范和配置重新生成 spec.html |
| [CHANGELOG.md](CHANGELOG.md) | 版本记录 |

专业术语（IVIM、AUC、病名等）放各课题术语锁定表，不写入批准词典。
领域通用名词（patient、feature、slice、reader 等）放 `term-lock-default.tsv`。

改完词典或配置后：

```
python tools/check_spec_examples.py
python tools/build_spec_html.py
```
