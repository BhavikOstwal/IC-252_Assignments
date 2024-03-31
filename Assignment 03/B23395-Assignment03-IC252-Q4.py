import numpy as np
from math import comb

# Part (a)
print("Part (a)")
theor_prob = (comb(4,3) * comb(13,1) * comb(4,2) * comb(12,1))/comb(52,5)
print("Probability of getting a full house =",theor_prob)

# Part (b)
print("\nPart (b)")
ranks_arr = np.arange(0,13)
ranks_arr = np.tile(ranks_arr,4)

def win_experiment(num_trials:int):
    win_count = 0
    for i in range(num_trials):
        np.random.shuffle(ranks_arr)
        my_hand = []
        for j in range(5):
            my_hand.append(ranks_arr[j])
        unique, count = np.unique(my_hand, return_counts=True)
        if (len(unique)==2):
            if (count[0]-count[1]==1)|(count[1]-count[0]==1):
                win_count+=1

    return win_count


num_trials = 10000
exp_prob = win_experiment(num_trials)/num_trials
print("Experimental value:",exp_prob)
print("Theoritical value:",theor_prob.__format__(".6f"))
 
# Part (c)
print("\nPart (c)")
c = 0
win_counts = []
num_tr = 10000

for i in range(num_tr):
    p = win_experiment(1000)
    win_counts.append(p)
    if p>=2:
        c+=1


print("Experimental value =", c/num_tr)
theritical_val = (1-(1-theor_prob)**1000) - comb(1000,1) * ((1-theor_prob)**999) * theor_prob
print(f"Theoritical value = {theritical_val:.5f}" )

print("\nMean:",np.average(win_counts))
print("Variance:",np.var(win_counts).__format__("0.6f"))


