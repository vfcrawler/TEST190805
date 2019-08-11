"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
import os

def print_directory_contents(sPath):
    tmp = 0
    for s_child in os.listdir(sPath):
        if os.path.isdir(os.path.join(sPath,s_child)):
            print_directory_contents(os.path.join(sPath,s_child))
        else:
            print('FilePath:',os.path.join(sPath,s_child))
            tmp = tmp +1
    print(tmp)

if __name__ == '__main__':
    print_directory_contents('D:\\360极速浏览器下载')
