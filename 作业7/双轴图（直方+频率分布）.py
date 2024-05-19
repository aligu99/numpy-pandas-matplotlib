import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(df['评分'], bins=100, color='m')
# print(n)
# print(bins)
# print(patches)

ax1.set_ylabel("电影数量", fontsize=15)
ax1.set_xlabel("评分", fontsize=15)
ax1.set_title("频率分布图", fontsize=20)

# 拟合
y = norm.pdf(bins, df['评分'].mean(), df['评分'].std())
ax2 = ax1.twinx()
ax2.plot(bins, y, 'b-')
ax2.set_ylabel('概率分布', fontsize=15)
plt.show()
