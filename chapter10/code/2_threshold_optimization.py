# -*- coding: utf-8 -*-
"""
阈值寻优
BY HJY
2018-7-20
"""
import numpy as np
import pandas as pd
from pandas import DataFrame

INPUT_FILE_PATH = '../data/water_heater.xls'
N = 5  # 使用以后包括自身共五个点的平均斜率
THRESHOLD = pd.Timedelta(minutes=5)  # 阈值暂定为5分钟


def event_num(THRESHOLD):
    """
    :param THRESHOLD:阈值
    :return: 该数据里根据时间阈值划分出来的事件总数
    """
    d = data[u'发生时间'].diff() > THRESHOLD  # 相邻时间作差分，比较是否大于阈值，大于阈值记为TRUE(1)
    return d.sum() + 1  # 返回事件数，+1是为了记录第一次间隔时间超过阈值的事件之前的事件


data = pd.read_excel(INPUT_FILE_PATH)
data[u'发生时间'] = pd.to_datetime(data[u'发生时间'], format='%Y%m%d%H%M%S')
data = data[data[u'水流量'] > 0]  # 只要流量大于0的记录

dt = [pd.Timedelta(minutes=i) for i in np.arange(1, 9, 0.25)]
h = DataFrame(dt, columns=[u'阈值'])  # 定义阈值列
h[u'事件数'] = h[u'阈值'].apply(event_num)  # 计算每个阈值对应的事件数
h[u'斜率'] = h[u'事件数'].diff() / 0.25  # 计算每两个相邻点对应的斜率
h[u'斜率指标'] = h[u'斜率'].abs().rolling(N).mean()  # 采用后n个的斜率绝对值平均作为斜率指标
ts = h[u'阈值'][h[u'斜率指标'].idxmin() - N + 1]  # 计算最优阈值
# 注：用idxmin返回最小值的Index，由于rolling_mean()自动计算的是前n个斜率的绝对值平均
# 所以结果要进行平移（-n+1）
