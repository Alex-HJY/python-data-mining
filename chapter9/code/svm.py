# -*- coding: utf-8 -*-
"""
构建SVM模型来分类数据
BY HJY
2018-7-20
"""
import pandas as pd
from numpy.random import shuffle  # 引入随机函数
from sklearn import svm  # 导入支持向量机函数
from sklearn.externals import joblib  # 导入JOBLIB库用于保存决策树模型
from sklearn import metrics  # 导入输出相关的库，生成混淆矩阵
from pandas import DataFrame

inputfile_path = '../data/moment.csv'  # 数据文件
outputfile1_path = '../output/cm_train.xls'  # 训练样本混淆矩阵保存路径
outputfile2_path = '../output/cm_test.xls'  # 测试样本混淆矩阵保存路径
data = pd.read_csv(inputfile_path, encoding='gbk')  # 读取数据，指定编码为gbk
data = data.values

train_ratio = 0.8  # 训练集占所有数据的比例
shuffle(data)  # 随机打乱数据
data_train = data[:int(len(data) * train_ratio), :]  # 选取前80%为训练数据
data_test = data[int(len(data) * train_ratio):, :]  # 选取前20%为测试数据

K = 30  # 数据放大倍数
x_train = data_train[:, 2:] * K
y_train = data_train[:, 0].astype(int)  # 数据类型转换为整形,经测试不使用整形也行
x_test = data_test[:, 2:] * K
y_test = data_test[:, 0].astype(int)

# 训练SVM模型
model = svm.SVC()
model.fit(x_train, y_train)

# 保存模型
svmfile_path = '../output/svm.model'
joblib.dump(model, svmfile_path)

# 构建混淆矩阵
cm_train = metrics.confusion_matrix(y_train, model.predict(x_train))
cm_test = metrics.confusion_matrix(y_test, model.predict(x_test))

# 输出混淆矩阵
DataFrame(cm_train, index=range(1, 6), columns=range(1, 6)).to_excel(outputfile1_path)
DataFrame(cm_test, index=range(1, 6), columns=range(1, 6)).to_excel(outputfile2_path)
