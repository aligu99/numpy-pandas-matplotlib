import pandas as pd

# （1）用字典数据类型创建DataFrame。 data={'state':['a','b','c','d'], 'year':[1991,1992,1993,1994], 'pop':[6,7,8,9]}
data = pd.DataFrame({'state': ['a', 'b', 'c', 'd'], 'year': [1991, 1992, 1993, 1994], 'pop': [6, 7, 8, 9]})
# print(data)
#   state  year  pop
# 0     a  1991    6
# 1     b  1992    7
# 2     c  1993    8
# 3     d  1994    9

# （2）将创建的Dataframe的索引设置为，ABCD。并且命名为“索引”。
data.index = list(['A', 'B', 'C', 'D'])
data.index.name = '索引'
# print(data)
#    state  year  pop
# 索引
# A      a  1991    6
# B      b  1992    7
# C      c  1993    8
# D      d  1994    9

# （3）在下面新增一行。然后删除。
add_rows = {'state': 'e', 'year': 1995, 'pop': 10}
data_new = pd.DataFrame(add_rows, index=['E'])
data_add = pd.concat([data, data_new], axis=0, ignore_index=False)
# print(data_add)
#   state  year  pop
# A     a  1991    6
# B     b  1992    7
# C     c  1993    8
# D     d  1994    9
# E     e  1995   10
data_add = data_add.drop(['E'], axis=0)
# print(data_add)
#   state  year  pop
# 0     a  1991    6
# 1     b  1992    7
# 2     c  1993    8
# 3     d  1994    9

# （4）增加新的属性列，列名设置为‘port’，值均为1。
data_add['port'] = 1
# print(data_add)
#   state  year  pop  port
# A     a  1991    6     1
# B     b  1992    7     1
# C     c  1993    8     1
# D     d  1994    9     1

# （5）取出1991和1994年的数据。
# print(data_add.iloc[['A', 'D']])  # 左闭右开取不了A
# print(data_add.loc[['A', 'D']])
#   state  year  pop  port
# A     a  1991    6     1
# D     d  1994    9     1

# （6）获取前‘state’和‘year’的数据。
# print(data_add[['state', 'year']])
#   state  year
# A     a  1991
# B     b  1992
# C     c  1993
# D     d  1994

# （7）查看每一列数据的数据格式，并且将‘pop’每个数据乘2。
# print(data_add.dtypes)
# state    object
# year      int64
# pop       int64
# port      int64
# dtype: object

data_add['pop'] = data_add['pop'] * 2
# print(data_add)
#   state  year  pop  port
# A     a  1991   12     1
# B     b  1992   14     1
# C     c  1993   16     1
# D     d  1994   18     1
