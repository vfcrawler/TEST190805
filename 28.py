def str2int(s):
    num = 0
    for c in s:
        for j in range(0,10):
            if c == str(j):
                num = num*10 + j
    return num

print(str2int('123123'))
