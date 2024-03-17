import numpy as np
import matplotlib.pyplot as plt

X_val = np.arange(0,6)
No_of_students = np.array([2,11,23,9,4,1])
# print(X_val)

n = 50
PDF_val =  No_of_students/n
# print(PDF_val.dot(X_val))

CDF_val = np.cumsum(PDF_val)

# plt.step(X_val, CDF_val,'g*', where='post')
# plt.show()

freq_500 = []
for i in range(500):
    freq_500.append(np.random.randint(0,5))

plt.hist(freq_500)
plt.show()