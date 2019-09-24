import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img = np.zeros(shape=(8, 8))

img[2:4, 1:3] = 1
img[2:4, 5:7] = 1
img[4:5, 3:5] = 1
img[5:7, 2:6] = 1
img[([7, 7], [2, 5])] = 1

plt.imshow(img, cmap='gray')

plt.show()