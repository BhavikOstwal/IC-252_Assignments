import numpy as np
import matplotlib.pyplot as plt

X_val = np.arange(0,6)
No_of_students = np.array([2,11,23,9,4,1])
# print(X_val)

n = 50
PDF_val =  No_of_students/n
# print(PDF_val.dot(X_val))

CDF_val = np.cumsum(PDF_val)

print()

# Part (a)
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.title("PDF")
plt.scatter(X_val,PDF_val,marker='o',color='r')
# plt.scatter(X_val, PDF_val ,marker='o', color='r')
plt.xlabel(r'$X$')
plt.ylabel(r'$P(X=x)$', rotation=0)
plt.xlim(-0.5,5.5)
plt.ylim(-0.1,1.1)
plt.grid()
# plt.show()

plt.subplot(1,2,2)
plt.title("CDF")
plt.hlines(CDF_val, np.arange(6),np.arange(1,7), color='r', linewidth=2.0)
plt.scatter(X_val, CDF_val,marker='o', color='r')
# plt.plot(np.arange(5,7), np.ones((2,)), color='r')
plt.plot(np.arange(-1,1), np.zeros((2,)), color='r', linewidth=2.0)
plt.xlabel(r'$X$')
plt.ylabel(r'$P(X≤x)$', rotation=0)
plt.xlim(-0.5,5.5)
plt.ylim(-0.1,1.1)
plt.grid()
plt.show()


# Part (B)


