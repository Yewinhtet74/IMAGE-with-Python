# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:34:25 2023

@author: MICRO
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

x=np.arange(256)
y=np.sin(2*np.pi*x/50)

y+=max(y)

y_img=np.array([[y[j]*127 for j in range(256)] for i in range(256)],dtype=np.uint8)

plt.imshow(y_img)

img=cv2.imread('images/onion.png',0)

dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)

dft=np.fft.fftshift(dft) #shift to center

magnitude_spectrum = 20*np.log((cv2.magnitude(dft[:,:,0],dft[:,:,1]))+1) #to rise negative value


fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('Input image')

ax2=fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum)
ax2.title.set_text('FFT image')
