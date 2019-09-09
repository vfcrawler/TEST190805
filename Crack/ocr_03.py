import tesserocr
from PIL import Image

image = Image.open('code.jpg')
image = image.convert('L')
image.show()

image = Image.open('code.jpg')
image = image.convert('1')
image.show()


