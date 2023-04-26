# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:44:44 2023

@author: MICRO
"""

import cv2
from skimage.filters import median
from skimage.morphology import disk

img=cv2.imread('images/apple_noise.png',0)
img=cv2.imread('images/apple_pepper.png',0)

median_cv2=cv2.medianBlur(img,3) #3 is kernel

#example
a=disk(3) #3 for 3*2+1=7 kernel, 1 for 3 kernel

median_sk=median(img,disk(1),mode='constant',cval=0.0) #when we add boundary the value is 0.0

cv2.imshow('Original img',img)
cv2.imshow('Gaussian with cv2',median_cv2)
cv2.imshow('Gaussian with scikit image',median_sk)

cv2.waitKey(0)
cv2.destroyAllWindows()