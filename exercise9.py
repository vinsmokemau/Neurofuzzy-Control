import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random

hardlims = nl.trans.HardLims()

p = np.array([[1, 1,],
              [-1, 1,],
              [-1, -1,]])
print("p: {}\n".format(p))
p = p.transpose()
print("Number of patterns: {}\n".format(p.shape[0]))

t = np.array([-1, 1])
print("t: {}\n".format(t))

p1 = np.array([[1],
              [-1],
              [-1]])
p2 = np.array([[1],
              [1,],
              [-1,]])

r = np.array([0.5])*(np.add(np.dot(p1,p1.transpose()) , np.dot(p2,p2.transpose())))
print("R: {}\n".format(r))

l = np.linalg.eig(r)[0]
print("Eigen Values: {}\n".format(l))

maxeig = np.amax(l)
print("Max Eigenvalue: {}\n".format(maxeig))

alpha = 1/maxeig
rand = 0
while rand == 0:
    rand = random()
alpha *= rand
print("Alpha: {}\n".format(alpha))

w = np.random.rand(1,p.shape[1])
b = np.random.rand(1,1)

print("w: {}\n".format(w))
print("b: {}\n".format(b))

a1 = np.array([[-1]])
a2 = np.array([[1]])

epocks = int(input("Enter the number of epocks:\n"))
for i in range(epocks):
    for j in range(p.shape[0]):
        pn = p[j].transpose()
        tn = t[j]
        a = hardlims(np.dot(w,pn) + b)
        e = tn - a
        w = w + 2*alpha*e*pn
        b = b + 2*alpha*e

print("Error value: {}".format(e))
print("Weight value: {}".format(w))
print("Bias value: {}".format(b))
print("Last a: {}".format(a))

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

ax.scatter([1], [-1], [-1], c='y')
ax.scatter([1], [1], [-1], c='g')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
