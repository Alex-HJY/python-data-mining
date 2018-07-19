# -*- coding: utf-8 -*-
'''
数据清洗，过滤数据
By HJY
2018-7-19
'''
import pandas as pd

datafile_path = '../data/air_data.csv'  # 航空原始数据,第一行为属性标签
cleanedfile_path = '../output/data_cleaned.csv'  # 数据清洗后保存的文件
data = pd.read_csv(datafile_path, encoding='utf-8')  # 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）

data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
# 票价非空值才保留,通过.notnull检索剔除空值
# 原书为data['SUM_YR_1'].notnull()*data['SUM_YR_2']，建议将*改为&

# 只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
# 只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
data = data[index1 | index2 | index3]
#  只要符合三者之一就可以，故用|

data.to_csv(cleanedfile_path)  # 导出结果
