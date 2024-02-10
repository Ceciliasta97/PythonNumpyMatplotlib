import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(-3,3,50) # 50 points from -1 to 1
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num = 2, figsize = (8,5))  # setting figure = 3
plt.plot(x, y2)  #figure 3
plt.plot(x, y1, color = "red", linewidth = 2.0, linestyle = "--")  # draw second line in the same figure

plt.xlim((-1, 2))  
plt.ylim((-2, 3))
plt.xlabel(' i am x') 
plt.ylabel('i am y')

new_ticks = np.linspace(-1, 2,5)  # change tick in x / y axis
print (new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.5, -1,  1.22,  3],
        ['$really\ bad$', r'$bad\ \alpha$' ,r'$normal$',r'$good$' ,'$really\ good$']) 
       
# gca : 'getcurrent axis '
ax = plt.gca()  # ax represent the graph (line 4 - line 23)
ax.spines['right'].set_color('none')  # make the right spine line disappear
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom') # setting defalut x axis
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0)) # x zhou bang ding zai y zhou 0 de weizhi
                                            # x axis stay at the position where y = 0
ax.spines['left'].set_position(('data', 0))



plt.show()

