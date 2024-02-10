import numpy as np
import matplotlib.pyplot as plt

# learn Bar

n = 12  # 12 bars 
X = np.arange(n)  
Y1 = (1-X / float(n)) * np.random.uniform(0.5, 1.0, n) # uniform distribution
Y2 = (1-X / float(n)) * np.random.uniform(0.5, 1.0, n) # so create 23 Y1 and 12 Y2

plt.bar(X, +Y1, facecolor='#9999ff',edgecolor='white') # this bar is up ward
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white') # edge color: border color


# create text(value) of each bar (upward bar)
for x , y in zip(X, Y1):
    plt.text( x + 0.04, y + 0.05, '%.2f' %y  , ha = 'center', va = 'bottom' ) # put x and y separately inside S and Y1
                                            # %.2f : 2 digital 

# create text(value) of each bar (downward bar)
for x , y in zip(X, Y2):
    plt.text( x + 0.04, -y - 0.05, '%.2f' %y  , ha = 'center', va = 'top' ) # put x and y separately inside S and Y2
                                            # %.2f : 2 digital 
                                            # ha : horizontal alignment.   va : vertial alignment

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())




plt.show()
