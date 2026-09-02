#!/usr/bin/env python3
"""extract_docx.py - docx 文档批量提取（模板）
功能：遍历目录下所有 .docx，提取指定关键词内容
依赖：python-docx, pandas
用法：修改配置后运行
"""

import csv
import re
from pathlib import Path
from docx import Document

# ==================== 配置区（软编码，置顶） ====================
DOCX_DIR = r"E:\lxf\cln\one"         # 源目录（含 .docx）
OUTPUT_CSV = r"E:\lxf\docx_extract.csv"  # 输出 CSV
RECURSIVE = True                       # 是否递归子文件夹
# ================================================================

# 需要提取的关键词（可扩展）
KEYWORDS = {
    "姓名": ["姓名", "患者姓名"],
    "性别": ["性别"],
    "年龄": ["年龄"],
    "门诊号": ["门诊号"],
    "住院号": ["住院号"],
}


def extract_docx(file_path: Path):
    """提取单个 docx 内容"""
    doc = Document(str(file_path))
    text = "\n".join(p.text for p in doc.paragraphs)
    return text


def find_keyword(text: str, keywords: list):
    """从文本找关键词后的值"""
    for kw in keywords:
        pattern = rf"{re.escape(kw)}[：:\s]*([^\s，。；]+)"
        m = re.search(pattern, text)
        if m:
            return m.group(1)
    return ""


def main():
    src = Path(DOCX_DIR)
    records = []

    pattern = "**/*.docx" if RECURSIVE else "*.docx"
    for file in sorted(src.glob(pattern)):
        try:
            text = extract_docx(file)
            row = {field: find_keyword(text, kws)
                   for field, kws in KEYWORDS.items()}
            row["文件路径"] = str(file)
            records.append(row)
            print(f"✅ {file.name}: {row.get('姓名', '')}")
        except Exception as e:
            print(f"❌ {file.name}: {e}")

    # 输出
    if records:
        fieldnames = ["文件路径"] + list(KEYWORDS.keys())
        with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
        print(f"✅ 已写入 {OUTPUT_CSV}，共 {len(records)} 条")


if __name__ == "__main__":
    main()