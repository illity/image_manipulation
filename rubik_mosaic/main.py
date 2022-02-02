# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 25/02/2020
#Version     : 1.0

import numpy as np
import cv2

def square(r,g,b):
    img=np.zeros((20,20,3),dtype='uint8')
    for i in range(18):
        for j in range(18):
            img[i+1,j+1,0]=b
            img[i+1,j+1,1]=g
            img[i+1,j+1,2]=r
    return img

def imgxmean(cube):
    imgx=[mean(i) for i in cube]
    return imgx

def mean(img):
    b, g, r = img[...,0], img[...,1], img[...,2]
    return np.mean(b), np.mean(g), np.mean(r)

def match(pixel, data, line, chosens):
    mindiff=3*(255**2)
    chosen=0
    for i in range(len(data)):
        diff=(pixel[0]-data[i][0])**2+(pixel[1]-data[i][1])**2+(pixel[2]-data[i][2])**2
        if diff<mindiff:
            chosen=i
            mindiff=diff
    return chosen

def mosaic(data):
    chosens=[]
    for i in range(imgsz[1]):
        line=[-1]*imgsz[0]
        for j in range(imgsz[0]):
            line[j]=match(original[i,j], data, line, chosens)
        chosens.append(line)
    build(chosens)

def build(chosens):
    final=np.zeros((imgsz[1]*tilesz[1],imgsz[0]*tilesz[0],3), np.uint8)
    for i in range(imgsz[1]):
        for j in range(imgsz[0]):
            img = cube[chosens[i][j]]
            for k in range(tilesz[0]):
                for l in range(tilesz[1]):
                    final[i*tilesz[0]+k,j*tilesz[1]+l]=img[k,l]
    cv2.imwrite('final.png',final)

filename='img.png'
green=square(0,155,72)
red=square(185,0,0)
blue=square(0,69,173)
white=square(255,255,255)
yellow=square(255,213,0)
orange=square(255,89,0)
tilesz=(20,20)
cube=[green,red,blue,white,yellow,orange]
imgsz=(96,40)
original=cv2.resize(cv2.imread(filename),imgsz)
mosaic(imgxmean(cube))
cv2.waitKey()