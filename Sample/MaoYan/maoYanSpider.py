import json
import re
import time
import requests
from requests.exceptions import RequestException

# 抓取单个链接的内容
def get_one_page(url):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException as e:
        return None

# 将抓取内容转化为字典迭代器
def parse_one_page(html):

    str_pattern = '<dd.*?' \
                  '<i.*?board-index.*?>(.*?)</i>.*?' \
                  '<a.*?title="(.*?)".*?' \
                  '<img.*?data-src="(.*?)".*?</a>.*?' \
                  'star.*?>(.*?)</p>.*?' \
                  'releasetime.*?>(.*?)</p>.*?' \
                  'integer.*?>(.*?)</i>.*?' \
                  'fraction.*?>(.*?)</i>.*?</dd>'

    pattern = re.compile(str_pattern,flags=re.S)

    items = re.findall(pattern,html)

    for item in items:

        rank = item[0]
        title = item[1]
        imgsrc = item[2]
        star = item[3].strip()[3:]
        releasetime = item[4].strip()[5:]
        score = item[5]+item[6]


        # print(rank,title,imgsrc,star,releasetime,score,sep='---')

        yield {
            'rank':rank,
            'title':title,
            'imgsrc': imgsrc,
            'star': star,
            'releasetime': releasetime,
            'score': score
        }

# 将字典类型的数据以文本的形式写入文件
def write_to_file(item):
    content = json.dumps(item,ensure_ascii=False)

    # 文本形式写入
    # with open('MaoYan.txt','a+',encoding='utf-8') as f:
    #     f.write(content+'\n')

    # 以字节流形式写入
    with open('MaoYan.txt','ab+') as f:
        f.write(bytes(content+'\n',encoding='utf-8'))

def run(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    items = parse_one_page(html)

    for item in items:
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        run(i*10)
        time.sleep(1)













