# mode='r'
def get_lines():
    with open('file.txt','r',encoding='utf-8') as f:
        for i in f:
            yield i

# mode='rb'
def get_lines1():
    with open('file.txt','rb') as f:
        for i in f:
            yield i


def get_lines2():
    with open('file.txt','r') as f:
        print(f.fileno())


if __name__ == '__main__':
    get_lines2()
