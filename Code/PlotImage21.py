import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# learn 3D
fig = plt.figure()
ax = plt.axes(projection="3d")  # 3d model


# X, Y value
X = np.arange(-4, 4, 0.25)  # range from -4 to 4 with a step of 0.25
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y) # Generates a 2D grid from the X and Y arrays. 
                        #  so each point (X, Y) on the grid will have a corresponding Z value.
R = np.sqrt(X **2 + Y**2 )

# height value
Z = np.sin(R) # create a wave-like surface in 3D.


ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap = plt.get_cmap('rainbow')) # rstride : row stride  cstride : column
                                         # rstride, cstride: control the row and column stride (step size for sampling the data)

ax.contourf(X, Y, Z, zdir ='z',offset=-2, cmap='rainbow') # Adds a filled contour plot beneath the surface plot


plt.show()


