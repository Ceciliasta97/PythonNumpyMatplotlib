import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, axes = plt.subplots(3, 2) # create a figure and a subplot. row = 3, column =

""" Iterate column's axes"""
def iterate_columns(cols, x):
   for col in cols:
      col.plot(x, color='red')

""" Iterate row's axes"""
for row in axes:
   x = np.random.normal(0, 1, 100).cumsum()
   iterate_columns(row, x)

plt.show()