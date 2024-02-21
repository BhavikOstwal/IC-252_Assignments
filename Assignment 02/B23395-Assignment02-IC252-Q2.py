import numpy as np
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

plt.style.use('dark_background')
plt.plot(n_val, ratio_val, color='green', linewidth=1.5)
plt.grid(alpha=0.2)
plt.ylim(0,2)
plt.xlabel(r"$n$")
plt.ylabel(r"$\frac{n!}{\sqrt{2 \pi n}} \left(\frac{e}{n}\right)^n$", fontsize=12)
plt.xticks(np.arange(0,21,2))
plt.yticks(fontsize = 8)
plt.title("Stirling's Factorial Approximation Test")
plt.savefig("Q2.png")
plt.show()