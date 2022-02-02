# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-10-28
#Version     : 1.0

import cv2
import numpy as np
a=cv2.imread('img.png')
b=cv2.imread('img.png')
b_channel, g_channel, r_channel = cv2.split(a)
img_BGRA = cv2.merge((b_channel, g_channel, r_channel, np.ones(b_channel.shape, dtype=b_channel.dtype) * 50))
r=5
c=287+358*1j
    	
for i in range(100):
    a=a[int(c.real)-287:int(c.real)+287,int(c.imag)-287:int(c.imag)+287]
    a=cv2.resize(a,(720,720),interpolation=cv2.INTER_AREA)
    r=r*1.2
    r=int(r)
    c-=int(c.real)-287 + 1j*(int(c.imag)-287)
    c=c*720/287/2
    print(c)
    img=cv2.resize(b,(2*r,2*r),interpolation=cv2.INTER_AREA)
    #cv2.imshow('',img); cv2.waitKey()
    for i in range(2*r):
        for j in range(2*r):
            if (i-r)**2+(j-r)**2<r**2:
                a[int(c.imag)+i-r][int(c.real)+j-r]=img[i][j]
            else:
                a[int(c.imag)+i-r][int(c.real)+j-r]=(0,0,0)
    cv2.imshow('',a); cv2.waitKey()

'''358, 287
o tamanho do olho é "5x5"
dando um zoom numa parcela 600x600->720x720 da tela "em direção a 358,287" o que era 5x5 vira 6x6
a parcela do zoom será 58:658 no eixo x e 0:600 no eixo x
o novo centro do olho será em 300, 287
que é multiplicado por 1.2
360, 344
dando um zoom numa parcela 600x600->720x720 da tela "em direção a 360, 344" o que era 6x6 vira 7x7
a parcela do zoom será 60:660 no eixo x e 44:644 no eixo x
o novo centro do olho será em 300, 300
que é multiplicado por 1.2
360,360'''
