import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

joint_prob = {
    "T-Shirt":[0.1,0.05,0.1],
    "Sweater":[0.05,0.1,0.2],
    "Jacket":[0.1,0.2,0.1]
}
df = pd.DataFrame(joint_prob,index=['Sunny', 'Rainy', 'Cloudy'])
print(df, "\n")

# Part (b)
print("\nMarginal distribution of Y:\n")
print(pd.Series(df.sum(axis=1)))

print("\nMarginal distribution of X:\n")
print(pd.Series(df.sum(axis=0)))

clothing_choice = ["T-Shirt", "Sweater", "Jacket"]
weather = ['Sunny', 'Rainy', 'Cloudy']


def choose_with_dependent_bias(item_from_list1):
    probabilities = joint_prob[item_from_list1]
    return random.choices(weather, probabilities, k=1)[0]


print("\n")
lst = []
n = 100000
for i in range(n):
    a = np.random.choice(clothing_choice)
    lst.append(f"{a},{choose_with_dependent_bias(a)}")
    
unique_pairs, count = np.unique(lst, return_counts=True)
for i,j in enumerate(unique_pairs):
    print(f"({j}) = {count[i]/n}")

print("\n")
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.title('Marginal Probabilities of Weather')
plt.bar(weather, df.sum(axis=1), edgecolor='black', color='red', linewidth=1.5)
plt.ylabel(r'$f_X(x)$', rotation=0)

plt.subplot(1,2,2)
plt.title('Marginal Probabilities of Clothing Choice')
plt.bar(clothing_choice, df.sum(axis=0), edgecolor='black', color='red', linewidth=1.5)
# plt.savefig('Q1_(b).png')
plt.show()