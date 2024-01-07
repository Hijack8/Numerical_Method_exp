from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义一个函数模型，用于曲线拟合
# x: 独立变量
# a, b, c: 模型参数
def func(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c

# 定义函数readfile，用于从文件中读取数据
# filename: 文件名
def readfile(filename):
    fans = []  # 初始化一个空列表，用于存储读取的数据

    # 打开文件并按行读取
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            fans.append(int(line))  # 将每行数据转换为整数并添加到列表中
    return fans  # 返回读取的数据列表

# 定义主函数
def main():
    filename = "fans.txt"  # 定义文件名
    fans = readfile(filename)  # 读取文件内容
    x = [i + 1 for i in range(len(fans))]  # 生成x坐标列表
    ys = np.array(fans)  # 将fans转换为numpy数组
    xs = np.array(x)  # 将x转换为numpy数组

    # 使用curve_fit函数进行曲线拟合
    popt, pcov = curve_fit(func, xs, ys)
    # 打印拟合得到的参数a, b, c
    print("a = " + str(popt[0]))
    print("b = " + str(popt[1]))
    print("c = " + str(popt[2]))

    x2 = linspace(1, 100, 1000)  # 生成一个线性空间，用于绘制拟合曲线
    y2 = [func(i, popt[0], popt[1], popt[2]) for i in x2]  # 计算拟合曲线的y坐标
    plt.plot(x2, y2)  # 绘制拟合曲线
    plt.plot(x, fans, "+")  # 在相同的图上绘制原始数据点
    plt.show()  # 显示图像

# 当脚本被直接运行时，执行main函数
if __name__ == '__main__':
    main()


