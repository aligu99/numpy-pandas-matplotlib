import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)
data = df[['投票人数', '评分', '时长']]
# print(data[:5])
result = pd.plotting.scatter_matrix(data[::100], diagonal='kde', color='k', alpha=0.3, figsize=(10, 10))
plt.show()
