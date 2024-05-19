# 在同一张图中创建两个子图，分别画出sinx和cosx在[-3.14,3.14]上的函数图像。设置线条宽度为2.5.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

x = np.linspace(-np.pi, np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sqrt(x)

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(x, y1, linewidth=2.5, color='r')

plt.subplot(2, 1, 2)
plt.plot(x, y2, linewidth=2.5, color='g')

plt.show()
