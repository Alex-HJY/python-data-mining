# -*- coding: utf-8 -*-
"""
对DATA1数据作探索,并计算相关系数矩阵
BY HJY
2018-7-23
"""
import pandas as pd
import numpy as np

INPUT_FILE_PATH = '../data/data1.csv'  # 输入的数据文件
data = pd.read_csv(INPUT_FILE_PATH)
r = [data.min(), data.max(), data.mean(), data.std()]  # 依次计算最小值、最大值、均值、标准差
r = pd.DataFrame(r, index=['Min', 'Max', 'Mean', 'STD']).T  # 合成一个数据框DATAFRAME
r.round(2) #保留两位小数 # 保留两位小数
#以上功能完全可以用data.describe()来实现
corr_matrix=np.round(data.corr(method='pearson'),2)#计算相关系数矩阵，保留两位小数
