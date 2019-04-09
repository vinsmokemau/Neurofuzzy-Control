"""Exercise 14."""
import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

purelin = nl.trans.PureLin()
logsig = nl.trans.LogSig()

alpha = 0.01

epochs = 350
x=np.array([2, 5, 4, 5, 3, 2, 3, 2])
y=np.array([1, 3, 4, 2, 3, 3, 6, 4])

p = np.array([x,y])
p = p.T

s = 1
t = np.array([1, 1, 1, 1, -1, -1, -1, -1])

w1=np.random.rand(2,2)
b1=np.random.rand(2,1)
w2=np.random.rand(1,2)
b2=np.random.rand(1,1)

a2_list = []

for epoch in range(epochs):
    for id_p in range(p.shape[0]):
        pn=np.random.rand(2,1)
        pn[0][0] = p[id_p][0]
        pn[1][0] = p[id_p][1]
        a1 = logsig(np.dot(w1,pn)+b1)
        a2 = purelin(np.dot(w2,a1)+b2)
        e = t[id_p] - a2
        s2 = np.dot(-2,(t[id_p] - a2))
        s1 = np.array([[np.dot((1 - a1[0]),a1[0]), 0],
                       [0, np.dot((1-a2[0]),a2[0])]])
        s1 = np.dot(np.dot(s1, w2.T),s2)
        w1 = w1 - alpha*s1*p[id_p]
        b1 = b1 - alpha*s1
        w2 = w2 - alpha*s2*a1.T
        b2 = b2 - alpha*s2
        if epoch == epochs - 1:
            a2_list.append(a2[0][0])

plt.figure()

for x in range(60):
    x *= 0.1
    for j in range(60):
        j *= 0.1
        a1=logsig(np.dot(w1,np.array([x,j]).T) + b1)
        a2=purelin(np.dot(w2,a1)+b2)
        if (a2[0][0]>=0):
            plt.plot([x], [j], 'bo')
        if (a2[0][0]<0):
            plt.plot([x], [j], 'ro')

plt.plot([2, 5, 4, 5], [1, 3, 4, 2], 'k*')
plt.plot([3, 2, 3, 2], [3, 3, 6, 4], 'w*')
plt.show()
                        