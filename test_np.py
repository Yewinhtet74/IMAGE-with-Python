# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:54:13 2023

@author: User
"""
import numpy as np
import random as rd
import cv2
d=cv2.imread('images/ttt2.png',0)
d=d[:,76:]
#+15+18+15+21+13+12+46
'''
d=[]
for i in range(50):
    d.append(rd.choice([0,rd.randrange(0,2)]))
d=np.asarray(d)
d=d.reshape(5, 10)
print(d)
'''
def pain(lin,x,y):
    #print(x,y)
    global ccc
    if ccc<y: 
        ccc=y
        print(x,y,ccc)
    lin[x,y]=2
    if y<lin.shape[1]-1 and lin[x,y+1]==0: pain(lin,x,y+1)
    if x<lin.shape[0]-1 and lin[x+1,y]==0: pain(lin, x+1, y)
    if x>0 and lin[x-1,y]==0: pain(lin, x-1, y)
    if x<lin.shape[0]-1 and y<lin.shape[1]-1 and lin[x+1,y+1]==0: pain(lin,x+1,y+1)
    if x>0 and y<lin.shape[1]-1 and lin[x-1,y+1]==0: pain(lin,x-1,y+1)

for i in range(20):
    if d[i,0]==0:
        ccc=0
        pain(d,i,0)
        break
print(ccc)
