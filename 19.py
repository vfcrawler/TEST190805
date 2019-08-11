import os

def get_files(sPath,suffix,ls):
    for os_path in os.listdir(sPath):
        full_path = os.path.join(sPath,os_path)
        if os.path.isdir(full_path):
            get_files(full_path,suffix,ls)
        else:
            if os.path.splitext(full_path)[1] == suffix:
                res.append(full_path)


if __name__ == '__main__':
    res = []
    get_files(r'F:\BigDataTools','.gz',res)
    print(res)




#
# str_path = '‪F:\BigDataTools\CDH安装包\flume-ng-1.5.0-cdh5.3.6.tar.gz'
#
# print(os.path.splitext(str_path)[1])


