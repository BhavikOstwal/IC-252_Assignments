import matplotlib.pyplot as plt
import numpy as np

val=np.random.normal(size=(500), scale=5, loc=30)

bins=np.arange(10,50,2)
# print(bins)

plt.hist(val, bins=bins, edgecolor = 'black', color = 'r')
plt.xlabel('Opening price')
plt.ylabel('Number of occurrences')
plt.title('Normal distribrution')
# plt.xticks(bins)
# plt.grid()
plt.savefig("Q.2.png")
plt.show()