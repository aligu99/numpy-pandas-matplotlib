import numpy as np

# 创建一个1到10的数组，然后逆序输出。
# a = np.arange(1, 11)
# print(a[::-1])  # [10  9  8  7  6  5  4  3  2  1]

# 创建一个长度为20的全是1的数组，然后变成一个4×5的二维矩阵并转置。
# b = np.ones(20)
# print(b.astype(int))  # [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
# print(b.reshape(4, 5))
# # [[1. 1. 1. 1. 1.]
# #  [1. 1. 1. 1. 1.]
# #  [1. 1. 1. 1. 1.]
# #  [1. 1. 1. 1. 1.]]

# # 创建一个3x3x3的随机数组。 (提示: np.random.random)
# a = np.random.random((3, 3, 3))
# print(a)

# # 从1到10中随机选取10个数，构成一个长度为10的数组，并将其排序。获取其最大值最小值，求和，求方差。
# a = np.random.randint(1, 10, 10)
# b = sorted(a)
# print(b)
# print(max(a))
# print(min(a))
# print(sum(a))
# print(np.std(a))

# 从1到10中随机选取10个数，构成一个长度为10的数组，选出其中的奇数。
# a = np.random.randint(1, 11, 10)
# print(a[np.where(a % 2 == 1)])
# print(a[a % 2 == 1])
#
# # 生成0到100，差为5的一个等差数列，然后将数据类型转化为整数。
# a = np.linspace(start=0, stop=100, num=21)
# b = np.arange(start=0, stop=100, step=5, dtype=np.int64)
# print(a)
# print(b)

# # 从1到10中随机选取10个数，大于3和小于8的取负数。
# a = np.random.randint(1, 10, size=10)
# a[np.logical_and(a > 3, a < 8)] *= -1
# print(a)

# # 从1到10中随机选取10个数，大于3和小于8的取负数。
# a = np.random.randint(1, 10, 10)
# # a[np.where((a > 3) & (a < 8))] = a[np.where((a > 3) & (a < 8))] * -1
# # print(a)
# # a[(a > 3) & (a < 8)] = a[(a > 3) & (a < 8)] * -1
# # print(a)

# # 在数组[1, 2, 3, 4, 5]中相邻两个数字中间插入1个0。
# a = np.array([1, 2, 3, 4, 5])
# b = np.zeros(9)
# b[::2] = a
# print(b)

# # 新建一个5乘5的随机二维数组，交换其中两行？比如交换第一二行。
# a = np.random.randint(1, 10, 25)
# b = a.reshape(5, 5)
# print(b)
# b = b[[1, 0, 2, 3, 4]]
# print(b)

# 把一个10*2的随机生成的笛卡尔坐标转换成极坐标。

# # 创建一个长度为10并且除了第五个值为1其余的值为2的向量。
# a = np.random.randint(1, 10, 10)
# a.fill(2)
# a[4] = 1
# print(a)

# # 创建一个长度为10的随机向量，并求其累计和。
# a = np.random.randint(1, 10, 10)
# print(a.sum())

# # 将数组中的所有奇数替换成-1。
# a = np.random.randint(1, 10, 10)
# print(a)
# a[np.where(a % 2 == 1)] = -1
# print(a)

# # 构造两个4乘3的二维数组，按照3种方法进行连接
# a = np.random.randint(1, 10, 12).reshape(4, 3)
# b = np.random.randint(1, 10, 12).reshape(4, 3)
# print(a)
# print(b)
# print(np.vstack((a, b)))
# print(np.dstack((a, b)))
# print(np.hstack((a, b)))

# # 获取数组 a 和 b 中的共同项（索引位置相同，值也相同）。 a = np.array([1,2,3,2,3,4,3,4,5,6])，b = np.array([7,2,10,2,7,4,9,4,9,8])
# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# print(a[np.asanyarray(a == b)])

# 从数组 a 中提取 5 和 10 之间的所有项。a=np.array([7,2,10,2,7,4,9,4,9,8])
a = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(a[np.where((a > 5) & (a < 10))])
