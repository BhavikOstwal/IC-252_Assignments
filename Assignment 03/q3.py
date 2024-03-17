import numpy as np
from statistics import NormalDist

np.random.seed(0)
samples = np.random.normal(size=100, loc=150, scale=10)
# samples = np.sort(samples)
exp_ND = NormalDist.from_samples(samples)
theory_ND = NormalDist(140,10)

# Part (a)
print("Part (a)")
print("Experimented value:",exp_ND.pdf(140))
print("Theoritical value:",theory_ND.pdf(140))


# Part (b)
print("\nPart (b)")
# min_premium_weight = np.percentile(samples, 95)
# print(min_premium_weight)
print("Experimented value:",exp_ND.inv_cdf(0.95))
print("Theoritical value:",theory_ND.inv_cdf(0.95))

#  Part (c)
print("\nPart (c)")
# max_defective_wt = np.percentile(samples,10)
# print(max_defective_wt)
print("Experimented value:",exp_ND.inv_cdf(0.1))
print("Theoritical value:",theory_ND.inv_cdf(0.1))

# Part (d)
print("\nPart (d)")
print("Experimented value:",exp_ND.cdf(exp_ND.inv_cdf(0.95)) - exp_ND.cdf(exp_ND.inv_cdf(0.1)))
print("Theoritical value:",theory_ND.cdf(theory_ND.inv_cdf(0.95)) - theory_ND.cdf(theory_ND.inv_cdf(0.1)))
# print(exp_ND.cdf(min_premium_weight) - exp_ND.cdf(max_defective_wt))

'''
class Normal_dist:
    def __init__(self, mu:float, sigma:float):
        self.mu = mu
        self.sigma = sigma
        self.mean = self.mu
        self.std = self.sigma

    def PDF_fn(self, x:float):
        return (1/(self.sigma*np.sqrt(2*np.pi)))*np.e**(-(((x-self.mu)/self.sigma)**2)/2)
    
exp_ND = Normal_dist(150,10)
PDF_val = []
X_val = []

for i in samples:
    PDF_val.append(exp_ND.PDF_fn(i))
    X_val.append(i)

plt.plot(X_val,PDF_val)
plt.show()   



th_ND = NormalDist(150,10)

z = th_ND.zscore(170)

pdf_val = []
x_val = []
for i in np.arange(100,200,1):
    pdf_val.append(th_ND.pdf(i))
    x_val.append(i)

plt.plot(x_val,pdf_val)
plt.show()

print(th_ND.inv_cdf(0.95))
'''

        
