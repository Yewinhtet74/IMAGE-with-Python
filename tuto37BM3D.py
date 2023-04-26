# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:04:17 2023

@author: HP
"""

#Block matching & 3D filtering

import cv2
import bm3d
from skimage import io,img_as_float

img=img_as_float(io.imread('images/white_temple.png', as_gray=True))

denoise_img=bm3d.bm3d(img, sigma_psd=0.1,   #noise standard deviation
                      stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING) #but it slow
#stage_arg=determine to perform post-processing hard-thresholding or Wiener filtering
#BM3DSatges.HARd_THRESHOLDING or BM3DStagse.ALL_STAGES (slow but powerful)


cv2.imshow('Original',img)
cv2.imshow('BM3D Filter',denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()