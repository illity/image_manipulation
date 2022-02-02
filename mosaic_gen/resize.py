# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-01-04
#Version     : 1.0

import sys
import os
import re
import cv2
#sys.argv[1] = input filename
#sys.argv[2] = output filename
if re.findall('(.*)/(.*)$',sys.argv[1])!=[]:
    b=re.findall('(.*)/(.*)$',sys.argv[1])[0]
    print(b)
    ipath, ifile = b[0], b[1]
    os.chdir(ipath)
else:
    ifile=sys.argv[1]
img=cv2.imread(ifile)
if re.findall('(.*)/(.*)$',sys.argv[2])!=[]:
    b=re.findall('(.*)/(.*)$',sys.argv[2])[0]
    print(b)
    opath, ofile = b[0], b[1]
    os.chdir(opath)
else:
    ofile=sys.argv[2]
newimg=cv2.resize(img, (int(sys.argv[3]),int(sys.argv[4])), interpolation = cv2.INTER_AREA)
cv2.imwrite(ofile, newimg)
