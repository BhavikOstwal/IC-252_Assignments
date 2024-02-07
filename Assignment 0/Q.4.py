import numpy as np
import matplotlib.pyplot as plt

def f(x_inp:np.ndarray):
    return (np.sin(x_inp)**7 +np.cos(x_inp)**5)/np.exp(x_inp)

steps = 0.01
x_inp = np.arange(0,4.01,steps)
# print(x_inp)

plt.rcParams["text.usetex"] = False #set to False so that matplotlib will use its own rendering for Latex (as Latex isn't installed on my system)

# print(plt.style.available)
plt.style.use('dark_background')
plt.plot(x_inp, f(x_inp), color = 'green')
plt.plot(x_inp,np.zeros((401,)), color = 'purple') # showing the x-axis to separate 1st and 4th quadrant
plt.xlim(0,4)
plt.grid()
plt.xlabel('x')
plt.ylabel(r'$f(x) = \frac{\sin^7(x) + \cos^5(x)}{e^x}$')
plt.savefig("Q.4.png")
# plt.show()