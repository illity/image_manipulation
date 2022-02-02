# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-03-03
#Version     : 1.0

import re
import random
moves = ['R','RR','RRR','L','LL','LLL','U','UU','UUU','D','DD','DDD','F','FF','FFF','B','BB','BBB']
UBL='W'; UBM='W'; UBR='W'; UTL='W'; UTM='W'; UTR='W'; UFL='W'; UFM='W'; UFR='W'
DFL='Y'; DFM='Y'; DFR='Y'; DTL='Y'; DTM='Y'; DTR='Y'; DBL='Y'; DBM='Y'; DBR='Y'
LUB='R'; LUT='R'; LUF='R'; LCB='R'; LCT='R'; LCF='R'; LDB='R'; LDT='R'; LDF='R'
RUF='O'; RUT='O'; RUB='O'; RCF='O'; RCT='O'; RCB='O'; RCF='O'; RCT='O'; RCB='O'
FUL='B'; FUM='B'; FUR='B'; FCL='B'; FCM='B'; FCR='B'; PDL='B'; FDM='B'; FDR='B'
BDL='G'; BDM='G'; BDL='G'; BCL='G'; BCM='G'; BCR='G'; BUL='B'; FUM='B'; BUR='B'
UP=UBL+UBM+UBR+UTL+UTM+UTR+UFL+UFM+UFR
LEFT=LUB+LUT+LUF+LCB+LCT+LCF+LDB+LDT+LDF
FRONT=FUL+FUM+FUR+FCL+FCM+FCR+PDL+FDM+FDR
UB=UBL+" "+UBM+" "+UBR
UT=UTL+" "+UTM+" "+UTR
UF=UFL+" "+UFM+" "+UFR
LU=LUB+" "+LUT+" "+LUF
LC=LCB+" "+LCT+" "+LDF
LD=LDB+" "+LDT+" "+LDF
s=" "
ts="\x1b[0,30,40m"
ts="\x1b[0,38,40m"
command4="FFF"
advn=1
circles = 0
commandstop = "no"
stime = 'first'
ndo = 0
wdo = 'n'
solve = 'no'
comando = 'no'
turnshow = 'yes'
stopsolve = 'y'
state = 'nothing'
advmode = 'off'
stopsequence = 'y'
tcircles = 0
while commandstop=='no':
    UP=UBL+UBM+UBR+UTL+UTM+UTR+UFL+UFM+UFR
    LEFT=LUB+LUT+LUF+LCB+LCT+LCF+LDB+LDT+LDF
    FRONT=FUL+FUM+FUR+FCL+FCM+FCR+PDL+FDM+FDR
    if cicles<0:
        command="show"
        turnshow="yes"
        tcicles=tcicles+1
        cicles=0
        print(str(tcicles)+'milhares')
        commandstop=input('Want stop?')
        if commandstop=="no"
            ask='no'
    if cicles>100000:
        tcicles=tcicles+1
        cicles=0
        print(str(tcicles)+'tenthousandcicles')
    if ask=='permitted' and ndo==0
        command = input('insira um comando')
        ask='no'
        asked='yes'
    if command == 'stop':
        ask='no'
        commandstop='yes'
        print('bye')
    if command == 'advanced':
        wdo=input('wdo')
        ndo=int(input('ndo'))
        ask='no'
        advmode='on'
        command='show'
    if asked=='yes':
        if command=?
            state=?


            elif wdo='R':
                nRUB=UBL; nUBL=LDB; nLDB=DBR; NBR=RUB;
            command='show'
            ?
        ndo=ndo-1
        wdo=wdoo
        cicles=cicles+1
    if ndo==0 and solve!='s' and state!='hand':
        advmode='off'
        ask='permitted'
    if command=='show' and turnshow!='no':
        exec('UBLs='+UBL+'+s+UBL+s')#p/ tudo