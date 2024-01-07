import csv
import numpy as np
import math
import matplotlib.pyplot as plt

# 全局列表用于存储 CSV 数据
x_list = []
y_list = []

# 读取 CSV 文件并返回 x 和 y 值列表
def read_csv(filename):
    x_list = []
    y_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # 忽略非数字的行
            if not row[0].isdigit():
                continue
            x_list.append(int(row[0]))
            y_list.append(float(row[1]))
    return x_list, y_list

# 使用 LU 分解和追赶法解三对角矩阵
def solve_eq(a, b, c, d, n):
    mu = [0] * (n + 1)
    l = [0] * (n + 1)
    # 初始化
    mu[1] = b[1]
    for i in range(2, n + 1):
        l[i] = a[i] / mu[i - 1]
        mu[i] = b[i] - l[i] * c[i - 1]
    # 追赶法求解
    y = [0] * (n + 1)
    x = [0] * (n + 1)
    y[1] = d[1]
    for i in range(2, n + 1):
        y[i] = d[i] - l[i] * y[i - 1]
    x[n] = y[n] / mu[n]
    for i in range(n - 1, 0, -1):
        x[i] = (y[i] - c[i] * x[i + 1]) / mu[i]
    return x

# 三次样条插值函数
def f(x, M, h):
    n = len(x_list) - 1
    i = 0
    # 查找 x 所在的区间
    for j in range(1, n + 1):
        if x <= x_list[j]:
            i = j
            break
    # 计算插值
    return M[i - 1] * ((x_list[i] - x) ** 3 ) / (6 * h[i]) + \
           M[i] * ((x - x_list[i - 1]) ** 3 ) / (6 * h[i]) + \
           (y_list[i - 1] - M[i - 1] * h[i] * h[i] / 6) * (x_list[i] - x) / h[i] + \
           (y_list[i] - M[i] * h[i] * h[i] / 6) * (x - x_list[i - 1]) / h[i]

# 绘制三次样条插值曲线和原始数据点
def plot_this_func(M, h, len):
    x = np.arange(x_list[0], x_list[-1], 0.1)
    y = []

    for t in x:
        y_1 = f(t, M, h)
        y.append(y_1)
    plt.plot(x, y, label="cubic spline interpolation")
    plt.plot(x_list, y_list, '+', label="initial points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Cubic spline interpolation curve(Curve length =" + str(len) + ")")
    plt.legend()
    plt.show()

# 计算三次样条插值曲线的长度
def cal_length(M, h):
    x = np.arange(x_list[0], x_list[-1], 0.01)
    s = 0
    for i in range(1, len(x)):
        s += math.sqrt((f(x[i - 1], M, h) - f(x[i], M, h)) ** 2 + 0.01 ** 2)
    return s

# 主函数
def main():
    filename = 'sea2023.csv'
    global x_list, y_list
    x_list, y_list = read_csv(filename)

    n = len(x_list) - 1

    # 初始化 h, d, C, lambda, mu 数组
    h = [0] * (n + 1)
    d = [0] * (n + 1)
    C = [0] * (n + 1)
    lam = [0] * (n + 1)
    mu = [0] * (n + 1)

    # 计算 h, d, C, lambda, mu
    for i in range(1, n + 1):
        h[i] = x_list[i] - x_list[i - 1]
    for i in range(1, n):
        d[i] = 6 * ((y_list[i + 1] - y_list[i]) / h[i + 1] - (y_list[i] - y_list[i - 1]) / h[i]) / (h[i] + h[i + 1])
        C[i] = 2
        lam[i] = h[i + 1] / (h[i] + h[i + 1])
        mu[i] = 1 - lam[i]
    C[n] = 2

    # 求解 M
    M = solve_eq(mu, C, lam, d, n - 1)
    M.append(0)  # Mn=0

    # 计算插值曲线长度并绘制图形
    # print(cal_length(M, h))
    length = cal_length(M, h)
    plot_this_func(M, h, length)

if __name__ == '__main__':
    main()
