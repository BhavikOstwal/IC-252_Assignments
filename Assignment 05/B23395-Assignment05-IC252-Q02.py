import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

main_file = pd.read_csv("2021_IN_Region_Mobility_Report.csv")

for_days = main_file[90:140]
a = []
a1 = []

plt.figure(figsize=(18,13))

for i in range(10):
    # exec(f"file{i} = file[90+365*i:140+365*i]")
    # file = main_file[90+365*i:140+365*i]
    file = main_file[239064+365*i:239114+365*i]

    columns = file.columns[9:]
    days = file['date'].to_numpy()
    a = days
    
    # regions
    a = file.iloc[0].to_numpy()
    a1.append(a[3])

    prob_values = [0.2, 0.2, 0.02, 0.05, 0.03, 0.5]

    def Expected_mobility(i):
        mob = file.iloc[i].to_numpy()
        
        mob = mob[9:]
        ans = mob.dot(prob_values)
        return ans

    E_values = []
    for i in range(len(days)):
        E_values.append(Expected_mobility(i))

    plt.plot(days, E_values)


plt.xticks(rotation=90)
plt.legend(a1)
plt.savefig('Q2.png')
plt.show()


# Calculating RMSE
def calculate_rmse(true_values, predicted_values):
    return np.sqrt(np.mean((true_values - predicted_values) ** 2))

true_mobilities = np.random.rand(len(E_values))  

mobilities = main_file.iloc[239064+365*0:239114+365*0, 9:].to_numpy()
predicted_mobilities = np.array([Expected_mobility(j) for j in range(len(mobilities))])  

rmse = calculate_rmse(true_mobilities, predicted_mobilities)
print(f"RMSE = {rmse}")

# Calculating absolute error
def calculate_absolute_error(true_values, predicted_values):
    return np.mean(np.abs(true_values - predicted_values))

true_mobilities = np.random.rand(len(E_values))  

mobilities = main_file.iloc[239064+365*0:239114+365*0, 9:].to_numpy()
predicted_mobilities = np.array([Expected_mobility(j) for j in range(len(mobilities))])  

absolute_error = calculate_absolute_error(true_mobilities, predicted_mobilities)
print(f"Absolute Error = {absolute_error}")

