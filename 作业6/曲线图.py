import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # 关闭一些可能出现但对数据分析并无影响的警告
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)
# print(df[:5])
data = df['年代'].value_counts()
data = data.sort_index()[:-2]
x = data.index
y = data.values
plt.figure(figsize=(12, 8))
plt.plot(x, y, color='blue')
plt.title("每年电影数量", fontsize=20)
plt.ylabel("电影数量", fontsize=18)
plt.xlabel("年份", fontsize=18)

for (a, b) in zip(x[::10], y[::10]):  # 每隔10年进行数量标记，防止过于密集
    plt.text(a, b + 10, b, ha="center", va="bottom", fontsize=10)

# 标记特殊点如极值点，xy设置箭头尖的坐标，xytext注释内容起始位置，arrowprops对箭头设置，传字典，facecolor填充颜色，edgecolor边框颜色
plt.annotate("2012年达到最大值", xy=(2012, data[2012]), xytext=(2020, 2040),
             arrowprops=dict(facecolor="black", edgecolor="red"))

# 纯文本注释内容，例如注释增长最快的地方
plt.text(1980, 1000, "电影数量开始快速增长")
plt.show()
