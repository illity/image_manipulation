# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-12-11
#Version     : 1.0

import cv2
import numpy as np

def closest(x):
    if x>127: return 255
    return 0


img = cv2.imread('a.jpg')
print(dir(cv2))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
floyd = np.copy(img)
#cv2.imshow('',img); cv2.waitKey()
print(img.shape)
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
            old = floyd[i][j]
            new = closest(floyd[i][j])
            floyd[i][j] = new
            err = old-new
            floyd[i][j+1] += err * (7/16)
            floyd[i+1][j] += err * (5/16)
            floyd[i+1][j-1] += err * (3/16)
            floyd[i+1][j+1] += err * (1/16)
    cv2.imshow('h_v',floyd); cv2.waitKey(1)
cv2.imwrite('a_h.png',floyd)