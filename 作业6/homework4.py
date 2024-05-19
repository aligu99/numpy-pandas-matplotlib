# 画出每个价格等级酒店数量的柱状图。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx")
data = df['等级'].value_counts()

x = data.index
y = data.values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='red')
plt.title('每个价格等级酒店数量', fontweight='bold', fontsize=18)
plt.xlabel('等级', fontweight='bold', fontsize=16)
plt.ylabel('酒店数量', fontweight='bold', fontsize=16)
for a, b in zip(x, y):
    plt.text(a, b + 1, str(b), ha='center', va='bottom', fontweight='bold', fontsize=10)
plt.show()
