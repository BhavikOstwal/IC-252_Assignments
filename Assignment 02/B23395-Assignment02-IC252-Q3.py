import matplotlib.pyplot as plt

def factorial(n:int):
    if (n<2):
        return 1
    return n*factorial(n-1)

n_values = []
p_val = []
for i in range(2,200):
    n_values.append(i)
    p=0
    for k in range(0,i):
        p+=((-1)**k)/factorial(k)
    p_val.append(p)

plt.plot(n_values,p_val)
plt.show()