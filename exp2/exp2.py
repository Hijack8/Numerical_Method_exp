from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c

def readfile(filename):
    fans = []

    with open("fans.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            fans.append(int(line))
    return fans

def main():
    filename = "fans.txt"
    fans = readfile(filename)
    x = [i + 1 for i in range(len(fans))]
    ys = np.array(fans)
    xs = np.array(x)

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

if __name__ == '__main__':
    main()


