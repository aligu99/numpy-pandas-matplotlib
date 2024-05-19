import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)

x = df["时长"][::100]
y = df["评分"][::100]  # 解决数据冗杂的问题

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='c', marker='p', label="评分")
plt.legend()  # 图例
plt.title("电影时长与评分散点图", fontsize=20)
plt.xlabel("时长", fontsize=18)
plt.ylabel("评分", fontsize=18)
plt.show()
