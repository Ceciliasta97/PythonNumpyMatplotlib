import numpy as np
import matplotlib.pyplot as plt

# learn annotation

x =np.linspace(-3,3,50) # 50 points from -1 to 1
y = 2 * x + 1

plt.figure(num = 2, figsize = (8,5))  
plt.plot(x,y)

ax = plt.gca()
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom') 
ax.spines['bottom'].set_position(('data', 0)) 

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s= 50, color = 'b') # plot(): draw a line.   scatter() : draw a continous dot
                                        # s : size = 50,   b : black
plt.plot([x0, x0], [y0,0], 'k--' , lw = 2.5)  #  k : black.    k--: black dotted line.    lw: linewidth

# annotation method 1
plt.annotate('$2x+1=%s$' % y0, xy = (x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize = 16, arrowprops=dict(arrowstyle = '->', connectionstyle = 'arc3, rad=.2'))

# annotation method 2
plt.text(-3.7, 3, r'$this\ is\ a\ sample\ text. \mu\ \sigma_i\ \alpha_t$', 
         fontdict={'size':16, 'color':'r'})

plt.show()

