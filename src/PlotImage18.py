import numpy as np
import matplotlib.pyplot as plt

# learn Contours   (deng gao xiantu)

def f(x, y):
    # theheightfunction
    return( 1-x / 2 + x**5 + y**3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n) # x y each has 256 points
y = np.linspace(-3, 3, n)

# match X, Y
X, Y = np.meshgrid(x, y)

# uaw plt.contourfto filling contours
#X Y andvalue for (X Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha= 0.75, cmap = plt.cm.hot) # function "contour" : deng gao xian.    contourf() : filling the color inside contour 
                                # cmap = plt.cm.hot : color map the color of cmap is dependon the value.


# useplt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth= .5)  # 8: contour line
# adding label
plt.clabel(C,inline=True, fontsize=10) # give thevalue of each contour line

plt.xticks(())
plt.yticks(())
plt.show()
