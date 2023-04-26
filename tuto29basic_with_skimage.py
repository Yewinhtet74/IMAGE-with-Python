# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:20:46 2023

@author: MICRO
"""

import matplotlib.pyplot as plt
from skimage import io,color
from skimage.transform import rescale,resize,downscale_local_mean

img=io.imread('images/fruits.jpeg', as_gray=True)

 #scale,for smooth boundries asign True
imgRescale=rescale(img,1.0/4.0,anti_aliasing=False)

#size of pixels,as about
imgResize=resize(img,(200,200),anti_aliasing=True)

imgDown=downscale_local_mean(img,(4,3))

plt.imshow(imgDown,cmap='gray')


from skimage.filters import gaussian,sobel

gaussianImg=gaussian(img,sigma=1,mode='constant',cval=0.0) #constant=0.0
plt.imshow(gaussianImg)

#edge detection
sobelImg=sobel(img)
plt.imshow(sobelImg,cmap='gray')