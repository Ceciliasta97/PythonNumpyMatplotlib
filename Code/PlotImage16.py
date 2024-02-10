import numpy as np
import matplotlib.pyplot as plt

# learn scatter

n = 1024
X = np.random.normal(0,1,n)  # random generate value
Y = np.random.normal(0,1,n) # mean = 0, standard dev1ation = 1
T = np.arctan2(Y,X) #  T : for color value


plt.scatter(X, Y, s = 75, c = T, alpha = 0.5 ) # size = 75, color = T (color is varied due to color map(T is random))
                                                # X, Y : coordinates
# plt.scatter(np.arange(5), np.arange(5))  # see the scatter point in a linear line 

plt.xlim((-1.5, 1.5))  # x range
plt.ylim((-1.5,  1.5))

plt.xticks(())  # hide all ticks
plt.yticks(())

plt.show()
