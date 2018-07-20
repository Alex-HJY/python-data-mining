# -*- coding: utf-8 -*-
"""
确定最佳p、d、q值
BY HJY
2018-7-20
"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import numpy as np

discfile = '../data/discdata_processed.xls'

data = pd.read_excel(discfile, index_col='COLLECTTIME')  # 把时间作为行INDEX
data = data.iloc[: len(data) - 5]  # 不使用最后5个数据
xdata = data['CWXT_DB:184:D:\\']

pmax = int(len(xdata) / 10)  # 一般阶数不超过length/10
qmax = int(len(xdata) / 10)  # 一般阶数不超过length/10
bic_matrix = []  # bic矩阵

for p in range(pmax + 1):
    tmp = []
    for q in range(qmax + 1):
        try:  # 存在部分报错，所以用try来跳过报错。
            tmp.append(ARIMA(xdata, (p, 1, q)).fit().bic)
        except:
            tmp.append(np.nan)
    bic_matrix.append(tmp)

bic_matrix = pd.DataFrame(bic_matrix)
a = bic_matrix.min().min()  # 找出最小值
p, q = np.where(bic_matrix == a)  # 找出最小值坐标
# 从中找出最小值
print(u'BIC最小的p值和q值为：%s、%s' % (p[0], q[0]))
