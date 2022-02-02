# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-06-09
#Version     : 1.0

a = (0,0)
b = (2,8)
dist = [b[0]-a[0],b[1]-a[1]]
slope = (max(abs(dist[0]),abs(dist[1]))+1) / (min(abs(dist[0]),abs(dist[1]))+1)
if abs(dist[1])>=abs(dist[0]):
    if dist[1]>0:
        for i in range(abs(dist[1])+1):
            print(int(i/slope)+a[1],i+a[0])
    if dist[1]<0:
        for i in range(abs(dist[1])+1):
            print(-int(i/slope)+a[1],-i+a[0])
else:
    if dist[0]>0:
        for i in range(abs(dist[0])+1):
            print(i+a[0],int(i/slope)+a[1])
    if dist[0]<0:
        for i in range(abs(dist[0])+1):
            print(-i+a[0],-int(i/slope)+a[1])


distancia = dist(pontos[origem],pontos[i])
        for j in range(distancia):
            pos = (int(pontos[origem][0] + j*(pontos[i][0] - pontos[origem][0])/distancia),\
                                        int(pontos[origem][1] + j*(pontos[i][1] - pontos[origem][1])/distancia))
        soma += img_gray[pos[1],pos[0]]/distancia