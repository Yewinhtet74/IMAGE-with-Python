# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:48:29 2023

@author: MICRO
"""
#!pip install --upgrade scikit-image
#unsharpeened=original + amount*(original-blurred)

from skimage import io,img_as_float
from skimage.filters import unsharp_mask,gaussian

img=img_as_float(io.imread('images/onion.png',as_gray=True))

gaus_img=gaussian(img,sigma=2,mode='constant',cval=0.0)
img2=(img-gaus_img)*2
img3=img+img2

import matplotlib.pyplot as plt
plt.imshow(img3,cmap='gray')

#work with ready made function
from skimage.filters import unsharp_mask

unsharp=unsharp_mask(img,radius=3,amount=2) # radius=the amount of blur

fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(1,2,1)
ax1.imshow(img,cmap='gray')
ax1.title.set_text('Original Image')
ax2=fig.add_subplot(1,2,2)
ax2.imshow(unsharp,cmap='gray')
ax2.title.set_text('Unsharpened Image')
plt.show()