import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlim = nl.trans.HardLim()

p = np.array([[1, 2, -1, -1],
              [1, -1, 2, -1]])
print("p: {}\n".format(p))
p = p.transpose()
print("Number of patterns: {}\n".format(p.shape[0]))

t = np.array([[1, 1, 0, 0],
			 [1, 0, 1, 0]])
print("t: {}\n".format(t))
t = t.transpose()


w = np.array([[0.25, 0],
              [0, 0.25]])
b = np.array([0, -0.125]).transpose()

a1 = np.array([0,0]).transpose()
a2 = np.array([0,1]).transpose()
a3 = np.array([1,0]).transpose()
a4 = np.array([1,1]).transpose()

epocks = int(input("Enter the number of epocks:\n"))

for i in range(epocks):
    for j in range(p.shape[0]):
        pn = p[j].transpose()
        tn = t[j].transpose()
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

plt.axvline(x=0, color='b', linestyle='--')
plt.axhline(y=0.5, color='b', linestyle='--')
plt.show()
