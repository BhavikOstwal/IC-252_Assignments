import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open("fileA-TimeMachine.txt", 'r') as my_txt:
# with open("t.txt", 'r') as my_txt:
    a = my_txt.read().strip().split()
    # a = a.strip('.').lstrip('(,\"').rstrip('.\"').split()
    lst = []
    for i in a:
        lst.append(i.lstrip('\'_("“‘’*').rstrip('\'_”).";—!?,:‘’ …*'))

print(lst)

unique, counts = np.unique(lst, return_counts=True)



# Frequency
tab = pd.DataFrame(counts, unique)
# print(tab)


# PDF
prob = []
for i in range(len(unique)):
    prob.append(counts[i]/len(lst))

plt.bar(unique, prob)
# plt.xticks(counts, rotation=90)
plt.show()