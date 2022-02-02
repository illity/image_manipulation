# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-04-08
#Version     : 1.0

import cv2, numpy as np

name=cv2.imread('alphabet.png')
#hye=name[:,0:10,0]
#nyon=name[:,11:21,0]
#kim=name[:,22:32,0]
#open('hy.txt','w').write(str(np.ndarray.tolist(hye)))
#open('ny.txt','w').write(str(np.ndarray.tolist(nyon)))
#open('ki.txt','w').write(str(np.ndarray.tolist(kim)))
for i in range(26):
    print(chr(i+97))
    open('alphabet.txt','a').write(chr(i+97)+'='+str(np.ndarray.tolist(name[:,11*i:10+11*i,0]))+'\n')