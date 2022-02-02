# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-10-28
#Version     : 1.0

import cv2
import numpy as np
sz = 235
img = cv2.imread('src.png')
colors=[]
for i in range(235):
    test = img[:20,8*i:8*(i+1)]
    colors.append(np.mean(test))
    #cv2.imshow('test',test); cv2.waitKey()
tgt = cv2.imread('yubel.jpeg')
tgt = cv2.resize(tgt, (sz,sz))
src = open('src.txt','r',encoding='utf-8').read()
print(src)
txt=''
for i in range(sz):
    print(i)
    for j in range(sz):
        char=0
        d=255
        for k in range(235):
            if abs(np.mean(tgt[i,j,:])-colors[k])<d:
                d=abs(np.mean(tgt[i,j,:])-colors[k])
                char=k
        txt+=src[char]
    txt+='\n'
open('out.txt','w',encoding='utf-8').write(txt)
cv2.imshow('',tgt);cv2.waitKey()
