import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
joint_prob = {
    "T-Shirt":[0.1,0.05,0.1],
    "Sweater":[0.05,0.1,0.2],
    "Jacket":[0.1,0.2,0.1]
}
df = pd.DataFrame(joint_prob,index=['Sunny', 'Rainy', 'Cloudy'])
# df.to_csv('joint_prob.csv')
print(df, "\n")

df['F_Y(y)'] = pd.Series(df.sum(axis=1))
df.loc['F_X(x)'] = pd.Series(df.sum(axis=0))
# df.to_csv('marginal_prob.csv')
print(df, "\n")

clothing_choice = ["T-Shirt", "Sweater", "Jacket"]
weather = ['Sunny', 'Rainy', 'Cloudy']


def choose_with_dependent_bias(item_from_list1):
    probabilities = joint_prob[item_from_list1]
    return random.choices(weather, probabilities, k=1)[0]


lst = []
for i in range(1000000):
    a = np.random.choice(clothing_choice)
    lst.append((a,choose_with_dependent_bias(a)))
    

    
freq = lst.count(('Sweater', 'Cloudy'))/1000000
print(freq)
