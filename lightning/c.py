# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-09-05
#Version     : 1.0

import cv2
import numpy as np

sz, scale, p, q = 60, 10, 0.4, 0.4#chance em x, chance em y
maze, img = np.random.random((sz,sz,2)), np.zeros((scale*sz,scale*sz,3)).astype(np.uint8)

def pathfind(maze,pos,depth):
    d = np.zeros((sz,sz)); d[pos] = 1; depth+=1
    queue = [pos]
    while np.any(d==0) and np.all(d[:,-1]==0) and queue!=[]:
        newqueue = []
        for pos in queue:
            if maze[pos[0],pos[1],1]>q and pos[0]<sz-1: #direita
                if not d[pos[0]+1,pos[1]]:
                    d[pos[0]+1,pos[1]] = depth; newqueue.append((pos[0]+1,pos[1]))
            if maze[pos[0],pos[1]+1,0]>p and pos[1]<sz-1: #baixo
                if not d[pos[0],pos[1]+1]:
                    d[pos[0],pos[1]+1] = depth; newqueue.append((pos[0],pos[1]+1))
            if maze[pos[0]-1,pos[1],1]>q and pos[0]>0: #esquerda
                if not d[pos[0]-1,pos[1]]:
                    d[pos[0]-1,pos[1]] = depth; newqueue.append((pos[0]-1,pos[1]))
            if maze[pos[0],pos[1],0]>p and pos[1]>0: #cima
                if not d[pos[0],pos[1]-1]:
                    d[pos[0],pos[1]-1] = depth; newqueue.append((pos[0],pos[1]-1))
        queue = newqueue; depth+=1
    return d.T

for i in range(sz): 
    for j in range(sz): 
        if maze[i,j,0]<p:  cv2.line(img,(scale*i,scale*j),(scale*i+scale,scale*j),(255,255,255)) 
        if maze[i,j,1]<q: cv2.line(img,(scale*i+scale,scale*j),(scale*i+scale,scale*j+scale),(255,255,255))

path = pathfind(maze,(sz//2,0),1)
for i in range(sz):
    for j in range(sz):
        sqr = np.array([[[scale*j+1,scale*i+1],[scale*(j+1)-1,scale*i+1],[scale*(j+1)-1,scale*(i+1)-1],[scale*j+1,scale*(i+1)-1]]]).astype(np.int32)
        if path[i][j]:
            cv2.fillPoly(img,sqr,(100+155*path[i][j]/np.amax(path),0,0))
end = (sz-1,np.argmax(path[-1]))
if path[end]==0: quit()#sem solução
shortcut = [end]
while(path[end]!=1):
    if path[end[0]-1,end[1]] == path[end]-1 and maze[end[1],end[0],0]>p: end = (end[0]-1,end[1]); shortcut.append(end); continue
    if path[end[0]+1,end[1]] == path[end]-1 and maze[end[1]+1,end[0],0]>p: end = (end[0]+1,end[1]); shortcut.append(end); continue
    if path[end[0],end[1]-1] == path[end]-1 and maze[end[1]-1,end[0],1]>p: end = (end[0],end[1]-1); shortcut.append(end); continue
    if path[end[0],end[1]+1] == path[end]-1 and maze[end[1],end[0],1]>p: end = (end[0],end[1]+1); shortcut.append(end); continue
for pos in shortcut:
    sqr = np.array([[[scale*pos[1]+1,scale*pos[0]+1],[scale*(pos[1]+1)-1,scale*pos[0]+1],[scale*(pos[1]+1)-1,scale*(pos[0]+1)-1],[scale*pos[1]+1,scale*(pos[0]+1)-1]]]).astype(np.int32);
    cv2.fillPoly(img,sqr,(0,0,100+155*path[pos[0]][pos[1]]/np.amax(path)))
cv2.imshow('',img); cv2.waitKey()