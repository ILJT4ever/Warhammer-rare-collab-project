# -*- coding: utf-8 -*-
"""
淘宝爬虫模块（初版）
功能：通过关键词搜索淘宝，抓取商品标题与价格
注意：淘宝页面存在动态加载与反爬，后续可能改为 Selenium
当前脚本适用于淘宝 PC 页面搜索结果的静态结构，如淘宝页面变化或加载机制不同，则需切换为 Selenium。
若页面数据抓不到，请切换网络环境（淘宝有地域/风控限制）。
爬虫文件已经存储在 outputs/taobao_test_output.xlsx，会被 .gitignore 忽略 ✅
"""

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import time


def crawl_taobao(keyword: str, max_pages: int = 1):
    """
    抓取淘宝指定关键词的商品信息

    参数：
        keyword: 搜索关键词（例如 "战锤 模型"）
        max_pages: 抓取页数，默认 1 页

    返回：
        pandas.DataFrame 格式，包含标题和价格
    """

    base_url = "https://s.taobao.com/search"
    headers = {
        "User-Agent": UserAgent().random
    }

    all_items = []

    for page in range(max_pages):
        params = {
            "q": keyword,
            "s": str(page * 44)  # 淘宝每页大约 44 个商品
        }

        print(f"[INFO] 正在抓取第 {page + 1} 页：{keyword}")
        try:
            response = requests.get(base_url, headers=headers, params=params, timeout=10)
            html = response.text

            soup = BeautifulSoup(html, "html.parser")
            scripts = soup.find_all("script")

            # 淘宝数据通常隐藏在第 n 个 <script> 标签中，可调试以下逻辑
            for script in scripts:
                if 'g_page_config' in script.text:
                    start = script.text.find('{"')
                    end = script.text.rfind('}}') + 2
                    json_text = script.text[start:end]
                    break
            else:
                print("[WARN] 页面中未找到商品数据脚本")
                continue

            import json
            data = json.loads(json_text)
            items = data["mods"]["itemlist"]["data"]["auctions"]

            for item in items:
                all_items.append({
                    "标题": item.get("title", ""),
                    "价格": item.get("view_price", ""),
                    "链接": item.get("detail_url", ""),
                    "位置": item.get("item_loc", ""),
                    "卖家昵称": item.get("nick", "")
                })

        except Exception as e:
            print(f"[ERROR] 抓取失败：{e}")
            continue

        time.sleep(1)  # 避免过快请求被封 IP

    return pd.DataFrame(all_items)


# 调试用：可在命令行执行本文件测试
if __name__ == "__main__":
    df = crawl_taobao("战锤 模型", max_pages=1)
    print(df.head())
    df.to_excel("outputs/taobao_test_output.xlsx", index=False)
