import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec # for method 2

# learn subplot 

# method 1 : subplot2 grid
plt.figure()
ax1 = plt.subplot2grid((3, 3), (0,0), colspan=3, rowspan=1)  # 3 rows 3 columns # 0,0 : first row, first column
                                                            # this figure accounts the space : 1 row, 3 columns
ax1.plot([1,2], [1,2])
ax1.set_xlabel # if ax1 , write ax1.set_xlabel.   If figure, write figure.xlabel
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3, 3), (1,0), colspan=2) # (1, 0): the subplot starts from the second row, first column
ax3 = plt.subplot2grid((3, 3), (1,2), rowspan=2) # (2, 3): second row, third column.  rowspan = 2: subplot has two rows
ax4 = plt.subplot2grid((3, 3), (2,0)) 
ax5 = plt.subplot2grid((3, 3), (2,1)) 

# every subplot need "plt.figure()"
# method 2 : gridspec
plt.figure()
gs = gridspec.GridSpec(3, 3) # 3 rows, 3 columns
ax1 = plt.subplot(gs[0, :]) # first row, accoutns for all columns (3)
ax2 = plt.subplot(gs[1, :2]) # second row, acoounts for first two column
ax3 = plt.subplot(gs[1:, 2]) # second row, third column
ax4 = plt.subplot(gs[-1, 0]) # 
ax5 = plt.subplot(gs[-1, -2])

# method 3 : easy to define structure
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True) # want to share x axis and y axis
                                                                            #(so 2nd and 4th square share x axis with 1st and 3rd square)
                                    # (ax11, ax12) : subplot in first row
                                    # (ax21, ax22) : subplot in second row
ax11.scatter([1, 2], [1,2]) # plot point in first subplot




plt.tight_layout()  # make plot for the figure
plt.show()