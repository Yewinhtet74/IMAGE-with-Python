# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:43:45 2023

@author: HP
"""

'''
Canny Edge dection

step1:
step2: 
step3:
step4:
step5:
'''
import cv2
import numpy as np


img=cv2.imread('images/white_temple.png',0)

canny_edge=cv2.Canny(img,103,148)

#Custom Canny
sigma=0.3
median=np.median(img)

lower=int(max(0, (1.0-sigma)*median)) #30% smaller than median value
upper =int(min(255,(1.0+sigma)*median))#30% greater than median value

custom_canny=cv2.Canny(img,lower,upper)

cv2.imshow('Canny',canny_edge)
cv2.imshow('Custom canny',custom_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()