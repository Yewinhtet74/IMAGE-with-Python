# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:01:38 2023

@author: HP
"""
#filtering preserve edges non local mean, bilateral and BM3D
import cv2
import numpy as np
from skimage import io,img_as_float
from skimage.restoration import denoise_nl_means,estimate_sigma

img=img_as_float(io.imread('images/white_temple.png',as_gray=False))

sigma_est=np.mean(estimate_sigma(img,multichannel=True))#estimate sigma values

denoise_img=denoise_nl_means(img,h=1.15 * sigma_est,    #Larger h allows more smothing disimilar patches
                             fast_mode=True,            #False = a special Gaussian weighting is applied
                             patch_size=5,              #5*5 patches is used
                             patch_distance=3,          #patch distances
                             multichannel=True)

from skimage import img_as_ubyte

#make it ready to save or plot (by converting to int)
img_8byte=img_as_ubyte(img)
denoise_img_8byte=img_as_ubyte(denoise_img)

original_img=cv2.cvtColor(img_8byte,cv2.COLOR_BGR2RGB)
final_img=cv2.cvtColor(denoise_img_8byte,cv2.COLOR_BGR2RGB)

cv2.imshow('Original',original_img)
cv2.imshow('NLM filter',final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()