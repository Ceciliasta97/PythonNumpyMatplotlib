import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(-3,3,50) # 50 points from -1 to 1
y1 = 2 * x + 1
y2 = x ** 2

plt.figure() 
plt.plot(x, y1)  

plt.figure(num = 2, figsize = (8,5))  # setting figure = 3
plt.plot(x, y2)  #figure 3
plt.plot(x, y1, color = "red", linewidth = 2.0, linestyle = "--")  # draw second line in the same figure

plt.xlim((-1, 2))  # the range of x
plt.ylim((-2, 3))# range of y
plt.xlabel(' i am x') # dexcription of x
plt.ylabel('i am y')

plt.show()

