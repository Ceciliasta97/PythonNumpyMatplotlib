import numpy as np
import matplotlib.pyplot as plt

#createa a visual representation of a vector field
# using "numpy" for calculations and "matplotlib"  for plotting

plt.rcParams["figure.figsize"] = [7.50, 3.50]

n = 8  # size of grid = 8 * 8
X, Y = np.mgrid[0:n, 0:n]  # Creates a mesh grid of X and Y coordinates ranging from 0 to 7 (since n=8).
T = np.arctan2(Y - n / 2., X - n/2.) # calculate the angle "T" for each point in the grid relative to the center (n / 2, n / 2)
                                    # "np.arctan2" computes the angle between the positive x-axis and the point(Y-n/2, X-n/2)
R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2) # compute the magnitue R of eavh vector in the grid. 
                                                            # offset of "10": ensure all magnitures are positive
U, V = R * np.cos(T), R * np.sin(T)  # Calculates the x (U) and y (V) based on magnitude "R" and angle "T"

fig, ax = plt.subplots() # plot vector Field
ax.quiver(X, Y, U, V, R, cmap="copper")  # plot the vector field using "quiver" function (plots vectors as arrows at the grid points (X, Y))
                                        # color represents R. The color map copper is used to differentiate the magnitudes.
fig.tight_layout() # adjust the subplot parameters , prevent overlapping

plt.show() #display the figure
