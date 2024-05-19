import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)
data = df[df.产地 == '美国']['评分']

plt.figure(figsize=(10, 6))
plt.boxplot(data, whis=2,
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'markeredgecolor': 'black', 'linewidth': 2},
            patch_artist=True, boxprops={'linewidth': 2, 'alpha': 0.5, 'color': 'k', 'facecolor': '#9999ff'})
plt.title('美国电影评分', fontsize=20)
plt.show()
