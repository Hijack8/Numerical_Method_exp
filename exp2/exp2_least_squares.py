from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def phi0(x):
    return 1
def phi1(x):
    return 1 / x

def f(x):
    return ys[x - 1]

def readfile(filename):
    fans = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            fans.append(int(line))
    return fans

def dot(f1, f2, xs):
    sum = 0
    for i in xs:
        sum += f1(i) * f2(i)
    return sum

def least_squares(phi0, phi1, xs):
    A = np.zeros((2, 2))
    A[0][0] = dot(phi0, phi0, xs)
    A[0][1] = dot(phi0, phi1, xs)
    A[1][0] = dot(phi1, phi0, xs)
    A[1][1] = dot(phi1, phi1, xs)

    b = np.zeros((2, 1))
    b[0][0] = dot(phi0, f, xs)
    b[1][0] = dot(phi1, f, xs)

    return A, b

def main():
    filename = "fans.txt"
    fans = readfile(filename)
    x = [i + 1 for i in range(len(fans))]

    global ys
    ys = np.array(fans)
    xs = np.array(x)

    A, b = least_squares(phi0, phi1, xs)
    c = (np.linalg.inv(A).dot(b))

    x2 = linspace(1, 100, 1000)
    y2 = [c[0][0] * phi0(i) + c[1][0] * phi1(i) for i in x2]
    plt.plot(x2, y2)
    plt.plot(x, fans, "+")
    plt.show()

if __name__ == '__main__':
    main()


