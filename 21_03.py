a=[1,2,3,4,5,6,7,8]

print(id(a))
for i in range(len(a)-1,-1,-1):
    if a[i]>5:
        pass
    else:
        a.remove(a[i])
print(id(a))
print('---------------')
print(a)


