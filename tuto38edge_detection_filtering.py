# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:26:27 2023

@author: HP
"""
import cv2

img=cv2.imread('images/white_temple.png',0)

from skimage.filters import roberts,sobel,scharr,prewitt,farid

#fast speed with no daley
robert_img=roberts(img)
sobel_img=sobel(img)
scharr_img=scharr(img)
prewitt_img=prewitt(img)
farid_img=farid(img)

cv2.imshow('Original',img)
cv2.imshow('Robert',robert_img) #robert is so detail and sobel is better
cv2.imshow('Sobel',sobel_img)   #sobel and scharr is similar
cv2.imshow('Scharr',scharr_img)
cv2.imshow('Prewitt',prewitt_img)
cv2.imshow('Farid',farid_img)
cv2.waitKey(0)
cv2.destroyAllWindows()