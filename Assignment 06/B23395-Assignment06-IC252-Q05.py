import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(2)
def random_gen(n,size):
    return np.random.normal(65, 15, size=(n, size))


plt.style.use('dark_background')
def pltAndCompare(s_rand):
    s_means = np.mean(s_rand, axis=1)
    s_std = np.std(s_rand, axis=1)

    x = np.linspace(10, 130, 1000)
    plt.plot(x, norm.pdf(x, 65, 15), linestyle='-', color='red', lw=2, label='Population Distribution')

    for i in range(5):
        plt.hist(s_rand[i], bins=10, density=True, label=f'{i+1}')

    plt.title('Histogram of Random Samples and Population Distribution')
    plt.xlabel('Marks')
    plt.ylabel(r'$f_X(x)$', rotation=0)
    plt.grid(True)
    plt.show()
    plt.clf()
    plt.cla()

    for i in range(5):
        print(f"Sample {i+1} Stats:")
        print(f"Mean: {s_means[i]:.2f} \nStandard Deviation: {s_std[i]:.2f}")

s_rand50 = random_gen(5,50)
pltAndCompare(s_rand50)

'''Part (b)'''
print("\nPart(b)")

s_rand100 = random_gen(5,100)
s_rand150 = random_gen(5,150)
s_rand250 = random_gen(5,250)

pltAndCompare(s_rand100)
pltAndCompare(s_rand150)
pltAndCompare(s_rand250)

'''Part (c)'''
# Stratified Sampling
print("\nPart(c)")
def rand_stratified(group_size, num_groups):
    a = np.random.normal(65,15,size=(num_groups,group_size))
    return [np.random.choice(a[i]) for i in range(a.shape[0])]


def pltStratified(s_stratified):
    s_mean = np.mean(s_stratified)
    s_std = np.std(s_stratified)

    x = np.linspace(10, 130, 1000)
    plt.plot(x, norm.pdf(x, 65, 15), linestyle='-', color='red', lw=2, label='Population Distribution')

    plt.hist(s_stratified, bins=15, density=True)
    plt.title('Histogram of Stratified Sampling and Population Distribution')
    plt.xlabel('Marks')
    plt.ylabel(r'$f_X(x)$', rotation=0)
    plt.grid(True)
    plt.show()
    plt.clf()
    plt.cla()

    print(f"Mean: {s_mean:.2f} \nStandard Deviation: {s_std:.2f}")


s_stratified = rand_stratified(5,250)
pltStratified(s_stratified)
