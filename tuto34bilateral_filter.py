# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:09:38 2023

@author: Admin
"""
#bilateral filtering preserve edges
import cv2

img=cv2.imread('images/girl_noise.png',0)

bilateral_cv2=cv2.bilateralFilter(img,5,20,100,borderType=cv2.BORDER_CONSTANT)
# 5 for kernel
#20 for sigma color or weight
#100 for sigma space

cv2.imshow('original',img)
cv2.imshow('Bilateral Filtering',bilateral_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#bilateral filtering in skimage is slower than cv2
from skimage.restoration import denoise_bilateral
bilateral_sk=denoise_bilateral(img,sigma_color=0.05,sigma_spatial=15,multichannel=False)