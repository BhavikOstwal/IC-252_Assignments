import math
import numpy as np
import matplotlib.pyplot as plt

class BivariateGaussian:
    def __init__(self, mean_x, mean_y, var_x, var_y, cov):
        self.mean_x = mean_x;
        self.mean_y = mean_y;
        self.var_x = var_x;
        self.var_y = var_y;
        self.cov = cov;
        self.std_x = var_x**0.5
        self.std_y = var_y**0.5
        self.cor = cov/(self.std_x*self.std_y)

    def calculate_pdf(self,x,y):
        rho = self.cov / (self.std_x * self.std_y)
        z = ((x - self.mean_x) / (self.std_x)) ** 2 - (2 * rho * (x - self.mean_x) * (y - self.mean_y)) / (
                    self.std_x * self.std_y) + ((y - self.mean_y) / (self.std_y)) ** 2
        return np.exp(-z / (2 * (1 - rho ** 2))) / (2 * np.pi * self.std_x * self.std_y * ((1 - rho ** 2) ** 0.5))

    def marginal_pdf_x(self, x):
        return math.exp(-0.5*((x-self.mean_x)/(self.std_x))**2)/(self.std_x*math.sqrt(2*math.pi))
    
    def marginal_pdf_y(self, y):
        return math.exp(-0.5*((y-self.mean_y)/(self.std_y))**2)/(self.std_y*math.sqrt(2*math.pi))
        
    def plot_pdf_contour(self):
        x_range = 10
        y_range = 10
        num_points = 100
        x = np.linspace(self.mean_x - x_range * self.std_x, self.mean_x + x_range * self.std_x, num_points)
        y = np.linspace(self.mean_y - y_range * self.std_y, self.mean_y + y_range * self.std_y, num_points)
        X, Y = np.meshgrid(x, y)
        Z = self.calculate_pdf(X, Y)
        plt.contour(X, Y, Z, cmap='viridis')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Bivariate Gaussian PDF Contour Plot')
        plt.show()



distribution = BivariateGaussian(2,3,16,25,0.2)
pdf_value = distribution.calculate_pdf(1,1)
print(pdf_value)
marginal_pdf_x = distribution.marginal_pdf_x(1.0)
print(marginal_pdf_x)
distribution.plot_pdf_contour()