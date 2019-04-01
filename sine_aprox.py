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
w1 = np.random.rand(2,1)
b1 = np.random.rand(2,1)
w2 = np.random.rand(1,2)
b2 = np.random.rand(1,1)
alpha = 0.1

epocks = int(input("Enter number of epocks: "))

a2_list = []

for epock in range(epocks):
    for id_p in range(p.size):
        a1 = logsig(np.dot(w1,p[id_p])+b1)
        a2 = purelin(np.dot(w2,a1)+b2)
        e = g[id_p] - a2
        s2 = np.dot(-2,(g[id_p] - a2))
        s1 = np.array([[np.dot((1 - a1[0]),a1[0]), 0],
                       [0, np.dot((1-a2[0]),a2[0])]])
        s1 = np.dot(np.dot(s1, w2.T),s2)
        w1 = w1 - alpha*s1*p[id_p]
        b1 = b1 - alpha*s1
        w2 = w2 - alpha*s2*a1.T
        b2 = b2 - alpha*s2
        if epock == epocks - 1:
            a2_list.append(a2[0][0])

plt.figure()
plt.plot(p, g, 'b')
plt.plot(p, a2_list, 'g')
plt.show()