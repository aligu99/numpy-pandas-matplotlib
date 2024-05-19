import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业3\movie_data.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df.drop([31644], inplace=True)
df.drop([32949], inplace=True)
df.loc[[14934, 15205], "年代"] = 2008
df['时长'] = df['时长'].astype('int')
df["年代"] = df["年代"].astype("int")
# print(df.sort_values(by=['年代', '投票人数'], ascending=False)[:20])
df.drop(df[df["年代"] > 2018].index, inplace=True)
df.drop(df[df["时长"] > 1000].index, inplace=True)
df.index = range(len(df))
df.to_excel("movie_data_fix.xlsx")
