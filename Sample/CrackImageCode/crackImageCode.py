import requests
import tesserocr
from PIL import Image

# 知网为例，生成图形验证码的请求地址
generateCodeUrl = 'http://my.cnki.net/Register/CheckCode.aspx'

# 生成临时的文件名
filename = 'code.jpg'

res = requests.get(generateCodeUrl)
if res.status_code == 200:

    # 生成验证码图片
    with open(filename,'wb+') as f:
        f.write(res.content)

    # 灰度处理
    image = Image.open(filename)
    image = image.convert('L')

    # 二值化阈值处理
    thesold = 127
    table = []
    for i in range(256):
        if i<thesold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table,'1')

    # 转化文字
    result = tesserocr.image_to_text(image)
    print(result)
