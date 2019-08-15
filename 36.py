def list_merge(l1,l2):
    tmp = []
    while len(l1)>0:
        tmp.append(l1[0])
        del(l1[0])
    while len(l2)>0:
        tmp.append(l2[0])
        del(l2[0])

    return tmp

if __name__ == '__main__':
    l1 = [2,3,4,6,1,21,0]
    l2 = [4,0,1,6,7]
    ret = list_merge(l1,l2)
    print(ret)



