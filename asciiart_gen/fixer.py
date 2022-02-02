# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2020-12-26
#Version     : 1.0
a = open('out.txt','r',encoding='utf-8').read()
b = ''
for ch in a:
    if ch!='\n':
        b=b+ch+ch
    else:
        b=b+ch
a = open('out2.txt','w',encoding='utf-8').write(b)
print(b)