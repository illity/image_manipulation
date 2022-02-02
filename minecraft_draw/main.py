# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-08-02
#Version     : 1.0

import cv2
import numpy as np

#stone
#gold_block
#diamond_block
#redstone_block
#grass
#sand
#white_terracota
#nether_bricks

##Extraindo as cores

sample=cv2.imread('sample2.png')
sample_extract=sample[230:260,90:870]

#for i in range(2):
    #for j in range(8):
        #print(sample_extract.shape[1]/8) -> 48
        #color=(sample_extract[8+15*i,45+97*j])
colors=[sample_extract[8+15*i,45+97*j] for i in range(2) for j in range(8)]
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
#print(colors)
#for i in colors: print(i)

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
    if x==8: return res+'stone'
    if x==9: return res+'gold_block'
    if x==10: return res+'diamond_block'
    if x==11: return res+'redstone_block'
    if x==12: return res+'grass_block'
    if x==13: return res+'sand'
    if x==14: return res+'white_terracotta'
    if x==15: return res+'nether_bricks'

img=cv2.imread('c.jpeg')
img=cv2.resize(img,(img.shape[1]//6,img.shape[0]//6))
cv2.imshow('eloquin.jpg',img)
cv2.waitKey()
print(img.shape)
for i in range(img.shape[0]):
    print(i)
    for j in range(img.shape[1]):
        best=0
        mindiff=255*255*3
        for k in range(0,16):
            diff=(int(img[i,j,0])-int(colors[k][0]))**2+(int(img[i,j,1])-int(colors[k][1]))**2+(int(img[i,j,2])-int(colors[k][2]))**2
            if diff<mindiff: best=k; mindiff=diff
        #print(best)
        open('luisa.mcfunction','a').write('fill '+'{} 4 {} '.format(i,j)*2+cor(best)+'\n')
    #print(line)