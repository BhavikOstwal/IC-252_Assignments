import numpy as np
import matplotlib.pyplot as plt

# Part (d)
def normal_prob(x, mu, sigma):
    return (np.e**(-(1/2)*((x-mu)/sigma)**2))/(((2*np.pi)**2)*sigma)

X = np.linspace(0,100, 10000)

plt.plot(X, normal_prob(X,78,5), label='Prof. A\'s Exam')
plt.plot(X, normal_prob(X,85,3), label='Prof. B\'s Exam')
plt.xlabel('Marks')
plt.ylabel(r'$f_X(x)$', rotation=0)
plt.title('PDFs of both Professor A\'s and Professor B\'s exams')
plt.legend()
plt.savefig('Q3_(d).png')
plt.show()