# -*- coding: utf-8 -*-
"""
建立、训练多层神经网络，并完成模型的检验
由于所给数据量太少，，模型效果很不好
BY HJY
2018-7-20
"""
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout

TRAIN_DATA_PATH = '../data/train_neural_network_data.xls'  # 训练数据
TEST_DATA_PATH = '../data/test_neural_network_data.xls'  # 测试数据
TEST_OUTPUT_PATH = '../output/test_output_data.xls'  # 测试数据模型输出文件
data_train = pd.read_excel(TRAIN_DATA_PATH)  # 读入训练数据(由日志标记事件是否为洗浴)
data_test = pd.read_excel(TEST_DATA_PATH)  # 读入测试数据(由日志标记事件是否为洗浴)
y_train = data_train.iloc[:, 4].values  # 训练样本标签列
x_train = data_train.iloc[:, 5:17].values  # 训练样本特征
y_test = data_test.iloc[:, 4].values  # 测试样本标签列
x_test = data_test.iloc[:, 5:17].values  # 测试样本特征
print(x_train)
model = Sequential()
model.add(Dense(input_dim=11, units=17))  # 添加输入层、隐藏层的连接
model.add(Activation('relu'))  # 以Relu函数为激活函数
model.add(Dense(input_dim=17, units=10))  # 添加隐藏层、隐藏层的连接
model.add(Activation('relu'))  # 以Relu函数为激活函数
model.add(Dense(input_dim=10, units=1))  # 添加隐藏层、输出层的连接
model.add(Activation('sigmoid'))  # 以sigmoid函数为激活函数
# 编译模型，损失函数为binary_crossentropy，用adam法求解
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x_train, y_train, batch_size=1, epochs=500)  # 训练模型,迭代100次，BATCH设置为1
model.save_weights('..\output\model')  # 保存模型参数

r = pd.DataFrame(model.predict_classes(x_test), columns=[u'预测结果'])
pd.concat([data_test.iloc[:,:5],r],axis=1).to_excel(TEST_OUTPUT_PATH)
print(model.predict(x_test))