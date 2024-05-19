# 画出$y=x^{2}+2x+1$在区间[-5,3]的函数图像。
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字符乱码的问题
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

t = np.linspace(-5.0, 3.0, 100)
plt.figure(figsize=(8, 6))
plt.plot(t, t * t + 2 * t + 1, 'b--')
plt.grid(True)
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.plot([-1, -1], [-1, 16], 'r--')
plt.show()
