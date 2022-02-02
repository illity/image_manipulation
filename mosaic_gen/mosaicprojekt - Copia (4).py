# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-04
#Version     : 1.0

﻿import cv2
import numpy as np
import time
import os
import glob
n=626
tilesz=(30,30)
pasta_fotos='c:/prog/mosaic/dofus/images'
foto='C:\prog\mosaic\lvup'

def foldprep(folder):
 folder = folder.strip('\u202a')
 os.chdir(folder)
 filenames = [x for x in glob.glob('*.png')]
 for i in range(len(filenames)):
  os.chdir(folder)
  img=cv2.imread(filenames[i])
  newimg=cv2.resize(img, tilesz, interpolation = cv2.INTER_AREA)
  os.chdir(pasta_fotos.strip('\u202a'))
  cv2.imwrite('img{}.png'.format(i), newimg)
 #foldprep('C:/prog/mosaic/images')

def mean(filename):
 os.chdir(pasta_fotos.strip('\u202a'))
 img = cv2.imread(filename)
 b, g, r = img[...,0], img[...,1], img[...,2]
 return np.mean(b), np.mean(g), np.mean(r)
 #mean('rec.jpg')

def imgxmean():
 os.chdir(pasta_fotos.strip('\u202a'))
 imgx=[mean('img{}.png'.format(i)) for i in range(n)]
 return imgx

def match(pixel, data, line, chosens):
 mindiff=3*(255**2)
 chosen=0
 for i in range(len(data)):
  diff=(pixel[0]-data[i][0])**2+(pixel[1]-data[i][1])**2+(pixel[2]-data[i][2])**2
  diff=diff+999*line.count(i)+(9999*chosens[len(chosens)-1].count(i) if len(chosens)>=1 else 0)+(999*chosens[len(chosens)-2].count(i) if len(chosens)>=2 else 0)
  if diff<mindiff:
   chosen=i
   mindiff=diff
 return chosen

def mosaic(filename, data):
 os.chdir(foto.strip('\u202a'))
 original = cv2.imread(filename)
 os.chdir(pasta_fotos.strip('\u202a'))
 chosens=[]
 for i in range(imgsz[1]):
  line=[-1]*imgsz[0]
  for j in range(imgsz[0]):
   line[j]=match(original[i,j], data, line, chosens)
  chosens.append(line)
 build(chosens,filename)

def build(chosens,filename):
 final=np.zeros((imgsz[1]*tilesz[1],imgsz[0]*tilesz[0],3), np.uint8)
 for i in range(imgsz[1]):
  for j in range(imgsz[0]):
   img = cv2.imread('img{}.png'.format(chosens[i][j]))
   for k in range(tilesz[0]):
    for l in range(tilesz[1]):
     final[i*tilesz[0]+k,j*tilesz[1]+l]=img[k,l]
 cv2.imwrite('mosaic'+filename,final)

#foldprep('c:/prog/mosaic/dofus/icones')
#print(mean('images/img1.png'))
#foldprep(foto)
os.chdir(foto.strip('\u202a'))
filenames = [x for x in glob.glob('*.png')]
for f in filenames:
 os.chdir(foto.strip('\u202a'))
 imgsz=(cv2.imread(f).shape[1],cv2.imread(f).shape[0])
 data = imgxmean()
 #print(match((123,93,41),data))
 a=time.time()
 mosaic(f,data)
 print(time.time()-a)
