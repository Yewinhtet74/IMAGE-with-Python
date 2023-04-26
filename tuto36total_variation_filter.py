# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:34:01 2023

@author: HP
"""


import cv2
from skimage import io,img_as_float
from skimage.restoration import denoise_tv_chambolle

img=img_as_float(io.imread('images/white_temple.png'))

from matplotlib import pyplot as plt
plt.hist(img.flat,bins=100,range=(0,1)) #bins=number of bin or group, range=the range of pixels you want to show

denoise_img=denoise_tv_chambolle(img,weight=0.1,    #the greater weight, the more denoising
                                 eps=0.0002,        #how smaller error do u want to
                                 n_iter_max=200,    #number of iterlation
                                 multichannel=True)

cv2.imshow('Original',img)
cv2.imshow('TV filter',denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()