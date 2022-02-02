# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-08-28
#Version     : 1.0

import cv2
import numpy as np
import random
from math import sin,cos

def rect(sq,color):
    v1, v2, v3, v4=sq
    T=np.array([[1, 0, 0],[0, 1, 0],[1/2, -(3**0.5)/2, 0]])
    arr=[(np.matmul(v1,T)),(np.matmul(v2,T)),(np.matmul(v3,T)),(np.matmul(v4,T))]
    arroz=np.array(arr)[:,:2].astype(np.int32)
    arroz=arroz.reshape((-1,1,2))
    cv2.fillPoly(img,[arroz],color)

def translate(u, v):
    for i in range(len(u)):
        for j in range(len(v)):
            u[i][j]=u[i][j]+v[j]
    return u

def rotatey(u, th):
    return np.matmul(u,[[cos(th),0,sin(th)],[0,1,0],[-sin(th),0,cos(th)]])
def rotatex(u,th):
    return np.matmul(u,[[1,0,0],[0,cos(th),-sin(th)],[0,sin(th),cos(th)]])
def rotatez(u,th):
    return np.matmul(u,[[cos(th),-sin(th),0],[sin(th),cos(th),0],[0,0,1]])

cor=[[(255,0,0)]*9,[(0,255,0)]*9,[(0,0,255)]*9,[(0,255,255)]*9,[(255,0,255)]*9,[(255,255,0)]*9]
#cor=[[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(9)]for j in range(6)]
print(cor)
canon = [[1,0,0], [0,1,0], [0,0,1]]
print(canon)
img = np.zeros((800,1000,3))
faces=[]
for k in range(10):
    for i in range(6):
        t=np.array([canon[i%2+(i%3==0)+(i==1)],canon[i%3]])
        face=[]
        for j in range(9):
            #bsq=np.array([[100*(j%3),100+100*int(j/3)], [100+100*(j%3),100+100*int(j/3)], [100+100*(j%3),+100*int(j/3)], [100*(j%3),100*int(j/3)]])
            bsq=np.array([[100+100*int(j/3),100*(j%3)], [100+100*int(j/3),100+100*(j%3)], [100*int(j/3),100+100*(j%3)], [100*int(j/3),100*(j%3)]])
            sq=(np.matmul(bsq,t))
            if i/3>=1: sq=translate(sq,300*np.array(canon[(1+i)%3]))
            centro=np.array([200, 200, 200])
            sq=sq-centro
            sq=rotatex(sq,0.8)
            sq=sq+centro
            xd=translate(sq, (300,300,0))
            face.append(xd)
        faces.append(face)
    organizar=[faces[0],faces[1],faces[2],faces[4],faces[5],faces[3]]
    faces=np.array(organizar)
    z=faces[:,4,:,2]
    for i in range(3):
        for j in range(9):
            if i==0: rect(faces[np.where(faces[:,4,:,0]==np.amax(faces[:,4,:,0]))[0][0],j],cor[i][j])
            if i==1: rect(faces[np.where(faces[:,4,:,1]==np.amin(faces[:,4,:,1]))[0][0],j],cor[i][j])
            if i==2: rect(faces[np.where(faces[:,4,:,2]==np.amin(faces[:,4,:,2]))[0][0],j],cor[i][j])
            # img=cv2.resize(img,(640,360))
    img=np.array(img,dtype=np.uint8)
    cv2.imshow('rubik',img)
    cv2.waitKey()
cv2.destroyAllWindows()