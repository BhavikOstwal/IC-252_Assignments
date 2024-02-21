import math
import matplotlib.pyplot as plt

def factorial(n:int):
    if (n<2):
        return 1
    return n*factorial(n-1)

def factroial_s(n:int):
    return ((2*np.pi*n)**0.5)*((n/math.e)**n)
n_val = []
ratio_val = []
for i in range(1,21):
    n_val.append(i)
    ratio_val.append(factorial(i)/factroial_s(i))
plt.plot(n_val, ratio_val)
plt.ylim(0,2)
plt.show()