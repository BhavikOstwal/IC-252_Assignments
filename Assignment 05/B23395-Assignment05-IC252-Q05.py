import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def Monte_carlo_sim(n):
    count = 0
    for i in range(n):
        z = np.random.rand()
        theta = np.random.uniform(0,np.pi)
        if (z<=np.sin(theta)/2 or 1-z<=np.sin(theta)/2 ):
            count+=1
    if count==0:
        return 1000 # a big number like infinity
    return (2*n)/count

# print(Monte_carlo_sim(10000))


# Now animating
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlim(1, 3000)
ax.set_ylim(0, 5)
line, = ax.plot([], [], lw=1, color='green')
line2, = ax.plot([], [], lw=1, color='blue')

def init():
    line.set_data([], [])
    return line,


x = np.arange(1,3000,1)
y = np.empty((len(x), ))
for i in range(len(x)):
    y[i] = Monte_carlo_sim(x[i])

line2.set_data(x, np.pi*np.ones((len(x),)))


def animate(i):
    ax = x[:i+1]
    ay = y[:i+1]
    line.set_data(ax,ay)
    return line,


ani = FuncAnimation(fig, animate, init_func=init, frames=3000, interval=1, blit=True, repeat=False)

plt.show()