# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 20:56:10 2023

@author: MICRO
"""

#pip install tifffile

from skimage import io

img=io.imread('images/ballons.tif', as_gray=True)

import cv2

greyImg=cv2.imread('images/ballons.tif',0)
colorImg=cv2.imread('images/ballons.tif',1)

import tifffile as tf
import numpy as np
img2=tf.imread('images/ballons.tif')
print(np.shape(img2))

#pip instal czifile 


from matplotlib import pyplot as pt

fig=pt.figure(figsize=(10,10))
ax1=fig.add_subplot(2,2,1)
ax1.imshow(img2[:,:,0],cmap='hot')
ax1.title.set_text('Red channel')
ax2=fig.add_subplot(2,2,2)
ax2.imshow(img2[:,:,1])
ax2.title.set_text('Green channel')
ax3=fig.add_subplot(2,2,3)
ax3.imshow(img2[:,:,2])
ax3.title.set_text('Blue channel')
pt.show()