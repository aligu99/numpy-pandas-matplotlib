import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题  
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号  

# 读取数据  
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业6/酒店数据2.xlsx", index_col=0)

# 计算每个地区的平均价格，并排序  
average_price = df.groupby('地区')['价格'].mean().reset_index().sort_values(by='价格', ascending=False)

# 选择平均价格前5个地区的评分数据  
top_5_regions = average_price.head(5)['地区'].tolist()  # 转换为列表
top_5_data = [df[df['地区'] == region]['评分'] for region in top_5_regions]

# 反转地区列表和评分数据列表，以确保最高价格的地区在最上面
top_5_regions_reversed = top_5_regions[::-1]  # 使用切片操作反转列表
top_5_data_reversed = top_5_data[::-1]  # 同样反转评分数据列表

# 绘制箱线图  
plt.figure(figsize=(12, 8))
plt.boxplot(top_5_data_reversed, labels=top_5_regions_reversed, whis=2,
            flierprops={'markersize': 6, 'marker': 'o', 'markerfacecolor': 'red', 'markeredgecolor': 'black',
                        'linewidth': 2}, patch_artist=True,
            boxprops={'linewidth': 1, 'color': 'k', 'facecolor': '#9999ff'},
            vert=False)

# 设置图表背景颜色等属性  
ax = plt.gca()
ax.patch.set_facecolor('grey')
ax.patch.set_edgecolor('grey')
ax.patch.set_alpha(0.3)

# 设置图表标题  
plt.title('酒店评分箱线图', fontweight='bold', fontsize=20)
plt.show()
