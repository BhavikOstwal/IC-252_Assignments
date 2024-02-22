import matplotlib.pyplot as plt

def factorial(n:int):
    if (n<2):
        return 1
    return n*factorial(n-1)

k_values = []
p_values = []
for k in range(2,101):
    a = factorial(365)
    a/= (factorial(365-k))*(365**k)
    k_values.append(k) 
    p_values.append(1-a) 

plt.style.use('ggplot')
plt.plot(k_values, p_values)
plt.xlabel("Number of people")
plt.ylabel(r"Probability of same birthday of atleast one pair", fontsize=9)
# plt.savefig("Q1.png")
plt.show()