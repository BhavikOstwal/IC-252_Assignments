import numpy as np
import matplotlib.pyplot as plt
from statistics import NormalDist

samples = np.random.normal(size=100, loc=150, scale=10)

plt.hist(samples, edgecolor = 'r')
plt.show()

class Normal_dist:
    def __init__(self, mu:float, sigma:float):
        self.mu = mu
        self.sigma = sigma
        self.mean = self.mu
        self.std = self.sigma

    # def PDF_fn(self, x:float)
        
th_ND = NormalDist(150,10)
z = th_ND.zscore(170)
print(th_ND.cdf(140))

