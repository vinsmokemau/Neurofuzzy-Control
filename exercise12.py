import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlims = nl.trans.HardLims()

w1 = np.array([[1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1],
               [1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1]]).transpose()

b1 = np.array([-2, 3, 0.5, 0.5, -1.75, -2.25, -3.25, 3.75, 6.25, -5.75, -4.75]).transpose()

w2 = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],])
b2 = np.array([-3 -3 -3 -3]).transpose()

w3 = np.array([1, 1, 1, 1])
b3 = np.array([3])

points = [x * 0.1 for x in range(0, 61)]

for pointx in points:
    for pointy in points:
        p = np.array([pointx, pointy]).transpose()
        a1 = hardlims(np.dot(w1, p) + b1)
        a2 = hardlims(np.dot(w2, a1.transpose()) + b2)
        a3 = hardlims(np.dot(w3, a2) + b3)
        if a3 == 1:
            plt.plot([pointx], [pointy], 'ro')
        else:
            plt.plot([pointx], [pointy], 'bo')

plt.show()
