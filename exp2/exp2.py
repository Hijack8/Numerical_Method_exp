import matplotlib.pyplot as plt

fans=[]

with open("fans.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        fans.append(int(line))

x = [i for i in range(len(fans))]
plt.plot(x, fans)
plt.show()
