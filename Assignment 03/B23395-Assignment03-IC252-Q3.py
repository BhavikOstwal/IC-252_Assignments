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



        
