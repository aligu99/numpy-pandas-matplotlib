import numpy as np
import pandas as pd

df = pd.read_excel(r'D:\Pycharm-beginner\数据分析_numpy＆pandas\python\作业4\酒店数据1.xlsx', index_col=0)

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# （1）读取上次作业保存的数据，酒店数据1.xlsx
print(df.head())

# （2）将“类型”和“名字”设置为层次化索引，并交换索引的位置。然后将层次化索引取消。
df = df.set_index(["类型", "名字"])
print(df[:10])
#                                                          城市   地区                      地点   评分   评分人数    价格
# 类型   名字
# 浪漫情侣 香港铜锣湾皇悦酒店(Empire Hotel Hong Kong-Causeway Bay)      香港   东区                铜锣湾永兴街8号  4.5  12708   693
# 商务出行 香港碧荟酒店(The BEACON)                                  香港  油尖旺              九龙旺角洗衣街88号  4.7    328   747
# 浪漫情侣 香港湾仔帝盛酒店(Dorsett Wanchai)                           香港   湾仔           皇后大道东387-397号  4.4   5014   693
#      如心艾朗酒店(L‘hotel elan)                                香港   观塘                观塘创业街38号  4.6   3427   581
#      香港隆堡柏宁顿酒店(Hotel Pennington by Rhombus)              香港   湾仔           铜锣湾边宁顿街13-15号  4.5   1938   869
# 海滨风光 海景嘉福洲际酒店(InterContinental Grand Stanford Hong K...  香港  油尖旺             尖沙咀東部麽地道70号  4.7   4366  1296
#      香港怡东酒店(Excelsior Hotel)                             香港   湾仔             铜锣湾告士打道281号  4.6   6961  1184
# 休闲度假 香港富豪九龙酒店(Regal Kowloon Hotel)                       香港  油尖旺               尖沙嘴麽地道71号  4.5  11265   692
# 海滨风光 港岛香格里拉大酒店(Island Shangri-La)                        香港  中西区             金钟中区法院道太古广场  4.8   4182  2836
# 地铁周边 香港广易商务宾馆(家庭旅馆)(WIDE EVER HOSTEL)                    香港  油尖旺  九龙旺角弥敦道607号新兴大厦14楼16单位  4.1   1029   218

df = df.swaplevel('名字', '类型')
print(df[:10])
#                                                          城市   地区                      地点   评分   评分人数    价格
# 名字                                                 类型
# 香港铜锣湾皇悦酒店(Empire Hotel Hong Kong-Causeway Bay)     浪漫情侣  香港   东区                铜锣湾永兴街8号  4.5  12708   693
# 香港碧荟酒店(The BEACON)                                 商务出行  香港  油尖旺              九龙旺角洗衣街88号  4.7    328   747
# 香港湾仔帝盛酒店(Dorsett Wanchai)                          浪漫情侣  香港   湾仔           皇后大道东387-397号  4.4   5014   693
# 如心艾朗酒店(L‘hotel elan)                               浪漫情侣  香港   观塘                观塘创业街38号  4.6   3427   581
# 香港隆堡柏宁顿酒店(Hotel Pennington by Rhombus)             浪漫情侣  香港   湾仔           铜锣湾边宁顿街13-15号  4.5   1938   869
# 海景嘉福洲际酒店(InterContinental Grand Stanford Hong K... 海滨风光  香港  油尖旺             尖沙咀東部麽地道70号  4.7   4366  1296
# 香港怡东酒店(Excelsior Hotel)                            海滨风光  香港   湾仔             铜锣湾告士打道281号  4.6   6961  1184
# 香港富豪九龙酒店(Regal Kowloon Hotel)                      休闲度假  香港  油尖旺               尖沙嘴麽地道71号  4.5  11265   692
# 港岛香格里拉大酒店(Island Shangri-La)                       海滨风光  香港  中西区             金钟中区法院道太古广场  4.8   4182  2836
# 香港广易商务宾馆(家庭旅馆)(WIDE EVER HOSTEL)                   地铁周边  香港  油尖旺  九龙旺角弥敦道607号新兴大厦14楼16单位  4.1   1029   218
df = df.reset_index()
print(df[:10])
#                                                   名字    类型  城市   地区                      地点   评分   评分人数    价格
# 0     香港铜锣湾皇悦酒店(Empire Hotel Hong Kong-Causeway Bay)  浪漫情侣  香港   东区                铜锣湾永兴街8号  4.5  12708   693
# 1                                 香港碧荟酒店(The BEACON)  商务出行  香港  油尖旺              九龙旺角洗衣街88号  4.7    328   747
# 2                          香港湾仔帝盛酒店(Dorsett Wanchai)  浪漫情侣  香港   湾仔           皇后大道东387-397号  4.4   5014   693
# 3                               如心艾朗酒店(L‘hotel elan)  浪漫情侣  香港   观塘                观塘创业街38号  4.6   3427   581
# 4             香港隆堡柏宁顿酒店(Hotel Pennington by Rhombus)  浪漫情侣  香港   湾仔           铜锣湾边宁顿街13-15号  4.5   1938   869
# 5  海景嘉福洲际酒店(InterContinental Grand Stanford Hong ...  海滨风光  香港  油尖旺             尖沙咀東部麽地道70号  4.7   4366  1296
# 6                            香港怡东酒店(Excelsior Hotel)  海滨风光  香港   湾仔             铜锣湾告士打道281号  4.6   6961  1184
# 7                      香港富豪九龙酒店(Regal Kowloon Hotel)  休闲度假  香港  油尖旺               尖沙嘴麽地道71号  4.5  11265   692
# 8                       港岛香格里拉大酒店(Island Shangri-La)  海滨风光  香港  中西区             金钟中区法院道太古广场  4.8   4182  2836
# 9                   香港广易商务宾馆(家庭旅馆)(WIDE EVER HOSTEL)  地铁周边  香港  油尖旺  九龙旺角弥敦道607号新兴大厦14楼16单位  4.1   1029   218

# （3）将数据集转置，获取转置后的index和columns。
df = df.T
print(df)
# 名字……
# 类型……
# 城市……
# 地区……
# 地点……
# 评分……
# 评分人数……
# 价格……
# print(df.index)
# print(df.columns)
# Index(['名字', '类型', '城市', '地区', '地点', '评分', '评分人数', '价格'], dtype='object')
# Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
#        ...
#        386, 387, 388, 389, 390, 391, 392, 393, 394, 395],
#       dtype='int64', length=396)

# （4）用Groupby方法来计算每个地区的评分人数的总和以及均值。
print(df.评分人数.groupby(df['地区']).sum())
print(df.评分人数.groupby(df['地区']).mean())
print(df['评分人数'].groupby(df['地区']).agg(['sum', 'mean']))
#          sum          mean
# 地区
# 东区     56643   3540.187500
# 中西区    59682   1808.545455
# 九龙城    49855   2374.047619
# 元朗      1200   1200.000000
# 其他地区   16831    300.553571
# 南区     12867   2573.400000
# 屯门      7324   3662.000000
# 沙田     39622   9905.500000
# 油尖旺   422574   2284.183784
# 深水埗区      16     16.000000
# 湾仔    107344   2618.146341
# 离岛     60359   5487.181818
# 罗湖区       24     24.000000
# 荃湾    114610  16372.857143
# 葵青     11544   2308.800000
# 观塘     19137   2733.857143

# （5）用Grouby方法计算每个类型的平均价格，最高价和最低价。
print(df['价格'].groupby(df['类型']).agg(['mean', 'max', 'min']))
#               mean    max  min
# 类型
# 交通方便    421.000000    421  421
# 亲子酒店    745.400000   1686  269
# 休闲度假   1151.300000   4443  358
# 其他类型    269.300000    881   67
# 印象好     297.000000    297  297
# 商务出行   1045.153846   3159  401
# 地铁周边    374.139535   2640   67
# 大学周边    325.000000    325  325
# 客栈      397.666667    553  245
# 干净卫生    185.000000    185  185
# 民宿      258.500000    506  157
# 浪漫情侣    608.573529   1908  225
# 海滨风光   1543.573770  12926  331
# 火车站周边   968.000000    968  968
# 环境不错    357.666667    484  176
# 老板热情    385.000000    385  385
# 酒店公寓   1182.000000   2309  588
# 青年旅舍    189.250000    348   70

# （6）数据离散化，按照价格将酒店分为3个等级,0-500为C，500-1000为B,大于1000为A，列名设置为“价格等级”。
df["价格等级"] = pd.cut(df["价格"], bins=[0, 500, 1000, 12926], labels=['C', 'B', 'A'])
print(df[:6])
#                                                   名字    类型  城市   地区             地点   评分   评分人数    价格 价格等级
# 0     香港铜锣湾皇悦酒店(Empire Hotel Hong Kong-Causeway Bay)  浪漫情侣  香港   东区       铜锣湾永兴街8号  4.5  12708   693    B
# 1                                 香港碧荟酒店(The BEACON)  商务出行  香港  油尖旺     九龙旺角洗衣街88号  4.7    328   747    B
# 2                          香港湾仔帝盛酒店(Dorsett Wanchai)  浪漫情侣  香港   湾仔  皇后大道东387-397号  4.4   5014   693    B
# 3                               如心艾朗酒店(L‘hotel elan)  浪漫情侣  香港   观塘       观塘创业街38号  4.6   3427   581    B
# 4             香港隆堡柏宁顿酒店(Hotel Pennington by Rhombus)  浪漫情侣  香港   湾仔  铜锣湾边宁顿街13-15号  4.5   1938   869    B
# 5  海景嘉福洲际酒店(InterContinental Grand Stanford Hong ...  海滨风光  香港  油尖旺    尖沙咀東部麽地道70号  4.7   4366  1296    A

# （7）获取评分均值最高和最低的地区的数据，分别使用append和concat方法将获取的两个数据集合并。
print(df['评分'].groupby(df['地区']).agg(['mean']))
#           mean
# 地区
# 东区    4.480186
# 中西区   4.548485
# 九龙城   4.428571
# 元朗    4.500000
# 其他地区  4.184117
# 南区    4.220000
# 屯门    4.600000
# 沙田    4.575000
# 油尖旺   4.194663
# 深水埗区  4.300000
# 湾仔    4.375610
# 离岛    4.371179
# 罗湖区   4.282973
# 荃湾    4.442857
# 葵青    4.040000
# 观塘    4.500000
print(df['评分'].groupby(df['地区']).agg(['mean']).sort_values('mean', ascending=False))
#           mean
# 地区
# 屯门    4.600000
# 沙田    4.575000
# 中西区   4.548485
# 元朗    4.500000
# 观塘    4.500000
# 东区    4.480186
# 荃湾    4.442857
# 九龙城   4.428571
# 湾仔    4.375610
# 离岛    4.371179
# 深水埗区  4.300000
# 罗湖区   4.282973
# 南区    4.220000
# 油尖旺   4.194663
# 其他地区  4.184117
# 葵青    4.040000

# 评分均值最高和最低的地区分别是屯门和葵青
print(df[df['地区'] == '屯门'])
#                                            名字    类型  城市  地区             地点   评分  评分人数   价格
# 24       香港黄金海岸酒店(Hong Kong Gold Coast Hotel)  海滨风光  香港  屯门  屯门 黄金海岸青山公路1号  4.7  6326  696
# 168  香港屯门贝尔特酒店(pentahotel Hong Kong Tuen Mun)  浪漫情侣  香港  屯门      新界屯门震寰路六号  4.5   998  582

print(df[df['地区'] == '葵青'])
#                                         名字    类型  城市  地区           地点   评分  评分人数   价格
# 42          香港荃湾旭逸酒店(Hotel Ease Tsuen Wan)  浪漫情侣  香港  葵青  葵涌圳边街15-19号  4.4   598  394
# 199             香港永倫800酒店(WINLAND800HOTEL)  其他类型  香港  葵青      新界青衣路一号  3.4  3098  196
# 200            香港青逸酒店(Rambler Oasis Hotel)  浪漫情侣  香港  葵青        青衣路1号  4.0  3091  349
# 213           香港华逸酒店(Rambler Garden Hotel)  浪漫情侣  香港  葵青     青衣 青衣路1号  4.0  3031  349
# 215  香港文化旅馆-翠雅山房(Hong Kong Heritage Lodge)  浪漫情侣  香港  葵青  香港九龙青山道800号  4.4  1726  423

df_tunmen = df[df.地区 == "屯门"]
df_kuiqing = df[df.地区 == "葵青"]
print(df_kuiqing._append(df_tunmen))
print(pd.concat([df_tunmen, df_kuiqing], axis=0, ignore_index=True))
#                                          名字    类型  城市  地区             地点   评分  评分人数   价格
# 0      香港黄金海岸酒店(Hong Kong Gold Coast Hotel)  海滨风光  香港  屯门  屯门 黄金海岸青山公路1号  4.7  6326  696
# 1  香港屯门贝尔特酒店(pentahotel Hong Kong Tuen Mun)  浪漫情侣  香港  屯门      新界屯门震寰路六号  4.5   998  582
# 2            香港荃湾旭逸酒店(Hotel Ease Tsuen Wan)  浪漫情侣  香港  葵青    葵涌圳边街15-19号  4.4   598  394
# 3                香港永倫800酒店(WINLAND800HOTEL)  其他类型  香港  葵青        新界青衣路一号  3.4  3098  196
# 4               香港青逸酒店(Rambler Oasis Hotel)  浪漫情侣  香港  葵青          青衣路1号  4.0  3091  349
# 5              香港华逸酒店(Rambler Garden Hotel)  浪漫情侣  香港  葵青       青衣 青衣路1号  4.0  3031  349
# 6     香港文化旅馆-翠雅山房(Hong Kong Heritage Lodge)  浪漫情侣  香港  葵青    香港九龙青山道800号  4.4  1726  423

# （8）数据离散化，按照评分人数将酒店平均分为3个等级，三个等级的酒店数量尽量保持一致。评分人数最多的为A，最少的为C。列名设置为“热门等级”。
bins = np.percentile(df["评分人数"], [0, 33, 66, 100])  # 获取分位数
df['热门等级'] = pd.cut(df['评分人数'], bins, labels=['C', 'B', 'A'])
print(df[:6])

# （9）选出评分人数为A，价格也为A的酒店数据，计算其平均评分。
df["价格等级"] = pd.cut(df["价格"], bins=[0, 500, 1000, 12926], labels=['C', 'B', 'A'])
bins = np.percentile(df["评分人数"], [0, 33, 66, 100])  # 获取分位数
df['热门等级'] = pd.cut(df['评分人数'], bins, labels=['C', 'B', 'A'])
print(df[(df.热门等级 == 'A') & (df.价格等级 == 'A')][:6])
#                                                    名字    类型  城市   地区           地点   评分   评分人数    价格 价格等级 热门等级
# 5   海景嘉福洲际酒店(InterContinental Grand Stanford Hong ...  海滨风光  香港  油尖旺  尖沙咀東部麽地道70号  4.7   4366  1296    A    A
# 6                             香港怡东酒店(Excelsior Hotel)  海滨风光  香港   湾仔  铜锣湾告士打道281号  4.6   6961  1184    A    A
# 8                        港岛香格里拉大酒店(Island Shangri-La)  海滨风光  香港  中西区  金钟中区法院道太古广场  4.8   4182  2836    A    A
# 10   香港铜锣湾皇冠假日酒店(Crowne Plaza Hong Kong Causeway Bay)  休闲度假  香港   湾仔     铜锣湾礼顿道八号  4.7   4446  1633    A    A
# 13                      香港朗廷酒店(The Langham Hong Kong)  休闲度假  香港  油尖旺     尖沙嘴北京道8号  4.7  11039  1899    A    A
# 14                 迪士尼探索家度假酒店(Disney Explorers Lodge)  海滨风光  香港   离岛     迪士尼乐园度假区  4.8   4794  1662    A    A
# print(df[(df.热门等级 == 'A') & (df.价格等级 == 'A')]['评分'].mean())  # 4.66

# （10）取价格最高的5个酒店的数据，使用stack和unstack方法实现dataframe和Series之间的转换。
print(df.sort_values(by="价格", ascending=False)[:5].stack())
# 116  名字               香港四季酒店(Four Seasons Hotel Hong Kong)
#      类型                                               海滨风光
#      城市                                                 香港
#      地区                                                中西区
#      地点                                           中环 金融街8号
#      评分                                                4.8
#      评分人数                                             3461
#      价格                                              12926
# 115  名字      香港置地文华东方酒店(The Landmark Mandarin Oriental HK)
#      类型                                               休闲度假
#      城市                                                 香港
#      地区                                                中西区
#      地点                                    中环 皇后大道中15号置地广场
#      评分                                                4.8
#      评分人数                                             1285
#      价格                                               4443
# 88   名字                                奕居(The Upper House)
#      类型                                               海滨风光
#      城市                                                 香港
#      地区                                                中西区
#      地点                                         金钟道88号太古广场
#      评分                                                4.8
#      评分人数                                             1369
#      价格                                               4356
# 82   名字                    香港半岛酒店(The Peninsula Hong Kong)
#      类型                                               海滨风光
#      城市                                                 香港
#      地区                                                油尖旺
#      地点                                           尖沙咀梳士巴利道
#      评分                                                4.8
#      评分人数                                             3693
#      价格                                               3862
# 18   名字              香港文华东方酒店(Mandarin Oriental Hong Kong)
#      类型                                               海滨风光
#      城市                                                 香港
#      地区                                                中西区
#      地点                                           中环干诺道中5号
#      评分                                                4.8
#      评分人数                                             2452
#      价格                                               3609
# dtype: object
print(df.sort_values(by="价格", ascending=False)[:5].stack().unstack())
#                                                 名字    类型  城市   地区               地点   评分  评分人数     价格
# 116           香港四季酒店(Four Seasons Hotel Hong Kong)  海滨风光  香港  中西区         中环 金融街8号  4.8  3461  12926
# 115  香港置地文华东方酒店(The Landmark Mandarin Oriental HK)  休闲度假  香港  中西区  中环 皇后大道中15号置地广场  4.8  1285   4443
# 88                             奕居(The Upper House)  海滨风光  香港  中西区       金钟道88号太古广场  4.8  1369   4356
# 82                 香港半岛酒店(The Peninsula Hong Kong)  海滨风光  香港  油尖旺         尖沙咀梳士巴利道  4.8  3693   3862
# 18           香港文华东方酒店(Mandarin Oriental Hong Kong)  海滨风光  香港  中西区         中环干诺道中5号  4.8  2452   3609

# （11）纵向拆分数据集，分为df1和df2，df1包含名字，类型，城市，地区，df2包含名字，地点，评分，评分人数，价格，价格等级，热门等级。
df["价格等级"] = pd.cut(df["价格"], bins=[0, 500, 1000, 12926], labels=['C', 'B', 'A'])
bins = np.percentile(df["评分人数"], [0, 33, 66, 100])  # 获取分位数
df['热门等级'] = pd.cut(df['评分人数'], bins, labels=['C', 'B', 'A'])
df1 = df[['名字', '类型', '城市', '地区']]
df2 = df[['名字', '地点', '评分', '评分人数', '价格', '价格等级', '热门等级']]
print(df1)
print(df2)

# （12）将df2按照价格进行排序，重新设置df2的索引。索引值等于价格排名。
df["价格等级"] = pd.cut(df["价格"], bins=[0, 500, 1000, 12926], labels=['C', 'B', 'A'])
bins = np.percentile(df["评分人数"], [0, 33, 66, 100])  # 获取分位数
df['热门等级'] = pd.cut(df['评分人数'], bins, labels=['C', 'B', 'A'])
df2 = df[['名字', '地点', '评分', '评分人数', '价格', '价格等级', '热门等级']]
df2 = df2.sort_values(by='价格', ascending=False, ignore_index=True)
print(df2[:5])
#                                               名字               地点   评分  评分人数     价格 价格等级 热门等级
# 0           香港四季酒店(Four Seasons Hotel Hong Kong)         中环 金融街8号  4.8  3461  12926    A    A
# 1  香港置地文华东方酒店(The Landmark Mandarin Oriental HK)  中环 皇后大道中15号置地广场  4.8  1285   4443    A    B
# 2                            奕居(The Upper House)       金钟道88号太古广场  4.8  1369   4356    A    B
# 3                香港半岛酒店(The Peninsula Hong Kong)         尖沙咀梳士巴利道  4.8  3693   3862    A    A
# 4          香港文华东方酒店(Mandarin Oriental Hong Kong)         中环干诺道中5号  4.8  2452   3609    A    A

# （13）使用merge方法将df1和df2合并
df["价格等级"] = pd.cut(df["价格"], bins=[0, 500, 1000, 12926], labels=['C', 'B', 'A'])
bins = np.percentile(df["评分人数"], [0, 33, 66, 100])  # 获取分位数
df['热门等级'] = pd.cut(df['评分人数'], bins, labels=['C', 'B', 'A'])
df1 = df[['名字', '类型', '城市', '地区']]
df2 = df[['名字', '地点', '评分', '评分人数', '价格', '价格等级', '热门等级']]
df = pd.merge(df1, df2, how="inner", on="名字")
print(df)

# （14）将合并后的数据集保存数据到“酒店数据2.xlsx”。
df["价格等级"] = pd.cut(df["价格"], bins=[0, 500, 1000, 12926], labels=['C', 'B', 'A'])
bins = np.percentile(df["评分人数"], [0, 33, 66, 100])  # 获取分位数
df['热门等级'] = pd.cut(df['评分人数'], bins, labels=['C', 'B', 'A'])
df1 = df[['名字', '类型', '城市', '地区']]
df2 = df[['名字', '地点', '评分', '评分人数', '价格', '价格等级', '热门等级']]
df = pd.merge(df1, df2, how="inner", on="名字")
df.to_excel("酒店数据2.xlsx")
