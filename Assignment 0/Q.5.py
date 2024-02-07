import numpy as np
import matplotlib.pyplot as plt

x_inp = np.arange(-15*np.pi/2, 15*np.pi/2,0.01)

def sin(x:float):
    return np.sin(x)

def cos(x:float):
    return np.cos(x)

y_sin = sin(x_inp)
y_cos = cos(x_inp)

plt.style.use('dark_background')
plt.figure(figsize=(20,6))

plt.subplot(1,2,1)
plt.title('Sine Graph', fontsize=30)
plt.grid()
plt.plot(x_inp, y_sin,label = 'sin(x)', color = 'red', linewidth = 2)
plt.ylim(-2,2)
plt.xlim(-20,20)
plt.xlabel("x", fontsize=20)
plt.ylabel("sin(x)", fontsize=20)
plt.legend()

plt.subplot(1,2,2)
plt.title('Cosine Graph', fontsize=30 )
plt.grid()
plt.plot(x_inp, y_cos, label = 'cos(x)', color='yellow', linewidth = 2)
plt.xlim(-20,20)
plt.ylim(-2,2)
plt.xlabel("x", fontsize=20)
plt.ylabel("cos(x)", fontsize=20)
plt.legend()
plt.savefig('Q.5.png')

# plt.show()
