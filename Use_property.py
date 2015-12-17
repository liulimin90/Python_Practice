#!/usr/bin/env python3
#* -*- coding: utf-8 -*-

'''
利用@property给一个Screen对象加上width和height属性，
以及一个只读属性resolution
'''

__author__="Limin Liu"

class Screen(object):
    __slots__=('_width','_height','_resolution')

    @property
    def width(self):
        return self._width   #self.width实际上是调方法，而不是变量，因此需不同的变量名区分方法和属性

    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._width*self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution