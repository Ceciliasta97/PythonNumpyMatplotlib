# PythonNumpyMatplotlib
learn numpy and matplotlib

## Run the code: 
    pip install matplotlib
    python PlotImage1.py

## resources: 
    https://www.tutorialspoint.com/matplotlib-plot-over-an-image-background-in-python
    https://www.tutorialspoint.com/plot-a-vector-field-over-the-axes-in-python-matplotlib
    https://www.tutorialspoint.com/how-to-plot-a-3d-continuous-line-in-matplotlib
    https://www.tutorialspoint.com/plot-3d-bars-without-axes-in-matplotlib
    https://www.bilibili.com/video/BV1Jx411L7LU/?spm_id_from=333.337.search-card.all.click
    
# difference between subplot() and subplots()
    subplot(): create a single subplot
    subplots(): create multiple subplots at once 
    e.g.:
        plt.subplot(1, 2, 1)  # Create a subplot with 1 row, 2 columns, and index 1
        fig, axes = plt.subplots(2, 2)  # Create a 2x2 grid of subplots

# what I have learn
    NumPy:
    np.array(): Creates a NumPy array.
    np.arange(): Returns evenly spaced values within a given interval.
    np.zeros(), np.ones(): Creates arrays filled with zeros or ones.
    np.random.rand(), np.random.randn(): Generates random numbers from uniform or normal distributions.
    np.sum(), np.mean(), np.median(): Computes the sum, mean, and median of array elements.
    np.min(), np.max(): Finds the minimum and maximum values in an array.
    np.sin(), np.cos(), np.sqrt(), np.log(), np.sum()

    Matplotlib:
    plt.plot(): Plots lines and/or markers.
    plt.scatter(): Plots a scatter plot.
    plt.bar(), plt.barh(): Plots vertical or horizontal bar plots.
    plt.imshow(): Displays an image.
    plt.contour(), plt.contourf(): Plots contour lines or filled contours.
    plt.xlabel(), plt.ylabel(): Sets the labels for the x and y-axes.
    plt.title(): Sets the title of the plot.
    plt.legend(): Adds a legend to the plot.
    plt.grid(): Adds a grid to the plot.
    plt.xlim(), plt.ylim(): Sets the limits of the x and y-axes.
    plt.show(): Displays the plot.
