import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\movie_data2.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# print(df['年代'].dtype)  # int64
# print(df['投票人数'].dtype)  # int64
# print(df['时长'].dtype)  # int64
# print(df['评分'].dtype)  # float64

# print(df['年代'].unique())
# 选择数值列进行聚合，比如 '评分' 和 '时长'（如果它们是数值类型的话）
# pivot_table = pd.pivot_table(df, index=["年代"], values=['投票人数', '评分', '时长'], aggfunc=np.mean)
# print(pivot_table)

# D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\test3.py:18: FutureWarning: The provided callable
# <function mean at 0x00000243FA919300> is currently using DataFrameGroupBy.mean. In a future version of pandas,
# the provided callable will be used directly. To keep current behavior pass the string "mean" instead.
#   pivot_table = pd.pivot_table(df, index=["年代"], values=['投票人数', '评分', '时长'], aggfunc=np.mean)

aggfunc_dict = {'投票人数': 'sum', '评分': 'mean', '时长': 'mean'}
pivot_table = pd.pivot_table(df, index=["年代"], values=['投票人数', '评分', '时长'], aggfunc=aggfunc_dict)

