# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-08-29
#Version     : 1.0

import numpy as np
import cv2

rx = lambda u,th: np.matmul(u,np.array([[1,0,0],[0,np.cos(th),-np.sin(th)],[0,np.sin(th),np.cos(th)]]))
ry = lambda u,th: np.matmul(u,np.array([[np.cos(th),0,np.sin(th)],[0,1,0],[-np.sin(th),0,np.cos(th)]]))
rz = lambda u,th: np.matmul(u,np.array([[np.cos(th),-np.sin(th),0],[np.sin(th),np.cos(th),0],[0,0,1]]))
def show(im,t=0): cv2.imshow('', im); cv2.waitKey(t)

class polygon():
    def __init__(self, v=np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]]), color=(0,0,0), fill=0, line=1):
        self.v = v; self.color = color; self.fill = fill; self.line=line
    def rx(self, th): self.v = rx(self.v,th)
    def ry(self, th): self.v = ry(self.v,th)
    def rz(self, th): self.v = rz(self.v,th)
    def _2d(self):
        T=np.array([[1, 0],[0, 1],[1/2, -(3**0.5)/2]])
        return (self.v@T).astype(np.int32)
    
class screen():
    def __init__(self, sz=(1920,1080,3)):
        self.sz = sz; self.objects = []
    def __add__(self, object):
        self.objects.append(object); return self
    def rotate(self, th):
        for obj in self.objects: obj.rx(th[0]); obj.ry(th[1]); obj.rz(th[2])
    def draw(self):
        img = 40*np.ones(self.sz).astype(np.uint8)
        for obj in self.objects:
            poly = obj._2d()+(self.sz[1]//2,self.sz[0]//2)
            pts = poly.reshape((1, -1, 2))
            if obj.fill: cv2.fillPoly(img,pts,obj.color)
            if obj.line: cv2.polylines(img,pts,0,(0,0,0),2)
        return img

scale, p = 200, 30
hat = [polygon(scale*np.array([[-1,-1, 1], [-1,.6, 1], [ 1,.6, 1], [ 1,-1, 1]]),(0,255,255),1),#trás
                            polygon(scale*np.array([[-1,-1,-1], [-1,-1, 1], [-1,.6, 1], [-1,.6,-1]]),(0,255,255),1),#esquerda
                            polygon(scale*np.array([[ 1,-1,-1], [ 1,-1, 1], [ 1,.6, 1], [ 1,.6,-1]]),(0,255,255),1),#direita
                            polygon(scale*np.array([[-1,-1,-1], [-1,.6,-1], [ 1,.6,-1], [ 1,-1,-1]]),(0,255,255),1),#frente
                            polygon(scale*np.array([[-1,-1,-1], [ 1,-1,-1], [ 1,-1, 1], [-1,-1, 1]]),(0,255,255),1)]#cima
eyes = [polygon(scale*np.array([ .4,-.5,-1])+.3*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),(40,200,200),1,0),#mancha
                                polygon(scale*np.array([-.4,-.5,-1])+.2*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),fill=1),#esquerdo
                                polygon(scale*np.array([ .4,-.5,-1])+.2*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),fill=1),#direito
                                polygon(scale*np.array([-.5,-.6,-1])+.1*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),(0,255,255),1,0),#brilho
                                polygon(scale*np.array([ .5,-.6,-1])+.1*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),(0,255,255),1,0)]#brilho
ears = [polygon(scale*np.array([-1.1,-1.1,-1])+.5*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),fill=1),
                                polygon(scale*np.array([ 1.1,-1.1,-1])+.5*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),fill=1)]
nose = polygon(scale*np.array([0,.4,-1])+.2*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(2*p)]),fill=1); hat.append(nose)
head = list()
for i in range(scale):
    new = polygon(scale*np.array([ 0, .6, 0])+.8*scale*np.array([[np.cos(np.pi*i/p), np.sin(np.pi*i/p),0] for i in range(-p//2,p//2)]),(162,204,235),1,0)
    new.ry(i*np.pi/50)
    head.append(new)
mouth = polygon(scale*np.array([0, 1, -.4])+.2*scale*np.array([[-1,0,0],[1,0,0]])); head.append(mouth)

sc = screen()
[sc+h for h in head]; [sc+h for h in hat]; [sc+e for e in ears]; [sc+e for e in eyes]
V=np.pi/300
writer = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"xvid"), 30,(1080,1920))
for i in range(20): sc.rotate((V,0,0)); writer.write(sc.draw())
for i in range(60): sc.rotate((0,V,0)); writer.write(sc.draw())
for i in range(60): sc.rotate((0,0,V)); writer.write(sc.draw())
for i in range(60): sc.rotate((0,-V,-V)); writer.write(sc.draw())
writer.release()