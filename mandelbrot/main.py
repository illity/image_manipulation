# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-10-09
#Version     : 1.0

import cv2, numpy as np,time
sz=100
iter=500
def product(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sum(a,b):
    return (a[0]+b[0],a[1]+b[1])
def mandelbrot(c):
    z=0
    for i in range(iter):
        if (abs(z))<4: z=z*z+c
        else: return i
    return iter

p=0
interval=2
print('commands: wasd xz')
while(1):
    original=np.zeros((sz,sz),dtype=complex)
    for i in range(0,sz):
        for j in range(0,sz):
            original[sz-j-1][i]=p-interval-interval*1j+2*interval*i/(sz-1)+2*interval*j*1j/(sz-1)
    img=np.array(np.array(original))
    for i in range(iter):
        img=np.square(img)+original
    img=abs(img)
#  print((img>4)[50,50])
    img=np.array((np.isnan(img)+(img>4))*255,dtype=np.uint8)
    cv2.imshow('mandel',img)
    k=cv2.waitKey()
    if (k==ord('d')):
        p=p+interval*0.1
    if (k==ord('a')):
        p=p-interval*0.1
    if (k==ord('w')):
        p=p+1j*interval*0.1
    if (k==ord('s')):
        p=p-1j*interval*0.1
    if (k==ord('z')):
        interval*=0.9
    if (k==ord('x')):
        interval*=1.1