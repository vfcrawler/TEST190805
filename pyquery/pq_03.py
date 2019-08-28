from pyquery import PyQuery as pq
import requests

doc = pq(requests.get('https://www.cuiqingcai.com').text)

print(doc('title'))
