# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-05-28
#Version     : 1.0

import numpy as np
import cv2
from math import sin,cos,pi
import random

def circle(img, point, sz):
    for i in range(8*sz):
        x=(point[0]+sz*(sin(i*2*pi/(8*sz))),point[1]+sz*(cos(i*2*pi/(8*sz))))
        if x[0]<img.shape[0] and x[1]<img.shape[1]:
            img[int(x[0]),int(x[1])]=255
    return img

def circleb(img, point, sz):
    for i in range(8*sz):
        x=(point[0]+sz*(sin(i*2*pi/(8*sz))),point[1]+sz*(cos(i*2*pi/(8*sz))))
        if x[0]<img.shape[0] and x[1]<img.shape[1]:
            img[int(x[0]),int(x[1])]=0
    return img

def circlesum(img, point, sz):
    sum=0
    for i in range(8*sz):
        x=(point[0]+sz*(sin(i*2*pi/(8*sz))),point[1]+sz*(cos(i*2*pi/(8*sz))))
        if x[0]<img.shape[0] and x[1]<img.shape[1]:
            sum=sum+(img[int(x[0]),int(x[1])][0]**2+img[int(x[0]),int(x[1])][1]**2+img[int(x[0]),int(x[1])][2]**2)
    return (sum-sz*3*127**2)/sz

def where(img,points):
    sums=[]
    for point in points:
        sums.append(circlesum(img,point,3))
        #print(min(sums))
        #print(sums)
    val, idx = min((val, idx) for (idx, val) in enumerate(sums))
    return (idx)

img = cv2.imread('img.png')
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2),interpolation = cv2.INTER_AREA)
img2 = np.zeros((img.shape[0], img.shape[1]))
j=0
while(1):
    j=j+1
    points=[]
    for i in range(10): points.append((random.randint(0,img.shape[0]),random.randint(0,img.shape[1])))
    c=where(img,points)
    img=circleb(img,points[c],3)
    img2=circle(img2,points[c],3) 
    if not j%20: cv2.imshow('',img2); cv2.waitKey(1)
