import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection="3d")  # 3d model

X, Y = np.mgrid[-3:3:100j, -3:3:100j]
Z = np.exp(-X**2 - Y**2)

# Use plot_surface function to draw a rotating paraboloid with colors set to rainbow
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

ax.set_zlim(-0.1, 1)  # Limit z-axis coordinates to (-0.1, 1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")  # Set labels for the XYZ axes

plt.show()  # Correct way to display the plot
