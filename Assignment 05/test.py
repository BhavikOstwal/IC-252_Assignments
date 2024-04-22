import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function whose convergence we want to visualize
def f(x):
    return np.cos(x)

# # Generate the data
# x_values = np.linspace(0, 10, 100)
# y_values = f(x_values)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.2, 1.2)
line, = ax.plot([], [], lw=2)

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: update the plot with new data for each frame
def animate(i):
    x = np.linspace(0, 10, 500)
    y = f(x)
    x = x[:i]
    y = y[:i]
    line.set_data(x, y)
    return line,

# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=400, interval=100, blit=True)

plt.show()
