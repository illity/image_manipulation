# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-04-02
#Version     : 1.0

import cv2, numpy as np,time
sz=400
iter=100
def product(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sum(a,b):
    return (a[0]+b[0],a[1]+b[1])
def mandelbrot(c):
    z=(0,0)
    for i in range(iter):
        if (z[0]*z[0]+z[1]*z[1])<4: z=sum(product(z,z),c)
        else: return i
    return iter

start=time.time()
img=np.ones((sz,sz),dtype=np.uint8)
img=img*255
p=(-0.01,0.70997)
interval=(-0.00005,0.00005)#x,y
for i in range(0,sz):
    for j in range(0,sz):
        img[sz-j-1][i]=255-255*mandelbrot((p[0]+i*(interval[1]-interval[0])/sz+interval[0],p[1]+j*(interval[1]-interval[0])/sz+interval[0]))/(iter)
        if img[sz-j-1][i]>255: img[sz-j-1][i]=255
        if img[sz-j-1][i]<0: img[sz-j-1][i]=0
#cv2.imshow('janelinha :)',img)
#cv2.waitKey()
img=(255/(np.amax(img)-np.amin(img)))*img
cv2.imwrite(str(p)+'_'+str(interval)+'_'+str(iter)+'.png',img)
print(time.time()-start)