import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def generate_exponential_samples(lamda, sample_size):
    return np.random.exponential(scale=1/lamda, size=sample_size)

def plot_samples(samples, lamda):
    plt.hist(samples, bins=12, density=True)
    x = np.linspace(0, 10/lamda, 1000)
    plt.plot(x, lamda * np.exp(-lamda * x), linestyle='-', color='red', lw=2)
    plt.title('Comparison of Sample Data with Parent Distribution')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f_X(x)$', rotation=0)
    plt.grid(True)
    plt.show()

def calculate_stats(samples):
    sample_mean = np.mean(samples)
    sample_var = np.var(samples)
    return sample_mean, sample_var

lamda = float(input("Enter the lambda: "))

sample_sizes = [50, 100, 200, 500, 5000]

for i, n in enumerate(sample_sizes, 1):
    samples = generate_exponential_samples(lamda, n)
    
    if i <= 3:
        plot_samples(samples, lamda)
    
    sample_mean, sample_var = calculate_stats(samples)
    
    print(f"Sample Size (n={n}):")
    print(f"Sample mean: {sample_mean:.4f}, Sample lamda: {1/sample_mean:.4f}, Sample Variance: {sample_var:.4f}")
