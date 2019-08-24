import urllib.parse

query = 'name=germey&age=22'

print(urllib.parse.parse_qs(query))
