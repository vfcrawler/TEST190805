from mmap import mmap

def get_lines(fp):

    with open(fp,'rb+') as f:
        m = mmap(f.fileno(),0)
        maxsize = m.__len__()
        tmp = 0
        print(type(enumerate(m)))
        for i,char in enumerate(m):
            if i==maxsize-1 or char == b'\n':
                yield m[tmp:i+1].decode('utf-8')
                tmp = i+1

if __name__ == '__main__':
    for line in get_lines('file.txt'):
        print(line)

