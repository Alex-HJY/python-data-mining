# -*- coding: utf-8 -*-
"""
线性回归预测
BY HJY
2018-7-23
"""
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import matplotlib.pyplot as plt

INPUT_FILE_PATH = '../output/data1_GM11.xls'  # 灰色预测后保存的路径
OUTPUT_FILE_PATH = '../data/revenue.xls'  # 神经网络预测后保存的结果
MODEL_FILE_PATH = '../output/1-net.model'  # 模型保存路径
data = pd.read_excel(INPUT_FILE_PATH)  # 读取数据
feature = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']  # 特征所在列

data_train = data.loc[range(1994, 2014)].copy()  # 取2014年前的数据建模
data_mean = data_train.mean()
data_std = data_train.std()
data_train = (data_train - data_mean) / data_std  # 数据标准化
x_train = data_train[feature].values  # 特征数据
y_train = data_train['y'].values  # 标签数据

model = Sequential()
model.add(Dense(input_dim=6, units=12))
model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(input_dim=12, units=1))
model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型，损失函数为均方误差
model.fit(x_train, y_train, epochs=10000, batch_size=16, )  # 训练模型，学习一万次
model.save_weights(MODEL_FILE_PATH)  # 保存模型参数

x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
data.to_excel(OUTPUT_FILE_PATH)

# 画出预测结果图
p = data[['y', 'y_pred']].plot(subplots=False, style=['b-o', 'r-*'])  # 显示在一张图内更直观
plt.show()
