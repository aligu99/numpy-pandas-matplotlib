# 画出各个价格等级占比的饼图。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx")
data = df['等级'].value_counts()
y = data.values
y = y / sum(y)

plt.figure(figsize=(7, 7))
plt.title('各个价格等级占比', fontsize=15)
patches, l_text, p_text = plt.pie(y, labels=data.index, autopct='%1.1f%%', colors=('blue', 'green', 'red'),
                                  startangle=90)
for i in l_text:
    i.set_color('red')
    i.set_size(15)
for i in p_text:
    i.set_color('white')
    i.set_size(15)
plt.axis('equal')
plt.legend()
plt.show()
