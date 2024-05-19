# 绘制一个评分，评分人数和价格之间的相关系数图
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx", index_col=0)
data = df[['评分人数', '评分', '价格']]

result = pd.plotting.scatter_matrix(data, diagonal='kde', alpha=0.3, figsize=(10, 10), marker='p', color='k')
plt.show()
