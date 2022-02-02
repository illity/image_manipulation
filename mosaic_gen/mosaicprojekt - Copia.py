# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-04
#Version     : 1.0

﻿import cv2
import numpy as np
import time
import os
import glob
n=238
tilesz=(50,50)
imgsz=(50,50)
last=[]*5

def foldprep(folder):
 folder = folder.strip('\u202a')
 os.chdir(folder)
 filenames = [x for x in glob.glob('*.jpg')]
 for i in range(len(filenames)):
  os.chdir(folder)
  img=cv2.imread(filenames[i])
  newimg=cv2.resize(img, tilesz, interpolation = cv2.INTER_AREA)
  os.chdir('c:/prog/mosaic/images'.strip('\u202a'))
  cv2.imwrite('img{}.png'.format(i), newimg)
 #foldprep('C:/prog/mosaic/images')

def mean(filename):
 print(filename)
 img = cv2.imread(filename)
 b, g, r = img[...,0], img[...,1], img[...,2]
 return np.mean(b), np.mean(g), np.mean(r)
 #mean('rec.jpg')

def imgxmean():
 imgx=[mean('images/img{}.png'.format(i)) for i in range(n)]
 return imgx

def match(pixel, data):
 mindiff=3*(255**2)
 chosen=0
 for i in range(len(data)):
  diff=(pixel[0]-data[i][0])**2+(pixel[1]-data[i][1])**2+(pixel[2]-data[i][2])**2
  if diff<mindiff and chosen not in last:
   chosen=i
   mindiff=diff
 last=[last[1],last[2],chosen]
 return chosen

def mosaic(filename, data):
 original = cv2.imread(filename)
 chosens=[]
 for i in range(imgsz[0]):
  chosens.append([(match(original[i,j], data)) for j in range(imgsz[1])])
 build(chosens)

def build(chosens):
 final=np.zeros((imgsz[0]*tilesz[0],imgsz[1]*tilesz[1],3), np.uint8)
 for i in range(imgsz[0]):
  for j in range(imgsz[1]):
   img = cv2.imread('images/img{}.png'.format(chosens[i][j]))
   for k in range(tilesz[0]):
    for l in range(tilesz[0]):
     final[i*imgsz[0]+k,j*imgsz[1]+l]=img[k,l]
 cv2.imwrite('final.png',final)
#foldprep('‪c:/users/-/downloads/wallpapers')
#foldprep('c:/users/-/pictures/screenshots')
#print(mean('images/img1.png'))
data = imgxmean()
#print(match((123,93,41),data))
a=time.time()
mosaic('images/img46.png',data)
print(time.time()-a)
