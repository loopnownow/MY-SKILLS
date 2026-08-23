#!/usr/bin/env python3
"""query_patient.py - 医院 HIS 系统查询（模板）
功能：登录医院系统，按患者 ID 查询出院小结与检验报告
依赖：selenium, pandas
用法：修改配置后运行
"""

import time
import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==================== 配置区（软编码，置顶） ====================
LOGIN_URL = "http://172.16.9.68:9001/Portal/Auth/LoginInterface"
USERNAME = "synadmin"
PASSWORD = "Fie1denginee!r"
QUERY_URL = "http://172.16.9.68:9001/patientMain"
ID_FILE = r"F:\testdata\patient_ids.txt"     # 患者 ID 列表
OUTPUT_CSV = r"F:\testdata\query_results.csv"  # 输出
WAIT_TIMEOUT = 20                              # 等待超时（秒）
RETRY_TIMES = 3                                # 重试次数
# ================================================================


def login(driver):
    """登录系统"""
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    # 等待搜索框出现（若未找到则延时等待）
    try:
        user_box = wait.until(EC.presence_of_element_located((By.NAME, "userCode")))
        user_box.send_keys(USERNAME)
        pwd_box = driver.find_element(By.NAME, "passWord")
        pwd_box.send_keys(PASSWORD)
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)
    except Exception as e:
        print(f"❌ 登录失败: {e}")


def query_patient(driver, patient_id):
    """查询单个患者"""
    driver.get(QUERY_URL)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    # 等待搜索框出现
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search")))
    # 清空原有 ID
    search_box.clear()
    search_box.send_keys(patient_id)
    search_box.send_keys("\n")
    time.sleep(3)
    # 提取结果（示例）
    return {"patient_id": patient_id, "status": "ok"}


def main():
    ids = Path(ID_FILE).read_text(encoding="utf-8").splitlines()
    driver = webdriver.Chrome()
    login(driver)

    records = []
    for pid in ids:
        for attempt in range(RETRY_TIMES):
            try:
                result = query_patient(driver, pid)
                records.append(result)
                print(f"✅ {pid}")
                break
            except Exception as e:
                print(f"⚠️ {pid} 第 {attempt+1} 次失败: {e}")
                time.sleep(2)
        else:
            records.append({"patient_id": pid, "status": "failed"})

    driver.quit()
    # 输出
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["patient_id", "status"])
        writer.writeheader()
        writer.writerows(records)
    print(f"✅ 已写入 {OUTPUT_CSV}")


if __name__ == "__main__":
    main()