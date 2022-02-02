# -*- coding: utf-8 -*-
#Created By  : Illity
#Created Date: 2022-02-01
#Version     : 1.0

from glob import glob
import os

def menu(l):
    print('which one do you want to execute\n')
    for i, name in enumerate(l):
        print(f'{i+1} - {name}')
    x = input('')
    return int(x)-1

if __name__ == '__main__':
    l = glob('**\main.py')
    # l.remove('main.py')
    p = menu(l)
    print(f'\nCalling {l[p]}...')
    os.system(l[p])
    print('\nDone! Final result should be ready by now')