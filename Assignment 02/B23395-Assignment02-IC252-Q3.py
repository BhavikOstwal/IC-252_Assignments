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
        
plt.plot(n_values, prob_values)
plt.xlabel(r'$n$')
plt.ylabel(r"probability of winning")
plt.show()
