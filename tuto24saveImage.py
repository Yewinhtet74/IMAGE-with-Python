# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:31:01 2023

@author: MICRO
"""

from skimage import io,filters,img_as_ubyte

img=io.imread('images/ballons.tif')
gaus_img=filters.gaussian(img,sigma=3)

gaus_img_8=img_as_ubyte(gaus_img)  #convert floating point to 0-255 scale
io.imsave('images/ballonstif.tif',gaus_img_8)

import cv2
cv2.imwrite('images/abcd.jpg',gaus_img) #covert directly to int may be{0,1,2}

#iimg=io.imread('images/abcd.jpg')


cv2.imwrite('images/ballonscv2imwrite.jpg',gaus_img_8) #save img as BGR

imgRGB= cv2.cvtColor(gaus_img_8,cv2.COLOR_BGR2RGB) #convertBRGtoRGB
cv2.imwrite('images/ballonscv2imwrite2.jpg',imgRGB)


import matplotlib.pyplot as plt

plt.imsave('images/ballonspyplot.jpg',gaus_img)


import tifffile as tf
tf.imwrite('images/ballonstifffile.tif',gaus_img_8)