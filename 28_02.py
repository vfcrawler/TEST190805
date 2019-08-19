def str2int(s):
    num = 0
    for c in s:
        t = '%s*1'%c
        n = eval(t)
        num = num*10 + n
    return num

print(str2int('3344'))

