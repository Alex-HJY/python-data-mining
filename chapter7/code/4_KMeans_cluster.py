# -*- coding: utf-8 -*-
'''
KMeans 聚类
By HJY
2018-7-19
'''
import pandas as pd
from sklearn.cluster import KMeans  # 导入SKLEANRN中K均值聚类算法

INPUTFILE_PATH = '../output/zscoreddata.xls'  # 待聚类的数据文件
K = 5  # 需要进行的聚类类别数
data = pd.read_excel(INPUTFILE_PATH)  # 读取数据

# 调用k-means算法，进行聚类分析
Kmodel = KMeans(n_clusters=K, n_jobs=1)
# n_clusters=K表示有K簇
# n_jobs是并行数，一般等于CPU数较好
Kmodel.fit(data)  # 训练模型

print(Kmodel.cluster_centers_)  # 输出聚类中心
print(Kmodel.labels_)  # 输出各样本对应的类
