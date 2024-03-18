import numpy as np
import matplotlib.pyplot as plt

# Based on the given data, between 17th April 2020 and 23rd April 2020, there were on average 1373 confirmed cases per day, i.e. on average around 57 cases per hour.
# To model time to the arrival of the next confirmed case of Covid-19 in India, we'll be using the exponential distribution.


class Exp_dist:
    def __init__(self, lmda:float):
        self.lambda_exp = lmda
        self.Mean = 1/lmda
        self.Variance = 1/(lmda**2)

    def PDF_fn(self, x:float):
        if (x>=0) and (self.lambda_exp>0):
            return (self.lambda_exp)*(np.e**(-self.lambda_exp*x))
        else:
            return None

    def CDF_fn(self, x:float):
        if (x>=0) and (self.lambda_exp>0):
            return 1 - np.e**(-self.lambda_exp*x)
        else:
            return None


lambda_exp = 57

Exp_d = Exp_dist(lambda_exp)
# print(Exp_d.Mean)

#  Plotting PDF
pdf_lst = []
x_lst = []
for i in np.arange(0,0.3,0.001):
    pdf_lst.append(Exp_d.PDF_fn(i))
    x_lst.append(i)
    # print(f"At x = {i}, PDF = {Exp_d.PD/F_fn(i)}")


plt.plot(x_lst, pdf_lst)
plt.savefig("Q1.png")
# plt.show()

# Part (b)
print('\n\nPART (b)')
print(f'The probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute = {Exp_d.CDF_fn(1/60)}')

#  Part (c)
print('\n\nPART (c)')
print(f'The probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes = {Exp_d.CDF_fn(2/60) - Exp_d.CDF_fn(1/60)}')

#  Part (d)
print('\n\nPART (d)')
print(f'The probability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes = {1-Exp_d.CDF_fn(2/60)}')

#  Part (e)
print('\n\nPART (e)')
print('The average number of cases per hour doubled,')
print('So, new lamda = 2 x 57')
Exp_d_new = Exp_dist(2*lambda_exp)
print(f'The probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes = {Exp_d_new.CDF_fn(2/60) - Exp_d_new.CDF_fn(1/60)}')
