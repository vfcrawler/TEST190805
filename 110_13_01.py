# 列表[1,2,3,4,5],
# 请使用map()函数输出[1,4,9,16,25]，
# 并使用列表推导式提取出大于10的数，最终输出[16,25]

alist = [1,2,3,4,5]

amap = map(lambda x:x**2,alist)

ret = [x for x in amap if x>10]

print(ret)



