import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业5\movie_data3.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# _append(),append()有误
# df_usa = df[df.产地 == '美国']
# df_china = df[df.产地 == '中国大陆']
# # 使用concat函数代替append
# df_combined = df_usa._append(df_china)
# df_combined.to_excel('movie_data4.xlsx')

# # merge
# df1 = df.loc[:5]
# df2 = df.loc[:5][['名字', '产地']]
# df2["票房"] = [123344, 23454, 55556, 333, 6666, 444]
# df2 = df2.sample(frac=1)
# df2.index = range(len(df2))
# df_merge = pd.merge(df1, df2, how='inner', on='名字')
# print(df_merge)

# concat
df1 = df[:10]
df2 = df[100:110]
df3 = df[200:210]
df_concat = pd.concat([df1, df2, df3], axis=0)
print(df_concat)
