# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-12
#Version     : 1.0

import cv2
import numpy as np

img = np.zeros((500,500,3),dtype=np.uint8)
def rect(sq):
    v1, v2, v3, v4=sq
    T=np.array([[1, 0, 0],[0, 1, 0],[1/2, -(3**0.5)/2, 0]])
    arr=[(np.matmul(v1,T)),(np.matmul(v2,T)),(np.matmul(v3,T)),(np.matmul(v4,T))]
    arroz=np.array(arr)[:,:2].astype(np.int32)
    arroz=arroz.reshape((-1,1,2))
    cv2.fillPoly(img,[arroz],(255,0,0))
    cv2.imshow('',img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def translate(u, v):
    for i in range(len(u)):
        for j in range(len(v)):
            u[i][j]=u[i][j]+v[j]
    return u
canon = np.array([[0,0,1], [0,1,0], [1,0,0]])
print(canon)
for i in range(6):
    for j in range(9):
        bsq=np.array([(4*(j%3!=0))+100*(j%3),100+100*int(j/3)], [100+100*(j%3),100+100*int(j/3)], [100+100*(j%3),(4*(int(j/3)!=0))+100*int(j/3)],[(4*(j%3!=0))+100*(j%3),(4*(int(j/3)!=0))+100*int(j/3)])
        print(bsq)
        print(np.matmul(bsq, canon[:1]))
        #sq=[(4*(not not j%3))+100*(j%3),100+100*int(j/3),0], [100+100*(j%3),100+100*int(j/3),0], [100+100*(j%3),(4*(not not int(j/3)))+100*int(j/3),0], [(4*(not not j%3))+100*(j%3),(4*(not not int(j/3)))+100*int(j/3),0]
        sq=translate(sq,[0,100,0])
        print(sq)
        #o do topo seria quase o mesmo mas movendo no eixo z ao inves do eixo x
        #sq=[0,100+100*int(j/3),(4*(not not j%3))+100*(j%3)], [0,100+100*int(j/3),100+100*(j%3)], [0,(4*(not not int(j/3)))+100*int(j/3),100+100*(j%3)], [0,(4*(not not int(j/3)))+100*int(j/3),(4*(not not j%3))+100*(j%3)]
        rect(sq)
    for j in range(9):
        sq=[100+100*int(j/3),0,(4*(not not j%3))+100*(j%3)], [100+100*int(j/3),0,100+100*(j%3)], [(4*(not not int(j/3)))+100*int(j/3),0,100+100*(j%3)], [(4*(not not int(j/3)))+100*int(j/3),0,(4*(not not j%3))+100*(j%3)]
        sq=translate(sq,[0,100,0])
        rect(sq)