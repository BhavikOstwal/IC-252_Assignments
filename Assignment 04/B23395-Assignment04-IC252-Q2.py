import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# X -> No. of LED bulbs
# Y -> No. of defective bulbs

dict = {
    0:[0.081,0.018,0.001],
    1:[0.513,0.084,0.003],
    2:[0.27075,0.0285,0.00075]
}

df = pd.DataFrame(dict)
df = df.rename_axis('Y', axis='index').rename_axis('X', axis='columns')
print(df)

# Part (a)

X = np.arange(len(df.columns))
Y = np.arange(len(df.index))
X, Y = np.meshgrid(X, Y)

Z = df.values

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

for (x, y, z_row) in zip(X, Y, Z):
    ax.bar3d(x, y, np.zeros(len(z_row)), 1, 1, z_row, shade=True)

ax.set_xlabel('X (No. of LED bulbs)')
ax.set_ylabel('Y (No. of defective bulbs)')
ax.set_zlabel('Probability')
plt.title('Joint PDF')
# plt.savefig('Q2_(a).png')
plt.show()

# Part (b)
print("\nMarginal distribution of Y:")
F_Y = pd.Series(df.sum(axis=1))
print(F_Y)

print("\nMarginal distribution of X:")
F_X = pd.Series(df.sum(axis=0))
print(F_X)

# Part (c)
# PMF of X
plt.bar([0,1,2], df.sum(axis=0), edgecolor='black', color='red', linewidth=1.5)
plt.title('PMF of X')
plt.xlabel(r"$X$")
plt.ylabel(r'$f_X(x)$', rotation=0)
# plt.savefig('Q2_(c).png')
plt.show()

# Part (d)
# This part is done on paper (theoritical)

# Part (e)
print("\n\n")
dict2 = {
    0:[0.1296,0.0288,0.0016],
    1:[0.4104,0.0672,0.0024],
    2:[0.3249,0.0342,0.0009]
}

df2 = pd.DataFrame(dict2)
df2 = df2.rename_axis('Y', axis='index').rename_axis('X', axis='columns')
print(df2)


# part (g)
print("\nMarginal distribution of X:")
F_X2 = pd.Series(df2.sum(axis=0))
print(F_X2)
      
print("\n Yes. The PMF of X is affected when the bulbs are drawn with replacement, as probabilities of joint distribution will also be changed ")