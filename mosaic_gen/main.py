# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-10-29
#Version     : 1.0

import cv2
import numpy as np
import time
import os
import glob

n=115
tilesz=(200,200)
tiles_source='C:/users/-/temp/julia_chansz'
tiles_path='c:/prog/temp'
photo_path='c:/prog/temp'
photo_filename='img103.png'
imgsz=[]
def foldprep(folder):
    folder = folder.strip('\u202a')
    os.chdir(folder)
    filenames = [x for x in glob.glob('*.jpg')]
    for i in range(len(filenames)):
        os.chdir(folder)
        img=cv2.imread(filenames[i])
        newimg=cv2.resize(img, tilesz, interpolation = cv2.INTER_AREA)
        os.chdir(tiles_path.strip('\u202a'))
        cv2.imwrite('img{}.png'.format(i), newimg)
    #foldprep('C:/prog/mosaic/images')

def mean(filename):
    os.chdir(tiles_path.strip('\u202a'))
    print(filename)
    img = cv2.imread(filename)
    b, g, r = img[...,0], img[...,1], img[...,2]
    return np.mean(b), np.mean(g), np.mean(r)
    #mean('rec.jpg')

def imgxmean():
    os.chdir(tiles_path.strip('\u202a'))
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
    os.chdir(photo_path.strip('\u202a'))
    original = cv2.imread(filename)
    os.chdir(tiles_path.strip('\u202a'))
    chosens=[]
    for i in range(imgsz[1]):
        line=[-1]*imgsz[0]
        for j in range(imgsz[0]):
            line[j]=match(original[i,j], data, line, chosens)
        chosens.append(line)
    build(chosens)

def build(chosens):
    for i in range(imgsz[1]):
        for j in range(imgsz[0]):
            if j==0: img = cv2.imread('img{}.png'.format(chosens[i][0]))
            else:
                img2 = cv2.imread('img{}.png'.format(chosens[i][j]))
                img = np.concatenate((img, img2), axis=1)
        if i==0: final = img
        else:
            final=np.concatenate((final, img), axis=0)
    cv2.imwrite('3004.png',final)

foldprep(tiles_source)
#print(mean('images/img1.png'))
os.chdir(photo_path.strip('\u202a'))
imgsz=(cv2.imread(photo_filename).shape[1],cv2.imread(photo_filename).shape[0])
data = imgxmean()
#print(match((123,93,41),data))
a=time.time()
mosaic(photo_filename,data)
print(time.time()-a)