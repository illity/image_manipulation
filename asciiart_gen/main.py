# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-10-31
#Version     : 1.0

import cv2
import numpy as np

def asciiart_gen(tgt):
    sz = 20
    nc = 6
    colors = [255-255*i/nc for i in range(1,nc+1)]
    tgt = cv2.cvtColor(tgt, cv2.COLOR_RGB2GRAY)
    tgt = tgt - np.amin(tgt)
    tgt = 255 - tgt
    tgt = cv2.resize(tgt, (sz,tgt.shape[0]*sz//tgt.shape[1]), interpolation = cv2.INTER_AREA)
    #src = ['...',',,,,,','---','~ ','::::',';;;;','= ','!!!!','**','# ','$ ','@']
    src = [', , ',',.,.','+-','%\'','#!','@','@']
    #src = [2*i for i in ['.',',','-','~',':',';','=','!','*','#','$','@']]
    txt=''
    for i in range(tgt.shape[0]):
        for j in range(tgt.shape[1]):
            char=0
            char = int(tgt[i,j]//(255/(nc)))
            for c in src[char]:
                txt+=c
        txt+='\n'
    print(txt)
    return txt

a = open('out.txt','r',encoding='utf-8').read()
b = ''
for ch in a:
    if ch!='\n':
        b=b+ch+ch
    else:
        b=b+ch
a = open('out2.txt','w',encoding='utf-8').write(b)
print(b)