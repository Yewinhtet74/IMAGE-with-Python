# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:35:22 2023

@author: HP
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 6, 9, 11]
plt.plot(x, y)

# doing with numpy array but it's working the same
a = np.array(x)
b = np.array(y)
plt.plot(a, b)


greyImg = cv2.imread('images/fruits.jpeg', 0)

# plt.imshow(greyImg,cmap='gray')
# plt.hist(greyImg.flat,bins=155,range=(0,255))#bins is the number of line

plt.plot(a, b)
plt.plot(a, b, 'bo')  # blue dots
plt.plot(a, b, 'r--')  # red desh
plt.plot(a, b, 'g^')  # green triangle
plt.axis([0, 6, 0, 50])  # range for x and y axis

wells = ['well1', 'well2', 'well3', 'well4', 'well5']
cells = [90, 43, 66, 49, 50]

plt.bar(wells, cells)  # bar plot
plt.scatter(wells, cells)  # dots plot
plt.plot(wells, cells)  # line plot

plt.plot(a, b, linewidth=5.0)

fig = plt.plot(a, b)
plt.setp(fig, color='r', linewidth=4.0)
plt.show()

# set plot with full label
plt.figure(figsize=(8, 8))

plt.bar(wells, cells)
plt.xlabel('Well #', fontsize=18, color='red')
plt.ylabel('#dead cells')
plt.title('Dead cells in each well')
plt.axis([1, 6, 20, 120])
plt.grid(True)
plt.show()

# subploting
plt.figure(figsize=(12, 6))  # x,y

plt.subplot(121)  # row,colum,position
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

plt.subplot(122)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# ploting horizontally
plt.figure(figsize=(16, 6))

plt.subplot(131)
plt.bar(wells, cells)

plt.subplot(132)
plt.scatter(wells, cells)

plt.subplot(133)
plt.plot(wells, cells)
plt.suptitle('Mutiple Plots')
plt.show()

# Initialize the plot and subplots
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(221)
ax1.set(title='vertical bar', xlabel='Well#', ylabel='Cell')
ax2 = fig.add_subplot(222)
ax2.set(title='horizontal bar', xlabel='Well#', ylabel='Cell')
ax3 = fig.add_subplot(223)


ax1.bar(wells, cells)
ax2.barh(wells, cells)
ax3.plot(wells, cells)

plt.savefig('images/myplot.jpg')
plt.show()
