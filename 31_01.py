import re

def countwords(filepath):

    diswords={}
    with open(filepath,'r+') as f:
        for line in f:
            # 将所有非字母数字下划线字符转化为空字符串
            line = re.sub('\W+',' ',line)
            # 按空格分隔行
            lineone = line.split()
            for keyone in lineone:
                if not diswords.get(keyone):
                    diswords[keyone] = 1
                else:
                    diswords[keyone] += 1
    # 获取前10(单词:频次) 的字典列表
    num_top10 = sorted(diswords.items(),key=lambda x:x[1],reverse=True)[:10]
    # 获取前10单词的字典列表
    num_top10 = [x[0] for x in num_top10]

    return num_top10

if __name__ == '__main__':
    print(countwords('31_01.txt'))

    


