# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-08-14
#Version     : 1.0

import cv2
import numpy as np

sample=cv2.imread('sample2.png')
sample_extract=sample[230:260,90:870]
colors=np.array([sample_extract[8+15*i,45+97*j] for i in range(2) for j in range(8)]).astype(np.int64)

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
colorset = [cor(i) for i in range(16)]

import time
vid = cv2.VideoCapture('dio.gif')
im=0
while(1): 
    ret, img = vid.read()
    tempo=time.time()
    diff = np.argmin(np.array([np.sum((img-colors[i])**2,axis=2) for i in range(colors.shape[0])]),axis=0)
    print(time.time()-tempo)
    quit()
    best=np.argmin(np.sum((colors-img[i,j])**2,axis=1))
    line+='fill '+'{} {} 0 '.format(i,j)*2+colorset[best]+'\n'
    open(f'dio{im}.mcfunction','a').write(line)
    im+=1
