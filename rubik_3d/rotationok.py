# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-12
#Version     : 1.0

import cv2
import numpy as np
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
canon = [[1,0,0], [0,1,0], [0,0,1]]
print(canon)
img = np.zeros((600,1000,3))
faces=[]
for i in range(6):
    face=[]
    t=np.array([canon[i%2+(i%3==0)+(i==1)],canon[i%3]])
    for j in range(9):
        #bsq=np.array([[(4*(j%3!=0))+100*(j%3),100+100*int(j/3)], [100+100*(j%3),100+100*int(j/3)], [100+100*(j%3),(4*(int(j/3)!=0))+100*int(j/3)],[(4*(j%3!=0))+100*(j%3),(4*(int(j/3)!=0))+100*int(j/3)]])
        bsq=np.array([[100+100*int(j/3),(4*(j%3!=0))+100*(j%3)], [100+100*int(j/3),100+100*(j%3)], [(4*(int(j/3)!=0))+100*int(j/3),100+100*(j%3)],[(4*(int(j/3)!=0))+100*int(j/3),(4*(j%3!=0))+100*(j%3)]])
        sq=(np.matmul(bsq,t))
        centro=np.array([203, 203, 203])
        sq=sq-centro
        print(sq-centro)
        sq=np.matmul(sq,[[0,0,1],[0,1,0],[-1,0,0]])
        sq=rotatez(sq,1.57)	
        sq=sq+centro
#  rot=[[0.7,0,0.7],[0,1,0],[-0.7,0,0.7]]
#  sq=np.matmul(sq,rot)
        #.,.,y,x,.,z
        #print(300*np.array(canon[i%3]))
        sq=translate(sq, (0,500,0))
        face.append(sq)
    faces.append(face)
for i in range(3):
    for j in range(9):
        rect(faces[i][j],cor[i][j])
#  if i in [0,2,5]:
#   rect(faces[i][j],cor[i][j])
#  else:
#   faces[i][j]=translate(faces[i][j], (510, 0, 0))
#   rect(faces[i][j],cor[i][j])
cv2.imshow('rubik',img)
cv2.waitKey()