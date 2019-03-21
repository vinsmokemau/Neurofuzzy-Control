import numpy as np
import neurolab as nl
from random import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

purelin = nl.trans.PureLin()
logsig = nl.trans.LogSig()

p = np.linspace(-2, 2)
g = 1 + np.sin((np.pi/4)*p)
w1 = np.random.rand(1,2)
b1 = np.random.rand(2,1)
w2 = np.random.rand(1,2)
b2 = np.random.rand(1,1)

print("w1: {}\n".format(w1))
print("b1: {}\n".format(b1))
print("w2: {}\n".format(w2))
print("b2: {}\n".format(b2))

epocks = int(input("Enter number of epocks: "))

for epock in range(epocks):
    for id_p in range(p.size):
        a1 = logsig(np.dot(w1,p[id_p].T)+b1)
        a2 = purelin(np.dot(w2,a1)+b2)
        e = g[id_p] - a2
        s2 = -2*(e)
        s1 = np.array([
                       [np.dot((1 - a1),a1), 0],
                       [0, np.dot((1-a2),a2)]
                       ])
        s1 = np.dot(s1, w2.T)*s2


print("a1: {}\n".format(a1))
print("a2: {}\n".format(a2))
print("s1: {}\n".format(s1))
print("s2: {}\n".format(s2))