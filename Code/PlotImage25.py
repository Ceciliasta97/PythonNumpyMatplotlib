import numpy as np
import matplotlib.pyplot as plt

# learn subplot
fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

# first big figure
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 # the percentage of size of graph in the figure 
ax1 = fig.add_axes([left, bottom, width, height]) # add an axes
ax1.plot(x, y, 'r') # plot the data of x, and y, with color "red"
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

# second small figure
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25 # the percentage of the figure 
ax1 = fig.add_axes([left, bottom, width, height]) # add an axes
ax1.plot(y, x, 'b') # plot the data of x, and y, with color "red"
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('inside 1')

# another method to define figure
plt.axes([.6, .2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('inside 2')




plt.show()