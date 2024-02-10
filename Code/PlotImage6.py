# How to plot a 3D continuous line in Matplotlib?

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(-4 * np.pi, 4 * np.pi, 50) # generates 50 linearly spaced value between -4Pi and 4Pi for x-axis
y = np.linspace(-4 * np.pi, 4 * np.pi, 50) # for y-axis
z = -x ** 3 - y ** 2  # calculate x, y, z (all are 1d array)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # adds a 3D subplot
ax.plot(x, y, z)
plt.show()