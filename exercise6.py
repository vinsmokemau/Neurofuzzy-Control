"""Exercise 6 AND, Learning Rules."""
import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlim = nl.trans.HardLim()

p = np.array([[0, 0, 1, 1],
              [0, 1, 0, 1]])
print("p: {}\n".format(p))
p = p.transpose()
print("Number of patterns: {}\n".format(p.shape[0]))

t = np.array([0, 0, 0, 1])
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
        a = hardlim(np.dot(w,pn) + b)
        e = tn - a
        w = w + e*pn
        b = b + e

print("Error value: {}".format(e))
print("Weight value: {}".format(w))
print("Bias value: {}".format(b))

points = [x * 0.1 for x in range(-30, 31, 2)]

for pointx in points:
    for pointy in points:
        p_n = np.array([pointx, pointy]).transpose()
        a = hardlim(np.dot(w,p_n)+b)
        if a == 0:
            plt.plot([pointx], [pointy], 'ro')
        else:
            plt.plot([pointx], [pointy], 'bo')
plt.show()
