# -*- coding:utf-8 -*-
# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

import functools

def log(*arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            func(*args, **kw)
            print('end call')
        return wrapper
    return decorator

@log()
def now():
    print('2015.11.19')

now()