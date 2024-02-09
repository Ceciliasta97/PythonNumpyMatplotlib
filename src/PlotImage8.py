# How to annotate a heatmap with text in Matplotlib?

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

data = np.random.rand(4, 4) # create random data with 4 * 4 dimension array
heatmap = plt.pcolor(data, cmap="PuBuGn_r") # pcolor() creates a pseudocolor plot (heatmap) with a rectangular grid, 
                                            # using the values in data to determine the color of each cell
                                            # cmap="PuBuGn_r" argument specifies the colormap :
                                            # a reversed Purple-Blue-Green gradient, to color the cells based on their values.
for y in range(data.shape[0]):
   for x in range(data.shape[1]):
      plt.text(x + 0.5, y + 0.5, '%.4f' % data[y, x], # text() : put text in the pixels
         horizontalalignment='center',
         verticalalignment='center',
      )
plt.show()