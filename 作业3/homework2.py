import pandas as pd

# 设置Pandas显示选项，确保所有数据都能显示
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# （1）读取香港酒店数据。
df = pd.read_excel(r'D:/Pycharm-beginner/数据分析_numpy＆pandas/python/作业3/香港酒店数据.xlsx')
# print(df.head())
#    Unnamed: 0                                             字段1   字段2  字段3  字段4            字段5  字段6      字段7    字段8
# 0         NaN                                             NaN   NaN  NaN  NaN            NaN  NaN      NaN    NaN
# 1         0.0             香港嘉湖海逸酒店(Harbour Plaza Resort City)  休闲度假   香港   元朗     天水围 天恩路18号  4.6  17604.0  422.0
# 2         1.0  香港铜锣湾皇悦酒店(Empire Hotel Hong Kong-Causeway Bay)  浪漫情侣   香港   东区       铜锣湾永兴街8号  4.5  12708.0  693.0
# 3         2.0                              香港碧荟酒店(The BEACON)  商务出行   香港  油尖旺     九龙旺角洗衣街88号  4.7    328.0  747.0
# 4         3.0                       香港湾仔帝盛酒店(Dorsett Wanchai)  浪漫情侣   香港   湾仔  皇后大道东387-397号  4.4   5014.0  693.0

# （2）按照数据的内容，重新设置数据的索引，重新设置列名称为'名字','类型','城市','地区','地点','评分','评分人数','价格'。
df.index = range(1, len(df) + 1)
df.columns = ['索引', '名字', '类型', '城市', '地区', '地点', '评分', '评分人数', '价格']
# print(df)

# （3）查看所有类型为“浪漫情侣”的酒店
# print(df[df.类型 == '浪漫情侣'])

# （4）查看所有类型为“浪漫情侣”，地区在湾仔的酒店
# print(df[(df.类型 == '浪漫情侣') & (df.地区 == '湾仔')])

# （5）查看所有地址在观塘或者油尖旺，评分大于4的酒店
# print(df[(df.地区 == '观塘') | (df.地区 == '油尖旺') & (df.评分 > 4)])

# （6）查看类型缺失的数据
# print(df[df.类型.isnull()])

# （7）用“其他”填充类型和地区
df.类型.fillna('其他', inplace=True)  # inplace意为直接在原始数据中进行修改
df.地区.fillna('其他', inplace=True)
# print(df)

# （8）用评分均值填充缺失值

