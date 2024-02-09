from matplotlib import pyplot as plt

# Create a figure object
fig = plt.figure()

# Add a subplot to the figure
ax = fig.add_subplot(111)

# Create the bar plot
bars = ax.bar(['A', 'B', 'C'], [4, 8, 5])

# Loop through the bars and add annotations
for bar in bars:
   height = bar.get_height()
   ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 2),
               # annotate: add textannoatation, thetext is the heiht of the bar
               # xy: specified the position of anotation (xy : center  of the top of bar)
               # xy text : 2 points above the bar here
   textcoords="offset points", ha='center', va='bottom') # text offset coordinates
                                                        # ha, va : horizontal and vertical alignment of the text

plt.title('Bar Plot (With Annotations)')
plt.show()