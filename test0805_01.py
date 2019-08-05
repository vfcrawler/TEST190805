def createfile():
    try:
        with open('file.txt','wb+') as f:
            f.write(b'ceshiwenjia')
    except Exception as e:
        print(e)
    finally:
        with open('file.txt','r+') as f:
            s = f.readlines()
            print(s)



if __name__ == '__main__':
    for li in [1,3,5,56,6,66]:
        print(li)


