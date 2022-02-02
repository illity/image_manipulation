# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-10-21
#Version     : 1.0

import cv2, numpy as np,time
sz=400
iter=100
def product(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sum(a,b):
    return (a[0]+b[0],a[1]+b[1])
def mandelbrot(c):
    z=0
    for i in range(iter):
        if (abs(z))<4: z=z*z*z+c
        else: return i
    return iter

start=time.time()
p=0
interval=1
img=np.ones((sz,sz),dtype=np.uint8)
img=255*img
for i in range(0,sz):
    for j in range(0,sz):
        img[sz-j-1][i]=(255-255/iter*mandelbrot(p-interval-interval*1j+2*interval*i/sz+2*interval*j*1j/sz))
        #if img[sz-j-1][i]>255: img[sz-j-1][i]=255
        #if img[sz-j-1][i]<0: img[sz-j-1][i]=0
cv2.imshow('mandel',img)
k=cv2.waitKey()