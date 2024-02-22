import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

n_values = np.arange(2,501)
prob_values=[]
for n in range(len(n_values)):
    arr = np.arange(1,n_values[n]+1)
    rlt_frq =0
    for j in range(1000):
        np.random.shuffle(arr)
        for i in range(len(arr)):
            if (arr[i]==i+1):
                rlt_frq+=1
                break
    prob_values.append(rlt_frq/1000)


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
plt.text(0,0.3,"As from my inference from the graph,at some point, \nthe event of getting number on kth card (from a \ndeck of well-shuffled cards) equal to k is \ncompleletly random. In the graph, we can see that for \nany value of n, the local maxima of probability is \nnot sure. So, there doesn't exist any strategy for choosing \nn to maximize our winning probability.", fontsize=14)


# plt.savefig("Q3.png")
plt.show()
