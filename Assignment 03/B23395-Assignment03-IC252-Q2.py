import numpy as np
import matplotlib.pyplot as plt

X_val = np.arange(0,6)
No_of_students = np.array([2,11,23,9,4,1])
# print(X_val)

n = 50
PDF_val =  No_of_students/n
# print(PDF_val.dot(X_val))

CDF_val = np.cumsum(PDF_val)


# Part (a)
print("Part (a)")
plt.figure(figsize=(12,5))

# PDF
plt.subplot(1,2,1)
plt.title("PDF")
plt.scatter(X_val,PDF_val,marker='o',color='r')
# plt.scatter(X_val, PDF_val ,marker='o', color='r')
plt.xlabel(r'$X$')
plt.ylabel(r'$P(X=x)$', rotation=0)
plt.xlim(-0.5,5.5)
plt.ylim(-0.1,1.1)
plt.grid()

# CDF
plt.subplot(1,2,2)
plt.title("CDF")
plt.hlines(CDF_val, np.arange(6),np.arange(1,7), color='r', linewidth=2.0)
plt.scatter(X_val, CDF_val,marker='o', color='r')
# plt.plot(np.arange(5,7), np.ones((2,)), color='r')
plt.plot(np.arange(-1,1), np.zeros((2,)), color='r', linewidth=2.0)
plt.xlabel(r'$X$')
plt.ylabel(r'$P(X≤x)$', rotation=0)
plt.xlim(-0.5,5.5)
plt.ylim(-0.1,1.1)
plt.grid()
# plt.savefig("Q2_(a).png")

plt.show()


# Part (b)
print("\nPart (b)")
def rep_exp(num_trials:int):
    my_val = np.random.randint(0,6,num_trials)
    unique, counts =np.unique(my_val, return_counts=True)
    mean = unique.dot(counts)/num_trials
    variance = (unique**2).dot(counts)/num_trials - mean**2
    stdeviation = variance**0.5
    return mean, stdeviation

th_mean = (np.arange(0,6)).dot((np.ones((6,)))*(0.2))
th_var = ((np.arange(0,6))**2).dot((np.ones((6,)))*(0.2)) - th_mean**2

print(f"\nFor 50 trials:")
print(f"Experimental values:\nMean = {rep_exp(50)[0]}\nStd_deviation = {rep_exp(50)[1]}")
print(f"Theoritical values:\nMean = {th_mean}\nStd_deviation = {th_var**0.5}")

print(f"\nFor 500 trials:")
print(f"Experimental values:\nMean = {rep_exp(500)[0]}\nStd_deviation = {rep_exp(500)[1]}")
print(f"Theoritical values:\nMean = {th_mean}\nStd_deviation = {th_var**0.5}")


print(f"\nFor 5000 trials:")
print(f"Experimental values:\nMean = {rep_exp(5000)[0]}\nStd_deviation = {rep_exp(5000)[1]}")
print(f"Theoritical values:\nMean = {th_mean}\nStd_deviation = {th_var**0.5}")


# Part (c)
print("\nPart (c)")
def mean_of_means(num_tr:int, picked_n:int):
    means_arr = np.empty((num_tr,))
    for i in range(num_tr):
        means_arr[i] = rep_exp(picked_n)[0]

    # Plotting Historgram
    plt.hist(means_arr ,edgecolor = 'black', color='g')
    # plt.savefig("Q2_(c).png")
    plt.show()

    # mean & var
    mean_sample = np.mean(means_arr)
    var_sample = np.var(means_arr)
    return mean_sample , var_sample 

mean_ofm, var_ofm = mean_of_means(1000,500)
print(mean_ofm, var_ofm)