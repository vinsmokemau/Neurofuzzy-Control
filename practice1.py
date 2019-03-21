import numpy as np
import neurolab as nl
from random import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

rabbit = mpimg.imread("buggs.png")
bear = mpimg.imread("bear.png")

# Import the Hard Limit function and assign it.
hardlim = nl.trans.HardLim()
# Import the Hard Limits function and assign it.
purelin = nl.trans.PureLin()

# Set initial patterns.
p = np.array([[4, 5, 4, 5, 3, 2, 1, 2],
              [1, 1, 2, 2, 3, 3, 4, 4]])

# Set patterns in a better format to work with adeline.
p1 = np.array([[4],
              [1]])

p2 = np.array([[5],
              [1]])

p3 = np.array([[4],
              [2]])

p4 = np.array([[5],
              [2]])

p5 = np.array([[3],
              [3]])

p6 = np.array([[2],
              [3]])

p7 = np.array([[1],
              [4]])

p8 = np.array([[2],
              [4]])

r = np.add(np.dot(p1,p1.transpose()) , np.dot(p2,p2.transpose()))
r = np.add(r , np.dot(p3,p3.transpose()))
r = np.add(r , np.dot(p4,p4.transpose()))
r = np.add(r , np.dot(p5,p5.transpose()))
r = np.add(r , np.dot(p6,p6.transpose()))
r = np.add(r , np.dot(p7,p7.transpose()))
r = np.add(r , np.dot(p8,p8.transpose()))
r = np.array([0.125])*r

l = np.linalg.eig(r)[0]

maxeig = np.amax(l)

alpha = 0.2*(1/(2*maxeig))

# Transpose Patterns for a simpler use.
p = p.transpose()

# Set the initial targets for perceptron.
t_perceptron = np.array([1, 1, 1, 1, 0, 0, 0, 0])

# Set the initial targets for perceptron.
t_adeline = np.array([1, 1, 1, 1, -1, -1, -1, -1])

# Set a initial random weight for perceptron.
w_perceptron = np.random.rand(1,p.shape[1])
# Set a initial random bias for perceptron.
b_perceptron = np.random.rand(1,1)

# Set a initial random weight for adeline.
w_adeline = w_perceptron
# Set a initial random bias for adeline.
b_adeline = b_perceptron

# Asking the number of epocks for the learning process of perceptron and adeline.
epocks = int(input("Enter the number of epocks:\n"))

# Set the a empty error list for perceptron.
perceptron_error_list = []

# Perceptron's Learning Process.
for i in range(epocks):
    for j in range(p.shape[0]):
        pn = p[j].transpose()
        tn = t_perceptron[j]
        a_perceptron = hardlim(np.dot(w_perceptron,pn) + b_perceptron)
        e_perceptron = tn - a_perceptron
        #Adding the perceptron error in the list.
        perceptron_error_list.append(e_perceptron[0][0])
        w_perceptron = w_perceptron + e_perceptron*pn
        b_perceptron = b_perceptron + e_perceptron


# Set a list to plot all the perceptron's erros.
perceptron_error_len = [x for x in range(len(perceptron_error_list))]

w11_perceptron = w_perceptron[0][0]
w12_perceptron = w_perceptron[0][1]

# Set the range for the plot of perceptron's weight equation.
x_perceptron = np.linspace(0, 5)
# Calculate the equation of perceptron's weight.
y_perceptron = (-w11_perceptron/w12_perceptron)*x_perceptron + (-b_perceptron/w11_perceptron)

# Set the a empty error list for adeline.
adeline_error_list = []

# Adeline's Learning Process.
for i in range(epocks):
    for j in range(p.shape[0]):
        pn = p[j].transpose()
        tn = t_adeline[j]
        a_adeline = purelin(np.dot(w_adeline,pn) + b_adeline)
        e_adeline = tn - a_adeline
        # Adding the adeline error in the list.
        adeline_error_list.append(e_adeline[0][0])
        w_adeline = w_adeline + 2*alpha*e_adeline*pn
        b_adeline = b_adeline + 2*alpha*e_adeline

# Set a list to plot all the perceptron's erros.
adeline_error_len = [x for x in range(len(adeline_error_list))]

w11_adeline = w_adeline[0][0]
w12_adeline = w_adeline[0][1]

# Set the range for the plot of adeline's weight equation.
x_adeline = np.linspace(0, 5)
# Calculate the equation of adeline's weight.
y_adeline = (-w11_adeline/w12_adeline)*x_adeline + (-b_adeline/w11_adeline)


fig = plt.gcf()
fig.show()
fig.canvas.draw()

plt.subplot(2,2,1)
plt.title("Neural Network Plot")
#Plot equation of perceptron's weight.
plt.plot(x_perceptron, y_perceptron.transpose(), 'b', linestyle='--')
#Plot equation of adeline's weight.
plt.plot(x_adeline, y_adeline.transpose(), 'r', linestyle='--')
for pattern in range(p.shape[0]):
    x = p[pattern][0]
    y = p[pattern][1]
    p_test = np.array([x, y]).transpose()
    a = hardlim(np.dot(w_perceptron, p_test) + b_perceptron)
    if a == 0:
        plt.plot(x, y, 'ro')
    else:
        plt.plot(x, y, 'bo')

"""plt.figure(2)
plt.subplot(2,1,1)
plt.title("Perceptron Error")
plt.plot(perceptron_error_len, perceptron_error_list, 'b')

plt.subplot(2,1,2)
plt.title("Adeline Error")
plt.plot(adeline_error_len, adeline_error_list, 'b')"""

loop = input("Do you wanna evaluate a point? y/n\n").lower()
if loop != "y":
    loop = False
else:
    loop = True

while loop:

    x_user = float(input("Give me the x point\n"))
    y_user = float(input("Give me the y point\n"))

    p_user = np.array([x_user, y_user]).transpose()
    a_adeline = purelin(np.dot(w_adeline,p_user)+b_adeline)
    print(a_adeline)
    if a_adeline < 0:
        AX = fig.add_subplot(223)
        AX.set_title("Adeline Result")
        AX.imshow(rabbit)
    else:
        AX = fig.add_subplot(223)
        AX.set_title("Adeline Result")
        AX.imshow(bear)

    a_perceptron = hardlim(np.dot(w_perceptron,p_user)+b_perceptron)
    print(a_perceptron)
    if a_perceptron == 0:
        AX = fig.add_subplot(224)
        AX.set_title("Perceptron Result")
        AX.imshow(rabbit)
    else:
        AX = fig.add_subplot(224)
        AX.set_title("Perceptron Result")
        AX.imshow(bear)

    loop = input("Do you wanna evaluate another point? y/n\n").lower()
    if loop != "y":
        fig.clf()
        loop = False
    else:
        fig.clf()
        plt.subplot(2,2,1)
        plt.title("Neural Network Plot")
        #Plot equation of perceptron's weight.
        plt.plot(x_perceptron, y_perceptron.transpose(), 'b', linestyle='--')
        #Plot equation of adeline's weight.
        plt.plot(x_adeline, y_adeline.transpose(), 'r', linestyle='--')
        for pattern in range(p.shape[0]):
            x = p[pattern][0]
            y = p[pattern][1]
            p_test = np.array([x, y]).transpose()
            a = hardlim(np.dot(w_perceptron, p_test) + b_perceptron)
            if a == 0:
                plt.plot(x, y, 'ro')
            else:
                plt.plot(x, y, 'bo')

plt.show()