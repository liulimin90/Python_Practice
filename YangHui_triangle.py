# -*- coding:utf-8 -*-
#用list方法产生杨辉三角

def triangle(max):
    L1=[1]
    yield L1
    L2=[1,1]
    n=1
    while n<max:
        yield L2
        n=n+1
        L1=L2[:]    #如果是用L1=L2，并不是把L2的值赋给L1，而是把L1指向L2，而是用L1=L2[:],则这是复制语句
        for i in range(1,n):
            L2[i]=L1[i-1]+L1[i]
        L2.append(1)

for t in triangle(10):
    print(t)

#way 2
def triangle1():
    L=[1]
    yield L
    L=[1,1]
    yield L
    while True:
        for i in range(len(L)-1,0,-1):
            L[i]=L[i-1]+L[i]
        L.append(1)
        yield L

n = 0
for t in triangle1():
    print(t)
    n = n + 1
    if n == 10:
        break
        