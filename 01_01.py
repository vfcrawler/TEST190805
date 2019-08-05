from mmap import mmap


def get_lines(fp):
    with open(fp,"rb+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0

        lists = enumerate(m)



        for i, char in enumerate(m):
            print(char)
            if char==b"\n":
                yield m[tmp:i+1].decode()
                tmp = i+1

if __name__=="__main__":
    for i in get_lines('file.txt'):
        pass