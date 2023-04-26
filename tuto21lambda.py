# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:27:39 2023

@author: MICRO
"""
#pip install matplotlib
a=lambda x:x**2
print(a(5))

b=lambda x,y: x+y
print(b(4,5))

def dist(u,a):
    return lambda t:u*t+a*t
dd=dist(5, 6) #lambda t:5*t+6*t
print(dd(2))
print(dist(2,3)(5))

time,distance=[],[]
for i in range(5,7):
    dis=dist(i, i+1)
    for t in range(0,22,2):
        time.append(t)
        distance.append(dis(t))

from matplotlib import pyplot as plt
plt.plot(time,distance)