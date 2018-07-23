# -*- coding: utf-8 -*-
"""
数据标准化
BY HJY
2018-7-23
"""
import pandas as pd

INPUT_FILE_PATH = '../data/business_circle.xls'  # 原始数据文件
OUTPUT_FILE_PATH = '../output/standardized.xls'  # 标准化后数据保存路径

data = pd.read_excel(INPUT_FILE_PATH)

data = (data - data.min()) / (data.max() - data.min())  # 离差标准化
data.reset_index()

data.to_excel(OUTPUT_FILE_PATH, index=False)
