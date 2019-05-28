"""Practice 2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([i * 0.1 for i in range(101)])
m1 = x / (x + 2)
m2 = 2**(-x)
m3 = 1 / (1 + 10 * (x - 2)**2)
plt.figure(1)
plt.suptitle('Complement, Intersection, Union, Morgan Laws')

# COMPLEMENTO
try1 = 1 - m1
plt.subplot(4, 3, 1)
plt.plot(x, m1, 'b.')
plt.plot(x, try1, 'g.')
try2 = 1 - m2
plt.subplot(4, 3, 2)
plt.plot(x, m2)
plt.plot(x, try2, 'g')
try3 = 1 - m3
plt.subplot(4, 3, 3)
plt.plot(x, m3)
plt.plot(x, try3, 'g')

# INTERSECCIÓN
try1 = np.array([min(m1[i], m2[i]) for i in range(101)])
plt.subplot(4, 3, 4)
plt.plot(x, m1)
plt.plot(x, m2)
plt.plot(x, try1, 'g')
try2 = np.array([min(m1[i], m3[i]) for i in range(101)])
plt.subplot(4, 3, 5)
plt.plot(x, m1)
plt.plot(x, m3)
plt.plot(x, try2, 'g')
try3 = np.array([min(m2[i], m3[i]) for i in range(101)])
plt.subplot(4, 3, 6)
plt.plot(x, m2)
plt.plot(x, m3)
plt.plot(x, try3, 'g')

# UNIÓN
try1 = np.array([max(m1[i], m2[i]) for i in range(101)])
plt.subplot(4, 3, 7)
plt.plot(x, m1)
plt.plot(x, m2)
plt.plot(x, try1, 'g')
try2 = np.array([max(m1[i], m3[i]) for i in range(101)])
plt.subplot(4, 3, 8)
plt.plot(x, m1)
plt.plot(x, m3)
plt.plot(x, try2, 'g')
try3 = np.array([max(m2[i], m3[i]) for i in range(101)])
plt.subplot(4, 3, 9)
plt.plot(x, m2)
plt.plot(x, m3)
plt.plot(x, try3, 'g')

# Morgan Laws not A and B
try1 = 1 - (np.array([max(m1[i], m2[i]) for i in range(101)]))
plt.subplot(4, 3, 10)
plt.plot(x, m1)
plt.plot(x, m2)
plt.plot(x, try1, 'g')
try2 = 1 - (np.array([max(m1[i], m3[i]) for i in range(101)]))
plt.subplot(4, 3, 11)
plt.plot(x, m1)
plt.plot(x, m3)
plt.plot(x, try2, 'g')
try3 = 1 - (np.array([min(m2[i], m3[i]) for i in range(101)]))
plt.subplot(4, 3, 12)
plt.plot(x, m2)
plt.plot(x, m3)
plt.plot(x, try3, 'g')

plt.show()
