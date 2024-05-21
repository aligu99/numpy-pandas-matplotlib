import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\酒店数据1.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# （1）读取上次作业保存的数据，酒店数据1.xlsx
print(df.head())

# （2）查看“评分”的格式，并分别进行升序和降序排序
print(df['评分'].dtype)  # float64
print(df.sort_values('评分', ascending=False)[:5])
print(df.sort_values('评分', ascending=True)[:5])

# （3）对酒店按照价格进行排名，计算“油尖旺”地区的均价。
df.sort_values('价格', ascending=True)
print(df[df.地区 == '油尖旺']['价格'].mean())  # 544.3621621621621

# （4）对酒店数据进行描述性统计，并求所有价格的均值方差，最大最小值，中值。
print(df.describe())
# #                评分          评分人数            价格
# # count  396.000000    396.000000    396.000000
# # mean     4.285536   2473.818182    682.315657
# # std      0.484353   4508.745613    907.334845
# # min      1.500000      1.000000     67.000000
# # 25%      4.200000     95.500000    246.750000
# # 50%      4.400000    866.500000    416.500000
# # 75%      4.600000   3247.000000    766.000000
# # max      4.900000  45463.000000  12926.000000
print(df['价格'].mean())
print(df['价格'].var())
print(df['价格'].max())
print(df['价格'].min())
print(df['价格'].median())
# 682.3156565656566
# 823256.5203618463
# 12926
# 67
# 416.5

# （5）计算评分和价格之间的的相关系数，协方差
print(df[['评分', '价格']].corr())
print(df[['评分', '价格']].cov())
#           评分        价格
# 评分  1.000000  0.288901
# 价格  0.288901  1.000000
#             评分             价格
# 评分    0.234598     126.963415
# 价格  126.963415  823256.520362

# （6）按照评分降序排序，评分相同时按价格升序排序。
print(df.sort_values(by=['评分', '价格'], ascending=[False, True]))

# （7）计算一下，评分小于3分的酒店数量和占比。
print(df[df.评分 < 3])
print(len(df[df.评分 < 3]))  #
print(len(df[df.评分 < 3])/len(df))  # 0.030303030303030304

# （8）计算一下，酒店评分大于等于4分的酒店的价格均值。
print(df[df.评分 >= 4]['价格'].mean())  # 743.165191740413

# （9）计算出每个地区的酒店占总酒店数量的比例。
print(df.地区.value_counts()/len(df))
# 地区
# 油尖旺     0.467172
# 其他地区    0.141414
# 湾仔      0.103535
# 中西区     0.083333
# 九龙城     0.053030
# 东区      0.040404
# 离岛      0.027778
# 观塘      0.017677
# 荃湾      0.017677
# 南区      0.012626
# 葵青      0.012626
# 沙田      0.010101
# 屯门      0.005051
# 元朗      0.002525
# 深水埗区    0.002525
# 罗湖区     0.002525
# Name: count, dtype: float64

# （10）找出酒店评分人数排名前20的酒店，并计算他们的价格均值。
print(df.sort_values(by=['评分人数'], ascending=False)[:20])
print(df.sort_values(by=['评分人数'], ascending=False)[:20]['价格'].mean())  # 1111.8

# （11）查看酒店分布的类型数量和地区数量，并统计各个类型和地区包含的酒店数量。
print(len(df.类型.unique()))  # 18
print(len(df.地区.unique()))  # 16
print(df.类型.unique())
# ['浪漫情侣' '商务出行' '海滨风光' '休闲度假' '地铁周边' '交通方便' '亲子酒店' '其他类型' '民宿' '印象好' '酒店公寓'
#  '青年旅舍' '客栈' '火车站周边' '老板热情' '环境不错' '干净卫生' '大学周边']
print(df.地区.unique())
# ['东区' '油尖旺' '湾仔' '观塘' '中西区' '南区' '离岛' '九龙城' '荃湾' '屯门' '葵青' '其他地区' '沙田'
#  '元朗' '深水埗区' '罗湖区']
print(df.地区.value_counts())
# 地区
# 油尖旺     185
# 其他地区     56
# 湾仔       41
# 中西区      33
# 九龙城      21
# 东区       16
# 离岛       11
# 观塘        7
# 荃湾        7
# 南区        5
# 葵青        5
# 沙田        4
# 屯门        2
# 元朗        1
# 深水埗区      1
# 罗湖区       1
# Name: count, dtype: int64
print(df.地区.value_counts())
# 地区
# 油尖旺     185
# 其他地区     56
# 湾仔       41
# 中西区      33
# 九龙城      21
# 东区       16
# 离岛       11
# 观塘        7
# 荃湾        7
# 南区        5
# 葵青        5
# 沙田        4
# 屯门        2
# 元朗        1
# 深水埗区      1
# 罗湖区       1
# Name: count, dtype: int64

# （12）用数据透视表，计算每个类型的酒店的评分人数总数量。
print(pd.pivot_table(df, index=['类型'], values=['评分人数'], aggfunc='sum'))
#          评分人数
# 类型
# 交通方便      152
# 亲子酒店    11492
# 休闲度假   219657
# 其他类型     4858
# 印象好        68
# 商务出行     9630
# 地铁周边    91323
# 大学周边       23
# 客栈        229
# 干净卫生      146
# 民宿       2493
# 浪漫情侣   238436
# 海滨风光   394600
# 火车站周边     578
# 环境不错     1327
# 老板热情       48
# 酒店公寓     1967
# 青年旅舍     2605

# （13）用数据透视表，计算每个类型的酒店价格的均值和标准差
print(pd.pivot_table(df, index=['类型'], values=['价格'], aggfunc=['mean', 'std']))
#               mean          std
#                 价格           价格
# 类型
# 交通方便    421.000000          NaN
# 亲子酒店    745.400000   546.616227
# 休闲度假   1151.300000   831.027704
# 其他类型    269.300000   199.264727
# 印象好     297.000000          NaN
# 商务出行   1045.153846   870.595663
# 地铁周边    374.139535   377.604830
# 大学周边    325.000000          NaN
# 客栈      397.666667   154.017315
# 干净卫生    185.000000          NaN
# 民宿      258.500000   127.000394
# 浪漫情侣    608.573529   303.356119
# 海滨风光   1543.573770  1746.828349
# 火车站周边   968.000000          NaN
# 环境不错    357.666667   161.283394
# 老板热情    385.000000          NaN
# 酒店公寓   1182.000000   697.624899
# 青年旅舍    189.250000   116.851401

# （14）用数据透视表，计算每个地区酒店价格和评分的最大值和最小值
print(pd.pivot_table(df, index=['地区', '类型'], values=['价格', '评分'], aggfunc=['max', 'min']))
#               max             min
#                价格        评分    价格        评分
# 地区   类型
# 东区   其他类型     567  4.600000   567  4.600000
#      商务出行     637  4.500000   581  4.500000
#      客栈       553  4.282973   553  4.282973
#      浪漫情侣    1908  4.500000   407  4.200000
#      海滨风光    1408  4.700000   331  4.200000
# 中西区  亲子酒店    1686  4.600000  1686  4.600000
#      休闲度假    4443  4.800000   614  4.500000
#      商务出行    3159  4.700000   468  4.400000
#      地铁周边    2640  4.600000   254  3.800000
#      浪漫情侣     636  4.500000   436  4.000000
#      海滨风光   12926  4.800000   396  4.500000
#      酒店公寓    2309  4.600000  1394  4.300000
# 九龙城  亲子酒店     269  4.100000   269  4.100000
#      休闲度假    1583  4.600000   426  4.300000
#      其他类型     369  3.700000   369  3.700000
#      地铁周边     909  4.800000   137  4.200000
#      浪漫情侣     737  4.600000   225  4.000000
#      海滨风光    1742  4.700000  1403  4.700000
#      环境不错     484  4.200000   484  4.200000
# 元朗   浪漫情侣     425  4.500000   425  4.500000
# 其他地区 其他类型     298  4.700000    67  2.000000
#      印象好      297  4.700000   297  4.700000
#      地铁周边    1450  4.700000    75  2.300000
#      大学周边     325  4.500000   325  4.500000
#      客栈       245  4.700000   245  4.700000
#      民宿       264  4.800000   181  4.300000
#      浪漫情侣     245  4.700000   245  4.700000
#      环境不错     176  4.500000   176  4.500000
# 南区   休闲度假     447  4.400000   447  4.400000
#      其他类型     259  3.800000   259  3.800000
#      干净卫生     185  4.300000   185  4.300000
#      浪漫情侣     553  4.400000   377  4.200000
# 屯门   浪漫情侣     582  4.500000   582  4.500000
#      海滨风光     696  4.700000   696  4.700000
# 沙田   休闲度假    1052  4.600000   569  4.400000
#      海滨风光     997  4.700000   997  4.700000
# 油尖旺  交通方便     421  4.600000   421  4.600000
#      亲子酒店     676  4.600000   567  4.600000
#      休闲度假    2342  4.700000   548  4.500000
#      其他类型     445  4.800000    70  3.100000
#      商务出行     747  4.700000   401  4.100000
#      地铁周边    1520  4.900000    67  1.500000
#      客栈       395  4.900000   395  4.900000
#      浪漫情侣    1161  4.700000   237  4.100000
#      海滨风光    3862  4.800000   536  4.500000
#      火车站周边    968  4.600000   968  4.600000
#      酒店公寓     784  4.400000   588  4.100000
#      青年旅舍     348  4.700000    70  4.000000
# 深水埗区 地铁周边     648  4.300000   648  4.300000
# 湾仔   亲子酒店     529  4.400000   529  4.400000
#      休闲度假    1731  4.700000   469  4.400000
#      商务出行    1006  4.600000   566  4.400000
#      地铁周边    1662  4.600000   131  3.400000
#      民宿       157  3.700000   157  3.700000
#      浪漫情侣    1349  4.700000   309  4.200000
#      海滨风光    2856  4.700000   756  4.400000
#      老板热情     385  4.400000   385  4.400000
#      酒店公寓     835  4.300000   835  4.300000
# 离岛   休闲度假    1667  4.500000   768  4.300000
#      其他类型     881  4.282973   352  2.900000
#      海滨风光    1662  4.800000   527  4.200000
#      环境不错     413  4.400000   413  4.400000
# 罗湖区  民宿       506  4.282973   506  4.282973
# 荃湾   休闲度假     358  4.500000   358  4.500000
#      浪漫情侣     370  4.400000   225  4.300000
#      海滨风光     709  4.500000   418  4.400000
# 葵青   其他类型     196  3.400000   196  3.400000
#      浪漫情侣     423  4.400000   349  4.000000
# 观塘   休闲度假    1132  4.600000   654  4.600000
#      其他类型     448  4.200000   448  4.200000
#      浪漫情侣     595  4.600000   581  4.500000
#      海滨风光     736  4.600000   484  4.400000

# （15）用数据透视表，计算每个地区和类型的酒店的评分的均值和标准差
print(pd.pivot_table(df, index=['地区', '类型'], values=['评分'], aggfunc=['mean', 'std']))
#                 mean       std
#                   评分        评分
# 地区   类型
# 东区   其他类型   4.600000       NaN
#      商务出行   4.500000  0.000000
#      客栈     4.282973       NaN
#      浪漫情侣   4.425000  0.150000
#      海滨风光   4.512500  0.155265
# 中西区  亲子酒店   4.600000       NaN
#      休闲度假   4.650000  0.212132
#      商务出行   4.540000  0.114018
#      地铁周边   4.400000  0.339116
#      浪漫情侣   4.325000  0.236291
#      海滨风光   4.664286  0.108182
#      酒店公寓   4.450000  0.212132
# 九龙城  亲子酒店   4.100000       NaN
#      休闲度假   4.480000  0.130384
#      其他类型   3.700000       NaN
#      地铁周边   4.516667  0.231661
#      浪漫情侣   4.350000  0.251661
#      海滨风光   4.700000  0.000000
#      环境不错   4.200000       NaN
# 元朗   浪漫情侣   4.500000       NaN
# 其他地区 其他类型   4.044204  0.786834
#      印象好    4.700000       NaN
#      地铁周边   4.121387  0.506469
#      大学周边   4.500000       NaN
#      客栈     4.700000       NaN
#      民宿     4.550000  0.208167
#      浪漫情侣   4.700000       NaN
#      环境不错   4.500000       NaN
# 南区   休闲度假   4.400000       NaN
#      其他类型   3.800000       NaN
#      干净卫生   4.300000       NaN
#      浪漫情侣   4.300000  0.141421
# 屯门   浪漫情侣   4.500000       NaN
#      海滨风光   4.700000       NaN
# 沙田   休闲度假   4.533333  0.115470
#      海滨风光   4.700000       NaN
# 油尖旺  交通方便   4.600000       NaN
#      亲子酒店   4.600000  0.000000
#      休闲度假   4.633333  0.086603
#      其他类型   4.220743  0.779992
#      商务出行   4.400000  0.424264
#      地铁周边   4.002033  0.617022
#      客栈     4.900000       NaN
#      浪漫情侣   4.414286  0.155669
#      海滨风光   4.638889  0.091644
#      火车站周边  4.600000       NaN
#      酒店公寓   4.250000  0.212132
#      青年旅舍   4.375000  0.330404
# 深水埗区 地铁周边   4.300000       NaN
# 湾仔   亲子酒店   4.400000       NaN
#      休闲度假   4.560000  0.114018
#      商务出行   4.500000  0.115470
#      地铁周边   4.077778  0.432371
#      民宿     3.700000       NaN
#      浪漫情侣   4.446667  0.135576
#      海滨风光   4.600000  0.141421
#      老板热情   4.400000       NaN
#      酒店公寓   4.300000       NaN
# 离岛   休闲度假   4.400000  0.141421
#      其他类型   3.591486  0.977910
#      海滨风光   4.616667  0.213698
#      环境不错   4.400000       NaN
# 罗湖区  民宿     4.282973       NaN
# 荃湾   休闲度假   4.500000       NaN
#      浪漫情侣   4.350000  0.070711
#      海滨风光   4.475000  0.050000
# 葵青   其他类型   3.400000       NaN
#      浪漫情侣   4.200000  0.230940
# 观塘   休闲度假   4.600000  0.000000
#      其他类型   4.200000       NaN
#      浪漫情侣   4.550000  0.070711
#      海滨风光   4.500000  0.141421
