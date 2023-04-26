# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:50:25 2023

@author: MICRO
"""
#pip install opencv-python
from skimage import io,img_as_float,img_as_ubyte

img=io.imread('images/idface.jpg')
print('shape',img.shape)

img2=img_as_float(img) #convert to float scale from 0 to 1

import numpy as np
img3=img.astype(np.float) #covert float as original values

img_8bit=img_as_ubyte(img2) #covert from float-scale to 8bit


import cv2

img_grey=cv2.imread('images/idface.jpg',0) #0 mean to read image as grey
img_cv2=cv2.imread('images/idface.jpg') #cv2 read as BGR array, this is the difference
#img_cv2=cv2.imread('images/idface.jpg',1)

img_opencv=cv2.cvtColor(img_cv2,cv2.COLOR_BGR2RGB) #convert BGR to RGB