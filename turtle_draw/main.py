# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-10-28
#Version     : 1.0

import cv2
import numpy as np
import turtle

img=cv2.imread('img.png')
imgnew=np.ones((20,20,3),dtype='uint8')
imgnew=255*imgnew
def disp(poly,color):
    for x in poly:
        print(x)
        imgnew[x[0],x[1]]=color
    cv2.imshow('',cv2.resize(imgnew,(300,300),interpolation = cv2.INTER_AREA))
    cv2.waitKey()
    cv2.destroyAllWindows()

def adj(pos,x):
    if x==[]: return []
    nrep=[]
    for po in x:
        if po not in nrep:
            nrep.append(po)
    found=[]
    for po in nrep:
        if (po[0],po[1]) in pos:
            found=found+[(po[0],po[1])]
        if (po[0]-1,po[1]) in pos:
            found=found+[(po[0]-1,po[1])]
        if (po[0]+1,po[1]) in pos:
            found=found+[(po[0]+1,po[1])]
        if (po[0],po[1]-1) in pos:
            found=found+[(po[0],po[1]-1)]
        if (po[0],po[1]+1) in pos:
            found=found+[(po[0],po[1]+1)]
        if po in pos: pos.pop(pos.index(po))
    next=[]
    for el in found:
        next.append(el)
    for po in nrep:
        if po in pos:
            next.pop(next.index(po))
    return found+adj(pos,next)

def find(img):
    pos=[]
    print(np.where(img==255))
    print(img.shape)
    all=np.reshape(img, (img.shape[0]*img.shape[1],3))
    colors=np.unique(all,axis=0)
    for color in colors:
        if color[0]!=255 and color[1]!=255 and color[2]!=255:
            findpro(img,color)

def findpro(img,color):
    pos=[]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j,0]==color[0] and img[i,j,1]==color[1] and img[i,j,2]==color[2]: 
                pos.append((i,j))
    polygon=[]
    while pos!=[]:
        polygon.append(adj(pos,[pos[0]]))
    newpoly=[]
    for el in polygon:
        if not el in newpoly:
            newpoly.append(el)
    for poly in newpoly:
        disp(poly,color)
    return polygon

find(img)
turtle.forward(100)