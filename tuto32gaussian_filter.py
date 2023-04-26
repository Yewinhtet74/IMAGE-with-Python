# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:23:06 2023

@author: MICRO
"""

import cv2
from skimage import io,img_as_float
from skimage.filters import gaussian

img=img_as_float(io.imread('images/apple_noise.png',as_gray=True))
img=img_as_float(io.imread('images/apple_pepper.png',as_gray=True))

gaus_cv2=cv2.GaussianBlur(img,(3,3),0,borderType=cv2.BORDER_CONSTANT)
gaus_sk=gaussian(img,sigma=1,mode='constant',cval=0.0)

cv2.imshow('Original img',img)
cv2.imshow('Gaussian with cv2',gaus_cv2)
cv2.imshow('Gaussian with scikit image',gaus_sk)

cv2.waitKey(0)
cv2.destroyAllWindows()