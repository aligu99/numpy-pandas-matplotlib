import numpy as np
import pandas as pd

# df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\movie_data2.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 行和列的层次化索引[['a', 'a', 'b', 'b'], [1, 2, 1, 2]]-->[外层],[内层]]
data = pd.DataFrame(np.arange(12).reshape(4, 3), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                    columns=[['A', 'A', 'B'], ['Z', 'X', 'C']])
# print(data)
# print(data['A'])
data.index.names = ['row1', 'row2']
# print(data)
data.columns.names = ['col1', 'col2']
# print(data)

# swaplevel 函数并不直接修改DataFrame的索引，而是返回一个新的索引，你需要将这个新的索引重新赋值给DataFrame。
data.index = data.index.swaplevel('row1', 'row2')
print(data)
