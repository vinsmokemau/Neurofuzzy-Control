import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

hardlims = nl.trans.HardLims()

p = np.array([[0, 0,],
              [0, 0,],
              [1, 0,]])
print("p: {}\n".format(p))
p = p.transpose()
print("Number of patterns: {}\n".format(p.shape[0]))

t = np.array([1, -1])
print("t: {}\n".format(t))

w = np.random.rand(1,p.shape[1])
b = np.random.rand(1,1)

print("w: {}\n".format(w))
print("b: {}\n".format(b))

epocks = int(input("Enter the number of epocks:\n"))

for i in range(epocks):
    for j in range(p.shape[0]):
        pn = p[j].transpose()
        tn = t[j]
        a = hardlims(np.dot(w,pn) + b)
        e = tn - a
        w = w + e*pn
        b = b + e

print("Error value: {}".format(e))
print("Weight value: {}".format(w))
print("Bias value: {}".format(b))
print("Last a: {}".format(a))

w11 = w[0][0]
w12 = w[0][1]

a1 = np.array([[-1]])
a2 = np.array([[1]])

"""
x = np.linspace(-3, 3)
y = (-w11/w12)*x + (-b/w11)
plt.plot(x, y.transpose(), 'b', linestyle='--')
plt.plot([0,w11], [0,w12], 'ro-')
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

points = [x * 0.1 for x in range(-10, 12, 2)]

for pointx in points:
    for pointy in points:
        for pointz in points:
            p_n = np.array([pointx, pointy, pointz]).transpose()
            a = hardlims(np.dot(w,p_n)+b)
            if np.array_equal(a, a1):
                ax.scatter([pointx], [pointy], [pointz], c='r')
            else:
                ax.scatter([pointx], [pointy], [pointz], c='b')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
