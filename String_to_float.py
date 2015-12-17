# -*- coding:utf-8 -*-

from functools import reduce

def str2float(s):
    return(reduce(lambda x,y:x*10+y,map(int,''.join(s.split('.'))))\
        /(10**(len(s)-s.find('.')-1)))

print('str2float(\'123.456\')=',str2float('123.456'))