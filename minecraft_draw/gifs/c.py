# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-08-14
#Version     : 1.0

import cv2
import imageio
import glob

filenames = glob.glob('dio\*.png')
image_lst = [cv2.imread(file) for file in filenames]
writer = cv2.VideoWriter("dio.mp4", cv2.VideoWriter_fourcc(*"xvid"), 15,(image_lst[0].shape[1],image_lst[0].shape[0]))
for i in range(12):
    for frame in image_lst:
        writer.write(frame)

writer.release()