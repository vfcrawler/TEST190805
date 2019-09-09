from PIL import Image
import tesserocr

image = Image.open('code2.jpg')
result = tesserocr.image_to_text(image)

print(result)

