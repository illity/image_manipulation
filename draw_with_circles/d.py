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

def circlesum(img, point, sz):
    sum=0
    for i in range(8*sz):
        x=(point[0]+sz*(sin(i*2*pi/(8*sz))),point[1]+sz*(cos(i*2*pi/(8*sz))))
        if x[0]<img.shape[0] and x[1]<img.shape[1]:
            sum=sum+(img[int(x[0]),int(x[1])][0]**2+img[int(x[0]),int(x[1])][1]**2+img[int(x[0]),int(x[1])][2]**2)
    return (sum-sz*3*127**2)/sz

def where(img,point):
    sums=[]
    for sz in range(1,25):
        sums.append(circlesum(img,point,sz))
        #print(min(sums))
        #print(sums)
    val, idx = min((val, idx) for (idx, val) in enumerate(sums))
    return (idx)

img = cv2.imread('c.png')
img = cv2.resize(img, (img.shape[1]//4, img.shape[0]//4),interpolation = cv2.INTER_AREA)
img2 = np.zeros((img.shape[0], img.shape[1]))
i=0
while(1):
    i=i+1
    point=(random.randint(0,img.shape[0]),random.randint(0,img.shape[1]))
    c=where(img,point)
    img=circle(img,point,c)
    img2=circle(img2,point,c)
    if not i%100:
        cv2.imshow('',img2)
        cv2.waitKey(10)
