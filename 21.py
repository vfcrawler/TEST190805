a = [1,2,3,4,5,6,7,8]
print('原列表a ',a)
print('新列表a[:] ',a[:])

print('原列表a的id ',id(a))
print('新列表a[:]的id ',id(a[:]))

for i in a[:]:      # 遍历在新列表
    if i>5:
        pass
    else:
        a.remove(i) # 删除在原列表

print('----------------')

print('原列表a的id ',id(a))
print('新列表a[:]的id ',id(a[:]))




