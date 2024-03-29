import numpy as np
import matplotlib.pyplot as plt

# learn coordinates

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx() # creates a twin Axes sharing the same x-axis as ax1. 
                # allows two different y-axes to be plotted on the same figure, with the same x-axis.
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color = 'g')
ax2.set_ylabel('Y2', color = 'b')






plt.show()