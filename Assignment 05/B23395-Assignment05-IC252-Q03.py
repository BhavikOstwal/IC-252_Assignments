import numpy as np
import matplotlib.pyplot as plt

step = [-1,1]

def random_walk(num_steps:int, prob_val:list):
    final_locations = []
    for i in range(10000):
        strt_pt = 0
        for j in range(num_steps):
            strt_pt += np.random.choice(step, p=prob_val)
        final_locations.append(strt_pt)
    return final_locations

# print(random_walk(100))

def plot_pdf(num_steps:int, prob_val:list, part:str):
    unique, count = np.unique(random_walk(num_steps, prob_val), return_counts=True)
    plt.bar(unique, count/10000)
    # plt.savefig(f"Q.3_{part}_{num_steps}.png")
    plt.show()
    plt.clf()

'''PART (a)'''
prob_lst = [0.5,0.5]

# For n = 100 steps
plot_pdf(100, prob_lst, part='a')
# For n = 1000 steps
plot_pdf(1000, prob_lst, part='a')
# For n = 10000 steps
plot_pdf(10000, prob_lst, part='a')


'''PART (b)'''
prob_lst = [0.4,0.6]

# For n = 100 steps
plot_pdf(100, prob_lst, part='b')
# For n = 1000 steps
plot_pdf(1000, prob_lst, part='b')
# For n = 10000 steps
plot_pdf(10000, prob_lst, part='b')


