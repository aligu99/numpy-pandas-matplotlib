import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\movie_data2.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# aggfunc_dict = {'投票人数': 'sum', '评分': 'mean', '时长': 'mean'}
# pivot_table = pd.pivot_table(df, index=["年代"], values=['投票人数', '评分', '时长'], aggfunc=aggfunc_dict)
# print(pivot_table)

# 双索引
# aggfunc_dict = {'投票人数': 'sum', '评分': 'mean', '时长': 'mean'}
# pivot_table = pd.pivot_table(df, index=['年代', '产地'], values=['投票人数', '评分', '时长'], aggfunc=aggfunc_dict,
#                              fill_value=0, margins=True)
# print(pivot_table)

# pivot_table = pd.pivot_table(df, index=['年代'], values=['投票人数', '评分'],
#                              aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0, margins=True)
# print(pivot_table)

# pivot_table = pd.pivot_table(df, index=['年代'], values=['投票人数', '评分'],
#                              aggfunc={'投票人数': np.sum, '评分': np.mean}, fill_value=0, margins=True)
# print(pivot_table.sort_values('评分', ascending=False))
# print(pivot_table[pivot_table.index == 1994])

pivot_table = pd.pivot_table(df, index=["产地", "年代"], values=["投票人数", "评分"],
                             aggfunc={"投票人数": np.sum, "评分": np.mean},
                             fill_value=0)
print(pivot_table)
