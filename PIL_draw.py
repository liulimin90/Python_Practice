#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__="Limin Liu"

'''
Generate image verification
'''

from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

# produce random character
def rndChar():
    return chr(random.randint(65,90))

# random color
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

height = 60
width = height * 4
image = Image.new('RGB', (width,height), (255,255,255))
font = ImageFont.truetype('C:\Windows.old\WINDOWS\Fonts\Arial.ttf',36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

for t in range(4):
    draw.text((60*t+10,10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)

image.save('code.jpg','jpeg')