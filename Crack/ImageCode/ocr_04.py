from PIL import Image

image = Image.open('code.jpg')
# 灰度处理
image = image.convert('L')
# 指定二值化的阈值
thresold = 80
table = []
for i in range(256):
    if i<thresold:
        table.append(0)
    else:
        table.append(1)
image.point(table,'1')

image.show()
