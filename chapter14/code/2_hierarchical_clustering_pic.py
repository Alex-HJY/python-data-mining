#-*- coding: utf-8 -*-
"""
谱系聚类确定聚类的簇数
BY HJY
2018-7-23
"""
import  pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
#这里使用scipy的层次聚类函数

INPUT_FILE_PATH = '../data/standardized.xls' #标准化后的数据文件
data = pd.read_excel(INPUT_FILE_PATH, index_col =u'基站编号') #读取数据
Z = linkage(data, method = 'ward', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()