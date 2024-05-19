import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)

data = pd.cut(df['时长'], [0, 60, 90, 110, 1000]).value_counts()
print(data)
# 时长
# (90, 110]      13201
# (0, 60]         9884
# (60, 90]        7661
# (110, 1000]     7417
# Name: count, dtype: int64
y = data.values
y = y / sum(y)
plt.figure(figsize=(7, 7))
plt.title('电源市场占比', fontsize=20)
explode = (0, 0.1, 0, 0)
patches, l_text, p_text = plt.pie(y, explode=explode, labels=data.index, autopct='%1.1f%%', colors='bgyr',
                                  startangle=90)

for i in p_text:
    i.set_color('white')
    i.set_size('medium')
for i in l_text:
    i.set_color('red')
    i.set_size('large')

plt.legend(loc='upper left')
plt.show()
