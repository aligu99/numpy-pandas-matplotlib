# 读取酒店数据2.xlsx，根据评分和价格信息，绘制散点图
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx", index_col=0)

x = df["价格"]
y = df["评分"]

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='c', marker='.', s=10, label="评分")
plt.legend()  # 图例
plt.title("酒店价格与评分散点图", fontsize=20)
plt.xlabel("价格", fontsize=18)
plt.ylabel("评分", fontsize=18)
plt.show()
