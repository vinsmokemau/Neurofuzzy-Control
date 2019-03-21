from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-6, 6, 500, endpoint=False)
plt.plot(t, signal.square(2 * np.pi * t))
plt.ylim(-2, 2)
plt.show()
