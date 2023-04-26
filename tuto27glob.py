# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 22:26:39 2023

@author: MICRO
"""

import cv2
import glob

files=glob.glob('images/*.*')
print(files)


img=[]

for file in glob.glob('images/*.*'):
    a=cv2.imread(file)
    img.append(a)
    
import matplotlib.pyplot as plt
plt.imshow(img[0])

count=1
for file in glob.glob('images/*.*'):
    a=cv2.imread(file)
    c=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
    cv2.imwrite('images/converted/color_image'+str(count)+'.jpg',c)
    count+=1
    cv2.imshow('Color Image',c)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()