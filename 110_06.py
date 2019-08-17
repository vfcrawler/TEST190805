
alist = [1,2,3,4,5,6,1,2,3,4,5]
slist = set(alist)
print(slist)

# 方法1 列表推导式
ret = [x for x in slist]
print(ret)

# 方法2 直接转化
print(list(slist))




