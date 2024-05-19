# # 绘制一个评分，评分人数和价格之间的热力图
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx", index_col=0)

data = df[['评分人数', '评分', '价格']]

corr = data.corr()
corr = abs(corr)  # 相关系数绝对值

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

sns.heatmap(corr, vmax=1, vmin=0, annot=True, annot_kws={"size": 13, 'weight': 'bold'}, linewidths=0.05)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()
