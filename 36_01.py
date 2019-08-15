def list_merge(l1,l2):
    tmp = []
    for l in l1:
        tmp.append(l)
    for l in l2:
        tmp.append(l)

    return tmp

if __name__ == '__main__':
    l1 = [2,3,4,6,1,21,0]
    l2 = [4,0,1,6,7]
    ret = list_merge(l1,l2)
    print(ret)

