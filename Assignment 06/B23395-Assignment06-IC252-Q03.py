import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.style.use('dark_background')

def generate_normal_samples(mean, std, sample_size):
    return np.random.normal(mean, std, sample_size)

def plot_samples(samples, mu, sigma):
    plt.hist(samples, bins=10, density=True)
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    plt.plot(x, norm.pdf(x, mu, sigma), linestyle='-', color='red', lw=2)
    plt.title('Comparison of Sample Data with Parent Distribution')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f_X(x)$', rotation=0)
    plt.grid(True)
    plt.show()

def calculate_stats(samples):
    sample_mean = np.mean(samples)
    sample_var = np.var(samples)
    return sample_mean, sample_var

mu = float(input("Enter the mean: "))
sigma = float(input("Enter the standard deviation: "))

sample_sizes = [50, 100, 200, 500, 5000]

for i, n in enumerate(sample_sizes, 1):
    samples = generate_normal_samples(mu, sigma, n)
    
    if i <= 3:
        plot_samples(samples, mu, sigma)
    
    sample_mean, sample_var = calculate_stats(samples)
    
    print(f"Sample Size (n={n}):")
    print(f"Sample Mean: {sample_mean:.4f}, Sample Variance: {sample_var:.4f}")
