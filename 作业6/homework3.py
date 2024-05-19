# 读取上次作业保存的酒店数据，画出每个地区酒店数量的柱状图，柱状颜色为红色
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx")
data = df['地区'].value_counts()
x = data.index
y = data.values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='red')
plt.title('每个地区酒店数量', fontweight='bold', fontsize=18)
plt.xlabel('地区', fontweight='bold', fontsize=16)
plt.ylabel('酒店数量', fontweight='bold', fontsize=16)
plt.xticks(rotation=45)
for a, b in zip(x, y):
    plt.text(a, b + 1, str(b), ha='center', va='bottom', fontweight='bold', fontsize=10)
plt.show()
