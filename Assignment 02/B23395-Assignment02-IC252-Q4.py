import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table


result_val = np.empty((10000,))
for i in range(10000):
    a = np.random.randint(1,7)
    b = np.random.randint(1,7)
    result_val[i] = a+b


unique_sums, counts = np.unique(result_val, return_counts=True)
unique_sums = unique_sums.astype(np.int32)
probabilities = counts/len(result_val)

# print(counts, type(counts))
# print(unique_sums, type(unique_sums))

table_df = pd.DataFrame(
    {
        'Sums': unique_sums,
        'Frequency(out of 10000)': counts
    }
)

print(table_df)
# print(plt.style.available)
plt.figure(figsize=(13,5))

# To display table side-by-side of my graph, I use pandas documentation
subplt = plt.subplot(1,2,1)
plt.axis('off')
tab = table(subplt, table_df, loc='center', colWidths=[0.3,0.3], fontsize=15)     #referred to website for plotting Dataframe Table side by side to histogram

# plt.subplot(1,2,2)
plt.bar(unique_sums, probabilities, color='green', edgecolor='black', alpha=0.7)
plt.title('Probability Distribution of the Sum of Two Dice')
plt.xlabel('Sum')
plt.ylabel('Probability')
plt.xticks(np.arange(2, 13))
plt.grid(axis='y')
# plt.savefig("Q4.png")
plt.show()
