# -*- coding: utf-8 -*-
"""
构建并测试CART决策树模型
By HJY
2018-7-18
"""
import pandas as pd
from random import shuffle  # 导入随机函数shuffle，用来打散数据
from sklearn.tree import DecisionTreeClassifier  # 导入决策树模型
from sklearn.externals import joblib  # 导入JOBLIB库用于保存决策树模型
import matplotlib.pyplot as plt  # 导入二维直线图函数
from sklearn.metrics import roc_curve  # 导入ROC曲线函数
from cm_plot import *  # 导入自行编写的混淆矩阵可视化函数

datafile_path = '../data/model.xls'  # 数据名
data = pd.read_excel(datafile_path)  # 读取数据，数据的前三列是特征，第四列是标签
data = data.values
# 将表格转换为ndarray,原书为data.as_matrix()，\
# 但实际返回ndarray而不是matrix类，该方法未来会被弃用，应用values代替
shuffle(data)  # 随机打乱数据

P = 0.8  # 设置训练集比例
train_data = data[:int(len(data) * P), :]  # 前80%为训练集
test_data = data[int(len(data) * P):, :]  # 后20%为测试集

tree = DecisionTreeClassifier()  # 建立决策树模型
tree.fit(train_data[:, :3], train_data[:, 3])  # .fit方法训练测模型，第一个参数为输入向量，第二个参数为输出向量（结果）

treefile_path = '../output/tree.pkl'  # 模型输出路径，以便下次直接调用
joblib.dump(tree, treefile_path)  # 保存模型到文件中
cm_plot(train_data[:,3], tree.predict(train_data[:,:3])).show() #显示混淆矩阵可视化结果
# 注意到Scikit-Learn使用predict方法直接给出预测结果.类型为ndarray

fpr, tpr, thresholds = roc_curve(test_data[:, 3], tree.predict_proba(test_data[:, :3])[:, 1], pos_label=1)
# .predict_prboa返回决策树预测的结果的概率
# 计算ROC曲线，返回值为假正率，真正率，阈值
# 第一个参数为实际结果，第二个参数为预测结果或者概率，pos_label=1表示当结果值为1时记为正

plt.plot(fpr, tpr, linewidth=2, label='ROC of CART', color='green')  # 作出ROC曲线
plt.xlabel('False Positive Rate')  # X坐标轴标签
plt.ylabel('True Positive Rate')  # Y坐标轴标签
plt.ylim(0, 1.05)  # X边界范围
plt.xlim(0, 1.05)  # Y边界范围
plt.legend(loc=4)  # 显示标签(label)图例，LOC=4表示位置位于右下方
plt.show()  # 显示作图结果
