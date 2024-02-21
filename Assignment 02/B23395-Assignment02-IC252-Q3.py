import numpy as np
import matplotlib.pyplot as plt

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
plt.style.use('ggplot')
plt.plot(n_values, prob_values)
plt.title(r"Probabilities at various values of $n$")
plt.xlabel(r'$n$')
plt.ylabel(r"Probability of Winning")
plt.grid(alpha=0.5)
plt.savefig("Q3.png")
plt.show()
