import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


'''Part (a)'''
def entropy(p):
    if p == 0 or p == 1:
        return 0  # Entropy is 0 for edge cases outcomes
    else:
        return - (p * np.log2(p) + (1 - p) * np.log2(1 - p))

probabilities = np.linspace(0.001, 0.999, 1000)

entropies = [entropy(p) for p in probabilities]

plt.style.use('dark_background')
plt.plot(probabilities, entropies, label='Entropy', color='red')
plt.plot(0.5*np.ones((len(entropies,))), entropies)
plt.title('Entropy of a Biased Coin')
plt.xlabel('Probability of Heads (p)')
plt.ylabel('Entropy')
plt.grid(True)
plt.show()
plt.clf()
plt.cla()


'''Part (b)'''
def gaussian(x, mean, variance):
    return norm.pdf(x, mean, np.sqrt(variance))

def kl_divergence(p, q, x):
    return np.sum(p * np.log(p / q))

def cross_entropy(p, q, x):
    return -np.sum(p * np.log(q))

x = np.linspace(-10, 10, 1000)

scenarios = [
    {'mean_p': 0, 'variance_p': 1, 'mean_q': 0, 'variance_q': 1},  
    {'mean_p': 0, 'variance_p': 1, 'mean_q': 1.5, 'variance_q': 1},  
    {'mean_p': 0, 'variance_p': 1, 'mean_q': 4, 'variance_q': 1}   
]

for scenario in scenarios:
    p = gaussian(x, scenario['mean_p'], scenario['variance_p'])
    q = gaussian(x, scenario['mean_q'], scenario['variance_q'])
    
    plt.plot(x, p, color='blue')
    plt.plot(x, q, color='red')
    plt.title('Gaussian Distributions')
    plt.xlabel(r'$x$')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.show()

    kl_div = kl_divergence(p, q, x)
    cross_ent = cross_entropy(p, q, x)

    print(f"KL Divergence: {kl_div}")
    print(f"Cross-Entropy: {cross_ent}")
    print()
