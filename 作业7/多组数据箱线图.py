import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)
data1 = df[df.产地 == '中国大陆']['评分']
data2 = df[df.产地 == '日本']['评分']
data3 = df[df.产地 == '中国香港']['评分']
data4 = df[df.产地 == '英国']['评分']
data5 = df[df.产地 == '法国']['评分']

plt.figure(figsize=(12, 8))
plt.boxplot([data1, data2, data3, data4, data5], labels=['中国大陆', '日本', '中国香港', '英国', '法国'], whis=2,
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'markeredgecolor': 'black', 'linewidth': 2},
            patch_artist=True, boxprops={'linewidth': 2, 'color': 'k', 'facecolor': '#9999ff'},
            vert=False)

ax = plt.gca()
ax.patch.set_facecolor('grey')
ax.patch.set_alpha(0.3)

plt.title('电影评分箱线图', fontsize=20)
plt.show()
