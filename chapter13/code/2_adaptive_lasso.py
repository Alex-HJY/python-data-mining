#-*- coding: utf-8 -*-
"""
LASSO回归选择变量
BY HJY
2018-7-23
"""
import pandas as pd
#导入LASSO模块，书中使用ADAPTIVE LASSO 但是最新版本SKLEARN库已将这个函数删去
from sklearn.linear_model import Lasso

INPUT_FILE_PATH='../data/data1.csv' #输入的数据文件
data=pd.read_csv(INPUT_FILE_PATH)

model=Lasso(alpha=500,max_iter=10000)
model.fit(data.iloc[:,0:13],data['y'])
print(model.coef_) #获得各个特征的系数
