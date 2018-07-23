# -*- coding: utf-8 -*-
"""
层次聚类区分商圈
BY HJY
2018-7-23
"""

import pandas as pd
from sklearn.cluster import AgglomerativeClustering  # 导入sklearn的层次聚类函数
import matplotlib.pyplot as plt

INPUT_FILE_PATH = '../data/standardized.xls'  # 标准化后的数据文件
K = 3  # 聚类数
data = pd.read_excel(INPUT_FILE_PATH, index_col=u'基站编号')  # 读取数据

model = AgglomerativeClustering(n_clusters=K)
model.fit(data)  # 训练模型,可以直接使用dataframe数据类型

# 详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  # 合并样本数据和每个样本对应的类别
r.columns = list(data.columns) + ['聚类类别']  # 重命名表头

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

style = ['ro-', 'go-', 'bo-']
xlabels = [u'工作日人均停留时间', u'凌晨人均停留时间', u'周末人均停留时间', u'日均人流量']
pic_output = '../output/type_'  # 聚类图文件名前缀

for i in range(K):
    plt.figure()
    tmp = r[r[u'聚类类别'] == i].iloc[:, :4]
    for j in range(len(tmp)):
        plt.plot(range(1, 5), tmp.iloc[j], style[i])  # 对每个样本画线
    plt.xticks(range(1, 5), xlabels, rotation=20)  # X轴坐标标签
    plt.title(u'商圈类别 %s' % (i + 1))  # 我们计数习惯从1开始
    plt.subplots_adjust(bottom=0.15)  # 底部调整为0.15,防止标签显示不全
    plt.savefig(u'%s%d.png' % (pic_output, i + 1))  # 保存图片
