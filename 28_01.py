def str2int(s):
    num = 0
    for c in s:
        num = num * 10 + (ord(c)-ord('0'))
    return num

if __name__ == '__main__':
    print(str2int('445566'))
