# -*- coding: utf-8 -*-
"""
利用经验阈值划分用水事件
BY HJY
2018-7-20
"""
import pandas as pd

THRESHOLD = pd.Timedelta('4 min')  # 阈值暂定为4分钟
INPUTFILE_PATH = '../data/water_heater.xls'
OUTPUTFILE_PATH = '../output/dividsequence.xls'

data = pd.read_excel(INPUTFILE_PATH)
data[u'发生时间'] = pd.to_datetime(data[u'发生时间'], format='%Y%m%d%H%M%S')
# 将表中时间由字符串转换成时间格式
data = data[data[u'水流量'] > 0]  # 剔除水流量为0记录
d = data[u'发生时间'].diff() > THRESHOLD  # 记录时间间隔大于阈值的记录
data[u'事件编号'] = d.cumsum() + 1  # 根据记录给各个时间编号
data.to_excel(OUTPUTFILE_PATH)
