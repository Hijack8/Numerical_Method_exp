from numpy import *
import numpy as np
import matplotlib.pyplot as plt
# 定义函数phi0，接受一个参数x，返回常数1
def phi0(x):
    return 1

# 定义函数phi1，接受一个参数x，返回1除以x的结果
def phi1(x):
    # return 1 / np.exp(0.1 * x)
    # return 1 / x ** 0.65
    return 1 / x
# 定义函数phi2，接受一个参数x，返回1除以x的结果
def phi2(x):
    return 1 / x ** 2

# 定义函数f，接受一个参数x，返回数组ys中x-1位置的元素
def f(x):
    return (ys[x - 1])

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

# 定义函数dot，计算两个函数在一系列点上的内积
# f1, f2: 两个函数
# xs: 一系列点的集合
def dot(f1, f2, xs):
    sum = 0  # 初始化求和为0
    for i in xs:
        sum += f1(i) * f2(i)  # 计算每一点上两个函数的乘积，并累加到求和中
    return sum  # 返回最终的点积求和结果

# 定义最小二乘法函数，用于拟合数据
# functions: 基函数以及原函数的集合
# xs: 数据点的x坐标集合
def least_squares(functions, n, xs):

    A = np.zeros((n, n))  # 初始化nxn的零矩阵A
    b = np.zeros((n, 1))  # 初始化nx1的零矩阵b
    # 计算矩阵A的元素
    for i in range(n):
        phi_i = functions["phi" + str(i)]
        b[i][0] = dot(phi_i, functions["f"], xs)
        for j in range(n):
            phi_j = functions["phi" + str(j)]
            A[i][j] = dot(phi_i, phi_j, xs)

    return A, b  # 返回矩阵A和b

# 主函数
def main():
    n = 2
    filename = "fans.txt"  # 定义文件名
    fans = readfile(filename)  # 读取文件内容
    x = [i + 1 for i in range(len(fans))]  # 生成x坐标列表

    global ys  # 声明全局变量ys
    ys = np.array(fans)  # 将fans转换为numpy数组
    xs = np.array(x)  # 将x转换为numpy数组
    functions = {"phi0": phi0, "phi1": phi1, "phi2": phi2, "f": f}

    # 执行最小二乘法拟合
    A, b = least_squares(functions, n, xs)
    c = (np.linalg.inv(A).dot(b))  # 计算系数
    print(c)
    x2 = linspace(1, 100, 1000)  # 生成一个线性空间，用于绘制拟合曲线
    y2 = []
    # 计算拟合曲线的y坐标
    for i in x2:
        y2i = 0
        for j in range(n):
            y2i += c[j][0] * functions["phi"+str(j)](i)
        y2.append(y2i)
    plt.plot(x2, y2)  # 绘制拟合曲线
    plt.plot(x, fans, "+")  # 在相同的图上绘制原始数据点
    plt.show()  # 显示图像

# 当脚本被直接运行时，执行main函数
if __name__ == '__main__':
    main()
