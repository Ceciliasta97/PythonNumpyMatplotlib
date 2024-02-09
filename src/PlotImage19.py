import numpy as np
import matplotlib.pyplot as plt

# learn Image


# every value is a pixel
# image data
a = np.array ([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.4395599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower') #cmap: color map# interpolation: nearest / bicubic / hamming / hermite.... (can search online)
                                            # interpolation: nearest / bicubic / hamming / hermite.... (can search online)
                                            # origin = 'upeer' / lower
plt.colorbar(shrink=0.9) # shrink : change the height of the bar

plt.xticks(())
plt.yticks(())
plt.show()
