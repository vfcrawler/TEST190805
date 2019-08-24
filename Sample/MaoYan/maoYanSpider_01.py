import json
import re
import time

import requests

def get_one_page(url):
    res = requests.get(url)
    html = res.text
    return parse_one_page(html)

def parse_one_page(html):
    pattern = re.compile('<dd>.*?<i.*?>(.*?)</i>.*?'
                         '<a.*?title="(.*?)".*?>.*?'
                         '<img.*?src="(.*?)".*?/>.*?'
                         '<img.*?src="(.*?)".*?/>.*?'
                         '</a>.*?movie-item-info.*?'
                         '<p.*?star.*?>.*?主演：(.*?)</p>.*?'
                         '<p.*?releasetime.*?>.*?上映时间：(.*?)</p>.*?'
                         '<p.*?score.*?'
                         '<i.*?integer.*?>(.*?)</i>.*?'
                         '<i.*?fraction.*?>(.*?)</i>.*?'
                         '</p>.*?'
                         '</dd>',flags=re.S)

    ret = re.findall(pattern,html)
    for e in ret:
        rank = e[0]
        title = e[1]
        imgsrc = e[3]
        star = re.sub('\n|\s','',e[4],flags=re.S)
        releasetime = e[5]
        score = e[6]+e[7]

        yield {
            'rank':rank,
            'title':title,
            'imgsrc':imgsrc,
            'star':star,
            'releasetime':releasetime,
            'score':score
        }

def write_to_file(item):
    with open('MaoYan.txt','ab+') as f:
        f.write(bytes(json.dumps(item,ensure_ascii=False)+'\n',encoding='utf-8'))

def run(offset):
    base_url = 'https://maoyan.com/board/4?offset='
    url = base_url + str(offset)
    for e in get_one_page(url):
        print(json.dumps(e, ensure_ascii=False))
        write_to_file(e)

if __name__ == '__main__':

    # with open('MaoYan.txt','w+',encoding='utf-8') as f:
    #
    #     for i in range(0,10):
    #         base_url = 'https://maoyan.com/board/4?offset='
    #         offset = i * 10
    #         url = base_url+str(offset)
    #
    #         for e in get_one_page(url):
    #             f.write(json.dumps(e,ensure_ascii=False)+'\n')

    # with open('MaoYan.txt','wb+') as f:
    #     for i in range(0,10):
    #         base_url = 'https://maoyan.com/board/4?offset='
    #         offset = i * 10
    #         url = base_url+str(offset)
    #
    #         for e in get_one_page(url):
    #             print(json.dumps(e,ensure_ascii=False))
    #             f.write(bytes(json.dumps(e,ensure_ascii=False)+'\n',encoding='utf-8'))

    for i in range(0, 10):
        run(i*10)
        time.sleep(1)

