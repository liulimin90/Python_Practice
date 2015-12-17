# -*- coding: utf-8 -*-
# Change the fist letter of a name to uppercase
# Using map()

from collections import Iterable

# defination 1
def normalize (name):
    if not isinstance(name,str):
        raise TypeError('Bad operand type')
    if not isinstance(name,Iterable):
        raise TypeError('Not iterable')
    name_out=''  # 由于str不是可变的，因此不能直接用name[n]=name[n].upper()来赋值
    n=0
    for s in name:
        if n == 0:
            name_out=name_out+s.upper()
        else:
            name_out=name_out+s.lower()
        n=n+1
    return name_out

# defination 2
# def normalize(name):
#     if not isinstance(name,str):
#         raise TypeError('Bad operand type')
#     if not isinstance(name,Iterable):
#         raise TypeError('Not iterable')
#     return name[0].upper()+name[1:].lower()

# defination 3
# def normalize(name):
#     if not isinstance(name,str):
#         raise TypeError('Bad operand type')
#     if not isinstance(name,Iterable):
#         raise TypeError('Not iterable')
#     return name.title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)