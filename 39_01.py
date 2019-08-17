def multi1():
    return [lambda x : i*x for i in range(4)]

def multi2():
    ret = []
    for i in range(4):
        def fun(x):
            return i*x
        ret.append(fun)
    return ret

print('第1种方法返回：')
for m in multi1():
    print(m(2))
print('第2种方法返回：')
for m in multi2():
    print(m(2))





