import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open("fileA-TimeMachine.txt", 'r') as my_txt:
    a = my_txt.read().strip().split()
    lst = []
    for i in a:
        lst.append(i.lstrip('\'_("“‘’*').rstrip('\'_”).";—!?,:‘’ …*'))

# print(lst)

unique, counts = np.unique(lst, return_counts=True)

# Frequency
tab = pd.DataFrame(counts, unique)
# print(tab)

# PDF
prob = []
for i in range(len(unique)):
    prob.append(counts[i]/len(lst))

# print(np.where((counts==max(counts))))
# print(unique[5030])
plt.bar(unique, counts/len(lst))
plt.xticks(unique, rotation=90)
plt.savefig("Q1.png")
plt.show()
# plt.clf()



'''PART (b)'''
lst_pairs = []
for i in range(len(lst)):
    if (len(lst[i])>=2):
        for j in range(len(lst[i]) - 1):
            if(len(lst[i][j:j+2].lower().lstrip('\'_("“‘’*').rstrip('\'_”).";—!?,:‘’ …*')) == 2):
                lst_pairs.append(lst[i][j:j+2].lower())

unique_pairs, count_pairs = np.unique(lst_pairs, return_counts=True)

u = pd.Series(unique_pairs)
c = pd.Series(count_pairs)

df = pd.DataFrame(u)
df['counts'] = c
df = df.sort_values(by=['counts'],ascending=False)
df = df.head(10)
top_pairs = df[0].to_numpy()
top_counts = df['counts'].to_numpy()

plt.bar(top_pairs, top_counts/len(lst_pairs))
# plt.savefig('Q1_b.png')
# plt.show()

'''PART (c)'''
with open("fileA-TimeMachine.txt", 'r') as my_txt:
    a = my_txt.read().strip().split()
    # a = a.strip('.').lstrip('(,\"').rstrip('.\"').split()
    lst1 = []
    for i in a:
        lst1.append(i)

lst_pairs = []
for i in range(len(lst1)):
    if (len(lst1[i])>=2):
        for j in range(len(lst1[i]) - 1):
            if(len(lst1[i][j:j+2].lower()) == 2):
                lst_pairs.append(lst[i][j:j+2].lower())

unique_pairs, count_pairs = np.unique(lst_pairs, return_counts=True)

u = pd.Series(unique_pairs)
c = pd.Series(count_pairs)

df = pd.DataFrame(u)
df['counts'] = c
df = df.sort_values(by=['counts'],ascending=False)
df = df.head(10)
top_pairs = df[0].to_numpy()
top_counts = df['counts'].to_numpy()

print("\nPart(c):")
print(top_counts/len(lst_pairs))
