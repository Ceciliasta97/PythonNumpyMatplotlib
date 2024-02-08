# Creating a 3D plot in Matplotlib from a 3D numpy array

import numpy as np
from matplotlib import pyplot as plt


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = np.random.random(size=(3, 3, 3)) # generate a 3 * 3 * 3 array of random number between 0 and 1 
# x, y, z are arrays of indices for the non-zero elements in the "data" array
z, x, y = data.nonzero() # extract the non-zero indices of the array
ax.scatter(x, y, z, c=z, alpha=1) # create a 3D scatter plot
                                # The color (c) of each point is determined by its z value, creating a color gradient based on height.
                                # The alpha parameter: transparency of the points,  1 making the points fully opaque.
plt.show()