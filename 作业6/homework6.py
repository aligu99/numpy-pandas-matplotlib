# 画出酒店评分的直方图。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx")

data = df['评分'].value_counts()
x = data.index
y = data.values

plt.figure(figsize=(10, 6))
plt.hist(df['评分'], bins=20, edgecolor='black', alpha=0.5)
plt.title('酒店评分直方图', fontweight='bold', fontsize=18)
plt.xlabel('评分', fontweight='bold', fontsize=16)
plt.ylabel('评分个数', fontweight='bold', fontsize=16)
plt.show()
