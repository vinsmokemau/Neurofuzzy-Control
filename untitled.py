import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

hardlim = nl.trans.HardLim()

w = np.array([0.75, 0], 
             [0.75, 0.25])

b = np.array([-0.375],
             [-0.375])

p1 =np.array([0,0]).transpose()
p2 =np.array([0,2]).transpose()
p3 =np.array([1,0]).transpose()
p4 =np.array([1,1]).transpose()

print(hardlim(np.dot(w,p1) + b))
print(hardlim(np.dot(w,p2) + b))
print(hardlim(np.dot(w,p3) + b))
print(hardlim(np.dot(w,p4) + b))

"""
loop = True
plot_eq = True

fig = plt.gcf()
fig.show()
fig.canvas.draw()

while loop:
    x_user = float(input("Give me the x point\n"))
    y_user = float(input("Give me the y point\n"))

    p = np.array([x_user, y_user]).transpose()

    if plot_eq == True:
        x = np.linspace(-2, 2)
        y = -(x)
        plt.plot(x, y)
    a = hardlim(np.dot(w,p))
    if a == 0:
        plt.plot([x_user], [y_user], 'ro')
        print("This point {} is from red area".format(p))
    else:
        plt.plot([x_user], [y_user], 'bo')
        print("This point {} is from blue area".format(p))

    fig.canvas.draw()

    plot_eq = False

    loop = input("Do you wanna evaluate another point? y/n\n").lower()
    if loop != "y":
        loop = False
"""