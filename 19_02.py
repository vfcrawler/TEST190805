from glob import iglob

def get_files(sPath,suffix):
    res = []
    # ** 代表所有
    for file in iglob(f'{sPath}/**/*{suffix}',recursive=True):
        res.append(file)
    return res

if __name__ == '__main__':
    ret = get_files(r'F:\BigDataTools','.pyc')
    print(ret)



