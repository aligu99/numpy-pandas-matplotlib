import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\movie_data2.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Series的层次化索引
s = pd.Series(np.arange(1, 10), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 3]])
print(s)
print(s.index)
print(s['a'])  # 外层索引
print(s['a':'c'])  # 切片
print(s[:, 1])  # 内层索引
print(s['c', 3])  # 提取具体的值
print(s.unstack())  # 通过unstack方法可以将Series变成一个DataFrame
#      1    2    3
# a  1.0  2.0  3.0
# b  4.0  5.0  NaN
# c  7.0  NaN  6.0
# d  NaN  8.0  9.0
print(s.unstack().stack())  # 转回
# a  1    1.0
#    2    2.0
#    3    3.0
# b  1    4.0
#    2    5.0
# c  1    7.0
#    3    6.0
# d  2    8.0
#    3    9.0
# dtype: float64

