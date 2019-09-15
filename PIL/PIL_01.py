# -*-coding:utf-8-*-

from PIL import Image

im = Image.open('01.png')
im.save('02.png')



im1 = im.crop((1,2,3,4))
im1.save('03.png')



