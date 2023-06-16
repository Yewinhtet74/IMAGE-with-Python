# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:37:08 2023

@author: User
"""
import cv2
import skimage as sk
import matplotlib.pyplot as plt
import numpy as np 

def find_line(img1):
    line_s=0
    line_e=0
    sh=img1.shape
    for i in range(sh[0]):
        if not(line_s):
            found=np.where(img1[i]==0)[0]
            if found.size>0:
                line_s=i
        elif not(line_e):
            found=np.where(img1[i]==0)[0]
            if found.size==0:
                line_e=i
        else:break
    return [line_s,line_e]

def crop_vertical_space(img):
    line_s=0
    line_e=0
    sh=img.shape
    for i in range(sh[0]):
        if not(line_s):
            found=np.where(img[i]==0)[0]
            if found.size>0:
                line_s=i;break
    for i in range(sh[0]-1,-1,-1):
        if not(line_e):
            found=np.where(img[i]==0)[0]
            if found.size>0:
                line_e=i;break
    return img[line_s:line_e+1,:]



def pain(lin,x,y):
    #print(x,y)
    global ccc
    if ccc<y: 
        ccc=y
    lin[x,y]=2
    if y<lin.shape[1]-1 and lin[x,y+1]==0: pain(lin,x,y+1)
    if x<lin.shape[0]-1 and lin[x+1,y]==0: pain(lin, x+1, y)
    if x>0 and lin[x-1,y]==0: pain(lin, x-1, y)
    if x<lin.shape[0]-1 and y<lin.shape[1]-1 and lin[x+1,y+1]==0: pain(lin,x+1,y+1)
    if x>0 and y<lin.shape[1]-1 and lin[x-1,y+1]==0: pain(lin,x-1,y+1)

#plt.imshow(img)
#plt.hist(img.flat, bins=100, range=(0,255)) 


img= cv2.imread('images/text5.png',0)

ret2, thresh2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#plt.imshow(thresh2,cmap="gray")

img1=np.digitize(thresh2, bins=np.array([ret2]))
#plt.imshow(img1,cmap='gray')


[line_s,line_e]=find_line(img1)

line=img1[line_s:line_e+1,:]
plt.imshow(line)
'''
for i in range(line.shape[0]):
    print(i,np.where(line[i]==0)[0])
z=line[:,1900:]
'''
'''
word_s=0
word_e=0
words=[]
for i in range(line.shape[1]):
    if not(word_s):
        found=np.where(line[:,i]==0)[0]
        if found.size>0:
            word_s=i
    elif not(word_e):
        found=np.where(line[:,i]==0)[0]
        if found.size==0:
            word_e=i
            words.append(crop_vertical_space(line[:,word_s:word_e]))
            word_s=word_e=0
'''
word_s=0
word_e=0
words=[]
ccc=0
for i in range(line.shape[1]):
    if i<=ccc:   continue
    if not(word_s):
        found=np.where(line[:,i]==0)[0]
        if found.size>0:
            word_s=i
    elif not(word_e):
        for i in range(line.shape[0]):
            if line[i,word_s]==0:
                linecop=line.copy()
                ccc=word_s
                pain(linecop,i,word_s)
                word_e=ccc
                
                #words.append(line[:,word_s:word_e+1])
                words.append(crop_vertical_space(line[:,word_s:word_e+1]))
                word_s=word_e=0

#cv2.imwrite('images/ttt2.png',line[:,word_s:])

fig=plt.figure(figsize=(10,len(words)*10))

for i in range(len(words)):
    ax1=fig.add_subplot(1,len(words),i+1)
    ax1.imshow(words[i])

plt.show()

'''
a=words[0]
rgb_img = cv2.cvtColor(a, cv2.BI)
resized = cv2.resize(rgb_img, (100,100))
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''