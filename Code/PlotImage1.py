import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]  # width and height of the figure in inches.
plt.rcParams["figure.autolayout"] = True  # enabling automatic adjustment of the layout,, avoid overlapping.

# read and display image
im = plt.imread("minion.png")
fig, ax = plt.subplots()  # create a figure and a subplot
im = ax.imshow(im, extent=[0, 300, 0, 300]) # display the image on the axes
                                            # extent : defines the bounds of the image
# plot a dotted line
x = np.array(range(300)) # generates an array from 0 - 299
ax.plot(x, x, ls='dotted', linewidth=2, color='red') # ax.plot(x, x, ...) plots a line on the axes. 
plt.show() # display the figure
