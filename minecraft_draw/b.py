# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-03-19
#Version     : 1.0

import cv2
import numpy as np

##Extraindo as cores
sample=cv2.imread('sample.png')
sample_extract=sample[230:260,290:680]
for i in range(8):
    #print(sample_extract.shape[1]/8) -> 48
    color=(sample_extract[25,23+47*i])
colors=[sample_extract[25,23+47*i] for i in range(8)]
    #cmp=np.zeros((50,50,3),dtype=np.uint8)
    #print(color)
    #for l in range (50):
    # for j in range(50):
    #  for k in range(3):
    #   cmp[l,j,k]=color[k]
    #print(cmp)
    #cv2.imshow('',cmp)
    #cv2.waitKey()
#cv2.imshow('',sample_extract)
#cv2.waitKey()
print(colors)

def cor(x):
    res='minecraft:'
    if x==0: return res+'white_wool'
    if x==1: return res+'black_wool'
    if x==2: return res+'red_wool'
    if x==3: return res+'lime_wool'
    if x==4: return res+'lapis_block'
    if x==5: return res+'magenta_wool'
    if x==6: return res+'light_blue_wool'
    if x==7: return res+'yellow_wool'

img=cv2.imread('gon.jpg')
#cv2.imshow('',img)
#cv2.waitKey()
for i in range(137):
    print(i)
    for j in range(243):
        best=0
        mindiff=255*255*3
        for k in range(0,8):
            diff=(int(img[i,j,0])-int(colors[k][0]))**2+(int(img[i,j,1])-int(colors[k][1]))**2+(int(img[i,j,2])-int(colors[k][2]))**2
            if diff<mindiff: best=k; mindiff=diff
        #print(best)
        open('gon.mcfunction','a').write('fill '+'{} 4 {} '.format(i,j)*2+cor(best)+'\n')
    #print(line)