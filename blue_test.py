# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:14:05 2023

@author: User
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/colors.jpg", 1)

#########################MANUAL##################
#Separate blue channels as they contain nuclei pixels (DAPI). 
blue_channel = img[:,:,0]
plt.imshow(blue_channel, cmap='gray')

plt.hist(blue_channel.flat, bins=100, range=(0,255))  #.flat returns the flattened numpy array (1D)

ret2, thresh2 = cv2.threshold(blue_channel,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(thresh2,cmap="gray")


img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue=img[:,:,0]
plt.imshow(hue,cmap='gray')
plt.hist(hue.flat, bins=100, range=(0,255))



blue=(hue>100)
plt.imshow(blue, cmap='gray')

ret2, thresh2 = cv2.threshold(hue,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(thresh2,cmap="gray")


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
 # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
 # Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
plt.imshow(res, cmap='gray')
cv2.imshow('res',res)
cv2.destroyAllWindows()