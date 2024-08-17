
# Practica 1

import cv2
import numpy as np
import matplotlib.pyplot as plt

# imagen negra

img = np.zeros((10,10,1), np.uint8)

img[0,1] = 30
img[1,2] = 50
img[3,4] = 200
img[6,9] = 140

# Mostramos los valores numericos 
# print(img)

# Mostramos nuestra imagen

plt.imshow(img, cmap='gray')
plt.show()

