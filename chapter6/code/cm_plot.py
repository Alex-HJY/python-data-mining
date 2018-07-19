# -*- coding: utf-8 -*-
'''
混淆矩阵作图函数
By HJY
2018-7-18
'''
import numpy as np
def cm_plot(y, yp):
    '''
    混淆矩阵作图函数
    :param y: 实际结果
    :param yp: 模型输出结果
    :return:
    '''
    from sklearn.metrics import confusion_matrix  # 导入混淆矩阵函数
    import matplotlib.pyplot as plt  # 导入作图库

    cm = confusion_matrix(y, yp)  # 混淆矩阵，实际上返回为array类
    plt.matshow(cm, cmap=plt.cm.Greens)  # 通过.matshow方法传入一个矩阵，画混淆矩阵图，cmap为配色风格，使用cm.Greens，更多风格请参考官网。
    plt.colorbar()  # 显示颜色数值条
    for x in range(len(cm)):  # 在图中显示数值。xy为坐标，显示方式为居中
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')  # X坐标轴标签
    plt.xlabel('Predicted label')  # Y坐标轴标签
    return plt
