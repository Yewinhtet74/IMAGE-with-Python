# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:32:48 2023

@author: User
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/bay2.jpg", 0)

ret2, thresh2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(thresh2, cmap='gray')
cv2.imshow('',thresh2)

cv2.waitKey(0) #shutdown after 3 seconds, 0 for no shutdown
cv2.destroyAllWindows()