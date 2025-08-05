# -*- coding: utf-8 -*-
"""
主程序入口：统一调用所有爬虫，汇总输出
"""

import pandas as pd
import os

# 导入各平台爬虫（目前只有淘宝）
from crawlers.taobao import crawl_taobao
# from crawlers.xianyu import crawl_xianyu
# from crawlers.ebay import crawl_ebay
# from crawlers.mercari import crawl_mercari


def run_all_crawlers(keyword="战锤 模型", pages=1):
    """
    调用所有平台爬虫，返回合并后的 DataFrame
    """
    print(f"[INFO] 开始抓取关键词：{keyword}，共 {pages} 页")

    df_taobao = crawl_taobao(keyword, pages)
    df_taobao["平台"] = "淘宝"

    # TODO: 后续添加其他平台
    # df_xianyu = crawl_xianyu(keyword, pages)
    # df_xianyu["平台"] = "闲鱼"

    # 合并所有结果
    all_data = pd.concat([df_taobao], ignore_index=True)

    return all_data


def save_output(df, filename="outputs/all_prices.xlsx"):
    """
    保存数据为 Excel 文件
    """
    os.makedirs("outputs", exist_ok=True)
    df.to_excel(filename, index=False)
    print(f"[INFO] 已保存结果到 {filename}")


if __name__ == "__main__":
    result_df = run_all_crawlers(keyword="战锤 模型", pages=1)
    print(result_df.head())
    save_output(result_df)
