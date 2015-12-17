#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#to move tower of Hanoi using recursive function
def move(n, a, b, c):
    if n==1:
        print("%s --> %s" %(a,c))
        return
    move(n-1,a,c,b)
    print('%s --> %s' %(a,c))
    move(n-1,b,a,c)
move(5, 'A', 'B', 'C')