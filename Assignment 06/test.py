import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

a = 1  
b = 5  
lambda_param = 0.5 

trunc_exp_dist = stats.truncexpon(b - a, loc=a, scale=1/lambda_param)
random_numbers = trunc_exp_dist.rvs(size=1000)  

# Create a range of values for x-axis
x = np.linspace(a, b, 100)

# Calculate the PDF values for the given x values
pdf_values = trunc_exp_dist.pdf(x)

# Plot histogram of the samples
plt.hist(random_numbers, bins=30, density=True, alpha=0.5, label='Histogram')

# Plot the PDF of the truncated exponential distribution
plt.plot(x, pdf_values, 'r-', lw=2, label='Truncated Exponential PDF')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram and PDF of Truncated Exponential Distribution')
plt.show()
