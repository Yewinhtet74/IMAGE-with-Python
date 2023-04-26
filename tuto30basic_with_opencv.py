# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:12:08 2023

@author: MICRO
"""

import cv2
from matplotlib import pyplot as plt

img=cv2.imread('images/colors.jpg',1) #read color image as BGR
#plt.imshow(img)

img2=cv2.resize(img,None,fx=1/2,fy=1/2,interpolation=cv2.INTER_CUBIC)#fx,fy is size of x,y axis

cv2.imshow('original pic',img)
cv2.imshow('resized pic',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#split channel
blue=img2[:,:,0]
green=img2[:,:,1]
red=img2[:,:,2]


cv2.imshow('resized pic',img2)
cv2.imshow('blue pic',blue)
cv2.imshow('green pic',green)
cv2.imshow('red pic',red)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Another way
b,g,r=cv2.split(img2)

cv2.imshow('blue pic',b)
cv2.imshow('green pic',g)
cv2.imshow('red pic',r)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Canny
img2=cv2.imread('images/onion.png',1)
edge=cv2.Canny(img2,100,200)#min threatshold,max threadshold
cv2.imshow('Original img',img2)
cv2.imshow('Canny',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()