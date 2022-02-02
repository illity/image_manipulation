# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2021-04-30
#Version     : 1.0

f=open('mi.mcfunction','r').read()
c=f.split('\n')
i=0
for el in c:
    i=i+1
    open('mi{}.mcfunction'.format(int(i/65536)),'a').write(el+'\n')
#for j in range(4):
# open('fullfunction.mcfunction','a').write('function custom:example/serpico{}\n'.format(j))