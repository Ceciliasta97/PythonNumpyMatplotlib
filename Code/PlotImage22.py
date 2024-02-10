import numpy as np
import matplotlib.pyplot as plt

plt.figure()


# create xiao tu
plt.subplot(2, 2, 1) # the figure has two row, tow columns, in the first position.
plt.plot([0,1], [0, 1]) # the coord of x and y

# create xiao tu
plt.subplot(2, 2, 2) # the figure has two row, tow columns, in the second position.
plt.plot([0,1], [0, 2]) # the coord of x and y

# create xiao tu
plt.subplot(223) #  2, 2, 3 == 223
plt.plot([0,1], [0, 3]) # the coord of x and y

# create xiao tu
plt.subplot(2, 2, 4) # the figure has two row, tow columns, in the first position.
plt.plot([0,1], [0, 1]) # the coord of x and y


plt.show()

