#方法1.使用Set集合去重
def distFunc1(ls):
    ret = list(set(ls))
    return ret

#方法2.将一个列表的数据取出放到另一个列表中，中间作判断
def distFunc2(ls):
    ls_new = []
    for i in ls:
        if i not in ls_new:
            ls_new.append(i)
    return ls_new

#方法3.使用字典
def distFunc3(ls):
    dic = {}
    dic = dic.fromkeys(ls)
    ret = list(dic.keys())
    return ret

if __name__ == '__main__':
    ls = [1,2,3,4,5,55,5,5,6,6]
    print(distFunc1(ls))
    print(distFunc2(ls))
    print(distFunc3(ls))



