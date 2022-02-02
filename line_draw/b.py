# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-06-09
#Version     : 1.0

import cv2
import numpy as np

raio = 200
th_div = 100
pontos = []

def dist(a,b):
    return int(((a[0]-b[0])**2+(a[1]-b[1])**2)**.5)+1

def nextline(origem,img_gray):
    #map -> centro será shape/2, do centro cria-se raio r
    #cv2.line(img_gray,pontos[origem],pontos[i],(0,0,0),1)\
    highest = [0,9999999999] # quanto menor o score, melhor, o primeiro valor é o angulo e o segundo o score
    for i in range(th_div):
        if i == origem: continue
        soma = 0
        dist = [pontos[i][0] - pontos[origem][0],\
                                        pontos[i][1] - pontos[origem][1]]
        slope = (max(abs(dist[0]),abs(dist[1]))+1) / (min(abs(dist[0]),abs(dist[1]))+1)
        if abs(dist[1])>=abs(dist[0]):
            if dist[1]>0:
                for i in range(abs(dist[1])+1):
                    pos=(int(i/slope)+pontos[origem][1],i+pontos[origem][0])
            if dist[1]<0:
                for i in range(abs(dist[1])+1):
                    pos=(-int(i/slope)+pontos[origem][1],-i+pontos[origem][0])
        else:
            if dist[0]>0:
                for i in range(abs(dist[0])+1):
                    pos=(i+pontos[origem][0],int(i/slope)+pontos[origem][1])
            if dist[0]<0:
                for i in range(abs(dist[0])+1):
                    pos=(-i+pontos[origem][0],-int(i/slope)+pontos[origem][1])
        if soma<highest[1]: highest[0]=i; highest[1]=soma
    print(highest)
    for j in range(distancia):
        pos = (int(pontos[origem][0] + j*(pontos[highest[0]][0] - pontos[origem][0])/distancia),\
                                    int(pontos[origem][1] + j*(pontos[highest[0]][1] - pontos[origem][1])/distancia))
        img_gray[pos[1],pos[0]] += 63
        draw[pos[1],pos[0]] = 0
    #cv2.imshow('',img_gray); cv2.waitKey(1)
    return highest[0]

img = cv2.imread('gaara.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.resize(img_gray, (500,500))
img_gray = np.array(img_gray,dtype=np.int32)
draw = 255*np.ones((img_gray.shape[0], img_gray.shape[1]),dtype=np.uint8)
c = img_gray.shape[0]//2+img_gray.shape[1]//2*1j
for i in range(th_div):
    pos=c+raio*np.e**((2*np.pi*i/th_div+np.pi/2)*1j)
    pontos.append((int(pos.real),int(pos.imag)))
    img_gray[int(pos.imag),int(pos.real)]=0
#print(pontos)
last=0
#angulos serão 0 a 2pi
for i in range(1000):
    last = nextline(last,img_gray)
    if i%50==0: cv2.imshow('',draw); cv2.waitKey(1)
    