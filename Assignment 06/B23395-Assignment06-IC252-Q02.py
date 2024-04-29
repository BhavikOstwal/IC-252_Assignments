import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats

np.random.seed(1)
sample_size = 1000

uniform_data = np.random.uniform(0, 1, sample_size)

mu, sigma = 0, 1
normal_data = np.random.normal(mu, sigma, sample_size)

a = 1  
b = 5  
beta = 2
trunc_exp_dist = stats.truncexpon(b - a, loc=a, scale=beta)
random_numbers = trunc_exp_dist.rvs(size=1000)  

fig, axs = plt.subplots(3, 1)

axs[0].hist(uniform_data, bins=15, density=True, alpha=0.5, color='b', label='Sample Data')
x = np.linspace(0, 1, 100)
axs[0].plot(x, np.ones_like(x), 'r-', lw=2, label='Uniform Density Function')
axs[0].set_title('Uniform Distribution')

axs[1].hist(normal_data, bins=20, density=True, alpha=0.5, color='g', label='Sample Data')
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
axs[1].plot(x, norm.pdf(x, mu, sigma), 'r-', lw=2, label='Normal Density Function')
axs[1].set_title('Normal Distribution')

axs[2].hist(random_numbers, bins=20, density=True, alpha=0.5, color='m', label='Sample Data')
x = np.linspace(a, b, 100)
axs[2].plot(x, trunc_exp_dist.pdf(x), 'r-', lw=2, label='Truncated Exponential Density Function')
axs[2].set_title('Truncated Exponential Distribution')

plt.show()


'''Part(b)'''
def inverse_cdf(u):
    return (-3 + (9+160*u)**0.5)/2

sample_size = 1000
uniform_samples = np.random.uniform(0, 1, sample_size)
random_samples = inverse_cdf(uniform_samples)

def f(x):
    return (1/40) * (2*x + 3)

x_values = np.linspace(0.0001, 5, 100)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'r-', label='Density Function')

plt.hist(random_samples, bins=30, density=True, alpha=0.5, color='b')

plt.title('Density Function and Histogram of Random Samples')
plt.xlabel('x')
plt.ylabel('Density')
plt.grid(True)
plt.show()