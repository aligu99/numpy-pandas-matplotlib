# 画出每个热门等级酒店评分均值的柱状图。（按照评分均值从小到大排序。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx")
average_ratings = df.groupby('等级')['评分'].mean().reset_index()
x = average_ratings['等级']
y = average_ratings['评分']

plt.figure(figsize=(10, 6))
plt.bar(x, y, width=0.5, color='red')
plt.title('每个热门等级酒店评分平均值', fontweight='bold', fontsize=18)
plt.xlabel('等级', fontweight='bold', fontsize=18)
plt.ylabel('评分均值', fontweight='bold', fontsize=18)
for a, b in zip(x, y):
    plt.text(a, b + 0.01, str(round(b, 1)), ha='center', va='bottom', fontweight='bold', fontsize=10)
plt.show()
