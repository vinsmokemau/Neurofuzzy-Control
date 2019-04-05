"""Exercise 14."""
import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

purelin = nl.trans.PureLin()
s = 1
R = 2
w = np.random.rand(1, 2)
b = np.random.rand(1, 1)
f = 60
fs = 1000
step = 1 / fs
t = np.linspace(0, 1, 1000)
v = 1.2 * np.sin(2 * np.pi * f * t)
m = (0.12 * np.sin(2 * np.pi * f * t)) + (np.pi / 2)
s = 0.1 * np.random.rand(m.shape[0])
tm = s + m
v1 = np.append(np.array([0]), v[:len(v) - 1])

p = np.array([v, v1])
p = p.T

e = np.zeros(p.shape[0])
a = np.zeros(p.shape[0])

target = s
alpha = 0.01

for i in range(10):
    for j in range(p.shape[0]):
        pn = p[j].T
        tn = target[j]
        a[j] = purelin(np.dot(w, pn) + b)
        e[j] = tn - a[j]
        w = w + 2*alpha*e[j] * pn
        b = b + 2*alpha*e[j]

plt.figure("Exercise 14")

plt.subplot(3, 2, 1)
plt.title("EEG Signal")
plt.plot(t, s)
plt.axis('off')

plt.subplot(3, 2, 2)
plt.title("Signal + Noise")
plt.plot(t, tm)
plt.axis('off')

plt.subplot(3, 2, 3)
plt.title("60Hz Input")
plt.plot(t, v)
plt.axis('off')

plt.subplot(3, 2, 4)
plt.title("Error")
plt.plot(t, e)
plt.axis('off')

plt.subplot(3, 2, 5)
plt.title("Noise Path (m)")
plt.plot(t, m)
plt.axis('off')

plt.subplot(3, 2, 6)
plt.title("Output Signal")
f = tm - e
plt.plot(t, f)
plt.axis('off')


plt.figure("Results")
plt.plot(t, s, 'b')
plt.plot(t, e, 'y')

plt.show()
