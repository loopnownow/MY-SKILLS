#!/usr/bin/env python3
"""extract_patient_data.py - 患者信息与检验指标提取（模板）
功能：从 .txt 文件提取患者基本信息与检验指标
依赖：pandas, re
用法：修改配置后运行
"""

import re
import csv
from pathlib import Path

# ==================== 配置区（软编码，置顶） ====================
TXT_DIR = r"F:\IDs\DMB_zjl"          # 源目录（含 .txt 文件）
OUTPUT_CSV = r"F:\IDs\patient_data.csv"  # 输出 CSV
# ================================================================

# 检验指标关键词字典（LAB_DICT）
LAB_DICT = {
    "姓名": ["姓名", "患者姓名"],
    "性别": ["性别"],
    "年龄": ["年龄"],
    "门诊号": ["门诊号", "门诊号码"],
    "白细胞": ["白细胞", "WBC"],
    "血红蛋白": ["血红蛋白", "Hb"],
    "血小板": ["血小板", "PLT"],
    "谷丙转氨酶": ["谷丙转氨酶", "ALT"],
    "谷草转氨酶": ["谷草转氨酶", "AST"],
    "肌酐": ["肌酐", "Cr"],
    "尿素氮": ["尿素氮", "BUN"],
    "血糖": ["血糖", "Glu"],
    "总胆固醇": ["总胆固醇", "TC"],
    "甘油三酯": ["甘油三酯", "TG"],
    "C反应蛋白": ["C反应蛋白", "CRP"],
}


def extract_value(text: str, keywords: list):
    """从文本中提取关键词后的值"""
    for kw in keywords:
        # 匹配 "关键词: 值" 或 "关键词 值"
        pattern = rf"{re.escape(kw)}[：:\s]*([\d.]+)"
        m = re.search(pattern, text)
        if m:
            return m.group(1)
    return ""


def extract_patient_info(text: str):
    """提取单个患者的全部信息"""
    row = {}
    for field, keywords in LAB_DICT.items():
        row[field] = extract_value(text, keywords)
    return row


def main():
    src = Path(TXT_DIR)
    records = []

    for file in sorted(src.glob("*.txt")):
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
            row = extract_patient_info(text)
            row["文件名"] = file.stem
            records.append(row)
            print(f"✅ {file.stem}: {row.get('姓名', '')}")
        except Exception as e:
            print(f"❌ {file.name}: {e}")

    # 输出 CSV
    if records:
        fieldnames = ["文件名"] + list(LAB_DICT.keys())
        with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
        print(f"✅ 已写入 {OUTPUT_CSV}，共 {len(records)} 条")


if __name__ == "__main__":
    main()