import numpy as np
import neurolab as nl
from random import random
import matplotlib.pyplot as plt

purelin = nl.trans.PureLin()

p = np.array([[1, 2, -1, -1],
              [1, -1, 2, -1]])
print("p: {}\n".format(p))
p = p.transpose()
print("Number of patterns: {}\n".format(p.shape[0]))

t = np.array([[1, 1, -1, -1],
             [1, -1, 1, -1]])
print("t: {}\n".format(t))
t = t.transpose()

p1 = np.array([[1],
              [1],])
p2 = np.array([[2],
              [-1,],])
p3 = np.array([[-1],
              [2,],])
p4 = np.array([[-1],
              [-1,],])

plist = [p1, p2, p3, p4]

for pid in range(4):
    if pid == 0:
        r = np.dot(plist[pid],plist[pid].transpose())
    else:
        r = np.add(r , np.dot(plist[pid],plist[pid].transpose()))
    print(r)

r = np.array([0.25])*r

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

w = np.array([[0.25, 0],
              [0, 0.25]])
b = np.array([0, -0.125]).transpose()

a1 = np.array([-1,-1]).transpose()
a2 = np.array([-1,1]).transpose()
a3 = np.array([1,-1]).transpose()
a4 = np.array([1,1]).transpose()

epocks = int(input("Enter the number of epocks:\n"))

for i in range(epocks):
    for j in range(p.shape[0]):
        pn = p[j].transpose()
        tn = t[j].transpose()
        a = purelin(np.dot(w,pn) + b)
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
        a = purelin(np.dot(w,p)+b)
        if a[0] > 0 and a[1] > 0:
            plt.plot([pointx], [pointy], 'ro')
        elif a[0] > 0 and a[1] < 0:
            plt.plot([pointx], [pointy], 'bo')
        elif a[0] < 0 and a[1] > 0:
            plt.plot([pointx], [pointy], 'go')
        elif a[0] < 0 and a[1] < 0:
            plt.plot([pointx], [pointy], 'yo')

plt.axvline(x=0, color='b', linestyle='--')
plt.axhline(y=0.5, color='b', linestyle='--')
plt.show()
