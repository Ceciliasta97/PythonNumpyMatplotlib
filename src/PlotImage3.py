import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure() # createa a new figure
ax1 = fig.add_subplot(111, projection='3d') # adds a subplot to the figure with a 3D projection
                                            # 111: 1 row, 1 column, first subplot
# x3, y3, z3 defines the position 
x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
y3 = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z3 = np.zeros(10)

# dx, dy : width and depth of each bar
dx = np.ones(10) # means 1 for all bars
dy = np.ones(10) # so all bars have same width and depth
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # height of bars range from 1 to 10

ax1.bar3d(y3, x3, z3, dx, dy, dz, color="red") # plot the 3D bars
ax1.axis('off') # axes and their labels will not be displayed

plt.show()