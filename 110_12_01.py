
f = open('1.txt','wb+')
try:
    f.write(b'sadfsa')
except Exception as e:
    pass
finally:
    f.close()



