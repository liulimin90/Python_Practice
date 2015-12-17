# -*- coding:utf-8 -*-
#calcuate prime number using filter

def main():
    for n in prime_number():
        if n < 100:
            print(n)

def prime_number():
    yield 2
    next_prim = _num_bigger_than_3()
    while True:
        n = next(next_prim)
        yield n
        next_prim = filter(_not_divisible(n),next_prim)

def _num_bigger_than_3():
    n = 3
    while True:
        yield n
        n = n + 2

def _not_divisible(n):
    return lambda x: x % n >0

if __name__ == '__main__':
    main()
# 在cmd 中直接运行.py文件,则__name__的值是'__main__';
# 而在import 一个.py文件后,__name__的值就不是'__main__'了;
# 从而用if __name__ == '__main__'来判断是否是在直接运行该.py文件