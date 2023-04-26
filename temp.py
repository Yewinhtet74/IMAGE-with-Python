# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from skimage import io
img=io.imread('images/idface.jpg')
print(type(img))
io.imshow(img)