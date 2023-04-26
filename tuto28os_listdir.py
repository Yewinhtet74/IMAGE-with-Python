# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 20:52:41 2023

@author: MICRO
"""

import os

print(os.listdir('images/')) #the list of file name in the directory  

for img in os.listdir('images'):
    print(img)
    
    
#print(os.walk('.'))
for root,dirs,files in os.walk('.'): #dirs is list of folder name in these path
    print('ROOT: ',root) #folders and subfolders name
    path=root.split(os.sep) #split with / or \
    print(path)
    print(files) #all files in these directory
    
    
#beautiful files display
for root,dirs,files in os.walk('.'):
    path=root.split(os.sep)
    print((len(path)-1)*'---',os.path.basename(root))
    for f in files:
        print(len(path)*'---',f)
        
        
#Another way
for root,dirs,files in os.walk('.'):
    print('ROOT: ',root)
    for n in dirs:
        print(root,'AND',n)
        print(os.path.join(root,n))
    for n in files:
        print(os.path.join(root,n))