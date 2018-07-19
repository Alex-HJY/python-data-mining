# -*- coding: utf-8 -*-
'''
标准差标准化
By HJY
2018-7-19
'''
import pandas as pd

datafile_path = '../data/zscoredata.xls'  # 需要进行标准化的数据文件；
zscoredfile_path = '../output/zscoreddata.xls'  # 标准差化后的数据存储路径文件；
data = pd.read_excel(datafile_path)

# 标准化处理
data = (data - data.mean(axis=0)) / (data.std(axis=0))
# 简洁的语句实现了标准化变换,.mean为求均值，.std求标准差，axis=0为按列求
data.columns = ['Z_' + i for i in data.columns]  # 表头重命名。
data.to_excel(zscoredfile_path, index=False)  # 数据写入,不加索引标签
