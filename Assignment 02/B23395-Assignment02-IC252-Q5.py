import numpy as np
import matplotlib.pyplot as plt

choices_arr = np.array([0,0,1])

def MontyHall(switch=True):
    win_freq = 0
    for i in range(10000):
        np.random.shuffle(choices_arr)
        index = np.random.randint(0,3)
        for i in range(3):
            if (choices_arr[i]==0) and (index!=i):
                host_choice=i
                break
        if (switch):
            final_choice = 3-(index+host_choice)
        else:
            final_choice=index

        if(choices_arr[final_choice]==1):
            # print("CAR")
            win_freq+=1
    return win_freq


counts = np.array([MontyHall(True), MontyHall(False)], dtype=np.int32)
probabilities = counts/10000

plt.style.use('dark_background')
plt.title('\'Monty-Hall\' Game Probability Distribution')
plt.bar(["Switch", "Stick"],probabilities, color='green',edgecolor='white', width=0.5)
plt.ylabel("Probability of winning the Car")
plt.xlabel("Decision of the Player")
plt.ylim(0,1)
# plt.savefig("Q5.png")
plt.show()
# print((MontyHall(True)+ MontyHall(False))/10000) --> it won't necessarily be equal to 1





