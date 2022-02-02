# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-12
#Version     : 1.0

import cv2
import numpy as np

img = np.zeros((500,500,3),dtype=np.uint8)
T=np.array([[1, 0, 0],[0, 1, 0],[1/2, -(3**0.5)/2, 0]])
arr=[(np.matmul([0,100,0],T)),(np.matmul([100,100,0],T)),(np.matmul([100,100,100],T)),(np.matmul([0,100,100],T))]
brr=[(np.matmul([0,200,0],T)),(np.matmul([0,100,0],T)),(np.matmul([100,100,0],T)),(np.matmul([100,200,0],T))]
crr=[(np.matmul([100,100,0],T)),(np.matmul([100,100,100],T)),(np.matmul([100,200,100],T)),(np.matmul([100,200,0],T))]
arroz=np.array(arr)[:,:2].astype(np.int32)
arroz=arroz.reshape((-1,1,2))
brroz=np.array(brr)[:,:2].astype(np.int32)
brroz=brroz.reshape((-1,1,2))
crroz=np.array(crr)[:,:2].astype(np.int32)
crroz=crroz.reshape((-1,1,2))
print(brroz)
cv2.fillPoly(img,[arroz],(255,0,0))
cv2.fillPoly(img,[brroz],(0,255,0))
cv2.fillPoly(img,[crroz],(0,0,255))
cv2.imshow('',img)
cv2.waitKey()
cv2.destroyAllWindows()