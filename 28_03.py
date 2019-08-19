from functools import reduce

def str2int(s):
    ret = reduce(lambda num,c:num*10+(ord(c)-ord('0')),s,0)
    return ret

print(str2int('123'))

