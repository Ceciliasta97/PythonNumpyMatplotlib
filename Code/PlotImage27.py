import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()  # create a figure and axis

x = np.arange(0, 2*np.pi, 0.01)  
line, = ax.plot(x, np.sin(x))  # (x, y)  # returns a line object


def animate(i): # i represent frame number
    line.set_ydata(np.sin(x + i / 40))  # increase the speed: 1 / < 40  # shafting phase # updating y values
    return line,

def init(): # define the initial figure of the animation
    line.set_ydata(np.sin(x))
    return line,
    

ani = animation.FuncAnimation(fig = fig, func = animate, frames = 1000, init_func=init, interval=10, blit=False)
# fig = fig : the figure object(fig) that the animation will be drawn
# frames : total number of frames
# interval : delay between frames in ms
# blit = false : entire figure will be drawn at each frame

plt.show()



