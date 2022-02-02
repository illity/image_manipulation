# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-05-28
#Version     : 1.0

import numpy as np
import cv2
from math import sin,cos,pi

def circle(img, point, sz):
    for i in range(8*sz):
        x=(point[0]+sz*(sin(i*2*pi/(8*sz))),point[1]+sz*(cos(i*2*pi/(8*sz))))
        img[int(x[0]),int(x[1])]=255
    return img

img = np.zeros((100,100)) 
img = circle(img,(35,35),25)
img = circle(img,(38,38),22)
cv2.imshow('',img)
cv2.waitKey()
