# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 05:36:53 2023

@author: MICRO
"""

from PIL import Image

img=Image.open('images/idface.jpg')
#print(img)
#img.show()
print(img.format)

import numpy as np
img1=np.asarray(img)
print(type(img1))


import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img2=mpimg.imread('images/idface.jpg')
print(type(img2))
print(img2.shape)
plt.imshow(img2)