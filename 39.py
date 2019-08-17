def multi():
    return [lambda x : i*x for i in range(4)]

# 可以写成以下方式
def multi1():
    ret = []
    for i in range(4):
        def fun1(x):
            return i*x
        ret.append(fun1)
    return ret

print('第1种方法返回：')
print([m(3) for m in multi()])

print('第2种方法返回：')
print([m(3) for m in multi1()])




