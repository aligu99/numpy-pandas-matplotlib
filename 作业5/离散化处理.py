import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\movie_data2.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df['评分等级'] = pd.cut(x=df['评分'], bins=[0, 3, 5, 7, 9, 10], labels=['E', 'D', 'C', 'B', 'A'])
# print(df[:100])

bins = np.percentile(df['投票人数'], [0, 20, 40, 60, 80, 100])
# [2.10000e+01 8.00000e+01 2.06000e+02 6.36000e+02 2.83800e+03 6.92795e+05]

df['热门程度'] = pd.cut(x=df['投票人数'], labels=['E', 'D', 'C', 'B', 'A'], bins=bins)
df = df[(df.热门程度 == 'E') & (df.评分等级 == 'A')]
print(df)

