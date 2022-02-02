# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-12
#Version     : 1.0

import cv2
import numpy as np

def dist(a,b):
    return (((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5)

def sort(va,vb,vc,vd):
    list=np.array([va,vb,vc,vd])
    x=list[...,0]
    y=list[...,1]
    print(y)
    l=list[np.where(x==min(x))[0]]
    #topleft=l[np.where(l==np.amax(l))[0][0]]
    #print(topleft)
    r=list[np.where(x==max(x))[0]]
    u=list[np.where(y==min(y))[0]]
    d=list[np.where(y==max(y))[0]]
    #ponto xy=(12,19)
    #topleft line
    line=np.array([[l[np.where(l==np.amax(l))[0][0]][0],l[np.where(l==np.amax(l))[0][0]][1]]])
    for i in range(int(dist(l[np.where(l==np.amax(l))[0][0]],u[np.where(u==np.amin(u))[0][0]]))):
        #print(int(dist(l[np.where(l==np.amax(l))[0][0]],u[np.where(u==np.amin(u))[0][0]])))
        #x=print((u[np.where(u==np.amin(u))[0][0]][0]-l[np.where(l==np.amax(l))[0][0]][0]))
        #y=print((u[np.where(u==np.amin(u))[0][0]][1]-l[np.where(l==np.amax(l))[0][0]][1]))
        xi=l[np.where(l==np.amax(l))[0][0]][0]+(i+1)*((u[np.where(u==np.amin(u))[0][0]][0]-l[np.where(l==np.amax(l))[0][0]][0]))/dist(l[np.where(l==np.amax(l))[0][0]],u[np.where(u==np.amin(u))[0][0]])
        yi=l[np.where(l==np.amax(l))[0][0]][1]+(i+1)*((u[np.where(u==np.amin(u))[0][0]][1]-l[np.where(l==np.amax(l))[0][0]][1]))/dist(l[np.where(l==np.amax(l))[0][0]],u[np.where(u==np.amin(u))[0][0]])
        line=np.append(line, [[xi,yi]],axis=0)
    #print(line)
    #mais da esquerda entre os dois: l[np.where(l==np.amax(l))[0][0]][0]
    #mais da direita entre os dois:  u[np.where(u==np.amin(u))[0][0]][0]
    #mais de baixo entre os dois:    l[np.where(l==np.amax(l))[0][0]][1]
    #mais de cima entre os dois:     u[np.where(u==np.amin(u))[0][0]][1]
    for i in range(l[np.where(l==np.amax(l))[0][0]][0],u[np.where(u==np.amin(u))[0][0]][0]):
        for j in range(u[np.where(u==np.amin(u))[0][0]][1],l[np.where(l==np.amax(l))[0][0]][1]):
            #tracando paralela ao eixo y print(line[np.where(line[...,0].astype(np.uint16)==i)][0])
            if j>line[np.where(line[...,0].astype(np.uint16)==i)][0][1]:
                img[j,i]=(255)
    #topright
    line=np.array([[r[np.where(r==np.amax(r))[0][0]][0],u[np.where(u==np.amax(u))[0][0]][1]]])
    for i in range(int(dist(r[np.where(r==np.amax(r))[0][0]],u[np.where(u==np.amin(u))[0][0]]))):
        xi=r[np.where(r==np.amax(r))[0][0]][0]+(i+1)*((u[np.where(u==np.amin(u))[0][0]][0]-r[np.where(r==np.amax(r))[0][0]][0]))/dist(r[np.where(r==np.amax(r))[0][0]],u[np.where(u==np.amin(u))[0][0]])
        yi=r[np.where(r==np.amax(r))[0][0]][1]+(i+1)*((u[np.where(u==np.amin(u))[0][0]][1]-r[np.where(r==np.amax(r))[0][0]][1]))/dist(r[np.where(r==np.amax(r))[0][0]],u[np.where(u==np.amin(u))[0][0]])
        line=np.append(line, [[xi,yi]],axis=0)
    for i in range(u[np.where(u==np.amin(u))[0][0]][0],r[np.where(r==np.amax(r))[0][0]][0]):
        for j in range(u[np.where(u==np.amin(u))[0][0]][1],r[np.where(r==np.amax(r))[0][0]][1]):
            if j>line[np.where(line[...,0].astype(np.uint16)==i)][0][1]:
                img[j,i]=(255)
    #bottomright
    line=np.array([[r[np.where(r==np.amax(r))[0][0]][0],d[np.where(d==np.amax(d))[0][0]][1]]])
    for i in range(int(dist(r[np.where(r==np.amax(r))[0][0]],d[np.where(d==np.amin(d))[0][0]]))):
        xi=r[np.where(r==np.amax(r))[0][0]][0]+(i+1)*((d[np.where(d==np.amin(d))[0][0]][0]-r[np.where(r==np.amax(r))[0][0]][0]))/dist(r[np.where(r==np.amax(r))[0][0]],d[np.where(d==np.amin(d))[0][0]])
        yi=r[np.where(r==np.amax(r))[0][0]][1]+(i+1)*((d[np.where(d==np.amin(d))[0][0]][1]-r[np.where(r==np.amax(r))[0][0]][1]))/dist(r[np.where(r==np.amax(r))[0][0]],d[np.where(d==np.amin(d))[0][0]])
        line=np.append(line, [[xi,yi]],axis=0)
    for i in range(d[np.where(d==np.amin(d))[0][0]][0],r[np.where(r==np.amax(r))[0][0]][0]):
        for j in range(r[np.where(r==np.amax(r))[0][0]][1],d[np.where(d==np.amin(d))[0][0]][1]):
            if j<line[np.where(line[...,0].astype(np.uint16)==i)][0][1]:
                img[j,i]=(255)
    #bottomleft
    line=np.array([[l[np.where(l==np.amax(l))[0][0]][0],d[np.where(d==np.amax(d))[0][0]][1]]])
    for i in range(int(dist(l[np.where(l==np.amax(l))[0][0]],d[np.where(d==np.amin(d))[0][0]]))):
        xi=l[np.where(l==np.amax(l))[0][0]][0]+(i+1)*((d[np.where(d==np.amin(d))[0][0]][0]-l[np.where(l==np.amax(l))[0][0]][0]))/dist(l[np.where(l==np.amax(l))[0][0]],d[np.where(d==np.amin(d))[0][0]])
        yi=l[np.where(l==np.amax(l))[0][0]][1]+(i+1)*((d[np.where(d==np.amin(d))[0][0]][1]-l[np.where(l==np.amax(l))[0][0]][1]))/dist(l[np.where(l==np.amax(l))[0][0]],d[np.where(d==np.amin(d))[0][0]])
        line=np.append(line, [[xi,yi]],axis=0)
    for i in range(l[np.where(l==np.amin(l))[0][0]][0],d[np.where(d==np.amin(d))[0][0]][0]):
        print('oi')
        for j in range(l[np.where(l==np.amax(l))[0][0]][1],d[np.where(d==np.amin(d))[0][0]][1]):
            if j<line[np.where(line[...,0].astype(np.uint16)==i)][0][1]:
                img[j,i]=(255)





    newlist=[] #mais da esquerda, mais de cima, mais da direita, mais de baixo
    left=[]

def rectangle(im,va,vb,vc,vd):
    cont=0
    return im

def start():
    print('oi')

rubik=[['R']*9]*6
img=np.zeros((500,500,3), np.uint8)
rectangle(img, (20,20), (20,40), (40,40), (40,20))
sort((0,432), (125,216), (250,432), (250,432))
sort((250,432),(375,216),(500,432), (500,432))
sort((125,216),(250,0),(375,216),(375,216))
cv2.imshow('',img)
cv2.waitKey()
cv2.destroyAllWindows()
print(rubik[0][1])