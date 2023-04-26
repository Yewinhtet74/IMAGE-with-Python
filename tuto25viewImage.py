# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from skimage import io

img=io.imread('images/fruits.jpeg')
io.imshow(img)

import matplotlib.pyplot as plt
plt.imshow(img) #can decided image size when display

imgGrey=io.imread('images/edin_castle.png',as_gray=True)
plt.imshow(imgGrey,cmap='hot')
plt.imshow(imgGrey,cmap='Greys')
plt.imshow(imgGrey,cmap='Greens')
plt.imshow(imgGrey,cmap='jet')


fig=plt.figure(figsize=(10,10)) #x,y the size of plot

ax1=fig.add_subplot(2,2,1)
ax1.imshow(imgGrey,cmap='Greys')
ax1.title.set_text('Geys image')
ax2=fig.add_subplot(2,2,2)
ax2.imshow(imgGrey,cmap='hot')
ax2.title.set_text('Hot image')
ax3=fig.add_subplot(2,2,3)
ax3.imshow(imgGrey,cmap='Greens')
ax3.title.set_text('Greens image')
ax4=fig.add_subplot(2,2,4)
ax4.imshow(imgGrey,cmap='bone')
ax4.title.set_text('Bone image')

plt.show()

import cv2

greyImg=cv2.imread('images/onion.png',0)
colorImg=cv2.imread('images/onion.png',1)

cv2.imshow('pic from skimage',img) #weird colors where R and B channels are swaped
cv2.imshow('after swapped pic from skimage',cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
cv2.imshow('greyimage',greyImg)
cv2.imshow('color image',colorImg)

cv2.waitKey(3000) #shutdown after 3 seconds, 0 for no shutdown
cv2.destroyAllWindows()