#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__="Limin Liu"

'''
Using pillow library to filter image and resize image
'''

from PIL import Image,ImageFilter

im=Image.open('test.jpg')   # open image


im2=im.filter(ImageFilter.BLUR)   # filter image
im2.save('blur.jpg','jpeg')


w,h=im.size
print('Original image size: %sx%s' %(w,h))
im.thumbnail((w//2,h//2))    #resize image as half of source image
print('Resize image to: %sx%s' %(w//2,h//2))
im.save('thumbnail.jpg','jpeg')