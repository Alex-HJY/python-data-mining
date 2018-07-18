# -*- coding: utf-8 -*-
"""
构建LM神经网络模型
"""
import pandas as pd
from random import shuffle
from keras.models import Sequential  # 导入神经网络初始化函数
from keras.layers.core import Dense, Activation  # 导入神经网络层函数、激活函数
from cm_plot import *
from sklearn.metrics import roc_curve  # 导入ROC曲线函数
import matplotlib.pyplot as plt  # 导入二维直线图函数

datafile = '../data/model.xls'
data = pd.read_excel(datafile)
data = data.values
shuffle(data)

P = 0.8
train_data = data[:int(len(data) * P), :]
test_data = data[int(len(data) * P):, :]

net = Sequential()  # 建立神经网络
net.add(Dense(input_dim=3, units=10))  # 添加输入层（3节点）到隐藏层（10节点）的连接
# 原文为Dense(input_dim = 3, output_dim = 10)，根据Keras2建议修改为Dense(input_dim=3, units=10)
net.add(Activation('relu'))  # 隐藏层使用relu激活函数
net.add(Dense(input_dim=10, units=1))  # 添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid'))  # 输出层使用sigmoid激活函数
net.compile(loss='binary_crossentropy', optimizer='adam')
# 编译模型，使用adam方法求解，损失函数为交叉熵
# 原文为net.compile(loss = 'binary_crossentropy', optimizer = 'adam', class_mode = "binary")
# 但似乎最新版本KERAS不支持class_mode，会报错，故删除
net.fit(train_data[:, :3], train_data[:, 3], epochs=1000, batch_size=1)  # 训练模型，循环1000次，batch大小为1
# 原文为nb_epoch=1000，根据Keras2建议修改为epochs=1000
lmnetfile_path = '../output/net.model'  # 构建的lm神经网络模型存储路径
net.save_weights(lmnetfile_path)  # 保存模型

predict_result = net.predict_classes(train_data[:, :3]).reshape(len(train_data))  # 预测结果变形
# 这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n

cm_plot(train_data[:, 3], predict_result).show()  # 显示混淆矩阵可视化结果

predict_result = net.predict(test_data[:, :3]).reshape(len(test_data))
fpr, tpr, thresholds = roc_curve(test_data[:, 3], predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')  # 作出ROC曲线
plt.xlabel('False Positive Rate')  # X坐标轴标签
plt.ylabel('True Positive Rate')  # Y坐标轴标签
plt.ylim(0, 1.05)  # X边界范围
plt.xlim(0, 1.05)  # Y边界范围
plt.legend(loc=4)  # 显示标签(label)图例，LOC=4表示位置位于右下方
plt.show()  # 显示作图结果
