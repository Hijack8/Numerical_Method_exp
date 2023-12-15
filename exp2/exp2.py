from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# 生成e指数函数
def func(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c
## 绘制散点图和拟合曲线
def m_plot(x, y, x1, y1, err):
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(x, y, label='实际票房')
    plt.scatter(x, err, marker='x', label='误差')
    plt.plot(x1, y1, label='预测曲线')
    plt.title("累计票房散点图,拟合曲线,误差")
    plt.legend()
    plt.show()

def residuals(p, x, y):
    fun = np.poly1d(p)
    return y - fun(x)

## 计算2-范数误差
def res2_cal(y1, y2):
    return np.sqrt(np.power(y1 - y2, 2))

if __name__ == '__main__':
    fans = []

    with open("fans.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            fans.append(int(line))

    x = [i + 1 for i in range(len(fans))]
    plt.plot(x, fans, "+")
    plt.show()
    n = 8  # 多项式最高次数
    ys = np.array(fans)
    xs = np.array(x)
    # 设置初始参数估计和参数边界
    # initial_guess = [1.0, 1.0, 1.0]  # 示例初始猜测
    # bounds = (0, [np.inf, np.inf, np.inf])  # 设置参数的边界
    # 使用指数拟合
    popt, pcov = curve_fit(func, xs, ys)
    # popt数组中，三个值分别是待求参数a,b,c
    print("a = " + str(popt[0]))
    print("b = " + str(popt[1]))
    print("c = " + str(popt[2]))
    x2 = linspace(1, 100, 1000)
    y2 = [func(i, popt[0],popt[1],popt[2]) for i in x2]
    plt.plot(x2, y2)
    plt.plot(x, fans, "+")
    plt.show()


