import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlim = nl.trans.HardLim()

w = np.array([0.1, 0.1])
p = np.array([0, 0.5]).transpose()
b = np.array([-0.05])

points = [x * 0.1 for x in range(-10, 22, 2)]

x = np.linspace(-1, 2)
y = -(x) + 0.5
plt.plot(x, y)

for pointx in points:
    for pointy in points:
        p_n = np.array([pointx, pointy]).transpose()
        a = hardlim(np.dot(w,p_n)+b)
        if a == 0:
            plt.plot([pointx], [pointy], 'ro')
        else:
            plt.plot([pointx], [pointy], 'bo')
plt.show()
