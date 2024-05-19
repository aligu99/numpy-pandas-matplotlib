import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\movie_data2.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# print(df.index)
# set_index可以把列变成索引
df = df.set_index(['产地', '年代'])
df = df.swaplevel('产地', '年代')  # 需要一个参数接收df.swaplevel()的返回值
df = df.loc[1994]
df = df.reset_index()  # 取消层次化索引
print(df[:5])
