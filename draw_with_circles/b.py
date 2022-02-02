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
    for i in range(8*sz):
        x=(point[0]+sz*(sin(i*2*pi/(8*sz))),point[1]+sz*(cos(i*2*pi/(8*sz))))
        img[int(x[0]),int(x[1])]=255
    return img

img = cv2.imread('a.jpg')
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2),interpolation = cv2.INTER_AREA)
while(1):
    point=(random.randint(0,img.shape[0]),random.randint(0,img.shape[1]))
    img=circle(img,point,5)
    cv2.imshow('',img)
    cv2.waitKey(10)
