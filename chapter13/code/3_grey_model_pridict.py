# -*- coding: utf-8 -*-
"""
LASSO回归选择变量
BY HJY
2018-7-23
"""
import numpy as np
import pandas as pd
from GM11 import GM11

INPUT_FILE_PATH = '../data/data1.csv'  # 输入的数据文件
OUTPUT_FILE_PATH = '../output/data1_GM11.xls'  # 灰色预测后保存的路径
data = pd.read_csv(INPUT_FILE_PATH)
data.index = range(1994, 2014)  # 添加索引
data.loc[2014] = None
data.loc[2015] = None

labels = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']
for label in labels:
    f = GM11(data.loc[range(1994, 2014), label].values)[0]  # f为灰度预测函数
    data.loc[2014, label] = f(len(data) - 1)  # 2014年预测结果
    data.loc[2015, label] = f(len(data))  # 2015年预测结果

data = data[labels + ['y']].round(2)  # 限制为两位小数，添加结果y
data.to_excel(OUTPUT_FILE_PATH)
