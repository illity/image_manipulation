# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-10-28
#Version     : 1.0

from math import *
import cv2
import numpy as np

g=1
r1 = 100; r2 = 100
m1 = 10; m2 = 10
th1 = pi/2; th2 = pi/2
v1=0; v2=0

def tup(z):
    return (int(z.real),int(z.imag))

center = 200+100*1j
img = np.zeros((400,400,3),np.uint8)
frames=[]
#writer = cv2.VideoWriter("pendulum.mp4", cv2.VideoWriter_fourcc(*"xvid"), 30,(400,400))
start=10000
i=0
while(1):
    a1=(-g*(2*m1+m2)*sin(th1)-m2*g*sin(th1-2*th2)-2*sin(th1-th2)*m2*(v2**2*r2+v1**2*r1*cos(th1-th2)))/(r1*(2*m1+m2-m2*cos(2*th1-2*th2)))
    a2=(2*sin(th1-th2)*(v1**2*r1*(m1+m2)+g*(m1+m2)*cos(th1)+v2**2*r2*m2*cos(th1-th2)))/(r1*(2*m1+m2-m2*cos(2*th1-2*th2)))
    v1=v1+a1; v2=v2+a2
    th1=th1+v1; th2=th2+v2
    i=i+1
    bob1 = r1*e**(th1*1j+1j*pi/2); bob2 = bob1 + r2*e**(th2*1j+1j*pi/2)
    img2 = np.copy(cv2.circle(img, tup(center+bob2), 1, (255,0,0),1))
    if i>start:
        img2 = cv2.line(img2, tup(center), tup(center+bob1), (255,255,255),1)
        img2 = cv2.line(img2, tup(center+bob1), tup(center+bob2), (255,255,255),1)
        cv2.imshow('',img2); cv2.waitKey(1)
    #frames.append(img2)
#for frame in frames:
# writer.write(frame)
#writer.release()
