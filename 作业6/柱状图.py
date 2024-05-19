import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # 关闭一些可能出现但对数据分析并无影响的警告
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
df = pd.read_excel(r"D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业5/movie_data3.xlsx", index_col=0)
# print(df[:5])
data = df['产地'].value_counts()
# print(data.index)
# Index(['美国', '日本', '中国大陆', '中国香港', '法国', '英国', '其他', '韩国', '德国', '意大利', '加拿大',
#        '中国台湾', '俄罗斯', '西班牙', '印度', '澳大利亚', '泰国', '丹麦', '瑞典', '波兰', '荷兰', '比利时',
#        '墨西哥', '阿根廷', '巴西'],
#       dtype='object', name='产地')
x = data.index
y = data.values
plt.figure(figsize=(10, 8))  # 设置图片大小
plt.bar(x, y, color="g")  # 绘制柱状图，表格给的数据是怎样就怎样，不会自动排序
# plt.savefig('picture.png')
plt.title("各国家或地区电影数量", fontsize=20)  # 设置标题
plt.xlabel("国家或地区", fontsize=18)
plt.ylabel("电影数量")  # 对横纵轴进行说明
plt.tick_params(labelsize=14)  # 设置标签字体大小
plt.xticks(rotation=90)  # 标签转90度

for a, b in zip(x, y):  # 数字直接显示在柱子上（添加文本）
    # a:x的位置，b:y的位置，加上10是为了展示位置高一点点不重合，
    # 第二个b:显示的文本的内容,ha,va:格式设定,center居中,top&bottom在上或者在下,fontsize:字体指定
    plt.text(a, b + 10, b, ha="center", va="bottom", fontsize=10)

# plt.grid()  # 画网格线，有失美观因而注释点

plt.show()
