import tesserocr
from PIL import Image

# 灰度处理
image = Image.open('code.jpg')
image = image.convert('L')
image.show()

# 二值化处理
image = Image.open('code.jpg')
image = image.convert('1')
image.show()


