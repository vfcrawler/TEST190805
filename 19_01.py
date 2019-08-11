import os

def get_files(sPath,suffix):
    res = []
    for root,dirs,files in os.walk(sPath):
        # for dir in dirs:
        #     print('dir:',os.path.join(root,dir))
        for filename in files:
            if os.path.splitext(filename)[1] == suffix:
                res.append(os.path.join(root,filename))
    return res

if __name__ == '__main__':
    ret = get_files('F:\\BigDataTools','.pyc')
    print(ret)

