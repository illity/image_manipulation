# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-12
#Version     : 1.0

import cv2
import numpy as np

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
        #.,.,y,x,.,z
        #print(300*np.array(canon[i%3]))
        sq=translate(sq, (0,280,0))
        if i/3>=1:
            sq=translate(sq,300*np.array(canon[(1+i)%3]))
        face.append(sq)
    faces.append(face)
for i in range(6):
    for j in range(9):
        if i in [0,2,5]:
            rect(faces[i][j],cor[i][j])
        else:
            faces[i][j]=translate(faces[i][j], (510, 0, 0))
            rect(faces[i][j],cor[i][j])
cv2.imshow('rubik',img)
cv2.waitKey()