import requests

res = requests.get('https://github.com/favicon.ico',verify=False)

print(type(res.content))
print(res.content)

with open('favicon.ico','wb+') as f:
    f.write(res.content)



