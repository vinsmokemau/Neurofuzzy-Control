import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlim = nl.trans.HardLim()

w = np.array([[0.75, 0],
              [0.5, -0.5]])

b = np.array([-0.375, -0.25]).transpose()

a1 = np.array([0,0]).transpose()
a2 = np.array([0,1]).transpose()
a3 = np.array([1,0]).transpose()
a4 = np.array([1,1]).transpose()

# plt.axhline(x=0.5, color='b', linestyle='--')
plt.axvline(x=0.5, color='b', linestyle='--')

x = np.linspace(-3, 3)
y = x - 0.5
plt.plot(x, y, 'b', linestyle='--')

points = [x * 0.1 for x in range(-30, 31, 2)]

for pointx in points:
    for pointy in points:
        p = np.array([pointx, pointy]).transpose()
        a = hardlim(np.dot(w,p)+b)
        if np.array_equal(a, a1):
            plt.plot([pointx], [pointy], 'ro')
        elif np.array_equal(a, a2):
            plt.plot([pointx], [pointy], 'bo')
        elif np.array_equal(a, a3):
            plt.plot([pointx], [pointy], 'go')
        else:
            plt.plot([pointx], [pointy], 'yo')
 
plt.show()
