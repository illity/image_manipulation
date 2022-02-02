# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-12-11
#Version     : 1.0

import cv2
import numpy as np

def closest(x):
    if x>127: return 255
    return 0


img = cv2.imread('t.jpeg')
floyd = np.copy(img)
#cv2.imshow('',img); cv2.waitKey()
print(img.shape)
for i in range(1,img.shape[0]-1):
    print(i)
    for j in range(1,img.shape[1]-1):
        for k in range(3):
            old = floyd[i][j][k]
            new = closest(floyd[i][j][k])
            floyd[i][j][k] = new
            err = old-new
            floyd[i][j+1][k] += err * (7/16)
            floyd[i+1][j][k] += err * (5/16)
            floyd[i+1][j-1][k] += err * (3/16)
            floyd[i+1][j+1][k] += err * (1/16)
    cv2.imshow('',floyd); cv2.waitKey(1)
#cv2.imwrite('h.png',floyd)