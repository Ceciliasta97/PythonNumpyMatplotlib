import numpy as np
import matplotlib.pyplot as plt


#learn subplot

plt.figure()


# create xiao tu
plt.subplot(2, 1, 1) # the figure has two row, tow columns, in the first position.
plt.plot([0,1], [0, 1]) # the coord of x and y

# create xiao tu
plt.subplot(2, 3, 4) #  first subplot account for whole row(three column, so next subplot is 4th)
plt.plot([0,1], [0, 2]) # the coord of x and y

# create xiao tu
plt.subplot(235) #  2, 2, 3 == 223
plt.plot([0,1], [0, 3]) # the coord of x and y

# create xiao tu
plt.subplot(2, 3, 6) # the figure has two row, tow columns, in the first position.
plt.plot([0,1], [0, 1]) # the coord of x and y


plt.show()

