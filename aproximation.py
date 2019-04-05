import numpy as np
import neurolab as nl
from random import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

purelin = nl.trans.PureLin()
logsig = nl.trans.LogSig()

p = np.linspace(-2, 2)
g = 1 + np.sin((np.pi / 4) * p)
w1 = np.random.rand(2, 2)
b1 = np.random.rand(2, 1)
w2 = np.random.rand(1, 2)
b2 = np.random.rand(1, 1)
alpha = 0.1

epocks = int(input("Enter number of epocks: "))

a2_list = []
