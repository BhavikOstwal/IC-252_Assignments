import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

repair_times_FM = np.random.normal(1.5, 0.75, 100)
repair_times_AM = np.random.normal(1, 0.5, 100)


# Part (a)
AM_range = np.linspace(0, 3, 100)
FM_range = np.linspace(0, 4.5, 100)
AM_grid, FM_grid = np.meshgrid(AM_range, FM_range)


def joint_dist(x, y, mu_x, sigma_x, mu_y, sigma_y):
    return (1 / (2 * np.pi * sigma_x * sigma_y) *np.exp(-0.5 * (((x - mu_x) / sigma_x) ** 2 + ((y - mu_y) / sigma_y) ** 2)))

joint_prob = joint_dist(AM_grid, FM_grid, 1, 0.5, 1.5, 0.75)


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(AM_grid, FM_grid, joint_prob, cmap='viridis')

ax.set_xlabel('AM Repair Time (hours)')
ax.set_ylabel('FM Repair Time (hours)')
ax.set_zlabel('Joint Probability Density')

plt.title('Joint Probability Distribution of AM and FM Repair Times')

# plt.savefig('Q4_(a).png')
plt.show()


# Part (b)
print("This part is done on paper (theoritical)")


# Part (c)
T = repair_times_AM + repair_times_FM
print(T)

# Part (d)
T = repair_times_AM + repair_times_FM
mu_T = np.mean(T)
sigma_T = np.std(T)
print(mu_T,sigma_T )

plt.hist(np.random.normal(loc=mu_T, scale=sigma_T, size=10000), edgecolor='black', color='red', linewidth=1.5)
# plt.savefig('Q4_(d).png')
plt.show()

# Part (e)
'''to be continued...'''

