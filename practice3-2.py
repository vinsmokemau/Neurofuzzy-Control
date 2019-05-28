"""Practice 2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([i * 0.1 for i in range(-150, 151)])
M1 = 1 / (1 + ((x + 5) / 7.5)**4)
M2 = 1 / (1 + ((x - 5) / 5)**2)

# Snorm
Smax = np.array([max(M1[i], M2[i]) for i in range(301)])
Sa = np.subtract(np.add(M1, M2), (M1 * M2))
Sb = np.array([min(1, np.add(M1[i], M2[i])) for i in range(301)])
Sd = np.zeros(301)

for i in range(301):
    if (M1[i] == 0):
        Sd[i] = M2[i]
    if (M2[i] == 0):
        Sd[i] = M1[i]
    if (M1[i] > 0 and M2[i] > 0):
        Sd[i] = 1

# Tnorm
Tm = np.array([min(M1[i], M2[i]) for i in range(301)])
Ta = M1 * M2
Tb = np.array([max(0, np.add(M1[i], M2[i]) - 1) for i in range(301)])
Td = np.zeros(301)
for i in range(301):
    if (M1[i] == 1):
        Td[i] = M2[i]
    if (M2[i] == 1):
        Td[i] = M1[i]
    if (M1[i] < 1 and M2[i] < 1):
        Td[i] = 0

# Snormplot
plt.figure(1)
plt.suptitle('Snorm')
plt.subplot(221)
plt.plot(x, M1, 'g', x, M2, 'b', x, Smax, 'r')
plt.subplot(222)
plt.plot(x, M1, 'g', x, M2, 'b', x, Sa, 'r')
plt.subplot(223)
plt.plot(x, M1, 'g', x, M2, 'b', x, Sb, 'r')
plt.subplot(224)
plt.plot(x, M1, 'g', x, M2, 'b', x, Sd, 'r')
plt.figure(2)

# Tnormplot
plt.suptitle('Tnorm')
plt.subplot(221)
plt.plot(x, M1, 'g', x, M2, 'b', x, Tm, 'r')
plt.subplot(222)
plt.plot(x, M1, 'g', x, M2, 'b', x, Ta, 'r')
plt.subplot(223)
plt.plot(x, M1, 'g', x, M2, 'b', x, Tb, 'r')
plt.subplot(224)
plt.plot(x, M1, 'g', x, M2, 'b', x, Td, 'r')
plt.show()
