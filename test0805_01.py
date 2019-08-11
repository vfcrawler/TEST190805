def get_line(fp):
    with open(fp,'rb+') as f:
        return f.readlines()

if __name__ == '__main__':
    print(type(get_line('file.txt')))
