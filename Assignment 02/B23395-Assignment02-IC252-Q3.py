import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def factorial(n:int):
    if (n<2):
        return 1
    return n*factorial(n-1)

n_values = np.arange(2,201)
prob_values=[]
for n in range(len(n_values)):
    count = 0
    for i in range(n_values[n]+1):
        count+= ((-1)**i)/factorial(i)
    prob_values.append(1-count)


# print(plt.style.available)
plt.figure(figsize=(14,5))
plt.style.use('ggplot')
plt.subplot(1,2,1)
plt.plot(n_values, prob_values)
plt.title(r"Probabilities at various values of $n$")
plt.xlabel(r'$n$')
plt.ylabel(r"Probability of Winning")
plt.grid(alpha=0.5)


plt.subplot(1,2,2)
plt.axis('off')
plt.text(0,0.3,"As from my inference from the graph, \nthe probability of getting number on kth card, at some \npoint, (from a deck of well-shuffled cards) equal to k is \nmaximum at n=3, i.e., Probability = 0.66(approx.). And there \nis also a local maxima at n=5.  Also, as n increases, \nthe probability also converges to 0.63(approx.). So, \nthe strategy to maximize our winning probability is choose \nn=3 or n>=7 but do not choose n=2,4 or n=6 (as they have \nlocal minima)", fontsize=14)


plt.savefig("Q3.png")
plt.show()
