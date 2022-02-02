# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-06-09
#Version     : 1.0

a = (0,0)
b = (2,8)
dx = b[0]-a[0]
dy = b[1]-a[1]
slope = (max(abs(dx),abs(dy))+1) / (min(abs(dx),abs(dy))+1)
if abs(dy)>=abs(dx):
    if dy>0:
        for i in range(abs(dy)+1):
            print(int(i/slope)+a[1],i+a[0])
    if dy<0:
        for i in range(abs(dy)+1):
            print(-int(i/slope)+a[1],-i+a[0])
else:
    if dx>0:
        for i in range(abs(dx)+1):
            print(i+a[0],int(i/slope)+a[1])
    if dx<0:
        for i in range(abs(dx)+1):
            print(-i+a[0],-int(i/slope)+a[1])
