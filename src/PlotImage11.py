import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(-3,3,50) # 50 points from -1 to 1
y1 = 2 * x + 1
y2 = x ** 2


plt.figure(num = 2, figsize = (8,5))  # setting figure = 3
plt.plot(x, y2)  #figure 3
plt.plot(x, y1, color = "red", linewidth = 2.0, linestyle = "--")  # draw second line in the same figure

plt.xlim((-1, 2))  # the range of x
plt.ylim((-2, 3))# range of y
plt.xlabel(' i am x') # dexcription of x
plt.ylabel('i am y')

new_ticks = np.linspace(-1, 2,5)  # change tick in x / y axis
print (new_ticks)
plt.xticks(new_ticks)

# plt.yticks([-2,-1.8, -1, 1.22,  3],
#             ['really bad', 'bad' ,'normal','good' ,'really good'])

# make the yticks have a prettier font:
plt.yticks([-2,-1.5, -1,  1.22,  3],
        ['$really\ bad$', r'$bad\ \alpha$' ,r'$normal$',r'$good$' ,'$really\ good$']) # use Regular Expression
        # use \alpha to represent mathematical alpha

plt.show()

