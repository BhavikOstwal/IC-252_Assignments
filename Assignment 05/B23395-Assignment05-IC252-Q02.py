import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

main_file = pd.read_csv("2021_IN_Region_Mobility_Report.csv")

file = main_file[90:140]

plt.style.use('dark_background')
plt.figure(figsize=(10,6))

columns = file.columns[9:].to_numpy()
days = file['date'].to_numpy()
a = days

prob_values = [0.2, 0.2, 0.02, 0.05, 0.03, 0.5]

def Mobility(i):
    simple_mob = file.iloc[i].to_numpy()
    all_mob = simple_mob[9:]
    return all_mob

Mob0 = []
Mob1 = []
Mob2 = []
Mob3 = []
Mob4 = []
Mob5 = []

for i in range(len(days)):
    Mob0.append(Mobility(i)[0])
    Mob1.append(Mobility(i)[1])
    Mob2.append(Mobility(i)[2])
    Mob3.append(Mobility(i)[3])
    Mob4.append(Mobility(i)[4])
    Mob5.append(Mobility(i)[5])

def Expected_mobility(i):
    mob = file.iloc[i].to_numpy()
    
    mob = mob[9:]
    ans = mob.dot(prob_values)
    return ans

E_values = []
for i in range(len(days)):
    E_values.append(Expected_mobility(i))


plt.plot(days, Mob0)
plt.plot(days, Mob1)
plt.plot(days, Mob2)
plt.plot(days, Mob3)
plt.plot(days, Mob4)
plt.plot(days, Mob5)
plt.plot(days, E_values,color = 'white')

columns = [i[:-24] for i in columns]
columns.append('Expected Mobility')

plt.xticks(rotation=90)
plt.legend(columns, loc='upper right')
# plt.savefig('Q2.png')
# plt.show()
plt.clf()


'''PART (c)'''
# RMSE
rmse = []
for i in range(len(days)):
    error = 0
    for j in range(6):
        exec(f"error += (E_values[i]-Mob{j}[i])**2")
    rmse.append((error/6)**0.5)
    
plt.plot(days,rmse)


# Absolute error
absolute_err = []
for i in range(len(days)):
    error = 0
    for j in range(6):
        exec(f"error += abs(E_values[i]-Mob{j}[i])")
    absolute_err.append((error/6))
    
plt.plot(days, absolute_err)


# # KL divergence
# kl_div = []
# for i in range(len(days)):
#     error = 0
#     for j in range(6):
#         exec(f"error += Mob{j}[i]*math.log(2,abs((Mob{j}[i])/(E_values[i])))")
#     kl_div.append((error/6))
    
# plt.plot(days, kl_div)

plt.xticks(rotation=90)
plt.legend(['RMSE', 'AME'])
plt.show()