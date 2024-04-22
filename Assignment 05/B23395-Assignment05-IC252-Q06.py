import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x):
    return (np.sin(3*x))**4

def Integral_sim(n):
    count = 0
    for i in range(n):
        x = np.random.uniform(0,np.pi)
        y = np.random.uniform(0,1)
        if y<=f(x):
            count+=1
    return count*(np.pi)/n

# print(Integral_sim(100000))


# Now animating
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlim(1, 2500)
ax.set_ylim(0, 5)
line, = ax.plot([], [], lw=1, color='green')

def init():
    line.set_data([], [])
    return line,


x = np.arange(1,2000,1)
y = np.empty((len(x), ))
for i in range(len(x)):
    y[i] = Integral_sim(x[i])

def animate(i):
    ax = x[:i+1]
    ay = y[:i+1]
    line.set_data(ax,ay)
    return line,


ani = FuncAnimation(fig, animate, init_func=init, frames=2000, interval=1, blit=True, repeat=False)

plt.show()

plt.clf()
plt.cla()


def f(x):
    return 3*(np.pi)/8

def Second_Integral_sim(n):
    count = 0
    for i in range(n):
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1.5)
        if y<=f(x):
            count+=1
    return count*(1.5)/n


# Now animating
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlim(1, 2500)
ax.set_ylim(0, 5)
line, = ax.plot([], [], lw=1, color='green')

def init():
    line.set_data([], [])
    return line,


x = np.arange(1,2000,1)
y = np.empty((len(x), ))
for i in range(len(x)):
    y[i] = Integral_sim(x[i])

def animate(i):
    ax = x[:i+1]
    ay = y[:i+1]
    line.set_data(ax,ay)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=2000, interval=1, blit=True, repeat=False)

plt.show()

