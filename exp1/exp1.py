import csv
import numpy as np
import math
import matplotlib.pyplot as plt

x_list = []
y_list = []

# read CSV file
def read_csv(filename):

    x_list = []
    y_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if( not row[0].isdigit()):
                continue
            x_list.append(int(row[0]))
            y_list.append(float(row[1]))
    return x_list, y_list

def solve_eq(a, b, c, d, n):
    # LU decomposition
    mu = [0] * (n + 1)
    l = [0] * (n + 1)
    mu[1] = b[1]
    for i in range(2, n + 1):
        l[i] = a[i] / mu[i - 1]
        mu[i] = b[i] - l[i] * c[i - 1]
    # chasing
    y = [0] * (n + 1)
    x = [0] * (n + 1)
    y[1] = d[1]
    for i in range(2, n + 1):
        y[i] = d[i] - l[i] * y[i - 1]

    x[n] = y[n] / mu[n]
    for i in range(n - 1, 0, -1):
        x[i] = (y[i] - c[i] * x[i + 1]) / mu[i]
    return x

def f(x, M, h):
    n = len(x_list) -1
    i = 0
    for j in range(1, n + 1):
        if(x <= x_list[j]):
            i = j
            break
    return M[i - 1] * ((x_list[i] - x) ** 3 ) / (6 * h[i]) + \
        M[i] * ( (x - x_list[i - 1]) ** 3 ) / (6 * h[i]) + \
        (y_list[i - 1] - M[i - 1] * h[i] * h[i] / 6) * (x_list[i] - x) / h[i] + \
        (y_list[i] - M[i] * h[i] * h[i] / 6) * (x - x_list[i - 1]) / h[i]

def plot_this_func(M, h):
    x = np.arange(x_list[0], x_list[-1], 0.1)
    print(x)
    y = []

    for t in x:
        y_1 = f(t, M, h)
        y.append(y_1)
    plt.plot(x, y, label="cubic spline interpolation")
    plt.plot(x_list, y_list, '+', label="initial points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def cal_length(M, h):
    x = np.arange(x_list[0], x_list[-1], 0.01)
    s = 0
    print(len(x))
    for i in range(1, len(x)):
        s += math.sqrt((f(x[i - 1], M, h) - f(x[i], M, h)) ** 2 + 0.01 ** 2)
    return s

def main():
    filename = 'sea2023.csv'
    global x_list, y_list
    x_list, y_list = read_csv(filename)

    # n+1 dots
    n = len(x_list) - 1

    h = [0] * (n + 1)
    d = [0] * (n + 1)
    C = [0] * (n + 1)
    lam = [0] * (n + 1)
    mu = [0] * (n + 1)
    # cal h
    for i in range(1, n + 1):
        h[i] = x_list[i] - x_list[i - 1]
    # cal d C lambda mu
    for i in range(1, n):
        d[i] = 6 * ( (y_list[i + 1] - y_list[i]) / h[i + 1] - (y_list[i] - y_list[i - 1]) / h[i]) / (h[i] + h[i + 1])
        C[i] = 2
        lam[i] = h[i + 1] / (h[i] + h[i + 1])
        mu[i] = 1 - lam[i]
    C[n] = 2
    # if M0=0 and Mn=0 solve this equations
    M = solve_eq(mu, C, lam, d, n - 1)
    M.append(0) # Mn=0
    print(cal_length(M, h))
    plot_this_func(M, h)


if __name__ == '__main__':
    main()

