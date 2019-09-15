# -*- coding:utf-8 -*-
from PIL import Image

box = (19,322.01,24.89,513)

img = Image.open('full.png')

img1 = img.crop((box))

img1.save('full_01.png')









