# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-04-08
#Version     : 1.0

import cv2, numpy as np
import random
class pchar:
    A=[[0, 0, 0, 0, 0, 0, 255, 255, 255, 0], [255, 255, 255, 255, 255, 0, 255, 255, 255, 0], [255, 255, 255, 255, 0, 255, 255, 255, 255, 0], [255, 255, 255, 0, 255, 255, 255, 255, 255, 0], [255, 255, 0, 255, 255, 255, 255, 255, 255, 0], [0, 0, 255, 255, 255, 255, 255, 255, 255, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 0, 255, 255, 255, 255, 255, 255, 0], [255, 255, 0, 255, 255, 255, 255, 255, 255, 0], [255, 255, 0, 0, 0, 0, 0, 0, 0, 0]]
    B=[[255, 255, 255, 0, 255, 255, 255, 255, 255, 0], [0, 0, 0, 0, 0, 0, 0, 255, 255, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 0], [255, 255, 0, 0, 0, 255, 255, 255, 255, 0], [255, 0, 255, 255, 255, 0, 255, 0, 0, 0], [255, 0, 255, 255, 255, 0, 255, 255, 255, 0], [255, 255, 0, 0, 0, 255, 255, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 0], [255, 0, 255, 255, 255, 255, 255, 255, 255, 0], [255, 0, 255, 255, 255, 255, 255, 255, 255, 255], [255, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    C=[[255, 0, 0, 0, 0, 0, 255, 255, 255, 0], [0, 255, 255, 255, 255, 255, 0, 0, 0, 0], [0, 255, 255, 255, 255, 255, 0, 255, 255, 0], [0, 255, 255, 255, 255, 255, 0, 0, 0, 0], [255, 0, 0, 0, 0, 0, 255, 255, 255, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 0, 255], [255, 0, 255, 255, 255, 255, 255, 255, 255, 0], [255, 0, 255, 255, 255, 255, 255, 255, 255, 0], [255, 0, 255, 255, 255, 255, 255, 255, 255, 0], [255, 255, 0, 0, 0, 0, 0, 0, 0, 255]]
    a=[[255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    b=[[0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 255]]
    c=[[255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255]]
    d=[[0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255]]
    e=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    f=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255]]
    g=[[255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255]]
    h=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    i=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    j=[[255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255]]
    k=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    l=[[0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    m=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 255, 255, 0, 0, 0, 0], [0, 0, 0, 0, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 0, 0, 255, 255, 0, 0], [0, 0, 255, 255, 0, 0, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    n=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 0, 0, 255, 255, 0, 0], [0, 0, 255, 255, 0, 0, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    o=[[255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255]]
    p=[[0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 255, 255]]
    q=[[255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [0, 0, 255, 255, 255, 255, 255, 0, 0, 255], [255, 255, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 0, 0]]
    r=[[0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    s=[[255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255]]
    t=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255]]
    u=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    v=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 255, 255]]
    w=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 0, 0, 255, 255, 0, 0], [0, 0, 255, 255, 0, 0, 255, 255, 0, 0], [0, 0, 0, 0, 255, 255, 0, 0, 0, 0], [0, 0, 0, 0, 255, 255, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    x=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 255, 255, 0, 0, 255, 255], [255, 255, 0, 0, 255, 255, 0, 0, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 0, 0, 255, 255, 0, 0, 255, 255], [255, 255, 0, 0, 255, 255, 0, 0, 255, 255], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0]]
    y=[[0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [0, 0, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 0, 0, 255, 255, 0, 0, 255, 255], [255, 255, 0, 0, 255, 255, 0, 0, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255]]
    z=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 0, 0], [255, 255, 255, 255, 255, 255, 0, 0, 0, 0], [255, 255, 255, 255, 0, 0, 0, 0, 255, 255], [255, 255, 255, 255, 0, 0, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 255, 255, 255, 255], [255, 255, 0, 0, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


frase=['','feliz aniversario','happy birthday','hyeonyeong kim', 'ABC']
qts=20
tamanho = [len(f) for f in frase]
#print(tamanho)
img=np.ones((12*len(frase),11*max(tamanho)),dtype=np.uint8)
img=255*img
for k in range(len(frase)):
    for i in range(10*tamanho[k]):
        for j in range(11):
            #print(('pchar.'+frase[k][i//10]+'[{}%11][{}%10]'.format(i,j)))
            if frase[k][i//10]!=' ':img[12*k+j][11*(max(tamanho)//2-tamanho[k]//2)+i+i//10]=eval('pchar.'+frase[k][i//10]+'[{}][{}]'.format(j%11,i%10))
ct=0
print()
pixels=list( zip( list(np.where(img==0))[0],list(np.where(img==0))[1],[0 for i in range(len(list(np.where(img==0))[0]))] ) )
print(pixels)
pixels=random.sample(pixels,len(pixels))
print(pixels)
imgo=np.ones((12*len(frase),11*max(tamanho)),dtype=np.uint8)
imgo=255*imgo
nonalocated=[]
imgs=[]
for i in range(len(pixels)//qts):
    img=np.array(imgo)
    for j in range(qts):
        #print(pixels[0],pixels[1])
        nonalocated.append(pixels[qts*i+j])
    for k in range(len(nonalocated)):
        #print(nonalocated[k][2])
        if nonalocated[k][0]!=0:
            #print(nonalocated[k][2],nonalocated[k][1])
            nonalocated[k]=(nonalocated[k][0]-1,nonalocated[k][1],nonalocated[k][2]+1)
            img[nonalocated[k][2],nonalocated[k][1]]=not(img[nonalocated[k][2],nonalocated[k][1]]*255)
        if nonalocated[k][0]==0:
            imgo[nonalocated[k][2],nonalocated[k][1]]=0
    cv2.imshow('',img)
    imgs.append(img)
    cv2.waitKey(1)
img=imgo
for i in range(qts*(len(pixels)//qts),len(pixels)):
    nonalocated.append(pixels[i])
times=0
while(1):
    img=np.array(imgo)
    #print(img.shape)
    for k in range(len(nonalocated)):
        re=0
        #print(nonalocated[k][2])
        if nonalocated[k][0]!=0:
            #print(nonalocated[k][2],nonalocated[k][1])
            nonalocated[k]=(nonalocated[k][0]-1,nonalocated[k][1],nonalocated[k][2]+1)
            img[nonalocated[k][2],nonalocated[k][1]]=not(img[nonalocated[k][2],nonalocated[k][1]]*255)
            re=re+1
        if nonalocated[k][0]==0:
            imgo[nonalocated[k][2],nonalocated[k][1]]=not(img[nonalocated[k][2],nonalocated[k][1]]*255)
    cv2.imshow('',img)
    imgs.append(img)
    cv2.waitKey(1)
    if re==0: times=times+1
    if times==61: break
cv2.imshow('',img)
imgs.append(img)
cv2.waitKey(1)
cv2.imshow('',imgo)
cv2.waitKey(1)
writer = cv2.VideoWriter("output3.mp4", cv2.VideoWriter_fourcc(*"xvid"), 30,(4*11*max(tamanho),4*12*len(frase)))
for i in imgs: writer.write(cv2.resize(cv2.cvtColor(i,cv2.COLOR_GRAY2RGB), (4*11*max(tamanho),4*12*len(frase)), interpolation = cv2.INTER_AREA))
print((4*11*max(tamanho),4*12*len(frase)))
writer.release()