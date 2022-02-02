# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-04-02
#Version     : 1.0

import cv2, numpy as np
sz=200
iter=255

def product(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sum(a,b):
    return (a[0]+b[0],a[1]+b[1])
def mandelbrot(c):
    z=(0,0)
    for i in range(iter):
        if (z[0]*z[0]+z[1]*z[1])<10000: z=sum(product(z,z),c)
        else: return i
    return 255

img=np.ones((sz,sz),dtype=np.uint8)
img=img*255
for i in range(-sz//2,sz//2):
    for j in range(-sz//2,sz//2):
        img[sz//2-j-1][sz//2+i]=255-255*mandelbrot((4*i/sz,4*j/sz))//(iter+1)
cv2.imshow('janelinha :)',img)
cv2.waitKey()