# -*- coding: utf-8 -*-
'''
聚类离散化，最后的result的格式为：
      1           2           3           4
A     0    0.178698    0.257724    0.351843
An  240  356.000000  281.000000   53.000000
即(0, 0.178698]有240个，(0.178698, 0.257724]有356个，依此类推。

BY HJY
2018-7-19
'''
import pandas as pd
from sklearn.cluster import KMeans  # 导入K均值聚类算法

datafile_path = '../data/data.xls'  # 待聚类的数据文件路径
processedfile_path = '../output/data_processed.xls'  # 数据处理后文件
typelabel = {u'肝气郁结证型系数': 'A', u'热毒蕴结证型系数': 'B', u'冲任失调证型系数': 'C', u'气血两虚证型系数': 'D', u'脾胃虚弱证型系数': 'E', u'肝肾阴虚证型系数': 'F'}
K = 4

data = pd.read_excel(datafile_path)  # 读取数据
labels = list(typelabel.keys())  # 读取标签
result = pd.DataFrame()

if __name__ == '__main__':  # 加了这句话后，之后的内容必须直接运行该PY文件才可以运行，如果本文件作为库导入则不运行以下代码
    for label in labels:
        # 利用Kmeans聚类离散化
        print(u'正在进行“%s”的聚类...' % label)
        Kmodel = KMeans(n_clusters=K)
        Kmodel.fit(data[label].values.reshape(len(data[label]), 1))
        # 原书为kmodel.fit(data[label].as_matrix()),但是KMeans要求输入二维矩阵，故引入reshape方法

        r1 = pd.DataFrame(Kmodel.cluster_centers_, columns=[typelabel[label]])  # 聚类中心
        # 将各个簇中心制成DATAFRAME
        r2 = pd.Series(Kmodel.labels_).value_counts()
        # 统计各簇的数目
        r2 = pd.DataFrame(r2, columns=[typelabel[label] + 'n'])  # 转为DataFrame，记录各个类别的数目
        r = pd.concat([r1, r2], axis=1).sort_values(by=[typelabel[label]])
        # 匹配聚类中心和类别数目并按簇中心排序
        r.index = [1, 2, 3, 4]
        # 重新命名索引
        r[typelabel[label]] = r.rolling(2).mean()
        # .rolling().mean()用来计算相邻2簇的均值，以此作为边界点。
        r.loc[1, typelabel[label]] = 0.0  #
        # .loc为搜索行
        # 这两句代码将原来的聚类中心改为边界点。
        result = result.append(r.T)  # 放入结果中

    result.to_excel(processedfile_path)
