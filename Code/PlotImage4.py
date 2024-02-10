import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure() 
ax1 = fig.add_subplot(111, projection='3d') 
                                           
# x3, y3, z3 defines the position 
x3 = [1, 2, 3, 4, 6, 7, 8, 10] 
y3 = [5, 6, 7, 8, 2, 2, 6, 7]
z3 = np.zeros(8) #  z3 should match the lengths of x3, y3, and dz

# dx, dy : width and depth of each bar
dx = np.zeros(8) 
dy = np.ones(8)
dz = [1, 2, 3, 4, 5, 7, 6, 9] # height of bars range from 1 to 10

ax1.bar3d(y3, x3, z3, dx, dy, dz, color="red") 
ax1.axis('off') # axes and their labels will not be displayed

plt.show()