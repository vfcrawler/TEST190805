from PIL import Image
import tesserocr
import requests

res = requests.get('http://my.cnki.net/Register/CheckCode.aspx')
print(res.content)
with open('code.jpg','wb+') as f:
    f.write(res.content)

image = Image.open('code.jpg')
image = image.convert('L')

thresold = 127
table = []

for i in range(256):
    if i<thresold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table,'1')
result = tesserocr.image_to_text(image)

print(result)