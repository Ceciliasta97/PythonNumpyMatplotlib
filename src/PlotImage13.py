import numpy as np
import matplotlib.pyplot as plt

## learn legend 

x =np.linspace(-3,3,50) # 50 points from -1 to 1
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num = 2, figsize = (8,5))  # setting figure = 3

plt.xlim((-1, 2))  
plt.ylim((-2, 3))
plt.xlabel(' i am x') 
plt.ylabel('i am y')

new_ticks = np.linspace(-1, 2,5)  # change tick in x / y axis
plt.xticks(new_ticks)
plt.yticks([-2,-1.5, -1,  1.22,  3],
        ['$really\ bad$', r'$bad\ \alpha$' ,r'$normal$',r'$good$' ,'$really\ good$']) 
       
l1, = plt.plot(x, y1, label = 'up')  # ifwaan use l1(line 1) in lengend "handles" function, must use a ',' 
l2, = plt.plot(x, y2, label= 'down', linestyle = '--') 
# plt.legend() # show the message of each line at top left # tu li
plt.legend(handles= [l1, l2] , labels= ['aaa', 'ccc'] , loc='best')




plt.show()

