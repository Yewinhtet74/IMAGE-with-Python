# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:14:03 2023

@author: MICRO
"""
#pip install numpy
#pip install scikit-image
import numpy as np
a=[0,1,2,3,4,5]
b=np.array(a)
print(b*2)
print(b**2)

c=np.array([5,4,3,2,1,0])
print(b+c)

x=np.array([[1,2],[3,4]],dtype=np.float64)

from skimage import io
img=io.imread('images/idface.jpg')
print(type(img))

aa=np.ones((3,4))
bb=np.zeros((3,3))
cc=np.ones_like(img)

cd=np.random.random((3,3))

n=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]])
print('shape',np.shape(n),n[:2],sep='\n')
print('selete',n[:2,1:3])

print('axis',np.sum(n,axis=0),np.sum(n,axis=1))
print('max',np.max(n))
print('flit\n',n.T)