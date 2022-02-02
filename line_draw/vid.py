# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-06-09
#Version     : 1.0

import cv2
import numpy as np
filename='gordon'

img = cv2.imread(filename+'\\'+str(0)+'.png')
sz = (img.shape[0], img.shape[1])
writer = cv2.VideoWriter("{}.mp4".format(filename), cv2.VideoWriter_fourcc(*'XVID'), 15,sz)
for i in range(109):
    img=cv2.imread(filename+'\\'+str(i*20)+'.png')
    img3=cv2.imread(filename+'.png')
    img3=cv2.resize(img3,(120,120))
    img2 = cv2.resize(img,(120,120))
    img[60:180,60:180]=img2
    img[sz[0]-180:sz[0]-60,sz[1]-180:sz[1]-60]=img3
    writer.write(img)

writer.release()